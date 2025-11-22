#ST-L15
### Control Theory
![[controlT|600]]
- $e(t)=r(t)-y(t)$ 
- Process is given
- Reference Signal is given $r(t)$
Goal: realizzare un controller dinamico per rendere $y(t)\simeq r(t)$ per $t\to +\infty$ 

### System Theory
![[systemT]]
Goal: realizzare uno static state feedback in modo tale che gli autovalori (o le elementary modes[[R5 Exponential Matrix|(1)]] [[R4 Power of a Square Matrix and Jordan Form|(2)]]) del controlled system risultante siano come desiderate


Consideriamo ora un  (vale sia per DT che per CT)
![[Linear contiunuous time s.s.m.#Strictly Proper]]

considerando la Static state feedback law:
$$u(t)=v(t)+Kx(t)\qquad K\in \mathbb R^{m\times n}$$
allora il sistema diventa:
$$
\begin {align}
\Sigma_k=
&\begin{cases}
\dot x(t)=Fx(t)+Gv(t)+Gx(t)\\
\quad\ \ \, =(F+G)x(t)+Gv(t)\\
y(t)=Hx(t)
\end{cases}
\end{align}
$$
Si può vedere che con $\Sigma=(F,G,H)$ e $\Sigma_k=(F+GK,G,H)$
- si può passare da $\Sigma$ a $\Sigma_k$ tramite $K$
- si può passare da $\Sigma_k$ a $\Sigma$ tramite $-K$ 
e le dimensioni di $x,u,y$ rimangono invariate

## Cosa viene lasciato invariato dall' feedback
### Proposition 1
Dato un paio $(F,G)$ con:
- $F\in R^{n\times n}$ 
- $G\in R^{n\times m}$ 
- $K\in R^{m\times n}$
per ogni $i\in \mathbb Z\quad i\geq 1$ si ha:
$$Im [G|(F+GK)G|\dots|(F+GK)^{i-1}G]\equiv Im[G|FG|\dots|F^{i-1}G]$$

Questo implica che hanno lo stesso rango e:
$$
((F+GK),G)\text{ è reachable}\iff(F,G)\text{ è reachable}
$$
	Di conseguenza possiamo dire che il feedback non modifica la raggiungibilità

### Proposition 2
Consideriamo un paio $(F,G)$ non raggiungibile con:
- $F\in R^{n\times n}$ 
- $G\in R^{n\times m}$ 
e lo assumiamo in [[SRF Standard Reachability Form#Riassunto|Standard Reachability Form]]  con $(F_{11},G_1)$  raggiungibile
Allora $\forall K\in R^{m\times n}$  il paio $(F+GK,G)$  non è raggiungibile in *Standard Reachability Form* ed ha la stessa matrice $F_{22}$ del sistema originale $(F,G)$
#### Proof
Assumiamo $K=[K_1|K_2]$ 
$$
\begin{align}
F+GK&= 
\begin{bmatrix}
F_{11} & F_{12} \\
0 & F_{22} \\
\end{bmatrix}
+
\begin{bmatrix}
G_1 \\
0\\
\end{bmatrix}
\begin{bmatrix}
K_1 &K_2
\end{bmatrix}\\
&=
\begin{bmatrix}
F_{11} & F_{12} \\
0 & F_{22} \\
\end{bmatrix}
+
\begin{bmatrix}
G_1K_1 & G_1K_2 \\
0 & 0\\
\end{bmatrix}\\
&=
\begin{bmatrix}
F_{11}+G_1K_1 & F_{12}+G_1K_2 \\
0 & F_{22}\\
\end{bmatrix}
\end{align}
$$
Per la [[State Feedback#Proposition 1| Prop 1]] possiamo dire che $(F_{11}+G_1K_1,G_1)$ è reachable
Mentre $F_{22}$ rimane invariato. 
	Se lui da problemi ci costringe a cambiare il controllore
## Riassunto
#ST-L16-1
$$\Huge
\substack{\Sigma=(F,G,H)\\dim \Sigma=n\\m\ Input\\p\ Output}
\xrightarrow[\substack{u(t)=v(t)+kx(t)\\K\in\mathbb R^{m\times n}}]{}
\substack{\Sigma=(F+GK,G,H)\\dim \Sigma=n\\m\ Input\\p\ Output}
$$
[[State Feedback#Proposition 1|P1]] dice che per $\forall K\in \mathbb R^{m\times n}$ $$((F+GK),G)\text{ è reachable}\iff(F,G)\text{ è reachable}$$
[[State Feedback#Proposition 2|P2]] se $(F,G)$ è in [[SRF Standard Reachability Form#Riassunto|SRF]]  allora  $\forall K\in \mathbb R^{m\times n}$  $((F+GK),G)$ è in SRF con lo stesso $F_{22}$ 

Se abbiamo un paio generico non reachable $(F,G)$ non necessariamente in SRF il risultato rimane vero
##
$$\Huge
\substack{(F,G)non\\reachable}\xrightarrow[T\in \mathbb R^{n\times n}]{}(\bar F,\bar G)=(T^{-1}FT,T^{-1}G)\xrightarrow[\forall \bar K\in \mathbb R^{m\times n}]{}(\bar F+\bar G\bar K,\bar G)
$$
$\rightarrow$ con $\Delta_{\bar F+\bar G\bar K}(s)$ è un multiplo di $\Delta_{F_{22}}$ 
$$\Huge
(\bar F+\bar G\bar K,\bar G)\xrightarrow[T^{-1}]{}\substack{(F+GK,G)non\\reachable}
$$
$\rightarrow$ con $\Delta_{F+GK}(s)$ è un multiplo di $\Delta_{F_{22}}$ 

Questo implica che:
$\Large\Delta_{F+GK}(s)=\Delta_{F_{11}+G_1K_1(s)}\Delta_{F_{22}}$ 
Per trovare una relazione tra $K$ e $\bar K$ è sufficente osservare:
$\bar F+\bar G\bar K\quad=\quad T^{-1}FT+T^{-1}G\bar K\quad =\quad T^{-1}[F+G{\color {orange}\bar K T^{-1}}]T$  
quindi $K=\bar KT^{-1}$ 
