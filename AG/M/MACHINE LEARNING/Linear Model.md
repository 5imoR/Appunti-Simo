#ML-L6[[MACHINE LEARNING]]
## Prediction problem
Dato un Sample serve trovare una funzione adeguata
![[Prediction problem]]

**Notazione** $\large [x_i]_j$  componente $j$ di $x_i$ 
$y=w^T x+b=\sum_{i=1}^dw_i[x]_i$ 

## Classification
![[Drawing 2025-10-13 18.16.31.excalidraw]]
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
$$\large\hat h_{w,b}\in argmin_{h\in H} \frac 1 m \sum_{i=1}^m(y_i-h(x_i))^2\ =\ \frac 1 m \sum_1^m(y_i-w^Tx_i+b)^2$$
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
$$\begin{align}
\nabla_wLs(w)&=-\frac 2 m \left(\sum_1^my_ix_i-\sum_1^m(x_ix_i^T)w\right)\\&=
-\frac 2 m \left(\sum_1^m\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}-\sum_1^m(\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}\begin{bmatrix}\cdot&\cdot&\cdot\end{bmatrix})\begin{bmatrix}\cdot\\\cdot\\\cdot\end{bmatrix}\right)\\
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

$L_S(w)=\frac 1 m \sum_1^m e_i^2=\frac 1 m E^T E=\large\frac 1 m [Y^TY-T^TXw-w^TX^TY+w^TX^TXw]$ 