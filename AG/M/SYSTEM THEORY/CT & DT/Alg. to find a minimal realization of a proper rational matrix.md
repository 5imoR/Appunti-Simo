## Alg
$W(s)\in\mathbb R^{p\times m}(s)$

#### Step 1
Trova $D=\lim_{s\to\infty} W(s)$ e settiamo $W_{sp}\triangleq W(s)-D$ 
#### Step 2
Rappresenta $\displaystyle W_{sp}(s)=\frac 1{d(s)}N(s)$ dove:
- $d(s)\in\mathbb R[s]$  è un [[Monic polynomial]] (scalare) con $\deg d(s)=n$ 
- $N(s)=B_0+B_1(s)+\dots B_{n-1}s^{n-1}\in\mathbb R[s]^{p\times m}$
Se $m<p$ scegliamo una reachable realization $\Sigma(F,G,H)$ di dimensione $n\times m$ 
Se $m>p$ scegliamo una observable realization $\Sigma(F,G,H)$ di dimensione $n\times p$ 
Se $m=p$ scegliamo una delle due realization
#### Step 3
Se $\Sigma$ è una reachable realization controlla se è anche osservabile
- Se è così è minima, altrimenti  la si riduce in [[SOF Standard Observability Form]] ottenendo $\Sigma_1 =(F_11,G_1,H_1)$ observable
- [[Alg. to find a minimal realization of a proper rational matrix#Proof|è anche possibile provare]] che  $\Sigma_1$ rimane reachable $\Rightarrow\Sigma_1$ è una minimal realization

Se $\Sigma$ è un observable realization si fa l'analogo osservando che sia anche reachable




## Proof
Vogliamo provare che se $\Sigma=(F,G,H)$ è reachable allora l'observable subsystem $\Sigma_1=(F_{11},G_1,H_1)$ ottenuto dalla SOF nel terzo step è ancora reachable.
$$
\begin{align}
&rank\ 
\begin{bmatrix}
G_1 & F_{11}G_1 & F_{11}^2G_1 & \dots & F_{11}^{n-1}G_1 \\
G_2 & * & * & \dots & * \\
\end{bmatrix}
\begin{array}{c}
\}\rho\ \ \ \ \ \ \ \\
\}n-\rho
\end{array}=n\\
&\Rightarrow rank\ \begin{bmatrix}
G_1 & F_{11}G_1 & F_{11}^2G_1 &\dots& F_{11}^{\rho-1}G_1  &\dots & F_{11}^{n-1}G_1 \\
\end{bmatrix}=\rho\\
\text{Hemilton}&\Rightarrow rank\ \begin{bmatrix}
G_1 & F_{11}G_1 & F_{11}^2G_1 &\dots& F_{11}^{\rho-1}G_1  \\
\end{bmatrix}=\rho\\
&\Rightarrow (F_{11},G_1)\text { is reachable}
\end{align}
$$
