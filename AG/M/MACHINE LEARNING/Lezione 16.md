#ML-L16
### Riassunto L15
- $\Large P_w[y|x]=\frac 1 {1+ {e^{-y\ \hat w^T_{}x}}}$

- $\hat w_{ML}=\arg\min_{\large w\in\mathbb R^d}\underbrace{-\frac 1m\sum_{i=1}^m\log \left({1+e^{-y_iw^Tx_i}}\right)}_{\large L_S(w)}$
- $L_S(w)$ è convessa
- Si trova $\hat w_{ML}$ usando gradient descend $w^{(k+1)}=w^{(k)}-\gamma_k\nabla_wL_S(w)$ 
- Dato $\hat w_{ML}$ usiamo l'Optimal Baies Classification Rule per fare una classificazione:$\hat y(x)=\arg\max_{j\in Y}P_w(y=j|x)$  nel caso binario basta guardare il segno di  $w^Tx$
### Estendiamo la Logistic Regression a multiclassification/non linear classification
$$y=\set{1\dots k}$$
Dati $\phi_1(x),\dots,\phi_k(x)$ sono i "punteggi" per ogni classificazione.
Li mappiamo nell'intervallo $[0,1]$ 
#### Definiamo un modello probabilistico (Soft Max)
$$P[y=j|x]=\frac{e^{\phi_j(x)}}{\sum^k_{i=1}e^{\phi_i(x)}}\in [0,1]\qquad  \text{SOFT MAX}$$
##### Esempio nel caso binario
- $k=2$ 
- $y\in\set{1,2}\to\set{-1,1}$ 
- $\phi_1(x)=w_1^Tx\qquad \phi_2(x)=w_2^Tx$

$\displaystyle P_w[y=1|x]=\frac {e^{w_1^Tx}}{e^{w_1^Tx}+e^{w_2^Tx}}\cdot \frac {e^{-w_1^Tx}}{e^{-w_1^Tx}}=\frac 1 {1+ {e^{-(w_1-w_2)^Tx}}}$
$\displaystyle P_w[y=2|x]=\frac {e^{w_2^Tx}}{e^{w_1^Tx}+e^{w_2^Tx}}\cdot \frac {e^{-w_2^Tx}}{e^{-w_2^Tx}}=\frac 1 {1+ {e^{+(w_1-w_2)^Tx}}}$
##### Esempio 3 classi

- $\Delta_{21}=w_2-w_1$
- $\Delta_{31}=w_3-w_1$
- $\Delta_{32}=w_3-w_2$ 

$\displaystyle P_w[y=1|x]=\frac {e^{w_1^Tx}}{e^{w_1^Tx}+e^{w_2^Tx}+e^{w_3^Tx}}=\frac 1 {1+ e^{\Delta_{21}^Tx}+e^{\Delta_{31}^Tx}}$
$\displaystyle P_w[y=2|x]=\frac {e^{w_2^Tx}}{e^{w_1^Tx}+e^{w_2^Tx}+e^{w_3^Tx}}=\frac 1 {1+ e^{-\Delta_{21}^Tx}+e^{\Delta_{32}^Tx}}$ 
#####
![[logisticRegin multiclass]]
	Il prof l'aveva fatta 2D ma ha detto che era 3D
### Gradient Descent (& Stochastic Gradient Descent)
Goal: data una cost function $J(w)$
Bisogna risolvere  $w=\arg\min_w J(w)$
![[fforgraddesc]]
Quando $J$ non è convessa non sappiamo quando siamo in un minimo locale o globale
L'update step-size generico è:
$$w^{(k+1)}=w^{(k)}-\gamma_k\nabla_wJ(w)|_{w=w^{(k)}}$$
#### Remark
- $J(w)\simeq J(w^{(k)})+\nabla_wJ(w-w^{(k)})$ 
- $J(w^{(k+1)}-w^{(k)})\simeq\nabla_wJ(\gamma_k\nabla_wJ)=-\gamma_k||\nabla_wJ||^2$  essendo negativo stiamo scendendo
[[Taylor]]
- $J(w)=J(w^{(k)})+\nabla_wJ(w-w^{(k)})+\frac 12 H_w(.)(w-w^{(k)})^2$
- $J(w^{(k+1)})-J(w^{(k)})=\underbrace{-{\cancel\gamma_k}\cancel{||\nabla_wJ||^2}+\frac 12\gamma_k^{\cancel2}H_w(.)\cancel{||\nabla_wJ||^2}}_{<0}$  
- $\frac 12 \gamma_kH_w(.)<1$
- $\gamma_k<\frac2{H(.)}$             possiamo dare un upper bound: $\gamma_k<\frac 2 M\quad M=\max H_w(.)$  

Quello che abbiamo fatto finora(Gradient Descend) nella pratica è inutile a causa della necessità di una quantità di dati spropositata. La versione stocastica è meglio.

Prendiamo una minipatch del data point $\mathcal B^{(k)}\subset\set{1\dots m}$ 
$J_{\mathcal B^{(k)}}=\frac 1{|\mathcal B^{(k)}|}\sum_{j\in\mathcal B^{(k)}}l(z_j,w)$ 
$w^{(k+1)}=w^{(k)}-\gamma_k\nabla_wJ(w)|_{w=w^{(k)}}$ 

#### Esempio grafico
- $w\in\mathbb R$ 
- $l(z,w)$ quadratica in $w$
- $J_w=\frac 1{m}\sum_{i=1}^ml(z_i,w)$
- $J_{\mathcal B^{(k)}}=\frac 1{|\mathcal B^{(k)}|}\sum_{j\in\mathcal B^{(k)}}l(z_j,w)$ 
![[graddescminibatch]]
dovrebbe essere come dovrebbe essere la nostra funzione avendo solo i campioni della minibatch

### Esempio perceptron

![[SGDperc]]
$$w^{(k+1)}=w^{(k)}+y_ix_i$$
Introduciamo una perdita per il perceptron.
Se $yw^Tx$ è negativo allora aumenta il costo.