[[Linearization of a n.l. continuous time s.s.m.]] [[Laplace Transform]]
## Definition

## Ripasso di State Space Models a tempo continuo
#ST-L4
Sono definiti dalla seguente equazione differenziale:
$$
\begin{align}
&t\in \mathbb R+\\
&\begin{cases}
\dot{x}(t)&=Fx(t)+Gu(t) &State\ equation &1^{st}\text{ order diff. equation} \\
y(t)&=Hx(t)+Du(t)   &Output\ equation    &\text{static equation}\\
\end{cases}
\\\\
&x(t)\in \mathbb{R}^n\triangleq X\qquad\ \text{is the istate variable }\\
&u(t)\in \mathbb{R}^m\triangleq U\qquad \text{is the input }\\
&y(t)\in \mathbb{R}^p\triangleq Y\qquad\ \text{is the output }t\\
\end{align}
$$
Il sistema può essere rappresentato in maniera compatta come:
$$
\Sigma=(F,G,H,D)
$$
E per dimensione di $\Sigma$ si intende la dimensione della *state variable* ovvero $n$
$\Sigma$ è:
- Linear
- Time Invariant (lo consideriamo dinamico da $t=0,\quad t\in \mathbb{Z}$)
- Proper: il grado del numeratore è $\leq$ di quello al denominatore

In caso $D=0$ ($D$ è la FeedForward Matrix) il sistema è "Strictly Proper" e per semplicità lo scriveremo:
$$
\Sigma=(F,G,H)
$$
![[BlockDiagramOfCTSSM|600]]
- $F\in R^{n\times n}$ State Matrix
- $G\in R^{m\times m}$ Input Matrix
- $H\in R^{p\times n}$ Output Matrix
- $D\in R^{p\times m}$ Feedforward Matrix

se conosciamo $x(0)=x_0\in X$ e $u(t)\quad t\in \mathbb R+$ qual'è l'espressione di $x(t)$ e $y(t)$?
Usando il concetto di [[Exponential Matrix|matrice esponenziale]] possiamo dire che:
$$\Large
\begin{align}
&{\color{lightgreen} x(t)}=\underbrace{e^{Ft}x_0}_{x_l(t)}
+\underbrace{\int_0^te^{F(t-z)}Gu(\tau)d\tau}_{x_f(t)}\\
&y(t)=\underbrace{H{\color{lightgreen}e^{Ft}x_0}}_{y_l(t)}
{\color{lightgreen}+}\underbrace{{\color{lightgreen}\int_0^tHe^{F(t-\tau)}Gu(\tau)d\tau}+Du(t)}_{y_f(t)}
\end{align}
$$

### Impulse Response
$$
\begin{align}
&W(t)\triangleq D\delta(t)+He^{Ft}Gd_{-1}(t) \\
&y_f(t)=[W(t)*u](t)=\int_0^tW(\tau)u(t-\tau)d\tau=\int_0^tW(t-\tau)u(\tau)d\tau
\end{align}
$$

## Autonomous Case
#ST-L7 
Supponiamo di avere un c.t. s.s.m. lineare autonomo
$\dot x(t)=Fx(t)\quad t\in \mathbb R+\quad dim(x)=n\quad (A)$
Si puo dire che:
1. $x_e$ è un punto di d'equilibrio di $(A)\iff0=Fx_e$ 
2. $x_e=\underline 0$ è sempre un punto di equilibrio
3. $\exists x_e\neq\underline 0$ che è un punto di equilibrio del sistema
	equivale a dire uno di questi
	$\iff \ker F\supsetneq \{\underline 0\}$
	$\iff F$ è singular
	$\iff o\in \sigma(F)$    
4. $x_e=0$ è un punto d'equilibrio attrattivo $\iff \forall x_0\ x_l(t)=e^{Ft}x_0\rightarrow 0$ per $t\to+\infty$ 
	
	equivalentemente tutte le elementary modes associate ad $e^{Ft}$ (come anche $F$)  convergono a $0$ per $t\to+\infty$.
	$\large\displaystyle{\frac{t^k}{k!} e^{\lambda it}}$  $\forall i\quad R_e(\lambda_i)<0\iff\lambda\in\sigma(F), Re(\lambda)<0$
	A tempo discreto  per essere attrattivo deve essere interno al cerchi a tempo continuo deve la parte reale deve essere minore di $0$ ![[ct vs dt]]
5. $x_e$ è un punto d'equilibrio stabile $\iff$ le elementary modes di $F$ sono bounded
	
	Sia in DT che CT puoi avere autovalori sulla boundary se hanno solo un elementary mode
	$\iff \forall i\ Re(\lambda_i)\leq 0$  e se $Re(\lambda_i)=0$ allora c'è solo un elementary mode associata a $\lambda_i$ in altre parole la i miniblock associati sono tutti scalari
6. Il sistema è (asintoticamente) stabile se $x_e=0$ è(asintoticamente) stabile

# Rechability
