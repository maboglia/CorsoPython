import os
import re


def rename_markdown_files(directory="."):
    # Pattern per estrarre il titolo tra i due asterischi dopo il numero
    # Cerca di gestire diversi tipi di trattini (en-dash, em-dash, hyphen)
    pattern = re.compile(r"## \*\*\d+ [–\-] (.*?)\*\*")

    # Nuovo pattern:
    # ^# -> Inizia con #
    # .*? -> Qualsiasi carattere fino ai primi asterischi (include spazio e emoji)
    # \*\*(.*?)\*\* -> Cattura tutto ciò che è tra i doppi asterischi
    pattern = re.compile(r"^## .*? \*\*(.*?)\*\*")

    # Pattern universale:
    # ^#     -> Inizia con #
    # .*?    -> Salta qualsiasi cosa (spazi, emoji, numeri) finché non trova **
    # \*\* -> Trova l'apertura del grassetto
    # (.*?)  -> Cattura il titolo (Gruppo 1)
    # \*\* -> Trova la chiusura del grassetto
    # pattern = re.compile(r"^#.*?\*\*(.*?)\*\*")

    # Nuova regola, tutto ciò che c'è dopo il cancelletto
    # pattern = re.compile(r"^#\s+(.*)")

    for filename in os.listdir(directory):
        if filename.endswith(".md") and filename[:2].isdigit():
            filepath = os.path.join(directory, filename)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()

                match = pattern.search(first_line)
                if match:
                    # Estrae il titolo (es: Comparison Operators)
                    title = match.group(1).strip()

                    # Sostituisce spazi e caratteri speciali non ammessi nei nomi file
                    clean_title = title.replace(" ", "_")
                    clean_title = re.sub(r'[\\/*?:"<>|]', "", clean_title)

                    # Costruisce il nuovo nome: 01_Comparison_Operators.md
                    prefix = filename.split('.')[0]
                    new_filename = f"{prefix}_{clean_title}.md"
                    new_filepath = os.path.join(directory, new_filename)

                    # Rinomina il file
                    os.rename(filepath, new_filepath)
                    print(f"Rinominato: {filename} -> {new_filename}")
                else:
                    print(
                        f"Salto {filename}: Formato prima riga non corrispondente.")

            except Exception as e:
                print(f"Errore durante l'elaborazione di {filename}: {e}")


if __name__ == "__main__":
    # Puoi specificare il percorso della cartella tra le parentesi
    rename_markdown_files()
