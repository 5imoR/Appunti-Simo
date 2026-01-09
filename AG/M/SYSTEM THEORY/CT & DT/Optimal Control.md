#ST-L32-2 
I 3 ingredienti principali di un optimal control problem sono:
- the system description
- the constraints on the system variables
- a cost function (or a reward function) that dipends on the system variables and that we want to minimize (to maximize)

## LQOCP Linear Quadratic Optimal control problem
Ci si concentrerà su uno specific optimal control problem che sarà chiamato  **Linear Quadratic (LQ) Optimal control problem** per il quale
- La descrizione del sistema è un Linear DT ssm
	Il CT è più complicato e si usa taylor
- l'unico vincolo che ci saà è il valore dello stato iniziale
- la cost function è una funzione quadratica dello stato e dell'input

Andremo a vedere 2 versioni di questo problema:
- Finite Horizon LQ Optimal Control problem
	la cost function valuta l'evoluzione del sistema in una finestra di tempo limitata
- Infite Horizon LQ Optimal Control problem
	la cost function valuta l'evoluzione del sistema in $\mathbb Z+=[0,+\infty)$

### Finite Horizon LQ Optimal Control Problem
cost function
$$
\min_{u(\cdot)} J_T(x_0,u(\cdot))=\min_{u(\cdot)}\sum_{t=0}^{T-1}
\left[x^\top(t)Qx(t)+u^\top(t)Ru(t)\right]+x^\top(T)S\ x(T)
$$
subjet to(S.T.)  
$x(t+1)=Fx(t)+Gu(t) \qquad t=0,1\dots T-1$ 
$x(0)=x_0$

dove 
$x(t)\in X=\mathbb R^n, u(t)\in U=\mathbb R^n, x_0\in X$
and $Q=Q^\top\ge 0 \qquad S=S^\top\ge 0\qquad R=R^\top> 0$  
	$Q,S$ PSD
	$R$ PD
Motivazione per l'ipotesi su $Q,S$ e $R$ :
Prma di tutto ogni quadratic form può essere espressa usando una matrice simmetrica, quindi lo prendiamo per garantito. A questo punto è:
Perchè vogliamo che queste tre matrici siano al meno Positive Semi Definite?
If $M=M^\top$ (una qualunque delle 3) è PSD allora $\forall v\ne 0\quad V^TMV\ge 0$ e siccome stiamo lavorando con una cost function ha senso imporre che tutti i suoi termini siano non negativi.

Nel caso speciale di $R=R^\top$ imponiamo PD perchè vogliamo assicurarci che $\forall u(t)\ne 0$
$u^\top(t)Ru(t)>0$ ci sia sempre un costo da pagare per agire sul sistema
Da un punto di vista matematico questo è conveniente perchè:
- a) $R> 0\Rightarrow R$ è non singular 
- b) $R^{-1}$è PD

![[R9 Review of Positive (Semi) Definitess#Review of Positive (Semi) Definitess]]

#### Considerazioni su PSD
$2\Rightarrow a$ Dato che $R$ non può avere $\underline 0$ come autovalore.
Ora osserviamo che se 
$$
R=T^\top\begin{bmatrix}
\lambda_1\\&\ddots\\&&\lambda_m
\end{bmatrix}
T\qquad \lambda_i\>0
$$
$$
\Rightarrow R^{-1}= T^\top
\begin{bmatrix}
\frac 1{\lambda_1}\\&\ddots\\&&\frac1{\lambda_m}
\end{bmatrix}
T\qquad \frac 1{\lambda_i}>0

$$
e quindi anche $2\Rightarrow b$ 
### Method: Completition of the square
#ST-L33-1
#### Step 1 Rewriting the cost function
$$\begin{align}
J_T(x_0,u(\cdot))
&=\sum_{t=0}^{T-1}
\left[x^\top(t)Qx(t)+u^\top(t)Ru(t)\right]+x^\top(T)S\ x(T)\\
&=\sum_{t=0}^{T-1}
\begin{bmatrix}
u^\top(t) & x^\top(t)
\end{bmatrix}
\begin{bmatrix}
 R & 0\\ 0& Q
\end{bmatrix}
\begin{bmatrix}
u(t)\\x(t)
\end{bmatrix}
+x^\top(T)S\ x(T) \qquad(1)
\end{align}$$
Osserviamo che  per ogni scelta di $T+1$ matrici  $n\times n$ simmetriche reali: $M(0)\dots M(T)$ e per ognia trajectory $\set{x(t)}^T_{t=0}$
$$
\begin{align}
0&=x^\top(0)M(0)x(0){\color{lightgreen}{\color{orange}[}-x^\top(0)M(0)x(0)}\\
&\color{lightgreen}+x^\top(1)M(1)x(1){\color{orange}]}{\color{orange}[}-x^\top(1)M(1)x(1)\\
&\color{lightgreen}\ \ \vdots\\
&{\color{lightgreen}+x^\top(T)M(T)x(T){\color{orange}]}}-x^\top(T)M(T)x(T)\\\\
0&=x^\top(0)M(0)x(0)-x^\top(T)M(T)x(T)\\
&{\color{lightgreen}+\sum_{t=0}^{T-1}{\color{orange}[}x^\top(t+1)M(t+1)x(t+1)-x^\top(t)M(t)x(t){\color{orange}]}}\qquad (2)
\end{align}
$$
Vogliamo riscrivere $\color{orange} [\dots]$ utilizzando la state equation:
$$
\begin{align}
&=x^\top(t+1)M(t+1)x(t+1)-x^\top(t)M(t)x(t)\\
&=[Fx(t)+Gu(t)]^\top\ \ M(t+1)\ \ [Fx(t)+Gu(t)]- x^T(t)M(t)x(t)\\
&=\begin{bmatrix}
u^\top(t) & x^\top (t)
\end{bmatrix}
\begin{bmatrix}
G^\top M(t+1)G & & G^\top M(t+1)F\\\\
F^\top M(t+1)G& & F^\top M(t+1)F-M(t)
\end{bmatrix}
\begin{bmatrix}
u(t)\\ x(t)
\end{bmatrix}
\end{align}
$$
Si vuole riscrivere $(2)$ come:
$$
\begin{align}
0&=x^\top(0)M(0)x(0)-x^\top(T)M(T)x(T)\\
&+\sum^{T-1}_{t=0}\begin{bmatrix}
u^\top(t) & x^\top (t)
\end{bmatrix}
\begin{bmatrix}
G^\top M(t+1)G & G^\top M(t+1)F\\
F^\top M(t+1)G& F^\top M(t+1)F-M(t)
\end{bmatrix}
\begin{bmatrix}
u(t)\\ x(t)
\end{bmatrix}\qquad (3)
\end{align}
$$
Se ora andiamo a sommare $(1)+(3)$ otteniamo una descrizione equivalente di  $J_T(x_0,u(\cdot))$ 
$$
\begin{align}
J_T(x_0,u(\cdot))&=x^\top(0)M(0)x(0)+x^\top(T)\ [S-M(T)]\ x(T)\qquad\qquad\qquad\quad\qquad (4)\\
&+ \sum^{T-1}_{t=0}\begin{bmatrix}
u^\top(t) & x^\top (t)
\end{bmatrix}
\begin{bmatrix}
G^\top M(t+1)G+R & G^\top M(t+1)F\\
F^\top M(t+1)G& F^\top M(t+1)F-M(t)+Q
\end{bmatrix}
\begin{bmatrix}
u(t)\\ x(t)
\end{bmatrix}
\end{align}
$$
A questo punto posiamo aprofittare del fatto che $M(0),\dots,M(T)$ sono arbitrarie per rendere l'espressione di $J_T(x_0,u(\cdot))$  più semplice.
Prima di tutto scegliamo
$$M(T)=S=S^\top\succeq 0$$
Per scegliere le restianti $M(T-1)\dots M(1)$ matrici dobbiamo prima introdurre una lemma.
##### Lemma
Supponiamo che 
$$
M\triangleq
\begin{bmatrix}
A & B\\ B^\top & C
\end{bmatrix}
$$
sia simmetrica con:
- $A=A^\top\in\mathbb R^{m\times m}$ 
- $C=C^\top \in \mathbb R^{n\times n}$ 
Se $A$ è  PD $(A=A\top\succ 0)$ allora:
- $\det M = \det A \ \det [C-B^\top A^{-1}B]$
- $M$ è PD (PSD)$\iff C_B^\top A^{-1}B$ è PD (PSD)
- se $C=B^\top A^{-1}B$ allora $M=\begin{bmatrix}A \\B^\top\end{bmatrix}\begin{bmatrix} A^{-1}\end{bmatrix}\begin{bmatrix}A & B\end{bmatrix}$ 
$C_B^\top A^{-1}B$ è detto Shur component di $A$ in $M$ 
#####

Applichiamo ora il terzo punto della lemma precente assumendo:
$$
\begin{bmatrix}
A & B\\ B^\top & C
\end{bmatrix}
=
\begin{bmatrix}
G^\top M(t+1)G+R & G^\top M(t+1)F\\
F^\top M(t+1)G& F^\top M(t+1)F-M(t)+Q
\end{bmatrix}
$$
e $C=B^\top A^{-1} B$ 
questo comporta che:
$$
\begin{align}
{\color{orange}F^\top M(t+1)F}-M(t){\color{orange}+Q}=\color{lightgreen}F^\top M(t+1)G\ [G^\top M(t+1)G+R]^{-1}\ G^\top M(t+1)F\\
M(t)={\color{orange}F^\top M(t+1)F+Q} -\color{lightgreen}F^\top M(t+1)G\ [G^\top M(t+1)G+R]^{-1}\ G^\top M(t+1)F\\
\end{align}
$$
Questa è chiamata Difference Riccati Equation DRE.

Mettendo insieme
- la condizione  di $M(T)=S$
- la DRE 
Si ottengono le matrici $M(T-1)\dots M(1)$ 

##### Remark
Per usare la lemma abbiamo bisogno di avere che $\forall t\qquad A=G^\top M(t+1)G+R$  sia PD?
E' possibile dimostrare (non lo si fa nel corso) che se $M(T)=S\succeq0$ allora  $M(T-1)\dots M(1)$ sono tutte PSD
#####
Ora dimostriamo che se $M(t+1)\succeq 0$ allora $G^\top M(t+1)G+R\succ 0$ 
$\forall \underline v \ne \underline 0$ si ha:
$$\underline v^\top [G^\top M(t+1)G+R]\underline v=\underbrace{[G\underline v]^\top M(t+1)[G\underline v]}_{\succeq 0}+\underbrace{\underline v^\top R\underline v}_{\succ 0}\succ 0$$
Ora si riscrive $(4)$ usando il terzo punto della lemma:
$$
\begin{align}
J_T(x_0,u(\cdot ))&=x^\top(0)M(0)x(0)\\
&+\sum_{t=0}^{T-1}
\underbrace{\begin{bmatrix}
u^\top(t) & x^\top (t)
\end{bmatrix}
\begin{bmatrix}
G^\top M(t+1)G+R \\ F^\top M(t+1)G
\end{bmatrix}}_{\displaystyle\triangleq z^\top(t)}
\underbrace{\begin{bmatrix}
G^\top M(t+1)G+R
\end{bmatrix}^{-1}}_{\displaystyle PD}\cdot\\&\cdot
\underbrace{\begin{bmatrix}
G^\top M(t+1)G+R & G^\top M(t+1)F
\end{bmatrix}
\begin{bmatrix}
u(t)\\ x(t)
\end{bmatrix}}_{\displaystyle\triangleq z(t)}\\
\end{align}
$$
#### Step 2 Choice of the minimising input
Osserviamo che 
$J_T(x_0,u(\cdot ))=x^\top(0)M(0)x(0)+z^\top(t)\underbrace{\begin{bmatrix}G^\top M(t+1)G+R\end{bmatrix}^{-1}}_{PD}z(t)$ 
Chiaramente $\min_{u(\cdot)} J_T(x_0, u(\cdot))$ è ottenuto se possibile imponendo che $z(t)=0\quad t=1\dots T-1$ 
e così si ottiene:
$J_T(x_0,u(\cdot ))=x^\top(0)M(0)x(0)$
si osserva che 
$$
\begin{align}
z(t)&=[G^\top M(t+1)G+R]\cdot u(t)+[G^\top M(t+1)F]x(t)\equiv 0\\
\iff u(t)&\equiv \underbrace{-[G^\top M(t+1)G+R]^{-1}G^\top M(t+1)F}_{\triangleq K(t)}\ x(t)\triangleq u^*(t)
\end{align}
$$

#### Summarize
- Sotto l'assunzione che $R=R^\top\succ 0\qquad S=S^\top\succeq 0\qquad Q=Q^\top \succeq 0$ possiuamo assicurarci che il problema sia sempre risolvibile e che la soluzione sia unica ed è ottenuta tramite un "time-varing state feedback"
- Algoritmo per ottenere la soluzione:
	1. $M(T)=S$
	2. Calcolo $M(T-1)\dots M(1)$ usando DRE                                                                             $\Rightarrow J_T^*(x_0)\triangleq \min_u(\cdot)J_T(x_0,u(\cdot))\equiv x^\top(0)M(0)x(0)$
	3. usando $M(T-1)\dots M(1)$ otteniamo $K(0)\dots K(T-1)$  usando $K(t)=-[G^\top M(t+1)G+R]^{-1}G^\top M(t+1)F$ $\Rightarrow\text{ minimising input è:} u^*(t)=K(t)x(t) \quad t=0\dots T-1$  