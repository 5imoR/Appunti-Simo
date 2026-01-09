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
### E-step
#### I
$$\begin{aligned} Q(\theta,\hat{\theta}^{(k)}) &:= E_{p_{\hat{\theta}^{(k)}}(z|x)}[\log(p_{\theta}(x|z)p_{\theta}(z))] \\ &= E_{p_{\hat{\theta}^{(k)}}(z|x)} \left[ \sum_{i=1}^{m} \log(p_{\theta}(x_i|z_i)p_{\theta}(z_i)) \right] \\ &= \sum_{i=1}^{m} E_{p_{\hat{\theta}^{(k)}}(z_i|x_i)} [\log(p_{\theta}(x_i|z_i)p_{\theta}(z_i))] \\ &= \sum_{i=1}^{m} \left\{ \sum_{l=1}^{K} \log(p_{\theta}(x_i|z_i=l) \underbrace{p_{\theta}(z_i=l)}_{\Large\pi_l}) \underbrace{p_{\hat{\theta}^{(k)}}(z_i=l|x_i)}_{\Large w_{li}} \right\} \\ &= \sum_{i=1}^{m} \left\{ \sum_{l=1}^{K} \log(p_{\theta}(x_i|z_i=l)\pi_l)w_{li} \right\} \end{aligned}$$
Qui viene  definito $$
w_{li}=p_{\hat{\theta}^{(k)}}(z_i=l|x_i)
$$
#### II
Sfruttando il fatto che
$$

\log(p_{\theta}(x_{i}|z_{i}=l)) = \text{const} - \frac{1}{2}\log(\det(\Sigma_{l})) - \frac{1}{2}(x_{i}-\mu_{l})^{\top}\Sigma_{l}^{-1}(x_{i}-\mu_{l}) $$
Otteniamo:
$$
\begin{aligned}
Q(\theta,\hat{\theta}^{(k)}) &:= \text{const} - \frac{1}{2}\sum_{l=1}^{K}\log(\det(\Sigma_{l}))\sum_{i=1}^{m}w_{li} \\
& - \frac{1}{2}\sum_{l=1}^{K}\sum_{i=1}^{m}(x_{i}-\mu_{l})^{\top}\Sigma_{l}^{-1}(x_{i}-\mu_{l})w_{li}\\&+ \left\{\sum_{l=1}^{K}\log(\pi_{l})\sum_{i=1}^{m}w_{li}\right\}
\end{aligned}
$$
#### III
Osserviamo che
$$
\begin{aligned}
\Large
&w_{li} := p_{\hat{\theta}^{(k)}}(z_{i}=l|x_{i}) = \frac{\overbrace{p_{\hat{\theta}^{(k)}}(x_{i}|z_{i}=l)}^{\displaystyle\mathcal{N}(\hat{\mu}_{l}^{(k)}, \hat{\Sigma}_{l}^{(k)})}\overbrace{p_{\hat{\theta}^{(k)}}(z_{i}=l)}^{\displaystyle \hat{\pi}_{l}^{(k)}}}{\sum_{j=1}^{K} p_{\hat{\theta}^{(k)}}(x_{i}|z_{i}=j)p_{\hat{\theta}^{(k)}}(z_{i}=j)}
\end{aligned}
$$
### M-Step
#### $\pi_l$ 
Per massimizzare  w.r.t. $\pi_l$ stando al vincolo $\sum^k_{l=1}\pi_l=1$ usiamo i Lagrange multipliers
$$
\Lambda(\theta, \lambda) =Q(\theta,\hat{\theta}^{(k)})+\lambda\left(\sum^k_{l=1}\pi_l-1\right)
$$
imponiamo a zero le derivate parziali:
$$
\frac{\partial\Lambda(\theta, \lambda) }{\partial \pi_l}=\frac 1 {\pi_l}\sum^m_{i=1}w_{li}+\lambda=0
$$
che sotto la condizione $\sum^k_{l=1}\pi_l=1$ ha un unica soluzione:
$$
\hat\pi_l^{(k+1)}=\frac{\sum^m_{i=1}w_{li}}{\sum^K_{j=1}\sum^m_{i=1}w_{ji}}=\frac 1m\sum^m_{i=1}w_{li}
$$
#### $\mu_l$
Similmente w.r.t. $\mu_l$ otteniamo:
$$
\frac{\partial\Lambda(\theta, \lambda) }{\partial \mu_l}=\sum_l^{-1}\sum_{i=1}^m(x_i-\mu_l)w_{li}=0
$$
che ammette un unica soluzione:
$$
\hat\mu_l^{(k+1)}=\frac{\sum^m_{i=1}x_iw_{li}}{\sum_{i=1}^mw_{li}}
$$
#### $\Sigma_l$
Infine è possibile mostrare che la soluzione di $\Sigma_l$ è data da l'equazione:
$$
\begin{aligned}
\hat{\Sigma}_{l}^{(k+1)} = \frac{\sum_{i=1}^{m} w_{li} (x_{i} - \hat{\mu}_{l}^{(k+1)})(x_{i} - \hat{\mu}_{l}^{(k+1)})^{T}}{\sum_{i=1}^{m} w_{li}}
\end{aligned}
$$
#### Conclusioni
- $\Sigma_l=\Sigma_l^T>0$
- $\pi_l\ge 0 \sum_{l=1}^k\pi_l=1$
Una volta calcolato $w_{li}$ si può calcolare tutto il resto
E' un metodo che converge lentamente, ma è poco costoso
Non è presente un tuning parameter
Può accadere che si finisca in un punto di massimo locale/globale che non riguarda il punto di partenza
![[Drawing 2026-01-09 11.19.22.excalidraw]]
non è perfetto ma per dare un idea


# Principal Component Analysis
![[Drawing 2026-01-09 11.29.14.excalidraw|300]]
- $x_i\in\mathbb R^d\quad d=2$
- $i=1\dots m\quad m=11$
- ${\Large\color{#1971c2}\bullet} \equiv \hat x_i$    
Immaginiamo di avere un immagine $I(t)\in\mathbb R^{200\times 300}\quad t\in[1,300]$  
se $x(t)=\text{vectorization }(I(t))\qquad x(t)\in\mathbb R^{200\times 300}$ 
