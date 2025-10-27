# Controllability CT
#ST-L11 
[[Reachability and controllability problems]]
![[Linear contiunuous time s.s.m.#State equation]] 

### Definition
Dato un tempo $t>0$ uno stato $x_o\in X$ è detto controllable to 0 al tempo $t$ se $\exists u(\cdot)\in\mathcal U|_{[0,t]}$ 
$$
\large
(x(0)=x_0\xrightarrow[{u(\cdot)} ]{} x(t)=\underline 0)
$$
#### Recal
$x(t)=x_l(t)+x_f(t)=e^{Ft}x_0+R_tu(\cdot)$ 
####
$$
\begin{align}
(F,G) {\Large\substack{\text{ is controllable }\\\text{at time t>0}}}
&\iff \exists u(\cdot)\in \mathcal U|_{[0,t]}\ s.t.\quad 0=e^{Ft}x_0+R_tu(\cdot)\\
&\iff \exists u(\cdot)\in \mathcal U|_{[0,t]}\ s.t.\quad e^{Ft}x_0=-R_tu(\cdot)\\
&\iff e^{Ft}x_0\in Im\ R_t
\end{align}
$$
Se introduciamo il set $X^C_t$ degli stati di $X$ che sono controllabili a 0 in tempo  $t>0$ allora 
$$
X_t^C=\set{x\in X:e^{Ft}x\in Im\ R_t=X^R = Im\mathcal R}
$$
#### Proof
Vogliamo provare che  $\forall t>0\qquad X_t^C\equiv X^R)=Im \mathcal R$ 
1. $\begin{align}x\in X_t^C&\iff e^{Ft}x\in X^R\\&\iff x\in e^{-Ft}X^R\end{align}$ quindi $X_t^C=e^{-Ft}X^R$ 
2. $X^R$ è F-invariant 
	$$\begin{align}\displaystyle &\Rightarrow\quad FX^R\subseteq\dots\subseteq F^kX^R\subseteq X^R\Rightarrow\Large\underbrace{\sum_{k=0}^{+\infty}\left[F^k\frac {(-t)^k}{k!}\right]}_{e^{-Ft}}X^R\subseteq X^R\\&\Rightarrow \underbrace{e^{-Ft}X^R}_{\text{non singular }dim (e^{-Ft}X^R)=r}\subseteq X^R\rightarrow \text{supponiamo }X^R=r\end{align}$$
	Siccome $e^{-Ft}X^R$ è incluso in $X^R$ ed hanno la stessa dimensione allora coincidono
3. $X_t^C=e^{-Ft}X^R=X^R_t$ 