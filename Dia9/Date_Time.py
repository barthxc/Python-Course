from datetime import datetime
#almacenar, y uso de horas y fechas

#mi_hora = datetime.time(17,35)
#print(mi_hora.hour)

#mi_fecha = datetime.date(2025,10,17)
#print(mi_fecha)

#mi_fecha = datetime(2025,5,15,22,10,15,2500)
#mi_fecha = mi_fecha.replace(month = 11)
#print(mi_fecha)

despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022,10,5,23,45)

vigilia = duerme - despierta
print(vigilia)


hoy = datetime.today().minute
print("yee")
print(hoy)


