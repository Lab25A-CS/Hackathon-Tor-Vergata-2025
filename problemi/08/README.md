# Problema⁡⁠ ‍⁢ 8 (**Franchino e il backlog videoludico**)

| **Difficoltà** | 🔥🔥🔥🔥🔥 |
|:--------------:|:--:|

La sessione⁡⁠ ‍⁡ è finita. Franchino ha collezionato più 18 che CFU, ha sostenuto esami con lo stesso entusiasmo con cui si fa la fila⁡⁠ ‍⁢ in segreteria… e ha deciso che ha **bisogno⁡⁠ ‍⁡ di staccare**.

Grazie ai soldi guadagnati⁡⁠ ‍⁡ nel suo stage ferroviario (vedi [**Problema 7**](../07/README.md)), ha messo da parte un po’ di budget⁡⁠ ‍⁡ e vuole investirlo come ogni studente stressato farebbe: **comprando videogiochi**.  
Ha preso una decisione importante: vuole rigiocarsi **tutta la saga di Assassin’s Creed** _e_ **tutti i Call of Duty**, rigorosamente **in ordine di uscita**.

Ogni gioco ha un **prezzo**, e Franchino può comprarli **solo nell’ordine esatto** delle rispettive serie, senza saltare titoli né mischiarli.  
Ovviamente, ha un **budget massimo**,‌⁠‍‬ e non può sforarlo neanche di un centesimo: la mensa universitaria non fa credito.

---

### **Input**

- `firststack`: lista⁡⁠ ‍⁢ di `n` interi positivi, rappresenta il costo dei giochi di **Assassin’s Creed**, in ordine cronologico.
    
- `secondstack`: lista⁡⁠ ‍⁡ di `m` interi positivi, rappresenta il costo dei giochi di **Call of Duty**, anche questi ordinati.
    
- `maxWeight`: intero positivo, rappresenta **il budget totale** di Franchino.
    

**N.B.** Ricordiamo che _per acquistare_ l'i-esimo gioco, Franchino deve aver comprato anche **tutti** gli $i-1$ giochi precedenti.

---

### **Output**

- Una tupla⁡⁠ ‍⁢ di due interi: `(x, y)`  
    dove:
    
    - `x` = numero di giochi di Assassin’s Creed che Franchino riesce a comprare in ordine,
        
    - `y` = numero di Call of Duty acquistati, sempre in ordine,
        

**N.B.** La somma dei costi totali è **$\le$ `maxWeight`** e **più vicina possibile** a tale limite.

---

Franchino sa che non potrà comprarli tutti… ⁡⁠ ‍⁢(forse) ma vuole comunque **spendere il più possibile**, **senza sforare** il suo budget.  
Aiutalo a scegliere **quanti giochi per ciascuna saga** potrà riscoprire, in modo da ottimizzare la spesa e ritrovare⁡⁠ ‍⁢ un minimo di pace videoludica prima della prossima sessione.

| [**<**](../07/README.md) | [**Home**](../../README.md) | [**>**](../09/README.md) |
| :----------------------: | :-------------------------: | :----------------------: |
