[[FCA]]


# Ripasso

![[Cloesed Loop#Closed System]]

---
#ST-L1
##### Esempio (Mass Spring Dumper Model)

| ![[carE]] | Una buona rappresentazione di una macchina.<br>Serve usare gli State Space Models per modellare e controllare<br> |
| --------- | ----------------------------------------------------------------------------------------------------------------- |
## Ripasso di State Space Models a tempo discreto
Sono definiti dalla seguente equazione differenziale:
$$
\begin{align}
&\begin{cases}
x(t+1)&=Fx(t)+Gu(t) &State\ equation  \\
y(t)&=Hx(t)+Du(t)   &Output\ equation\\
\end{cases}
\\\\
&x(t)\in \mathbb{R}^n\triangleq X\qquad is\ the\ state\ variable\\
&u(t)\in \mathbb{R}^m\triangleq U\qquad is\ the\ input\\
&y(t)\in \mathbb{R}^p\triangleq Y\qquad is\ the\ output\\
\end{align}
$$
Il sistema può essere rappresentato in maniera compatta come:
$$
\Sigma=(F,G,H,D)
$$
E per dimensione di $\Sigma$ si intende la dimensione della state variable ovvero $n$
$\Sigma$ è:
- Linear
- Time Invariant (lo consideriamo dinamico da $t=0,\quad t\in \mathbb{Z}$)
- Proper

In caso $D=0$ ($D$ è la FeedForward Matrix) il sistema è "Strictly Proper" e per semplicità lo scriveremo:
$$
\Sigma=(F,G,H)
$$
![[BlockDiagramOfDTSSM|600]]
- $F\in R^{n\times n}$ State Matrix
- $G\in R^{m\times m}$ Input Matrix
- $H\in R^{p\times n}$ Output Matrix
- $D\in R^{p\times m}$ Feedforward Matrix

Il polinomio caratteristico di $F$ è $\triangle_F(Z)\triangleq det(zIm-F) = z^n+a_{n-1}z^{n-1}+...a_1\ z\in \mathbb{R}[z]$ 

Un polinomio si dice *monic* se il coefficiente di $z^n$ è $1$ 

Il grado(degree) del polinomio è $deg\triangle_F(z)=n$ 

Gli zeri di $\triangle_F(z)$ sono gli autovalori della matrice $F$
Se prendiamo gli autovalori distinti di $F$ come $\lambda_1,\lambda_2...\lambda_r\in \mathbb{C}$ allora avremo:
$$
\triangle_F(z) = (z-\lambda_1)^{n1}(z-\lambda_2)^{n2}...(z-\lambda_r)^{nr}
$$
Dove $n1, n2,...,nr$ sono interi positivi chiamati molteplicità algebrica di $\lambda_1,\lambda_2...\lambda_r$ 


### Espressione di *state and output* ad un tempo generico $t>0$

$$
\begin{align}
x(t) &= 
\underbrace{F^t x(0)}_
{\text{unfroced/free state evolution }x_l(t)} + 
\underbrace{\sum_{k=0}^{t-1} F^{t-1-k} G u(k)}_
{\text{forced state evolution}x_f(t)} \\
y(t) &=
\underbrace{H F^t x(0)}_{\text{unforced/free output evolution }y_l(t)}  + \underbrace{\sum_{k=0}^{t-1} HF^{t-1-k}Gu(k)+Du(t)}_{\text{forced output evolution}y_f(t)}
\end{align}
$$
--- 
#ST-L2

## Impulse response
Unitary Discrete Time Inpulse (Kronecker delta)

| $\delta(t)\triangleq\begin{cases}1\qquad t=0\\0\qquad t\neq0\end{cases}$          | ![[dirac\|200]]   |
| --------------------------------------------------------------------------------- | ----------------- |
| $\delta_{-1}(t)\triangleq\begin{cases}0\qquad t<0\\1\qquad t\geq0\end{cases}$<br> | ![[dirac-1\|200]] |
nel caso di $\delta_{-1}(t)\rightarrow W(t)\triangleq D\delta(t)+HF^{t-1}G\delta_{-1}(t-1)$
#### Caso m=1 (m=numero di inpulsi)
${\color{orange}{x(0)=0}}\quad u(t)=\delta(t)$
$$
\begin{align}

&y(0)={\color{orange}{\cancel{Hx(0)}}}+Du(0)=D\\\\
&x(1)={\color{orange}{\cancel{Fx(0)}} }+Gu(0)=\color{lightgreen}G\\
&y(1)=H{\color{lightgreen}x(1)} +\cancel{Du(1)}=HG
\\\\
&x(2)=F{\color{lightgreen}x(1)}+\cancel{Gu(1)}={\color{lightblue}FG}\\
&y(2)=H{\color{lightblue}x(2)} +\cancel{Du(2)}=HFG
\\\\
\end{align}
$$
In generale:
$$
y(t)=
\begin{cases}
D\qquad\qquad t=0\\
HF^{t-1}G\quad t\geq1
\end{cases}
$$

#### Caso m>1
${x(0)=0}\quad u(t)=e_i\delta(t)$
dove $e_i$ è l'$i$ esimo vettore della base canonica $e_2=\begin{bmatrix}0\\1\\0\end{bmatrix}$ 
$$
y(t)=
\begin{cases}
De_i=col_i(D)\qquad\qquad\qquad\quad\ \ t=0\\
(HF^{t-1}G)e_i=col_i(HF^{t-1}G)\quad t\geq1
\end{cases}
$$
$\Rightarrow W(t)\triangleq D\delta(t)+HF^{t-1}G\delta_{-1}(t-1)$ 


*what?*
Richiamando la convoluzione di due sequenze a tempo discreto:
$$
t\in \mathbb{Z}:[V_1+V_2](t)\triangleq\sum_{k=0}^tV_1(t-k)V_2(k)\qquad t\in\mathbb{Z}
$$
possiamo vedere che:
$$
\begin{align}
y_F(t)&\triangleq[W+u](t)=\sum_{k=0}^t W(tk)u(k)\\
&\triangleq\sum_{k=0}^{t-1}W(t-k)u(k)+W(0)u(t)
\end{align}
$$


