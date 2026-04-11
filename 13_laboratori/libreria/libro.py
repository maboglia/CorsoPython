
class Libro:
    
    def __init__(self, id, Codice, Autore, Titolo, Editore, Classificazione):
        self.id = id
        self.Codice = Codice
        self.Autore = Autore
        self.Titolo = Titolo
        self.Editore = Editore
        self.Classificazione = Classificazione
        
    def __str__(self):
        return f"""
        Titolo: {self.Titolo}
        Autore: {self.Autore}
        Classificazione: {self.Classificazione}
        """

    def toHtml(self):
        return f"""
        <article class='card'>
            <header><h1>Titolo: {self.Titolo}</h1></header>
            <h2>Autore: {self.Autore}</h2>
            <footer><h3>Classificazione: {self.Classificazione}</h3></footer>
        </article>
        """