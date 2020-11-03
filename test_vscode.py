import numpy

# Creo una list:
names = ['andrea' , 'filippo' , 'mario']

# Sostitusco l'ultimo elemento della list:
names[-1] = 'tizio'

####################### AGGIUNGERE ELEMENTI #########################
# Aggiungo 2 elementi con 2 metodi diversi:
# 1.Aggiungo in fondo alla lista:
names.append('turiddu')
# 2.Aggiungo l'elemento nella posizione specificata:
names.insert(1,'carlo')
#####################################################################

####################### ELIMINARE ELEMENTI ###########################
# Elimino elementi con 3 metodi diversi:
# 1.Utilizzo il del statement:
del names[1]
# 2.Utilizzo il .pop method per memorizzare l'elemento eliminato (se non si mette nulla tra parentesi, viene eliminato l'ultimo elemento):
name_canc = names.pop(-2)
# 3.Rimuovo un valore spcifico con remove method:
names.remove('turiddu')
#####################################################################

################################ SORT ###############################
# Sort temporaneo di una list:
print(sorted(names))
# Sort permanente di una list:
names.sort(reverse=True)
print(names)
#####################################################################

######## Determinare il numero di elementi della lista: #############
print(len(names))
#####################################################################

############################## LOOP  ################################
frutta = ['pera', 'mela', 'ananas']
print(frutta)
for fruit in frutta:
    print(f"Buona questa {fruit.upper()}")
#####################################################################

############################## RANGE ################################
# Con la funzione range() si crea una serie numerica:
prova = range(1,5)
print(prova[3])
# Si può convertire la serie creata in una list numerica:
num_list = list(range(1,6,2))
print(num_list)
# range() è molto comoda da usare in for loops:
for value in range(1,6):
    print(value)
#####################################################################

########################### MIN,MAX,SUM #############################
num_list = list(range(1,6))
print(min(num_list),max(num_list),sum(num_list))
#####################################################################

########################## SLICING A LIST ############################
frutta = ['pera', 'mela', 'ananas']
print(frutta[0:2])
print(frutta[:2])
print(frutta[1:])
print(frutta[-2:])
for fruit in frutta[0:2]:
    print(f"Buona questa {fruit.upper()}!")
#####################################################################

############################## TUPLE ################################
# Analoghe alle liste, ma i cui elementi sono IMMUTABILI
dimensioni = (10 , 45 , 20)
for dim in dimensioni:
    print(dim)