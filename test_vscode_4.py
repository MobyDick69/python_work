######################### Ex. 9-5 Python Crash Course #########################
class User:
    """ A class that describes users """
    def __init__(self,first_name,last_name,age,email,rating):
        ''' Initialize attributes '''
        self.nome    = first_name
        self.cognome = last_name
        self.eta     = age
        self.email   = email
        self.rating  = rating
        self.login_attempts = 0
    
    def describe_user(self):
        ''' Print user's informations '''
        print("Qui di seguito le informazioni sull'utente:")
        print(f"Nome: {self.nome.title()}\nCognome: {self.cognome.title()}\n"
              f"Eta': {self.eta}\nMail: {self.email}\nStato: {self.rating}\n"
              )

    def greet_user(self):
        ''' Saluto personalizzato all'utente '''
        print(f"Ciao {self.nome}!\nComplimenti, sei di livello {self.rating}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Numero di login: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Azzerati i login!")

"""
io = User('andrei', 'koimasky', 33, 'mailfasulla@123.it', 5)
print(f"Sono {io.nome}")
io.describe_user()
io.greet_user()
io.increment_login_attempts()
io.increment_login_attempts()
io.increment_login_attempts()
io.reset_login_attempts()
print(f"Numero di login totali: {io.login_attempts}")


altro = User('ajeje', 'brazorf', 40, 'pippofranco@123.it', 2)
altro.describe_user()"""
###############################################################################

######################### Ex. 9-7 Python Crash Course #########################
class Admin(User):
    """ Class that inherits attributes and methods from class Users """
    def __init__(self,first_name,last_name,age,email,rating,
                 privileges=['read','write','execute']
                 ):
        ''' Inizializzo attributi della parent class '''
        super().__init__(first_name,last_name,age,email,rating)
        ''' Inizializzo nuovo attributo '''
        self.privilegi = privileges

    def mostra_privilegi(self):
        print(self.privilegi)

io_adm = Admin('andrei', 'koimasky', 33, 'mailfasulla@123.it', 5)
io_adm.describe_user()
io_adm.mostra_privilegi()
###############################################################################
