class User:
    # Não preciso saber como a classe funciona, lalalalala
    def __init__(self, name, email, password):
        """
        Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!
        """
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
      print("Envia email de reset da senha ")
      # A classe tem essa função? Ótimo! Pra mim basta!


# Para invocar o método construtor, a sintaxe é NomeDaClasse(parametro 1, parametro 2)
# Repare que o parâmetro self foi pulado -- um detalhe do Python.
meu_user = User("valetino trocatapa", "valetino@tinytoons.com", "grana123")
meu_user.reset_password()

# Já sei o suficiente pra agir!
print(meu_user)
print(meu_user.name)
print(meu_user.email)
print(meu_user.password)
print(meu_user.reset_password())


# A variável `meu_user` contém o objeto criado pelo construtor da classe User!