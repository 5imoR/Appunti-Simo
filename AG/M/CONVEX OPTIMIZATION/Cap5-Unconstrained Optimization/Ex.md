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