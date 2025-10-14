[[ALGEBRA]][[Vettori]][[Funzioni Lineari]]
### Introduzione
$f:V \rightarrow W$ lineare con:
$\{v_1,...,v_n\}$ base di $V$
$\{w_1,...,w_m\}$ base di W
- $f(v_1) \in W$ = $a_1w_1+...+a_mw_m$
- ...
- $f(v_n) \in W$ = $z1w_1+...+z_mw_m$
oppure
- $f(v_j)$ = $a_{1j}w_1+...+a_{mj}w_m$

$A = (a_{ij})$  è una matrice 
	$i=1,...,m = dim (W)$
	$j=1,...,n = dim(V)$
	$-A$ è la matrice che sommata ad A da la matrice nulla ( tutti 0)

$M(m \times n)$ $m$=righe $n$=colonne
$$
A=
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
$$
$A = M^{\underline{W}}_{\underline{V}}(f)$  è la matrice di $f:V \rightarrow W$
### Rango
 Il numero di colonne linearmente indipendenti
- Il numero di righe indipendenti è sempre uguale al numero di colonne linearmente indipendenti
### Operazioni
##### Somma
$(f+g)(v_j) = f(v_j)+g(v_j) = \sum_i a_{ij}w_i+\sum_i b_{ij}w_i = \sum_i (a_{ij}+b{ij})w_i$ 
$$
A+B=
\begin{bmatrix}
a_{11}+b_{11} & a_{12}+a_{12} & \dots & a_{1n}+b_{1n} \\
a_{21}+b_{21} & a_{22}+b_{22} & \dots & a_{2n}+b_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1}+b_{m1} & a_{m2}+b_{m2} & \dots & a_{mn}+b_{mn}
\end{bmatrix}
$$
##### Prodotto per uno Scalare
$$
\lambda \cdot A=
\begin{bmatrix}
\lambda \cdot a_{11} & \lambda \cdot a_{12} & \dots &\lambda \cdot  a_{1n} \\
\lambda \cdot a_{21} & \lambda \cdot a_{22} & \dots & \lambda \cdot a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
\lambda \cdot a_{m1} & \lambda \cdot a_{m2} & \dots & \lambda \cdot a_{mn}
\end{bmatrix}
$$

##### Prodotto tra Matrici
###### Composizione di Funzioni
$v \in V  \xrightarrow{f} f(v) \in W  \xrightarrow{g} Z$   oppure   $V \xrightarrow{g_of} Z$
$(g_of)(v) = g(f(v))$

$$A = M^{\underline{W}}_{\underline{V}}(f) \quad
B = M^{\underline{Z}}_{\underline{W}}(g) \quad
C=M^{\underline{Z}}_{\underline{V}}(g_of)$$
$$
\begin{align}
 f(v_j)=\sum_{i=1}^ma_{ij}w_i\qquad A=M_\underline{v}^\underline{w}(f)\\
 g(w_i)=\sum_{h=1}^mb_{hi}z_h\qquad B=M_\underline{w}^\underline{z}(g)\\
 
(g_of)(v_j)=\sum_{h=1}^r \left(\sum_{i=1}^m b_{hi}\cdot a_{ij} \right)z_{h}=\sum_{h=1}^rc_{hj}\cdot z_h\qquad C=M_\underline{v}^\underline{z}(g_of)
\end{align}
$$

###### Prodotto effettivo
Si moltiplica la i-esima riga per la j-esima colonna
$$
c_{hj} =\sum_{i=1}^m b_{hi}\cdot a_{ij}
$$

$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23}
\end{bmatrix}
\cdot
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
b_{31} & b_{32}
\end{bmatrix}
=
\begin{bmatrix}
a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31} & a_{11}b_{12} + a_{12}b_{22} + a_{13}b_{32} \\
a_{21}b_{11} + a_{22}b_{21} + a_{23}b_{31} & a_{21}b_{12} + a_{22}b_{22} + a_{23}b_{32}
\end{bmatrix}
$$
#### Proprietà
- Esistono matrici che se elevate alla $n$ danno la matrice nulla 
- $A \cdot B \neq B \cdot A$
- $(A \cdot B)C = A(B\cdot C)$
- $(A + B)C = A\cdot C + B\cdot C$  e viceversa
- esiste l'elemento neutro per il prodotto
$$
I=
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$
- trasposizione:
	$A^t$ è la trasposta di $A$ e si ottiene invertendo le righe con le colonne 

### Operazioni elementari
Possono essere fatte sulle righe o sulle colonne ed hanno una rappresentazione matriciale:
- scambiare due righe tra loro
$$
P(1,3)=
\begin{bmatrix}
0&0&1&0&0\\
0&1&0&0&0\\
1&0&0&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{bmatrix}
$$
$P(i,j)\cdot A$ ottiene la matrice $A$ con le righe $i$ e $j$ invertite
$A\cdot P(i,j)$ ottiene la matrice $A$ con le colonne $i$ e $j$ invertite

- modificare una riga per un numero $\neq 0$ 
$$
M(4,\lambda)=
\begin{bmatrix}
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&\lambda&0\\
0&0&0&0&1
\end{bmatrix}
$$
$M(i,\lambda)\cdot A$ ottiene la matrice $A$ con l'iesima riga moltiplicata per $\lambda$ 
$A\cdot M(i,\lambda)$ ottiene la matrice $A$ con l'iesima colonna moltiplicata per $\lambda$ 

- sommare(sottrarre) ad una riga una combinazione lineare delle altre righe
$$
S(3,4,\alpha)=
\begin{bmatrix}
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&\alpha&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{bmatrix}
$$
$S(i,j,\alpha)\cdot A$ ottiene la matrice $A$ con sulla $i$-esima riga la somma della riga $i$ e la riga $j$ moltiplicata per $\alpha$ 
$A \cdot S(i,j,\alpha)$ ottiene la matrice $A$ con sulla $i$-esima colonna la somma della colonna $i$ e la colonna $j$ moltiplicata per $\alpha$ 

La matrice risultante sarà qualcosa del tipo:
$$
S(...)\cdot S(...)\cdot M(...)\cdot P(...)\cdot A = A'
$$ con a sinistra le ultime matrici applicate

**Queste operazioni non midificano il rango della matrice**




## Tipi di Matrici
### Matrici simili
Si dicono simili se rappresentano la stessa funzione rispetto a basi diverse
$$
A = P^{-1}\cdot B\cdot P\qquad det(A)=det(B)
$$
Ciò non include che $A = B$ 

### Matrici diagonabizzabili
#molteplicita
Una matrice $A(n\times n)$ si dice diagonabizzabile se e solo se esistono autovalori di $A$ tali che la somma delle loro molteplicità algrebriche sia $n$.
Inoltre per ogni autovalore, la sua molteplicità geometrica deve essere uguale alla molteplicità algebrica

Questo vuol dire che devono esserci massimo n autovalori e ogni autovalore deve generare abbastanza autovettori per creare una base

### Matrice Simmetrica
#simmetrica
$A$ è simmetrica se $A^T=A$ 
A è antisimmetrica se $A^T = -A$ 

### Matrici di Proiezione



##
## Matrice e funzioni lineari
$A$ matrice $m\times n$ ($m$ righe e $n$ colonne)
- $A$ corrisponde alla funzione lineare:  
	$f:V \rightarrow W\qquad\qquad m=dim(W) \quad n=dim(V)$
- $A^{-1}$ corrisponde alla funzione:
	$f^{-1}:W \rightarrow V$ 
$A$ invertibile $\Leftrightarrow$ $f$ invertibile

$$
\begin{align}
A\ invertibile &\Leftrightarrow  f \ invertibile\\
&\Leftrightarrow f\ biiettiva\\
&\Leftrightarrow f\ (initettiva\ e \ suriettiva)\\
&\Leftrightarrow f\ isomorfa
\end{align}
$$
- Quindi per essere isomorfa  la matrice deve essere quadrata quindi solo le matrici quadrate possono essere invertibili
- Se  $ker(f) = \{\vec 0\}$ allora è iniettiva 
- Se $ker(f) = \{\vec 0\}$ allora $dim(Im(f)) = dim(W)$
- Se $dim(Im(f)) = dim(W)$ allora è suriettiva

