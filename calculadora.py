def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida proporciona un número distinto")
    return a / b

def funcion_nueva_con_bug():
    # Este bug haría fallar la aplicación en producción
    return 1 / 0
