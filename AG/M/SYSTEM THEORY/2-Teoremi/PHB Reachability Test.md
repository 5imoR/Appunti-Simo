---
tags:
  - "#ST-L14"
---
## Theorem
Dato un paio$(F,G)$ con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$ 
1. Il paio $(F,G)$ è reachable $\iff rank[z-In-F|G]=n\quad \cancel{\forall z\in \mathbb C}\rightarrow \forall z\in\sigma(F)$ 
	![[PHB Reachability Test#Remark a]]
	Questo remark ci permette di dover testare questa condizione solo per $\forall z\in\sigma(F)$ 
2. Il paio non è reachable $\Rightarrow rank[\lambda In-F|G]<n\iff \lambda\in \sigma(F_{22})$
	Dove $F_{22}$ è la matrice del non reachable subsystem nella [[Standard Reachability Form]] associata al paio $(F,G)$

Questo criterio torna utile dato che ci permette di identificare $\sigma(F_{22})$ senza dover calcolare la SRF
## Corollary
Sia $(F,G)$ $F\in\mathbb R^{n\times n}\quad G\in \mathbb R^{n\times m}$ Assumendo che $F$ sia in
![[R3 Jordan Form#Jordan Form]]
Allo stesso modo 
$$
G=\begin{bmatrix}
G_1\\
\vdots\\
G_r
\end{bmatrix}
\qquad G_i=\begin{bmatrix}
G_{i1}\\
\vdots\\
G_is_i
\end{bmatrix}
$$
Dove 
- $G_1$ ha $n_1$ righe
- $G_r$ ha $n_r$ righe
- $G_{i1}$ ha $n_i1$ righe
- $G_{n_is_i}$ ha $n_is_i$ righe
$(F,G)\text{ reachable}\iff \forall i\in \set{1\dots r}$  la famiglia dell'ultima riga dei blocchi $G_{i1}...$ sono linearmente indipendenti
### Esempio
$$
F=J=\begin{bmatrix}
\begin{bmatrix}
\begin{bmatrix}
{2}&1\\
&{2}&1\\
&&{2}\\
\end{bmatrix}\\
&2\\&&2\\
\end{bmatrix}\\
&\begin{bmatrix}
	
		\begin{bmatrix}
		1&1\\
		&1
		\end{bmatrix}\\
		&\begin{bmatrix}
		1&1\\
		&1
		\end{bmatrix}\\
	\end{bmatrix}
\end{bmatrix}
G=\begin{bmatrix}
g_1\\g_2\\g_3\\g_4\\g_5\\g_6\\g_7\\g_8\\g_9
\end{bmatrix}
$$

| $i$ | $\lambda_i$ | $n_i$ | $s_i$ | $n_i1$ |
| --- | ----------- | ----- | ----- | ------ |
| 1   | 2           | 5     | 3     | 3      |
| 2   | 1           | 5     | 2     | 2      |

Vogliamo capire sotto quali condizioni di $G$ otteniamo che il paio $(F,G)=(J,G)$ è raggiungibile usando [[PHB Reachability Test]] 
	Per  $(1)$  possiamo dire che  basta guardare il rango dei blocchi degli autovalori
Controlliamo il rank della *PBH Reachability Matrix* solo per $z=\lambda_1$ e $z=\lambda_2$ 

Assumiamo $z=\lambda_1=2$ 
	è tutta un'unica matrice, ne ho usate 2 solo per semplicità
$$
[F-2I|G]\begin{bmatrix}
\begin{bmatrix}
\begin{bmatrix}
{0}&1\\
&{0}&1\\
&&\color{orange}{0}\\
\end{bmatrix}\\
&\color{orange}0\\&&\color{orange}0\\
\end{bmatrix}\\
&\begin{bmatrix}
	
		\begin{bmatrix}
		-1&1\\
		&-1
		\end{bmatrix}\\
		&\begin{bmatrix}
		-1&1\\
		&-1
		\end{bmatrix}\\
	\end{bmatrix}
\end{bmatrix}
\begin{bmatrix}
g_1\\g_2\\\color{orange}g_3\\\color{orange}g_4\\\color{orange}g_5\\g_6\\g_7\\g_8\\g_9
\end{bmatrix}
$$
$\textcolor{orange}{■}$ sono le righe linearmente dipendenti, quindi per avere la matrice con rango $n$ serve che $g_3,g_4,g_5$ siano indipendenti tra loro
Assumiamo $z=\lambda_2=1$ 
$$[F-1I|G]\begin{bmatrix}
\begin{bmatrix}
\begin{bmatrix}
1&1\\
&1&1\\
&&1\\
\end{bmatrix}\\
&1\\&&1\\
\end{bmatrix}\\
&\begin{bmatrix}
	
		\begin{bmatrix}
		0&1\\
		&\color{lightgreen}0
		\end{bmatrix}\\
		&\begin{bmatrix}
		0&1\\
		&\color{lightgreen}0
		\end{bmatrix}\\
	\end{bmatrix}
\end{bmatrix}
\begin{bmatrix}
g_1\\g_2\\g_3\\g_4\\g_5\\g_6\\\color{lightgreen}g_7\\g_8\\\color{lightgreen}g_9
\end{bmatrix}$$
$\textcolor{lightgreen}{■}$ sono le righe linearmente dipendenti, quindi per avere la matrice con rango $n$ serve che $g_7,g_9$ siano indipendenti tra loro

non serve che siano tutti e 5 linearmente indipendenti, basta che lo siano rispettivamente al loro "gruppo"
## Proof
1 $\Rightarrow$ Per counter positive    (per provare $A\Rightarrow B$ proviamo $\bar B\Rightarrow \bar A$ )
	Assumiamo che $\exists \lambda \in \mathbb C$ s.t. $rank [\lambda In-F|G]<n$
	Le linee di $[\lambda In-F|G]$ sono linearmente indipendenti e quindi $\exists \underline v\neq \underline 0$ s.t. 
	$$
	\begin{align}
	\underline v^T[\lambda In-F|G]=[0_n^T|0_m^T]\iff&
	\begin{cases}
	\color{orange}\underline v^TF=\lambda \underline v^T\\
	\color{lightgreen}\underline v^TG = 0^T
	\end{cases}\\
	\end{align}
	$$
	$\Rightarrow$  ${\color{orange}\underline v^TF}G=\lambda\color{lightgreen}\underline v^TG$ 
	$\Rightarrow$  $\underline v^TF^2G={\color{orange}\underline v^TF}(FG)=\lambda {\color{orange}\underline v^TF}G=\color{lightgreen}\underline0^T$
	$\vdots$  
	$\Rightarrow$  $\underline v^TF^{n-1}G=\underline 0^T$ 
	$\Rightarrow$  $\underline v^T[G|FG|\dots|F^{n-1}G]=[0_n^T|0_m^T]$
	$\Rightarrow$  $\underline v^T\mathcal R =\underline 0^T \Rightarrow rank\mathcal R<n$
	$\Rightarrow$ $(F,G)$ non è reachable

1 $\Leftarrow$ Per counter positive
	Assumiamo che $(F,G)$ non è reachable e proviamo che *PBH reachability matrix*  perde rank per alcuni punti in $\mathbb C$.
	Se$(F,G)$ non è raggiungibile alebricamente equivalente ad un paio $(\bar F,\bar G)$ in ![[Standard Reachability Form#Riassunto]] mentre per![[PHB Reachability Test#Remark b]] Se $z=\lambda\in\sigma(F_{22})$ allora
	le righe di $[zIn-\bar F|\bar G]$ sono linearmente dipendenti
	e di conseguenza lo sono anche quelle di: $[0\ \ zI_{n-\rho}-F_{22}\ \ 0]$ 
	quindi $rank [\lambda I-F|G]<n$ 
2 $\Leftarrow$ 
	Questo è già provato da 1$\Leftarrow$ 
2 $\Rightarrow$
	Assumiamo che il paio $(F,G)$ non sia reachable e quindi esiste $(\bar F,\bar G)$  allora
	$rank [\lambda In-F|G]=rank[\lambda I-\bar F|\bar G]<n$ 
	Vogliamo provare  $\lambda \in \sigma(F_ {22})$  per alcuni valori  $\lambda\in \mathbb C$ 
	Come il rango della matrice:$\begin{bmatrix}zI_\rho-F_{11}&-F_{12}&G_1\\0 &zI_{n-\rho}-F_{22} &0\end{bmatrix}<n$
	allora:
	$\exists \underline v^T=[\overbrace{v_1^T}^\rho |\overbrace{v_2^T}^{n-\rho}]\neq [0^T|0^T]$  s.t.
	  $[{v_1^T} |{v_2^T}]\begin{bmatrix}zI_\rho-F_{11}&G_1\\0 &0\end{bmatrix}=[0^T|0^T]$ $\Rightarrow$ $v_1^T\begin{bmatrix}zI_\rho-F_{11}&G_1\end{bmatrix}=[0^T|0^T]\Rightarrow v_1=\underline 0$   
	  $[\cancel{v_1^T}_{=0} |{v_2^T}]\begin{bmatrix}-F_{12}\\ zI_{n-\rho}-F_{22} \end{bmatrix}=0^T$ $\Rightarrow v_2^T[ zI_{n-\rho}-F_{22}]$ 
	  dato che $v_2^T$ non  può essere $0$ vuol dire che $zI_{n-\rho}-F_{22}$ è non singular e quindi $\lambda\in\sigma(F_{22})$









## Remarks

### Remark a
$\forall z\notin\sigma(F)$  abbiamo che $zI_n-F$ è non singular square e quindi $zI_n-F|G$ ha rango $n$

### Remark b
Supponiamo che $(\bar F,\bar G)$ è [[R7 Basis of vector spaces and algebraically equivalent system|algebricamente equivalente]] a $(F,G)$ che significa che $\exists T$ non singular square s.t. $(\bar F,\bar G)=(T^{-1}FT,T^{-1}G)$  allora:
$[zIn-\bar F|\bar G]=[zT^{-1}InT-T^{-1}FT|T^{-1}G]=T^{-1}[zIn-F|G]\begin{bmatrix}T & 0 \\0 & Im \\\end{bmatrix}$ 
$\Rightarrow \forall z\in \mathbb C\qquad rank[zIn-\bar F|\bar G]=rank[zIn-F|G]=\begin{bmatrix}zI_\rho-F_{11}&-F_{12}&G_1\\0 &zI_{n-\rho}-F_{22} &0\end{bmatrix}$ 
