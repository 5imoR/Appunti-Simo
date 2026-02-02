#ML-L19[[Lezione 18 OAROS alg]]
## Ridge Regression 
### Lin. Reg. with quadratic loss & $e^2$ regularization
Abbiamo:
$H=\set{h_w(x):h_w(x)=w^Tx,w\in \mathbb R^d}$ 
$\hat W_R=\hat w_{RR}=\arg\min_{w\in\mathbb R^d}\underbrace{\frac 1m ||Y-Xw||^2}_{L_S(w)}+\lambda\underbrace{||w||^2}_{\sum^d_{i=1}w_i^2}$ 
Se si prende un $\lambda$ troppo grande è come non andare a guardare i dati.

La soluzione è:

$$\hat W_R  =\left(\frac{X^TX}m+\lambda I\right)^{-1}\frac{X^TY}m=\left(\frac{X^T}{\sqrt{m}}\frac X{\sqrt{m}}+\lambda I\right)^{-1}\left(\frac X{\sqrt{m}}\right)^T\frac Y{\sqrt{m}}$$  Questo è stato introdotto per evitare overfitting. Se il sistema è stabilem non c'è overfit 
	(vuol dire che in presenza di perturbazioni sul dataset non ci sono grandi differenze nel risultato) 
- $\sqrt m$ è detto normalization term



[[SVD Singular Value Decomposition]]
$$
\begin{align}
\frac X{\sqrt{m}}&=USV^T\\
\hat W_R&=\left[VS\cancel U^T \cancel USV^T+\lambda I\right]^{-1}VSU^T\frac Y{\sqrt{m}}\\
&=V[S^2+\lambda I]^{-1} \cancel V^T\cancel VSU^T \frac Y{\sqrt{m}}\\
&=V[(S^2+\lambda I)^{-1}S]U^T \frac Y{\sqrt{m}}\\
&=[v_1\cdots v_d]\begin{bmatrix}
{\Large\frac{\sigma_1}{\sigma_1^2+\lambda}}\\
&\ddots\\&&{\Large\frac{\sigma_d}{\sigma_d^2+\lambda}}
\end{bmatrix}
\begin{bmatrix}
u_1^T\\\vdots\\u_d^T
\end{bmatrix}\frac Y{\sqrt m}\\\\\\
&=\Large\sum_{i=1 }^dv_i{\frac{\sigma_i}{\sigma_i^2+\lambda}}u_i^T\frac Y{{\sqrt{m}}}
\end{align}
$$

[[9 Perturbation analisys of linear LS Problems#Deterministic worst case perturbation analysis]] 

$$
\max {\Large
\frac{\frac{||\Delta w||}{||\hat w||}}{\frac{||\Delta Y||}{||Y||}}}=\frac{\max{\Large\frac{\sigma_i}{\sigma_i^2+\lambda}}}{\min{\Large\frac{\sigma_i}{\sigma_i^2+\lambda}}}
$$
### Proposition (Proof nel book)
Per $\hat W_R$ trovato con la R.R. con il *regression parameter* $\lambda$
	$\hat w_R$ è il regression estimator
$\displaystyle E[L_D(\hat w_R(\lambda))-L_S(\hat w_R(\lambda))]\simeq -\frac 1 {\lambda m}$ 

#### Come scegliamo $\lambda$?
$$
L_D(\hat w_R(\lambda))={\color{lightgreen}L_D(\hat w_R(\lambda))-L_S(\hat w_R(\lambda))}+{\color{orange}L_S(\hat w_R(\lambda))}
$$
![[chooselambda|700]]
$\textcolor{cyan}{■}$ Valore effettivo

L'empirical error è $\hat w_R(\lambda)=\arg\min_w {\color{orange}L_S(\hat w_R(\lambda))}$  non sono sicuro
$\lambda_{opt}$ è il valore ottimale ma è necessario conoscere $L_D$ per sapere il valore

#### Idea
Usiamo Validation data per trovare una stima del true risk $\hat L_D(\hat w_R(\lambda))$
$\hat \lambda_{opt}=\arg\min_\lambda \hat L_D(\hat w_R(\lambda))$ 

## K-Fold Cross Validation
![[kfold]]
- $S_i$ è chiamato fold
- $S^{i}$ è quello che manca di S
- ci sono $k$ fold solitamente $5,10, m$ 
	nel caso di $m$ si tratta di Leave One Out

- $\bigcup^k S_i=S$
- $S_i\cap S_j=\emptyset$
- $S^{(i)}\cup S_i=S$
- $S^{(i)}\cap S_i=\emptyset$ 

