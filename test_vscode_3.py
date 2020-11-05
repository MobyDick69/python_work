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

################################### RETURN ####################################
# return statement restituisce un elemento calcolato nella function:
def music_album(artist,title,number_songs=None):
    album = {'artist_name' : artist ,
             'album_title'  : title ,
             }
    if number_songs:
        album['number_of_songs'] = number_songs
    return album

album_1 = music_album(artist='slayer',title='raining blood', number_songs=13)
print(album_1)
###############################################################################

####################### Ex. 8-9,10,11 Python Crash Course #####################
messages = ['ciao', 'bella', 'hola',"com'e'"]
sent_messages = []
def send_messages(da_spedire, spediti):
    ''' 
    Tolgo un item alla volta dalla lista d'input e lo aggiungo alla lista
    d'output.
    '''
    while da_spedire:
        in_spedizione = da_spedire.pop()
        spediti.append(in_spedizione)
        print(f"Messaggio in spedizione: {in_spedizione}")

send_messages(messages[:],sent_messages)
print(messages)
print(sent_messages)
###############################################################################

######################### Ex. 8-14 Python Crash Course ########################
def make_car(maker, model, **kwargs):
    kwargs['manufacturer'] = maker
    kwargs['model_name'] = model
    return kwargs

car_info = make_car('fiat',
                    '500',
                    cylinders=4,
                    hybrid='yes')

print(car_info)
###############################################################################