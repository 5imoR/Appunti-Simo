## $l_1$- Regularization
Può essere usata per fare una selezione sulle variabili

$P(w)=||w||_1=\sum_{i=1}^d|w_i|$  è chiamato *penalty term*

Si vuole sapere quali $[x]_i$ sono utili per predirre.
Fin ora usavamo i confidence intervals per rispondere a questa domanda.
Ora usiamo un regularization term in gradop di mandare a zero i termini $w_i$ che corrispondono alle feature irrilevanti.
#### Example linear prediction
$h(x)=w^Tx=\sum^d_{i=1}w_i[x]_i$  dove $[x]_i$ non è utile se  $w_i=0$

### Therminology
Diciamo che un vettore $w$ è *sparse* se alcuni valori dei suoi componenti sono a zero
$w=[0\ 1\ 0\ 0\ 3\ 0]^T$ 
### Definition
$l_1$-Reg. per linear least squares with quadratic loss è chiamata *Lasso*
Lasso=$\hat w_L=\arg\min_{w\in\mathbb R^d}\frac 1m ||Y-Xw||^2+\lambda||w||_1$ 
- E' convesso
- $\lambda$ è detto lagrange parameter/multiplier

La Lasso solution può essere sparsa.

Si può aggiungere un vincolo del tipo: $||w||_1\le k$ ottenendo:
$$
\hat w_L=\arg\min_{\substack{w\in\mathbb R^d\\||w||_1\le k}}\frac 1m ||Y-Xw||^2+\lambda||w||_1\longrightarrow\hat w_L=\arg\min_{w\in\mathbb R^d}\frac 1m ||Y-Xw||^2+\lambda(||w||_1-k)
$$
### Remark
Questo  è un caso particolare di 
$$\min_{s.t.\ f(w)\le 0}J(w)\Rightarrow\min J(w)+\lambda f(w)$$
Per un $\lambda\ge 0$  che dipende da $k$.

### Remark
$\frac 1m||Y-Xw||^2$ è convesso
Con:
- $w\in \mathbb R^2$ 
- $|w_1|+|w_2|\le k$ 
![[remarkconvex]]
Passare dalla forma con i costraint alla versione di lagrange è utile dal punto di vista computazionale.
### Case 1
Il punto di minimo della funzione è compreso dai vincoli, quello è il nostro punto di minimo.
Si ha la soluzione con $\lambda =0$ 
![[Case1]]

### Case 2
Il minimo è al di fuori dei vincoli, il minimo è il vertice $\hat w_1= 0\ \hat w_2\ne 0$.
Questo è un punto non diferenziabile.

Quando ci troviamo su un vertice anche in presenza di piccole perturbazioni il punto di minimo rimane invariato
![[Case 2]]
### Case 3
Il minimo è al di fuori dei vincoli,il minimo è la tangente $\hat w_1\ne 0\ \hat w_2\ne 0$.
Questo è un punto differenziabile e tangente alla level curve
![[Case 3]]
### Case  R.R.
$$\hat w_L=\arg\min_{\substack{w\in\mathbb R^d\\||w||^2\le k}}{\color{orange}\frac 1m ||Y-Xw||^2}+\lambda||w||^2$$
![[Case RR]]
Quello nel disegno è un caso sparse, che scompare alla minima perturbazione. La probabilità di essere in uno dei casi sparsi, in questo caso è statisticamente nulla.


## Domande
$$\hat w_L=\arg\min_{w\in\mathbb R^d}L_S(w)+\lambda||w||_1$$
- Come scegliamo $\lambda$?
	K-cross validation
- Come cambia la soluzione in funzione di $\lambda$?

![[Drawing 2025-11-25 16.17.03.excalidraw|700]]
Man mano che si aumenta il valore di $\lambda$ più variabili diventano irrilevanti.
Le linee tratteggiate sono nel caso della Ridge Regression
Andando ad utilizzare il $\hat \lambda_{opt}$ della lezione precedente, si possono trovare le variabili utili in quel momento. E' presente un problema: ti sei liberato dei valori inutili MA sei andato a ridurre anche i valori che ti interessano, serve quindi trovare il giusto tradeoff.
	Se stai pensado di fare il Lasso, trovare i parametri inutili per il tuo lambda ed andare ad usare i paramentri originali non c'è la certezza che quello che trovi sia effettivamente migliore del caso iniziale.

### Reweighted $l_1$  NON RICHIESTO
Ogni feature ha il suo peso $\gamma_i$
$$\lambda ||w||_1\to\sum_i\frac {|w_i|}{\gamma_i}$$
### Towards Non Linear Models

First step $h(x)=w^Tx\longrightarrow h(x)=w^T$