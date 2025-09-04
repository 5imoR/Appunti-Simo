[[Matrici]][[Permutazione]]

$A = (a_{ij})$ matrice $n\times n$ 
$S_n =$ $\sigma$ permutazioni

$$
det(A) = \sum_{\sigma \in S_n}segno(\sigma)\cdot a_{1\sigma_1}\cdot a_{2\sigma_2}\cdot \ldots \cdot a_{n\sigma_n}
$$
Equivale a dire la somma di ogni elemento della matrice in tutti i modi possibili.In una matrice $4\times4$ sarebbe la somma di $24$ elementi. **Poco pratica**

### Proprietà
Tutte le proprietà dei determinanti che valgono per le righe valgono anche per le colonne

---
- $A$ matrice triangolare
$$
A=
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
0 & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & a_{nn}
\end{bmatrix}
\rightarrow
det(A) =a_{11}\cdot a_{22}\cdot \ldots \cdot a_{nn}
$$
Il determinante è il prodotto degli elementi sulla diagonale principale

--- 
- $A^t$ matrice trasposta di $A$
$det(A^t) = det(A)$
---
- Se sono presenti delle operazioni sulle righe il determinante ne risente
$$
\begin{align}
&A=
\begin{bmatrix}
2 &1 &-1\\
6 &1 &2\\
-4 &3 &-3\\
\end{bmatrix}
\xrightarrow{\color{orange}r2-3r1}
\begin{bmatrix}
2 &1 &-1\\
0 &-2 &5\\
-4 &3 &-3\\
\end{bmatrix}
=A'\\\\
&Allora:\\\\
&det(A') =
det
\begin{bmatrix}
2 &1 &-1\\
\color{orange}6 &\color{orange}1 &\color{orange}2\\
-4 &3 &-3\\
\end{bmatrix} 
{\color{orange}- 3}\cdot det
\begin{bmatrix}
2 &1 &-1\\
\color{orange}2 &\color{orange}1 &\color{orange}-1\\
-4 &3 &-3\\
\end{bmatrix}
\end{align}
$$
---
- Sia $A'$ la matrice ottenuta scambiando 2 righe fra loro il determinante sarà:
$$det(A') = -det(A)$$
- Sia $A'$ la matrice ottenuta moltipicando una riga per $\lambda$ il determinante sarà:
$$
det(A') )=\lambda det(A)
$$
- Se una matrice ha due righe uguali  il determinante sarà:
$$det(A) = 0$$
- Supponendo che $A$ abbia una riga nulla il determinante sarà
$$ det(A) = 0$$
- Se ad una riga di $A$ si somma una combinazione lineare di altre righe di $A$ il determinante di $A$ non cambia

- Se una matrice ha determinante diverso da 0 allora è invertibile 
### Teorema di Binet

$A,B$ matrici $n\times n$
$$
det(A \cdot B) = det(A)\cdot det(B)\qquad det(A+B)\neq det(A)+det(B)
$$

### Determinante dell'inversa
Se $A$ è invertibile $A\cdot A^{-1} = I$  allora (tramite il teorema di Binet):
$$
det(A\cdot A^{-1}) = det (I) = 1
\Rightarrow
det(A^{-1}) = 1/det(A)
$$
### Teorema di Gramen
Utile solo dal lato teorico [Lezione 22]([[a]][https://www.youtube.com/watch?v=ZPf8icgW47M&list=PLhEwqlL10MqMSHePf3Kn4T8AaR0ItUUer&index=22]) al minuto 25 circa
### Matrice  2x2
$$
\begin{align}
A = 
\begin{bmatrix}
a &b\\c &d
\end{bmatrix}
\qquad
A^{-1} = 
\begin{bmatrix}
\frac{d}{ad-bc} &-\frac{b}{ad-bc}\\
-\frac{c}{ad-bc} &\frac{a}{ad-bc}
\end{bmatrix}\\\\
\exists A^{-1} \Leftrightarrow ad-bc\neq 0\qquad\qquad
\end{align}
$$
Il determinante di una matrice $2\times2$  è :
$$
det(A) = ad-bc
$$ 
### Matrice 3x3
#### Regola di Sarrus
Si prendono i prodotti degli elementi sulle diagonali che vanno in basso a destra e si scrivono i valori con il segno positivo.
Si prendono i prodotti degli elementi sulle diagonali che vanno in basso a sinistra e si scrivono i valori con il segno negativo.
$$
\begin{bmatrix}
a_{11}&a_{12}&a_{13}&&a_{11}&a_{12}\\
a_{21}&a_{22}&a_{23}&&a_{21}&a_{22}\\
a_{31}&a_{32}&a_{33}&&a_{31}&a_{32}\\
\end{bmatrix}
\quad\Rightarrow\quad
\begin{align}
a_{11}\cdot a_{22}\cdot a_{33} +
a_{12}\cdot a_{23}\cdot a_{31} +
a_{13}\cdot a_{21}\cdot a_{32}\\
-a_{11}\cdot a_{23}\cdot a_{32}
-a_{13}\cdot a_{22}\cdot a_{31}
-a_{12}\cdot a_{21}\cdot a_{33}\\
\end{align}
$$
Il risultato equivale al determinante della matrice
### Matrice nxn
#### Formula di Laplace
$$
A = 
\begin{bmatrix}
&\vdots&\\
\cdots& a_{ij}&\cdots\\
&\vdots&\\
\end{bmatrix}
$$
Definisco la matrice $aA_{ij}$ che è la matrice ottenuta andando a togliere ad $A$ la riga $i$ e la colonna $j$ di ordine $n-1$

- Fissiamo la riga $i$
$$
\begin{align}
&A=
\begin{bmatrix}
\cdots &\cdots&\cdots\\
a_{i1}& \cdots&a_{in}\\
\cdots &\cdots&\cdots\\
\end{bmatrix}
\qquad
\begin{aligned}
det(A) =&\\ 
&(-1)^{i+1}a_{i1}\cdot det(A_{i1})+\\
&(-1)^{i+2}a_{i2}\cdot det(A_{i2})+\\
&\dots+\\
&(-1)^{i+n}a_{in}\cdot det(A_{in})\\
\end{aligned}\\\\
&det(A)=\sum_{j=1}^n \left[(-1)^{i+j}\cdot det(A_{ij})\right] = \sum_{j=1}^n a_{ij}^*
\end{align}
$$
- Più zeri sono presenti nella riga $i$ o colonna $j$  più saranno semplici i conti
- La matrice $A_{ij}$ è la matrice $A$ senza gli elementi della riga $i$ e colonna $j$
- $a_{ij}^*$ è chiamato il complemento algebrico (cofattore) dell'elemento $a_{ij}$
