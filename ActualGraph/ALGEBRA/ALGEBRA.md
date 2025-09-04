$f:V \rightarrow W$ 


$dim(Ker(f)) + dim(Im(f)) = dim(V) = n$
- $dim(Ker(f))$ si chiama nullità di $f$
- $dim(Im(f))$ si chiama rango di $f$
- $n$ è il numero di incognite presenti nel sistema
- $rango(A)$ è il numero di colonne/righe/equazioni linearmente indipendenti di $A$
$$
\begin{align}
\begin{bmatrix}
a_{11} \\a_{21} \\\vdots \\a_{m1}
\end{bmatrix} \cdot x_1 +
\begin{bmatrix}
a_{12} \\a_{22} \\\vdots \\a_{m2}
\end{bmatrix} \cdot x_2 +\cdots +
\begin{bmatrix}
a_{1n} \\a_{2n} \\\vdots \\a_{mn}
\end{bmatrix} \cdot x_m =
\begin{bmatrix}
b_{1} \\b_{2} \\\vdots \\b_{m}
\end{bmatrix}\\
A_1\qquad\qquad\quad A_2\qquad\qquad\qquad\quad\: A_m\qquad\qquad\: B\quad
\end{align}
$$ $A_1,A_2,...,A_m$ sono le colonne di $A$
In notazione vettoriale: $A_1\cdot x_1+A_2\cdot x_2+\dots+A_m\cdot x_m = B$ 

$B$ è combinazione lineare delle colonne di $A$ quindi $B\in Im(f)$
### Formula di Grassman
$$
\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)
$$

### Teorema di Rouché-Capelli
Un sistema lineare $A\cdots X= B$ ammette soluzioni se e solo se:
$$rango(A) = rango (A\:\vdots \: B)$$

### Metodo di eliminazione Gauss
$$
A=
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
0 & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & a_{m2} & \dots & a_{mn}
\end{bmatrix} 
\rightarrow
\begin{bmatrix}
* & * & \dots & * \\
0 & * & \dots & * \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & *
\end{bmatrix} 
$$
