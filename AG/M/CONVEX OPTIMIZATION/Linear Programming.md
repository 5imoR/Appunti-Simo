#CO-L5

## Definition
E' un caso particolare di [[CONVEX OPTIMIZATION#Convex Programming|convex programming]]  che può essere scritto come:
$$
\begin{cases}
&\min c^Tx\\
&a^T_ix \sim b_i\quad\qquad i=1\dots m\quad \sim\in\{\leq, =, \geq\}&\text{per forza lineare}\\
&l_j\leq x_j\leq u_j\qquad l_j\in \mathbb{R}\cup\{-\infty\}\quad u_j\in \mathbb{R}\cup\{+\infty\}&\text{lineare}
\end{cases}
$$
Non sono ammessi $<$ e $>$  ed essendo che si trattano funzioni lineare è possibile, per cercare il massimo, invertire la funzione dato che rimane cominque lineare.

###
Di per se non ha molti utilizzi ma può essere usato per risolvere altri tipo di problemi.

- linear equality$\rightarrow$ hyperplane
- lineaar inequality $\rightarrow$ halfspace
- fiesible region di un linear program è un polyhedron
	polyhedron è la versione unbounded di polytope.

### Definition Vertex
Un vertice è un punto del polyhedron che non può essere rappresentato come strict combination dei punti di $P$.
Data una lista di vertici si può ottenere il polyhedron unico
![[polyhedron|200]]

### Theorem (Minkowski Weyl)
Ogni punto del polytope può essere espresso come convex combination dei suoi vertici
	Questo non si applica ai polyhedron

In altre parole un polytope può essere descritto in due modi diversi:
- $H$: ovvero l'intersezione dei suoi linear constraint 
- $V$: dai suoi vertici

#### Corollary
Se il feasible set $P$ di un linear program è bounded e non empty allora esiste almeno un optimal vertex.

#### Proof
- $x_1\dots x_k$ i vertici
- $y\in P$ una feasible solution arbitraria
- $z^*=\min \{c^T x^i : i=1\dots k\}$ 

$$
\begin{align}
c^Ty&=c^T\left(\sum_{i=1}^k\lambda_ix^i\right)\\
&=\sum_{i=1}^k\lambda_i(c^Tx^i)\geq\sum_{i=1}^k\lambda_iz^*\\
\end{align}
$$
- $\sum_{i=1}^k\lambda_i$  è pari a $1$ dato che siamo in un caso particolare di *convex program*
$$
c^Ty\geq z^*
$$

## Standard form
$$
\begin{cases}
&\min c^Tx\\
&Ax=b\quad \text{non viene persa generalità}\\
&x\geq 0
\end{cases}
$$
- $a^Tx\geq b$ può essere riscritto come $a^Tx+s=b$ al costo di introdurre un variablie $s=b-a^Tx\geq 0$ 
- $x\geq g$ può essere visto come $x-g\geq 0$ 
- Una variabile $x_j$ che non ha limitazioni può essere espressa come due variabili non negative $x_j=x_j^+-x_j^-$   con $x_j^+,x_j^-\geq 0$

Possiamo inoltre dire che il numero di colonne è maggiore o uguale al numero di righe nella matrice.$m\leq n$
	Vuol dire che abbiamo più variabili che equazioni.
La matrice $A$ ha $rank(A)=m$

## Bases
Una basis è definita come il set di $m$ colonne lineari indipendenti
- $\mathcal B=\{k_1,\dots,k_m\}$ il set di colonne indipendenti
- $B$ la matrice formata dalle colonne della base

- $\mathcal R$ le colonne non presenti nella base
- $R$ la matrice formata dalle colonne di $\mathcal R$ 

Possiamo quindi riscrivere il problema come:
$$
\begin {align}
Ax&=b\\
Bx_B+Rx_R&=b\\
B^{-1}(Bx_B+Rx_R)&=B^{-1}b\\
x_B&=B^{-1}b-BRx_R
\end{align}
$$
Se $x_R =0$ si ottiene
- *basic solution*: $x_B=B^{-1}b$ 
- *basic feasible solution*: se viene anche rispettato il vincolo di non negatività

### Theorem Bases=Vertex
Un punto $x\in\mathbb R^n$ è il vertice di un non empty polyhedron
$$P=\{x|Ax=b,x\geq0\} \iff x \text{ è una b.f.s. del sistema } Ax=b$$
#### Proof
- $x$ è una b.f.s. associata ad una base $B$
	è un set di variabili(non vettori)
- possiamo fare permutazioni su $B$ per ottenere i valori positivi di $x$ sulle prime $k$ colonne 
$$
x=[x_1\dots x_k,0\dots 0]^T
$$
- dato che $k<m$  una variabile della base può essere 0. Quando questo succede si dice che la base è *degenerate* 
- 