#ST-L11
![[Linear discrete time s.s.m.#State equation]]

### Problem 
Dato un tempo $k\in\mathbb Z+\quad k>0$ e due stati $x_0,x_f\in X$
Determinare se possibile la sequenza di input  $u(0)\dots u(k-1)\in U$  
che guida lo state da $x(0)=x_0$ a $x(k)=x_f$ 
$$
\large
x(0)=x_0\xrightarrow[u(0),u(1),\dots,u(k-1)]{} x(k)=x_f
$$
dato
$$
\begin{align}
x(k)&=x_l(k)+x_f(k)\\&=F^kx(0)+\mathcal R_k\begin{bmatrix}
u(k-1) \\
\vdots \\
u(0) \\
\end{bmatrix}\\
&=F^kx_0+\mathcal R_k\begin{bmatrix}
u(k-1) \\
\vdots \\
u(0) \\
\end{bmatrix}\\
{\color {lightgreen} \iff} &x_f-F^kx_0=\mathcal R_k\begin{bmatrix}
u(k-1) \\
\vdots \\
u(0) \\
\end{bmatrix}\\ \
\end{align}
$$
#### Solvability condition
Il problema è risolvibile $\iff \exists u(0)\dots u(k-1)\in U$ s.t.  $x_f-F^kx_0\in Im \mathcal R_k$ 
####
Se la solvability condition è rispettata allora l'equazione $\textcolor{lightgreen}{■}$  ha soluzione.
Ricordando ![[R6 Inner product and ortogonality and adjoint#Definition Adjoint#Proprietà adjoint|adjoint trasformation]] 
e il fatto che  stiamo lavorando con finite dimensional vector spaces:
$$
\begin{align}
Im \mathcal R_k=Im(\mathcal R_k\mathcal R_k^T)
\end{align}
$$
#ST-L12
	Se qualche conto non torna qualche passaggio probablilmente è colpa delle proprietà dell'adjoint
Se il problema è risolvibile allora l'equazione da risolvere sarà:
1. $x_f-F^Kx_0=\mathcal R_k\begin{bmatrix}u(k-1) \\\vdots \\u(0) \\\end{bmatrix}_{\mathcal U_k}$ 
2. $x_f-F^k x_0=\mathcal R_k\mathcal R_k^T v_k$ 

Possiamo risolvere $(2)$ e da una delle solluzioni di  $v_k$ possiamo dedurre la soluzione di $(!) nella forma $\mathcal U_k=\mathcal R^T_kv_k$  
##### Case 1:  $rank \mathcal R_k=n$
$\iff (F,G)$ è raggiungibile e $k\geq \bar k=r$ (reachability index)
Allora $\mathcal R_k\mathcal R_k^T$ ha rango $n$  che vuol dire che è non singular e quindi
$\Rightarrow v_k=[\mathcal R_k\mathcal R_k^T]^{-1}[x_f-F^kx_0]$ è l'unica soluzione di  $(2)$ 
##### Case 2:  $rank \mathcal R_k<n$
Allora $\mathcal R_k\mathcal R_k^T$ è singular e quindi esistono un infinito numero di soluzioni di $(2)$. 
Vogliamo provare che $v_k$ e $\bar v_k$ sono due soluzioni distinte di $(2)$ e comunque portano alla stessa soluzione di $(1)$ che vuol dire che : $\mathcal R^T_kv_k=\mathcal R^T_k\bar v_k$  

Se $v_k$ e $\bar v_k$ sono soluzioni di $(2)$ 
$\Rightarrow$ $\mathcal R_k\mathcal R_k^T v_k=x_f-F^kx_0=\mathcal R_k\mathcal R_k^T\bar v_k$ 
$\Rightarrow$$\mathcal R_k\mathcal R_k^T[v_k-\bar v_k]=0$
$\Rightarrow$$v_k=\bar v_k+a_k$ con $a_k\in \ker[\mathcal R_k\mathcal R_k^T]=\ker\mathcal R_k^T$ [[R6 Inner product and ortogonality and adjoint#Definition Adjoint#Proprietà adjoint|adjoint P2]]  
Quindi
$\Rightarrow$$\mathcal R_k^Tv_k=\mathcal R_k^T[\bar v_k+a_k]=\mathcal R_k^T\bar v_k+\cancel{\color{orange}\mathcal R_k^T a_k}$  $\textcolor{orange}{■}$ perchè $a_k$ fa parte del kernel

Quindi indipendentemente se siamo in $(1)$ o $(2)$ la soluzione ottenuta determinando prima una soluzione $v_k$ di $(2)$ e poi metterla in $\mathcal U_k=\mathcal R_k^Tv_k$ è sempre unica e la chiamiamo $\mathcal U^*_k$ 

#### Perchè $\mathcal U_k^*$ è speciale?
Sia $\mathcal U_k^*=\mathcal R^T_kv_k$ e sia $\mathcal U_k$ una qualunqiue altra soluzione di $(1)$ Questo vuol dire che:
$\mathcal R_k\mathcal U_k=F^kx_0=\mathcal R_k\mathcal U_k^*$
$\Rightarrow \mathcal R_k[\mathcal U_k-\mathcal U_k^*]=0$
$\Rightarrow \mathcal U_k=\mathcal U_k^*+\mathcal V_k$ con: [[R6 Inner product and ortogonality and adjoint#Definition Adjoint#Proprietà adjoint|adjoint P1]]  
- $\mathcal V_k\in \ker \mathcal R_k$
- $\mathcal U_k^*\in Im \mathcal R_k$ 
Quindi
$||\mathcal U_k||^2=||\mathcal U_k^*+\mathcal V_k||^2=||\mathcal U_k^*||^2+||\mathcal V_k||^2\Rightarrow ||\mathcal U_k||^2\geq ||\mathcal U_k^*||^2\Rightarrow$ 
$$
||\mathcal U_k||\geq||\mathcal U_k^*||
$$
(In questo modo stiamo scegliendo la soluzione ottima relativamente al consumo minimo)

## Exercise 1
 Consideriamo DT s.s.m.
 $$
 \begin{align}
 x(t+1)=Fx(t)+gu(t)=
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
3 & 0 & 0 \\
\end{bmatrix}
x(t)+
\begin{bmatrix}
0\\ 0\\ 1 \\
\end{bmatrix}
u(t)
\end{align}
$$
Vogliamo guidare lo stato del sistema da $x_0=\begin{bmatrix}1\\ 0\\ 0 \\\end{bmatrix}$ con $t=0$ a $x_f=\begin{bmatrix}1\\ 1\\ 0 \\\end{bmatrix}$ con $t=4$
Se così trovare la minimum norm solution


Problem is solvable$\iff x_f-F^4x_0\in Im\mathcal R_4$
$$\mathcal R_4=[g|Fg|F^2g|F^3g]=
\begin{bmatrix}
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 3 \\
\end{bmatrix}
$$
$$
\begin{align}
&x_0=\begin{bmatrix}1 \\ 0 \\ 0 \\\end{bmatrix}\rightarrow Fx_0=\begin{bmatrix}0 \\ 0 \\ 3 \\\end{bmatrix}\rightarrow F^2x_0=\begin{bmatrix}0 \\ 3 \\ 0 \\\end{bmatrix}\rightarrow F^3x_0=\begin{bmatrix}3 \\ 0 \\ 0 \\\end{bmatrix}\rightarrow F^4x_0=\begin{bmatrix}0 \\ 0 \\ 9 \\\end{bmatrix}\\\\
&x_f-F^4x_0=\begin{bmatrix}1 \\ 1 \\ 0 \\\end{bmatrix}-\begin{bmatrix}0 \\ 0 \\ 9 \\\end{bmatrix}=\begin{bmatrix}1 \\ 1 \\ -9 \\\end{bmatrix}
\end{align}
$$
$$
\begin {align}
&\mathcal R_4\mathcal R_4^T=
\begin{bmatrix}
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 3 \\
\end{bmatrix}
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 3 \\
\end{bmatrix}=
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 10 \\
\end{bmatrix}\\
&v_4=[\mathcal R_4\mathcal R_4^T]^{-1}[x_f-F^4x_0]=
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0.1 \\
\end{bmatrix}
\begin{bmatrix}1 \\ 1 \\ -9 \\\end{bmatrix}=
\begin{bmatrix}1 \\ 1 \\ -0.9 \\\end{bmatrix}
\end{align}
$$
Minimum norm solution:
$$
\mathcal U_4^*=\mathcal R_4^Tv_4=
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 3 \\
\end{bmatrix}
\begin{bmatrix}1 \\ 1 \\ -0.9 \\\end{bmatrix}
\begin{bmatrix}-0.9 \\ 1 \\ 1 \\-2.7\end{bmatrix}
$$
L'ultimo vettore corrisponde agli input $\begin{bmatrix}u(3)&u(2)&u(1)&u(0)\end{bmatrix}^T$ 

Se vogliamo trovare solo una soluzione $\mathcal U_4$ (non necessariamente di norma minima) risolviamo direttamente $(1)$:
$$
\mathcal U^*_4=
\begin{bmatrix}1 \\ 1 \\ -0.9 \\\end{bmatrix}=
\begin{bmatrix}
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 3 \\
\end{bmatrix}
\begin{bmatrix}u(3) \\ u(2) \\ u(1) \\u(0)\end{bmatrix}
$$
$u(1)=1\quad u(2)=1\quad u(3)+3u(0)=-9$ 

## Exercise 2
Consideriamo DT s.s.m.
 $$
 \begin{align}
 x(t+1)=Fx(t)+gu(t)=
\begin{bmatrix}
0 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1 \\
\end{bmatrix}
x(t)+
\begin{bmatrix}
0\\ 0\\ 1 \\
\end{bmatrix}
u(t)
\end{align}
$$
Determinare se possibile:
$k\in \mathbb Z\quad k\geq 1$ e $u(0)\dots u(k-1)\in U=\mathbb R$ 
che guida da $x(0)=x_0=\begin{bmatrix}1 \\ 1 \\ 1 \\\end{bmatrix}$ a $x(k)=x_f=\begin{bmatrix}0 \\ 16 \\ 0 \\\end{bmatrix}$


Problem is solvable$\iff x_f-F^kx_0\in Im\mathcal R_k$ 
$$
F^k=
\begin{bmatrix}
0 & 0 & 0 \\
0 & 2^k & 0 \\
0 & 0 & 1 \\
\end{bmatrix}
\qquad 
F^kx_0=
\begin{bmatrix}
 0 \\
 2^k \\
1 \\
\end{bmatrix}
\qquad x_f-F^kx_0=\begin{bmatrix}0 \\ 16 \\ 0 \\\end{bmatrix}\begin{bmatrix}0 \\ 2^k \\1 \\\end{bmatrix}=
\begin{bmatrix}0 \\ 16-2^k \\ -1 \\\end{bmatrix}
$$
$$
\mathcal R_k=[g|Fg|\dots|F^{k-1}g]=\begin{bmatrix}
0 & 0 &\dots& 0 \\
0 & 0 && 0 \\
1 & 1 &\dots& 1 \\
\end{bmatrix}\text{il sistema non è raggiungibile}
$$
solo per $k=4$ abbiamo $x_f-F^4x_0=\begin{bmatrix}0 \\ 0 \\ -1 \\\end{bmatrix}\in Im\mathcal R = <\begin{bmatrix}0 \\ 0 \\ 1 \\\end{bmatrix}>$ 
$$
\mathcal U^*_4=\begin{bmatrix}0 \\ 0 \\ -1 \\\end{bmatrix}\begin{bmatrix}
0 & 0 &0& 0 \\
0 & 0 &0& 0 \\
1 & 1 &0& 1 \\
\end{bmatrix}
\begin{bmatrix}u(3) \\ u(2) \\ u(1) \\u(0)\end{bmatrix}
$$
$u(0)=-1\quad u(1)=u(2)=u(3)=0$ 