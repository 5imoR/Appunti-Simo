#ST-L6 ![[Non linear discrete time s.s.m.#Definition of d.t.s.s.m.]]
# Linearizzazione vicino ad un equilibrio
Assumiamo che:
1. $x_e\in X=\mathbb R^n$ è un eq. point corrispondente a $u(t)=\overline u$ 
2. $f(\cdot,\cdot)$ e $h(\cdot,\cdot)$ sono continue con le loro derivate parziali attorno ad $(x_e,\overline u)$

Definiamo
- $\delta(x(t))\triangleq x(t)-x_e$
- $\delta(u(t))\triangleq u(t)-\bar u$
- $\delta(y(t))\triangleq y(t)-y_e$
#### Matrici della state equation
Tramite la seconda assunzione possiamo usare l'espansione di [[Taylor]] di  e   attorno a $(x_e,\overline u)$ 
$$
\begin{align}
x(t+1)&=f(x(t),u(t)) \\
\cancel{x_e+}\delta x(t+1)&= f(x_e+\delta x(t),\bar u+\delta u(t))\\
Taylor\ expansion&= \cancel{f(x_e,\bar u)}+
\left.\frac{\partial f}{\partial x}\right|_{\substack{x = x_e \\ u = u_e}}\delta x(t)+
\left.\frac{\partial f}{\partial u}\right|_{\substack{x = x_e \\ u = u_e}}\delta u(t)+
o(\delta_x,\delta_u)
\end{align}
$$


- andiamo ad approssimare escludendo $o(\cdot)$
- $F=\displaystyle\left.\frac{\partial f}{\partial x}\right|_{\substack{x = x_e \\ u = u_e}}$ è una matrice $n\times n$ dove al posto $i,j$ è $\displaystyle\frac{\partial f_i}{\partial x_j}$
 - $G=\displaystyle\left.\frac{\partial f}{\partial u}\right|_{\substack{x = x_e \\ u = u_e}}$ è una matrice $m\times m$ dove al posto $i,j$ è $\displaystyle\frac{\partial f_i}{\partial u_j}$


$\Rightarrow$ Un (approximate) linear s.s.m.  per descrivere le dinamiche dei vettori è:
$$\delta x(t+1)=F\ \delta x(t)+G\ \delta u(t)$$
$F,G$ sono dette matrici Jiacobiane $J$ di $f$ a rispetto di $x$ e $u$


#### Matrici  della output equation
In modo analogo otteniamo:
$$
\begin{align}
y(t)&=h(x(t),u(t)) \\
\cancel{y_e+}\delta y(t)&= h(x_e+\delta x(t),\overline u+\delta u(t))\\
Taylor\ expansion&= \cancel{h(x_e,\overline u)}+
\left.\frac{\partial h}{\partial x}\right|_{\substack{x = x_e \\ u = u_e}}\delta x(t)+
\left.\frac{\partial h}{\partial u}\right|_{\substack{x = x_e \\ u = u_e}}\delta u(t)+
\tilde o(\delta_x,\delta_u)
\end{align}
$$


- andiamo ad approssimare escludendo $o(\cdot)$
- $H=\displaystyle\left.\frac{\partial h}{\partial x}\right|_{\substack{x = x_e \\ u = u_e}}$ è una matrice $n\times n$ dove al posto $i,j$ è $\displaystyle\frac{\partial h_i}{\partial x_j}$
 - $D=\displaystyle\left.\frac{\partial h}{\partial u}\right|_{\substack{x = x_e \\ u = u_e}}$ è una matrice $m\times m$ dove al posto $i,j$ è $\displaystyle\frac{\partial h_i}{\partial u_j}$
$\Rightarrow$ $$\delta y(t)=H\ \delta x(t)+D\ \delta u(t)$$ $H,D$ sono dette matrici Jiacobiane $J$ di $h$ rispetto a $x$ e $u$

### Preposition \[Linearization method]
Consideriamo un non linear d.t. autonomous s.s.m.
$x(t+1)=f(x(t))\quad t\in \mathbb Z+\quad dim(x)=n\quad (A)$
assumiamo:
- $x_e$ è un punto d'equilibrio di $(A)$
- $f$ è continua nelle sue derivate parziali
Allora se  mettiamo $\delta x(t)\triangleq x(t)-x_e$ abbiamo il modello linearizzato:
$$
\delta x(t+1)=F\ \delta x(t)\quad\text{ dove }F\triangleq\left.\frac{\partial f}{\partial x}\right|_{x = x_e }
$$
Allora:
1. se $F$ è shur stable( $|\lambda|<1$ ) allora $x_e$ è un asymptotic stable equilibrium point di $(A)$
	$|\lambda|<1$ è come dire $-1<\lambda<1$ 
2. se $\exists \lambda\in\sigma(F)$ con $|\lambda|>1$ allora $x_e$ NON è un equilibrium point di $(A)$
3. se $\exists \lambda\in\sigma(F)$con $|\lambda|=1$ e nessun autovalore con $|\lambda|>1$ allora non possiamo dire nulla riguardo $x_e$ 
	questo è dovuto all'approssimazione di o-piccolo
![[lambdaEqLG|700]]
### Nota
Se la trace (ovvero la diagonale sommata $F_{11}+F_{22}...$) è maggiore di $1$ allora $\lambda$ non possono essere di modulo $<1$

#### Esercizio 1
Consideriamo il d.t. n.l. s.s.m
$$
\begin{align}
&x_1(t+1)=f_1(x_1(t),x_2(t),u(t))=x_1(t)[x_2(t)+1]+x_1(t)u(t)\\
&x_2(t+1)=f_2(x_1(t),x_2(t),u(t))=x_1(t)x_2^2(t)
\end{align}
$$
Determinare:
- $\forall\overline u\in \mathbb R$ il punto di equilibrio $x_e\in \mathbb R^2$ corrispondente a $u(t)=\overline u$ 
	Mettiamo: $u(t)=\overline u,\quad x(t)=x(t+1),\quad x_e=(x_1,x_2)$ 
	allora la condizione di equilibrio è determinata da:
	$$
	\begin{cases}
	x_1=f_1(x_1,x_2,\overline u)=x_1x_2+x_1-x_1\overline u&\\
	x_2=f_2(x_1,x_2,\overline u)=x_1x_2^2&\\
	\end{cases}
	\begin{cases}
	0=x_1x_2+x_1-x_1-x_1\overline u&\\
	0=(x_1x_2-1)x_2&\\
	\end{cases}
	$$
	Dalla prima equazione abbiamo due soluzioni:
	1. $x_1=0$
		$x_2=0\Rightarrow x_e=(\underline0,\underline0)\qquad\forall\overline u \in \mathbb R$ 
	2. $x_2=-\overline u$ 
		$0=x_1\overline u^2+\overline u$ 
			$\overline u=0\quad \forall x_1\in \mathbb R$
			$x_1=-1/\overline u$ 
		Quindi possiamo dire che abbiamo un equilibrio in
		$x_e(x_1,0)\ x_1\in\mathbb R$      per $\overline u=0$ 
		$x_e(0,0)\land(\frac{-1}{\overline u},-\overline u)$ per $\overline u\neq 0$ 
- Il modello linearizzato per ogni equazione di equilibrio
	
	$\delta x(t+1)=F\ \delta x(t)+G\ \delta u(t)$ 
	$$\large
	F=\begin{bmatrix}
	\frac{\partial f_1}{\partial x_1}&\frac{\partial f_1}{\partial x_2}\\
	\frac{\partial f_2}{\partial x_1}&\frac{\partial f_2}{\partial x_2}\\
	\end{bmatrix}=
	\begin{bmatrix}
	x_2+1+\overline u&x_1\\
	x_2^2&2x_1x_2{\color{orange}-1}
	\end{bmatrix}
	$$
	- Caso1  $\overline u =0\quad x_e(x_1,0)\quad\forall x_1\in\mathbb R$  
	$$F=\begin{bmatrix}
	1&x_1\\0&0
	\end{bmatrix}$$
	
	- Caso2 $\overline u \neq0\quad x_e(0,0)$
	$$
	F=\begin{bmatrix}
	1+\overline u &0\\0&0
	\end{bmatrix}
	$$
	- Caso3 $\overline u\neq0\quad x_e(\frac{-1}{\overline u},-\overline u)$
	$$
	F=\begin{bmatrix}
	1&\frac{-1}{\overline u}\\
	\overline u^2&2
	\end{bmatrix}
	$$
---
#### Esercizio 2
Consideriamo 
$$
\begin{align}
&x_1(t+1)=f_1(x_1(t),x_2(t),u(t))=x_1(t)x_2(t)\\
&x_2(t+1)=f_2(x_1(t),x_2(t),u(t))=\frac 1 2 x_2(t)- x_1(t)x_2(t)
\end{align}
$$
Determinare e studiare se sono asymptoticaly stable (se possibile) tramite la linearizzazione

**Equilibrio**
$$
	\begin{cases}
	x_1=x_1x_2\\
	x_2=\frac 1 2 x_2- x_1x_2
	\end{cases}\ \ \ \ 
	\begin{cases}
	0=x_1(x_2-1)\\
	0=\frac 1 2 x_2+ x_1x_2
	\end{cases}
$$
Dalla prima otteniamo:
- $x_1=0\longrightarrow x_2=0\quad x_e(0,0)$
- $x_2=1\longrightarrow x_1=-\frac 1 2\quad x_e(-\frac 1 2,1)$ 
$$\large
F=\begin{bmatrix}
	\frac{\partial f_1}{\partial x_1}&\frac{\partial f_1}{\partial x_2}\\
	\frac{\partial f_2}{\partial x_1}&\frac{\partial f_2}{\partial x_2}\\
	\end{bmatrix}=
	\begin{bmatrix}
	x_2&x_1\\
	x_2&\frac 1 2 {\color{orange}-}x_1
	\end{bmatrix}
$$
- $x_e=(0,0)\rightarrow F=\begin{bmatrix}0&0\\	0&\frac 1 2 \end{bmatrix}$     $\sigma(F)=(0,\ 1/2)$  quindi $x_e(0,0)$ è un punto asymptoticaly stable del sistema non lineare
- $x_e=(0,0)\rightarrow F=\begin{bmatrix}1&-\frac 1 2\\	-1&1 \end{bmatrix}$  non è un punto asintoticamente stabile
