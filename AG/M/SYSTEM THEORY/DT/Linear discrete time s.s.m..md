[[Linearization of a n.l. discrete time s.s.m.]] [[Zeta Transform (Z-trans)]]
## Linear DT ssm

$$
\begin {align}
&\begin{cases}
x(t+1)=Fx(t)+Gu(t)\qquad\qquad\qquad&t\in \mathbb Z+\\\\
y(t)=Hx(t)+Du(t)
\end{cases}
\end{align}
$$
$dim\ x=n\quad dim\ u=m\quad dim\ y=p\quad$ 
- $F\in R^{n\times n}$ State Matrix
- $G\in R^{m\times m}$ Input Matrix
- $H\in R^{p\times n}$ Output Matrix
- $D\in R^{p\times m}$ Feedforward Matrix


## Ripasso di State Space Models a tempo discreto
#ST-L1
Sono definiti dalla seguente equazione differenziale:
$$
\begin{align}
&\begin{cases}
x(t+1)&=Fx(t)+Gu(t) &State\ equation  \\
y(t)&=Hx(t)+Du(t)   &Output\ equation\\
\end{cases}
\\\\
&x(t)\in \mathbb{R}^n\triangleq X\qquad is\ the\ state\ variable\\
&u(t)\in \mathbb{R}^m\triangleq U\qquad is\ the\ input\\
&y(t)\in \mathbb{R}^p\triangleq Y\qquad is\ the\ output\\
\end{align}
$$
Il sistema può essere rappresentato in maniera compatta come:
$$
\Sigma=(F,G,H,D)
$$
E per dimensione di $\Sigma$ si intende la dimensione della state variable ovvero $n$
$\Sigma$ è:
- Linear
- Time Invariant (lo consideriamo dinamico da $t=0,\quad t\in \mathbb{Z}$)
- Proper: il grado del numeratore è $\leq$ di quello al denominatore

In caso $D=0$ ($D$ è la FeedForward Matrix) il sistema è "Strictly Proper" e per semplicità lo scriveremo:
$$
\Sigma=(F,G,H)
$$
![[BlockDiagramOfDTSSM|600]]
- $F\in R^{n\times n}$ State Matrix
- $G\in R^{m\times m}$ Input Matrix
- $H\in R^{p\times n}$ Output Matrix
- $D\in R^{p\times m}$ Feedforward Matrix

Il polinomio caratteristico di $F$ è $\triangle_F(Z)\triangleq det(zIm-F) = z^n+a_{n-1}z^{n-1}+...a_1\ z\in \mathbb{R}[z]$ 

Un polinomio si dice *monic* se il coefficiente di $z^n$ è $1$ 

Il grado(degree) del polinomio è $deg\triangle_F(z)=n$ 

Gli zeri di $\triangle_F(z)$ sono gli autovalori della matrice $F$
Se prendiamo gli autovalori distinti di $F$ come $\lambda_1,\lambda_2...\lambda_r\in \mathbb{C}$ allora avremo:
$$
\triangle_F(z) = (z-\lambda_1)^{n1}(z-\lambda_2)^{n2}...(z-\lambda_r)^{nr}
$$
Dove $n1, n2,...,nr$ sono interi positivi chiamati molteplicità algebrica di $\lambda_1,\lambda_2...\lambda_r$ 


### Espressione di *state and output* ad un tempo generico $t>0$
Usando il concetto di [[Power of a Square Matrix and Jordan Form|potenza di una matrice]] possiamo dire che:
$$
\Large
\begin{align}
x(t) &= 
\underbrace{F^t x(0)}_
{\text{unfroced/free state evolution }x_l(t)} + 
\underbrace{\sum_{k=0}^{t-1} F^{t-1-k} G u(k)}_
{\text{forced state evolution}x_f(t)} \\
y(t) &=
\underbrace{H F^t x(0)}_{\text{unforced/free output evolution }y_l(t)}  + \underbrace{\sum_{k=0}^{t-1} HF^{t-1-k}Gu(k)+Du(t)}_{\text{forced output evolution}y_f(t)}
\end{align}
$$

### Impulse response
#ST-L2
Unitary Discrete Time Inpulse (Kronecker delta)

| $\delta(t)\triangleq\begin{cases}1\qquad t=0\\0\qquad t\neq0\end{cases}$          | ![[dirac\|200]]   |
| --------------------------------------------------------------------------------- | ----------------- |
| $\delta_{-1}(t)\triangleq\begin{cases}0\qquad t<0\\1\qquad t\geq0\end{cases}$<br> | ![[dirac-1\|200]] |
nel caso di $\delta_{-1}(t)\rightarrow W(t)\triangleq D\delta(t)+HF^{t-1}G\delta_{-1}(t-1)$
#### Caso m=1 (m=numero di inpulsi)
${\color{orange}{x(0)=0}}\quad u(t)=\delta(t)$
$$
\begin{align}

&y(0)={\color{orange}{\cancel{Hx(0)}}}+Du(0)=D\\\\
&x(1)={\color{orange}{\cancel{Fx(0)}} }+Gu(0)=\color{lightgreen}G\\
&y(1)=H{\color{lightgreen}x(1)} +\cancel{Du(1)}=HG
\\\\
&x(2)=F{\color{lightgreen}x(1)}+\cancel{Gu(1)}={\color{lightblue}FG}\\
&y(2)=H{\color{lightblue}x(2)} +\cancel{Du(2)}=HFG
\\\\
\end{align}
$$
In generale:
$$
y(t)=
\begin{cases}
D\qquad\qquad t=0\\
HF^{t-1}G\quad t\geq1
\end{cases}
$$

#### Caso m>1
${x(0)=0}\quad u(t)=e_i\delta(t)$
dove $e_i$ è l'$i$ esimo vettore della base canonica $e_2=\begin{bmatrix}0\\1\\0\end{bmatrix}$ 
$$
y(t)=
\begin{cases}
De_i=col_i(D)\qquad\qquad\qquad\quad\ \ t=0\\
(HF^{t-1}G)e_i=col_i(HF^{t-1}G)\quad t\geq1
\end{cases}
$$
$\Rightarrow w(t)\triangleq D\delta(t)+HF^{t-1}G\delta_{-1}(t-1)$ 


*what?*
Richiamando la convoluzione di due sequenze a tempo discreto:
$$
t\in \mathbb{Z}:[V_1+V_2](t)\triangleq\sum_{k=0}^tV_1(t-k)V_2(k)\qquad t\in\mathbb{Z}
$$
possiamo vedere che:
$$
\begin{align}
y_F(t)&\triangleq[W+u](t)=\sum_{k=0}^t W(tk)u(k)\\
&\triangleq\sum_{k=0}^{t-1}W(t-k)u(k)+W(0)u(t)
\end{align}
$$

## Autonomous Case
#ST-L5
Supponiamo di avere un d.t. s.s.m. lineare autonomo
$$x(t+1)=Fx(t)+\cancel{Gu(t)}$$ 
Allora ad effetto a cascata possiamo dire che:
	sono tutti se e solo se che non sapevo come emttere
$x_e\in X=\mathbb R^n$  è un punto di equilibrio
$x_e=Fx_e$ 
$(In-F)x_e=0$
$x_e\in \ker(In-F)$ 
$x_e$ è un autovettore di $F$ corrispondente a $\lambda=1$

#### Caso 1 $\lambda=1\in\sigma(F)$ 
Se siamo in questo caso allora $\ker(In-F) contiene un numero infinito di elementi. 
Infatti se:
$\overline x \in \ker(In-F)$ allora
$\alpha \overline x \in \ker(In-F)\quad\forall\alpha\in\mathbb R$ 
![[case1eqpoint|300]]
se $x(0)= x_0=\alpha \overline x$ allora $x(t)\equiv x_0 \forall t\geq 0 \Rightarrow x(t)\cancel{\rightarrow}\overline x$ per $t\rightarrow +\infty$       
i punti di equilibrio non possono essere attractive poichè ci sarebbere diversi eq. point in $\overline \delta$ 
Possono cumunque essere stabili

#### Caso 2 $\lambda=1\notin\sigma(F)$ 
L'origine è sempre un punto di equilibrio del sistema.
In questo caso l'origine è l'unico punto di equilibrio $x_e=\underline 0$ 

Quand'è che $x_e$ è attrattivo?
Se e solo se $||x(0)||$ è sufficientemente piccolo che $x(t)\rightarrow 0$ per $t\rightarrow +\infty$ 

Sappiamo che:
$$
\begin{align}
x(t)&=x_e(t)=F^tx_0\\
&=TJ^tT^{-1}x_0
\end{align}
$$
Le elementary modes distinte saranno del tipo 
- $\delta(t),\delta(t-1)...$ se $0\in\sigma(F)$ 
- $\displaystyle\tilde{P_k}(t){\color{orange}\lambda^t}=\binom{t}{k}\lambda^{t-k}$ se $\lambda\in\sigma(F)$ 
	Polinomio in $t$ di grado $k$

$\displaystyle\binom{t}{k}\lambda^{t-k}$  ha 3 casi
- converge a $0$ se $|\lambda|<1$ 
- è bounded se $|\lambda|<1$ oppure $|\lambda|=1 \wedge k=0$ (and)
- diverge in ogni altro caso
$$x_e=0\Leftrightarrow \forall\lambda\in\sigma(F)\ \ $$
In d.t. systems $x_e$ è attrattivo e stabile
se$|\lambda|<1$  $F$ si dice Shur stable

Nel caso lineare se $x_e=\underline 0$ è un attractive equilibrium point e pure stable.

$$
\Rightarrow \Sigma \text{ è asymptoticaly stable }\Leftrightarrow \lambda\in\sigma(F)\quad|\lambda|<1
$$

$$
\begin{align}
&\Sigma \text{ è stabile }\Leftrightarrow \forall\lambda\in\sigma(F) \\
\text{ e}\\\quad &|\lambda|<1\quad\\\text{ oppure }\\&|\lambda|=1\ \text{e tutti i J mini-block associati hanno dimensione 1 } n_{i1}=1
\end{align}
$$



