# prodotto.py
class Prodotto:

    def __init__(self, nome, prezzo_unitario):
        self.nome = nome
        self.prezzo_unitario = prezzo_unitario

    def to_dict(self):
        return {
            'nome': self.nome,
            'prezzo_unitario': self.prezzo_unitario
        }
    