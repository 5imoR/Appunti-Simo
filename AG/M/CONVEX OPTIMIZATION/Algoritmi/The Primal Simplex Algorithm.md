#CO-L6
# Primal Simplex
L'idea dietro questo algoritmo è:
- Si parte da una feasible base $B$ del problema lineare
- Ci si sposta sulle basi adiacenti(o vertici) finche non raggiungiamo una optimal basis
	Per spostarci di base simette una colonna a 0 e se ne aggiunge un altre con costo migliore, si rivede più avanti
![[PrimalSimplex|500]]
 [[Convex Set#Global optimality theorem|Essendo convesso se trovi un minimo locale è un minimo globale]]

Per formalizzare l'algorimo serve trovare:
- come riconoscere una base ottimale (optimality conditions)
- come muoverci su una base adiacente migliore

## Optimality conditions
Dalla [[Linear Programming#Bases|definizione di base]] possiamo scrivere l'object function $z$:
$$
\begin{align}
z&=c_B^Tx_B+c_R^Tx_R\\
&=\underbrace{c_B^TB^{-1}}_{\pi^T}b+\underbrace{(c_R^T-c_B^TB^{-1}R)}_{d_j}x_R\\
&=\underbrace{\pi^Tb}_{costant}+\underbrace{d_jx_R}_{\text{lin. fun.}}
\end{align}
$$
Quindi ora l'objective function è espressa come un termine costante più una funzione lineare delle variabili non appartenenti alla base
$\pi^T=c_B^TB^{-1}$ è detto *vector of multiplierism* e permette la definizione del coefficente $d_j=c_R^T-\pi^TR$ chiamato *reduced cost*.
- Il reduced cost di variabili appartenenti alla base è sempre $0$.
- Il reduced cost di variabili non appartenenti alla base  da un *optimality condition* per la base corrente

Dato che $z= costante+d_jx_R$ si può vedere che $z$ cresce o diminuisce se $d_j > o < 0$ . 

Per capire il concetto:
$z=\pi^Tb+\sum_{j\in N}d_jx_j$  dove:
- $d_j$ sono tutte le possibili direzioni che possiamo prendere
- $x_j$ è a 0 a meno che non decido di seguire quella direzione
- $\pi^Tb$  è la base attuale
![[spostamentobasi|300]]

Possiamo concludere che se $d_j\geq0\quad\forall j\in \mathcal R$  non c'è modo di ridurre $z$ e quindi la base in cui ci troviamo è ottima

## Finding a better basis
Se la base corrente non soddisfa l'*optimality condition* allora esiste una variabile $x_q$ non appartenente alla base  con un reduced cost negativo $d_q<0$. 
Possiamo quindi aumentare $x_q$  finchè
	Più è grande $x_q$ più piccola sarà $z$ e quindi migliore
- continuiamo a soddisfare $Bx_B+Rx_R=b$
- le variabili della base sono non negative

Chiamiamo $t\geq0$ il valore di $x_q$. Sapendo che tutte le variabili non appartenenti alla base rimangono a 0 possiamo scrivere:
$$
Bx_B(t)+tA_q=b
$$
$$
\begin{align}
x_B(t)&=B^{-1}b-tb^{-1}A_q\\
&=\beta-t\alpha_q
\end{align}
$$
dove:
- $\beta=B^{-1}b$
- $\alpha_q=B^{-1}A_q$ 
### Quanto può aumentare?
Volendo mantenere la fattibilità delle variabili della base serve che:
$$x_B^i(t)=\beta_i-t\alpha_q^i\geq 0$$
#### Ratio test
Dato:$$\mathcal I =\{i\in\set{1,\dots,m}|x_q^i>0\}$$
possiamo calcolare il massimo valore di $t$ come:
$$
\theta=\frac {\beta_p}{\alpha_q^p}=\min_{i\in\mathcal I}\set {\frac {\beta_i}{\alpha_q^i}}
$$
La p-esima variabile è la *blocking variable* ed $\alpha_q^p$ è detto *pivot element*.
Per $t=\theta$ la blocking variable diventa $0$ quindi possiamo sostituirla con $x_q$ andando ad ottenere una nuova base
![[basispostate|700]]
Se $\mathcal I=\emptyset$ vuol dire che il problema è unbounded e che possiamo aumentare quanto vogliamo $x_q$ 
Se c'è una base degenerata il ratio test può dare 0 di conseguenza c'è il rischio di cambiare base ma rimanere sullo stesso vertice rischiando a sua volta di creare un loop. Queste sono chiamate *degenerate simplex interations* 