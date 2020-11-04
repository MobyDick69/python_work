################################# FUNCTIONS ###################################
# N.B. Nel body di una function, si scrivono commenti per la documentazione
# mettendoli dentro """:
def saluto(name, parola='ciao'):
    """ Saluta la persona di cui si specifica il nome """
    print(f"{parola.title()} {name.title()}, piacere mio!")

# Richiami (call) della funzione:
saluto("pippo")
saluto(parola="suca", name="pluto")

###############################################################################
