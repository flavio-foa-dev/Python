class Cachorro:
    cobertura = 'pelo'
    patas = 4
    tipo_animal = "mamifero"


    def __init__(self, name, do_bem):
        self.name = name
        self.do_bem = do_bem

    def grita(self):
        print(f"{self.name}: auu auuu...")

    def morde(self, bicho):
        if self.do_bem:
            print(f"{self.name}: eu nao mordo não não grita ")

        else:
            print(f"{self.name}: esta mordendo {bicho.name}")
            bicho.grita()



class Galinha:
    cobertura = 'pena'
    patas = 2
    tipo_animal = 'ave'

    def __init__(self, name):
        self.name = name

    def grita(self):
        print(f"{self.name}: cocorico...")

if __name__ == '__main__':
    rex = Cachorro("Rex", False)
    lili = Galinha("Lili")

    rex.morde(lili)
