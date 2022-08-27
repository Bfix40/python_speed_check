dis = int(input("distancia recorrida en metros: "))
min = int(input("ingrese la cantidad de minutos: "))
seg = int(input("ingrese la cantidad de segundos: "))
cen = int(input("ingrese la cantidad de centesimas: "))

vkm = ((dis/((min*60)+seg+(cen/100)))*3600)/1000

print("Tu velocidad es de ", vkm, "Km/h")


def current_speed():
    if (vkm >= 100):
        print("Slow down")
    elif (vkm == 80):
        print("continue")
    else:
        print("Speed up")


current_speed()
