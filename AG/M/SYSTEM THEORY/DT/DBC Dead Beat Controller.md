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
