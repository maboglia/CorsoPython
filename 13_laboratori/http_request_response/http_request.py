import requests

class Film:
    def __init__(self, titolo, anno):
        self.titolo = titolo
        self.anno = anno
    
    def __str__(self):
        return f"{self.titolo} - {self.anno}"
    
    def toHtml(self):
        return f"<p>{self.titolo} - {self.anno}</p>\n"

def scrivi_file(nome_file, contenuto):
    with open(nome_file, 'w') as file:
        file.write(contenuto)

URL = 'https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/film/best-free-yt-movies-rt.json'

response = requests.get(URL)

output = ''
if response.status_code == 200:
    data = response.json()
    for film in data:
        film_obj = Film(film['titolo'], film['anno'])
        output += film_obj.toHtml()
    scrivi_file('film.html', output)

else:
    print(f"Errore nella richiesta: {response.status_code}")




