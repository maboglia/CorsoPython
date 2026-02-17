# **MySQL** e **SQLite**

## 🆚 Confronto tra MySQL e SQLite

MySQL e SQLite sono due sistemi di gestione di database relazionali (RDBMS) molto popolari, ma con caratteristiche e casi d'uso differenti.

---

## 1️⃣ Architettura

### 🔹 MySQL

* Database **client-server**
* Processo server separato (`mysqld`)
* Accesso tramite socket o TCP/IP
* Supporta utenti, ruoli e permessi

### 🔹 SQLite

* Database **embedded (serverless)**
* Nessun processo server
* Il database è **un singolo file**
* Accesso diretto tramite libreria

📌 Differenza chiave:
MySQL = sistema di database completo
SQLite = libreria incorporabile nell’applicazione

---

## 2️⃣ Installazione e configurazione

| MySQL                             | SQLite                       |
| --------------------------------- | ---------------------------- |
| Richiede installazione server     | Nessuna installazione server |
| Configurazione utenti e privilegi | Nessuna gestione utenti      |
| Più complesso da amministrare     | Estremamente semplice        |

SQLite è ideale per:

* Applicazioni desktop
* Mobile (Android lo usa internamente)
* Prototipi
* Test automatici

---

## 3️⃣ Gestione della concorrenza

### MySQL

* Gestisce molte connessioni simultanee
* Lock a livello di riga (InnoDB)
* Ottimo per applicazioni web multiutente

### SQLite

* Supporta letture concorrenti
* Scrittura: **una alla volta**
* Non adatto a carichi elevati multiutente

---

## 4️⃣ Prestazioni

* SQLite è **molto veloce** per:

  * Operazioni locali
  * Dataset medio-piccoli
* MySQL è migliore per:

  * Database grandi
  * Sistemi con molte connessioni simultanee
  * Applicazioni distribuite

---

## 5️⃣ Funzionalità SQL

Entrambi supportano:

* SELECT
* INSERT
* UPDATE
* DELETE
* Indici
* Transazioni

MySQL offre in più:

* Stored procedure
* Trigger avanzati
* Replicazione
* Cluster
* Gestione utenti e privilegi avanzati

SQLite è più essenziale ma supporta:

* Trigger
* Foreign key
* Transazioni ACID

---

## 6️⃣ Sicurezza

MySQL:

* Sistema utenti/password
* Permessi granulari
* Accesso remoto configurabile

SQLite:

* Nessun sistema utenti interno
* Sicurezza affidata ai permessi del file system

---

## 7️⃣ Quando scegliere cosa?

### ✅ Usa MySQL se

* Stai sviluppando un'applicazione web
* Hai più utenti contemporanei
* Ti serve scalabilità
* Serve gestione utenti/ruoli

### ✅ Usa SQLite se

* Applicazione desktop o mobile
* Progetto didattico
* Applicazione embedded
* Test automatici
* Prototipazione veloce

---

## 8️⃣ Esempio pratico (in ambito PHP)

Nel tuo caso (dato che lavori spesso con PDO):

```php
// MySQL
$pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");

// SQLite
$pdo = new PDO("sqlite:database.db");
```

Con SQLite non devi configurare nulla: il file viene creato automaticamente.

---

# 🔎 Riassunto sintetico

| Caratteristica | MySQL               | SQLite              |
| -------------- | ------------------- | ------------------- |
| Tipo           | Client-Server       | Embedded            |
| File           | Più file + processo | 1 file              |
| Multiutente    | Ottimo              | Limitato            |
| Setup          | Medio/Complesso     | Zero                |
| Scalabilità    | Alta                | Bassa-Media         |
| Ideale per     | Web app             | Desktop/Mobile/Test |

