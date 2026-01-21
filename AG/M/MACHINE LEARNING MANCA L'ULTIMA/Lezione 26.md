#ML-L26 [[Lezione 25]]
### Gaussian Mixture Model GMM for clustering
![[GMMforclustering|1000]]
- $k$ clusters
- $x\in\mathbb R^d$
- $P(x)=\sum^k_{j=1}\pi_j p_j(x)$
	- $1\ge\pi_j\ge 0$  dove $\pi_l$ è il numero di elementi di ogni cluster
	- $p_j=p(x_i|z_i=j)\sim\mathcal N(\mu_j,\Sigma_j)$ 
Il procedimento per trovare $x_i$ è campionare $z_i$ per poi campionare $x_i$ da $p(x_i|z_i)$ 

$$
\begin{align}
p(x_i)&=\sum^k_{j=1}p(x_i|z_i=j)p(z_i=j)\\
&=\sum_{j=1}^k p(x_i|z_i=j)\pi_j
\end{align}
$$
### Assumption
$\set{x_i}\in[m]$ 
$$
p(x_i)=\sum^k_{j=1}p(x_i|z_i=j)\pi_j\qquad (1)
$$
### Problem 1
Dato $\set{x_i}$ stimare i parametri del modello $(1)$ ovvero:
$$
\theta=\set{\mu_j,\ \Sigma_j,\ \pi_j,\ j=1\dots k}
$$
### Problem 2
Assumiamo che $\theta$ sia fissato e conosciuto, dato un nuovo datapoit  $x$ bisogna decidere a quale cluster appartenga

Dato $\theta$ è possibile calcolare per ogni $x$ 
$$
p(z=j|x)=\frac{p(x|z=j)p(z=j)}{p(x)}
$$
La soluzione del problema 1 si risolve con il maximum likelihood:
$$
\hat \theta_{ML}=\arg\max \underbrace{P_{\theta}(x_1,\dots,x_m)}_{\displaystyle\prod^m_{i=1}\underbrace{P_\theta(x_i)}_{\displaystyle=(1)}}
$$
Si vuole introdurre una procedura iterativa che produca la sequenza di estimator $\hat\theta^{(k)}$  in modo tale che:$$\lim_{k\to\infty} \hat\theta^{(k)}=\hat \theta_{ML}$$
	$$\frac{\log P_\theta(\underline x)}{m}=\frac1m\sum_{i=1}^m\log p_\theta(x_i)\quad\text{non so che sia}$$

Quello che troviamo non è convesso rispetto a $\theta$ e quindi si può trovare un massimo locale invece che globale

## EM-algorithm (expected maximization)
Dobbiamo migliorare ad ogni step
Si crea una stima di $\log p_\theta(x_1,z_1,\dots, x_m,z_m)$
$$
\begin{align}
Q(\ \theta,\hat\theta^{(k)})=\underbrace{E_{P_{\hat\theta^{(k)}}(\underline Z|\underline X)}
[\log p_\theta(X,Z)]}+c\qquad (2)\\
\sum^k_{z_1=1}\dots\sum^k_{z_m=1}\log p_\theta(x_1,z_1\dots x_m,z_m)\cdot p_{\hat\theta^{(k)}}(z_1|x_1)\dots p_{\hat\theta^{(k)}}(z_m|x_m)
\end{align}
$$
#### Gli step di questo algoritmo sono:
Inizializzazione di $\hat\theta^{(0)}$ fissata per $k=1,2\dots$ 
- Calcolo $Q(\theta,\hat\theta^{(k-1)})$ come in $(2)$    (Expectation step)
- $\hat \theta^{(k)}=\arg\max Q(\theta,\hat\theta^{(k-1)})$             (Maximization step)
![[EM algorithm]]


![[KL divergence (kulback lieber)#KL divergence (kulback lieber)]]![[KL divergence (kulback lieber)#Theorem]]
