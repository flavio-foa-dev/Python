class Cachorro:
    cobertura = 'pelo'
    patas = 4
    tipo_animal = "mamifero"


    def __init__(self, name):
        self.name = name

    def grita(self):
        print(f"{self.name}: auu auuu...")



class Galinha:
    cobertura = 'pena'
    patas = 2
    tipo_animal = 'ave'

    def __init__(self, name):
        self.name = name

    def grita(self):
        print(f"{self.name}: cocorico...")

if __name__ == '__main__':
    rex = Cachorro("Rex")
    lili = Galinha("Lili")

    print(rex.cobertura)
    rex.grita()

    print (lili.cobertura)
    lili.grita()

    print(f"{rex.grita()}: {lili.grita()} Socorro")
