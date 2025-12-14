#ML-L22-1
# Important
$X$ gaussiana $\mathcal N(m_x,\Sigma_x)$ 
$Y=AX+b$  $Y\sim\mathcal N(Am_x+b,\ \ A \big[\ \Sigma_x\ \big] A^T)$ 
## Gaussian Processes (per N.L. Regression)
Non Linear
$$
h(x)=\sum_{i=0}^d\varphi_i(x)w_i=\phi^T(x)w
$$
- $\varphi_i(x)$ basis function conosciute
Prior on $p(w)\sim\mathcal N(0,\gamma I)$ 
	Più avanti potremo cambiare la matrice di covaianza.
Possiamo ripetere lo stesso processo probabilistico dati $(y_i,x_i)\quad i=1,\dots, m$, assumiamo che il modello sia:   $Y=\phi(x)w+E$:
$$\Phi=\begin{bmatrix}
\phi^T(x_1)\\\vdots\\\phi^T(x_m)
\end{bmatrix}
\qquad
\phi(x)=\begin{bmatrix}
\varphi_1(x)\\\vdots\\\varphi_d(x)
\end{bmatrix}
$$
Si vuole mappare $p(w)$ come una *equal assumption* su $h(x)$:
$w\sim\mathcal N(0,\gamma^2I)$ 
$\phi(x)$ è una costante perchè $x$ è fissata.
$h(x)$ è un *"gaussian random vector"* (la trasformazione lineare di vettori gaussiani)
$E[h(x)]=\sum^d_{i=1}\varphi_i(x)E[w_i]=0$ 
$Var\set {h(x)}=\phi^T(x)\ \big[\gamma I\big]\ \phi(x)$ 
![[Drawing 2025-12-11 10.15.21.excalidraw]]
Il disegno rappresenta:
- In verde la probabilità che $h(x)$ passi a quell'altezza, quindi più è "grande" la gaussiana più è probabile che sulla linea tratteggiata passi $h(x)$
- In arancione una possibile $h(x)$, la nostra candidata
- Le gaussiane verdi sono più o meno ripide in base a $\phi^T(x)w$ 
- Le gaussiane verdi sono centrate in $0$ perchè  il valore atteso è 0 (?)


Consideriamo:
$h(\underline x)=\begin{bmatrix}h(x_1)\\\vdots\\h(x_m)\end{bmatrix}=\begin{bmatrix}\phi^T(x_1)\\\vdots\\\phi^T(x_m)\end{bmatrix}w$  
$\Rightarrow$ 
$E[h(\underline x)]=0$ 
$$
\begin{align}
Var\set {h(\underline x)}&=
\begin{bmatrix}\phi^T(x_1)\\\vdots\\\phi^T(x_m)\end{bmatrix}\big[\gamma I\big] \begin{bmatrix}\phi(x_1)&\vdots&\phi(x_m)\end{bmatrix}\\\\
&=\gamma\begin{bmatrix}
\phi^T(x_1)\phi(x_1)&\cdots&\phi^T(x_1)\phi(x_m)\\
\vdots&\ddots&\vdots\\
\phi^T(x_m)\phi(x_1)&\cdots&\phi^T(x_m)\phi(x_m)\\
\end{bmatrix}
\end{align}
$$
Andiamo a chiamare $\gamma\phi^T(x_i)\phi(x_j) = k(x_i,x_j)$
Diciamo che una funzione $h(x)\in \mathbb R\quad x\in \mathbb R^d$ è un gaussian process con media $E[h(x)]=\mu(x)$ e covarianza $k(x,x')=Cov(h(x),h(x'))$  se $\forall \underline x\quad h(\underline x)$ è un Gaussian random vector con:
$E[h(\underline x)]=\begin{bmatrix}\mu(x_1)\\\vdots\\\mu(x_m)\end{bmatrix}$ 
$Var\set{h(\underline x)}=E[h(\underline x)-E[(h(\underline x)])(h(\underline x)-E[h(\underline x)])^T]=K_{\underline x\underline x}=K_{\underline x\underline x}^T\ge 0$  
$[Var\set{h(\underline x)}]_{ij}=k(x_i,x_j)=k_{x_i,x_j}$ 


### Come lo andiamo ad utilizzare per non linear regression
$\mu(x),k(x,x')$  sono dati 
l'obbiettivo è trovare la funzione $\hat h(x)$  partendo da dei punti.
Il modello è $y_i=h(x_i)+e_i$  con $e_i\perp e_j$ perchè indipendenti, inoltre $e_i=\mathcal N(0,\sigma^2)$ 

Trovare $\hat h(x)\forall x\Rightarrow(h(x)|Y)\sim\mathcal N(\cdot,\cdot)$ 
### Remark
$$
\begin{bmatrix}
h(x) \\
y_1 \\
\vdots \\
y_m \\
\end{bmatrix}
=
\begin{bmatrix}
h(x) \\
h(x_1) \\
\vdots \\
h(x_m) \\
\end{bmatrix}
+
\begin{bmatrix}
0\\
e_1\\
\vdots \\
e_m \\
\end{bmatrix}
\begin{array}{c}
\left.\phantom{
\begin{bmatrix}
\\
\end{bmatrix}
}\right\} Z_1\\
\left.\phantom{
\begin{bmatrix}
\\
\\
\\
\end{bmatrix}
}\right\} Z_2
\end{array}
$$
Tutti e tre sono gaussiani
$Z:=\begin{bmatrix}Z_1\\Z_2\\\end{bmatrix}\quad E[Z]=\begin{bmatrix}\mu_1\\\mu_2\\\end{bmatrix}\quad Var[Z]= Var\begin{bmatrix}Z_1\\Z_2\\\end{bmatrix} = \begin{bmatrix}\Sigma_{11} & \Sigma_{12}\\\Sigma_{21} & \Sigma_{22}\\\end{bmatrix}$ 

$p(Z_1|Z_2)\sim \mathcal N(\mu_{1|2},\Sigma_{1|2})$ 
dove:
- $\mu_{1|2}=\mu_1\Sigma_{11}\Sigma_{22}^{-1}(Z_2-\mu_2)$
- $\Sigma_{1|2}=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$

Manca la parte di giovedi