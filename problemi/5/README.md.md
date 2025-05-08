# Problema 5 (*Franchino ed il filo di Arianna*)
#### Difficoltà: 🔥🔥🔥🔥

Nel cuore del dipartimento, tra un esonero a sorpresa e un esercizio lasciato "per casa", il prof Giullà, che punta tantissimo su di lui (nessuno, compreso Franchino stesso, capisce perché), consegnò a Franchino una nuova sfida: un **labirinto**,‌ formato da stanze connesse da **corridoi a senso unico**, che scendevano sempre verso nuovi livelli più profondi.

In ogni corridoio, Franchino poteva trovare **monete** da raccogliere… oppure **goblin**‌ pronti a derubarlo.  
Alcuni percorsi gli facevano guadagnare ricchezza, altri gliela prosciugavano.

L’obiettivo?

> "Conta tutti i percorsi che partono da una stanza e si inoltrano verso le sue discendenti, in cui il totale delle monete (contando anche quelle che i goblin ti rubavano) sia **esattamente pari al target**.”

Camminando in avanti nel labirinto, da una stanza a quelle sotto di essa, Franchino poteva decidere dove fermarsi, ma non tornare indietro.  
E ogni volta che trovava un percorso che soddisfaceva la somma esatta… metteva una tacca sul muro.

Aiutalo a capire **quante tacche** dovrà fare.

---

### **Input**:

- Un albero binario‌ diretto con `n‍` nodi, in cui ogni nodo ha un valore intero `w_i‍` (positivo o negativo).
    
- Un intero `targetsum`.
### **Output**:

- Un intero: il numero di cammini `(u, v)`‌ tali che `v` sia discendente di `u` (incluso `u = v`), e la somma dei valori lungo il percorso da `u` a `v` sia esattamente `targetsum`.
