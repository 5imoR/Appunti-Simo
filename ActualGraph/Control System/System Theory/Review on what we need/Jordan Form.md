#ST-L2 
# Jordan Form
Una matrice $J\in \mathbb{C}^{n\times n}$  è detta in *Jordan form* se dopo permutazioni di righe e colonne può essere scritta nel seguente modo:

| $J=\begin{bmatrix}[J_1]&0&\cdots& 0\\0&[J_2]&\cdots& 0\\\vdots&\vdots&\ddots&\vdots&\\0&0&\cdots&[J_n]\end{bmatrix}$              | $\Large J_i\in \mathbb{C}^{n_i\times n_i}$<br>$J_i$: jordan mini-block<br>$\lambda_i\in\mathbb{C}\quad \lambda_i\neq\lambda_j$ |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| $J_i=\begin{bmatrix}[J_{i1}]&0&\cdots& 0\\0&[J_{i2}]&\cdots& 0\\\vdots&\vdots&\ddots&\vdots&\\0&0&\cdots&[J_{is_i}]\end{bmatrix}$ | $\Large J_{ik}\in \mathbb{C}^{n_{ik}\times n_{ik}}$<br>$J_{ik}$: jordan mini-block                                             |
| $J_{\lambda}=\begin{bmatrix}\lambda_i&1&\cdots& 0\\0&\lambda_i&\ddots& 0\\\vdots&\vdots&\ddots&1&\\0&0&0&\lambda_i\end{bmatrix}$  | La diagonale sopra la diagonale ha tutti 1<br>$n_{i1}\geq n_{i2}\geq ...\geq n_is_i$                                           |
Sappiamo che:
- $s_i$ è la molteplicità geometrica di $\lambda_i$
- $n_i$ è la moteplicità algebrica di $\lambda_i$
- $n_{i1}$ è il grado di $\Psi_J(s)$ (non cambia nulla tra $s$ o $z$ )

# Esempi

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
