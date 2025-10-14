#ST-L7 ![[Non linear continuous time s.s.m.#Definition]]
# Linearizzazione vicino ad un equilibrio
Assumiamo che:
1. $x_e\in X=\mathbb R^n$ è un eq. point corrispondente a $u(t)=\overline u$ 
	$\Rightarrow 0=f(x_e,\bar u)$ e $y(t)=y_e\triangleq h(x_e,\bar u)$   
2. $f(\cdot,\cdot)$ e $h(\cdot,\cdot)$ sono continue con le loro derivate parziali attorno ad $(x_e,\overline u)$

Definiamo
- $\delta(x(t))\triangleq x(t)-x_e$
- $\delta(u(t))\triangleq u(t)-\bar u$
- $\delta(y(t))\triangleq y(t)-y_e$
#### Matrici della state equation
Tramite la seconda assunzione possiamo usare l'espansione di [[Taylor]] di  e   attorno a $(x_e,\overline u)$ 
$$
\begin{align}
\frac d{dt}[\delta x(t)]=\frac d{dt}[x(t)]&= f(x_e+\delta x(t),\bar u+\delta u(t))\\
Taylor\ expansion&= 
\left.\frac{\partial f}{\partial x}\right|_{\substack{x = x_e \\ u = u_e}}\delta x(t)+
\left.\frac{\partial f}{\partial u}\right|_{\substack{x = x_e \\ u = u_e}}\delta u(t)+
o(\delta_x,\delta_u)
\end{align}
$$


- andiamo ad approssimare escludendo $o(\cdot)$
- $F=\displaystyle\left.\frac{\partial f}{\partial x}\right|_{\substack{x = x_e \\ u = u_e}}$ è una matrice $n\times n$ dove al posto $i,j$ è $\displaystyle\frac{\partial f_i}{\partial x_j}$
 - $G=\displaystyle\left.\frac{\partial f}{\partial u}\right|_{\substack{x = x_e \\ u = u_e}}$ è una matrice $m\times m$ dove al posto $i,j$ è $\displaystyle\frac{\partial f_i}{\partial u_j}$

$F,G$ sono dette matrici Jiacobiane $J$ di $f$ a rispetto di $x$ e $u$


#### Matrici della output equation
In modo analogo otteniamo:
$$
\begin{align}
\delta y(t)&= H\ \delta x(t)+ D\ \delta u(t)\\
Taylor\ expansion&= 
\left.\frac{\partial h}{\partial x}\right|_{\substack{x = x_e \\ u = u_e}}\delta x(t)+
\left.\frac{\partial h}{\partial u}\right|_{\substack{x = x_e \\ u = u_e}}\delta u(t)+
\tilde o(\delta_x,\delta_u)
\end{align}
$$


- andiamo ad approssimare escludendo $o(\cdot)$
- $H=\displaystyle\left.\frac{\partial h}{\partial x}\right|_{\substack{x = x_e \\ u = u_e}}$ è una matrice $n\times n$ dove al posto $i,j$ è $\displaystyle\frac{\partial h_i}{\partial x_j}$
 - $D=\displaystyle\left.\frac{\partial h}{\partial u}\right|_{\substack{x = x_e \\ u = u_e}}$ è una matrice $m\times m$ dove al posto $i,j$ è $\displaystyle\frac{\partial h_i}{\partial u_j}$

 $H,D$ sono dette matrici Jiacobiane $J$ di $h$ rispetto a $x$ e $u$
 
### Preposition \[Linearization method]
Consideriamo un non linear c.t. autonomous s.s.m.
$\dot x(t)=f(x(t))\quad t\in \mathbb R+\quad dim(x)=n\quad (A)$
assumiamo:
- $x_e$ è un punto d'equilibrio di $(A)$
- $f$ è continua nelle sue derivate parziali
Allora se  mettiamo $\delta x(t)\triangleq x(t)-x_e$ abbiamo il modello linearizzato:
$$
\frac d {dt}[\delta x(t)]=F\ \delta x(t)\quad\text{ dove }F\triangleq\left.\frac{\partial f}{\partial x}\right|_{x = x_e }
$$
Allora:
1. se $\forall \lambda\in \sigma (F), Re(\lambda)<0$ allora $x_e$ è un asymptotic stable equilibrium point di $(A)$
2. se $\exists \lambda\in\sigma(F)$ con $Re(\lambda)>0$ allora $x_e$ NON è un equilibrium point di $(A)$
3. se $\nexists \lambda\in\sigma(F)$con $Re(\lambda)>0$ ma $\exists \lambda\in \sigma(F)$ con $Re(\lambda)=0$ allora non c'è modo di sapere se è un equilibrio
	questo è dovuto all'approssimazione di o-piccolo
![[lambda eqlg |700]]
