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