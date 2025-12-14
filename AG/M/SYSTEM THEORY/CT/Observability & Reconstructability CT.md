#ST-L25-3
## Observability of CT ssm
Consideriamo  ![[Linear contiunuous time s.s.m.#Strictly Proper]]
### Definition \[undistinguishable]
Dati due stati $x_1,x_2\in X=\mathbb R^n$  diciamo che $x_1$ è *undistinguishable* da $x_2$ in $[0,T]\quad T>0$  $(x_1\mathop{\simeq}\limits_{[0,T]}x_2)$   se la unforced output evolution che deriva da $x(0)=x_1$ e $x(0)=x_2$  diciamo  $y_{1l}(t)$ e $y_{2l}(t)$ , rispettivamente,  coincidono ad ogni istante $t\in [0,T]$ 
In altre parole:
$$
x_1\mathop{\simeq}\limits_{[0,T]}x_2\iff He^{Ft}x_1=y_{1l}(t)=y_{2l}(t)=He^{Ft}x_2\quad \forall t\in [0,T]
$$
Introduciamo la trasformazione lineare:
$$
\begin{align}
 w_T:X=\mathbb R^n&\to Y|_{[0,T]}\\
x&\to He^{Ft}x\quad \forall t\in [0,T]
\end{align}
$$
Il set di piece-wise funzioni continue definito da $[0,T]$ che prendono i valori in $Y=\mathbb R^p$ 
Allora si ha: $x_1\mathop{\simeq}\limits_{[0,T]}x_2\iff w_Tx_1\equiv w_Tx_2$ 
### Definition \[unobservable]
Uno stato $x_0\in X$ è detto unobservable in $[0,T]$ $T>0$  se è undistiquishable da $\underline 0$ in $[0,T]$ ovvero: $$x_1\mathop{\simeq}\limits_{[0,T]}\underline 0$$
Quindi $x_0$ non è osservabile in $[0,T]$ :
$$
\begin{align}
&\iff w_Tx_0=w_T\underline 0=\underline 0 y_{[0,T]} \\
&\iff x_0\in\ker w_T
\end{align}
$$
Se chiamiamo $X_{[0,T]}^{no}$ il set di stati che non sono osservabili in $[0,T]$  allora $X_{[0,T]}^{no}\equiv \ker w_T$  il quale implica che  $X_{[0,T]}^{no}$  è un sottospazio vettoriale di $X=\mathbb R^n$ 

Introduciamo $X$ e $Y|_{[0,T]}$  lo stesso inner product che abbiamo proposto per il secondo esempio (mentre introducevamo l' [[R6 Inner product and ortogonality and adjoint#Definition Adjoint|adjoint]])
$$
<x_1,x_2>_X\triangleq x_1^Tx_2\qquad \qquad <y_1(\cdot),y_2(\cdot)>_{Y|[0,T]}\triangleq\int^T_0y_1(t)^Ty_2(t)\ dt 
$$
L'adjoint di $w_T$, chiamata $w_T^*$  soddisfa:
$$\begin{align}
<w_T(x),y(\cdot)>_Y\equiv <x,w_T^*(y(\cdot))>_X
\end{align}$$
Deve essere vero $\forall x\in X$ e $y(\cdot)\in Y|_{[0,T]}$ 
Per trovare $w^*_T$  dobbiamo imporre che:
- $\displaystyle<w_T(x),y(\cdot)>_Y=\int^T_0[H_e^{Ft}x]^T y(t)\ dt=x^T{\color {orange}\left[\int^T_0 e^{Ft}H^Ty(t)\ dt\right]}$ 
- $<x,w_T^*(y(\cdot))>_X=x^T{\color{orange}[w_T^*y(\cdot)]}$
Di conseguenza
- $\left[\int^T_0 e^{Ft}H^Ty(t)\ dt\right] =[w_T^*y(\cdot)]$ 

$$
\begin{align}
 w_T:Y|_{[0,T]}&\to X=\mathbb R^n\\
y(t)\quad \forall t\in [0,T] &\to\int_0^T e^{Ft}H^Ty(t)\ dt
\end{align}
$$
Sappiamo che $\ker w_T=\ker [w_T^* w_T]$ 

$$
\begin{aligned}
 w_T&:X \xrightarrow[w_T ]{\hspace{1cm} }Y|_{[0,t]}\xrightarrow[w_T]{\hspace{1.8cm} } X\\
    &: x \xmapsto[]{\hspace{1cm}}
\begin{array}{c}
y(t)=He^{Ft}\\t\in[0,T]
\end{array}
    \xmapsto[]{\hspace{1cm}}
    \huge\underbrace{\left[\int_0^Te^{F^Tt}H^THe^{Ft}dt\right]}_
    {\substack{\triangleq \mathcal V_t\in \mathbb R^{n\times n}\\\text{Observability gramiant in $[0,T]$}}}x
\end{aligned}
$$
#ST-L27-1
### Proposition
 Per ogni $t>0$  $X_{[0,1]}^{no}=\ker w_T\equiv \ker \mathcal O$ 
 dove $\mathcal O=\small \begin{bmatrix} H \\ HF \\ \vdots\\ HF^k\end{bmatrix}$ è l'observability matrix
#### Proof
$$
\begin{align}
x\in\ker w_T&\iff He^{Ft}x=0&\forall t\in[0,T]\\
&\iff H\sum_{i=0}^{+\infty}F^i\frac{t^i}{i!}x&\forall t\in[0,T]\\
&\iff \sum_{i=0}^{+\infty} (HF^ix)\frac{t^i}{i!}&\forall t\in[0,T]\\
&\mathop{\iff}\limits_{\begin{aligned}
\text{Principle of} \\
\text{identity of}\\
\text{power series}
\end{aligned}}
HF^ix=0&\forall i=0,1,\dots &\mathop{\iff}\limits_{\text{Hemilton}}HF^ix=0\\
&&&\iff\begin{bmatrix} H \\ HF \\ \vdots\\ HF^{n-1}\end{bmatrix}x=0\\
&&&\iff x\in \ker \mathcal O
\end{align}
$$
####
Diciamo che un CT ssm ed equivalentemente un paio $(F,H)$ è  osservabile se è osservabile nell'intervallo di tempo $[0,T]\quad T>0$ che significa che $X_{[0,T]}^{no}=\set\underline 0$ 
$$
(F,H) \text{ observable}\iff \ker \mathcal O =\set\underline 0 \iff rank\ \mathcal O=n
$$
#### First Observability Criterion 
$$(F,H) \text{ observable}\iff rank\ \mathcal O=n$$
## Observation Problems CT
Assumiamo di sapere la descrizione del sistema, ovvero la tripla $(F,G,H)$  e gli input $u(t)$ e gli output $y(t)$ $t\in [0,T]$  quello che si vuole fare è identificare, se possibile $x(0)$ 
Possiamo determinare la forced output evolution $y_f(t)$ e di conseguenza anche quella libera $y_l(t)$.
Il problema è identificare $x_0$ s.t.  $y_l(\cdot)\equiv w_Tx_0$           $(1)$ 
Risolvere $(1)$ è equivalente a risolvere:
$$w^*_Ty_l(\cdot)=w_T^*w_T\ x(0)=\mathcal V_T x(0)\qquad \qquad (2)$$
### Case 1 $rank\ \mathcal V_T=n$ 
$\iff \mathcal O=n\iff (F,H)$ è observable
$\to x(0)=\mathcal V^{-1}_T[w_T^*y_l(\cdot)\equiv x_0$ 
### Case 2 $rank\ \mathcal V_T<n$ 
$\iff \mathcal O<n\iff (F,H)$ non è observable
In questo caso $(2)$ ha un infinito numero di soluzioni. 
Se $\hat x_0$ è una soluzione particolare di $(2)$  allora il set di tutte le possibili soluzioni sarà:
$\set{\hat x_0+v,\quad v\in \ker \mathcal V_T=X^{no}=\ker \mathcal O} =\hat x_0+\ker\mathcal O$ 
chiaramente $x_0\in\hat x_0+\ker \mathcal O$ 

## Reconstruction Problem for CT ssm
Dato un CT ssm $\Sigma=(F,G,H)$ ed un paio di input output:
- $u(t)\quad t\in [0,T]$
- $y(t)\quad t\in [0,T]$ 
vogliamo determinare $x(T)$ 
$X^{no}_{[0,T]}\equiv \ker \mathcal O$  dall' analisi precedente possiamo dire che:

### Case 1 $rank\ \mathcal O=n$ 
I dati permettono di identificare in modo univoco  $x(0)=x_0\to x_T$ 
### Case 2  $rank\ \mathcal O<n$ 
I dato permettono di dedurre l'equivalence class di $x_0$ ovvero:
$x_0+\ker \mathcal O 0 \set{x_0+v\quad v\in \ker \mathcal O}$ 
**Q:** In questa situazione posso ancora sperare di indentificare in modo univoco  $x(T)$?
Questo sarebbe il caso se e solo se:
$$
\begin {align}
x(T&=\cancel{e^{FT}x_0}+\cancel{\mathcal R_tu(\cdot)}\equiv e^{FT}(\cancel {x_0}+v)+\cancel{\mathcal R_Tu(\cdot)})\quad& \forall v\in \ker \mathcal O\\
&\iff e^{FT}v=0\qquad&\forall v\in \ker \mathcal O\\
&\iff v\in \ker \mathcal O
\end{align}
$$
per l'ulòtimo $\iff$ possiamo dire che $e^{FT}$ è non singular per qualsiasi $T$

$\Rightarrow$ Non c'è modo di determinare in modo univoco  $x(T)$ nel caso $2$ 

# For CT system
$$
\begin{array}{c}
\text{reconstruction problem}\\
\text{in $[0,T]$ is solvable}
\end{array}
\iff
\begin{array}{c}
\text{observation problem}\\
\text{in $[0,T]$ is solvable}
\end{array}
\iff
(F,H) \text{ is solvable}
$$
