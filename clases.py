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