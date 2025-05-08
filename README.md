# Hackathon-Tor-Vergata-2025

# Introduzione 

>Franchino quest'anno si è laureato, 

>a dir poco è stato molto fortunato, 

>delle lezioni si è sempre dimenticato, 

>ma agli esami il risultato a casa l'ha sempre portato. 

>Adesso in magistrale si è segnato, 

>e prevediamo che pagherà un conto salato... 

Nello specifico: Franchino, uno studente di informatica dell'università di Tor Vergata, è fresco di laurea triennale. La sua decisione è stata quella di continuare a mettere il passamontagna durante gli esami anche in magistrale, in cui però non avrà vita facile. 
ChatGPT, Gemini AI, Copilot &Co iniziano a vacillare dinanzi agli argomenti e ai problemi che vengono posti dinanzi a Franchino durante la magistrale: la probabilità di errare è più alta con argomenti complessi, e per lui leggere gli appunti che gli passano i colleghi gli comportano la stessa difficoltà di comprensione che avrebbe un dipendente delle poste davanti allo SPID.. 

Così, la comfort zone di Franchino al momento è ricordare i tempi passati in triennale, in cui tra una pausa sigaretta ed una chiacchierata sui nuovi aggiornamenti di Minecraft, magicamente si trovava qualche CFU in più sul suo Delphi, magari anche con accanto un 26 o un 28. Rivivi le avventure di Franchino in triennale, come se fossi accanto a lui, aiutandolo a studiare veramente gli argomenti e a svolgere correttamente gli esercizi ed i problemi che gli si presentavano davanti. 
# Istruzioni 

Sono stati forniti 11 problemi algoritmici, numerati da 0 a 10, che dovrete risolvere. Ad ogni problema è associato un livello di difficoltà, espresso in fiamme 🔥. Più fiamme indicano una maggiore difficoltà, da un minimo di 1 a un massimo di 6. Dovrete scrivere un programma in Python che risolva il problema assegnato, seguendo le specifiche fornite. Ad ogni problema risolto vi verrà assegnato un punteggio che dipenderà da: 
- Il numero di test superati; 
- Le performance della vostra soluzione; 
- La complessità della vostra soluzione. 

Alla fine dell'evento, il team con il punteggio più alto sarà dichiarato vincitore di questa edizione dell' Hackathon Tor Vergata 2025! 

Come primo passo dovrete clonare la repository dell'evento sul vostro computer, utilizzando il comando:

```bash 
git clone https://github.com/Lab25A-CS/Hackathon-Tor-Vergata-2025.git
```

Se siete utenti Windows (🐣) o avete timore di usare il terminale, potete scaricare un file .zip di questa repository, premendo i bottoni `Code->Download ZIP`. Una volta clonata la repository, troverete le tracce dei problemi nelle rispettive cartelle `problemi/<numero problema>`.

Ogni cartella contiene un file `README.md` che descrive il problema da risolvere, i vincoli e i dettagli dell'input e dell'output. 
Per ogni problema è fornito un file .py nel path `soluzioni/problema <numero problema>.py` all'interno del quale potrete trovare una funzione `solve`. Il vostro compito è quello di implementare la funzione '`solve`' in modo che risolva il problema relativo al file. Per esempio, se volete risolvere il problema 0, dovrete per prima cosa aprire il file `soluzioni/problema0.py`. Al suo interno troverete uno scheletro della funzione `solve` che dovrete implementare.

```python 
class Solution:

    # ...

    @staticmethod
    def solve(n: int) -> int:
        """
        Scrivi qui la tua soluzione
        """
        pass

    # ...
```

Leggendo la *firma* della funzione `solve` potrete capire quali sono i parametri in input e il loro tipo, e qual è il tipo di ritorno della funzione. In questo caso la funzione `solve` prende in input un intero $n$ e restituisce un intero. All'interno del file python ci sono molti altri metodi e funzioni, i quali ***NON*** devono essere modificate per nessuno motivo. Questi metodi sono utili per il corretto funzionamento dei test che valuteranno le vostre soluzioni, e qualsiasi vostro tentativo di modifica verrà rilevato! Una volta implementata la funzione `solve`, potrete testare la vostra soluzione eseguendo il file `run.py` presente nella root del progetto.

Dovrete eseguire i seguenti comandi da terminale:
```bash 
# Esegui TUTTI i test 
python3 run.py 
# Esegui solo i test per un problema specifico, per esempio il problema 3 
python3 run.py -t 3 python3 run.py --test 3 
```

Il programma `run.py` esegue una serie di test basati su input ed output pre-calcolati, e vi darà un resoconto di quanti test sono stati superati e quanti no, qual è il punteggio ottenuto e quanto tempo è stato impiegato per eseguire i test. Per ogni istanza di test superata, otterrete un punteggio variabile in base alla complessità del problema e alla performance della vostra soluzione. Il punteggio totale sarà la somma dei punteggi ottenuti per ogni test superato. 

Attenzione: ogni problema ha un *tempo limite* entro il quale la vostra soluzione deve restituire un risultato. Se il tempo limite viene superato, il test verrà considerato fallito e non otterrete alcun punteggio per quel test. 

Per la consegna dei problemi, dovrete comprimere le vostre soluzioni all'interno di un file zip denominato `<NOMETEAM>.zip` ed inviarle via e-mail all'indirizzo `info.lab25a@gmail.com`. I file inviati di diverso nome/formato non verranno presi in considerazione.

***Buon divertimento!*** 

# Problemi


- [Problema 0](problemi/00/README.md) 🔥
- [Problema 1](problemi/01/README.md) 🔥🔥
- [Problema 2](problemi/02/README.md) 🔥🔥
- [Problema 3](problemi/03/README.md) 🔥🔥🔥
- [Problema 4](problemi/04/README.md) 🔥🔥🔥
- [Problema 5](problemi/05/README.md) 🔥🔥🔥🔥
- [Problema 6](problemi/06/README.md) 🔥🔥🔥
- [Problema 7](problemi/07/README.md) 🔥🔥🔥🔥
- [Problema 8](problemi/08/README.md) 🔥🔥🔥🔥🔥
- [Problema 9](problemi/09/README.md) 🔥🔥🔥🔥🔥
- [Problema 10](problemi/10/README.md) 🔥🔥🔥🔥🔥🔥
