#ST-L23-5 
### Definiton
Dato un DT n-dimensional system $\Sigma=(F,G,H)$ diciamo che $\Sigma$ è *finite memory* se
$\exists \bar k\in \mathbb Z, \bar k>0$ s.t. $\forall x_0\in X$ il corrispondente unforced state evolution $x_l(t)$ è identico a zero da $t=\bar k$ in poi.

Questo significa che  $\Sigma$ perde la memoria delle condizioni iniziali e quindi: $\forall t\ge\bar k\qquad x(t)=x_f(t)$ 

$$
\begin{align}
\Sigma \text{ is finite memory}\ \ &\overset{\Large x_l(t)=F^tx_0}{\iff}\\
&\ \ \ \ \ \iff\forall x_0\in X\quad F^tx_0=\underline 0\forall t\ge\bar k\\
&\ \ \ \ \ \iff\forall x_0\in X\quad F^\bar kx_0=\underline 0\\
&\ \ \ \ \ \iff F^\bar k=0_{n\times n}\\
&\ \ \ \ \ \iff\underbrace{\exists\bar k\in \mathbb Z\ \bar k>0\ s.t. F^\bar k=0_{n\times n}}_{\Large \text{nilpotent}}
\end{align}
$$
[[Nilpotent matrix]]
