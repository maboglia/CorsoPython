from libro import Libro
from libreria_dao import libreria

with open('biblioteca.html', 'w') as f:

    f.write(f"""
            <html>
            <head>
            <link
            rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
            >
            </head>
            <body>
            <div class='container'>
            """)

    for libro in libreria:
        f.write(libro.toHtml())

    f.write(f"""
            </div>
            </body>
            </html>
            
            """)

