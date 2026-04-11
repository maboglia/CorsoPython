from dataclasses import dataclass
from database import prodotti

@dataclass
class Prodotto:
    nome_prodotto: str
    prezzo: float
    stock: int
    categoria: str   
    fornitore: str   
    

lista_prodotti = []    
for a,b,c,d,e in prodotti:
    p = Prodotto(a,b,c,d,e)
    lista_prodotti.append(p)
