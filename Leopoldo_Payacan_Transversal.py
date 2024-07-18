import random
import math 

empleados = ["Juan Pérez", "María García", "Pedro Soto", "Isabel Gómez", "Miguel Sánchez", "Sofía Rodríguez", "Luis Hernández", "Ana López", "Carlos Díaz", "Daniela Morales"]

sueldos = [random.randint(300000, 2500000) for _ in range(10)]

def tabla_sueldos(empleados, sueldos):
    print("Sueldos menores a $800.000")
    print(f"TOTAL: {sum(1 for sueldo in sueldos if sueldo < 800000)}")
    print("Nombre empleado Sueldo")
    for i in range(len(sueldos)):
        if sueldos[i] < 800000:
            print(f"{empleados[i]} ${sueldos[i]}")

    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {sum(1 for sueldo in sueldos if 800000 <= sueldo < 2000000)}")
    print("Nombre empleado Sueldo")
    for i in range(len(sueldos)):
        if 800000 <= sueldos[i] < 2000000:
            print(f"{empleados[i]} ${sueldos[i]}")

    print("\nSueldo superior a $2.000.000")
    print(f"TOTAL: {sum(1 for sueldo in sueldos if sueldo >= 2000000)}")
    print("Nombre empleado Sueldo")
    for i in range(len(sueldos)):
        if sueldos[i] >= 2000000:
            print(f"{empleados[i]} ${sueldos[i]}")

    print(f"\nTOTAL SUELDOS: ${sum(sueldos)}")

def estadisticas_sueldo(sueldos):
    
    sueldo_mas_alto = max(sueldos)
    print(f"Sueldo más alto: ${sueldo_mas_alto}")

    
    lowest_wage = min(sueldos)
    print(f"Sueldo más bajo: ${lowest_wage}")

    
    average_wages = sum(sueldos) / len(sueldos)
    print(f"Promedio de sueldos: ${int(average_wages)}")

    
    l_sueldos = [math.log(sueldo) for sueldo in sueldos]
    media_log = sum(l_sueldos) / len(l_sueldos)
    media_geometrica = math.exp(media_log)
    print(f"Media geométrica: ${int(media_geometrica)}")

def reporteSueldo(empl, sueldos):
    print("Reporte sueldo:")
    print("Nombre empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido")
    with open("reporteSueldo.csv", "w") as csvfile:
        csvfile.write("Nombre empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido\n")
        for i in range(len(sueldos)):
            Base = sueldos[i]
            descsalu = Base * 0.07
            descuafp = Base * 0.12
            sueliqui = Base - descsalu - descuafp
            print(f"{empl[i]}, ${Base}, ${int(descsalu)}, ${int(descuafp)}, ${int(sueliqui)}")
            csvfile.write(f"{empl[i]}, ${Base}, ${int(descsalu)}, ${int(descuafp)}, ${int(sueliqui)}\n")

def menu():
    verdadero = True
    while verdadero:
        print("\n===MENU PRINCIPAL===")
        print("1. Sueldos al Azar")
        print("2. Clasificar")
        print("3. Estadísticas.")
        print("4. Reporte")
        print("5. Salir")
        opcion = input("Seleccione: ")
    
    menu()