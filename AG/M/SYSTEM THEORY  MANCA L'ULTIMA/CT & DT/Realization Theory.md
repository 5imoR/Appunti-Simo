#ST-L31-1
$$
\left.
\begin{array}{c}
\Sigma=(F,G,H,D)\\
\dim \Sigma=n\\
m \text { input}\\
p \text{ output}
\end{array}
\ \ \right]\to
\begin{array}{c}
\text{Transfer matrix}\\
W_\Sigma(s)=H(sI_n-F)^{-1}G+D\in\mathbb R^{p\times n}(s)\\
\text{proper rational}
\end{array}
$$
#### Problem schema
$$
\text{Given } 
\begin{array}{c}
W(s)\in\mathbb R^{p\times n}(s)\\
\text{proper}
\end{array}
\xrightarrow[\phantom{sssssss}]{\large ?}
\begin{array}{c}
n\in\mathbb Z+\\
\Sigma=(F,G,H,D)\\
\dim \Sigma=n\\
m=input\\
p=output
\end{array}
s.t.\ W_\Sigma(s)=H(sI_n-F)^{-1}G+D\equiv W(s)
$$
## Problem
Data una proper rational matrix $W(s)\in\mathbb R^{p\times n}(s)$  esiste $n\in \mathbb Z+$ e in un $n$-dimensional ssm $\Sigma(F,G,H,D)$ con $m$ input e $p$ output s.t.$W_\Sigma(s)\triangleq H(sI_n-F)^{-1}G+D\equiv W(s)$?
#### Remark
Se il problema è risolvibile ovvero che $H(sI_n-F)^{-1}G+D\equiv W(s)$ regge il limite:
$$
\lim_{s\to+\infty}W(s)\equiv \lim_{s\to+\infty}H(sI_n-F)^{-1}G+D=D\Rightarrow D\equiv W(+\infty)
$$
Quindi possiamo sempre ricondurci al problema di trovare uno strictly proper ssm $\Sigma=(F,G,H)$ s.t.
$$
H(sI_n-F)^{-1}G\equiv W(s)-D\triangleq W_{sp}(s)\text{ strictly proper rational matrix}
$$

**PER SEMPLICITA' DA QUI IN POI SI TRATTANO SOLO STRICTLY PROPER E SI OMETTE sp**
## Solution
### Case 1) $p=m=1$ 
$p=m=1\to W(s)=\frac{n(s)}{d(s)}$ 

con:
- $n(s),d(s)\in \mathbb R[s]$
- $\deg d(s)>\deg n(s)$ 
- W.L.O.G. $d(s)$ è [[Monic polynomial|monic]] 
allora:
- $d(s)=s^n+a_{n-1}s^{n-1}+\dots+a_1s+a_0$
- $n(s)=\phantom{s^n+\ } b_{n-1}s^{n-1}+\dots +b_1s+b_0$ 
#### Reachable Realization \[in CCF]
[[CCF Controlled Canonical Form]]
$$
F_c=\begin{bmatrix}
0 & 1 &  &  \\
 &  & \ddots &  \\
 &  &  & 1 \\
-a_0 & -a_1 & \dots & -a_{n-1} \\
\end{bmatrix}
g_c=\begin{bmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}
H_c=\begin{bmatrix} b_0 & b_1 & \dots & b_{n-1} \end{bmatrix}
$$
$$\begin{align}
W(s)&=H_c(sIn-F_c)^{-1}g_c\\
&=W(s)=g_c^T(sIn-F_c)^{-1}H^T\\
&=W(s)^T
\end{align}$$
#### Observable realization \[in OCF]
$$
\begin{array}{c}
F_o&=\\F_c^T&=
\end{array}\begin{bmatrix}
0 &  &  & -a_0 \\       
1 &  &  & -a_1 \\       
 & \ddots &  & \vdots \\
 &  & 1 & -a_{n-1} \\ 
\end{bmatrix}
\begin{array}{c}
g_o&=\\H_c^T&=
\end{array}
\begin{bmatrix} b_0 \\ b_1 \\ \vdots\\ b_{n-1} \end{bmatrix}
\begin{array}{c}
H_o\\g_c^T
\end{array}=
\begin{bmatrix} 0 & \dots & 0 & 1 \end{bmatrix}
$$
#### Remark
$\dim \Sigma_c=\dim \Sigma_o=\deg d(s)=n$ 
### Case 2) $p\ge 1\ \ m\ge 1$ 
$$W(s)=\left[w_{ij}(s)\right]_{\substack{i=1\dots p\\ j=1\dots m}}=\left[\frac{\tilde n_{ij}(s)}{\tilde d_{ij}(s)}\right]_{\substack{i=1\dots p\\ j=1\dots m}}
$$
$$
{\tilde n_{ij}(s)},{\tilde d_{ij}(s)}\in\mathbb R[s]
\qquad
\deg d_{ij}(s)>\deg n_{ij}(s)
$$
Definiamo $d(s)\triangleq$ monic least common multiple di tutti i polinomi $d_{ij}(s)$
$$
\Rightarrow W(s)=\left[\frac{\tilde n_{ij}(s)}{\tilde d(s)}\right]_{\substack{i=1\dots p\\ j=1\dots m}}
$$
$$
{\tilde n_{ij}(s)},{\tilde d(s)}\in\mathbb R[s]
\qquad
\deg d(s)>\deg n_{ij}(s)
$$

Assumiamo $d(s)=s^n+s^{n-1}a_{n-1}+\dots +a_1s+a_0$ 
$N(s)\triangleq [n_{ij}(s)]_{\substack{i=1\dots p\\ j=1\dots m}}=B_0+B_1+\dots+B_{n-1}s^{n-1}\qquad B_i\in \mathbb R^{p\times m}$
$$
\begin{align}
\Rightarrow W(s)&=\frac 1{d(s)}N(s)\\
&=\frac {B_0+B_1+\dots+B_{n-1}s^{n-1}}{s^n+s^{n-1}a_{n-1}+\dots +a_1s+a_0}
\end{align}
$$

#### Reachable Realization \[of dimension $n\cdot m$]
$$
F_c\begin{bmatrix}
0 & I_m \\
 &  & \ddots \\
 &  &  & I_m \\
-a0I_m & -a_1I_m & \dots & -a_{n-1}I_m \\
\end{bmatrix}
G_c=\begin{bmatrix} 0 \\ \vdots \\ 0 \\ I_m \end{bmatrix}
H_c=\begin{bmatrix} B_0 & B_1 & \dots & B_{n-1} \end{bmatrix}
$$
#### Observable realization \[of dimension $n\cdot p$]
$$
\begin{array}{c}
F_o=
\end{array}\begin{bmatrix}
0 &  &  & -a_0I_p \\       
I_p &  &  & -a_1I_p \\       
 & \ddots &  & \vdots \\
 &  & I_p & -a_{n-1}I_p \\ 
\end{bmatrix}
\begin{array}{c}
G_o=
\end{array}
\begin{bmatrix} B_0 \\ B_1 \\ \vdots\\ B_{n-1} \end{bmatrix}
\begin{array}{c}
H_o\\
\end{array}=
\begin{bmatrix} 0 & \dots & 0 & I_p \end{bmatrix}
$$
### Conclusione
Si il problema è sempre risolvibile

### Definition \[minimal realization] 
Data una strictly proper rational matrix $W(s)\in\mathbb R^{p\times m}$ uno strictly proper ssm di dimensione $\bar n$, $\bar \Sigma=(\bar F,\bar G,\bar H)$ è una minimal realization di $W(s)$ se:
- è una realization di $W(s)$
- per qualunque altra realization $\Sigma$ di $W(s)$ $\dim \Sigma\ge \dim\bar\Sigma=\bar n$ 

### ![[Characterization of minimal realizations#Theorem [Characterization of minimal realizations]]
![[Alg. to find a minimal realization of a proper rational matrix#Alg]]

## Ex
Determine a minimal realization of the proper rational matrix
$$
W(s)
\begin{bmatrix}
\displaystyle\frac{s+1}s & \displaystyle\frac{s+2}{s+1} \\
\displaystyle\frac{1-s}{s+1} & \displaystyle-\frac1s \\
\end{bmatrix}=\begin{bmatrix} F & G \\ H & D \end{bmatrix}\text{presumo}
$$
Non è strictly proper
- Step 1:
$D=\lim_{s\to\infty}W(s)=\begin{bmatrix} 1 & 1 \\ -1 & 0 \end{bmatrix}$ 
$W_{sp}(s)=W(s)-\begin{bmatrix} 1 & 1 \\ -1 & 0 \end{bmatrix}=\begin{bmatrix}\displaystyle\frac{1}s & \displaystyle\frac{1}{s+1} \\\displaystyle\frac{2}{s+1} & \displaystyle\frac1s \\\end{bmatrix}$

- Step 2:
Settiamo $d(s)\triangleq s(s+1)=s^2+1s+0\equiv s^2+a_1s+a_0$  
$$W(s)=\frac 1{s(s+1)}\begin{bmatrix}
{\color{lightgreen}s}+\color{orange}1 & {\color{lightgreen}s}+\color{orange}0 \\
{\color{lightgreen}2s}+\color{orange} 0 & {\color{lightgreen}s}+\color{orange}1 \\
\end{bmatrix}
\qquad N(s)=
\underbrace{\begin{bmatrix} \color{orange}1 & \color{orange}0 \\ \color{orange}0 & \color{orange}1 \end{bmatrix}}_{B_0}
\underbrace{\begin{bmatrix} \color{lightgreen}1 & \color{lightgreen}1 \\ \color{lightgreen}2 & \color{lightgreen}1 \end{bmatrix}}_{B_1}
$$

$m=p=2$ scegliamo un observable relation di dimensione $n\cdot p=4$
$$
\begin{align}
&F_o=\begin{bmatrix}
0 &  &  & -a_0I_p \\       
I_p &  &  & -a_1I_p \\       
 & \ddots &  & \vdots \\
 &  & I_p & -a_{n-1}I_p \\ 
\end{bmatrix}
&G_o=
\begin{bmatrix} B_0 \\ B_1 \\ \vdots\\ B_{n-1} \end{bmatrix}
&H_o=
\begin{bmatrix} 0 & \dots & 0 & I_p \end{bmatrix}\\\\
&F_o=
\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
1 & 0 & -1 & 0 \\
0 & 1 & 0 & -1 \\
\end{bmatrix}
&G_o=
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
1 & 1 \\
2 & 1 \\
\end{bmatrix}
&H_o=
\begin{bmatrix}
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\end{align}
$$

- Step 3:
Controlliamo la reachability di $\Sigma=(F_o,G_o,H_o)$
$$
\begin{align}
\mathcal R_o &= [G_o |F_oG_o|F_o^2G_o|F_o^3G_o]\\
&=
\begin{bmatrix}
1 & 0 & | & 0 & 0 & |s\dots \\
0 & 1 & | & 0 & 0 & |\dots \\
1 & 1 & | & 0 & -1 &| \dots \\
2 & 1 & | & -2 & 0 &| \dots \\
\end{bmatrix}\\
\end{align}
$$
Ha rango $4\Rightarrow (F_o,G_o,H_o)$ è anche reachable di conseguenza minima
##
### Proposition \[Minimality in the case m=p=1] 
	 \[Characterization of minimality for realizations of scalar functions]
Sia $W(s)\in\mathbb R(s)$ una strictly proper rational function e sia $\Sigma=(F,g,H)$ una n-dimensional realization di $W(s)$
$$
\Sigma \text{ è una minimal realization}\iff \text{I polinomi $H$ adj $(sI_n-F)g$ e $\Delta_F(s)$ sono coprimi}
$$

#### Proof
#ST-L32-1
##### $\Rightarrow$ by counterpositive
Assumiamo che esista un minic polinomial $\delta(S)\in\mathbb R(s), \deg \delta(s)\ge 1$ s.t.
$$
\begin{align}
H \text{adj } (sIn-F)g&=\delta(s)\bar n(s)&\exists \bar n(s),\bar d(s)\in\mathbb R[s]\\
\Delta_F(s)&=\delta(s)\bar d(s)
\end{align}
$$
Nota che:
- $\bar d(s)$ è monico
- $\deg \bar d(s)<\deg\Delta_F(s)=n$ 
Allora
$$
W(s)=\frac{\cancel{\delta(s)}\bar n(s)}{\cancel{\delta(s)}\bar d(s)}=\frac{\bar n(s)}{\bar d(s)}
$$
Questo implica il Remark alla fine della soluzione del [[Realization Theory#Case 1) $p=m=1$#Remark|problema della realizazione nel primo caso]] ovvero che esiste una realization:
$$\bar\Sigma\text{ di $W(s)$ con } \dim \bar \Sigma=\deg\bar d(s)<n=\dim \Sigma$$
Di conseguenza $\Sigma$ non è minima
	Questa proposition diceva che era una minimal realization, fine prova

##### $\Leftarrow$ by counterpositive
Assumiamo che  $\Sigma$ non sia minimo. Allora $\exists \bar \Sigma=(\bar F,\bar g,\bar H)$ realizzazione di $W(s)$ con $\dim \bar \Sigma\triangleq \bar n<n=\dim\Sigma$. Possiamo anche calcolare 
$$
W(s)=\frac{H \text{adj } (sI_n-F)g}{\Delta_F(s)}
    =\frac{\bar H \text{adj } (sI_n-\bar F)\bar g}{\Delta_\bar F(s)}
$$
Dato che $\deg \Delta_\bar F(s)=\bar n <n=\deg \Delta_F(s)$
Le due rappresentazioni sono compatibili solo se $H \text{adj } (sI_n-F)g$  e $\Delta_F(s)$ hanno un fattore in comune
	Questo contraddice la coprimality
#### Remark 1
Una conseguenza immediata di questa [[Realization Theory#Proposition [Minimality in the case m=p=1]|proposition]] è che dato uno strictly proper $W(s)\in\mathbb R(s)$ la dimensione di una minimal realization di $W(s)$ coincide con $\deg d(s)$ in qualunque coprime rappresentation $\displaystyle\frac {n(s)}{d(s)}$ di $W(s)$.
#### Remark 2
Assumiamo che $W(s)\in\mathbb R(s)$ è strictly proper e $\Sigma(F,g,H)$ è una n-dimensional realization di $W(s)$
$$
\begin{align}
\begin{array}{c}
\Sigma\text{ is a minimal}\\
\text{realization}
\end{array}
&\iff
\begin{array}{c}
\Sigma \text{ is reachable}\\
\text{ and observable}
\end{array}\\
\Updownarrow \qquad\qquad&\\
\begin{array}{c}
\text{$H$ adj $(sI_n-F)g$}\\\text{ and $\Delta_F(s)$}\\
\text{are coprime}
\end{array}
\end{align}

$$

##### Conseguenze
Se  $H \text{adj } (sI_n-F)g$ e $\Delta_F(s)$ hanno un fattore in comune $(s-\lambda)$, $\exists \lambda \in\mathbb C$ allora:
- $(F,g,H)$ è non reachable o non observable o nessuno dei due
- $\lambda$ è un autovalore della non-reachable part o del non-observable subsystem o entrambi

Se sappiamo che $\Sigma=(F,g,H)$ è (per esempio) reachable allora automaticamente $\lambda$ sarà un autovalore del non-observable subsystem.
###### Recall
$$
\begin{align}
\begin{array}{c}
\text{SISO REACHABLE SYSTEM}\\
\Sigma=(F,g,H)\\
\text{with transfer function}\\
W(s)=\frac{n(s)}{d(s)}\\
\text{where}\\
n(s)=\text{$H$ adj $(sI_n-F)g$}\\
d(s)=\Delta_F(s)
\end{array}
\xrightarrow[]{\displaystyle K\in\mathbb R^{1\times m}}
\begin{array}{c}
\text{SISO REACHABLE SYSTEM}\\
\Sigma_K=(F+gK,g,H)\\
\text{with transfer function}\\
W_K(s)=\frac{n(s)}{\bar d(s)}\\
\text{where}\\
n(s)=\text{$H$ adj $(sI_n-F)g$}\\
\bar d(s)=\Delta_{F+gK}(s)
\end{array}
\end{align}
$$
Questo implica che tutte le possibili cancellazioni tra $n(s)$ e $d(s)$ o tra $n(s)$ e $\bar d(s)$ sono relative ad autovalori non-observable e il feedback mi permette di ottenere un observable system $\Sigma_K$ anche se $\Sigma$ non è observable.

## Ex
Consider the stricltly proper function
$W(s)=\frac{s+a}{s^2(s+1)}\quad a\in\mathbb R$ 
- Determine for $\forall a\in\mathbb R$ a minimal realization of $W(s)$
By remark 1 the dimension if a minimal realization coincides with the degree of the denominator in a coprime rapresentation of $W(s)$.
Clearly the given rappresentation is coprime $\forall a\ne 0, 1$
For $a=0$
$\displaystyle W(s)= \frac 1 {s+(s+1)}=\frac {\color{lightgreen}1}{s^2+{\color {cyan}1}s+\color {orange}0}\to \dim\Sigma_{MIN}=2$
$$\Sigma_{MIN}=(F_c,g_c,H_c)=\left(
\begin{bmatrix}
0 & 1\\\color {orange} 0 &\color {cyan}-1
\end{bmatrix}
\begin{bmatrix}
0\\ 1
\end{bmatrix}
\begin{bmatrix}
\color{lightgreen}1 &0
\end{bmatrix}\right)
$$
For $a=1$
$\displaystyle W(s)= \frac 1 {s^2}=\frac {\color{lightgreen}1}{s^2}\to \dim\Sigma_{MIN}=2$
$$\Sigma_{MIN}=(F_c,g_c,H_c)=\left(
\begin{bmatrix}
0 & 1\\ 0 &0
\end{bmatrix}
\begin{bmatrix}
0\\ 1
\end{bmatrix}
\begin{bmatrix}
\color{lightgreen}1 &0
\end{bmatrix}\right)
$$
For $a\ne 0,1$ 
The representation is coprime $\Rightarrow$ $\dim \Sigma_{MIN}=3$
$$
\begin{align}
s^2(s+1)=s^3+s^2+0s+0\\
\Sigma_{MIN}=\left(
\begin{bmatrix}
0 & 1 & 0\\ 0 &0 &1\\ 0 & 0 & -1
\end{bmatrix}
\begin{bmatrix}
0\\0\\ 1
\end{bmatrix}
\begin{bmatrix}
a &1 &0
\end{bmatrix}\right)
\end{align}
$$

- For $a=0$ provide a reachable realization of dimension $3$ is it observable?
For $a=0$ $\dim\Sigma_{MIN}=2$ therefore a realization of dimension $3$ cannot be minimal. So if we impose it is reachable it cannot be observable. A possible realization of dimension $3$ is
$$
\begin{align}
\Sigma=\left(
\begin{bmatrix}
0 & 1 & 0\\ 0 &0 &1\\ 0 & 0 & -1
\end{bmatrix}
\begin{bmatrix}
0\\0\\ 1
\end{bmatrix}
\begin{bmatrix}
0 &1 &0
\end{bmatrix}\right)
\end{align}
$$
$H$ is not observable since $\mathcal O$ has rank $2<3$
$$\mathcal O=\begin{bmatrix}
H_c\\ H_cF_c\\
H_cF_c^2
\end{bmatrix}=
\begin{bmatrix}
0 &1& 0\\
0 & 0 & 1\\
0 & 0 &-1\\
\end{bmatrix}
$$
- Design a state feedback s.t. $\Sigma_K=(F+gK,g,H)$ is also observable
$$
\begin{align}
\begin{array}{c}
\text{SISO REACHABLE SYSTEM}\\
\Sigma=(F,g,H)\\
\text{Reachable but not Observable}\\
\text{with transfer function}\\
W(s)=\frac{s}{s^2(s+1)}\\
\end{array}
\xrightarrow[\phantom{ssssssssssss}]{*}
\begin{array}{c}
\text{SISO REACHABLE SYSTEM}\\
\Sigma_K=(F+gK,g,H)\\
\text{Reachable and Observable}\\
\text{since n(s) and d(s) are coprime}\\
\text{with transfer function}\\
W_K(s)=\frac{s}{(s+1)^3}\\
\end{array}
\end{align}
$$
$*$We impose $\Delta_{F+gK}(s)$ arbitrary but with non zero in zero for istance $\Delta_{F+gK}(s)=(s+1)^3=s^3+3s^2+3s+1$


set $K=\begin{bmatrix} k_1 & k_2 &k_3\end{bmatrix}$

$F_c+g_cK_c=\begin{bmatrix}0 & 1 & 0\\ 0 &0 &1\\ k_0 & k_1 & k_2-1\end{bmatrix}\begin{bmatrix}0 & 1 & 0\\ 0 &0 &1\\ -1 & -3 & -3\end{bmatrix}$
$K=\begin{bmatrix} -1 & -3 &-2\end{bmatrix}$
