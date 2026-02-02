#CO-L18-1
Un esempio può essere:
$$
\begin {cases}
\min x^2+y^2\\
x\ge 1
\end{cases}
$$
![[wrong sol|300]]
C'è il rischio di avanzare troppo ed uscire dalla feasible region.
Si può pensare come soluzione di ripetere il passaggio che ci fa uscire andando a diminuire la step size ma questo non ci porterebbe al minimo.
La soluzione corretta è: quando si esce dalla feasible region si proitetta il punto per renderlo valido.
![[sol]]

![[Normal Cones#Definition [Normal Cones]]

![[Normal Cone Theorem#Theorem 6.1]]

![[Projections#Definition [Projection]]

### Proposition \[Minimum Principle]
Per ogni $x\in C$ abbiamo:
$$
(y-P_C(y))^T(x-P_C(y))\le 0
$$
#### Proof
E' una conseguenza diretta del teorema [[Normal Cone Theorem]] 
Scegliendo $f(z)=\frac 12||y-z||^2_2$ abbiamo  $\nabla f(z)=-(y-z)=(z-y)$  quindi $P_C(y)$ è ottimo se:
$$
(P_C(y)-y)^T(x-P_C(y)) \ge 0 \quad \forall x\in C
$$
C'è è esattamente la condizione che volevamo provare
![[Drawing 2025-12-09 18.28.09.excalidraw|200]]
### Proposition
Qualunque proiezione è una contrazione
$$
||P_C(a)-P_C(b)||\le||a-b||\quad \forall a,b\in \mathbb R^n
$$
#### Proof 
Da Minimum principle abbiamo 
$$
\begin{align}
(a-P_C(a))^T(x-P_C(a))\le0\qquad \forall x\in C\\
(b-P_C(a))^T(x-P_C(b))\le 0\qquad \forall x\in C
\end{align}
$$
Se possiamo scegliere $x=P_C(b)$ nella prima equazione e $x=P_C(a)$ nella seconda andando a sommarle si ottiene:
$$
[(b-a)+(P_C(a)-P_C(b))]^T(P_C(a)-P_C(b))\le 0
$$
Applicando [[Prodotti scalari#Teorema di Cauchy-Schwarz|Cauchy-Schwartz]] inequality e semplificando si ottiene:
$$
\begin{align}
||P_C(a)-P_C(b)||^2&\le (a-b)^T\ (P_C(a)-P_C(b))\\
&\le||a-b||\ ||P_C(a) - P_C(b)||
\end{align}
$$

## Projected Gradient
Questo è utile solo se il calcolo della proiezione non è costoso $O(n)$.
L'iterazione del [[UNB Gradient Descent|GD]]  è:
$$
x^{k+1}=x^k-t_k\nabla f(x^k)
$$
Per la [[Descent Lemma]] possiamo minimizzare l'approssimazione quadratica:
$$
x^{k+1}=\arg\min_{v\in\mathbb R^n} \set{f(x^k)+\nabla f(x^k)^T(v-x^k)+\frac 1{2t_k}||v-x^k||^2}
$$
Andiamo a sostituire $v\in\mathbb R^n$ con $v\in C$  e si arriva ad avere, [[ProjGrad.pdf#page=4|tramite passaggi]],
$$
x^{k+1} =\arg\min_{v\in\mathbb C} \left\{\frac 12||v-\underbrace{(x^k-t_k\nabla f(x^k))}_\text{solito $x^{k+1}$}||^2\right\}
$$
Quindi otteniamo:
$$x^{k+1}=P_C(x^k-t_k\nabla f(x^k))$$ Alcuni esempi in cui si può fare:
- $x\ge 0$ $x_j=\max\set {x_j,0}\ j=1\dots n$   
- $l\le x\le \mu$                                         bounded box
- $\sum_{x\ge 0}x_j=1$ 
- $a^Tx\le b$   oppure   $a^Tx=b$             un singolo linear constraint
- $||x||_p\le b$   oppure $||x||_p\le y$           norm balls or cones

### Convergence
Lo strumento necessari per studiare la convergenza è il gradient mapping.
### Definition 6.3
Dato un set convesso e chiuso $C\neq \emptyset$  ed una funzione differenziabile $f$ definiamo il gradient mapping come la funzione $G_\alpha:\mathbb R^n\to \mathbb R^n$ parametrizzata per $\alpha >0$ :
$$
G_\alpha(x)=\frac 1\alpha(x-{\color{orange}P_C({\color{lightgreen}x-\alpha\nabla f(x)})})
$$
$\textcolor{lightgreen}{■}$ calcolo del punto sucessivo con una step size $\alpha$
$\textcolor{orange}{■}$ faccio la proiezione del punto trovato su $C$ 
${■}$ calcolo la direzione nella quale ci siamo effettivamente mossi assumendo la stessa step size

Il gradient mapping ci permette di scrivere il projected gradient con una regola di aggiornamento molto simile a quella del GD
$$
x^{k+1}=x^k-t_kG_{t_k}(x^k)
$$
### Proposition 6.3
Simile al GD:

$x^*$ è ottimo $\iff G_\alpha(x^*)=0$ 

#### Proof
[[ProjGrad.pdf#page=5]] 

### Proposition 6.4
Con una step size costante $tk=\frac 1M$  la norma del gradient mapping ci da un progresso assicurato
$$
f(x^{k+1})\le f(x^k)-\frac 1{2M}||G_{1/M}(x^k)||^2
$$
#### Proof
[[ProjGrad.pdf#page=6]]

###
Ora possiamo provare gli stessi risultati della convergenza come nel gradient descent ovvero:
- error rate $\displaystyle O(\frac 1\varepsilon)$ nel caso convesso
- error rate $\displaystyle O(log \frac 1\varepsilon)$ nel caso strongly convex/PL case