import magic
import pandas as pd
import scipy
import scipy.stats
import pyssdeep
import sys
import os

class Watcher:
    def __init__(self, filename):
        path = r'config.txt'
        with open(path, 'r') as reader:
            directory = reader.readline().split(':')[1].strip()
            self.directory=directory.replace("\\", "/")
            backup = reader.readline().split(':')[1].strip()
            self.backup = backup.replace("\\", "/")
            user = reader.readline().split(':')[1].strip()
        self.monitor = directory + filename

        self.compared = backup + filename
        self.user = user



    def SameType(self):
        return magic.from_file(self.monitor) == magic.from_file(self.compared) or magic.from_file(self.monitor,
                                                                                                  mime=True) == magic.from_file(
            self.compared, mime=True)

    def SimilarityMeasurement(self):
        a = pyssdeep.get_hash_file(self.monitor)
        b = pyssdeep.get_hash_file(self.compared)
        return pyssdeep.compare(a, b) <= 1

    def ShannonEntropy(self):
        path = self.monitor
        bytes = []
        with open(path, 'rb') as reader:
            byte = reader.readline()
            bytes.append(byte)
            while byte != b'':
                byte = reader.readline()
                bytes.append(byte)

        serie = pd.Series(bytes)
        counts = serie.value_counts()
        entropy = scipy.stats.entropy(counts)
        return entropy <= 1.0


def main(file_name):
    count = 0
    dc = Watcher(file_name)
    if ~dc.SameType():
        count += 1
    if dc.SimilarityMeasurement():
        count += 1
    if dc.ShannonEntropy():
        count += 1
    if count >= 2:
        os.system('ps -u '+dc.user+' > LogProcesos.txt')
        os.system('fuser -c -k '+ dc.directory)


if __name__ == '__main__':
    main(sys.argv[1])
