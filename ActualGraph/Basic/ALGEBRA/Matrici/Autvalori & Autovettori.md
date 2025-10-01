[[Matrici]]
Permettono di creare matrici più semplici

$$
\begin{align}
&\{v1,v2,...,v_n\}\ base\ di\ V \quad f:V\rightarrow V\\\\
&f(v_1)=a_{11}\cdot v_1+a_{21}\cdot v_2+ \ldots+a_{n1}\cdot v_n\\
&f(v_2)=a_{12}\cdot v_1+a_{22}\cdot v_2+ \ldots+a_{n2}\cdot v_n
\end{align}
$$
Quindi per far si che esca una matrice diagonale tutte le $a_{ij}$  devono valere $0$ tranne quelle sulla diagonale($a_{11}, a_{22}...$) e quindi:
$$
\begin{cases}
f(v_1) = \lambda_1 \cdot v_1\\
f(v_2) = \lambda_2 \cdot v_2\\
\vdots\\
f(v_n) = \lambda_n \cdot v_n

\end{cases}
$$
I vettori devono essere scelti in modo tale che l'immagine tramite la funzione $f$ di ciascuno di questi vettori sia multipla dello stesso vettore
#### Definizione
Un vettore $v\neq \vec 0$ è detto autovettore di $f$ se $f(v) = \lambda \cdot v$ 
$\lambda$ si chiama autovalore
$f(v) = \lambda \cdot v \rightarrow A\cdot v =\lambda \cdot v$

### Come calcolarli
$$
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
\cdot
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
=
\lambda \cdot
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
$$
n equazioni
n+1 incognite ($x_1...x_n, \lambda$)

$$
A\cdot v = \lambda\cdot v
\qquad
A\cdot v -\lambda\cdot v = \vec 0
\qquad
(A -\lambda)v = \vec 0
$$
Non va bene perchè $A$ è matrice e $\lambda$ è numero.
Si deve considerare $\lambda$ come la matrice diagonale con tutti i valori sulla diagonale pari a $\lambda$
$$
\begin{align}
&A\cdot v = \lambda\cdot v
\qquad
A\cdot v -\lambda\cdot v = \vec 0
\qquad
(A - \lambda)v = \vec 0\\
&B = (A-\lambda\cdot I)
\qquad
B\cdot v = \vec 0
\end{align}
$$
- Esistono più soluzioni quindi non è invertibile (Gramen) e quindi $det(B) =0$
- $B$ è detto polinomio caratteristico ed il grado è pari all'ordine di $A$
- $det(A-\lambda\cdot I =0$ è l'equazione caratteristica che fornisce gli autovalori
Quindi per calcolarli si dovrà trovare il valore per il quale:
$$
det\left(
A-
\begin{bmatrix}
\lambda & 0& \dots & 0 \\
0 & \lambda & \dots & 0\\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & \lambda
\end{bmatrix}
\right) = 0
$$

- Non esistono sempre autovalori reali ma esistono sempre quelli complessi
- Se ci sono $r$ soluzioni coincidenti allora si dice che hanno molteplicità $r$ che è detta  __molteplicità algebrica__
- Due matrici simili hanno gli stessi autovalori

#### Esempio
$$
\begin{align}
&A=
\begin{bmatrix}
-7 & -9\\
6 & 8 
\end{bmatrix}\\
&det\left(
\begin{bmatrix}
-7-\lambda & -9\\
6 & 8-\lambda 
\end{bmatrix}
\right) = (-7-\lambda)(8-\lambda)-6\cdot(-9)=\lambda^2-\lambda-2=0
\end{align}
$$
- $\lambda^2-\lambda-2=0$ è lequazione caratteristica
- $\lambda$ sono gli autovalori
$$
\lambda = \frac{1\pm\sqrt{1+8}}{2} =2, -1 
$$

#### Esempio
$$
\begin{align}
&A=
\begin{bmatrix}
2 & -1\\
1 & 3 
\end{bmatrix}\\
&det\left(
\begin{bmatrix}
2-\lambda & -1\\
1 & 3-\lambda 
\end{bmatrix}
\right) = (2-\lambda)(3-\lambda)+1=\lambda^2-5\lambda-7=0
\end{align}
$$$$
\lambda = \frac{5\pm\sqrt{-3}}{2} = \frac{5\pm i\sqrt{3}}{2}
$$
#### Esempio
$$
\begin{align}
&A=
\begin{bmatrix}
 0 & 4\\
-1 & 4 
\end{bmatrix}\\
&det\left(
\begin{bmatrix}
-\lambda & 4\\
-1 & 4-\lambda 
\end{bmatrix}
\right) = (-\lambda)(4-\lambda)+4=(\lambda-2)^2=0
\end{align}
$$
$$\lambda = 2\pm \sqrt {0} $$
L'unico Autovalore è $\lambda =2$  e si dice che ha moltiplicità $2$ 

####
Ora che sappiamo trovare $\lambda$ tornamo al punto precedente:
$$
(A-\lambda\cdot I)
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0
\end{bmatrix}
$$
Questo corrisponde ad un sistema omogeneo di equazioni lineari.
- Le soluzioni non nulle sono gli autovettori che corrispondono all'autovalore $\lambda$
- L'insieme delle soluzioni di questo sistema è detto __autospazio__ relativo all'autovalore $\lambda$ 
- La dimensione di questo autospazio è detta __molteplicità geometrica__ dell'autovalore $\lambda$ 

#### Esempio
$$
\begin{align}
&A=
\begin{bmatrix}
-7 & -9\\
6 & 8 
\end{bmatrix}
\quad\lambda_1 = 2\qquad \lambda_2 = -1\\\\


Rispetto\ \lambda_1
\\&A-\lambda_1\cdot I 
=
\begin{bmatrix}
-7-\lambda_1 & -9\\
6 & 8-\lambda_1
\end{bmatrix}
=
\begin{bmatrix}
-9 & -9\\
6 & 6 
\end{bmatrix}\\\\
&\begin{bmatrix}
-9 & -9\\
6 & 6 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
= 
\begin{bmatrix}
0 \\
0
\end{bmatrix}\\\\\\


Rispetto\ \lambda_2
\\&A-\lambda_2\cdot I 
=
\begin{bmatrix}
-7-\lambda_2 & -9\\
6 & 8-\lambda_2
\end{bmatrix}
=
\begin{bmatrix}
-6 & -9\\
6 & 9 
\end{bmatrix}\\\\
&\begin{bmatrix}
-6 & -9\\
6 & 9 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
= 
\begin{bmatrix}
0 \\
0
\end{bmatrix}\\
\end{align}
$$
Per $\lambda_1$ esistono infinite soluzioni con $x_1 = -x_2$  
$$
\left\{
\begin{bmatrix}
-\alpha \\
\alpha
\end{bmatrix}
\in \mathbb{R} \ |\ \forall \alpha
\right\}\qquad 
v_1 = \begin{bmatrix}
-1 \\
1
\end{bmatrix}
$$

Per $\lambda_2$ esistono infinite soluzioni con $x_1 = -\frac{3}{2} x_2$ 
$$

v_1 = \begin{bmatrix}
-3 \\
2
\end{bmatrix}
$$

Si può provare che i due vettori sono linearmente indipendenti quindi i due autovettori sono una base di $\mathbb{R} ^2$
####
Usando i valori dell'esempio:
$$
\begin{align}
&\lambda_1 =2\rightarrow v_1(-1,1)\\
&\lambda_2 =1\rightarrow v_2(3,-2)\\
\\
&A\begin{bmatrix}-1 \\ 1\end{bmatrix} = 2\begin{bmatrix}-1 \\ 1\end{bmatrix} = \begin{bmatrix}-2 \\ 2\end{bmatrix}\\
&A\begin{bmatrix}-3 \\ -2\end{bmatrix} = -1\begin{bmatrix}-3 \\ -2\end{bmatrix} = \begin{bmatrix}-3 \\ 2\end{bmatrix}\\
\\
&A
\begin{bmatrix}
-1 & 3\\
1 & -2 
\end{bmatrix}
=
\begin{bmatrix}
-2 & -3\\
2 & 2 
\end{bmatrix}
=
\begin{bmatrix}
-1 & 3\\
1 & -2 
\end{bmatrix}
\begin{bmatrix}
2& 0\\
0 & -1 
\end{bmatrix}\\
&\quad
\underbrace{\hspace{2cm}}_{\text{S}}
\qquad\qquad\qquad\quad\;\;\;
\underbrace{\hspace{2cm}}_{\text{S}}
\;\;
\underbrace{\hspace{1.8cm}}_{\text{D}}
\quad
\end{align}
$$
#matrici_cambiamento_di_base
$$
\begin{align}
&A\cdot S = S\cdot D &S\ è\ la \ matrice\ le\ cui\ colonne\ sono \ autovettori \\
&A=S\cdot D\cdot S^-1 \qquad dove \quad &D\ è\ la\ matrice\ diagonale\ con\ i \ valori\ di\  \lambda \\
&D=S^-1\cdot A\cdot S\ &A\ e\ D\ sono\ simili&
\end{align}
$$
Sono le stesse formule del cambiamento di base 
- $S$ è la matrice di cambiamento di base 
Una matrice si dice diagonabizzabile se:
- è simile ad una matrice diagonale
- se sono presenti $n$ autovalori uguali si deve vedere la dimensione dell'autospazio generato da essi è pari alla loro molteplicità $n$

### Teorema 
Se tutti gli autovalori di $A$ sono distinti tra loro($\lambda_i \neq \lambda_j$) allora gli autovettori sono linearmente indipendenti
### Teorema
#molteplicita
Si ha sempre la
$$
molteplicità\ geometrica \leq molteplicità\ algebrica
$$
(dimostrazione Lezione 25)

### Teorema 
#simmetrica
Sia $A$ matrice simmetrica di ordine $n$ a coefficienti reali
Allora A possiede $n$ autovalori reali (eventualmente non tutti distinti)