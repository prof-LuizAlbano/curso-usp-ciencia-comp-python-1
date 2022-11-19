segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
total_segs = total_segs % 86400
horas = total_segs // 3600
total_segs = total_segs % 3600
minutos = total_segs // 60
total_segs = total_segs % 60

print(dias, "dias", horas, "horas,", minutos, "minutos e", total_segs, "segundos.")