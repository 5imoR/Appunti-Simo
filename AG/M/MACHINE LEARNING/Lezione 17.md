#ML-L17[[Lezione 16]]
### STG for Perceptron
Partiamo con:
- $\set{0,1}$ classification
- loss function  $l(w,z)=\begin{cases}-yw^Tx&yw^Tx<0\\0&yw^Tx>0\end{cases}$
- $L_S(w)=\frac 1m\sum_{i=1}^m l(w,z_i)$ 
Ad ogni terazione si fa:
$$w^{(k+1)}=w^{(k)}-\gamma_k\nabla_wL_{B^{(k)}}(w)\big|_{w=w^{(k)}}$$
con:
- $L_{B^{(k)}}(w)=\frac 1 {|B^{(k)}|}\sum_{i\in B^{(k)}}l((w,z_i)\qquad B^{(k)}\subset\set{1,\dots,m}$ 

##### Caso speciale $B^{(k)}=1$ 
Si prende un valore per volta
$i\in\set{1\dots m}\quad B=\set{i}$ 

Se $\gamma_k$ (step size) è pari a $1$ allora sarebbe identico al perceptron[[Lezione 16#Esempio perceptron]]
![[SGDperc]]

Sull'origine c'è un punto non diferenziabile, noi lo consideriamo con gradiente di $-1$ $\nabla_wl=\begin{cases}-yx&\text{if }yw^Tx\le0\\0&\text{otherwise}\end{cases}$

$$
\begin{align}
w^{(k+1)}&=w^{(k)}-\gamma_k\nabla_wl(w,z_i)\\
&=\begin{cases}
w^{(k)}+\gamma_k \ y_ix_i\quad &\text{if } y_i(w^{(k)})^Tx_i\le 0\\
w^{(k)}&\text{otherwise}
\end{cases}
\end{align}
$$
Date le condizioni tali che:
$$P[L_D(\hat h_s>\min_h\in H\ L_D(h)+\epsilon]<\delta$$
Fin'ora se non siamo in grado di soddisfare questa equazione, ci è necessario andare a richiedere un maggiore numero di dati.
Un alternativa può essere andare a cambiare objective function

### Overfitting, Stability and Regularization
- Overfitting: se ci sono troppi dati diventa troppo sensibile al dataset
- Stability: Come si comporta il nostro sistema se introduciamo delle perturbazioni ai nostri dati
- Set di metodi per modificare questo learning alghoritm aggiungendo un termine al costo e rendendo il modello stabile.

Definiamo:
- $\epsilon_\text{app}=\min L_D(h)+\epsilon$    (approximation) ed è la migliore linear rule
- $\epsilon_\text{est}=L_D(\hat h_s)-\epsilon_\text{app}$      (estimation) stima dell'errore
![[epsilonsauce|1200]]
$$E[L_D(\hat h_s)=E[\epsilon_\text{est}(H)]+E[\epsilon_\text{app}(H)]$$
$|H^*|$ è l' $m$ migliore ovvero il numero di elementi nel nostro dataset(?)


$$\Large\underbrace{L_D(\hat h_s)}_\text{generalization error}=\underbrace{L_D(\hat h_s)-L_S(\hat h_s)}_\text{generalization gap}+\underbrace{L_S(\hat h_s)}_\text{empirical risk}$$ 
![[underoverfit|700]]
Non vogliamo ne overfitting ne underfitting. Possiamo restare solo in mezzo.
Quello che succede a destra è per $m$ molto elevate, non viene coperto da questo corso.

### Come evitiamo l'overfitting?
- Definiamo una notazione di stabilità dei learning algorithm
- Un algoritmo stabile non va in overfit
- Introdiciamo strumenti per garantire la stabilità

