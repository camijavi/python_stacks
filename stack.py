#Definición de la estructura de datos
class Producto:
    def __init__(self,id:str, nombre:str, precio:float,stock:int):
        self.id =id
        self.nombre =nombre
        self.precio = precio
        self.stock = stock
        self.next = None

    def print(self):
        print(f"PRODUCTO --> id = {self.id} | NOMBRE {self.nombre} | PRECIO {self.precio} | STOCK {self.stock}")
 

class Stack:
    def __init__(self):
        self.top=None

        #operaciones de la pila
    def isEmpty(self)->bool:
        if self.top == None:
             return True
        else:
            return False

    def push(self,new:Producto):
        if self.isEmpty():
            self.top=new
        else: 
            new.next = self.top 
            self.top=new

    def pop(self)-> Producto:
        prod = None
        if not self.isEmpty():
            p = self.top
            prod = Producto(p.id, p.nombre, p.precio, p.stock)

            if p.next is not None:
                self.top = self.top.next
            
            else:
                self.top = None
        return prod

    def clear(self)->list[Producto]:
        lista = []

        while not self.isEmpty():
            p = self.pop()
            prod = Producto(p.id, p.nombre, p.precio, p.stock)
            lista.append(prod)
        return lista

    def peek(self)->Producto:
        prod = None
        if not self.isEmpty():
            p = self.top
            prod = Producto(p.id, p.nombre, p.precio, p.stock)
        return prod

    def print(self, interactive: bool = True):
        """
        Visualiza la pila en la terminal al estilo Python Tutor (Frames & Objects).
        Si interactive=True, inicia el simulador interactivo paso a paso con botones.
        """
        from simulator import print_stack_diagram
        print_stack_diagram(self, interactive=interactive)

    def simulate(self):
        """Inicia el simulador interactivo con botones paso a paso."""
        self.print(interactive=True)