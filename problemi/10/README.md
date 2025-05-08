# Problema 10 (*Franchino e l'arte della selezione strategica*)
#### Difficoltà: 🔥🔥🔥🔥🔥🔥
	Se lo fai sei uno forte

Questa⁠ ‍⁡⁠ ‍⁢⁠ ‍⁡⁠ ‍⁢⁠ ‍⁡ volta è⁡⁠ ‍⁡⁠ ‍⁢ diversa. Franchino si⁡⁢⁠ ‍⁡ trova alle⁡⁠ ‍⁢ battute⁢⁠ ‍⁢ finali del corso, ma ha toccato il fondo (accademicamente parlando), e si è finalmente deciso a **studiare⁡⁠ ‍⁢ con criterio**.

Il suo obiettivo: passare⁢⁠ ‍⁢ l’esame⁡ più⁢⁠ ‍⁢ ostico della sessione, ovvero Fondamenti di Informatica.

Il suo problema: il⁡⁠ ‍⁡ materiale è distribuito in una quantità **assurda di capitoli**, ciascuno con titoli del tipo "0", "1", "2", come se⁢⁠ ‍⁢ li avesse scritti un ingegnere… o un compilatore.

Ogni⁡⁠ ‍⁡ capitolo `Sᵢ` copre **almeno un argomento**, ma alcuni⁢⁠ ‍⁢ coprono più⁡⁠ ‍⁡⁠ ‍⁢ argomenti contemporaneamente. Tuttavia, ogni capitolo richiede **tempo**, e Franchino ha giusto il tempo di scaldare la sedia – ma non troppo.

È quindi⁡⁠ ‍⁢ fondamentale scegliere⁢⁠ ‍⁡ con cura⁡⁠ ‍⁡ quali capitoli studiare, in modo da coprire **tutti gli argomenti richiesti** per l’esame, ma impiegando **il minor tempo complessivo possibile**.

Sta⁢⁠ ‍⁢ a te costruirgli il **piano di studio perfetto**, scegliendo esattamente **quali capitoli leggere** per coprire ogni argomento, minimizzando il tempo speso.

---

### **Input**

- Un insieme di argomenti `U = {a₁, a₂, ..., aₙ}` che Franchino deve assolutamente conoscere per passare l’esame.
    
- Un insieme `S = {S₀, S₁, ..., Sₘ₋₁}` di **capitoli**, ognuno identificato da un numero naturale `i`, tale che:
    
    - ogni `Sᵢ` è un sottoinsieme non vuoto di `U` (cioè `|Sᵢ| ≥ 1`),
        
    - una funzione `w(Sᵢ) ∈ ℤ` indica il **tempo necessario** per studiare il capitolo.
        
### **Output**

- Una lista `O = {i₁, i₂, ..., iₖ}` di **interi**, corrispondenti ai nomi (indici) dei capitoli scelti, tale che:
    
    - la **unione degli argomenti** coperti dai `Sᵢ` selezionati in `O` sia esattamente `U`,
        
    - la **somma dei tempi di studio** `∑ w(Sᵢ)` per `i ∈ O` sia **minima**.
        

---

Franchino ha capito una cosa: il segreto dell’università non è sapere tutto, ma sapere **cosa studiare e quanto ti costa farlo**.  
Se riesce a risolvere questo problema… magari lo scrive anche nella sua tesi.

**P.S**: La soluzione non deve per forza essere ottima, va bene anche una soluzione approssimata.

| [**<**](../09/README.md) | [**Home**](../../README.md) |
| :----------------------: | :-------------------------: |
