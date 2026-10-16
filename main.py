from stack import Stack
from stack import Producto

def main():
    pila = Stack()
    prod = Producto("P-01", "Mascarilla", 15.23, 6200)
    pila.push(Producto)

    prod = Producto("P-02", "Alcohol", 64.54, 1000)
    pila.push(Producto)

    prod = Producto("P-03", "vitamina", 21.85, 7000)
    pila.push(Producto)

    productos = pila.clear()
    for p in productos:
        p.print

main()