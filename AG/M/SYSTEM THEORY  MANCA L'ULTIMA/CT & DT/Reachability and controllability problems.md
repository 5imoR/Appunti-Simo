#ST-L7
### Reachability question
Dato un tempo $T>0$ e uno stato finale $x_f\in X$ è possibile trovare il segnale in input
$u(t)\quad t\in[\ 0, T\ )$  che porta lo stato del sistema da $x(0)=\underline 0$ a $x(T)=x_f$?
### Controllability (to zero) question
Dato un tempo $T>0$ e uno stato $x_0\in X$  è possibile trovare un segnale in input  
$u(t)\quad t\in[\ 0, T\ )$ che porta lo stato del sistema da $x(0)=x_0$ a $x(T)=\underline 0$?

Queste due funzioni sono simmetriche nel caso continuo mentre quella della reachability è più forte nel caso discreto
![[reachcontrol]]


# Exercise DT
Dato il seguente DT s.s.m.
$$x(t+1)=Fx(t)-gu(t)=
\begin{bmatrix}
0&0&0\\
1&0&1\\
-1&1&1
\end{bmatrix}
x(t)+
\begin{bmatrix}
0\\1\\0
\end{bmatrix}
u(t)
$$
Si vuole determinare il sottospazio vettoriale $X^R_k$ e $X_k^C\quad \forall k\in \mathbb Z\quad k\geq 1$  
$X_k^R=\set{x\in X: x\in Im\mathcal R_k}=Im[G|FG|\dots|F^{k-1}G]$ 
$X_k^C=\set{x\in X:F^kx\in Im\mathcal R_k}$ 

## Reachability 
$$
\begin{align}
X^R_1=Im(g)&=Im\begin{bmatrix}0\\1\\0\end{bmatrix}=<e_2>\\
X^R_2=Im[g|Fg]&=Im\begin{bmatrix}0\\ {\color{orange}1}\\0\end{bmatrix}\begin{bmatrix}
0&{\color{orange}0}&0\\
1&{\color{orange}0}&1\\
-1&{\color{orange}1}&1
\end{bmatrix}=Im\begin{bmatrix}0&0\\1&0\\0&1\end{bmatrix}=<e_2, e_3>\\
X_3^R=Im[g|Fg|F^2g]&=Im\begin{bmatrix}
0&0&0\\
1&0&1\\
0&1&1
\end{bmatrix}=<e_2,e_3>
\end{align}
$$
Per calcolare $F^2G$ e simili, non si fa la potenza ma piuttosto $F(FG)$  soprattutto se $G$ è un vettore colonna.
$X_1^R=X_k^R=<e_2,e_3>\ \forall k\geq 2$ quindi non è reachable

**Nota**
$X_2^R=<e_2,e_3>\neq \mathbb R^2$ 
## Controllability
$$
\begin{align}
X_1^C=\set{x\in\mathbb R^3:Fx\in Im\ g}=\left\{\begin{bmatrix}
x_1\\x_2\\x_3
\end{bmatrix},s.t.\ \ x_1,x_2,x_3\in \mathbb R:
\begin{bmatrix}
0\\
x_1+x_3\\
x_1+x_2+x_3
\end{bmatrix}
\in \begin{bmatrix}
0\\1\\0
\end{bmatrix}
\right\}\\(\text{deve essere qualcosa del tipo: }\begin{bmatrix}
0&*&0
\end{bmatrix}^T)
\end{align}
$$
$$
\begin{align}
\qquad\qquad\qquad\qquad\qquad\qquad\qquad\ &=\left\{
\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}
,s.t.\ \ x_1,x_2,x_3\in \mathbb R:
-x_1+x_2+x_3=0\right\}\\
&=\left\{\begin{bmatrix}x_2+x_3\\x_2\\x_3\end{bmatrix}, s.t.\ \ x_2,x_3\ \mathbb R\right\}
=\left\{\begin{bmatrix}1\\1\\0\end{bmatrix}x_2+\begin{bmatrix}1\\0\\1\end{bmatrix}x_3,\ \ x_2,x_3\ \mathbb R\right\}
\end{align}
$$
La somma  devie dare $[0\ 1\ 0]$ quindi si ottiene:
$$
X_1^C=\{x\in \mathbb R^3: F_x\in Im\ g\}=<\begin{bmatrix}1\\1\\0\end{bmatrix},\begin{bmatrix}1\\0\\1\end{bmatrix}>
$$
$$
\begin{align}
X_2^C&=\{x\in \mathbb R^3: F^2_x\in Im\ [g|Fg]\}\\
&=\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}\ x_1,x_2,x_3 \in \mathbb R\\
&=\begin{bmatrix}
0&0&0\\
1&0&1\\
-1&1&1
\end{bmatrix}
\begin{bmatrix}
0\\
x_1+x_3\\
x_1+x_2+x_3
\end{bmatrix}=
\begin{bmatrix}
0\\
-x_1+x_2+x_3\\
x_2+2x_3
\end{bmatrix}\in <\begin{bmatrix}0\\1\\0\end{bmatrix},\begin{bmatrix}0\\0\\1\end{bmatrix}>\\\\
&\Rightarrow X_2^C=\mathbb R^3\quad X_k^C=\mathbb R^3\ \forall k\geq 2\qquad(F,G)
\text{ è controllable to } 0
\end{align}
$$



