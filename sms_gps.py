import android
from time import sleep

droid = android.Android()
droid.startLocating()
sleep(15)
latitud = droid.readLocation().result["network"]["latitude"]
longitud = droid.readLocation().result["network"]["longitude"]
droid.stopLocating()

num = droid.dialogGetInput("Destinatario","Numero Telefonico: ")
msg = "Prueba de SL4A python desde Android. Ubicacion en http://maps.google.com/maps?q=%s,%s"  % (latitud,longitud)
droid.smsSend(num.result,msg)