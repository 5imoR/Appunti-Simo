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
![[OCF Observable Canonical Form#Theorem OCF]]

$T=(S^{-1})^T$ 
##### 3 Standard Observability Form SOF
![[SOF Standard Observability Form#Theorem SOF]]
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

C'è una relazione tra  controllability e reconstructasbility? Nel caso DT, dato che in CT sono già la stessa cosa
$$
\begin{align}
(F,H) \text{ is reconstractable}&\iff \ker F^n\supseteq\ker \mathcal O\\
&\phantom{ssssss}\Updownarrow\\
Im\ (F^T)^n\subseteq Im\ \mathcal O^\perp=Im\ \mathcal R_d&\iff (\ker F^n)^\perp\supseteq(\ker \mathcal O)^\perp\\
\Updownarrow\phantom{sssssssssss}\\
(F^T,H^T) \text{ is controllable}
\end{align}
$$
Quindi in breve abbiamo che:
$$(F,H) \text{ is reconstractable}\iff(F^T,H^T) \text{ is controllable}$$

$$
W_d(s)=G^T(sI-F^T)^{-1}H^T\equiv[H(sI-F)^{-1}G]^T=W(s)^T
$$
