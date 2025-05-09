# Problema 6  (*Franchino e l'incubo della falsa laurea*)
| **Difficoltà** | 🔥🔥🔥 |
|:--------------:|:--:|

Dopo⁠ ‍⁡⁠ ‍⁢⁠ ‍⁡⁠ ‍⁢⁠ ‍⁡ aver⁡⁠ ‍⁢ passato⁡⁠ ‍⁡ l’intera notte⁡⁠ ‍⁡ a giocare⁢⁠ ‍⁢ a _Portal_ e ad ignorare l'orario delle lezioni⁡⁠ ‍⁡ del giorno dopo, Franchino si addormenta sulla tastiera. Quando riapre gli occhi, si ritrova in una versione distorta della sua città universitaria, un’enorme griglia di strade, corridoi e portali.

Sta sognando.⁡⁠ ‍⁢ E nel sogno, si **sta⁡⁠ ‍⁡⁠ ‍⁢ laureando**.

Il⁡⁠ ‍⁡ problema? È⁢⁠ ‍⁢ in **ritardo mostruoso**. Parte⁡⁠ ‍⁡ da casa sua, e deve raggiungere l’**Aula Magna** prima⁢⁠ ‍⁢ che leggano il suo nome.  
Ogni passo⁡⁠ ‍⁢ richiede **1 minuto**, e il mondo intorno a lui è regolato da regole bizzarre, un misto tra videogioco e incubo accademico.

Il⁡⁠ ‍⁢ percorso è disseminato di simboli strani, ognuno con un effetto⁡⁠ ‍⁡ diverso:

---

### **Legenda⁡⁠ ‍⁢ dei simboli nella griglia**

- 🐹 – **Start**: casa⁡⁠ ‍⁢ di Franchino, il punto di partenza.
    
- 🏁 – **End**: l’Aula Magna. Il suo traguardo.
    
- 🍄 – **Fungo**: lo teletrasporta **di +2 celle** in una delle 4 direzioni cardinali.
    
- 💀 – **Teschio**: casella⁡⁠ ‍⁢ bloccata, **non può** essere attraversata in nessun modo.
    
- 🍬 – **Caramella**: Franchino è carico⁡⁠ ‍⁢ di zuccheri e può muoversi liberamente oltre che nelle **quattro direzioni cardinali** anche **nelle lungo le 4 diagonali**.
    
- 🪞 – **Specchio**: confonde le coordinate, Franchino si ritrova in **M[y][x]** anziché M[x][y].
    
- 🠖 , 🠕 , 🠔 , 🠗 – **Freccia direzionale**: lo teletrasporta **fino all’ultima⁡⁠ ‍⁡ cella della riga/colonna corrente** nella **direzione puntata dalla freccia**.
    
- `--` – **Casella normale**: richiede 1 minuto per essere attraversata, si può muovere in direzioni cardinali.
    

---

### **Regole del sogno**

- Franchino può muoversi **solo in su, giù, sinistra o destra**, una casella alla volta.
    
- Ogni movimento costa **1 minuto**, tranne dove indicato diversamente.
    
- **I teletrasporti si attivano automaticamente**: se finisce su una casella con un effetto, lo subisce, cancellando i movimenti normali. Non può evitarlo.
    
- L’obiettivo è raggiungere l’Aula Magna nel **minor tempo possibile**, sfruttando (o sopravvivendo) a ogni simbolo.
    

---

### **Input**

- Una matrice `n × m` di simboli come descritti sopra.
    
- Esattamente una cella `S` (start) e una `E` (end).
    

### **Output**

- Un intero: il **numero minimo di minuti** necessari per andare da `S` a `E`, rispettando tutte le regole del sogno.

| [**<**](../05/README.md) | [**Home**](../../README.md) | [**>**](../07/README.md) |
| :----------------------: | :-------------------------: | :----------------------: |
