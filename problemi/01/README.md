# Problema 1 (*Franchino ed il misterioso verdetto del professor Pasquals*)
| **Difficoltà** | 🔥🔥 |
|:--------------:|:--:|

Primo appello, primo esame, primo trauma. Franchino si era iscritto a **Logica e Reti Logiche** con l’entusiasmo di chi ha appena imparato a montare una RAM... al contrario.  
Dopo settimane passate a copiare tabelle della verità e a fingere di capire la differenza tra **MUX** e **decoder**, arriva finalmente il giorno tanto atteso: il **professor Pasquals**, leggenda vivente del dipartimento e unico essere umano in grado di disegnare un circuito combinatorio a occhi chiusi, pubblica i risultati dell’esame.

O almeno... **sembrano** i risultati.

L’elenco consiste in una serie di **matricole‍ criptate** con un oscuro algoritmo (che poi a qualcuno sembra il _cifrario di Vigenère_, ma a Franchino sembrava più un nome da Pokémon), seguite da un numero che dovrebbe rappresentare il **voto**. Ovviamente, Pasquals non fornisce alcuna spiegazione: _“Chi vuole sapere il voto, lo decifri. È tutto lì. Logica, ragazzi.”_

Franchino, armato di una **chiave segreta** che aveva scritto sul diario in prima settimana (accanto alla scritta “Mai fidarsi dei professori simpatici”), si ritrova davanti a una sfida degna di un escape room.  
Aiuta Franchino a **decifrare la sua matricola** usando la chiave che ha, così potrà finalmente capire se dovrà rifare l’esame… o offrire da bere.

---

### **Input**:

- Due variabili `str‌`:  
      - `key‍`, che rappresenta la chiave di cifratura;  
      - `text​`, che rappresenta la matricola da decifrare.

### **Output**:

- Una variabile `str‍` che indica la stringa `text‍` decifrata.

### **Esempio**

- `key`  : "hackathon"
- `text` : "ttlcz lgcfmmx p saleu!"
  
| Key + Text | Risultato |
| -------------- | --------- |
| h + t          | b         |
| a + t          | u         |
| c + l          | o         |
| k + c          | n         |
| a + z          | a         |
| t + l          | f         |
| h + g          | o         |
| o + c          | r         |
| n + f          | t         |
| h + m          | u         |
| a + m          | n         |
| c + x          | a         |
| k + p          | a         |
| a + s          | u         |
| t + a          | t         |
| h + l          | t         |
| o + e          | t         |
| n + u          | i         |


`output` = buona fortuna a tutti!


| [**<**](../00/README.md) | [**Home**](../../README.md) | [**>**](../02/README.md) |
| :----------------------: | :-------------------------: | :----------------------: |
