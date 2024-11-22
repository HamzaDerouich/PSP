import threading

def CalcularAreaTriangulos(b,a):
    return ( (a * b ) / 2 )

def CalcularAreaRectangulo(b,a):
    return a * b

t1 = threading.Thread(CalcularAreaTriangulos(10,12))
t2 = threading.Thread(CalcularAreaRectangulo(5,1))
r1 = threading.Thread(CalcularAreaRectangulo(8,12))
r2 = threading.Thread(CalcularAreaRectangulo(6,15 ))