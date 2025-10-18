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
Un vertice è un punto del polyhedron che non può essere rappresentato come strict convex combination dei punti di $P$.
Data una lista di vertici si può ottenere il polyhedron unico
![[polyhedron|200]]


 ### ![[Theorem (Minkowski Weyl)#Theorem (Minkowski Weyl)]]


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
- $\mathcal B=\{k_1,\dots,k_m\}$ il set di indici delle colonne indipendenti
- $B$ la matrice formata dalle colonne della base

- $\mathcal R$ il set di indici delle colonne dipendenti
- $R$ la matrice formata dalle colonne di $\mathcal R$ 

Possiamo quindi riscrivere il problema come:
$$
\begin {align}
Ax&=b\\
Bx_B+Rx_R&=b\\
B^{-1}(Bx_B+Rx_R)&=B^{-1}b\\
x_B&=B^{-1}b-B^{-1}Rx_R
\end{align}
$$
Se $x_R =0$ si ottiene
- *basic solution*: $x_B=B^{-1}b$ 
- *basic feasible solution*: se viene anche rispettato il vincolo di non negatività

![[Theorem basis= vertex#Theorem Bases=Vertex]]

**NOTA** Il rapporto tra basi e vertici non è $1:1$  dato che un vertice può essere rappresentato da più matrici diverse nel caso siano degenerate.

## ![[The Primal Simplex Algorithm#Primal Simplex]]
