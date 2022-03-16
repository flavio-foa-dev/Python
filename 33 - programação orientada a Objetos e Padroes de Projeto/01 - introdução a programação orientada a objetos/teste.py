class telefone:
    def __init__(self, cor, modelo, marca, numero, tom):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.numero = numero
        self.tom = tom

    def ligar(self):
        print(f"ligando {self.numero}")


    def receber_ligacao(self):
        if(self.tom):
            print("recebe ligaçâo")

class carrinho:
    def __init__(self, marca str, tamanho):
        self.marca = marca
        self.tamanho= tamanho

    def pega_marca(self):
       print(f"tamanho{self.marca}")


    def diz_Tamanho(self):
        print(f"tamanho{self.tamanho}")

marca1 = carrinho.pega_marca("skolll")
tamanho1 = carrinho.diz_Tamanho("litão")

print(marca1)
print(tamanho1)