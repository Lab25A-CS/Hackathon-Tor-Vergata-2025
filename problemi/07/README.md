# Problema 7 (**Franchino e la passione per TrainVergata**)
#### Difficoltà:🔥🔥🔥🔥

Dopo un paio d'anni di crisi nervose, portafogli vuoto e sigarette scroccate, finalmente si vedono un po' di soldi: Franchino ha finalmente trovato lavoro presso TrainVergata.
Non proprio nel campo della sicurezza informatica o dell’intelligenza artificiale, ma… **ai treni**. Meglio di niente.

La sua mansione? Gestire i **vagoni** che devono essere agganciati per formare un treno completo.  
Ogni vagone è rappresentato da una coppia $(n_i, n_{i+1})$, dove:

- $n_i$ è la **lunghezza** del vagone,
    
- $n_{i+1}$ è l’**energia elettrica** che trasmette al successivo.


Il problema è che ogni volta che attacca due vagoni adiacenti, l’azienda gli scala dal compenso un **costo di aggancio**, calcolato con questa formula maledetta:

$costo = n_i\cdot n_{i+1}\cdot n_{i+2}$

Franchino si accorge che, nonostante tutto, **quelle robe di algoritmi studiate alla triennale servono**, e che c’è un modo per attaccare i vagoni in un ordine tale da **spendere il meno possibile**.

Ma lui ha ancora la testa nel cloud, quindi tocca a te aiutarlo a **combinare i vagoni nel modo più economico possibile**, formando un unico super-treno.

---

### **Input**

- Una lista di  $m+1$ coppie di interi rappresentanti $m$ vagoni in ordine della forma:  
    $(n_0, n_1), (n_1, n_2), ..., (n_{m-1}, n_m)$
    dove $[n_0, n_1, ..., n_m]\in\mathbb Z\ge 0$.
    
	- Due vagoni adiacenti, come $(n_i, n_{i+1})$ e $(n_{i+1}, n_{i+2})$, possono essere combinati in un unico vagone $(n_i, n_{i+2})$.
    
	- Il **costo per combinare** due vagoni adiacenti è calcolato come: $$n_i\cdot n_{i+1}\cdot n_{i+2}$$
### **Output**

- Un intero: il **costo minimo** per combinare tutti i vagoni in un unico treno.