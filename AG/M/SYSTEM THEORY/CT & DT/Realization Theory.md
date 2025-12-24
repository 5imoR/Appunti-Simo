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

### ![[Characterization of minimal realizations#Theorem [Characterization ofg minimal realizations]]
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
