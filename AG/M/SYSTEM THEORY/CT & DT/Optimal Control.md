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
and $Q=Q^\top\ge 0 \qquad S=S^\top\ge 0\qquad R=R^\top\> 0$  
	$Q,S$ PSD
	$R$ PD
Motivazione per l'ipotesi su $Q,S$ e $R$ :
Prma di tutto ogni quadratic form può essere espressa usando una matrice simmetrica, quindi lo prendiamo per garantito. A questo punto è:
Perchè vogliamo che queste tre matrici siano al meno Positive Semi Definite?
If $M=M^\top$ (una qualunque delle 3) è PSD allora $\forall v\ne 0\quad V^TMV\ge 0$ e siccome stiamo lavorando con una cost function ha senso imporre che tutti i suoi termini siano non negativi.

Nel caso speciale di $R=R^\top$ imponiamo PD perchè vogliamo assicurarci che $\forall u(t)\ne 0$
$u^\top(t)Ru(t)>0$ ci sia sempre un costo da pagare per agire sul sistema
Da un punto di vista matematico questo è conveniente perchè:
- a) $R\> 0\Rightarrow R$ è non singular 
- b) $R^{-1}$è PD

### Review of Positive (Semi) Definitess
Data una matrice quadrata simmetrica $M\in \mathbb R^{m\times m}$ i.e. $M=M^\top$ sappiamo che $\exists$ una matrice ortonormale $T\in\mathbb R^{m\times m}$ (i.e. s.t. $T^\top T=TT^\top= I_m$) s.t.
$$
M=T^\top \Lambda T=T^\top\begin{bmatrix}
\lambda_1\\&\ddots\\&&\lambda_m
\end{bmatrix} T\qquad 
\begin{array}{c}
\lambda_i\in \mathbb R\quad \forall i\\
\sigma(M) =\lambda_i
\end{array}
$$
Data $M=M^\top\in \mathbb R^{m\times m}$ :
1. $M\ge 0\iff \lambda_i\ge 0 \forall i$
2. $M>0\iff \lambda_i>0\forall i$

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
$2\Rightarrow a$