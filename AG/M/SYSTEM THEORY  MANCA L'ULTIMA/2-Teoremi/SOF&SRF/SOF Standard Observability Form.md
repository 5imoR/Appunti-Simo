### Theorem SOF
$T=(S^{-1})^T$ 
$$
\begin{align}
\begin{array}{c}
(F,H)\text{ is not}\\
\text{observable}
\end{array}
&\iff
\begin{array}{c}
(F^T, H^T)\text{ is not}\\
\text{reachable}
\end{array}\\
&\phantom {ssssssssss}\Updownarrow\\
\begin{array}{c}
\exists T\in \mathbb R^{n\times n} \text{ non sing. s.t.}\\
\small
T^{-1}FT=\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}\\
\small HT=\begin{bmatrix}H_1&0\end{bmatrix}\\
\text{with $(F_{11}, H_1)$ observable}
\end{array}
&\iff
\begin{array}{c}
\exists S\in \mathbb R^{n\times n} \text{ non sing. s.t.}\\
\small S^{-1}FS=\begin{bmatrix}F_{11}^T&F_{12}^T\\0& F_{22}^T\\\end{bmatrix}
\small S^{-1}H^T=\begin{bmatrix}H_1^T\\0\end{bmatrix}\\\\
\text{with $(F_{11}^T, H_1^T)$ reachable}
\end{array}
\end{align}
$$
####   Standard Observability Form SOB
Supponiamo di avere il sistema $\Sigma = (F,G,H)$ in SOF
$$
\begin{align}
 F=\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}
\begin{array}{c}\}\rho\phantom{ssss} \\\}n-\rho\end{array}
\qquad
 G=\begin{bmatrix}G_1\\ 0\end{bmatrix}
\begin{array}{c}\}\rho\phantom{ssss} \\\}n-\rho\end{array}
\qquad 
 H=\begin{bmatrix}H_1& 0\end{bmatrix}\ \}p\quad\text{ with $(F_{11},H_1)$ observable}\\
\underbrace{}_\rho\underbrace{}_{n-\rho}\phantom{sssssssssssssssss}\underbrace{}_{m}\phantom{ssssssssssasssss}\underbrace{}_\rho\underbrace{}_{n-\rho}\phantom{sssssssssaasssssssssssssssss}
\end{align}
$$
### Proof
Deriva dalla duality di [[SRF Standard Reachability Form]]
