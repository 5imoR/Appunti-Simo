# Neural Network

### Neuron
![[neuron|300]]
Come funnziona:
ad ogni valore del mio dato $x\in\mathbb R^d$ viene associato un peso $w$ ed il neourone ne calcola il risultato tramite l'activation function.
$$
y=\sigma(w^T,x)=\sum^d_{i=1}w_i[x]_i\ +w_{d+1}
$$
#### Activation Function

![[activation function| 800]]

### One hidden layer perceptron
![[HiddenLayer]]
Si ha uno strado di neuroni (Hidden Layer) che per ogni neurone tiene conto di tutti i neuroni del livello precedente moltiplicati per il loro peso.
Il risultato si ottiene prendendo i valori dell' ultimo livello e unendoli insieme.
$$
y=\underbrace{\sum^N_{i=1}\alpha_i\sigma\left(\sum^d_{j=1}w_{ij}[x]_j+w_{i,d+1}\right)+\alpha_{N+1}}_{\large h_\theta(x)}
$$
$\theta$ è l'insieme di tutti gli $w_{ij}$ e gli $\alpha_i$  con $i\in[1,N+1]\quad j\in[1,d+1]$ 

## NN for Regression
Dati:
- training data $(x_i,y_i)\quad i\in[m]$
- loss funtion $l(\theta,z)$ per esempio $(y-h_\theta(x))^2$  ci calcoliamo $\theta$ come:
$$
\hat \theta =\arg\min\frac 1m\sum^m(y-h_\theta(x))^2
$$


## NN for Binary Classification
$$
\begin{align}
P(y=1|x) &= \frac{e^{h_{\theta}(x)}}{e^{h_{\theta}(x)} + e^{-h_{\theta}(x)}}\\
&\simeq\frac{1}{1 + e^{-h_{\theta}(x)}}
\end{align}
$$
![[regressionNN|200]]
## SGD
Serve aggiornare i pesi per correggere gli errori, per fare ciò si va ad usare l'SGD (GD troppo costoso) andando a ritroso per aggiornarli
$$
\begin{align}
\hat \theta^{(k+1)}=\hat\theta^{(k)}-\gamma\nabla L_S(\theta)\\
\\
\nabla L_S(\theta)=\frac 1{|B^{(k)}|}\sum_{i\in B^{(k)}}\nabla_\theta(y_i-h_\theta(x_i))^2
\end{align}
$$
Prendiamo il caso dell' online GD($|B|=1$) si ha:
$$
\nabla L_S(\theta)=-2\underbrace{(y_i-h_\theta(x_i))^2}
_\text{error}
\underbrace{\nabla_\theta h_\theta(x_i)}
_\text{Jacobian}
$$
$$
\nabla_\theta h_\theta(x_i)=
\begin{bmatrix}
\frac{\partial h}{\partial\alpha_i}\\\vdots\\\frac{\partial h}{\partial w_{ij}}\\\vdots
\end{bmatrix}\qquad \frac{\partial h}{\partial\alpha_i}=\sigma\left(\sum^\alpha_{j=1}w_{ij}[x]_j+w_{i,N+1}\right)
$$
Fortunatamente lui vuole che capiamo il meccanismo e non i conti.
Quello che ho capito:
Partendo da $x$ si passa ad ogni neurone tutti gli "attributi" di $x$. Ogni neurone restituisce un valore moltiplicato per un peso $w_{ij}$ che viene dato in pasto ai neuroni del livello sucessivo.Questo si ripete fino all'ultimo livello che viene raggruppato da un singolo neurone che ci restituisce il risultato. Basandoci sull'errore  del risultato si fa il procedimento a ritroso andando a modificare i pesi dei neuroni che hanno causato l'errore. Noi usiamo una versione stocastica e infatti non usiamo tutti i neuroni contemporaneamente ma una minibatch.
## Reinforcement Learning
Stessa cosa fatta a Fondamenti di IA.
L'agente effettua delle azioni e viene premiato di conseguenza.

## Unsupervised Learning
Ha due problemi principali:
- clustering: è necessario avere dei gruppi di dati simili tra loro
	un esempio funzionante possono essere i numeri o le lettere dato che sono sempre quelle
	- k-means clustering
	- Gaussian mixture models
- dimensionality reduction: possiamo raggruppare i dati in uno spazio di dimensione minore se questo equivale ad una buona approssimazione.
### Clustering
#### K-means
Dati:
- $x_i\in\mathbb R^d\quad i\in[m]$
- $k=$ numero di cluster/gruppi
- $d(x,x')\equiv$ funzione della distanza
	un esempio è $||x-x'||^2$
Obbiettivo:
Trovare:
- $\mu_1\dots\mu_k$ (cluster centers)
- $\mathcal C_1\dots \mathcal C_k$ clusters
con $\mathcal C_i\cap\mathcal C_j=\emptyset\qquad \mathcal C_1\cup\dots\cup\mathcal C_k=\set{x_1\dots x_m}$  
s.t.:
$$\frac 1m\sum^k_{j=1}\sum_{x_i\in\mathcal C_j}d(x_i,\mu_j)$$

![[clustering|1000]]
- si scelgono i cluster center a caso 
- ogni punto $x_i$ viene associato al centro più vicino  $\mathcal C_\hat j^{(k)}$$$\hat j=\arg\min d(x_i,\mu_j^{(k)}$$
- ad ogni iterazione si spostano i cluster centers puntando seguendo:$$\mu_j^{(k+1)}=\arg\min_\mu\sum_{x_i\in\mathcal C_j^{(k)}}d(x_i,\mu)$$
- quando si raggiunge il minimo i cluster centers non si spostano più
