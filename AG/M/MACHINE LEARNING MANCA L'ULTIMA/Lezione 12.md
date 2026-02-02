#ML-L12
[[11 Confidence Interval]]
![[6 Linear Model#Regression#Linear Regression]]

Dato $x_0$ performare una predizione su  $\hat y_0=x^T\hat w$ 
- l'errore sarà: $\tilde y_0=\hat y_0-y_0=x_0^T(\hat w-w)-e_0$ 
- Var dell'errore sarà: $Var(\tilde y)=x_0^TVar(\hat w)x_0+\sigma^2\qquad Var(\hat w)=\Sigma_w =\sigma^2(X^TX)^{-1}$ 
Vogliamo calcolare  $L_D$ associata con $\bar w$
$$L_D=E[\underbrace{l(\bar w,z)}_{square\ loss}] \qquad\hat y=x^T\bar w\qquad l(\bar w, z)=(y-x^T\bar w)^2$$
Stiamo facendo la media rispetto alla distribuzione $z\sim \mathcal D$ dove $z=(x,y)$ 
$$
\begin{align}
L_D(\bar w)&=\int\int l(\bar w,z)p(z)\ dz&=\int\int l(\bar w,z)p(y|x)p(x)\ dx\ dy \\
&=\int\left[\underbrace{\int l(\bar w,z)p(y|x)\ dy}_{\large E[l(\bar w,z)|x]}\right]p(x)\ dx\\\\
&=\large E[E[l(\bar w,z)|x]]
\end{align}
$$

#### Domanda
Assumiamo $y=x^Tw+e$ con $e\sim \mathcal N(0,\sigma^2)$ generative model
- $p(y|x)$  prende $x$ e vede la distribuzione di $y$ con $x$ fissato
Come generiamo $x$?
Serve assegnare $p(x)$ su $x$

C'è una relazione tra
$Var(\tilde y_0)=x_0^T Var(\hat w)x_0+\sigma^2$ 
e
$E[E[l(\bar w,z)|x]]$ 

sia $E_D[l(\bar w,z)]$ che $Var(\tilde y_0)$ sono il valore atteso di $(\hat y-y)^2$
sono la stessa cosa?

$\tilde y_0=\hat y_0-y_0$ dipende da $\hat w$ 
noi prendiamo l'$\exp$ wrt $\hat w$ che cambia per ogni dataset, e quindi non è fissato

Stiamo guardando l'impatto dell'incertezza in $\hat w$ nella predizione che dipende dal dataset
####
$$
\begin{align}
 E[E[\underbrace{(y-x^T\bar w)^2|x]}_{\Large E[x^T(w-\bar w)+e)^2|x]}]&\\
\\\\
E[x^T(w-\bar w)+e)^2|x]&=\int x^T(w-\bar w)+e)^2p(y|x)\ dy\qquad p(y|x)\sim \mathcal N(x^Tw,\sigma^2)\\
E=[l(w,z)|x]&=\int x^T(w-\bar w)+e)^2p(e)\ de\qquad p(e)\sim \mathcal N(0,\sigma^2)\\
&= \int[x^T(w-\bar w)]^2+e^2+2ex^T(w-\bar w)\\
&=\int[x^T(w-\bar w)]^2+\sigma^2+0\\
&=\int(w-\bar w)^Txx^T(w-\bar w)+\sigma^2\\
\end{align}
$$

- $(w-\bar w)$ vettore colonna
- $x$ matrice
- $\sigma$ scalare
$$
\begin{align}
L_D(\bar w)&=E[E[l(\bar w, z)|x]]\\
&=\int [(w-\bar w)^Txx^T(w-\bar w)+\sigma^2]p(x)\ dx\\
&=(w-\bar w){\color {orange}\int xx^Tp(x)\ dx}\ (w-\bar w)+\sigma^2\\
&=(w-\bar w){\color{orange}M_x}(w-\bar w)+\sigma^2
\end{align}
$$

### Remark
Se ho $\tilde y_0^2 = (\hat w-w)^Tx_0x_0^T(\hat w-w)+e_0^2-2e_0(\hat w-w)^Tx_0$
	$e_0$ ha media pari a $0$

$E[\tilde y_0^2|x_0,S]=(\hat w-w)^Tx_0x_0^T(\hat w-w)+\sigma^2$

$E[E[\tilde y_0^2|x_0,S]|x]=x_0^T\underbrace{E[(\hat w-w)(\hat w-w)^T]}_{Var(\hat w)}x_0+\sigma^2$
### Remark 
$Var\set{\tilde y_0}=x_0^TVar\set{\hat w}x_0+\sigma^2= E[L_D(\hat w|x)|x]$  

$L_D(\hat w |x)=L_D(\bar w|x)|_{\bar w=\hat w}$
$L_D(\bar w|x)=E[l(\bar w,z)|X]$

### Reacall calcolo di $Var \{\hat w\}$ 
$\hat w = (X^TX)^{-1}XY$
$w=(X^T X)^{-1}X^T E$ 
$Var(\hat w-w)=\sigma^2(X^TX)^{-1}$
#Riguarda_appunti_lezione_di_merda