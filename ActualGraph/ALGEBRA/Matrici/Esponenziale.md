[[Matrici]]
Come definire $e^A$ ?

$e^x=1+x+\frac{x^2}{2!}+...$ 

$e^A =I+A+\frac{A^2}{2!}+...$  


Se $A$ è diagonale
$$
A=
\begin{bmatrix}
\lambda_1 & 0 & \dots & 0 \\
0 & \lambda_2 & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0& 0& \dots & \lambda_n
\end{bmatrix}
$$
$A^m$ sarà:
$$
A=
\begin{bmatrix}
\lambda_1^m & 0 & \dots & 0 \\
0 & \lambda_2^m & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0& 0& \dots & \lambda_n^m
\end{bmatrix}
$$
Quindi $e^D$:
$$
e^D=
\begin{bmatrix}
 e^{\lambda_1} & 0 & \dots & 0 \\
0 &  e^{\lambda_2} & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0& 0& \dots & e^{\lambda_n}
\end{bmatrix}
$$

### Caso in cui non sia diagonale
Si guarda se è diagonabizzabile.
Se è diagonizzabile $A^n=S^{}\cdot D\cdot S^{}$
Quindi $e^A$ equivale a:
$$e^A=S^{}\left[I+D+\frac{D^2}{2!}+...\right]S^{-1}$$
$$
e^D=S
\begin{bmatrix}
 e^{\lambda_1} & 0 & \dots & 0 \\
0 &  e^{\lambda_2} & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0& 0& \dots & e^{\lambda_n}
\end{bmatrix}S^{-1}
$$