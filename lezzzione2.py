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
"""
def aggrega_voti(voti: list[dict[str, int]]) -> dict[str:list[int]]:
    new_dict = {}
    for voto in voti:
        if voto["nome"] in new_dict:
            new_dict[voto["nome"]].append(voto["voto"])
        else:
            new_dict[voto["nome"]] = [voto["voto"]]
    return new_dict"""
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





