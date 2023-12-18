# Archivo: mi_programa.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def main():
    num1 = 5
    num2 = 2 
    resultado = suma(num1, num2)
    print(f"La suma es: {resultado}")

    resultado_resta = resta(num1, num2)
    print(f"La resta es: {resultado_resta}")

if __name__ == "__main__":
    main()
