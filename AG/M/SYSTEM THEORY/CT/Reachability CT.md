#ST-L11 [[R6 Inner product and ortogonality and adjoint#Definition Adjoint]]
[[Reachability and controllability problems]]
![[Linear contiunuous time s.s.m.#Linear CT ssm#State equation]]
### Definition
Dato un tempo $t> 0$  uno stato $x_f\in X=\mathbb R^n$ è reachable in $t$ se $\exists u(\cdot)\in\mathcal U|_{[0,t]}$ (set of piece wise continuous function definito in$[0,t]$ e con i valori in $U=\mathbb R^n$ ) che guida lo stato del sistema da $x(0)=\underline 0$ a $x(t)=x_f$
$$\large
(x(0)\xrightarrow[{u(\cdot)} ]{} x(t)=x_f)
$$

Da       $x(t)=x_f(t)=\int_0^te^{F(t-\tau}Gu(\tau)d\tau$    possiamo definire che:

$$
\begin{align}
\substack{x_f\text{ is reachable}\\\text{at time t}}
&\iff\exists u\in \mathcal U|_{[0,t]}\ s.t.\ x_f= \int_0^te^{F(t-\tau}Gu(\tau)d\tau\\
&\iff\exists u\in \mathcal U|_{[0,t]}\ s.t.\ x_f= R_tu(\cdot)\iff x_f\in Im R_t
\end{align}
$$
Introduciamo una mappa:
$$
\begin{aligned}
R_t &:~ \mathcal U|_{[0,t]} \xrightarrow[ ]{\hspace{2.4cm} }X = \mathbb{R}^n\\
    &:~ u(\tau),~ \tau\in[0,t] \xmapsto[]{\hspace{0.5cm}} \int_0^t{\color{orange}e^{F(t-\tau)}G}u(\tau)d\tau\qquad \qquad\color{orange} =M(\tau)
\end{aligned}
$$
Se denominiamo $x_t$ il set degli stati che sono raggiungibili in un tempo $t$ allora 
$$X_t^R\equiv Im R_t$$
Osserviamo che $\mathcal U|_{[0,t]}$ e $X$ sono spazi vettoriali reali e che:
$$R_t(\alpha_1u_1(\cdot)+\alpha_2u_2(\cdot))=\alpha_1R_t(u_1(\cdot))+\alpha_2R_t(u_2(\cdot)) $$
$\Rightarrow R_t$ è una trasformazione lineare
$\Rightarrow Im R_t$  è un sottospazio vettoriale di $X=\mathbb R^n$  ed è uno finite dimensional vector space
Possiamo introdurre l'inner product [[R6 Inner product and ortogonality and adjoint#Caso 2|caso 2]] 
$$
<u_1,u_2>_{\mathcal U|_{[0,t]}}\triangleq\int_0^tu_1^T(\tau)u_2(\tau)d\tau
\qquad \forall u_1(\cdot),u_2(\cdot)\in \mathcal U|_{[0,t]}
$$
$$
<x_1,x_2>_X\triangleq x_1^Tx_2\qquad \forall x_1,x_2\in X
$$
Riferendoci al [[R6 Inner product and ortogonality and adjoint#Caso 2|caso 2]] possiamo dire che l'adjoint trasformation di $R_t^*$ esiste
$$
\begin{aligned}
R_t &: X \xrightarrow[ ]{\hspace{1cm} }\mathcal U|_{[0,t]}= \mathbb{R}^n\\
    &: x \xmapsto[]{\hspace{1cm}} G^Te^{F^T(t-\tau)}x,\quad\tau\in [0,t]
\end{aligned}
$$
Sfruttando il fatto che $ImR_t$ ha una dimensione finita ed usando le [[R6 Inner product and ortogonality and adjoint#Proprietà|proprietà dell'adjoint trasformation]] possiamo dire che:
$$
Im\ R_t\equiv Im(R_tR^*_t)
$$
Cos'è $R_tR^*_t$?
#### Gramiant
$$
\begin{aligned}
R_t &: X \xrightarrow[R_t^* ]{\hspace{1cm} }\mathcal U|_{[0,t]}\xrightarrow[R_t ]{\hspace{1.8cm} } X\\
    &: x \xmapsto[]{\hspace{1cm}} \substack{G^Te^{F^T(t-\tau)}x\\\tau\in [0,t]}\xmapsto[]{\hspace{1cm}}
    \huge\underbrace{\left[\int_0^te^{F(t-\tau)}GG^Te^{F^T(t-\tau)}d\tau\right]}_{\substack{\triangleq W_t\in \mathbb R^{n\times n}\\\text{Reachability gramiant at time t}}}x
\end{aligned}
$$
Di conseguenza  $\forall t>0$
$$
X_t^R =Im(R_t)=Im(R_tR_t^*)=Im(W_t)
$$
### Proposition
per ogni $t>0$ 
$X_t^R=Im(R_t)=Im(R_tR_t^*)=Im(W_t)=\mathcal R$ 
dove $\mathcal R= [ G|FG|...|F^{n-1}G]$  è la reachability matrix
#### Proof 
Vogliamo provare che  $\forall t>0\quad Im R_t=Im\ \mathcal R$ siccome sono entrambi sottospazi vettoriali di $\mathbb R^n$ questo è l'equivalente di provare $(Im\ R_t)^\perp=(Im\ \mathcal R)^\perp$ 

##### Recall
$\ker \mathcal A=(Im \mathcal A^*)^\perp$ e il risultato è sempre vero se invertiamo $\mathcal A$ e $\mathcal A^*$ ($\ker \mathcal A^*=(Im \mathcal A)^\perp$)
#####
Possiamo dire che $\ker R_t^*=\ker \mathcal R^T$
$$
\begin{align}
x\in \ker R_t^*&\iff R_t^*x=0\in\mathcal U|_{[0,t]}\rightarrow\text{zero function}\\
&\iff G^T e^{F^T(t-\tau)}n=0
&\forall\tau\in [0,t]\\
&\iff G^T\sum_{k=0}^{+\infty}\left[(F^T)^k\frac {(t-\tau)^k}{k!}\right]x=0 &\forall\tau\in [0,t]\\
&\iff\sum_{k=0}^{+\infty}\left[G(F^T)^kx\right]\frac {(t-\tau)^k}{k!}=0
&\forall\tau\in [0,t]\\
&\overset{*}{\iff} G^T(F^T)^kx=0\qquad \forall k\in \mathbb Z_+\\
&\iff G^T(F^T)^kx=0\qquad k=0,1,\dots,n-1
\end{align}
$$
	l'ultimo $\iff$ $\Rightarrow$  ovvio $\Leftarrow$ [[Cayley-Hamilton's theorem]]
\* se questo è il caso l'espressione è la zero function ed ha un'unica  *power series expansion* (tutti i coefficienti devono essere $0$) Principle of identity of power series
$$
\iff
\begin{bmatrix}
G^T\\G^TF^T\\\vdots\\G^T(F^T)^{n-1}
\end{bmatrix}_{\mathcal R_*^T}
x=\begin{bmatrix}
0\\0\\\vdots\\0
\end{bmatrix}
\iff x\in \mathcal R^T
$$
#### Conseguenza
Se  chiamiamo  $X^R$ il più piccolo set di stati che possono essere raggiunti (dal CT system) in un tempo finito allora 
$$
X^R=X^R_t=Im \mathcal R 
$$
è il più piccolo spazio F-invariant incluso in $Im\ G$ 
Diciamo che in tempo continuo è reachable se $X^R=\mathbb R^n$ ovvero
$$(F,G)\text{è reachable}\iff rank \mathcal R=n$$
