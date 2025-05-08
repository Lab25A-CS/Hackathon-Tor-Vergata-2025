# Problema 5 (*Franchino ed il filo di Arianna*)
#### Difficoltà: 🔥🔥🔥🔥

Nel cuore del dipartimento, tra un esonero a sorpresa e un esercizio lasciato "per casa", il professor Giullà, che punta tantissimo su di lui (nessuno, compreso Franchino stesso, capisce perché), consegnò a Franchino una nuova sfida: un **labirinto**,‌ formato da stanze connesse da **corridoi a senso unico**, che scendevano sempre verso nuovi livelli più profondi.

In ogni corridoio, Franchino poteva trovare **monete** da raccogliere… oppure **fantasmi**‌ pronti a derubarlo.  
Alcuni percorsi gli facevano guadagnare ricchezza, altri gliela prosciugavano.

L’obiettivo?

> "Conta tutti i percorsi che partono da una stanza e si inoltrano verso le sue discendenti, in cui il totale delle monete (contando anche quelle che i fantasmi ti rubavano) sia **esattamente pari al target**.”

Camminando in avanti nel labirinto, da una stanza a quelle sotto di essa, Franchino poteva decidere dove fermarsi, ma non tornare indietro.  
E ogni volta che trovava un percorso che soddisfaceva la somma esatta… metteva una tacca sul muro.

Aiutalo a capire **quante tacche** dovrà fare.

---

### **Input**:

- Una lista di bivi, in cui ognuno di esso ha:
	- Un nome identificato da una stringa;
	- Un intero `w_i‍` (positivo o negativo) rappresentante il guadagno o la perdita di monete;
	- Il nome del bivio che si ritrova scendendo a destra;
	- Il nome del bivio che si ritrova scendendo a sinistra.
- Un intero `targetsum`.
### **Output**:

- Un intero: il numero di volte che Franchino si trova in tasca *esattamente* `targetsum` monete prendendo in considerazione tutti i percorsi che può intraprendere.
