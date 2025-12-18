#ML-L23 
## SVM as regularized ERM
se $y_i(w^Tx_i+b)\ge1\Rightarrow \xi_i=0$
se $y_i(w^Tx_i+b)\le1\Rightarrow \xi_i=\underbrace{1-y_i(w^Tx_i+b)}_{ei}$ 
$\xi_i=\max(0,e_i)$
$$(\hat w,\hat b)=\arg \min \frac 1{2\color{orange}m\lambda}||w||^2+\underbrace{\frac{\cancel\lambda}{\color{orange}m\cancel\lambda}\sum_{i=1}^m\max(0,1-y_i(w^Tx_i+b))}_\text{empirical risk}$$
### Hinge Loss
$$
	(\hat w,\hat b)=\arg \min_{w,b} \frac 1m\sum^m_{i=1}\underbrace{l(w,b,z_i)}_{\max(0,e_i)}+\underbrace\gamma_{\frac 1{2m\lambda}}||w||^2
$$

## From linear SVM to non linear SVM
L'idea di base è mappare gli input:
dati $\varphi_i(x)$
$$
x\in\mathbb R^d\to z\in\mathbb R^k\qquad z=\Phi(x)=\begin{bmatrix} \varphi_1(x) \\ \vdots \\ \varphi_k(x) \end{bmatrix}
\quad k>>d
$$
#### Example
$$
\begin{cases}
[z]_1=[x]_1^2+[x]_2^2&=\varphi_1(x)\\
[z]_2=\angle x&=\varphi_2(x)
\end{cases}
$$
![[change basis|600]]

Una volta che la trasformazione è stata computata è possibile fare SVM lineare nello spazio $Z$ 
$\Rightarrow h_{wb}(z)=w^Tz+b\quad \equiv \quad h_{wb}(x)w^T\phi(x)+b$ 
#### Recall
- $\displaystyle\hat\mu_i=\arg\max_{\substack{\mu_i\ge 0\\\exists \sum \mu_iy_i=0}}\sum_{i=1}^m \mu_i-\frac 12\sum^m_{i,j=1} \mu_i\mu_j\ y_iy_j\ {\color{lightgreen}z_i^Tz_j}$
	- se $\phi$ è dato allora abbiamo $<\phi(x_i),\phi(x_j)>$ al posto di $<z_i,z_j>$
	- in alternativa  può diventare $k(x_i,x_j)$ (guarda sotto)
- $\displaystyle h_w,b(z)=\underbrace{\sum_{i=1}^m\hat \mu_iy_i z_1^T}_{\hat w^T} z+\hat b$ 
#### Example
$x\in \mathbb R$
$$
\phi(x)=\begin{bmatrix} 1 \\ \sqrt2x \\ x^2 \end{bmatrix}\qquad
<\phi(x'),\phi(x)>=
\begin{bmatrix} 1 & \sqrt2x' & x'^2 \end{bmatrix}
\begin{bmatrix} 1 \\ \sqrt2x \\ x^2 \end{bmatrix}
=1+2xx'+x^2x'^2
$$
Polinomial kernel of degree 2
$$
(1+x'x)^2
$$
#### Example
- Linear Kernel:  $k(x,x')=1+x'x =\phi^T(x)\phi(x')=\begin{bmatrix} 1 & x \end{bmatrix}\begin{bmatrix} 1 \\ x'\end{bmatrix}$ 
- Gaussian Kernel:$\displaystyle k(x,x')=\exp\left\{-\frac{(x-x')^2}\gamma\right\}$ 
$$
\begin{align}
\exp\left\{-\frac{(x-x')^2}\gamma\right\}&=
\exp\left\{-\frac{x^2}\gamma\right\}\cdot
\exp\left\{\frac{2xx'}\gamma\right\}\cdot
\exp\left\{\frac{x'^2}\gamma\right\}\\
&=\sum_{k=0}^{+\infty}\underbrace{\exp\left\{-\frac{x^2}\gamma\right\}
\frac{({\sqrt 2x})^k}
{\sqrt{k!}\sqrt{\gamma^k}}}_{\phi_k(x)}
\underbrace{\exp\left\{\frac{x'^2}\gamma\right\}
\frac{({\sqrt 2x'})^k}
{\sqrt{k!}\sqrt{\gamma^{k-1}}}
}_{\phi_k(x')}
\end{align}
$$
$$
\exp\left\{\frac{2xx'}\gamma\right\}=\sum_{k=0}^{+\infty}\frac{(\frac{2xx'}{\gamma})^2}{k!}=
\sum_{k=0}^{+\infty}
\frac{({\sqrt 2x})^k}
{\sqrt{k!}\sqrt{\gamma^k}}
\frac{({\sqrt 2x'})^k}
{\sqrt{k!}\sqrt{\gamma^{k-1}}}
$$
Slide sulle reti neurali