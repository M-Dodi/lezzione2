class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
doc = MyClass()
docu =doc.f()
document = MyClass.__doc__

print(doc.i)
print(docu)
print(document)

"""
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
e aggrega i voti per studentein un nuovo dizionario.
"""
##############
"""
def aggrega_voti(voti: list[dict[str, int]]) -> dict[str:list[int]]:
    new_dict = {}
    for voto in voti:
        if voto["nome"] in new_dict:
            new_dict[voto["nome"]].append(voto["voto"])
        else:
            new_dict[voto["nome"]] = [voto["voto"]]
    return new_dict
"""
def aggrega_voti(voti: list[dict[str, int]]) -> dict[str, list[int]]:
    from collections import defaultdict
    new_dict = defaultdict(list)
    for voto in voti:
        new_dict[voto["nome"]].append(voto["voto"])
    return dict(new_dict)
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([])) 

""""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca 
un nuovo dizionario con solo i prodotti che hanno 
un prezzo superiore a 20, scontati del 10%"

"""

def sconta_prodotti(prodotti: dict[str, float]) -> dict[str, float]:
    scontati = {}
    for key,value in prodotti.items():
        if value > 20:
            scontati[key] = value * 0.9
    return scontati

print(sconta_prodotti({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:

    return {'name': name, 'email': email, 'telefono': telefono}

###########################################################

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    dictionary['name'] = name
    if email is not None:
        dictionary['email'] = email
    if telefono is not None:
        dictionary['telefono'] = telefono
    return dictionary
contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456))
##################################################################
lista_numeri = [42, 9, 23, 11, 17, 56, 3]
numero_maggiore = lista_numeri[0]
for numero in lista_numeri:
    if numero > numero_maggiore:
        numero_maggiore = numero
print("Il numero maggiore tra tutti è:", numero_maggiore)

##################################################################

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo numero: "))

if a >= b and a >= c:
    print("Il numero piu grande è:", a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)
##################################################################
"""
Scrivi un programma "moltiplicatore" che, data una lista di numeri,
 moltiplichi tra loro tutti gli elementi."""

lista_numeri = [1, 2, 3, 4, 5]
molt =  lista_numeri[0]
for i in lista_numeri:
    if i != 0:
      molt *= i
print(molt)
"""
Scrivi un programma che a partire da un elemento e una lista 
di elementi dica in output se l'elemento passato 
sia presente o meno nella lista.

Qualora l'elemento sia presente nella lista, il programma 
dovrà comunicarci l'indice dell'elemento tramite il metodo 
index.

"""
lista = [1,3,5,7,9]
elemento = int(input("inserisci un numero da 1 a 9:"))

if elemento in lista:
    indice = lista.index(elemento)
    print(f"{elemento} trovato all'indice, {indice}")
else:
    print("elemento non in lista")
######################################################


"""Scrivi una semplice funzione che, data una lista di numeri, fornisca 
in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa 
sequenza:
***
*******
*********
*****
"""
def istogramma(lista:list[int])-> None:
    for numero in lista:
        print("*" * numero)
lista = [2, 7, 4, 2]
istogramma(lista)
####################################################

def lunghezza_parola(parola: str) -> int:
    return len(parola)
print(lunghezza_parola("ciao"))
###################################


def frequenza(stringa: str) -> dict[str: int]:
    frequenza = {}
    for i in stringa:
        if i in frequenza:
            frequenza+=1
        else:
            frequenza[i] = 1
    return frequenza








