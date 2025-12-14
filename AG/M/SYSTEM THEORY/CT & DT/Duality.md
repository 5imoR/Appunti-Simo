#ST-L27-2
### Definition \[Dual]
Dato un ssm  n-dimensionale $\Sigma =(F,G,H)$ con:
- $m$ input 
- $p$ output 
Definiamo il suo duale $\Sigma_d$ come l' ssm n-dimensionale con:
- $p$ input 
- $m$ output
descritto come segue: $\Sigma_d=(F^T,H^T,G^T)$

**NOTE**
Se si calcola $(\Sigma_d)_d=\Sigma$ 

|                         | $\Sigma$                                                             | $\Sigma_d$                                                                             |
| ----------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Reachability<br>Matrix  | $\mathcal R=[G\|FG\|\dots\|F^nG]$                                    | $\mathcal R_d=[H^T\|F^TH^T\|\dots\|(F^T)^{n-1}H^T]$                                    |
| Observability<br>Matrix | $\mathcal O=\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k \end{bmatrix}$ | $\mathcal O_d=\begin{bmatrix} G^T \\ G^TF^T \\ \vdots \\ G^T(F^T)^{n-1} \end{bmatrix}$ |

- $\mathcal R_d=\mathcal O^T$  
- $\mathcal O_d = \mathcal R^T$
Di conseguenza:
#### 1
$$
\begin{align}
\Sigma \text{ is observable}&\iff rank\ \mathcal O=n\\
&\phantom{ssssss}\Updownarrow\\
\Sigma_d \text{ is reachable}&\iff rank\ \mathcal R_d=n
\end{align}
$$
#### 2
$$
\begin{align}
\Sigma \text{ is reachable}&\iff rank\ \mathcal R=n\\
&\phantom{ssssss}\Updownarrow\\
\Sigma \text{ is observable}&\iff rank\ \mathcal O_d=n
\end{align}
$$
####
La prima di queste due relationships ha diverse conseguenze: $\forall s\in \mathbb C$ 
##### 1
$$
\begin{align}
\Sigma \text{ is observable}&\iff (F^TH^T)\text{ is reachable}\\
&\phantom{ssssss}\Updownarrow \small PBH\\
rank\begin{bmatrix}sI-F \\H \\\end{bmatrix}=n
&\iff rank \begin{bmatrix} sI-F^T & H^T \end{bmatrix}=n
\end{align}
$$

##### 2 Observable Canonical Form OCF
$T=(S^{-1})^T$ 
$$
\begin{align}
\begin{array}{c}
(F,H)\text{ with }H\in\mathbb R^{1\times n} \text{ is observable}\\
\text{(single output system)}
\end{array}
&\iff 
\begin{array}{c}
(F^T,H^T)\text{ is reachable}\\
\text{(single input system)}
\end{array}\\
\Updownarrow\qquad \qquad\qquad & \qquad\qquad\qquad\qquad\Updownarrow\\
\begin{array}{c}
\exists T\in \mathbb R^{n\times n} \text{ non sing. s.t.}\\
\text{observable canonical form}\\
\small T^{-1}FT=
\begin{bmatrix}
0 &  &  & -a_0 \\
1 &  &  & -a_1 \\
 & \ddots &  & \vdots \\
 &  & 1 & -a_{n-1} \\
\end{bmatrix}\\
\small HT=\begin{bmatrix} 0 & \dots & 0 & 1 \end{bmatrix}
\end{array}
&\iff
\begin{array}{c}
\exists S\in \mathbb R^{n\times n} \text{ non sing. s.t.}\phantom{sssssssssssssssssss}\\
\text{controllable canonical form}\phantom{sssssssssssssssssss}\\
\small S^{-1}F^TS=
\begin{bmatrix}
0 & 1 &  &  \\
 &  & \ddots &  \\
 &  &  & 1 \\
-a_0 & -a_1 & \dots & -a_{n-1} \\
\end{bmatrix}
S^{-1}H^T=\begin{bmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}
\end{array}
\end{align}
$$
##### 3 Standard Observability Form SOB
$T=(S^{-1})^T$ 
$$
\begin{align}
\begin{array}{c}
(F,H)\text{ is not}\\
\text{observable}
\end{array}
&\iff
\begin{array}{c}
(F^T, H^T)\text{ is not}\\
\text{reachable}
\end{array}\\
&\phantom {ssssssssss}\Updownarrow\\
\begin{array}{c}
\exists T\in \mathbb R^{n\times n} \text{ non sing. s.t.}\\
\small
T^{-1}FT=\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}\\
\small HT=\begin{bmatrix}H_1&0\end{bmatrix}\\
\text{with $(F_{11}, H_1)$ observable}
\end{array}
&\iff
\begin{array}{c}
\exists S\in \mathbb R^{n\times n} \text{ non sing. s.t.}\\
\small S^{-1}FS=\begin{bmatrix}F_{11}^T&F_{12}^T\\0& F_{22}^T\\\end{bmatrix}
\small S^{-1}H^T=\begin{bmatrix}H_1^T\\0\end{bmatrix}\\\\
\text{with $(F_{11}^T, H_1^T)$ reachable}
\end{array}
\end{align}
$$
####   Standard Observability Form SOB
Supponiamo di avere il sistema $\Sigma = (F,G,H)$ in SOF
$$
\begin{align}
 F=\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}
\begin{array}{c}\}\rho\phantom{ssss} \\\}n-\rho\end{array}
\qquad
 G=\begin{bmatrix}G_1\\ 0\end{bmatrix}
\begin{array}{c}\}\rho\phantom{ssss} \\\}n-\rho\end{array}
\qquad 
 H=\begin{bmatrix}H_1& 0\end{bmatrix}\ \}p\quad\text{ with $(F_{11},H_1)$ observable}\\
\underbrace{}_\rho\underbrace{}_{n-\rho}\phantom{sssssssssssssssss}\underbrace{}_{m}\phantom{ssssssssssasssss}\underbrace{}_\rho\underbrace{}_{n-\rho}\phantom{sssssssssaasssssssssssssssss}
\end{align}
$$
####
Assumiamo  $x(t)=\begin{bmatrix}x_1(t)\\ x_2(t)\end{bmatrix}\begin{array}{c}\}\rho\phantom{ssss} \\\}n-\rho\end{array}$ 
Se  $\Sigma$ è in CT le sue equazioni diventano:
- $\dot x_1(t)=F_{11}x_1{t}+G_1u(t)$ 
- $\dot x_2(t)= F_{21}x_1(t)+F_{22}x_2(t)+G_2u(t)$
- $y(t)=H_1x_1(t)$ 
![[AdvancedBDofCT|1200]]
$\Sigma_{no}$ non ha alcun effetto sull'output
$$
W(s)= H(sI-F)^{-1}G\equiv W_o(s)=H_1(sI-F_{11})^{-1}G_1
$$
