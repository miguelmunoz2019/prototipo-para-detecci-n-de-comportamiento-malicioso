# prototipo-para-detecci-n-de-comportamiento-malicioso
/////Como configurar////////
En el archivo config.txt se debe poner frente a directory el path perteneciente al directorio que será monitoreado
en backup, se escribe el path del directorio donde se almacenara el backup de la informacion monitoreada, 
finalmente en user se debe escribir el usuario sobre el que se está ejecutando el monitoreo.
////Despues de deteccion///////
En caso que se detecte el comportamiento Ransomware, se detendrán todos los procesos del usuario,
la infomacion de los procesos detenidos estará almacenada en LogProcesos.txt, donde se podrá buscar
el proceso que demostró ese comportamiento. 