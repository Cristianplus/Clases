"""
Clases
"""
print("--------------------")
class Programador:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages
    
    def print(self):
        print(
            f"Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | lenguajes: {self.languages}"
        )

mi_programador = Programador("Cristian", 25, ["Python", "JavaScript", "PHP"])
mi_programador.print()
mi_programador.surname = "Cordero"
mi_programador.print()
mi_programador.age = 26
mi_programador.print()
mi_programador.languages.append("Java")
mi_programador.print()

"""
Extra
"""
print("---------PILA----------")

class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        if len(self.stack) == 0:
            return 0
        else:
            return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.print()
print(f"1) tienes {my_stack.count()} elementos en la pila")
print(f"2) se ha eliminado el elemento: {my_stack.pop()} de la pila")
print(f"3) tienes {my_stack.count()} elementos en la pila")
my_stack.push("D")
print("4) se ha añadido el elemento: D a la pila")
print(f"5) tienes {my_stack.count()} elementos en la pila")
print(f"6) se ha eliminado el elemento: {my_stack.pop()} de la pila")
print(f"7) tienes {my_stack.count()} elementos en la pila")
print("8) los elementos de la pila son:")
my_stack.print()
print(f"9) se ha eliminado el elemento: {my_stack.pop()} de la pila")
print(f"10) se ha eliminado el elemento: {my_stack.pop()} de la pila")
print(f"11) los elementos de la pila son: {my_stack.count()}")

print("---------COLA----------")

class Queue:

    def __init__(self):
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)

    def deequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        if len(self.queue) == 0:
            return 0
        else:
            return len(self.queue)

    def print(self):
        for item in (self.queue):
            print(item)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print("Elementos en la cola son:")
my_queue.print()
print(f"1) tienes {my_queue.count()} elementos en la cola")
print(f"2) se ha eliminado el elemento {my_queue.deequeue()} de la cola")
print(f"3) se ha eliminado el elemento {my_queue.deequeue()} de la cola")
print(f"4) se ha elimiando el elemento {my_queue.deequeue()} de la cola")
print("Elementos en la cola son:")
my_queue.print()
print(f"5) tienes {my_queue.count()} elementos en la cola")
my_queue.equeue("D")
print("6) se ha añadido el elemento D a la cola")
print("Los elementos en la cola son:")
my_queue.print()