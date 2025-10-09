#ST-L2
[[SYSTEM THEORY]]
Una matrice $J\in \mathbb{C}^{n\times n}$  è detta in *Jordan form* se dopo permutazioni di righe e colonne può essere scritta nel seguente modo:

| $J=\begin{bmatrix}[J_1]&0&\cdots& 0\\0&[J_2]&\cdots& 0\\\vdots&\vdots&\ddots&\vdots&\\0&0&\cdots&[J_n]\end{bmatrix}$              | $J_i\in \mathbb{C}^{n_i\times n_i}$<br>$J_i$: jordan mini-block<br>$\lambda_i\in\mathbb{C}\quad \lambda_i\neq\lambda_j$ |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| $J_i=\begin{bmatrix}[J_{i1}]&0&\cdots& 0\\0&[J_{i2}]&\cdots& 0\\\vdots&\vdots&\ddots&\vdots&\\0&0&\cdots&[J_{is_i}]\end{bmatrix}$ | $J_{ik}\in \mathbb{C}^{n_{ik}\times n_{ik}}$<br>$J_{ik}$: jordan mini-block                                             |
| $J=\begin{bmatrix}\lambda_i&1&\cdots& 0\\0&\lambda_i&\ddots& 0\\\vdots&\vdots&\ddots&1&\\0&0&0&\lambda_i\end{bmatrix}$            | La diagonale sopra la diagonale ha tutti 1<br>$n_{i1}\geq n_{i2}\geq ...\geq n_is_i$                                    |

#### Esempio 1
$$
J=
\begin{bmatrix}
\begin{bmatrix}
\begin{bmatrix}
{\color{orange}2}&1\\
&{\color{orange}2}&1\\
&&{\color{orange}2}\\
\end{bmatrix}\\
&\begin{bmatrix}
{\color{orange}2}&1\\
&{\color{orange}2}\\
\end{bmatrix}\\
\end{bmatrix}\\
&\begin{bmatrix}
\begin{bmatrix}
{\color{lightgreen}3}&1\\
&{\color{lightgreen}3}\\
\end{bmatrix}\\
&{\color{lightgreen}3}\\
&&{\color{lightgreen}3}\\
\end{bmatrix}\\
\end{bmatrix}
$$


- $\triangle_J(z)=(z-2)^{\color{orange}5}(z-3)^{\color{lightgreen}4}$ 
- $\lambda_1=2\quad \lambda_2=3$
- $n_1,n_2,...,n_r$ sono le molteplicità algebriche
$dim(U_{\lambda_i}= dim[ker(\lambda_iIm-J)]$
$dim\ ker=n-rank[\lambda_iIm-J]$
Quali sono le molteplicità geometriche di $\lambda_1, \lambda_2$?
$$
J-2I=
\begin{bmatrix}
\begin{bmatrix}
{\color{orange}\begin{bmatrix}
0&1\\
&0&1\\
&&0\\
\end{bmatrix}}\\
&{\color{orange}\begin{bmatrix}
0&1\\
&0\\
\end{bmatrix}}\\
\end{bmatrix}\\
&\begin{bmatrix}
\begin{bmatrix}
1&1\\
&1\\
\end{bmatrix}\\
&1\\
&&1\\
\end{bmatrix}\\
\end{bmatrix}
$$
- $n=9$
- $rank(J-2I)=7$
- $dim(ker(2I-J))={\color{orange}2}$
molteplicità 2

$$
J-3I=
\begin{bmatrix}
\begin{bmatrix}
\begin{bmatrix}
-1&1\\
&-1&1\\
&&-1\\
\end{bmatrix}\\
&\begin{bmatrix}
-1&1\\
&-1\\
\end{bmatrix}\\
\end{bmatrix}\\
&\begin{bmatrix}
{\color{lightgreen}\begin{bmatrix}
0&1\\
&0\\
\end{bmatrix}}\\
&{\color{lightgreen}0}\\
&&{\color{lightgreen}0}\\
\end{bmatrix}\\
\end{bmatrix}
$$
- $n=9$
- $rank(J-2I)=6$
- $dim(ker(2I-J))=\color{lightgreen}3$
motleplicità 3

La molteplicità geometrica degli autovalori $\lambda_i$ coincide con il numero di mini-block associati dall'autovalore

#### Esempio 2
$$
J=
\begin{bmatrix}
\begin{bmatrix}
1&1\\
&1
\end{bmatrix}\\
&\begin{bmatrix}
2&1\\
&2
\end{bmatrix}\\
&&0\\
&&&\begin{bmatrix}
2&1\\
&2&1\\
&&2
\end{bmatrix}\\
&&&&1
\end{bmatrix}
$$
**Dati**

| $i$ | $\lambda_i$ | n_i | molt. geom. |
| --- | ----------- | --- | ----------- |
| 1   | 1           | 3   | 2           |
| 2   | 2           | 5   | 2           |
| 3   | 0           | 1   | 1           |
Data una matrice $F\in\mathbb{R}^{n\times n}$ un polinomio $p(s)\in \mathbb{R}[s]$:
$$
p(s)=p_ds^d+p_{d-1}s^{d-1}+...+p_1s+p_0
$$
è chiamato *annihilating polinomial* di $F$ se:
$$
p(F)=p_dF^d+p_{d-1}F^{d-1}+...+p_1F+p_0=O_{n\times n}
$$
Se consideriamo $P_F$ di tutti gli annihilating polinomial di F possiamo provare che esiste un polinomio MONICO  di grado minimo $\Psi_F(s)$  in $P(s)$ tale che 
$$
\begin{align}
p(s)\in P_F\iff p(s) \text{ è un multiplo di }\Psi_F(s)\\\\
\exists q(s)\in\mathbb{R}[s] \text{ tale che } p(s)=\Psi_F(s)q(s)

\end{align}
$$
$\Psi_F(s)$ è chiamato *minimal annihilating polinomial* di $F$
E' possibile comprovare che  se $J$ è in Jordan Form:

$$
\Psi_J(s)=(s-\lambda_1)^{n_{11}}(s-\lambda_2)^{n_{21}}...(s-\lambda_r)^{n_{r1}}
$$

#### Esempio 3
$$
J=
\begin{bmatrix}
\begin{bmatrix}
{\color{orange}2}&1\\
&{\color{orange}2}&1\\
&&{\color{orange}2}
\end{bmatrix}\\
&2\\
&&\begin{bmatrix}
{\color{lightgreen}1}&1\\
&{\color{lightgreen}1}
\end{bmatrix}\\
&&&1\\
&&&&1\\
&&&&&\begin{bmatrix}
{\color{lightblue}0}&1\\
&{\color{lightblue}0}
\end{bmatrix}\\
&&&&&&0
\end{bmatrix}
$$


| $i$ | $\lambda_i$ | n_i | molt. geom. |
| --- | ----------- | --- | ----------- |
| 1   | 2           | 4   | 2           |
| 2   | 1           | 4   | 3           |
| 3   | 0           | 3   | 2           |
Di conseguenza possiamo calcolare anche il minimal annihilating polinomial:
$\Psi_J(s)=(s-2)^{\color{orange}3}(s-1)^{\color{lightgreen}2}s^{\color{lightblue}2}$


#### Esempio 4
Trovare la matrice a partire dai dati:


| $i$ | $\lambda_i$ | n_i | molt. geom. |
| --- | ----------- | --- | ----------- |
| 1   | 2           | 3   | 2           |
| 2   | 3           | 2   | 2           |
| 3   | 1           | 4   | 2           |
Per determinare $J_3$ andiamo ad usare 
$\Psi_J(s)=(s-2)^2(s-3)(s-1)^2$  

$$
J=
\begin{bmatrix}
	\begin{bmatrix}
		\begin{bmatrix}
		2&1\\
		&2
		\end{bmatrix}\\
		&2
	\end{bmatrix}\\
	&\begin{bmatrix}
		3&1\\
		&3
	\end{bmatrix}\\
	&&\begin{bmatrix}
	
		\begin{bmatrix}
		1&1\\
		&1
		\end{bmatrix}\\
		&\begin{bmatrix}
		1&1\\
		&1
		\end{bmatrix}\\
	\end{bmatrix}\\
	
\end{bmatrix}
$$

La potenza di una matrice in Jordan form dato che $J$ è diagonale a blocchi è pari a:
$$
J^t=
\begin{bmatrix}
\begin{bmatrix}
J_1^t
\end{bmatrix}\\
&\begin{bmatrix}
J_2^t
\end{bmatrix}\\
&&\begin{bmatrix}
J_3^t
\end{bmatrix}
\end{bmatrix}
$$
ma dato che $J_i$ è diagonale a blocchi posso anche dire che:

$$
J_i^t=
\begin{bmatrix}
\begin{bmatrix}
J_{i1}^t
\end{bmatrix}\\
&\begin{bmatrix}
J_{i2}^t
\end{bmatrix}\\
&&\begin{bmatrix}
J_{i3}^t
\end{bmatrix}
\end{bmatrix}
$$
quindi posso calcolare $J^t$ se conosco l'espressione di  $J_{ik}^t$ per un mini-block generico di $J$ 

## Power of a Jordan mini-block
#ST-L3
Tramite gli esempi precedenti possiamo dire che:
- il numero di $\lambda_i$ presenti nella matrice ci da la sua molteplicità algebrica
- il numero di mini-block relativi allo stesso $\lambda_i$ ci da la sua molteplicità geometrica
- la dimensione del primo mini-block ($n_{i1}$) è pari all'esponente relativo allo stesso $\lambda_i$ in $\Psi_J(s)$

Ora consideriamo di avere un mini-block $J$  di grandezza $\nu$ con un qualche autovalore complesso
$$
J_\lambda=\begin{bmatrix}
\lambda&1\\
&\lambda&1\\
&&\ddots&\ddots\\
&&&\lambda&1
\end{bmatrix}
$$
### Caso $\lambda=0$ 
$$
J_0=\begin{bmatrix}
0&1\\
&0&1\\
&&\ddots&\ddots\\
&&&0&1
\end{bmatrix}
$$
Le varie potenze saranno:
$$
\begin{align}
J_0^0&=I   &J_o^1&=J_0 \\
J_0^2&=\begin{bmatrix}
0&0&1\\
&0&0&1\\
&&\ddots&\ddots&\ddots\\
&&&0&0&1
\end{bmatrix}
&J_0^\nu&=\begin{bmatrix}
0&0&0&\cdots&0&1\\
&0&0&0&\cdots&0\\
&&\ddots&\ddots&\ddots&\vdots\\
&&&0&0&0
\end{bmatrix}
\end{align}
$$

Si può rappresentare $J^t$ in maniera compatta tramite segnali discreti( $\delta(t)$ )
	Si usa $\delta(t)$ perchè vale 1 solo quando $t=0$
$$
J_\lambda^t=\begin{bmatrix}
\delta(t)&\delta(t-1)&\delta(t-2)&\delta(t-\nu+1)\\
&\delta(t)&\ddots&\delta(t-2)\\
&&\ddots&\delta(t-1)\\
&&&\delta(t)\\
\end{bmatrix}
$$
$\delta(t),\delta(t-1),...,\delta(t-\nu+1)$ sono le *elementary modes* associate al mini-block $J_k$

### Caso $\lambda\neq0$ 
$$
J_\lambda=\begin{bmatrix}
\lambda&1\\
&\lambda&1\\
&&\ddots&\ddots\\
&&&\lambda&1
\end{bmatrix}=\lambda I_\nu+J_0\quad\text{(non importa il verso della moltiplicazione in questo caso)}
$$
 **Newton's binomial formula**
 $\displaystyle(a+b)^t=\sum_{i=0}^t\binom{t}{i}a^{t-i}b^i$  dove $\displaystyle\binom{t}{i}=\frac{n!}{k!(n-k)!}$ 

Possiamo usare questa formula in questo caso per calcolare $J_\lambda^t$ perche se considero
$$
\begin{align}
&(\lambda I_\nu)J_0=J_0(\lambda I_\nu)\\
\Rightarrow J_\lambda^t&=(\lambda I+J_0)^t=\sum_{i=0}^t\binom{t}{i}(\lambda I)^{t-i}J_o^i\\
&=\lambda^tI+\binom{t}{1}\lambda^{t-1}J_0+\binom{t}{2}\lambda^{t-2}J_0^2\dots+\binom{t}{\nu}\lambda^{t-\nu+1}J_0^\nu\\\\\\
&J_\lambda^t==
\begin{bmatrix}
\lambda^t&\binom{t}{1}\lambda^{t-1}&\binom{t}{2}\lambda^{t-2}&\binom{t}{\nu-1}\lambda^{t-\nu+1}\\
&\lambda^t&\ddots&\binom{t}{2}\lambda^{t-2}\\
&&\ddots&\binom{t}{1}\lambda^{t-1}\\
&&&\lambda^t\\
\end{bmatrix}
\end{align}
$$
$\lambda^t,\binom{t}{1}\lambda^{t-1},\binom{t}{2}\lambda^{t-2},\binom{t}{\nu-1}\lambda^{t-\nu+1}$ sono le *elementary modes* associate a $\lambda$.
Sono presenti $\nu$ *dinstinct elementary modes* associate a $\lambda$ 


Guardando al generico $J$ block è chiaro che il numero di *elementary modes* distinte associate coicide con la dimensione del mini-block più grande associato a $\lambda_i$ dato che e quindi sono:
$n_{i1}$ che corrisponde anche alla molteplicità di $\lambda_i$ in $\Psi_J(s)$.

Il numero di elementary modes distinte associate a tutti gli autovalori di $J$ è: $n_{11}+n_{21}+...+n_{r1}=deg(\Psi_J)$ 

#### Esempio 
$$
J=
\begin{bmatrix}
{\color{orange}\begin{bmatrix}
2&1\\
&2
\end{bmatrix}}\\
&2\\
&&2\\
&&&{\color{lightgreen}\begin{bmatrix}
1&1\\
&1&1\\
&&1
\end{bmatrix}}\\
&&&&\color{lightblue}0
\end{bmatrix}
$$
le elementary modes saranno:
- ${\color{orange} 2^t},{\color{orange}\binom{t}{1}2^{t-1}}$ 
- ${\color{lightgreen}1^t},{\color{lightgreen}\binom{t}{1}1^{t-1}},\color{lightgreen}\binom{t}{2}1^{t-2}$
- $\color{lightblue}\delta(t)$ 
### Preposition
Per ogni $f\in \mathbb{C^{n\times n}}$ in particolare $F\in \mathbb{R}^{n\times n}$ esiste $T\in \mathbb{R}^{n\times n}$  *non singular* tale che $T^{-1}F\ T=J$ e $F= T\ J\ T^{-1}$.

$F^t=(T\ J\ \cancel{T^{-1}})(\cancel{T}\ J\ \cancel{T^{-1}})...(\cancel{T}\ J\ T^{-1}) = T\ J^t\ T^{-1}$ 
Questo implica che le entries di $F^t$ sono combinazioni lineari delle elementary modes di $J$.
Questo implica che tutte le elementary modes associate a $J$ compaiono in $F^t$ e nessun altra quindo possiamo anche chiamarle elementary modes di $F^t$
NOTA: $\Psi_J(s)=\Psi_F(s)$ perchè sono matrici simili