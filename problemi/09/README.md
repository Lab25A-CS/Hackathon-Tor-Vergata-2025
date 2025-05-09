# Problema‌⁠‍‬⁡ 9 (**Franchino e la porta del Laboratorio**)

| **Difficoltà** | 🔥🔥🔥🔥🔥 |
|:--------------:|:--:|

### **Problema‌⁠‍‬ 9 – Franchino e la porta del laboratorio**

Sono gli ultimi momenti della⁠ ‍⁢ notte dell’Hackathon, e Franchino – esausto dopo 16 ore di RedBull, bug⁡⁠ ‍⁡ e false promesse su “ultimo problema” – si appoggia per un attimo sul divano di un’aula studio.  
Quel breve attimo si trasforma in un **sonno profondo**.

I suoi amici, ancora svegli‌⁠‍‬ e troppo carichi di taurina per essere razionali, decidono di fargli uno scherzo: lo **chiudono dentro** e collegano la maniglia della porta a un marchingegno fatto con **interruttori, cavi elettrici e una manopola**.

Davanti a lui, Franchino trova:

- una fila di `n` **interruttori**, tutti inizialmente **abbassati**;
    
- tra ogni coppia di interruttori, c'è un valore positivo⁡⁠ ‍⁢ o negativo;
    
- una **manopola** centrale che gira **in senso orario** quando Franchino colleziona un numero **positivo**, in **senso antiorario** per uno **negativo**, e resta ferma con uno **zero**.


La regola lasciata dai suoi amici è semplice ma sadica:

> "Puoi **alzare al massimo `k` interruttori**,⁡⁠ ‍⁡ e collezionare solo i numeri che hanno ai loro lati **un interruttore alto e uno basso**. Se entrambi sono abbassati o entrambi alzati… niente punto."

Franchino capisce che non è questione di forza, ma di **strategia**: deve scegliere **quali interruttori alzare** per ottenere la **somma massima possibile** di questi numeri… e far girare la manopola quanto più possibile **in senso orario**, così da sbloccare la maniglia e uscire.

---

### **Input**

- Una lista `L`⁡⁠ ‍⁢ di `n-1` interi, rappresentanti i valori tra ciascuna coppia consecutiva di interruttori (`L[0]` è tra l’interruttore 0 e 1, `L[1]` tra 1 e 2, ecc.).
    
- Un intero positivo `k`: il **numero massimo di interruttori** che Franchino può alzare.
    

---

### **Output**

- Un intero: la **somma massima raggiungibile** dei valori collezionati rispettando le regole (massimo `k` interruttori alzati, e solo valori con estremi alternati basso/alto).
    

---

Franchino non ha tempo da perdere. Se sbaglia a scegliere gli interruttori, resta chiuso dentro fino alla sessione invernale.  
Aiutalo a **far girare la manopola quanto più possibile verso la libertà**!

| [**<**](../08/README.md) | [**Home**](../../README.md) | [**>**](../10/README.md) |
| :----------------------: | :-------------------------: | :----------------------: |