#ML-L11-2
![[6 Linear Model#Regression#Linear Regression]]
Quindi:
- $\hat w-w\sim\mathcal N(0,\Sigma_w)$  
- $\Sigma_w=\sigma^2(X^TX)^{-1}$ 
Concentrandoci sull'iesimo elemento di $\hat w$:
$\hat w_i=e_i^T\hat w$
$\hat w_i- w_i\qquad\quad=e_i^T(\hat w- w)$  dove $w_i$ e $\hat w_i$ sono scalari
$\sim \mathcal N(0, e_i^T\Sigma_we^i)$ 


Definiamo:$$\sigma_{\hat w_n}^2=e_i^T\Sigma_we_i=\sigma^2e_i^T(X^TX)^{-1}e_i$$

$$\hat w_i\sim\mathcal N(w_i,\sigma_{\hat w_i})$$
Equivale ad una variabile della quale non sappiamo la media ma la varianza

Un [[11 Confidence Interval]]  di livello $(1-\alpha)\times 100\%$ è per $w_i$ è dato da:
$$I_{\hat w_i}=\big[\hat w_i-\sigma_{\hat w_i}z_{1-\frac \alpha 2},\hat w_i+\sigma_{\hat w_i}z_{1-\frac \alpha 2}\big]$$
![[Interval|600]]
In questo caso è improbabile che il valore $\hat w_i$ abbia valore $0$ dato che è fuori dall'intervallo
### Remark
$\sigma^2_{\hat w_i}=\sigma^2e_i^T(X^TX)^{-1}e_i$ 
$X^TX=[x_1\dots x_m]\begin{bmatrix}x^T_1\\\vdots\\x^T_m\end{bmatrix}=\displaystyle m(\frac 1m\sum_{i=1}^m x_ix_i^T)$  

### Remark
$X\in \mathbb R^d\qquad X\sim \mathcal D_x\qquad E[XX^T]=M_x$ 
$x_i$ i.i.d. $x_i\sim \mathcal D_x$
$\hat M_x=\frac 1m\sum_{i=1}^m x_ix_i^T)\to^{LLN}_{m\to+\infty}M_x$  


$\displaystyle\sigma^2_{\hat w_i}=\sigma^2e_i^T(X^TX)^{-1}e_i= \sigma^2\frac{e_i^TM_x^{-1}e_i}m$  
Dove la grandezza di $M_x$ cambia la grandezza dell'intervallo

# Risk
#ML-L11-4
$L_D(h)=E[l(h,z)]$ 
- loss $l(h,z)=(y-h_w(x))^2$
- $h_w(x)=w^Tz$  dove $w^T$ è la parametrizzazione del predittore h
- $L_D(h)=E_\mathcal D[(y-w^Tx)^2]$
	- $\mathcal D$ è la joint distribution su $x$ ed $y$


