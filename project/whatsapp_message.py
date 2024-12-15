# Instalar esto con el siguiente comando "pip install pywhatkit"
import pywhatkit as kit
import datetime

def send_message(number):
    mensaje = "Hola, informacion registrada"
    horaDeEnvio = datetime.datetime.now() + datetime.timedelta(minutes=1)

    kit.sendwhatmsg(number, mensaje, horaDeEnvio.hour, horaDeEnvio.minute, wait_time=15)
