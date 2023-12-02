#Conversor de unidades

print("--CONVERSOR DE UNIDADES--")

#Funciones de masa
def kilos_a_gramos(n1):
    return n1 * 1000

def gramos_a_kilos(n1):
    return n1 / 1000

#Funciones de longitud
def kilometros_a_metros(n1):
    return n1 * 1000

def metros_a_kilometros(n1):
    return n1 / 1000

def centimetros_a_metros(n1):
    return n1 / 100

def metros_a_centimetros(n1):
    return n1 * 100

#Funciones de volumen
def litros_a_mililitros(n1):
    return n1 * 1000

def mililitros_a_litros(n1):
    return n1 / 1000

#Funciones de temperatura
def fahrenheit_a_celcius(n1):
    return (n1 - 32) * 5/9

def celcius_a_fahrenheit(n1):
    return (n1 * 9/5) + 32


#Funciones de tiempo
def segundos_a_minutos(n1):
    return n1 / 60

def minutos_a_segundos(n1):
    return n1 * 60

def minutos_a_horas(n1):
    return n1 / 60

def horas_a_minutos(n1):
    return n1 * 60

def horas_a_segundos(n1):
    return n1 * 3600

def segundos_a_horas(n1):
    return n1 / 3600

#Funciones de velocidad
def kilometroshora_a_metrossegundo(n1):
    return (n1*1000)/3600
 
def metrossegundo_a_kilometroshora(n1):
    return n1*3.6

#Funciones de moneda
def mxn_a_dolar(n1):
    return n1 / 17.19

def dolar_a_mxn(n1):
    return n1 * 17.19

def mxn_a_euro(n1):
    return n1 / 18.71

def euro_a_mxn(n1):
    return n1 * 18.71

def dolar_a_euro(n1):
    return n1 * 0.92

def euro_a_dolar(n1):
    return n1 * 1.09

while True:
    print("Que unidades te gustaria convertir?")
    print("1.- Peso/Masa")
    print("2.- Longitud")
    print("3.- Volumen")
    print("4.- Temperatura")
    print("5.- Tiempo")
    print("6.- Velocidad")
    print("7.- Moneda")
    print("8.- Salir")
    
    opcion = input("Digite una opción:\n")
    match(opcion):
        case "1":
            print("----Eligió convertir unidades de Peso/Masa----")
            print("1.- Kilos - Gramos")
            print("2.- Gramos - Kilos")
            opcion_masa = input("Digite una opcion:\n")

            while True:
                match(opcion_masa):
                    case "1":
                        print("----Eligió convertir Kilos a Gramos----")
                        break

                    case "2":
                        print("----Eligió convertir Gramos a Kilos----")
                        break

                    case _:
                        print("Opción no valida, intentelo de nuevo")
                        print("----Eligió convertir unidades de Peso/Masa----")
                        print("1.- Kilos - Gramos")
                        print("2.- Gramos - Kilos")
                        opcion_masa = input("Digite una opcion:\n")
        case "2":
            print("----Eligió convertir unidades de Longitud---")
            print("1.- Kilometros - Metros")
            print("2.- Metros - Kilometros")
            print("3.- Centimetros - Metros")
            print("4.- Metros - Centimetros")
            opcion_longitud = input("Digite una opcion:\n")

            while True:
                match(opcion_longitud):
                    case "1":
                        print("----Eligió convertir Kilometros a Metros")
                        break
                    
                    case "2":
                        print("----Eligió convertir Metros a Kilometros")
                        break

                    case "3":
                        print("----Eligió convertir Centimetros a Metros")
                        break

                    case "4":
                        print("----Eligió convertir Metros a Centimetros")
                        break

                    case _:
                        print("Opción no valida, intentelo de nuevo")
                        print("----Eligió convertir unidades de Longitud---")
                        print("1.- Kilometros - Metros")
                        print("2.- Metros - Kilometros")
                        print("3.- Centimetros - Metros")
                        print("4.- Metros - Centimetros")
                        opcion_longitud = input("Digite una opcion:\n")
        case "3":
            print("----Eligió convertir unidades de Volumen----")
            print("1.- Litros - Mililitros")
            print("2.- Mililitros - litros")
            opcion_volumen = input("Digite una opcion:\n")

            while True:
                match(opcion_volumen):
                    case "1":
                        print("----Eligio convertir Litros a Mililitros")
                        break

                    case "2":
                        print("----Eligió convertir Mililitros a Litros")
                        break

                    case _:
                        print("Opción no valida, intentelo de nuevo")
                        print("----Eligió convertir unidades de Volumen----")
                        print("1.- Litros - Mililitros")
                        print("2.- Mililitros - litros")
                        opcion_volumen = input("Digite una opcion:\n")  
        case "4":
            print("----Eligió convertir unidades de Temperatura----")
            print("1.- Celsius - Fahrenheit")
            print("2.- Fahrenheit - Celsius")
            opcion_temperatura = input("Digite una opción:\n")

            while True:
                match(opcion_temperatura):
                    case "1":
                        print("----Eligió convertir Celsius a Fahrenheit----")
                        break

                    case "2":
                        print("----Eligió convertir Fahrenheit a Celsius")
                        break

                    case _:
                        print("Opción no valida, intentelo de nuevo")
                        print("----Eligió convertir unidades de Temperatura----")
                        print("1.- Celsius - Fahrenheit")
                        print("2.- Fahrenheit - Celsius")
                        opcion_temperatura = input("Digite una opción:\n")
        case "5":
            print("----Eligió convertir unidades de Tiempo----")
            print("1.- Segundos - Minutos")
            print("2.- Minutos - Segundos")
            print("3.- Minutos - Horas")
            print("4.- Horas - Minutos")
            print("5.- Horas - Segundos")
            print("6.- Segundos - Horas")
            opcion_tiempo = input("Digite una opcion:\n")

            while True:
                match(opcion_tiempo):
                    case "1":
                        print("----Eligió convertir Segundos a Minutos----")
                        break

                    case "2":
                        print("----Eligió convertir Minutos a Segundos----")
                        break

                    case "3":
                        print("----Eligió convertir Minutos a Horas----")
                        break

                    case "4":
                        print("----Eligió convertir Horas a Minutos----")
                        break

                    case "5":
                        print("----Eligió convertir Horas a Segundos----")
                        break

                    case "6":
                        print("----Eligió convertir Segundos a Horas----")
                        break

                    case _:
                        print("Opción no valida, intentelo de nuevo")
                        print("----Eligió convertir unidades de Tiempo----")
                        print("1.- Segundos - Minutos")
                        print("2.- Minutos - Segundos")
                        print("3.- Minutos - Horas")
                        print("4.- Horas - Minutos")
                        print("5.- Horas - Segundos")
                        print("6.- Segundos - Horas")
                        opcion_tiempo = input("Digite una opcion:\n")
        case "6":
            print("----Eligió convertir unidades de Velocidad----")
            print("1.- Kilometros/h - Metros/s")
            print("2.- Metros/s - Kilometros/h")
            opcion_velocidad = input("Digite una opción:\n")

            while True:
                match(opcion_velocidad):
                    case "1":
                        print("----Eligió convertir Kilometros/h a Metros/s----")
                        break

                    case "2":
                        print("----Eligió convertir  Metros/s a Kilometros/h")
                        break

                    case _:
                        print("Opción no valida, intentelo de nuevo")
                        print("----Eligió convertir unidades de Velocidad----")
                        print("1.- Kilometros/h - Metros/s")
                        print("2.- Metros/s - Kilometros/h")
                        opcion_velocidad = input("Digite una opción:\n")
        case "7":
            print("----Eligió convertir unidades de Moneda----")
            print("1.- MXN - Dolar")
            print("2.- Dolar - MXN")
            print("3.- MXN - Euro")
            print("4.- Euro - MXN")
            print("5.- Dolar - Euro")
            print("6.- Euro - Dolar")
            opcion_moneda = input("Digite una opción:\n")

            while True:
                match(opcion_moneda):
                    case "1":
                        print("----Eligió convertir MXN a Dolar----")
                        break

                    case "2":
                        print("----Eligió convertir Dolar a MXN----")
                        break

                    case "3":
                        print("----Eligió convertir MXN a Euro----")
                        break

                    case "4":
                        print("----Eligió convertir Euro a MXN----")
                        break

                    case "5":
                        print("----Eligió convertir Dolar a Euro----")
                        break
                    
                    case "6":
                        print("----Eligió convertir Euro a Dolar----")
                        break

                    case _:
                        print("Opción no valida, intentelo de nuevo")
                        print("----Eligió convertir unidades de Moneda----")
                        print("1.- MXN - Dolar")
                        print("2.- Dolar - MXN")
                        print("3.- MXN - Euro")
                        print("4.- Euro - MXN")
                        print("5.- Dolar - Euro")
                        print("6.- Euro - Dolar")
                        opcion_moneda = input("Digite una opción:\n")
        case "8":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida, vuelva a intentarlo\n")
            continue
    
    numero_1 = float(input("Digite el numero que le gustaría convertir:\n"))

    if opcion == "1":
        match(opcion_masa):
            case "1":
                resultado = kilos_a_gramos(numero_1)
                print(f"{numero_1} kilos son {resultado} gramos.\n")

            case "2":
                resultado = gramos_a_kilos(numero_1)
                print(f"{numero_1} gramos son {resultado} kilos.\n")
    
    elif opcion == "2":
        match(opcion_longitud):
            case "1":
                resultado = kilometros_a_metros(numero_1)
                print(f"{numero_1} kilometros son {resultado} metros.\n")

            case "2":
                resultado = metros_a_kilometros(numero_1)
                print(f"{numero_1} metros son {resultado} kilometros\n")

            case "3":
                resultado = centimetros_a_metros(numero_1)
                print(f"{numero_1} centimetros son {resultado} metros\n")

            case "4":
                resultado = metros_a_centimetros(numero_1)
                print(f"{numero_1} metros son {resultado} centimetros\n")
    
    elif opcion == "3":
        match(opcion_volumen):
            case "1":
                resultado = litros_a_mililitros(numero_1)
                print(f"{numero_1} litros son {resultado} mililitros\n")
            
            case "2":
                resultado = mililitros_a_litros(numero_1)
                print(f"{numero_1} mililitros son {resultado} litros\n")

    elif opcion == "4":
        match(opcion_temperatura):
            case "1":
                resultado = celcius_a_fahrenheit(numero_1)
                print(f"{numero_1} grados celsius son {resultado} grados fahrenheit\n")
            
            case "2":
                resultado = fahrenheit_a_celcius(numero_1)
                print(f"{numero_1} grados fahrenheit son {resultado} grados celsius\n")

    elif opcion == "5":
        match(opcion_tiempo):
            case "1":
                resultado = segundos_a_minutos(numero_1)
                print(f"{numero_1} segundos son {resultado} minutos\n")

            case "2":
                resultado = minutos_a_segundos(numero_1)
                print(f"{numero_1} minutos son {resultado} segundos\n")

            case "3":
                resultado = minutos_a_horas(numero_1)
                print(f"{numero_1} minutos son {resultado} horas\n")

            case "4":
                resultado = horas_a_minutos(numero_1)
                print(f"{numero_1} horas son {resultado} minutos\n")
            
            case "5":
                resultado = horas_a_segundos(numero_1)
                print(f"{numero_1} horas son {resultado} segundos\n")
            
            case "6":
                resultado = segundos_a_horas(numero_1)
                print(f"{numero_1} segundos son {resultado} horas\n")

    elif opcion == "6":
        match(opcion_velocidad):
            case "1":
                resultado = kilometroshora_a_metrossegundo(numero_1)
                print(f"{numero_1} kilometros/h son {resultado} metros/s")
            
            case "2":
                resultado = metrossegundo_a_kilometroshora(numero_1)
                print(f"{numero_1} metros/s son {resultado} kilometros/h")
    
    elif opcion == "7":
        match(opcion_moneda):
            case "1":
                resultado = mxn_a_dolar(numero_1)
                print(f"{numero_1} pesos mxn son {resultado} dolares")

            case "2":
                resultado = dolar_a_mxn(numero_1)
                print(f"{numero_1} dolares son {resultado} pesos mxn")

            case "3":
                resultado = mxn_a_euro(numero_1)
                print(f"{numero_1} pesos mxn son {resultado} euros")
            
            case "4":
                resultado = euro_a_mxn(numero_1)
                print(f"{numero_1} euros son {resultado} pesos mxn")

            case "5":
                resultado = dolar_a_euro(numero_1)
                print(f"{numero_1} dolares son {resultado} euros")

            case "6":
                resultado = euro_a_dolar(numero_1)
                print(f"{numero_1} euros son {resultado} dolares")
