[[Matrici]]
### Gauss
$$
A=
\begin{bmatrix}
* & * & \dots & * \\
0 & * & \dots & * \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & *
\end{bmatrix}
\rightarrow
\begin{bmatrix}
* & 0 & \dots & 0 \\
0 & * & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & *
\end{bmatrix}
\rightarrow
\begin{bmatrix}
1 & 0 & \dots & 0 \\
0 & 1 & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & 1
\end{bmatrix}
$$
Se è possibile, una volta raggiunta la matrice identica la martrice inversa di $A$ sarà la matrice creata eseguendo le stesse operazioni elementari effettuate su di $A$.
L'inversa della matrice $A$ esiste se il rango è massimo
$$
(A\ \vdots\ I) \rightarrow (I\ \vdots\ B)
$$
$B$ è l'inversa di $A$:
$$B\cdot A =I$$

#### Esempio
$$
\begin{align}
&
\begin{bmatrix}
1 & 2 & 1 &\vdots & 1 & 0 & 0\\
1 & 3 & 0 &\vdots & 0 & 1 & 0\\
1 & 2 & 2 &\vdots & 0 & 0 & 1\\
\end{bmatrix}
\xrightarrow{\substack{riga2- riga1\\ riga3- riga1}}
\begin{bmatrix}
1 & 2 & 1 &\vdots & 1 & 0 & 0\\
0 & 1 & -1 &\vdots & -1 & 1 & 0\\
0 & 0 & 1 &\vdots & -1 & 0 & 1\\
\end{bmatrix}
\xrightarrow{\substack{riga2+ riga3\\ riga1- riga3}}\\
&
\begin{bmatrix}
1 & 2 & 0 &\vdots & 2 & 0 & -1\\
0 & 1 & 0 &\vdots & -2 & 1 & 1\\
0 & 0 & 1 &\vdots & -1 & 0 & 1\\
\end{bmatrix}
\xrightarrow{\substack{riga1+ 2\cdot riga2}}
\begin{bmatrix}
1 & 0 & 0 &\vdots & 6 & -2 & -3\\
0 & 1 & 0 &\vdots & -2 & 1 & 1\\
0 & 0 & 1 &\vdots & -1 & 0 & 1\\
\end{bmatrix}
\end{align}
$$
### Laplace 
Utile solo per la teoria non per la pratica
Si costruisce $A^* = (A_{ij}^*)^t$  e il prodotto di $A \cdot A^*$  da una matrice che ha sulla diagonale tutti numeri uguali che sono il determinante di $A$ quindi:
$$ A^{-1} = \frac{A^*}{det(A)}$$

### E' unica?
Si, la matrice inversa di $A$ può essere messa sia a destra che sinistra di $A$, in ogni caso il risultato rimane $I$
$$
\begin{align}
(B\cdot A)C &= B(A\cdot C)\\
I\cdot C &= B \cdot I\\
C &= B
\end{align}
$$
