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
Ricordando [[R6 Inner product and ortogonality and adjoint#Definition Adjoint#Proprietà|adjoint trasformation]] e il fatto che  stiamo lavorando con finite dimensional vector spaces:
$$
\begin{align}
Im \mathcal R_k=Im(\mathcal R_k\mathcal R_k^T)
\end{align}
$$
