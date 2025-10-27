#ST-L12 
![[Linear contiunuous time s.s.m.#State equation]]
### Problem
Dato un tempo $t>0$ e due stati $x_0,x_f\in X=\mathbb R^n$ 
Determinare se possibile la sequenza di input $u(\cdot)\in\mathcal U|_{[0,t]}$ 
che guida lo state da $x(0)=x_0$ a $x(t)=x_f$ 
$$
\large
x(0)=x_0\xrightarrow[u(\cdot)]{} x(0)=x_f
$$
dato
$$
\begin{align}
x(t)&=x_l(t)+x_f(t)\\
&=e^{Ft}x(0)+R_tu(\cdot)\\
&=e^{Ft}x(0)+\int_0^te^{F(t-\tau)}Gu(\tau)d\tau
\end{align}
$$
#### Solvability condition
$$
\begin{align}
\text{il problema è risolvibile}
&\iff \exists u(\cdot)\in \mathcal U|_{[0,t]}\ s.t.\quad x_f=e^{Ft}x_0+R_tu(\cdot)\\
&\iff \exists u(\cdot)\in \mathcal U|_{[0,t]}\ s.t.\quad x_f-e^{Ft}x_0=-R_tu(\cdot)\quad(1)\\
&\iff x_f-e^{Ft}x_0\in Im\ R_t\equiv Im\mathcal R
\end{align}
$$
####

Se la solvability condition è corretta dobbiamo risolvere $(1)$ 
Ricordando![[R6 Inner product and ortogonality and adjoint#Definition Adjoint#Proprietà adjoint|adjoint trasformation]]
e il fatto che  stiamo lavorando con $Im R_t$ finite dimensional:
$$Im\ R_t= Im(R_tR_t^*)=Im\ W_t$$ 
- $W_t$ è il [[Reachability CT#Gramiant|Gramiant]] 
Di conseguenza $(1)$ è risolvibile se $(2)$ è risolvibile:
$$
x_f-e^{Ft}x_0=R_tR_t^*v_t=W_tv_t\quad (2)
$$
se $v_t$ risolve $(2)$ allora $R_tv_t=u(\cdot)$ risolve $(1)$
##### Case 1: $Im\ R_t=Im\ W_t=Im \mathcal R=\mathbb R^n$ 
Allora $W_t\in \mathbb R^{n\times n}$ è non singular e di conseguenza possiamo ottenere la soluzione di $(2)$ unicamente determinata come $v_t=W_t^{-1}[x_f-e^{Ft}x_0]$ 
$\Rightarrow u^*(\cdot) =R_t^*v_t$ è uniquely determined
##### Case 2: $Im\ R_t=Im\ (R_tR_t^*)=Im\ W_t=Im \mathcal R \subsetneq \mathbb R^n$
Allora  $W_t$ è singular 
$\Rightarrow$ se $v_t$ e $\bar v_t$ sono due soluzioni di $(2)$ 
$\Rightarrow$ $W_tv_t=R_tR_t^*v_t\equiv W_t\bar v_t=R_tR_t^*\bar v_t$
$\Rightarrow$ $v_t=\bar v_t+a_t$ con $a_t \in \ker W_t=\ker (R_tR_t^*)=\ker R_t^*$ [[R6 Inner product and ortogonality and adjoint#Definition Adjoint#Proprietà adjoint|adjoint P2]]  
Quindi
$\Rightarrow$$R_t^*v_t=R_t^*[\bar v_t+a_t]=R_t\bar v_t+\cancel{\color{orange}R_t^*a_t}$  $\textcolor{orange}{■}$ perchè $a_k$ fa parte del kernel

Quindi indipendentemente se siamo in $(1)$ o $(2)$ la soluzione ottenuta determinando prima una soluzione $v_t$ di $(2)$ 

Questo non l'ha detto ma c'era nella versione DT
	e poi metterla in $\mathcal U_t=\mathcal R_t^Tv_t$ è sempre unica e la chiamiamo $\mathcal U^*_t$ 

#####

Vogliamo provare che  $u(\cdot)^*=R_t^*v_t$ è minimal norm solution di $(1)$ 

Sia $u(\cdot)$ una qualunque soluzione dell'equazione(1) allora  $R_tu(\cdot)=x_f-e^{Ft}x_0=R_tu^*(\cdot)$
$\Rightarrow$ $u(\cdot)=u^*(\cdot)+\bar u(\cdot)$ 
Quindi
$||u(\cdot)||^2=|| \underbrace{u^*(\cdot)}_{\substack{\in Im\ R_t^*\\=(\ker R_t)^\perp}}+\underbrace{\bar u(\cdot)}_{\in\ker Rt}||^2=||u^*(\cdot)||^2+||\bar u(\cdot)||^2\Rightarrow ||u(\cdot)||^2\geq ||u^*(\cdot)||^2$ 


