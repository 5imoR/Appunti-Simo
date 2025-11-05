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
![[Drawing 2025-11-05 20.10.19.excalidraw]]
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

### MIP representability
Un set $S\subseteq \mathbb R^n$  è MIP-rapresentable se esiste un set di constraint nella forma:
$$
P=
\begin{cases}
Ax+Bu+Dy\le b\\
x\in \mathbb R^n, u\in \mathbb R^m, y_k\in \set{0,1}\forall k
\end{cases}
$$
tale che la sua projection del suo feasible set su $x$ è $S$ 