############################ Reading a txt file ###############################
file = 'C:\\Users\\andre\\Documents\\python_work\\files\\py_digits.txt'
with open(file) as file_obj:
    for line in file_obj:
        print(line.rstrip())
###############################################################################

####################### Ex 10-1,2 Python Crash Course #########################
filename = 'files\\learning_python.txt'
with open(filename) as file_obj:
    lines = file_obj.readlines()

for phrase in lines:
    phrase_mod = phrase.replace('Python','SAS')
    print(phrase_mod.rstrip())
###############################################################################

############################ Writing to a file ################################
filename = 'files\\learning_python.txt'
with open(filename, 'a') as file_obj:
    file_obj.write('In Python you can also write to a txt file!\n')
    file_obj.write('In Python you can also create an app that run on browser!')
###############################################################################

################################## Exceptions #################################
print("Inserisci numeratore e denominatore ('q' per uscire)\n")

while True:
    num = input("Numeratore: ")
    if num == 'q':
        break
    den = input("Denominatore: ")
    if den == 'q':
        break
    try:
        result = int(num) / int(den)
    except ZeroDivisionError:
        print("Non si può dividere un numero per 0;"
              " prego re-immettere il denominatore")
    except ValueError:
        print("Prego immettere un numero")
    else:
        print(result)
###############################################################################

######################## Ex 10-10 Python Crash Course #########################
filename = "C:\\Users\\andre\\Documents\\python_work\\files\\moby_dick.txt"

with open(filename, encoding='utf-8') as f:
    content = f.read()
    words = content.split()
    dick_count = 0
    for word in words:
        if word.lower() == 'dick':
            dick_count += 1
    print(dick_count)
###############################################################################
