Assumiamo di avere  un paio $(F,G)$ reachable con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$  reachable e di conseguenza  $\forall p(s)\in \mathbb R[s]$ monic di grado $n$ $\exists K\in \mathbb R^{m\times n}$ s.t. $\Delta_{F+GK}(s)\equiv p(s)$ 
### Q1
Cosa possiamo dire della [[R3 Jordan Form]] di $F+GK$ ?
In generale non molto. Unica cosa conosciamo i blocchi ma non il partizionamento in miniblocchi.
Ci sono alcune ecezzioni:
- Se tutti gli zero di $p(s)=\Delta_{F+GK}(s)$ sono distinti ($\lambda_i$ ha molt. alg. unitaria) si ottiene: $J_{F+GK}=\begin{bmatrix}\lambda_1 \\ & \lambda_2 \\ & & \ddots \\ &  &  & \lambda_r \\\end{bmatrix}$ 
- se iniziamo con un single input reachable system $(m=1)$  sappiamo che:
	se $(F,g)$ è reachable  $\to$  $(F+gK,g)$ è reachable e $\Delta_{F+gK}=p(s)$
	$M$ è  [[Cyclic matrix|cyclic]] $\iff \exists g\in \mathbb R^n$ s.t. $(M,g)$ è reachable
- Siccome $(F+gK,g)$ è raggiungiblie la matrice $F+gK$  è cyclica ma questo significa che la sua forma di jordan ha un singolo miniblocco per ogni valore. Di conseguenza se:
	$p(s)=(s-\lambda_1)^{n_1}\dots(s-\lambda_r)^{n_r}\quad \lambda i\ne \lambda_j\quad i\ne j\quad n_i>0$ allora:
	$$
	J_{F+GK}=
	\begin{bmatrix}
\begin{bmatrix}
\lambda_1 & 1 \\
 & \lambda_1 & 1 \\
 &  & \lambda_1 \\
\end{bmatrix}\\
& \begin{bmatrix}
\lambda_2 & 1 \\
 & \lambda_2 & \ddots \\
 &  & \ddots & 1 \\
 &  &  & \lambda_2 \\
\end{bmatrix}\\
&&\begin{bmatrix}
\lambda_r & 1 \\
 & \lambda_r & \ddots \\
 &  & \ddots & 1 \\
 &  &  & \lambda_r \\
\end{bmatrix}
\end{bmatrix}
	$$
