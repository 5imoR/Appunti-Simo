### Theorem OCF
$T=(S^{-1})^T$ 
$$
\begin{align}
\begin{array}{c}
(F,H)\text{ with }H\in\mathbb R^{1\times n} \text{ is observable}\\
\text{(single output system)}
\end{array}
&\iff 
\begin{array}{c}
(F^T,H^T)\text{ is reachable}\\
\text{(single input system)}
\end{array}\\
\Updownarrow\qquad \qquad\qquad & \qquad\qquad\qquad\qquad\Updownarrow\\
\begin{array}{c}
\exists T\in \mathbb R^{n\times n} \text{ non sing. s.t.}\\
\text{observable canonical form}\\
\small T^{-1}FT=
\begin{bmatrix}
0 &  &  & -a_0 \\
1 &  &  & -a_1 \\
 & \ddots &  & \vdots \\
 &  & 1 & -a_{n-1} \\
\end{bmatrix}\\
\small HT=\begin{bmatrix} 0 & \dots & 0 & 1 \end{bmatrix}
\end{array}
&\iff
\begin{array}{c}
\exists S\in \mathbb R^{n\times n} \text{ non sing. s.t.}\phantom{sssssssssssssssssss}\\
\text{controllable canonical form}\phantom{sssssssssssssssssss}\\
\small S^{-1}F^TS=
\begin{bmatrix}
0 & 1 &  &  \\
 &  & \ddots &  \\
 &  &  & 1 \\
-a_0 & -a_1 & \dots & -a_{n-1} \\
\end{bmatrix}
S^{-1}H^T=\begin{bmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}
\end{array}
\end{align}
$$
### Proof
Deriva dalla duality della [[CCF Controlled Canonical Form]]
