## 🔹 **xxargs (`**kwargs`)**

### **Idea chiave**

`**kwargs` permette di accettare **un numero variabile di argomenti con nome** (keyword arguments).
Questi argomenti vengono raccolti in un **dizionario**.

---

## **Che cos’è `**kwargs`?**

Quando in una funzione includi `**kwargs`, Python raccoglie tutti gli argomenti passati nella forma `chiave=valore` e li mette in un dizionario.

È utile quando:

* vuoi rendere le funzioni estremamente flessibili;
* non conosci in anticipo quali parametri opzionali verranno forniti;
* vuoi permettere configurazioni con nomi chiari.

---

## **Esempio base**

```python
def descrivi_persona(**kwargs):
    for chiave, valore in kwargs.items():
        print(f"{chiave}: {valore}")

descrivi_persona(nome="Anna", età=30, ruolo="Manager")
```

### Output

```
nome: Anna
età: 30
ruolo: Manager
```

✔ Tutti gli argomenti diventano coppie chiave–valore in un dizionario.

---

## **Regole importanti**

* `kwargs` è solo un nome convenzionale, ma `**kwargs` è lo standard.
* `**kwargs` deve comparire **alla fine** della definizione della funzione, dopo:

  1. argomenti normali
  2. `*args` (se presenti)

Ordine corretto:

```python
def funzione(a, b, *args, **kwargs):
    pass
```

---

## **Usi tipici**

* funzioni con configurazioni flessibili;
* parametri opzionali complessi;
* forwarding di argomenti in funzioni wrapper o decorator;
* costruzione dinamica di oggetti o messaggi.

