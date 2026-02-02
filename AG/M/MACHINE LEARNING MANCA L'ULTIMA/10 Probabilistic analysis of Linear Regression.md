#ML-L10-1
![[6 Linear Model#Regression# Linear Regression]]

Inoltre abbiamo le assunzioni probabilistiche sull'errore: **ASS1**
![[9 Perturbation analisys of linear LS Problems#Probabilistic analysis#Assunzioni probabilistiche su E]]

Aggiungiamo un altra assunzione:  **ASS2**
- $\displaystyle e_i\sim \mathcal N(0,\sigma^2)\rightarrow P(e)=\frac 1 {\sqrt{2\pi\sigma^2}}\exp\left\{-\frac 1 2\frac{e^2}{\sigma^2}\right\}$  
#### Recall
$P[A_1,A_2]=P[A_1\cap A_2]=A_1\ AND\ A_2=P[A_1]P[A_2]$ 
####
$\displaystyle p(e_1,\dots,e_m)=\prod_{i=1}^m p(e_i)=$$\displaystyle\left(\frac 1 {\sqrt{2\pi\sigma^2}}\right)^m\exp\left\{-\frac 12\frac{\sum^m_{i=1}e_i^2}{\sigma^2}\right\}$  


#### Fact
$e_i$ i.i.d. $\rightarrow\ E=\begin{bmatrix}e_1\\\vdots\\e_m\end{bmatrix}$ 
$e_i\sim \mathcal N(0,\sigma^2)$ $\rightarrow\ E\sim \mathcal N(0,\sigma^2I)$ 
#### Fact
se:
- $w\sim \mathcal N(m_w, \Sigma_w)$ 
- $Z=Aw+b$ con $A,b$ costanti(non scalari)
$Z\sim\mathcal N(m_z, \Sigma_z)\quad m_z=Am_z+b$
$$
\begin{align}
Var[Z]&=\mathbb E[(z-m_z)(z-m_z)^T]\\
&=\mathbb E[(Aw+b-Aw-b)(*)^T]\quad\text{$(*)$ è la stessa cosa di sinistra}\\
&=A\mathbb E[(w-m_w)(w-m_w)^T]A^T\\
&=A\ Var(w)\ A^T
\end{align}
$$
#### Domanda
$w\sim \mathcal N(m_w,\Sigma_w)\quad w\in\mathbb R^n$  quant'è la $P(w)$ ?

Dalla seconda assumption possiamo dire che:
se $e\sim\mathcal N(m,\sigma^2)$
$P(e)=\displaystyle\frac 1 {\sqrt{2\pi\sigma^2}}\exp\left\{-\frac 1 2\frac{(e-m)^2}{\sigma^2}\right\}$

quindi:
$$
P(w)=\frac 1 {\sqrt{(2\pi)^n\det\Sigma_w}}\exp\left\{-\frac 1 2(w-m_w)^T\Sigma_w^{-1}(w-m_w)\right\}
$$
Che da uno scalare quindi ok

#### Domanda
Cosa ci importa di $\tilde w$ s.t. ASS1+ASS2 e come lo usiamo?
$Y=Xw+E$  e non conosciamo $w$
noi abbiamo trovato $\hat w_s=(X^TX)^{-1}X^TY$ 
L'obbiettivo della Linear Regression è: trovare $\hat w_s$ in grado di predirre una tabella partendo dall'input: $\tilde y\simeq x^Tw=\sum_{i=1}^d[x]_iw_i$ 

se un valore è inutile avremo il valore corrispondente in $w$ pari a $0$
	$$
	x=\begin{bmatrix}
	\text{temp. today}\\
	\text{pressure}\\
	\text{dir. of wind}\\
	\text{€ to \$ change}\\
	\end{bmatrix}
	\qquad 
	w=\begin{bmatrix}
	*\\ *\\ *\\ 0
	\end{bmatrix}
	$$
Non a senso cercare $0$ in $\hat w$ poichè i valori trovati da noi non saranno mai esattamente zeri.
Ma non basta dire il valore, serve anche il range dell'errore per calcolare l'inpatto di $\tilde w =\hat w_s-w$ nella nostra previsione. Per questo si introduce il concetto di [[11 Confidence Interval]]
