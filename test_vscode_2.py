############################## CHECK VAR TYPE #################################
num_int = 1
num_dec = 2.0
char = 'Pippo'
lista = ['papete', 'zio']
tupla = ('porco', 3)
print(type(num_int),type(num_dec),type(char), type(lista), type(tupla))
###############################################################################

############################### IF STATEMENT ##################################
booleano = False
if booleano == True:
    print('Vero!')
elif booleano == False:
    print('Falso!')
else:
    print('Qualquadra non cosa...')
###############################################################################

################################# FOR LOOP ####################################
lista = ['papete', 'zio', 'abecedario']

for item in lista:
    print(f"Ma perché ho scritto {item}??")
###############################################################################

################################ DICTIONARY ###################################
# Collezione di coppie di key-value:
alien_0_pos = [ 0 , 0 , 0 ]

alien_0 = { 'color'  : 'green' ,
            'points' : 5 ,
            'pos'    : alien_0_pos
           }

print(f"L'alieno numero 0 si trova in posizione {alien_0['pos']}")
for coord in alien_0['pos']:
    print(f"Coordinata: {coord}")

# Add a key-value pair:
alien_0['speed'] = 'slow'
print(alien_0)
# Modify a value:
if alien_0['speed'] == 'slow':
    x_incr = 1
else:
    x_incr = 0

alien_0_pos[0] = alien_0_pos[0] + x_incr
print(f"L'alieno numero 0 nell'intervallo successivo rispetto all'inizio "
      f"si trova in posizione {alien_0['pos']}")

# Remove a key-value pair:
del alien_0['speed']
print(alien_0)

# Looping through a Dictionary:
user_0 = { 'username' : 'efermi@suca.it' ,
           'name'     : 'enrico' ,
           'surname'  : 'fermi'
          }
for k , v in user_0.items():
    print(f"La chiave {k} ha associato il valore {v.title()}")

for kappa in user_0.keys():
    print(f"Chiave:{kappa}")

for vi in user_0.values():
    print(f"Valore:{vi}")
###############################################################################

################################### INPUT #####################################
# N.B. Programmi con la funzione input() posso essere eseguiti solo da terminale!
prova_input = input("Scrivi qualcosa: ")
print(f"Hai scritto: {prova_input}")

prompt = "Quanti anni hai?\nRispondi qui: "
prova_input_num = input(prompt)
if int(prova_input_num) >= 30:
    print("Ma allora sei vecchio!")
else:
    print("Beh dai sei un g-g-giovane.")