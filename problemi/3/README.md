# Problema 3 (*Franchino ed il cruciverba maledetto*)
#### Difficoltà: 🔥🔥🔥

Franchino, con la fronte aggrottata e lo sguardo fisso sul foglio, stava cercando di decifrare un enigma che avrebbe messo alla prova anche il Paroliere. Il professor Red gli aveva dato un compito piuttosto curioso: trovare quanti numeri palindromi di lunghezza **k** iniziavano con un numero **start** in una matrice di numeri da 0 a 9.

Un esempio di matrice è la seguente:

```
712  
151  
217  
```

I parametri da considerare erano: _start = 2_ e _k = 3_. Franchino, però, non riusciva a capire come cominciare. "Ok, la matrice ha 8 direzioni in cui posso cercare," mormorò, "ma da dove inizio?"

Le direzioni erano tutte le possibili traiettorie che partivano da ogni numero della matrice e proseguivano in una delle otto direzioni (su, giù, destra, sinistra e le diagonali). Franchino sapeva che doveva iniziare con 2, ma poi si fermò a pensare: “E adesso cosa faccio? Quanti palindromi posso davvero trovare?”

Aiuta Franchino a trovare un algoritmo che risolva il problema.‌

---

### **Input**:

- `matrix‌`, una lista di liste di interi;
    
- `k‍`, un intero che indica la lunghezza dei numeri palindromi;
    
- `start‍`, un intero che indica il primo numero con cui far partire la sequenza palindroma.

---

### **Output**:

- Una variabile `int‍` che identifica la quantità di numeri palindromi considerando `k` e `start`.
