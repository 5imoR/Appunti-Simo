#ML-L7
#### Riassunto
$$\begin{align}
A=USV^T=U_1S_1V^T_1
\end{align}
$$
## The Singular Value Decomposition SVD
**MATRICI $A=\mathbb R^{n\times m}$**
$$
\forall A \in \mathbb R^{n\times m}\quad \exists\quad U\in\mathbb R^{n\times n}
\quad V\in\mathbb R^{m\times m}
\quad S\in\mathbb R^{n\times m}
$$
Dove:
$$
U^TU=UU^T=Im\qquad
V^TV=VV^T=Im
$$
Quindi le colonne di $U$ sono ortonormali(righe di $U^T$ ortonormali)
$$
S=\begin{bmatrix}
\sigma_1&&0\\
&\ddots&&&0&\\
0&&\sigma_k\\
&&&0\\
&0&&&0
\end{bmatrix}
$$
	La matrice formata dalle prime $k$ righe e colonne è diagonale metre il resto è tutto a $0$.
$\sigma_1\geq \sigma_2\geq\dots\geq\sigma_k$ 

$k=rank(A)$  tale che: $$A=USV^T$$ Possiamo dire che:
$$
\begin{align}
U=[\overbrace{U_1}^k\vdots \overbrace{U_1^\perp}^{n-k}]\qquad
V=[\overbrace{V_1}^k\vdots \overbrace{V_1^\perp}^{m-k}]\qquad
S=\begin{bmatrix}S_1&0\\0&0\end{bmatrix} S_1=\begin{bmatrix}\sigma_1&0\\0&\sigma_k\end{bmatrix}
\end{align}
$$
Le colonne di $U_1$ sono ortonormali ma le righe di$U_1^T$  non lo sono più ( $U_1U_1^T\neq Im$ )

#### Interpretazione geometrica
Data una matrice $A\in \mathbb R^{n\times m}$
$A$ può essere vista come la matrice che rappresenta una trasformazione lineare
$$
\begin{align}
L(A):&\mathbb R^m\longrightarrow\mathbb R^n\\
&\ \ \ \, v\longrightarrow u=Av
\end{align}
$$

Qual'è la direzione in $\mathbb R ^m$ lungo la quale la nostra trasformazione lineare($L(A)$ ) da l'amplificazione massima?
$\sup_{v\in\mathbb R^m}||Av||=\sigma_1$ 

#ML-L8
$\arg \max _{\substack{v\in\mathbb R^m\\||v||=1}}||Av||\subseteq\arg\max_{v\in\mathbb R^m}\frac{||Av||}{||v||}$ 
	usiamo la norma di v perchè noi interessa solo la direzione non il modulo 

- $v_1=\arg \max _{\substack{v\in\mathbb R^m\\||v||=1}}||Av||$ se da più di un massimo vanno bene entrambi
- $u_1=\frac{Av_1}{||Av_1||}$
- $\theta_1=||Av_1||$ 
$v_1\perp v_2\dots$ allora $\theta_1\geq \theta_2$ 
	questo perchè $v_1$ e $v_2$ fanno parte dello stesso set e $v_1$ dava il massimo
Allo stesso modo di $v_1$ ci si trovano tutti gli altri $k$ vettori che formano $V_1$.
L'ultimo valore, $v_k>0$ 

##### Remark
$$
\begin{cases}
u_1\theta_1=Av_1\\
u_2\theta_2=Av_2\\
\vdots\\
u_k\theta_k=Av_k\\
\end{cases}
\longrightarrow
\big[u_1\theta_1|u_2\theta_2|\dots|u_k\theta_k\big] =\big[Av_1|Av_2|\dots|Av_k\big]
\qquad V_1=m\Big\{ \underbrace{\Big[\ \vdots\ \vdots\ \vdots\ \Big]}_k
$$

Rendiamo $V=[V_1V_1^\perp]$  dove $V_1^\perp$ è il kernel
$$
\begin{align}
[U_1S_1\vdots 0]&=A[V_1V_1^\perp]\\
[U_1S_1\vdots 0]V^T&=A\cancel{VV^T}\\
[U_1U_1^\perp]\begin{bmatrix}S&0\\0&0\end{bmatrix}=U_1[S_1\vdots0]V^T&=A\\
USV^T=U_1S_1V^T_1&=A\\
\end{align}
$$
- $u_1\dots u_k$ left singular vector
- $v_1\dots v_k$ right singular vector
- $\sigma_1\dots \sigma_k$ singular vector
- $V_1^\perp$ sono il kernel di $A$
- $U_1$ sono l'immagine di $A$

Non abbiamo provato che $U^T_1U_1=I_k$ ma potremmo(non l'ha fatto) 

