#ML-L15
![[Logistic regression#Remark]]

#### Q1
Come troviamo  $w$ che meglio descrive i nostri dati? 
Dato $(x_i,y_i)\quad i=1\dots n$
$\displaystyle\hat w_{ML}=\arg\max_w \underbrace{P(x_1,y_1,\dots x_m,y_m)}_{Likelihood\   Function}=\arg\max_w \prod^m_{i=1}P_w(y_i|x_i)=\arg\max_w \prod^m_{i=1} \frac 1{1+e^{-y_iw^Tx_i}}$   
	Maximum Likelihood

#### Q2
Dato $\hat w_{ML}$ come classifichiamo un nuovo datapoint con input $x$?
##### Remark
$w_{ML}^Tx>0$
$\Rightarrow$ 
- $\displaystyle P_w[y=+1|x]=\frac 1 {1+ {e^{-w^T_{ML}x}}}>\frac 1 2$ se questo è alto vuol dire che c'è una alta prob di $y=1$
- $\displaystyle P_w[y=-1|x]=\frac 1 {1+ {e^{w^T_{ML}x}}}<\frac 12$ 
##### Risposta
$\hat y(x)=\arg\max_j P[y=j|x]$

#### Remark
Optimal vuol dire che  [[Lezione 15#Risposta|la risposta]] appena trovata minimizza  $L_D(h)$ (considerando 0-1 loss)
in altre parole:
$$
L_D(\hat y(x))\le L_D(h(x))\quad  \forall h(x) 
$$
sotto l'assunzione che $\Large P_w[y|x]=\frac 1 {1+ {e^{-y\ \hat w^T_{ML}x}}}$ 
####
#### Proof ($w=\hat w_{ML}$)
$$
\begin{align}
L_D(h)&= E_D[l(z,h)]\quad z\in \mathcal D\\
&= E_{Dx}[E_{Dy|x}[l(z,h)|x]]
\end{align}
$$
##### Remark
$E[l(z,h)|x]\qquad=\qquad P[h(x)\ne y|x]\qquad=\qquad1-P[h(x)= y|x]$ 
#####
ma noi sappiamo che:                                            quindi possiamo dire che:
$P[h(x)= y|x]\le P[\hat y(x)= y|x]$                               $E[l(z,h)|x]\ge E[l(z,\hat y(x))|x]$ 

Usando ora  $L_D(s)=E_{Dx}[E_{Dy|x}[l(z,h)|x]]$ possiamo affermare che:


$\Large E[l(z,h)|x]\ge E[l(z,\hat y(x))|x]$ se questo è vero allora lo è anche:

$\Large E_{Dx}[E_{Dy|x}[l(z,h)|x]]\ge E_{Dx}[E_{Dy|x}[l(z,\hat y(x))|x]]$
##### Remark
abbiamo $x$ variabile random e $f(x)\ge g(x)$ 
$E[f(x)]=\int f(x)p(x)\ dx$
$E[g(x)]=\int g(x)p(x)\ dx$
$E[f(x)]-E[g(x)]=\int \big[f(x)-g(x)\big]\ p(x)\ dx\ge 0$ 
### Training Logistic Regression (con ML)

$$
\begin{align}
\hat w_{ML}&=\arg\max_{\large w\in\mathbb R^d} \prod^m_{i=1} \frac 1{1+e^{-y_iw^Tx_i}}\\\\
&=\arg\max_{\large w\in\mathbb R^d}\log \left(\prod^m_{i=1} \frac 1{1+e^{-y_iw^Tx_i}}\right)\\
&=\arg\min_{\large w\in\mathbb R^d}-\log \left(\prod^m_{i=1} \frac 1{1+e^{-y_iw^Tx_i}}\right)\\
&=\arg\min_{\large w\in\mathbb R^d}-\frac 1m\sum_{i=1}^m\log \left(\underbrace{1+e^{-y_iw^Tx_i}}_{Log\ Loss}\right)
\end{align}
$$
Come risolviamo:
$$\hat w_{ML}=\arg\min_{\large w\in\mathbb R^d}\underbrace{-\frac 1m\sum_{i=1}^m\log \left({1+e^{-y_iw^Tx_i}}\right)}_{\large L_S(w)}$$?
$\displaystyle\frac{\partial L_s}{\partial{w}}=\frac 1m\sum_{i=1}^m{\Huge\frac{-y_ix_ie^{-y_iw^Tx_i}}{1+e^{-y_iw^Tx_i}}}=0$  
Sappiamo che $L_s(w)$ è convessa
