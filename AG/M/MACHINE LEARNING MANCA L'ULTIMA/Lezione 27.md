#ML-L27
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

$\hat x_i\simeq x_i$ 
$\hat x_i = V\alpha_i\qquad V\in\mathbb R^{d\times k}\quad k<<d$ 
Nell'esempio del disegno si ha $k=1\quad d=2\quad V=v_1\in \mathbb R^d=\mathbb R^2$ 
Quello che dobbiamo fare matematicamente è trovare $V$ e $\alpha_i\quad i\in[m]$ 
tali che vadano a minimizzare:
$$\frac 1m \sum^m_{i=1}||x_i-V\alpha_i||^2\qquad \alpha_i\in\mathbb R^k$$

Immaginiamo di avere un immagine $I(t)\in\mathbb R^{200\times 300}\quad t\in[1,300]$  
se $x(t)=\text{vectorization }(I(t))\qquad x(t)\in\mathbb R^{200\times 300}$ 
