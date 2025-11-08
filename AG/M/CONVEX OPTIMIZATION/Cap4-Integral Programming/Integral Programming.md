 #CO-L10
# Integral Programming
$$
\begin{cases}
\min/\max c^Tx=\sum_{j=1}^n c_jx_j&\text{lineare}\\
a^T_ix \sim b_i\quad\qquad i=1\dots m\quad \sim\in\{\leq, =, \geq\}&\text{lineare}\\
l_j\leq x_j\leq u_j\qquad l_j\in \mathbb{R}\cup\{-\infty\}\quad u_j\in \mathbb{R}\cup\{+\infty\}&\text{lineare}\\
x_j \in \mathbb Z \qquad\forall J\subseteq\set{1,\dots m} &\substack{\text{alcune variabili }\\\text{discrete}}
\end{cases}
$$
Permette di usare valori discreti permettendo di avere varibili utilizzabili come vero e falso o simili

###
![[integral prob]]
Se tutti i vertici fossero int potrebbe essere trattato come un [[Linear Programming|LP]] 


Questo ci permette di risolvere:
#### Binary problems
#### Discrete values problems
$$
\begin{align}
&y=\sum^k_{i=1}v_ix_i\\
&\sum^k_{i=1}x_i=1\qquad x_i\in \set {0, 1}\qquad \forall i\in\{1\dots k\}
\end{align}
$$

#### Fixed cost problem

$$
z=c(x)=
\begin{cases}
ax+b\quad & \text{if }x>0\\
0 &\text{if }x=0
\end{cases}
$$
Per ragioni tecniche il sistema avrà bisogno di avere $x\in[\varepsilon, U]$. Così facendo otteniamo:
$$y=
\begin{cases}
1\quad & \text{if }\varepsilon\le x\le U\\
0 &\text{if }x=0
\end{cases}$$
ed otteniamo il MIP model:
$$
\begin{cases}
z=ax+by\\
\varepsilon y\le x\le Uy\\
y\in\set{0,1}
\end{cases}
$$


### Disjunction
possono capitare casi in cui vogliamo avere un alternativa oppure in altra. Un esempio può essere l'organizzazione di lavori da fare, un lavoro non può iniziare se ne sta venendo effettuato un altro.
Prendiamo due vincoli lineari:
- $a_1^Tx\le b_1$
- $a_2^Tx\le b_2$
si vuole poter scrivere:
$$- a_1^Tx\le b_1\ \lor\  a_2^Tx\le b_2$$
Di nuovo per ragioni tecniche assumiamo che i domini delle variabili invonte siano limitati
- $l\le x\le u\qquad l\in\mathbb R^n\qquad u\in\mathbb R^n$ 
Il trucco è aggiungere una variabile binaria ad entrambe le parti esprimendo quale condizione deve essere presa in considerazione. Il MIP model sarebbe:
$$
\begin{cases}
a_1^Tx\le b_1+ M(1-y_1)\\
a_2^Tx\le b_2+ M(1-y_2)\\
y_1+y_2\ge 1
\\
l\le x\le u\\
y\in\set{0,1}
\end{cases}
$$
- $M$ è un numero molto grande che serve a "disattivare" il vincolo quando l'$y$ corrispondente è a $0$ 
	Se x va da 5 a 10 e noi mettiamo M=20 il vincolo non ha più senso dato che x non poteva già superare il 10

### 
![[MIP representability#MIP representability]]

#### Restriction
#CO-L11 
Consideriamo
- $P$ un optimization problem
- $F(P)$ il set delle feasible solution
$Q$ è la restriction di $P$ se $F(Q)\subset F(P)$ e si ottiene andando ad aggiungere vincoli aggiuntivi
![[restriction|200]]
- Quando $F(Q)=\emptyset$  non possiamo dedurre niente
- Se trovo una soluzione ottima in $F(Q)$ allora è una feasible solution di $P$ e quindi  la soluzione ottima di $P$ è migliore o uguale a questa

#### Search
Dato un problema $P$ fare un "search" significa andare a risolvere una sequenza di restriction $Q_1\dots Q_m$.  
L'idea è che andando a ridurre il "solution space" il problema di ottimizzazione diventa molto più semplice![[search|200]]

Si parla di *exaustive search* se 
$$\bigcup^k_{i=1}F(Q_i)=F(P)$$
- questo deve coprire esattamente $F(P)$ (ne più grande ne più piccolo)
- si vuole evitare di coprire una zona 2 volte dato che sarebbe uno spreco di risorse
#### Relaxation
Consideriamo
- $P$ un optimization problem
- $F(P)$ il set delle feasible solution
$R$ è la relaxation di $P$ se si ottiene andando a: (e/o)
- rimuovere dei vincoli      $F(P\subseteq)F(R)$
- sostituire l'objective function $f(x)$ con una sua approssimazione $g(x)$ $g(x)\le f(x)\ \forall x\in F(P)$
	$g(x)$ deve essere un lower-bound della funzione iniziale
![[relaxation|300]]
##### Proprietà
- $F(R)=\emptyset\Rightarrow F(P)=\emptyset$ 
- $x^*$ è una soluzione ottima per  $R\Rightarrow g(x^*)$ è un lower bound di $P$
- $x^*$ è una soluzione ottima per $R$ se $x^*\in F(P)$ allora è una soluzione ottima per $P$ 
## Algoritmi

![[INT Generate and Test algorithm#Generate and Test]]

**Tree search**
Utile perche permette di dividere in problemi più piccoli quello iniziale.
- bisogna guardare i valori della frontiera
- se non è fatto bene e si arriva ad avere che ogni nodo è una soluzione, è peggio del Generate and Test

