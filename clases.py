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


