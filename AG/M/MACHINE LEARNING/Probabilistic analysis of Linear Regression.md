#ML-L10
![[Linear Model#Regression# Linear Regression]]

Inoltre abbiamo le assunzioni probabilistiche sull'errore: **ASS1**
![[Perturbation analisys of linear LS Problems#Probabilistic analysis#Assunzioni probabilistiche su E]]

Aggiungiamo un altra assunzione:  **ASS2**
- $\displaystyle e_i\sim \mathcal N(0,\sigma^2)\left(\frac 1 {2\pi\sigma^2}\right)^m\exp\left\{-\frac 1 2\frac{e^2}{\sigma^2}\right\}$  
#### Recall
$P[A_1,A_2]=P[A_1\cap A_2]=A_1\ AND\ A_2=P[A_1]P[A_2]$ 
####
$\displaystyle p(e_1,\dots,e_m)=\prod_{i=1}^m p(e_i)=$$\displaystyle\left(\frac 1 {2\pi\sigma^2}\right)^m\exp\left\{-\frac 1 2\frac{e^2}{\sigma^2}\right\}$  


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
####


