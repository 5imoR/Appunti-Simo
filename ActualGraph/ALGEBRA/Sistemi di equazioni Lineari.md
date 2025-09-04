[[ALGEBRA]][[Matrici]][[Vettori]]
$$
\begin{align}
\begin{cases}
a_{11}\cdot x_1 +\dots +a_{1m}x_m = b_1 \\
a_{21}\cdot x_1 +\dots +a_{2m}x_m = b_2 \\
\vdots\qquad \qquad \ddots \qquad \qquad \vdots \\
a_{m1}\cdot x_1 +\dots +a_{mm}x_m = b_m \\
\end{cases}
X=
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_m
\end{bmatrix}
B=
\begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_m
\end{bmatrix}
A =(a_{ij}) m \times n
\end{align}
$$
Dove:
- $A$ è la matrice dei coefficienti del sistema
- $X$ è il vettore delle incognite
- $B$ è il vettore dei termini noti

$$
A\cdot X=B 
\qquad \qquad
X = A^{-1}\cdot B
$$

Funzione lineare f che manda $X$ in $AX$ 
$$
X = 
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_m
\end{bmatrix}
\xrightarrow{f}
f(x)=
A\cdot
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_m
\end{bmatrix}
=
B
\qquad B\in Im(f)
$$
Le soluzioni sono tutti i valori di $X$ che soddisfano il sistema
$$
f^{-1}(B) = \{ X | AX = B\}
$$
- Se $B = \vec{0}$  le soluzioni saranno $ker(f)$


###### Esempio
$AX = B$ sistema lineare non omogeneo
$AX = \vec 0$ sistema omogeneo associato $\rightarrow$ si trova $ker(f)$

Sia $\overline{X}$ una soluzione di $AX=B$
Sia $Y$ una soluzione di $AY=0$
$\overline{X} + Y$ è un altra soluzione di $AX=B$
- Vuol dire che partendo da una soluzione del sistema lineare non omogeneo e una soluzione del kernel, posso trovare altre soluzioni del sistema lineare non omogeneo

Siano $\overline{X_1},\overline{X_2}$ soluzioni di $AX=B$
$Y=\overline{X_1}-\overline{X_2} \qquad AY = A(\overline{X_1}-\overline{X_2}) = B-B= \vec 0$ 
- Vuol dire che partendo da due soluzioni del sistema non omogeneo posso ottenere una soluzione dei sistema omogeneo

Le soluzioni di $AX=B$ sono tutte del tipo:
$$
\{\overline{X}+Y | dove\quad Y \in AX=\vec 0 \} 
$$

###### Esercizio
$$
A=
\begin{bmatrix}
1 &-3 &2\\
-2 & 6 &-4
\end{bmatrix}
\quad 
X=
\begin{bmatrix}
x_1\\x_2\\x_3
\end{bmatrix}
\quad
B=
\begin{bmatrix}
b_1\\b_2
\end{bmatrix}
$$
1.  risolvere $AX=\vec 0$
2. trovare per quali $B \in \mathbb{R}^2$ il sistema  $AX=B$ ammette soluzioni
3. risolvere $AX = B$ con $B = \begin{bmatrix}5\\-10\end{bmatrix}$ 
---
1. Infinite soluzioni $\forall x_2,x_3$ quindi $dim(ker(f))=2$. Quindi $ker(f)$ è formato da $v_1 + v_2$ 
$$
\begin{align}
AX=\vec 0 
\begin{cases}
x_1 -3x_2+2x_3 =0\\
-2x_1+6x_2-4x_3=0
\end{cases}
=
\begin{cases}
x_1 =3x_2-2x_3\\
0=0
\end{cases} \\
v_1=
\begin{bmatrix}
3\\1\\0
\end{bmatrix}
v_2=
\begin{bmatrix}
-2\\0\\1
\end{bmatrix}
\end{align}
$$

2. Dal quale ricaviamo che ammette soluzioni solo se  $2b_1+b_2 =0$
$$
\begin{align}
AX=B 
\begin{cases}
x_1 -3x_2+2x_3 =b_1\\
-2x_1+6x_2-4x_3=b_2
\end{cases}
\end{align}
$$
 
3. Questo equivale a $f^{-1}(B) = \overline X + ker(f)$ 
$$
\begin{align}
AX=B 
\begin{cases}
x_1 -3x_2+2x_3 =5\\
-2x_1+6x_2-4x_3=-10
\end{cases}
\end{align}
$$
![[X+ker(f)]]


### Teorema di Rouché-Capelli
Un sistema lineare $A\cdots X= B$ ammette soluzioni se e solo se:
$$
\begin{align}
rango(A) = rango (A\:\vdots \: B)
\\\\

\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} & \vdots &b_1\\
a_{21} & a_{22} & \dots & a_{2n} & \vdots &b_2\\
\vdots & \vdots & \ddots & \vdots & \vdots&\vdots\\
a_{m1} & a_{m2} & \dots & a_{mn} & \vdots &b_m
\end{bmatrix}

\end{align}
$$
$rango(A) = r$
$rango(A\:\vdots \: B$ se:
- $= r+1$ $B$ è linearmente indipendente  dalle colonne di $A$
- $=r$ B è linearmente dipendente dalle colonne di $A$

sono presenti $n$ incognite nel nostro sistema se:
- $r=n$ la soluzione è unica 
- $r<n$ ci sono $\infty$ soluzioni  ($\infty^{n-r}$)

