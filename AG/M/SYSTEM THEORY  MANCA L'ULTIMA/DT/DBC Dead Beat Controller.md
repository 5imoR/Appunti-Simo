#ST-L24-1 
### Definition \[Dead Beat Controller]
Dato un n-dimensional DT model con $m$ input $\Sigma=(F,G,H)$ (equivalentemente un paio $(F,G)$) diciamo che  $\Sigma$ ammette un DBC se $\exists K\in\mathbb R^{m\times n}$ s.t. $\Sigma_K=(F+GK,G,H)$ è [[Finite Memory System|finite memory]](equivalentemente $F+GK$ è [[Nilpotent matrix|nilpotent]]). 

### Remark
$$
\begin{align}
F\begin{array}{c}  \text{ asympt.}\\\text{ stable}  \end{array}\iff
\Sigma\begin{array}{c}  \text{ asympt.}\\\text{ stable}  \end{array}
\quad\neq\quad
\begin{array}{c}  \Sigma\text{ is stabilizable i.e. }\\ \exists K\in\mathbb R^{m\times n}\ s.t.\ \Sigma_k\text{ asympt. stable}  \end{array}\iff
\begin{array}{c}\exists K\in \mathbb R^{m\times n}\ \ s.t.\\
F+GK\begin{array}{c}  \text{ asympt.}\\\text{ stable}  \end{array}
\end{array}
\end{align}$$

$$
\begin{align}
F \text{ nilpotent}\iff
\Sigma\begin{array}{c}  \text{ finite }\\\text{ memory}  \end{array}
\quad\neq\quad
\begin{array}{c}  \Sigma\text{ admits DBC i.e. }\\ \exists K\in\mathbb R^{m\times n}\ s.t.\ \Sigma_k\text{ finite memory}  \end{array}\iff
\begin{array}{c}\exists K\in \mathbb R^{m\times n}\ \ s.t.\\
F+GK\text{ nilpotent}
\end{array}\\
\end{align}
$$
###
![[Existence of DBC#Theorem [Existence of DBC]]

Se  un paio ammette DBC qual'è il valore minimo che il nilpotency index di $F+GK$ può avere con $k$ che varia tra un DBC e l'altro?
Dal teorema precente possiamo distinguere 2 casi:
- $(F,G)$ reachable
- $(F,G)$ non reachable ma $F_{22}$ è nilpotent

#### Caso 1
$(F,G)$ reachable e  $\exists k\in\mathbb R^{m\times n}$ s.t. $F+GK$ sia [[Nilpotent matrix|nilpotent]].
Il nilpotency index di  $F+GK\equiv \deg \Psi_{F+GK}(z)=\deg\Psi_1(z)$ 

Per la parte di analisi di [[Rosenbrock's Theorem#Analysis|Rosenbrock's Theorem]] 
$\Rightarrow$  $\deg\Psi_1(z)\ge k_1$ primo control invariant di $F,G)$ 
Ora proviamo che il *bound* è stretto ovvero che posso trovare $k$ s.t. $F+GK$ è nilpotent con nilpotency index di $k_1$. Usando il  [[Rosenbrock's Theorem#Case 2) $(c=q) wedge( deg p_i=k_i quad i=1 dots c_{=q})$|secondo caso limite della parte di sintesi]] posso dire che  se $k_1\ge k_2\ge\dots\ge k_q$  sono i control invariants di $(F,G)$ allora $\exists K$ s.t. $F+GK$ ha gli invariant polinomials:
$$
\begin{cases}
\Psi_1(z)=z^{k_1}\\
\ \ \ \vdots\\
\Psi_q(z)=z^q
\end{cases}
\Rightarrow\deg\Psi_1=\deg\Psi_{F+GK}=k_1\quad \Rightarrow F+GK \text{ è nilpotent con nil. index } k_1
$$
$k_1=r$ (reachability index)

#### Caso 2
w.l.o.g. assumiamo:
![[SRF Standard Reachability Form#Riassunto]]
Settiamo $K=\begin{bmatrix}K_1&K_2\end{bmatrix}\in \mathbb R^{m\times n}$   come DBC per il paio $(F,G)$ 
Questo vuol dire che:
$$
F+GK=\begin{bmatrix}
F_{11}+G_1K_1 & F_{12}+G_1K_2 \\
0 & F_{22}^h \\
\end{bmatrix}\text{ è nilpotent}
$$
Sia $h\in\mathbb Z\ h\ge 1$ il nilpotency index di $F+GK$ :
$$
\begin{align}
&0=(F*GK)^h=\begin{bmatrix}
(F_{11}+G_1K_1)^h & * \\
0 & F_{22} \\
\end{bmatrix}\\
&\Rightarrow
\begin{cases}
(F_{11}+G_1K_1)^h=0\\
F_{22}^h = 0
\end{cases}\\
&\Rightarrow
\begin{array}{c}
h\ge\text{nil. index di } F_{22} \\
F_{11}+G_1K_1\ge \text{reach. index di }(F_{11},G_1)
\end{array}
\end{align}
$$
Proviamo che 
$$
h\ge \max\set{r_{11},h_{22}}
$$
Può essere provato che il bound è stretto ovvero che:
$\exists k\in\mathbb R^{m\times n}$ s.t. $F+GK$ è nilpotent con $\max\set{r_{11},h_{22}}$ come nilpotency index.
## Ex
Considera il sistema DT
$$x(t+1)=Fx(t)+Gu(t)=
\begin{bmatrix}
0 & 0 & 0 \\
1 & 1 & 0 \\
2 & -1 & 1 \\
\end{bmatrix}x(t)+
\begin{bmatrix}
0 & 0 \\
1 & 1 \\
0 & 1 \\
\end{bmatrix}u(t)
$$
- Design, se possibile, un DBC  che utilizzi solamente il primo input.
- Design, se possibile, un DBC che usi entrambi gli input e minimizzi il nilpotency index della $F+GK$ risultante
Il sistema non è reachable per il primo o entrambi gli input.
Vediamolo in una forma rovesciata della SRF
$$
F=
\begin{bmatrix}
[0] & 0\quad\ \ \ 0 \\
\begin{array}{c}1 \\2\end{array}&\begin{bmatrix}
1 & 0 \\
-1 & 1 \\
\end{bmatrix}
\end{bmatrix}=
\begin{bmatrix}
\tilde{F_{11}} & \tilde{F_{12}} \\
\tilde{F_{21}} & \tilde{F_{22}} \\
\end{bmatrix}
\qquad g_1=\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
=\begin{bmatrix} 0 \\ \tilde g_2 \end{bmatrix}
$$
$\mathcal R[\tilde{g_{2}}|\tilde{F_{22}}\tilde{g_{2}}]=\begin{bmatrix}1 & 1 \\0 & -1 \\\end{bmatrix}$
$(\tilde{F_{22}},\tilde{g_{2}})$ è reachable
	In questo caso si ha che la matrice $T$ di cambiamento di base, invece di avere le prime righe che formano una base in $X^R$ e le ultime che la rendono invertibile si ha l'opposto.
#ST-L25-1 
La matrice $F_{22}$ del non reachable subsystem coincide con $\tilde{F_{11}}=[0]_{1\times 1}$  allora $\exists$ DBC se settiamo:
$$
k_1=[a\ b\ c]\qquad F_1+g_1k_1=
\begin{bmatrix}
[0] & 0\quad\ \ \ 0 \\
\begin{array}{c}1+a \\2\end{array}&\begin{bmatrix}
1+b & c \\
-1 & 1 \\
\end{bmatrix}
\end{bmatrix}
$$
Serve scegliere i valori di $b,c$ per ottenere il polinomio caratteristico pari a $z^2$ 
$$
\det \begin{bmatrix}
z-1-b & c \\
-1 & z-1 \\
\end{bmatrix}
=(z-1-b)(z-1)+c=z^2+(-2-b)z+(1+b+c)=z^2
$$
$k_1=[a\ -2\ 1]\quad \forall a\in\mathbb R$


Il sistema è sicuramente reachable dato che siamo riusciti ad ottenere questo risultato a partire da un singolo input.
Dato che esiste un DBC quello che ci serve fare è trovare il minimo nilpotency index appartenente ad $F+GK$.
Questo è pari a: ![[Nilpotent matrix#NI X SRF]]
${\text{nil. index di } F_{22}}= 1$
$\text{reach. index di }(F_{11},G_1)=\min\set{k:\mathcal R_k=[\tilde G_2|\tilde F_{22}\tilde G_2|\dots|F_{22}^{k-1}\tilde G_2]}$ per avere rango 2 serve $k=1$ 
Quindi il nilpotency index è pari a $1$ 
$$
\text{se } K=
\begin{bmatrix}
a & b & c \\
d & e & f \\
\end{bmatrix}
\quad F+GK=
\begin{bmatrix}
0 & 0 & 0 \\
1+a+d & 1+b+e & c+f \\
2+d & -1+e & 1+f \\
\end{bmatrix}=\underline 0_{\ 3\times 3}
$$
$$
\Rightarrow K=\begin{bmatrix}
1 & -2 & 1 \\
-2 & 1 & -1 \\
\end{bmatrix}
$$
 