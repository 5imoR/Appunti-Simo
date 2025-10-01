#CO-L1
Come è strutturato un problema:
$$
P=
\begin{cases}
\text{min (or max) f(x)}\\
g_i(x)\leq b_i \quad i=1,...,m\\
x_j\in D_j\quad j=1,...,n
\end{cases}
$$
- Una soluzione è detta *feasible* se rispetta i *constraint* del problema.
- Il set di feasible solution è $F(P)$
- L'*optimal solution* $x^*$ è la soluzione migliore al problema e possono essercene più di una o nessuna
$$
x^*\in F(P)\quad f(x^*)\leq (x) \quad \forall x\in F(P)
$$
- L'obbiettivo è trovare  $x^*$ e dimostrare che è tale

Casi particolari di $F(P)$:
- infeasible: non ci sono soluzioni   $F(P)=\varnothing$ 
- unbounded: esiste sempre una soluzione migliore di quella che si sta valutando tramite un $x$ più piccolo
$$
\begin{cases}
min(x)\\
x\in\mathbb{R}
\end{cases}
$$
- $\color{orange}\text{boh}$:l'inverso di unbounded ovvero che all'aumentare di $x$ la soluzione migliora
$$
\begin{cases}
min(e^{-x})\\
x\geq0
\end{cases}
$$
Mettendo molti vincoli si va ad ottenere una soluzione che funziona perfettamente ma non ha utilizzi. Lo scopo di Convex Optimization è trovare l'equilibrio nella quantità dei vincoli.
---
## Linear Programming
$$
\begin{cases}
&min(c^Tx)=\sum_{j=1}^n c_jx_j&\text{per forza lineare}\\
&a^T_ix \sim b_i\quad\qquad i=1\dots m\quad \sim\in\{\leq, =, \geq\}&\text{per forza lineare}\\
&l_j\leq x_j\leq u_j\qquad l_j\in \mathbb{R}\cup\{-\infty\}\quad u_j\in \mathbb{R}\cup\{+\infty\}&\text{non possono esserci buchi}
\end{cases}
$$
#### Diet Problem
- $n$ tipi di cibi
- $c_j$ costo di ogni cibo
- $m$ tipo di cibo
- $b_i$ quantità minima di cibo
- $a_{ij}$ valori della tabella nutrizionale
- $x_j$ quantità di cibo nella dieta $\geq 0$ 
Trovare la dieta migliore con il costo minimo
$$
\begin{cases}
\min\sum_{j=1}^nc_j\ x_j\\
\sum_{j=1}^na_{ij}\ x_{j}\geq b_i\\
x_j\geq 0\quad j=1\dots n
\end{cases}
$$

## Integral Programming
E' identico all'linear programming ma con l'aggiunta di un nuovo vincolo:
$$
x_j\in\mathbb{Z} \quad \forall j \in J\subseteq\mathbb{N}
$$
questo permette la possibilità di usare gli int come $1$ e $0$ per dire vero o falso ed altro.
#### Knapsack Problem
- $n$ oggetti
- $p_j$ profitto di un oggetto
- $w_j$ peso di un oggetto
- $B$ capacità di un contenitore
- $x_j\begin{cases}1\ se\ scelto\\ 0\ altrimenti \end{cases}$
Trovare gli oggetti con profilo maggiore che stanno dentro al contenitore
$$
\begin{cases}
\max\sum_{j=1}^np_j\ x_j\\
\sum_{j=1}^nw_j\ x_{j}\leq B\\
x_j\in \{0,1\}\quad j=1\dots n
\end{cases}
$$
## Convex Programming(non so il nome)
$$
P=
\begin{cases}
\text{min (or max) f(x)}c_jx_j&\text{convex function}\\
g_i(x)\leq b_i \quad i=1,...,m&\text{convex function}\\
x_j\in D_j\quad j=1,...,n
\end{cases}
$$
Può essere risolto in un tempo convesso

#### Portfolio Optimization
- $n$ investimenti
- $u_j$ guadagno investimento
- $p$ obbiettivo
- $R\succeq0$  rischio -> matrice con la covarianza
- $0\leq x_j\leq 1$ % investita in $j$ rispetto alla quota massima investibile, non al budget

$$
\begin{cases}
\min x^T R_x=\sum_{ij}^n R_{ij}x_ix_j\\
\sum_{j=1}^n u_jx_j\geq p\\
0\leq x_j\leq 1
\end{cases}
$$

