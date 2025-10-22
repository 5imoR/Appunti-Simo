#ST-L9 
# Controllability
[[Reachability and controllability problems]]
[[Linear discrete time s.s.m.]]
**State equation**
$$
x(t+1)=Fx(t)+Gu(t)\qquad\qquad\qquad t\in \mathbb Z+
$$
$dim\ x=n\quad dim\ u=m$  
- $F\in R^{n\times n}$ State Matrix
- $G\in R^{m\times m}$ Input Matrix
#ST-L10
$(F,G)$ è controllable $\iff Im F^n\subseteq Im\mathcal R$

Supponendo che $F$ sia non singular Allora $F^n$ è non singular $\Rightarrow ImF^n=\mathbb R^n$ allora:
Se $(F,G)$ è controllable è anche reachable se $F$ è non singular
$$
\begin{align}
(F,G)\text{ è controllable}&\Rightarrow Im F^n=\mathbb R^n\subseteq Im \mathcal R\subseteq \mathbb R^n\\
&\Rightarrow Im\mathcal R=\mathbb R^n\\
&\Rightarrow (F,G) \text{ è reachable}
\end{align}
$$

### Definition
#ST-L9
Dato $k\in \mathbb Z\quad k \geq 1$  diciamo che lo stato $x_0\in X=\mathbb R^n$  è controllable in 0 in $k$ steps (at time $k$) se 
$\exists u(0),u(1),\dots u(k-1)\in U=\mathbb R^m$  che guida lo stato da 
$x(0)=x_0$  a $x(u)=\underline 0$ 
$$
\large
(x(0)\xrightarrow[u(0),u(1),\dots,u(k-1)]{} x(k)=\underline 0)
$$

###
Il generico stato al tempo $k$ è:
$$\begin{align}
\displaystyle x_k=x_l(k)+x_f(k)=F^kx(0)+\mathcal R_k\begin{bmatrix}u(k-1)\\u(k-2)\\\vdots\\u(0)\end{bmatrix}
\end{align}$$


Di conseguenza
$$
\begin{align}
x_0 {\Large\substack{\text{ is controllable }\\\text{to 0 in k steps}}}&\iff\exists u(0),u(1),\dots u(k-1)\in U=\mathbb R^m s.t.\qquad \underline 0= F^kx_0+\mathcal R_k\begin{bmatrix}u(k-1)\\u(k-2)\\\vdots\\u(0)\end{bmatrix}\\
&\iff F^kx_0=-\mathcal R_k\begin{bmatrix}u(k-1)\\u(k-2)\\\vdots\\u(0)\end{bmatrix}\\\\
&\iff F^kx_0\in Im\mathcal R_k=X_k^R
\end{align}
$$
Se chiamiamo  $X_k^C$ il set di stati che possono essere controllati a 0 in $k$ steps allora
$$
X_k^C\equiv \set{x_0\in X:F^kx_0\in Im \mathcal R_k=X_k^R}
$$
$X_k^C$ è chiuso w.r.t. combinazioni lineari e quindi è un sottospazio vettoriale


##### In Generale
Per ogni $k \in \mathbb Z\quad k>0$ 
$X_k^C\subseteq X_{k+1}^C$ 
![[shifted2|700]]
$$
X_1^C\subset X_2^C\subset... \subset X_k^C\subset ... \subset X=\mathbb R^n
$$
Se $X_k^C \subsetneq X_{k+1}^C$   allora $dimX_{k+1}^C\geq dim X_k^C+1$  
e quindi
$$
\exists \bar k\in \mathbb Z\quad \bar k >0\quad\text{ s.t.}\quad X_\bar k^R=X_k^R \quad \forall k\geq\bar k
$$
### Proposition
1. se $X_k^C=X_{k+1}^C$ allora $X_{k+1}^C=X_{k+2}^C\iff X_{k+1}^C =X_k^C$  
2. se $\bar k \triangleq \min\{ k\in\mathbb Z\ k\geq 1:X_k^C=X_{k+1}^C\}$ allora $\bar k \leq n$
#### Proof
**1**
E' sempre vero che $X_{k+1}^C\subseteq X_{k+2}^C$  serve quindi provare che se
$X_{k}^C=X_{k+1}^C$ allora $X_{k+2}^C\subseteq X_{k+1}^C$

Questo vuol dire che: $\exists u(t)=u_t\quad t=1,...k+1$ tale che:

| Time  | $0$   | $1$   | $\cdots$ | $k+1$     | $k+2$          |
| ----- | ----- | ----- | -------- | --------- | -------------- |
| State | $x_0$ | $x_1$ | $\cdots$ | $x_{k+1}$ | $\underline 0$ |
| Input | $u_0$ | $u_1$ | $\cdots$ | $u_{k+1}$ |                |
Siccome  $x_{k+1}\in X_{k+1}^C=X_k^C$
$\exists u(t)=\bar u_t$  tale che:
$x_0=x(1)\xrightarrow[u(0),u(1),\dots,u(k-1)]{} x(k)=\underline 0$ 
Il sistema è quindi time invariant e quindi:
$x(1)=x_1\xrightarrow[u(0),u(1),\dots,u(k-1)]{} x(k)=\underline 0$

| Time  | $0$   | $1$        | $2$        | $\cdots$ | $k+1$          |
| ----- | ----- | ---------- | ---------- | -------- | -------------- |
| State | $x_0$ | $x_1$      | $\bar x_2$ | $\cdots$ | $\underline 0$ |
| Input | $u_0$ | $\bar u_0$ | $\bar u_1$ | $\cdots$ |                |
**2** 
	(uguale a quella della reachability)
- Se $G=0$ allora:
	$X_k^C=\set{\underline 0}\ \forall k\geq 1$ 
	e quindi il non essendoci un input resterà sempre $\underline 0$  e ok
- Se $G\neq 0$ allora:
	$X_1^C\subset X_2^C\subset\ldots\subset X_\bar k^C= X_{\bar k+1}^C\subseteq X=\mathbb R^n$ 
	$X$ è un sottospazio vettoriale quindi al suo interno non si può avere una dimensione maggiore ad $n$ 
Di conseguenza:
$X_1^C\subset X_2^C\subset\ldots\subset X_\bar k^C= X_{\bar k+1}^C=\ldots\subseteq X=\mathbb C^n\quad X_\bar k ^C\equiv X_n^C$  (è raggiungibile in $n$ passaggi)
###
#ST-L10 
Di conseguenza $X_1^C\subset X_2^C\subset...\subset X_\bar k^C= X_{\bar k+1}^C\subseteq X=\mathbb R^n$.
Se oriac chiamiamo $X^C$ il set di stati che possono essere controllati a zero in un numero finito di step allora:
$$
X^C=X_n^C\Big\{x\in X:F^nx\in Im\mathcal R_n=Im\mathcal R\Big\}
$$
Diciamo quindi che il sistema DT (equivalentemente $(F, G)$) è controllabile a zero se tutti gli stati sono controllabili a zero in un numero finito di steps i.e. $X^C=\mathbb R^n$

**RECAP**
$$\begin{align}
(F,G) {\Large\substack{\text{ is controllable }\\\text{to 0 in k steps}}}&\iff X^C =\set{x\in X:F^nx\in Im\mathcal R} =\mathbb R^n=X\\
&\iff\forall x \in X F^nx\in Im\mathcal R\\
&\iff ImF^n\subseteq Im \mathcal R
\end{align}
$$
