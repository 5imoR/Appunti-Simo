#ML-L6[[MACHINE LEARNING]]
## Prediction problem
Dato un Sample serve trovare una funzione adeguata
![[Prediction problem]]

**Notazione** $\large [x_i]_j$  componente $j$ di $x_i$ 
$y=w^T x+b=\sum_{i=1}^dw_i[x]_i$ 

## Classification
![[classification]]
L'esempio è di binary combination
$w^Tx+b=w_1[x]_1+w_2[x]_2+b=0$
Graficamente $w^Tx+b=0$ è l'iperpiano che interseca  $[x]_1$ e $[x]_2$

# Linear model for prediction

$z_i=(x_i,y_i)\quad x_i\in\mathbb R^d\quad y_i\in\mathbb R$
$H=\{h(x)=w^Tx+b,w\in\mathbb R^d\quad b\in \mathbb R\}$ questo dipende solo da $w$ e $b$ 
loss function $l(h,z)=(y-h(x))^2$  
	si utilizza il quadrato per dare lo stesso peso ad errori positivi e negativi

**E.R.M.**
$\hat h_s \in argmin_{h\in H} L_S(h)$
Qundi si ha:
$$\large\hat h_{w,b}\in \arg\min_{h\in H} \frac 1 m \sum_{i=1}^m(y_i-h(x_i))^2\ =\ \frac 1 m \sum_1^m(y_i-w^Tx_i+b)^2$$
$\hat h_{w,b}(x)=\hat w^Tx+\hat b$ dove $\hat w$ e $\hat b$ sono i valori che rendono minimo $h_{w,b}$

Quello che ci interessa è che $h$ sia lineare in $w$ e $b$. Infatti $x$ può anche non esserlo


$$
h(x)=w^Tx+b=
\begin{bmatrix}
w^T&b
\end{bmatrix}
\begin{bmatrix}
x\\1
\end{bmatrix}
=\overline w^T\overline x\quad \overline w^T\in \mathbb R^{d+1}
$$
Per semplicità da qui in poi rinominiamo:
$$
\overline w\rightarrow w\qquad \overline x\rightarrow x
$$

Guardiamo il problema attentamente:
$$\hat w_s\in argmin_{w\in\mathbb R^d}\frac 1 m \sum_1^m(y_i-w^Tx_i)^2
$$
#### Esempio con scalari
$x\in \mathbb R\longrightarrow x\ e\ w$ sono scalari
$\hat w=\arg\min_{w\in \mathbb R} \frac 1 m \sum_1^m(y_i-wx_i)^2=y^2+w^2x_1^2-2xwy$
che è uguale a dire:
$(\frac 1 m \sum_1^my_i^2)+(\frac 1 m \sum_1^mx_i^2)w-(\frac 1 m \sum_1^mx_iy_i)w$  che corrisponde ad una parabola in $w$ e $\hat w_s$ è il suo minimo



$\hat w$ è l'unica soluzione di 
$$
\begin{align}
\frac d {dw} L_S(w)=0&=\frac 1 m \sum _1^m 2(y_i-wx_i)\frac d {dw}(y_i-wx_i) \\
&=\frac 2 m \sum_1^m y_ix_i-wx_i^2\\
&=\cancel{\frac 2 m}\left[\sum_1^m(y_ix_i)-w\sum_1^mx_i^2\right]\\
\hat w_s&=\left(\sum_1^mx_i^2\right)^{-1}\sum_1^m(y_ix_i)
\end{align}
$$
#### Esempio con vettori
$w\in\mathbb R^d$
$$
L_s(w)=\frac 1 m \sum^m_i(y_i-w^Tx_i)^2=\frac 1 m \sum^m_i(y_i-\begin{bmatrix}\cdot&\cdot&\cdot\end{bmatrix}\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix})^2
$$
$$\Large
\nabla_w L_S(w)=\begin{bmatrix}
\frac{\partial L_S}{\partial w_1}\\\vdots\\\frac{\partial L_S}{\partial w_d}
\end{bmatrix}
$$
dove:
$$
\frac{\partial L_S}{\partial w_j}=
\frac 1 m \sum _1^m 2(y_i-w^Tx_i)\frac d {dw}(y_i-w^Tx_i)\qquad=
\frac 2 m \sum _1^m (y_i-w^Tx_i)(-[x_i]_j)
$$
tramite uno sfracello di passaggi del prof si arriva ad ottenere:
	$x_i^Tw=w^Tx_i$
$$
\nabla_wLs(w)=-\frac 2 m \left(\sum_1^my_ix_i-\sum_1^m(x_ix_i^T)w\right)
$$
Esempio con le dimensioni
	$$
	\begin{align}
	\nabla_wLs(w)&=-\frac 2 m \left(\sum_1^m\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}-\sum_1^m(\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}\begin{bmatrix}\cdot&\cdot&\cdot\end{bmatrix})\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}\right)\\
	&=-\frac 2 m \left(\sum_1^m\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}-\sum_1^m(\begin{bmatrix}\cdot&\cdot&\cdot\\\cdot&\cdot&\cdot\\\cdot&\cdot&\cdot\\\end{bmatrix})\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}\right)
	\end{align}
	$$
$\hat w_s$ è la soluzione di $\nabla_w L_S(w)=0$  e si ottiene:
$$
\hat w_s=(\sum^m_1 x_ix_i^T)^{-1}\sum_1^m y_ix_i
$$
### Stessi conti ma con vector matrix notation
$$
Y=\begin{bmatrix}
y_1\\y_2\\\vdots\\y_m
\end{bmatrix}
\in\mathbb R^m
\qquad
X=\begin{bmatrix}
x^T_1\\x^T_2\\\vdots\\x^T_m
\end{bmatrix}
\in\mathbb R^{m\times d}
$$
dove 
- $m$ è il numero di dati 
- $d$ è il numero di parametri

### Errori
$e_i=y_i-x_i^Tw$ 
$$
E=\begin{bmatrix}
e_1\\e_2\\\vdots\\e_m
\end{bmatrix}
=
\begin{bmatrix}
y_1-x_1^Tw\\y_2-x_2^Tw\\\vdots\\y_m-x_m^Tw
\end{bmatrix}
=Y-Xw
$$

$L_S(w)=\frac 1 m \sum_1^m e_i^2=\frac 1 m E^T E=\large\frac 1 m [Y^TY-Y^TXw-w^TX^TY+w^TX^TXw]$ 

## Regression 
#ML-L7

$$
Y=\begin{bmatrix}
y_1\\y_2\\\vdots\\y_m
\end{bmatrix}
\in\mathbb R^m
\qquad
X=\begin{bmatrix}
x^T_1\\x^T_2\\\vdots\\x^T_m
\end{bmatrix}
\in\mathbb R^{m\times d}\quad
E=\begin{bmatrix}
e_1\\e_2\\\vdots\\e_m
\end{bmatrix}
=
\begin{bmatrix}
y_1-x_1^Tw\\y_2-x_2^Tw\\\vdots\\y_m-x_m^Tw
\end{bmatrix}
=Y-Xw
$$

$L_S(w)=\frac 1 m \sum_1^m e_i^2=\frac 1 m E^T E=\large\frac 1 m [Y^TY-Y^TXw-w^TX^TY+w^TX^TXw]$ 
- $X$ è una matrice
- $Y$ è un vettore
- $w$ è un vettore

$L_S(w)$ può essere semplificata:
- $Y^TXw$ è$\displaystyle\begin{bmatrix}&&&\\\end{bmatrix}\begin{bmatrix}&&\\&&\end{bmatrix}\begin{bmatrix}\\ \ \end{bmatrix}$ che corrisponde ad uno scalare e quindi possiamo dire che  $(w^TX^TY)^T=YX^Tw$ 
$$L_S(w)=\frac 1 m [Y^TY-2w^TX^TY+w^TX^TXw]$$
Noi vogliamo il trovare il minimo della loss function ovvero dove la derivata è pari a 0 quindi:
$$\begin{align}
\nabla_wL_S(w)=
\begin{bmatrix}
\frac {\partial L_S}{\partial w_1}\\\vdots\\\frac {\partial L_S}{\partial w_d}
\end{bmatrix}&=
\frac 1 m \left[\frac d {dw}{Y^TY}-\frac d {dw}(2w^TX^TY)+\frac d {dw}(w^TX^TXw)\right]\\
&=\frac 1 m\left[0-2X^TY+X^TXw+w^TX^TX\right]\\
&=\frac 1 m\left[-2X^TY+X^TXw+(w^TX^TX)^T\right]\\
&=\frac 1 m\left[-2X^TY+2X^TXw\right]\\
\nabla_wL_S(w)=0&=-\frac 2 m\left[X^TY-X^TXw\right]=-\frac 2 m\left[\sum^my_ix_i-\sum^m(x_ix_i^T)w\right]
\end{align}
$$

Si può verificare che:
- $\sum^my_ix_i=X^TY$ 
	$$
	\begin{bmatrix}
	x_1^T\\	x_2^T\\\vdots\\	x_m^T\\
	\end{bmatrix}^T_{X^T}
	\begin{bmatrix}
	y_1\\	y_2\\\vdots\\	y_m\\
	\end{bmatrix}_Y
	=
	\begin{bmatrix}
	x_1&	x_2&\cdots&	x_m\\
	\end{bmatrix}
	\begin{bmatrix}
	y_1\\	y_2\\\vdots\\	y_m\\
	\end{bmatrix}
	$$

- $\sum_mx_ix_i^T=X^TX$
	$$
	
	$$

Quindi possiamo vedere $X^TY=(X^TX)w$ come: $b=Aw$ 

- C'è sempre una soluzione?
	$\exists w$ s.t. $Aw=b\iff b\in Im(A)= Range\ A=col\ span(A)$
	**Remark**
	$x^Tx\in \mathbb R^{d\times d}$ 
	$b=X^TY\quad A=X^TX\quad b\in Im(X^T)=Im(X^TX)=Im(A)$  
	$Im(X^T)$ è uguale a quella di $Im(X^TX)$ perchè sono 2 matrici della stessa dimensione moltiplicate per un vettore colonna. E' rivisto anche nella lezione 8 di ST
- C'è più di una soluzione?
	Possiamo vedere il tutto come:
	$b=Aw$
	dove $w^*$ è una soluzione 
	se $A=X^TX$ non è fullrank (con la riduzione a scala ci sono colonne dipendenti):
	$\exists \tilde w\neq0\ s.t.\ A\tilde w=0$ ovvero $\tilde w\ in \ker A$ 
	quindi $w^* + \tilde w$ è una soluzione $\forall \tilde w \in ker(A)$   
- Come le troviamo?
	
#ML-L8 
$w\in \arg\min L_s(w)=\frac 1 m ||Y-Xw||^2\iff (X^TX)w=X^TY$ 

Se  $X^TX$ non è invertibile?[[Singular Value Decomposition|Si usa SVD]]
- $X=USV^T=U_1S_1V^T_1\qquad rank (X)=k<d$  
- $X\in \mathbb R^{m\times d}\quad X^TX\in\mathbb R^{d\times d}$    $m\geq d$ 
	Un esempio per $m\geq d$ è che se sei su $\mathbb R^2$ e devi rappresentare una retta ti servono almeno $2$ o più punti 
- $X^TX=(V_1S_1\cancel{U_1^T})(\cancel{U_1}S_1V_1^T)=V_1S^2V_1^T$  
$w$ è tale da:
$(V_1S_1^2V_1^T)w=V_1S_1U_1^TY\iff (X^TX)w=X^TY$
  \*                        **   
### Lemma
$w^*=V_1S_1^{-1}U^T_1Y$ 
- $w^*$ è una soluzione di  * e **
	$(V_1S_1^2\cancel{V_1^T})\underbrace{(\cancel{V_1}S_1^{-1}U_1^TY_1)}_{w^*}=V_1S_1U_1^TY_1=$ right hand side of ** questo prova che $w^*$ è una soluzione 
- $w^*$ è la norma della soluzione minima
	$\forall\hat w$ s.t. $(X^TX)\hat w=X^TY\qquad ||\hat w||\geq||w^*||$
	- $(X^TX)\hat w=X^TY$
	- $(X^TX)w^*=X^TY$ 
	$\Rightarrow (X^TX)(\hat w-w^*=0$ 
	
	$\forall \hat w =w^*+\tilde w\quad \tilde w=\hat w-w^*$  con $\tilde w\in \ker(X^TX)=Im(V_1^\perp)$ 
	$\downarrow$ 
	$X^TX=V_1S_1^2V_1^T$  questo è l'SVD dove $V_1^\perp$ s.t. $V=[V_1V_1^\perp]\quad V^TV=VV^T=I\qquad \tilde w\perp V_1$
	
	$w^*=V_1S_1^{-1}U_1^TY\rightarrow w^*\in Im (V_1)$
	
	$\longrightarrow w^*\perp\tilde w$ 
	$||\hat w||^2=||w^*||^2+||\tilde w||^2$ sono tutti numeri non negativi quindi $||\hat w||^2\geq||w^*||^2$


