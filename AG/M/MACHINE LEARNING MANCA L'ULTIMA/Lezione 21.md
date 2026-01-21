#ML-L21 [[Lezione 20]]

# Probabilistic interpretation of Regularization 
**In particolare [[Lezione 19#Ridge Regression|Ridge Regression]] 

$Y=Xw+E$ 
$E\sim\mathcal N(0,\sigma^2I)$ 
$w\sim\mathcal N(0,\gamma I)$ 
$w\perp\!\!\!\perp E$ 
$w\perp\!\!\!\perp x$ 

$$
\begin{cases}
P(Y|X,w)=P(E=Y-Xw)\\
P(w|x)=p(w)\quad \text{distribuzione conosciuta}
\end{cases}
$$
sapendo questo possiamo scrivere:$$P(w|YX)=\frac{P(Y|Xw)P(w|x)}{P(Y|X)}$$
	- $P(w|YX)$ postirior (of $w$ given $Y,X$)
	- $P(Y|Xw)$ likelihood
	- $P(w|x)$ prior lo conosciamo già
	- $P(Y|X)$ serve solo a normalizzare non ci interessa
		$=\int p(Y|Xw)p(w)\ dw$ 
$$
\Rightarrow P(w|YX)\propto\underbrace{P(Y|X,w)}_{\large\mathcal N(Xw,\sigma^2I)}P(w)=
\begin{array}{c}
\
{\displaystyle\color{orange}\frac{1}{\sqrt{(2\pi)^m\det(\sigma^2 I)}}}
\displaystyle\exp\set{-\frac 12{\color{lightgreen}(Y-Xw)^T}(\sigma^2I)^{-1}{\color{lightgreen}(Y-Xw)}}\\\cdot\ \ 
{\displaystyle\color{orange}\frac{1}{\sqrt{(2\pi)^m\det(\gamma I)}}}
\displaystyle\exp\set{-\frac 12{\color{lightgreen}w^T}(\gamma I)^{-1}{\color{lightgreen}w}}\phantom{ssssssssssss}
\end{array}
$$
- $\textcolor{orange}{■}$  è costante rispetto ad $w$ e quindi non ci interessa per trovare il massimo
- $\textcolor{lightgreen}{■}$ la parte dentro l'esponente è uno scalare
Maximum at Posteriori
$$
\begin{align}
\hat w_{MAP}=\arg\max_w P(Y|Xw)p(w)
&=\arg\max \log P(Y|Xw)+\log P(w)\\
&=\arg\max -\frac 12\frac {||Y-Xw||^2}{\sigma^2}-\frac 12\frac{||w||^2}{\gamma}\cdot 2\cdot\sigma^2\frac 1m\\
&=\arg\max -\frac {||Y-Xw||^2}{m}-\frac{||w||^2\sigma^2}{m\gamma}\\
&=\arg\min \underbrace{\frac {||Y-Xw||^2}{m}}_{L_S(w)}+\underbrace{\frac{\sigma^2}{m\gamma}}_\lambda\underbrace{||w||^2}_{p(w)}\qquad \text{uguale a R.R.}\\
&=\arg\min L_S(w)+\lambda||w^2||
\end{align}
$$
$\lambda$ ha il denominatore conosciuto a priori mentre il numeratore che va calcolato

Possiamo stimare $\sigma^2$ e $\gamma$ dai dati? 
$$
\int P_{\sigma^2} (Y|Xw)P_\gamma(w)dw=P_{\sigma^2\gamma}(Y|X)\quad\text{Marginal Likelihood}
$$
Yes, $\displaystyle\hat \sigma^2,\hat \gamma=\arg\max_{\sigma^2,\gamma}P_{\sigma^2,\gamma}(Y|X)$
#### Remark
$Y=Xw+E=[X\quad I]\begin{bmatrix} w \\ E \end{bmatrix}$ 
$w$ e $E$ sono indipendenti tra loro,quindi hanno covarianza nulla.
esiste una matrice dove:$\begin{bmatrix}Var [w] & Cov \\Cov & Var[E] \\\end{bmatrix}$ quindi $\begin{bmatrix} w \\ E \end{bmatrix}=\mathcal N\left(0,\begin{bmatrix}\sigma^2 I& 0 \\0 & \gamma I \\\end{bmatrix}\right)$ 
####
$E[Y]=[X\quad I]E\begin{bmatrix} w \\ E \end{bmatrix}=0$
$Var[Y]=[X\quad I]\begin{bmatrix}\sigma^2 I& 0 \\0 & \gamma I \\\end{bmatrix}\begin{bmatrix} w \\ E \end{bmatrix}=\gamma X^TX+\sigma^2I$ 
### Empirical Bayes
$$P_{\sigma^2,\gamma}(Y|X)=\frac 1{\sqrt{(2\pi)^m\det(\gamma X^TX+\sigma^2 I)}}\cdot\exp\set{\frac 12 Y^T(\gamma X^TX+\sigma^2 I)^{-1}Y}\quad\text{not convex}$$
$\displaystyle\hat \sigma^2_{ML},\hat \gamma_{ML}=\arg\max_{\sigma^2,\gamma}P_{\sigma^2,\gamma}(Y|X)\longrightarrow\hat w=\arg\min_w\frac{||Y-Xw||^2}m+\frac{\hat\sigma^2_{ML}}{m\hat\gamma_{ML}}||w||^2$   

Questo è più generico rispetto a K-fold ma non ce nè uno migliore tra i due.


### Beyond Linear Regression
$\hat y=h(x)$ non lineare in $x$
#### (1) 
$$h_w(x)=\phi$$