#ML-L10 
![[confidence|300]]
Non si vuole sapere solo l'eventuale valore corrispondente all'input, ma anche quanto può essere grande l'errore secondo i nostri dati

Assumiamo di avere:
- $x\sim \mathcal N(m,\sigma^2)$ con:
- $\sigma^2$ conosciuto
- $P_x(x,\theta)\quad \theta=(m,\sigma^2)$
Obiettivo:
Ottenere un intervallo $I$  che contiene $m$ con una alta probabilità
Non si sa se $x$ ed il suo intervallo includono $m$ 

Serve trovare $I_x$ s.t. $P[I_x\ni m]=1-\alpha$ 
Ci sono svariati modi per mettere $\alpha$ ma noi vogliamo quello che ci da la massima probabilità
![[probXconfidence]]
$$
\begin{align}
&P[x\in[m-\Delta\alpha,m+\Delta\alpha]]=1-\alpha\\
&x\in[m-\Delta\alpha,m+\Delta\alpha]\iff [x-\Delta\alpha,x+\Delta\alpha]\ni m\\
&P[\underbrace{[x-\Delta\alpha,x+\Delta\alpha]}_{\huge I_x}\ni m]=1-\alpha
\end{align}
$$

### Definition
 Diciamo che $I_x$ è un Confidence Interval di livello $(1-\alpha)\times100\%$ per  $m$ se 
 $$P[I_x\ni m]=1-\alpha$$

### Come trovare $\Delta\alpha$ 
#### Step 1
Consideriamo:
- $z\sim \mathcal N(0,1)$ 
- $z_p$ il *p-th level percentile* s.t. $P[z\leq z_p]=p$ 
![[zp]]
#### Step 2
Voglio trovare l'intervallo che abbia probabilità $1-\alpha$ 

$$\huge P[z\in[-z_{(1-\frac\alpha2)},z_{(1+\frac \alpha2)}]]=1-\alpha$$

![[zp2]]
#### Step 3
Normaliziamo il tutto per tornare alla gaussiana standard
$\displaystyle x\sim\mathcal N(m,\sigma^2)\rightarrow \frac {x-m}\sigma\sim \mathcal N(0,1)$ 
$P[\frac {x-m}\sigma\in[-z_{(1-\frac\alpha2)},z_{(1+\frac \alpha2)}]=1-\alpha$ 
$\iff \Large P[x\in[m-\sigma z_{(1-\frac\alpha2)},m+\sigma z_{(1+\frac \alpha2)}]]=1-\alpha$  

### Conseguenza

$\displaystyle\large I_x=\big[m-\sigma z_{(1-\frac\alpha2)},m+\sigma z_{(1+\frac \alpha2)}\big]$ è un confidence interval di livello $(1-\alpha)\times 100\%$


## Valutare Confidence of Predictions
#ML-L11
![[Drawing 2025-11-03 18.02.26.excalidraw]]
Oltre a dire il valore $\hat y_0$ serve anche conoscere l'intervallo che siamo praticamente sicuri che contiene $y_0$ 
### Assunzioni
- $y_0=x_0^Tw+e_0$ 
- $\hat y_0=x_0^T\hat w$ 
- $\tilde y_0=\hat y_0-y_0=x_0^T(\hat w-w)-e_0$

- $e_0$ è indipendente dal resto
- $\hat w=(X^TX)^{-1}X^T Y$ 
	- $(X^TX)^{-1}X^T$ sono tutte le assunzioni fatte fin ora
	- $Y$ è il valore ottenuto dalle assunzioni + l'errore

$\tilde y_0=\hat y_0-y_0\sim \mathcal N(0,\sigma^2_{y_0})$
$$\begin{align}
\sigma^2_{y_0}&=x_0^T\Sigma_wx_0+\sigma^2\\
&=x_0^T(\sigma^2(X^TX)^{-1})x_0+\sigma^2\\
&=\sigma^2[x_0^T(X^TX)^{-1}x_0+1]
\end{align}$$
Posso costruire l'intervallo:
$$\Large
P[\hat y_0-y_0\in [\hat y_0-\sigma_{\hat y_0}z_{(1-\frac\alpha2)},\hat y_0+\sigma_{\hat y_0}z_{(1-\frac\alpha2)}]=1-\alpha
$$
