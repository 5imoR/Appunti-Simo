#ST-L32-2 
I 3 ingredienti principali di un optimal control problem sono:
- the system description
- the constraints on the system variables
- a cost function (or a reward function) that dipends on the system variables and that we want to minimize (to maximize)

# LQOCP Linear Quadratic Optimal control problem
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

## Finite Horizon LQ Optimal Control Problem
cost function
$$
\min_{u(\cdot)} J_T(x_0,u(\cdot))=\min_{u(\cdot)}\sum_{t=0}^{T-1}
\left[x^\top(t)Qx(t)+u^\top(t)Ru(t)\right]+x^\top(T)S\ x(T)
$$
subjet to(S.T.)  
$x(t+1)=Fx(t)+Gu(t) \qquad t=0,1\dots T-1$ 
$x(0)=x_0$

dove 
$x(t)\in X=\mathbb R^n, u(t)\in U=\mathbb R^m, x_0\in X$
and $Q=Q^\top\succeq 0 \qquad S=S^\top\succeq 0\qquad R=R^\top\succ 0$  
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
##### DRE

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
- la   DRE 
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

## Infinite Horizon LQ Optimal Control Problem
cost function
$$
\min_{u(\cdot)} J_T(x_0,u(\cdot))=\min_{u(\cdot)}\sum_{t=0}^{+\infty}
\left[x^\top(t)Qx(t)+u^\top(t)Ru(t)\right]
$$
subjet to(S.T.)  
$x(t+1)=Fx(t)+Gu(t) \qquad t\in\mathbb Z +$
$x(0)=x_0$
dove 
$x(t)\in X=\mathbb R^n, u(t)\in U=\mathbb R^m, x_0\in X$
and $Q=Q^\top\succeq 0 \qquad R=R^\top\succ 0$  

Quando, questo problema, è ben formulato?
### Well posedness problem
Stiamo gestendo una sommatoria con infinite somme e che quindi può dare $\infty$ come risultato. Il problema è formulato correttamente se e solo se:
$$
\forall x_o\in X=\mathbb R^n\ \exists\bar u(\cdot)\ s.t.\ J(x_0,\bar u(\cdot))<+\infty
$$
In tal caso si avrebbe che:
$$
J^\underline x(x_0)\triangleq\min_{u(\cdot)}J(x_0,u(\cdot))<+\infty
$$
Chiaramente se $(F,G)$ è controllabile a zero allora:
$\forall x_0\in X\quad\exists \bar u(0),\dots,\bar u(n-1)\in U=\mathbb R^m$ 
che guida lo stato da $x(0)=x_0\to x(n)=0$ 
Se a questo punto assumiamo che l'input sia $\bar u(t)=\underline 0\quad t\ge n$ allora $x(t)=\underline 0\quad \forall t>n$ 
$$
 J_T(x_0,\bar u(\cdot))=\sum_{t=0}^{n-1}
\left[x^\top(t)Qx(t)+u^\top(t)Ru(t)\right]<+\infty
$$
Questa però è una proprietà troppo forte da avere.
Se consideriamo la stabilizability (proprietà più debole) per provare che se $(F,G)$ è stabilizzabile allora l'[[Optimal Control#Infinite Horizon LQ Optimal Control Problem|IHLQOCP]]  è ben formulato.
### Lemma
Consideriamo di avere un DT ssm
$$
x(t+1)=Ax(t)\qquad t\in\mathbb Z+
$$
allora:
1. il sistema è asintoticamente stabile (Shur stable)$\iff$ $\forall \tilde Q=\tilde Q^\top\succeq0\quad \exists \tilde P=\tilde P^\top\succ 0$ s.t. $$A^\top\tilde PA-\tilde P=-\tilde Q\quad \text{Discrete Lyapunov equation}$$
2. Se il sistema è asintoticamente stabile$$\Rightarrow \forall \tilde Q=\tilde Q^\top\succeq 0\quad \exists \tilde P=\tilde P^\top\succeq 0 \text{ che risolve l'equazione precedente}$$
In entrambi i casi la soluzione è unica e può essere espressa come:$$
\tilde P=\sum^{+\infty}_{t=0}(A^\top)^tQA^t\quad \text{unica soluzione dato }\tilde Q
$$
### Lemma
Supponiamo che $(F,G)$ sia stabilizzabile e lasciamo $K\in\mathbb R^{m\times n}$ essere una qualunque matrice tale che $(F+GK)$ sia Shur stable.
Settiamo $\bar u(t)=Kx(t)$ allora
$$
J(x_0,\bar u(\cdot))=x_0^\top\tilde Px_0\quad \forall x_0\in\tilde x
$$
dove $\tilde P =\tilde P^\top\succ 0$ è la souzione della "discrete lyapunov equation"
$$
\underbrace{(F+GK)}_A^\top\tilde P(F+GK)-\tilde P=-\underbrace{[K^\top RK+Q]}_\tilde Q
$$
#### Proof
Assumiamo
$\bar u(t)=Kx(t)$
allora
$x(t+1)=(F+GK)x(t)\quad \forall t\in \mathbb Z+$
Possiamo dire che 
$x(t)=(F+GK)^tx_0\quad \forall t\in \mathbb Z$

Calcoliamo ora $J(x_0,\bar  u(\cdot))$
$$
\begin{align}
J(x_0,\bar  u(\cdot))&=\sum_{t=0}^{+\infty}
\left[x^\top(t)Qx(t)+x^\top(t)K^\top R\ Kx(t)\right]\\
&=\sum_{t=0}^{+\infty}
\left[x^\top(t)\ (Q+K^\top R\ K)\ x(t)\right]\\
&=\sum_{t=0}^{+\infty}\left[x_0^\top\left[(F+GK)^\top\right]^t(Q+K^\top RK)(F+GK)^tx_0\right]\\
&=x_0^\top\underbrace{\left[\sum^{+\infty}_{t=0}\left[(F+GK)^\top\right]^t\underbrace{(Q+K^\top RK)}_{\ge 0}\underbrace{(F+GK)^t}_\text{Shur stable}\right]}_{\displaystyle \tilde P}x_0
\end{align}
$$
Per la seconda lemma e la soluzione $\tilde P$ possiamo dire che $J(x_0,\bar  u(\cdot))=x_0^\top\tilde P\ x_0$  dove $\tilde P$ è l'unica soluzione di $\underbrace{(F+GK)}_A^\top\tilde P(F+GK)-\tilde P=-\underbrace{[K^\top RK+Q]}_\tilde Q$ 
###
**NOTA Daq qui in poi assumiamo sempre di  avere $(F,G)$ sabilizable**


### Solution to LQ control
Vogliamo ottenere la soluzione come un limite della soluzione del FHLQOC con zero finite cost ($S=0$)  in una finestra di tempo finita $[0,T)\quad T\to+\infty$ 
$$
\min_{u(\cdot)} J_T(x_0,u(\cdot))=\min_{u(\cdot)}\sum_{t=0}^{T-1}
\left[x^\top(t)Qx(t)+u^\top(t)Ru(t)\right]
$$
subjet to(S.T.)  
$x(t+1)=Fx(t)+Gu(t) \qquad t\in\mathbb Z +$
$x(0)=x_0$

Iniziamo definendo $M_T(T)=S=0$ 
[[Optimal Control#DRE|DRE]]: per calcolare $M(T-1)\dots M(0)$
$$
M_T(t)=F^\top M_T(t+1)F+Q-F^\top M_T(t+1)G[G^\top M_T(t+1)G+R]^{-1}G^\top M_T(t+1)F
$$
per ogni $t=T-1\dots 0$ abbiamo:
$$
\begin{cases}
\displaystyle J_T^*(x_0)=\min_{u(\cdot)}J_T(x_0,u(\cdot))=x_0^\top M_T(0)x_0\\
\displaystyle u^*(t)=K(t)x(t)=- [G^\top M_T(t+1)G+R]^{-1}G^\top M_T(t+1)F
\end{cases}
$$
$$\begin{align}
Q\phantom{ssssssssssssssssss}\\
||\phantom{ssssssssssssssssss}\\
M_1(0)\xleftarrow[]{DRE}M_1(1)=0\\
||\phantom{ssssssssssssssssss}\\
M_2(0)\xleftarrow[]{}M_2(1)\xleftarrow[]{DRE}M_2(2)=0\\
||\phantom{ssssssss}||\phantom{ssssssssssssssssss}\\
M_3(0)\xleftarrow[]{}M_3(1)\xleftarrow[]{}M_3(2)\xleftarrow[]{DRE}M_3(3)=0\\
\end{align}$$
Se scegliamo 
$T_1,T_2\in\mathbb Z+\qquad T_1\ne T_2\qquad M_{T1}(t)\ne M_{T2}(t)$ 
ma
$M_{T1}(T_1-t)\equiv M_{T2}(T_2-t)\quad \forall t\ge 0$ 
Allora possiamo ridefinire le matrici $M(T-1)=M(-1)$ che è lo stesso per ogni $T$
