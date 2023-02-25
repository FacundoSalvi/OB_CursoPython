import datetime

hora_actual = datetime.datetime.now()
hora = hora_actual.hour
tiempo_restante = 19 - hora
if hora >= 19:
        print("son las ", hora_actual, "ya se acabó el día, es hora de ir a casa")
else:
        print("todavìa no son las 7","faltan ", tiempo_restante,  "horas")




