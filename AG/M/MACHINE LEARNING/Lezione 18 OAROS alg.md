#ML-L18
On Avarange Replace One Stable
### Idea

Dato un dataset:
- $S=\set{z_1,\dots,z_i,\dots,z_m}\qquad i\in[m]\quad z_j\sim D\ \text{ i.i.d.}$ 
- $S^{(i)}=\set{z_1,\dots,z',\dots,z_m}$  l'unica differenza è l'aggiunta di perturbazione sull'i-esimo elemento

Se con l'aggiunta di una perturbazione il risultato non cambia di molto il nostro il nostro learning model significa che  non c'è overfitting.
###
Misuriamo la performance andando a vedere la differenza:
$$l(A(S^{(i)}),z_i)-l(A(S),z_i)$$
dove $A(S)\in H$ 

Più precisamente siamo interessati al valore atteso $E[\ \cdot\ ]$  di questa differenza.
### Definition
Diciamo che l'algoritmo $A(s)$ è OAROS con un rapporto $\epsilon(m)$ s.t. $(\epsilon(m)\to_{m\to\infty} 0$  se:
$$
E[l(A(S^{(i)}),z_i)-l(A(S),z_i)]\le \epsilon(m)
$$
#### Fact
$E\big[l(A(S^{(i)}),z_i)\big] = E\big[L_D(A(S))\big]$ 
$\qquad -\qquad \qquad \qquad\qquad-$  
$E\big[l(A(S),z_i)\big]\quad =E\big[L_S(A(S))\big]$
$\qquad \le\qquad \qquad \qquad\qquad\le$  
$\quad \epsilon(m)\qquad \qquad \qquad\quad\epsilon(m)$  

### Proposition
Se $A(S)$ è OAROS con  rate $\epsilon(m)$  allora:
$$E\big[\ \underbrace{l(A(S^{(i)}),z_i)-l(A(S),z_i)}_\text{generalization gap of alg A(S)}\ \big]\le \epsilon(m)$$
Che vuol dire che  l'algoritmo $A$ non va in overfit e il generalization gap è piccolo.
#### Proof
 $E\big[l(A(S),z_i)\big]\quad =E\big[L_S(A(S))\big]$ 
	 NOTE$$
	 \begin{align}
	 x\in \mathbb R^n \quad \underline x=\begin{bmatrix}x_1 &\cdots&x_n\end{bmatrix}^T\\
	 p(\underline x ) =p(x_1)p(x_2)\dots p(x_n)\\
	 E[f(\underline x)]=\int f(x)p(x_1)\dots p(x_n)\ dx\\
	 %=\int p(x_1)dx_1\int p(x_2)dx_2\dots\int f(\underline x)p(x_n) dx_n
	 \end{align}
	 $$

$$
\begin{align}
E[\ l(A(S),z_i)\ ]&= E_{\substack{S\sim D^m\\i\sim\mathcal U[m]}}[\ l(A(S),z_i)\ ]
&=E\left[\ {\sum^m_{i=1}l(A(S),z_i)}p(i)\right]\\
\
\small S=\set{z_1,\dots,z_i,\dots,z_m}&&=E\left[\ {\frac 1m\sum^m_{i=1}l(A(S),z_i)}\right]\\
\small S\sim D^m\ \ z'\sim D\ \ i\sim \mathcal U[m]&&=E[L_S(A(S))]\qquad\qquad\ \ \\
\small p(i=j)=\frac 1m
\end{align}
$$


#### Proof
$E\big[l(A(S^{(i)}),z_i)\big] = E\big[L_D(A(S))\big]$ 
 
 $$\begin{align}
E[\ l(A(S^{(i)}),z_i)\ ]
&= E_{\substack{S\sim D^m\\z\sim D\\i\sim\mathcal U[m]\\}}[\ l(A(\bar S),\bar z)\ ]
&= E_{\substack{S\sim D^m\\z\sim D}}[\ l(A(\bar S),\bar z)\ ]\qquad\ \ \ \\
\
\small S^{(i)}=\set{z_1,\dots,z',\dots,z_m}&&=E_{\bar S\sim D^m}\left[\ E_{z\sim D}[l(A(\bar S),\bar z]\right]\\
\small S\sim D^m\ \ z'\sim D\ \ i\sim \mathcal U[m]&&=E[L_D(A(S))]\qquad\qquad\ \ \ \ \ \\
\small S^{(i)}\to \bar S\ \ z_i\to \bar z
\end{align}$$


## Designing Stable Algorithms using regularization

Data una model class $H$ 
$$
A(S)=\hat h_R(\lambda)=\arg\min_{h\in H} L_S(h)+\lambda P(h)
$$
- $L_S(h)$ empirical risk chiamato anche fitting error
	Dipende dai dati
- $\lambda\ge 0$ serve a decidere quanto peso dare al costo è detto  "regularization parameter"
- $P(h)$ rappresenta il costo per scegliere un determinato modello
	Non dipende dai dati ma dal modello
	

Iniziamo  considerando $H=\set{h_w(x)=w^Tx, w\in \mathbb R^d}$ 
$$
P(h_w)=
\underbrace{\begin{cases}
||w||^2=\sum_{i=1}^dw_i^2
\\||w||_1=\sum_{i=1}^d||w_i||
\end{cases}}_\text{convex regularization terms}
\qquad
\begin{array}{cc}
\text{ridge regression } &e^2 cost\\
\text{lasso } & e^1 cost
\end{array}
$$
### Ridge Regression
$$
\hat w_{RR}=\arg\min_{w\in\mathbb R^d} L_S(w)+\lambda||w||^2
$$
- $L_S(w)= \frac 1m \sum(y_i-w^Tx_i)^2=\frac 1m||Y-Xw||^2$ 

$$\begin{align}
\nabla w(L_S(w)+\lambda w^Tw)=0\\
\frac {\cancel 2}m(X^TX)w-\frac{\cancel 2}mX^TY+2\lambda w=0\\
(X^TX+m\lambda I)w=X^TY\\\\
\hat w_{RR}=\left(\frac{X^TX}m+\lambda I\right)^{-1}\frac{X^TY}m
\end{align}$$
- $\frac{X^TX}m+\lambda I$ è sempre invertibile ed è Positive Semi Definite