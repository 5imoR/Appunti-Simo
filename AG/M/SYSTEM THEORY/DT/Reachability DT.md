# Reachability DT
#ST-L7 
[[Reachability and controllability problems]]
![[Linear discrete time s.s.m.#Linear DT ssm#State equation]]

#ST-L10 
$(F,G)$ è reachable $\iff \mathcal R=n \iff Im \mathcal R=\mathbb R^n$

Se $(F,G)$ è reachable è anche controllable
$$
\begin{align}
(F,G)\text{ è reachable}&\Rightarrow Im\mathcal R=\mathbb R^n\\
&\Rightarrow ImF^n\subseteq Im\mathcal R=\mathbb R^n\\
&\Rightarrow (F,G) \text{ è controllable}
\end{align}
$$

### Definition
#ST-L7
Dato $k\in\mathbb Z,\ k>0$ uno stato $x_f\in X\in \mathbb R^n$ è detto *reachable* al tempo $t=k$ (in $k$ steps) se $\exists u(0),u(1),\dots u(k-1)\in U=\mathbb R^m$ che guida lo stato da $x(0)=\underline 0$  a $x(u)=x_f$ 
$$\large
(x(0)\xrightarrow[u(0),u(1),\dots,u(k-1)]{} x(k)=x_f)
$$
Il generico stato al tempo $k$ è:
$$\begin{align}
\displaystyle x_k=x_f(k)&=\sum_{i=0}^kF^{k-1-i}Gu(i)\\
&=\begin{bmatrix}G|FG|F^2G|\dots|F^{k-1}G\end{bmatrix}\begin{bmatrix}u(k-1)\\u(k-2)\\\vdots\\u(0)\end{bmatrix}
\end{align}$$

$\begin{bmatrix}G|FG|F^2G|\dots|F^{k-1}G\end{bmatrix}$ è chiamata $\mathcal R_k$ (rechability matrix at time $k$)

###
Quindi:
$x_f$ è reachable al tempo $k\iff\exists u(0),u(1),\dots, u(k-1)\in \mathbb R^n=U$ 
tale che $$x_f=\mathcal R_k\begin{bmatrix}u(k-1)\\u(k-2)\\\vdots\\u(0)\end{bmatrix}\iff x_f\in Im\mathcal R_k$$

Se definiamo $X_k^R$ il set di stati che sono raggiungibili in $k$ steps
	$X_k^R\triangleq\{x_f\in X=\mathbb R^n:\exists u(0),u(1),\dots u(k-1):x(0)\xrightarrow[u(0),u(1),\dots,u(k-1)]{} x(k)=x_f\}$ 
allora:
$X_k^R\equiv Im\mathcal R_k$ 
di conseguenza $X_k^R$ è un sottospazio vettoriale di $X=\mathbb R^n$ 

##### In Generale
Per ogni $k \in \mathbb Z\quad k>0$ 
$X_k^R\subseteq X_{k+1}^R$ 
Che ci permette di dire che:
$$
X_k^R=\begin{bmatrix}G|FG|F^2G|\dots|F^{k-1}G\end{bmatrix}\subseteq\begin{bmatrix}G|FG|F^2G|\dots|F^{k}G\end{bmatrix}=X_{k+1}^R
$$
Una caratteristica è che:
se uno stato è raggiungibile in $k$ steps allora può essere raggiunto anche in $k+1$ step andando a shiftare di 1 i vari steps
![[shifted|700]]
Di conseguenza:
$$
 X_1^R\subset X_2^R\subset... \subset X_k^R\subset ... \subset X=\mathbb R^n
 
$$

Siccome ogni $X_k^R$  è un sottospazio vettoriale di $X$ e $X_k^R\subsetneq X_{k+1}^R\Rightarrow dim X_{k+1}^R\geq dim X_k^R+1$ 
e quindi
$$
\exists \bar k\in \mathbb Z\quad \bar k >0\quad\text{ s.t.}\quad X_\bar k^R=X_k^R \quad \forall k\geq\bar k
$$
#ST-L8
### Proposition
1. se $X_k^R=X_{k+1}^R$ allora $X_{k+1}^R=X_{k+2}^R\iff X_{k+1}^R =X_k^R$  
2. se $\bar k \triangleq \min\{ k\in\mathbb Z\ k\geq 1:X_k^R=X_{k+1}^R\}$ allora $\bar k \leq n$

#### Proof
**1**
E' sempre vero che $X_{k+1}^R\subseteq X_{k+2}^R$  serve quindi provare che se $X_{k}^R=X_{k+1}^R$ allora $X_{k+2}^R\subseteq X_{k+1}^R$ così possiamo assumere che $x_f\in X_{k+2}^R$ 

Questo vuol dire che:$\exists u(t)=u_t\quad t=1,...k+1$ tale che:

| Time  | $0$            | $1$   | $\cdots$ | $k+1$     | $k+2$ |
| ----- | -------------- | ----- | -------- | --------- | ----- |
| State | $\underline 0$ | $x_1$ | $\cdots$ | $x_{k+1}$ | $x_f$ |
| Input | $u_0$          | $u_1$ | $\cdots$ | $u_{k+1}$ |       |
Siccome  $x_{k+1}\in X_{k+1}^R=X_k^R$
$\exists u(t)=\bar u_t$  tale che:


| Time  | $0$            | $1$        | $\cdots$ | $k-1$          | $k$       | $k+1$ |
| ----- | -------------- | ---------- | -------- | -------------- | --------- | ----- |
| State | $\underline 0$ | $\bar x_1$ | $\cdots$ | $\bar x_{k-1}$ | $x_{k+1}$ | $x_f$ |
| Input | $\bar u_0$     | $\bar u_1$ | $\cdots$ | $\bar u_{k-1}$ | $u_{k+1}$ |       |
$\Rightarrow x_f\in X^R{k+1}$

**2**
- Se $G=0$ allora:
	$X_k^R=\set{\underline 0}\ \forall k\geq 1$ 
	e quindi il non essendoci un input resterà sempre $\underline 0$  e ok
- Se $G\neq 0$ allora:
	$X_1^R\subset X_2^R\subset\ldots\subset X_\bar k^R= X_{\bar k+1}^R\subseteq X=\mathbb R^n$ 
	$X$ è un sottospazio vettoriale quindi al suo interno non si può avere una dimensione maggiore ad $n$ 
Di conseguenza:
$X_1^R\subset X_2^R\subset\ldots\subset X_\bar k^R= X_{\bar k+1}^R=\ldots\subseteq X=\mathbb R^n\quad X_\bar k ^R\equiv X_n^R$  (è raggiungibile in $n$ passaggi)
###
Definiamo:
Reachable subspace del sistema $\Sigma$ (equivalentemente) il *paio* $(F,G)$  il set di stati che possono essere raggiunti in un numero finito di steps e lo chiamiamo $X^R$. Allora:
$$
\Large
X^R=X_\bar k ^R= X_n^R=\underbrace{[F|FG|\ldots|F^{n-1}G]}_{\mathcal R\in \mathbb R^{n\times nm}}
$$
Diciamo che il paio $(F,G)$ è reachable se ogni stato in $X$ può essere raggiunto in un tempo finito $X^R=X$

### Reachability Criterion
$$
(F,G)\text{ è reachable } \iff rank\  {[\ F|FG|\ldots|F^{n-1}G\ ]}=n
$$

### Proposition
Se $\Sigma$ è un reachable system con un singolo input allora $\bar k=n$ 
#### Proof
Sappiamo che $\bar k \leq n$  inoltre se consideriamo le reachability matrixes associate al paio$(F,G)=(F,g)\ (G=g)\in\mathbb R^n$ column vector allora
$$
X_\bar k^R=Im[g|Fg|\ldots|F^{\bar k -1}g]\rightarrow 
	n\Big \{\underbrace{\begin{bmatrix}&&\\&&\end{bmatrix}}_\bar k$$
se $\bar k <n$ la matrice non sarebbe più di rango $n$ 

D'ora in poi quando un paio è reachable chiameremo $\bar k$ il suo indice di reachability e gli daremo il nome $r$ 


### Remark
1. Sia $A\in \mathbb R^{n\times n}$ e $B\in \mathbb R^{n\times k}$  allora $A(Im(B))=Im(AB)$  
	$$
	\begin{align}
	x\in A(Im (B))&\iff xAy\quad \exists y\in Im (B)\\
	&\iff x=A(Bz)\quad \exists z\\
	&\iff x=(AB)z\\
	&\iff x\in Im(AB)
	\end{align}
	$$
2. Sia $F\in\mathbb R^{n\times n}$ e $S$ un vettore del sottospazio di $X=\mathbb R^n$ allora $S$ è *F-invariant* se $FS\subseteq S$ 

###
![[Cayley-Hamilton's theorem#Cayley-Hamilton's theorem]] 

### Proposition
Dato un paio$(F,G)\quad F\in\mathbb R^{n\times n}\quad G\in\mathbb R^{n\times m}$  sia 
$X^R=Im[G|FG|\ldots|F^{n-1}G]$ il sio reachable subspace
Allora $X^R$ è il più piccolo sottospazio *F-Invariant* di $X=\mathbb R^n$ che include $Im(G)$ 
![[insiemi FInvariant]]
#### Proof 
$X^R=Im[G|FG|\ldots|F^{n-1}G]$ 
Vogliamo provare che $X^R$ sia F-invariant

$$
+++
$$
Ora ci manca solo di provare che se $S$ è un sottospazio vettoriale di $X$ e che quindi include $Im(G)$  ed è *F-invariant* allora $S\supseteq X^R$

$$
\begin{align}
Im(G)&\subseteq S&\\
F\ Im(G)&\subseteq FS&\rightarrow Im(FG)\subseteq S\\
F\ Im(FG)&\subseteq FS&\rightarrow Im(F^2G)\subseteq S\\
&\vdots\\
Im(F^{n-1}G)&\subseteq S\\
\\
\Rightarrow Im\big[G|FG|\ldots|F^{n-1}G\big]&\subseteq S
\end{align}
$$
Questo può anche essere interpretato come:
Se 2 sottospazi vettoriali $W1, W2$ sono inclusi in uno spazio vettoriale $V$ allora tutte le combinazioni lineari dei due vettori sono incluse in $V$ 


#### Proprietà 1
[[R7 Basis of vector spaces and algebraically equivalent system#Definition algebraically equivalent|Algebraically equivalent]] 
Due sistemi alg. equiv. hanno la stessa transfor matrix
$$
\begin{align}
\bar W(z)&=\bar H(zIm-F)^{-1}\bar G+\bar D\\
&=HT[zT^{-1}ImT-T^{-1}FT]^{-1}T^{-1}G+D\\
&=HT[T^{-1}(zIm-F)T]^{-1}T^{-1}G+D
\end{align}
$$
se $A$, $B$, $C$ sono 3 matrici non singolari quadrate allora possiamo dire che:
$[A\ B\ C]^{-1}=C^{-1}B^{-1}A^{-1}$ 
$$
\begin{align}
&=H\cancel{T\ T^{-1}}(zIm-F)^{-1}\cancel{T\ T^{-1}}G+D\\
&=H(zIm-F)^{-1}G+D=W(z)
\end{align}
$$
#### Proprietà 2 
C'è una relazione tra le reachability matrix di $\Sigma$ e $\bar\Sigma$  chiamate $\mathcal R$ e $\bar {\mathcal R}$ 
$$
\begin{align}
\bar {\mathcal R}&=[\bar G|\bar F\bar G|\ldots|\bar F^{n-1}\bar G]\\
&=\bar F^k\bar G=T^{-1}F^k\cancel{T\ T^-1}G=T^{-1}F^kG\\
&=[T^{-1}G|T^{-1}FG|\ldots|T^{-1}F^{n-1}G]\\
&=T^{-1}[G|FG|\ldots|F^{n-1}G]\\
&=T^{-1} {\mathcal R}
\end{align}
$$
- $\bar {\mathcal R}, {\mathcal R}$ matrici $n\times mn$
- $T^{-1}$ matricxe $n\times n$ 
Di conseguenza abbiamo che $\bar {\mathcal R}$ e ${\mathcal R}$ hanno lo stesso rango e quindi se $\Sigma$ è reachable lo è pure  $\bar\Sigma$
##### Remark
Se $m=1$ e $\Sigma$ e $\bar\Sigma$ reachables (è il caso di un sistema con un solo input) allora:
$\bar{\mathcal R}=T^{-1}{\mathcal R}\qquad\Rightarrow T\bar {\mathcal R}={\mathcal R}\qquad\Rightarrow T={\mathcal R}\bar{\mathcal R}^{-1}$ 
