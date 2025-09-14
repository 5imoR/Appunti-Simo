[[Prodotti scalari]] 
- $v$ e $w$ si dicono ortogonali se $v\cdot w=0$ (sono perpendicolari tra loro)
- $v$ è normalizzato se $||v|| = 1$ (versore)
- $v \neq \vec 0$ vettore qualsiasi allora $\frac{v}{||v||} = \hat v$ è un vettore di $norma = 1$ (versore)

#### Calcolo proiezione ortogonale
![[proiezione_ortogonale|200]]
$w'$ è la proiezione ortogonale di $w$ 
![[proiezione_ortogonale2|200]]
$$
\begin{align}
&w'\in U \Rightarrow w' = \lambda u,\quad \lambda?\\
&w= w'+v\\
&\qquad\Downarrow\\
&v=w-w'\\
&v\cdot w' = 0\Rightarrow(w-w')\cdot w'=0\\
&(w-\lambda u')\cdot u=0\\
&\lambda = \frac{u\cdot w}{u\cdot u}\\
&w'=\frac{u\cdot w}{u\cdot u}u

\end{align}
$$
## Sottospazio ortogonale
Un vettore $v\in U^\perp$ (è perpendicolare a tutti i vettori di U) se e solo se è perpendicoale ai vettori della base
$$
U\cap U^\perp=\vec 0
$$
#### Teorema 
- Sia $U^\perp \subset \mathbb{R}^n$ un sottospazio di dimensione $r$ 
- $U \subset \mathbb{R}^n$ 
- $U$ ha una base $\{u_1,u_2,...u_r\}$
Allora $dim(U^\perp)=n-r$ 
ovvero $dim(U)+dim(U^\perp)=n$

### Matrici di Proiezione
- $U\subset \mathbb{R}^n$ 
- $f:\mathbb{R}^n\rightarrow\mathbb{R}^n$ 
- $v\rightarrow v'$ con $v'$ proiezione ortogonale di v sul sottospazio $U$ 
- $v' \in U\qquad v'' \in U^\perp\qquad v=v'+v''$ 
![[proiezione_ortogonale3|250]]
$$
\begin{align}
&A=
\begin{bmatrix}
\vdots &\vdots &\cdots &\vdots \\
u_1 & u_2 & \cdots & u_n\\
\vdots &\vdots &\cdots &\vdots \\
\end{bmatrix}\\\\
&v'\in U \qquad v'= x_1u_1+...x_nu_n\\\\
&A\cdot
\begin{bmatrix}
x_1 \\ x_2 \\ \vdots \\ x_n\\
\end{bmatrix} =A\cdot X= v'\\
\end{align}
$$
Quindi $v''=v-v'=v-AX$ 
Il prodotto scalare di due vettori è $u\cdot w = u^T w$ 
$A^T v''=0$ perchè ortogonali
$$
A=
\begin{bmatrix}
\cdots&u_1&\cdots \\
\cdots&u_2&\cdots \\
\cdots&\vdots&\cdots\\ 
\cdots&u_n&\cdots\\
\end{bmatrix}
$$
- $A^T(v-AX)=0\qquad (A^TA)X=A^Tv$ 
- $X=(A^TA)^{-1}A^Tv$ 
- $v'=AX=[A(A^TA)^{-1}A^T]v = Pv$
$P$ è la matrice di proiezione sul sottospazio U


## Basi ortogonali
Sia $U=<u_1,u_2,u_3>$ una base ortogonale di $U=<u_1',u_2',u_3'>$ è una base in cui i vettori sono ortogonali tra loro a due a due $u_i'\cdot u_j'=0$ 
Una base si dice ortonormale se i vettori sono normalizzati (norma 1)

### Procedimento di Gram Schmidt
Procedimento per trasformare una base qualunque in una base ortogonale/ortonormale
#### Come si ottiene
$$
\begin{align}
&u_1' = u_1
\\\\
&u_2'=u_2+\alpha_1u_1' & u_2'\cdot u_1'=0\\
&(u_2+\alpha_1u_1')u_1'=0 & \alpha_1=-\frac{u_2u_1'}{u_1'u_1'}\\
\end{align}
$$$$
\begin{align}
&u_3'=u_3+\alpha_1u_1'+\alpha_2u_2' \\
&\begin{cases}
u_3'\cdot u_1'=0\\
u_3'\cdot u_2'=0\\
\end{cases}
\quad
\begin{cases}
(u_3+\alpha_1u_1'+\alpha_2u_2')\cdot u_1'=0\\
(u_3+\alpha_1u_1'+\alpha_2u_2')\cdot u_2'=0\\
\end{cases}
\quad
\begin{cases}
\displaystyle\alpha_1=-\frac{u_3u_1'}{u_1'u_1'}\\
\displaystyle\alpha_2=-\frac{u_3u_1'}{u_2'u_2'}
\end{cases}\\
&u_3'=u_3-\left(\frac{u_3u_1'}{u_1'u_1'}\right)u_1'-\left(\frac{u_3u_2'}{u_2'u_2'}\right)u_2'

\end{align}
$$
$$
\begin{align}
&u_4'=u_4+\alpha_1u_1'+\alpha_2u_2'+\alpha_3u_3'\\
&u_4'=u_4-\left(\frac{u_4u_1'}{u_1'u_1'}\right)u_1'-\left(\frac{u_4u_2'}{u_2'u_2'}\right)u_2'-\left(\frac{u_4u_3'}{u_3'u_3'}\right)u_3'
\end{align}
$$

#### Formula generale
$$
u_r'=u_r
-\left(\frac{u_ru_1'}{u_1'u_1'}\right)u_1'
-\left(\frac{u_ru_2'}{u_2'u_2'}\right)u_2'
-\ldots
-\left(\frac{u_ru_{r-1}'}{u_{r-1}'u_{r-1}'}\right)u_{r-1}'
$$
$u_1',...u_r'$ sono una base ortogonale 

$\displaystyle u_i''=\frac{u_i'}{||u_i'||}$
$u_1''... u_r''$ sono una base ortonormale