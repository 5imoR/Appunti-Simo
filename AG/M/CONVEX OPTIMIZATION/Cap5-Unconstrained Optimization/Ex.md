#CO-L17-4
### Ex1
$\min f(x)=\frac 12 x^TPx+q^Tx+r$
$P\in S^n$ è simmetrica
- se $P\nsucceq 0$ (non PSD) $\Rightarrow$ unbounded 
	- $\exists v: v^TPv<0$
	- $x=tv$
	$\frac 12 t^2\underbrace{v^TPv}_\text{<0}+q^Tx+r$ 
	allora si tratta di una parabola $\cap$ e quindi dovendo cercare il minimo siamo nel caso unbounded

- se $P\succeq 0$ se $Px=-q$ non ha una soluzione $\Rightarrow$ unbounded 
	$q\notin Im(P) \qquad q=\tilde q+v$
	con 
	- $\tilde q\in Im(P)$ 
	- $v\in\ker(P)\to Pv=0\to v^TPv=0$ 
	- $x=tv$
	$$\begin{align}
	\frac 12 t^2\underbrace{v^TPv}_\text{=0}+q^Tx+r&=t(\tilde q+v)v+r\\
	&=t\underbrace{v^Tv}_{=||v||^2>0}+r
	\end{align}$$
	$\tilde q$ scompare perchè lo moltiplichiamo per $v$ quindi $Im\cdot \ker$ 
	ma quello che abbiamo trovato è una funzione lineare e quindi è unpounded
	

### Ex2
$\min 2(x-3)^2+(y-2)^2$
- $x^{(0)}=(0,0)$ 
- $\alpha=0.01$
- $\beta=0.5$ 
- $t=1$
Calcolare $x^{(1)}$ 
$$
\begin{align}
&\nabla f(x)|_{(0,0)}=
\begin{bmatrix}4(x-3) \\2(y-2) \\\end{bmatrix}
=
\begin{bmatrix}-12 \\-4 \\\end{bmatrix}
\qquad\qquad \Delta x=-\nabla f(x)=
\begin{bmatrix}12 \\4 \\\end{bmatrix}\\\\
&\alpha\nabla f(x)^T\Delta x=1.6\\
&t=1\ \ \ \quad f(x+\Delta x)=f(12,4) =166\qquad(22-166\not>1.6)\\
&t=0.5\quad f(x+\Delta x)=f(6,\ \ 2) = 18\qquad\ \  (22-18>1.6)\\
x^{(1)}=(6,2)
\end{align}
$$
