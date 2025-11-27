#ML-L9 [[SVD Singular Value Decomposition]] LS=Least Square
## Deterministic worst case perturbation analysis
$\hat w =\arg\min_w ||Y-Xw||^2\qquad X=U_1S_1V_1^T$ 
tramite [[Pseudo Inverse of the matrix A]] possiamo dire che:
$\hat w=V_1S_1^{-1}U_1^TY$

Cosa succede se $Y$ è perturbata ovvero invece di $Y$ si ha $Y+\Delta Y$ 
$$
\begin{align}
\bar w&=V_1S_1^{-1}U_1^T(Y+\Delta Y)\\
&=\underbrace{V_1S_1^{-1}U_1^TY}_{\Huge\hat w}+\underbrace{V_1S_1^{-1}U_1^T\Delta Y}_{\huge\Delta w}
\end{align}
$$
Qual'è la perturbazione peggiore $\Delta Y$(che ha l'effetto più grande sulla soluzione $\bar w$)?
$$
\begin{align}\Large
\frac{\frac{||\Delta w||}{||\hat w||}}{\frac{||\Delta Y||}{||Y||}}
\end{align}
$$
dove:
- $\displaystyle\frac{||\Delta w||}{||\hat w||}$ : relative part on the solution
- $\displaystyle\frac{||\Delta Y||}{||Y||}$ : relative part on the data

### Lemma
Vedremo che $\max_{\Delta Y, Y}\ \displaystyle\frac{||\Delta w||}{||\hat w||}\Big/\displaystyle\frac{||\Delta w||}{||\hat w||}=\frac{\sigma_1(x)}{\sigma_k(x)}$ dove:
- $\sigma_1$ è il valore più grande di $X$
- $\sigma_k$ è il valore più piccolo di $X$ 
- $X=U_1S_1V_1^T$ 
#### Proof
Per risolvere $\max_{\Delta Y, Y}\ \displaystyle\frac{||\Delta w||}{||\hat w||}\Big/\displaystyle\frac{||\Delta w||}{||\hat w||}=\frac{\sigma_1(x)}{\sigma_k(x)}$ possiamo fissare $||Y||=1\ e\ ||\Delta Y||=\delta$ 
Per avere il massimo andiamo a modificare $Y$ e $\Delta Y$ in:
- $\hat w=V_1S_1^{-1}U_1^TY$ 
- $\Delta w=V_1S_1^{-1}U_1^T\Delta Y$

$\Delta w=\displaystyle\max_{\substack{\Delta Y\\||\Delta Y||=\delta}}||\underbrace{V_1S_1^{-1}U_1^T}_A\underbrace{\Delta Y}_v||=\delta\frac 1 {\sigma_k(x)}$ 

	scrivendolo nella forma:
	$\displaystyle\max_{\substack{\Delta Y\\||\Delta Y||=\delta}}||Av||=\delta\frac 1 {\sigma_k(x)}$
	si può vedere che è la stessa formula per trovare la direzione dell'amplificazione massima nell' [[Singular Value Decomposition|SVD]].
Il massimo è ottenuto quando $\Delta Y=\delta u_k$ dove $U_1=[u_1,\dots, u_k]$ 
#ML-HW-L9
	Dimostra questo massimo


con un argomento simile si può provare:
$\hat w=\displaystyle\min_{\substack{Y\\||Y||=1}}||\underbrace{V_1S_1^{-1}U_1^T}_A\underbrace{Y}_v||=\frac 1 {\sigma_1(x)}$ 
Il minimo è ottenuto quando $Y=u_1$ 

Questo ci porta  a:
$$
\begin{align}
\max_{\substack{ ||Y||\\||\Delta Y||}}={\Large
\frac{\frac{||\Delta w||}{||\hat w||}}{\frac{||\Delta Y||}{||Y||}}}
=\frac{\cancel
{\delta}\frac 1 {\sigma_k(x)}\sigma_1(x)}{\cancel{\delta}}=\frac {\sigma_1(x)} {\sigma_k(x)}
\end{align}
$$
Possiamo quindi dire che una piccola perturbazione sui dati può generare grandi perturbazioni nella soluzione se i dati sono simili

### Definition Ill conditioned
Diciamo che un linear LS problem
$\hat w =\arg\min_w ||Y-Xw||^2\qquad X=U_1S_1V_1^T$ è *ill conditioned* se:
$\displaystyle c(x)=\frac {\sigma_1(x)} {\sigma_k(x)}>> 1\qquad (\simeq10^3 \simeq10^6)$ 


![[perturbation]]
Nell'immagine la perturbazione sui dati è la stessa ma l'effetto è molto maggiore per dati simili

## Probabilistic analysis
Assumiamo:
$$
y_i=x_i^Tw+e_i
$$
- $w, e_i$ non sono conosciuti
$$
\color {orange}Y=Xw+E
$$
Calcoliamo l'E.R.M.
- $\tilde w=\hat w-w$ 
- $\hat w=\arg \min ||Y-Xw||^2$ 
assumendo $X^TX$ invertibile
- $\color {lightgreen}{\hat w=(X^TX)^{-1}X^TY}$ 

andando ad unire <span style="color: orange;">■</span> e <span style="color: lightgreen;">■</span> si ottiene:
$$
\begin{align}
\hat w &=(X^TX)^{-1}X^T(Xw+E)\\
&=\cancel{(X^TX)^{-1}}\cancel{X^TX}w+(X^TX)^{-1}X^TE\\
&=(X^TX)^{-1}X^TE+w\\
\\
\tilde w&= \hat w- w=(X^TX)^{-1}X^TE
\end{align}
$$


##### Assunzioni probabilistiche su E
[[PROBABILITY]]
1. $\mathbb E[e_i]=0$ la media è 0
2. $Var\{e_i\}=\sigma^2$           $\qquad \Sigma_w$ matrice della varianza di $w$ 
3. $e_i$ sono i.i.d.
####
4. più avanti altre
	Spesso faremo assunzioni più importanti s.t. $e_i\sim \mathcal N(0,\sigma^2)$ 
		$\mathcal N$ è una distribuzione normale o gaussiana
		motivato dal teorema del limite centrale
Possiamo dire che:
$$\begin{align}
&E=\begin{bmatrix}e_1\\\vdots\\e_m\end{bmatrix}\rightarrow \mathbb E(E)=0\rightarrow \mathbb{E}(E)=\begin{bmatrix}0\\\vdots\\0\end{bmatrix} \\
&Var[E]=\mathbb E\Big[\ \underbrace{(E-\mathbb E(E))}_{1\times m}\underbrace{(E-\mathbb E(E))^T}_{m\times 1}\ \Big]=\sigma^2\underbrace{Im}_{m\times m}\\\\
\Rightarrow&\mathbb E[\tilde w]= \mathbb E\Big[\ \underbrace{(X^TX)^{-1}X^T}_{\text{fixed}}E\ \Big]=(X^TX)^{-1}X^T\ \mathbb E(E)=0\\
&Var[\tilde w]=\mathbb E[\tilde w\ \tilde w^T]=\mathbb E\Big[\ (X^TX)^{-1}X^TE\ E^TX(X^TX)^{-1}\ \Big]\\
&\qquad\qquad\qquad\qquad\,=\underbrace{(X^TX)^{-1}X^T}_{*}\ \  \underbrace{\mathbb E(E\ E^T)}_{Var\ E=\sigma^2I}\ \ \underbrace{X(X^TX)^{-1}}_{*^T}\\
&Var[\tilde w]=\cancel{(X^TX)^{-1}}\cancel{X^T X}(X^TX)^{-1}\sigma^2=\sigma^2 (X^TX)^{-1}
\end{align}$$
$Var[\tilde w]=\sigma^2 (X^TX)^{-1}$
dove:
- $\sigma^2$ è la quantità di perturbazione
- $(X^TX)^{-1}$ dipende dall'input
