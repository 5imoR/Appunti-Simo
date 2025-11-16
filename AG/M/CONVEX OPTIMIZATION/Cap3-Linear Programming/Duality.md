#CO-L8
Un problema di ottimizzazione $P$ è considerato un problema di ricerca, ovvero trovare la suluzione ottima $x^*$ 
Alternativamente lo stesso problema può essere interpretato come un inference problem ovvero trovare il miglior lowerbound possibile dell'oggetto
In [[Linear Programming]] ci permette di trovare una prova che dimostra che il nostro punto di minimo sia corretto. E' quindi utile sia dal lato teorico che pratico

Considerando un LP in standard form:
![[Linear Programming#Standard form#Problem]]
- Denotiamo con $P$ la feasible region definita dai vincoli $Ax=b, x\geq 0$ 
## Definition 
Dato un set $C\subset \mathbb R^n$ diciamo che una *linear inequality* $\alpha^Tx\geq \beta$ è valida per $C$ se è soddisfata per ogni punto in $C$.
$$\alpha^Tx\geq \beta\quad \forall x\in C$$

Il *dual point of view* consiste nel trovare il vincolo $Ax=b, x\geq 0$  definendo la feasible region $P$ del problema più stretta possibile. 
![[dual|300]]
Questo equivale a: $c^Tx\geq c_0 \forall x\in P$ possiamo quindi scriverlo come un problema di massimizzazione nella forma:
$$
\begin{cases}
\max c_0\\
c^Tx\geq c_0 \forall x\in P
\end{cases}
$$
Questo problema ha una singola variabile ed infiniti vincoli, uno per ogni punto di P.
Usando il [[Theorem (Minkowski Weyl)|Minkowski theorem]]  possiamo già semplificarlo notevolmente
$$
\begin{cases}
\max c_0\\
c^Tv^j\geq c_0\quad \forall v_j\ \text{vertex}\in P
\end{cases}
$$
Siamo passato ad avere un numero esponenziale di  vincoli. Abbiamo quindi bisogno di trovare una caratterizzazione differente dei vincoli validi di $P$ 


Si va a modificare il problema facendo modifiche su $Ax=b$ che la facciano rimanere valida, aggiungiamo un vettore di moltiplicatori$\rightarrow u^TAx=u^Tb$ 
Ora possiamo:
- sistituire $=$ con $\geq$ $\rightarrow u^TAx\geq u^Tb$
- ridurre il lato destro
- aumentare i coefficienti di $x$ a piacere dato che $x\geq 0$ 
Per mostrare che $\alpha^Tx\geq \beta$ è valida per $P$ serve trovare un vettore di moltiplicatori $u\in \mathbb R^m$ tale che:
$$\alpha^T\geq u^TA\quad u^Tb\geq \beta$$
![[Farka's Lemma#Theorem (Farka's Lemma)]]

Sia $x^*$ la soluzione ottimale computata dal [[LIN Primal Simplex Algorithm]] associato alla base $B$
Una volta partizionate le variabili in basic e non basic possiamo definire un vettore di moltiplicatori $u=\alpha_BB^{-1}$ che soddisfa 
- $\alpha^T\geq u^TA$  ovvero tutti i reduced cost $d_j$ sono positivi
- $u^Tb\geq \beta$ è ottenuta come: $\beta\leq z^*=\alpha^Tx=\alpha_B^TB^{-1}b=u^Tb$ 
![[Farka's Lemma#Corollary (Farka's Lemma)]] 
Non solo ha una dimensione polinomiale ma ha anche la stessa dimensione del LP originale con la matrice $A$ trasposta e l'objective e right-hand vectors scambiati di ruolo
![[Linear Programming#Standard form#Problem]]

## 
#CO-L9
$$
\begin{align}
&\text{Primal}&\text{Dual}\qquad\\
&\begin{cases}
\min c^Tx\\
Ax=b\\
x\geq 0
\end{cases}
&\begin{cases}
\max u^Tb\\
c^T\geq u^TA\\
u \text{ free}
\end{cases}
\end{align}
$$
### Weak duality
dati:
- $\bar x\in P$ 
- $\bar u \in D$
allora è sempre vero che:
$\bar u^T b\leq c^T\bar x$ 


### Strong duality
dati:
$x^*$ soluzione ottima
$u^*$ soluzione ottima
	comportano che ci sia un finite optimum
allra è sempre vero che:
$u^{*T}b=c^Tx^*$ 

###
| $\frac{\text{dual}}{\text{primal}}$ | unbouded               | optimal                | infisible               |
| ----------------------------------- | ---------------------- | ---------------------- | ----------------------- |
| unbounded                           | $\textcolor{RED}{■}$   | $\textcolor{RED}{■}$   | $\textcolor{green}{■}$  |
| optimal                             | $\textcolor{RED}{■}$   | $\textcolor{green}{■}$ | $\textcolor{RED}{■}$    |
| infeasible                          | $\textcolor{green}{■}$ | $\textcolor{RED}{■}$   | $\textcolor{orange}{■}$ |
$\textcolor{orange}{■}$ succede ma non è un caso importante




$$
\begin{cases}
\begin{cases}
Ax=b\\
x\geq 0
\end{cases} \quad\text{ primal fisibility}\\\\
u^TA\leq c^T\quad\text{ dual fisibility(equivale a dire che $d_j\geq 0$)}\\\\
u^Tb=c^Tx\quad\text{ optimality condition}
\end{cases}
$$
Possiamo riscrivere l'optimality condition come segue:
$$
u^Tb{\color{orange}=}u^TAx{\color {lightgreen}=}c^Tx
$$
- $\textcolor{orange}{■}$ :$u^T(Ax-b)=0$
- $\textcolor{lightgreen}{■}$ :$(c-\pi^TA)^Tx=0$ ma perchè questo sia vero almeno uno tra $(\dots)^T$ o $x$ deve essere a $0$
	E' proprio quello che succede nel simplex, le variabili della base $\neq 0$ ma $d_j=0$ e vice versa
di conseguenza possiamo scrivere un sistema equivalente andando a sostituire l'optimality condition:
$$
\begin{cases}
\begin{cases}
Ax=b\\
x\geq 0
\end{cases} \quad\text{ primal fisibility}\\\\
u^TA\leq c^T\quad\text{ dual fisibility(equivale a dire che $d_j\geq 0$)}\\\\
(c_j-\pi^TA_j)x_j=0\quad\text{ complementary slackness}
\end{cases}
$$
#### Primal simplex 
soddisfa:
- primal fisibility
- complementary slackness
solo una volta raggiunta la base ottima:
- dual fisibility

#### Dual simplex
fratello del primal simplex
(Solo una curiosità non viene trattato nel corso)

soddisfa:
- dual fisibility
- complementary slackness
solo una volta raggiunta la fine:
- primal fisibility

# Ex 1

$$
\begin{cases}
\min 2x_2+x_3- 3x_4\\
x_1-x_2+2x_4&{\color{lightgreen}\geq} {\color{cyan}2}
&u_1{\color{lightgreen}\geq} 0\\
2x_2+x_3&{\color{lightgreen}=}{\color{cyan}4}
& u_2\ {\color{lightgreen}free}\\
2x_1-x3+x_4&{\color{lightgreen}\leq} {\color{cyan}1}
& u_3{\color{lightgreen}\leq} 0\\
\color {orange}x_1\geq 0,\ x_2\leq 0,\ x_3,x_4\ free
\end{cases}
\qquad A=
\begin{bmatrix}
1 & -2 & 0 & 2 \\
0 & 2 & 1 & 0 \\
2 & 0 & -1 & 1 \\
\end{bmatrix}
$$
nel nuovo sistema si avrà ogni riga relativa ad una variabile $x$ 
$$
\begin{cases}
\max {\color{cyan}2}u_1+{\color{cyan}4}u_2+{\color{cyan}1}u_3\\
u_1+2u_3 &{\color {orange}\leq} 0 &(x_1)\\
-u_1+2u_2&{\color {orange}\geq} 2 &(x_2)\\
u_2-u_3 &{\color {orange}=}1&(x_3)\\
2u_1+u_3 &{\color {orange}=}-3&(x_4)\\
{\color{lightgreen}u_1\geq0,\ u_2\ free, u_3\leq 0}
\end{cases}
\qquad u^TA=
\begin{bmatrix}
1 & 0 & 2 \\
-1 & 2 & 0 \\
0 & 1 & -1 \\
2 & 0 & 1 \\
\end{bmatrix}\leq c^T=
\begin{bmatrix}
0 \\
2 \\
1 \\
-3 \\
\end{bmatrix}
$$
$\textcolor{orange}{■}$
- $u^{*T}b=c^Tx^*$        se $x$ è libera nel nuovo sistema serve l'uguale perchè altrimenti al primo cambiambento si sballa tutto
- $\bar u^T Ax\leq c^T\bar x$         se $x$ è negativo: $-\bar u^T Ax\leq -c^T\bar x$ allora moltiplico per $-1$ e inverto il segno  $\bar u^T Ax\geq c^T\bar x$ 
