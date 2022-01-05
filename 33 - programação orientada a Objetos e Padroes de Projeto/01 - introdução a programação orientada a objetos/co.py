class User:
  def __init__(self,name,email,password):
    self.name = name
    self.email = email
    self.password = password


meu_user = User("Valentino","valentino@semha.com","grana")
print(meu_user)
print(meu_user.name)
print(meu_user.email)
print(meu_user.password)


class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

# Para invocar o método construtor, a sintaxe é NomeDaClasse(parametro 1, parametro 2)
# Repare que o parâmetro self foi pulado -- um detalhe do Python.
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")

# A variável `meu_user` contém o objeto criado pelo construtor da classe User

class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        print("Envia email de reset de senha")


meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()
