#Primer Ejemplo de uso de python para Android.
#Envio de ubicacion gps por sms.

import android
from time import sleep

#Se crea un objeto con el que se manipulara la api de Android.
droid = android.Android()

#Se comienza el proceso de localizacion gps
droid.startLocating()
sleep(15)
latitud = droid.readLocation().result["network"]["latitude"]
longitud = droid.readLocation().result["network"]["longitude"]
droid.stopLocating()

#Se mostrara un dialogo solicitando el numero destino del mensaje 
#con el metodo dialogGetInput("Titulo del dialogo","mensaje del input")
num = droid.dialogGetInput("Destinatario","Numero Telefonico: ")
msg = "Prueba de SL4A python desde Android. Ubicacion en http://maps.google.com/maps?q=%s,%s"  % (latitud,longitud)
#Metodo smsSend(number,mesage) enviara el mensaje al destino. 
#aunque nombre la variable num, se debe de pedir .result para obtener el texto del dialogo.
droid.smsSend(num.result,msg)