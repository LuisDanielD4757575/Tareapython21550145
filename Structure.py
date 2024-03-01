class Equipos:
    def __init__(self, nombre, integrante1, integrante2, integrante3=""):
        self.nombre = nombre
        self.integrantes = [integrante1, integrante2, integrante3]

    def __str__(self):
        result = f"{self.nombre}:\n\n"
        for integrante in self.integrantes:
            result += f"{integrante}\n"
        return result

class FS3:
    def __init__(self, equipo1, equipo2, equipo3, equipo4, equipo5, equipo6):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.equipo3 = equipo3
        self.equipo4 = equipo4
        self.equipo5 = equipo5
        self.equipo6 = equipo6

    def __str__(self):
        result = str(self.equipo1) + "\n" + str(self.equipo2) + "\n"  + str(self.equipo3) + "\n" + str(self.equipo4) + "\n" + str(self.equipo5) + "\n" + str(self.equipo6) 

        return result

# Ejemplo de uso:
equipo1 = Equipos("Toyotalegacy", "Israel Chacon Rojo", "Dilan Mauricio Garcia Hernandez", "Jesus Elias Sierra Ruiz")
equipo2 = Equipos("WebHeros", "Jesus Manuel Arellano Merendon", "Luis Daniel Delgado Enriquez", "Axel Felipe Reyes Valadez")
equipo3 = Equipos("Los =^UwU^=", "Leonardo Alberto Gonzáles Carmona", "Norma Graciela Mendoza Ruiz", "Jonathan Durán Mendoza")
equipo4 = Equipos("LosPolystation", "Erick Fernando Siqueiros Zúñiga", "Paulina Ixchel Arreguin Ruiz")
equipo5 = Equipos("Los 3 Mosqueteros", "Dania Denisse Benavides Figueroa", "Erick Lozano Duarte", "Ana Cristina Valenzuela Ruiz")
equipo6 = Equipos("Equipo Pingüino Galáctico", "Yahir Antonio Monje Ochoa", "Yesica Cristina Rodriguez Renteria")

fs3 = FS3(equipo1, equipo2, equipo3, equipo4, equipo5, equipo6)

if __name__ == "__main__":
   print(fs3)
