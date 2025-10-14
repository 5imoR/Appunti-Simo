 #ST-L5
## Autonomous Case
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


# Rechability
#ST-L7 
[[Rechability and controllability problems]]
![[Non linear discrete time s.s.m.#Definition of d.t.s.s.m.]]

### Definition
Dato $k\in\mathbb Z,\ k>0$ uno stato $x_f\in X\in \mathbb R^n$ è detto *reachable* al tempo $t=k$ (in $k$ steps) se $\exists u(0),u(1),\dots u(k-1)\in U=\mathbb R^m$ che guida lo stato da $x(0)=\underline 0$  a $x(u)=x_f$ 
$$\large
(x(0)\xrightarrow[u(0),u(1),\dots,u(k-1)]{} x(k)=x_f)
$$
$$\begin{align}
\displaystyle x_k=x_f(k)&=\sum_{i=0}^kF^{k-1-i}Gu(i)\\
&=\begin{bmatrix}G|FG|F^2G|\dots|F^{k-1}G\end{bmatrix}\begin{bmatrix}u(k-1)\\u(k-2)\\\vdots\\u(0)\end{bmatrix}
\end{align}$$

$\begin{bmatrix}G|FG|F^2G|\dots|F^{k-1}G\end{bmatrix}$ è chiamata $\mathcal R_k$ (rechability matrix at time $k$)

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

Siccome ogni $X_k^R$  è un sottospazio vettoriale di $X$ e $X_k^R\subset X_{k+1}^R\Rightarrow dim X_{k+1}^R\geq dim X_k^R+1$ 
e quindi
$$
\exists \bar k\in \mathbb Z\quad \bar k >0\quad\text{ s.t.}\quad X_\bar k^R=X_k^R \quad \forall k\geq\bar k
$$
