#ML-L10  
![[6 Linear Model#Regression#Linear Regression]]
Quindi:
- $\hat w-w\sim\mathcal N(0,\Sigma_w)$  
- $\Sigma_w=\sigma^2(X^TX)^{-1}$ 
Concentrandoci sull'iesimo elemento di $\hat w$:
$\hat w_i=e_i^T\hat w$
$\hat w_i- w_i=e_i^T(\hat w- w)$  dove $w_i$ e $\hat w_i$ sono scalari
$\sim \mathcal N(0, e_i^T\Sigma_we^i)$ 


Definiamo:$$\sigma_{\hat w_n}^2=e_i^T\Sigma_we_i=\sigma^2e_i^T(X^TX)^{-1}e_i$$
	sadasd
$$\hat w_i\sim\mathcal N(w_i,\sigma_{\hat w_i})$$
Equivale ad una variabile della quale non sappiamo la media ma la varianza

Un [[11 Confidence Interval]]  di livello $(1-\alpha)\times 100\%$ è per $w_i$ è dato da:
$$I_{\hat w_i}=\big[\hat w_i-\sigma_{\hat w_i}z_{1-\frac \alpha 2},\hat w_i+\sigma_{\hat w_i}z_{1-\frac \alpha 2}\big]$$
![[Drawing 2025-11-02 10.17.11.excalidraw|600]]
In questo caso è improbabile che il valore $\hat w_i$ abbia valore $0$ dato che è fuori dall'intervallo
### Remark
$\sigma^2_{\hat w_i}=\sigma^2e_i^T(X^TX)^{-1}e_i$ 

