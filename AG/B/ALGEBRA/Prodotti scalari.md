[[ALGEBRA]][[Determinante]]
$$
V=\mathbb{R}^2\qquad\qquad
v=(a,b)\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad
$$
![[Prodotti_scalari|200]]
$v$ equivale dal vettore che parte dall'origine e raggiunge le cordinate $(a, b)$ la lunghezza è detta norma o modulo di $v$

$|v|,\, ||v|| =\sqrt{a^2+b^2} =$ norma o modulo di $v$

Nel piano tridimensionale si ha:

$||v|| =\sqrt{a^2+b^2+c^2}$ 

### Prodotto scalare di due vettori
$$
v\cdot w=||v||\ ||w||\cos(\alpha)
$$
non importa se l'angolo sia interno o esterno perchè stai usando il coseno
- $v\cdot w= a_1b_1+a_2b_2$  con $v,\ w \in\mathbb{R}^2$
- $v\cdot w= a_1b_1+a_2b_2+a_3b_3$  con $v,\ w \in\mathbb{R}^3$

- $\displaystyle \cos(\alpha)= \frac{v\cdot w}{||v||\ ||w||}$  

$v,\ w\in \mathbb{R}^n$:
- $||v|| = \sqrt{a_1^2+a_2^2+...+a_n^2}$
- $\displaystyle\sum_{i=1}^n{a_ib_i}$ 
- $\displaystyle\cos(\alpha)=\frac{v\cdot w}{||v||\ ||w||}$    se   $\displaystyle-1\leq \frac{v\cdot w}{||v||\ ||w||} \leq 1$   

### Teorema di Cauchy-Schwarz
$|v\cdot w|\leq ||v||\ ||w||$  quindi:
$\displaystyle-1\leq \frac{v\cdot w}{||v||\ ||w||} \leq 1$  è sempre vera  

### Area di un parallelogramma (in $\mathbb{R}^n$)

![[parallelogramma|300]]
$v,\ w \in\mathbb{R}^n\qquad h=||w||\sin(\alpha)$
$$
\begin{align}
Area(P)=& ||v||\cdot ||w||\cdot\sin(\alpha) = ||v|| \cdot h\\
(Area(P))^2&= ||v||^2\cdot ||w||^2\cdot\sin^2(\alpha)\\
&=||v||^2\cdot ||w||^2\cdot(1-\cos^2(\alpha))\\
&= ||v||^2\cdot ||w||^2-(v\cdot w)^2\\
&=(v\cdot v)(w\cdot w)-(v\cdot w)^2\\
&=det
\begin{bmatrix}
v\cdot v & v\cdot w\\
w\cdot v & w\cdot w\\
\end{bmatrix}
\end{align}
$$
#### Se sono presenti 3 vettori
![[Cubo|300]]
$v,\ w,\ u \in\mathbb{R}^n \qquad h=||w||\sin(\alpha)$ 
$$
\begin{align}
&Volume =Area\ di\ base \times h\\
& det 
\begin{bmatrix}
u\cdot u & u\cdot v & u\cdot w\\
v\cdot u & v\cdot v & v\cdot w\\
w\cdot u & w\cdot v & w\cdot w\\
\end{bmatrix}
= Volume^2
\end{align}
$$
