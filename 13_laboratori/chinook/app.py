import database

DB = database.connetti()

tabelle = ["album", "artist", "customer", "employee", "genre", "invoice", "invoice_line", "media_type", "playlist", "playlist_track", "track"]
tabelle = ["album", "artist", "customer", "employee", "genre", "track"]

output = []

for t in tabelle:
    output.append(f"Tabella: {t}")
    righe = database.trova_tutti(DB, t)
    for r in righe:
        output.append(r)
    output.append('-' * 40)

# righe = database.trova_tutti(DB, "album")
# for r in righe:
#     print(r)

database.disconnetti(DB)

with open("output.txt", "w", encoding="utf-8") as f:
    for r in output:
        f.write(str(r) + "\n")