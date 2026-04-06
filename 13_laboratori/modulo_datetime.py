from datetime import datetime, timedelta, date

# Data e ora corrente
ora_corrente = datetime.now()
print(f"Ora corrente: {ora_corrente}")
print(f"Formato personalizzato: {ora_corrente.strftime('%d/%m/%Y %H:%M')}")

# Operazioni con le date
domani = date.today() + timedelta(days=1)
una_settimana_fa = datetime.now() - timedelta(weeks=1)
print(f"Domani: {domani}")
print(f"Una settimana fa: {una_settimana_fa}")

# Parsing da stringa
data_string = "2026-12-25"
natale = datetime.strptime(data_string, "%Y-%m-%d")
print(f"Natale: {natale}")