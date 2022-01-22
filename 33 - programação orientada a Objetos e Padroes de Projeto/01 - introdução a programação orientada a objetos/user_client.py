import smtplib
import ssl

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def reset_password(self):
        subject = "reset your password"
        message = "Intruçoes para resetar a senha, com o link de reset"
        body = f"subject:{subject}\n\n{message}".encode('utf-8')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=context
        ) as server:
            server.login(self.from_email, self.from_password)
            try:
                server.sendmail(self.from_email, self.from_password, body=body)
            except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
                raise ValueError


class Mailer:
    def __init__(self, from_email, from_password, to_email):
        self.from_email = from_email  # email de origem
        self.from_password = from_password # password do email de origem
        self.to_email = to_email # email a receber a mensagem



meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()

meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_mailer = Mailer("password_reset@teste.com", "myverysafepassword", meu_user.email)
meu_mailer.reset_password(meu_user)