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
###############################################################################

####################### Ex. 7-5 Python Crash Course ###########################
# Write a loop asking user's age, charging a different ticket depending on it:
flag = True
while flag:
    age_c = input("Please enter your age, so that we'll charge your ticket.\n"
                  "(Enter 'shush' if you don't want to see the movie): ")
    if age_c != 'shush':
        age = int(age_c)
        if age < 3:
            print(f"As you are {age}, you can freely enter!\n")
        elif 3 <= age < 12:
            print(f"As you are {age}, you must pay $10.\n")
        else:
            print(f"As you are {age}, you must pay $15.\n")
    else:
        flag = False
###############################################################################

####################### Ex. 7-8 Python Crash Course ###########################
# List of orders for sandwiches:
sandwich_order = ['club' , 'tramezzino' , 'pastrami' , 'tuna' , 'pastrami']
# List of completed sandwiches, initially empty:
completed_sandwich = []
# Prima, prendo gli ordini in ordine:
sandwich_order.reverse()
orders_in_ordine = sandwich_order[:]
sandwich_order.reverse()
# Loop through every order for sandwiches:
while orders_in_ordine:
    sandwich = orders_in_ordine.pop()
    print(f"Stiamo facendo il sandwich: {sandwich}!")
    completed_sandwich.append(sandwich)
print("Qui la lista dei sandwich pronti:")
for panino in completed_sandwich:
    print(panino)
###############################################################################
