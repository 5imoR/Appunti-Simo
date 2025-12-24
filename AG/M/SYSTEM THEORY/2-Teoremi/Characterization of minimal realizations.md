---
tags:
---
#ST-31-2
## Theorem \[Characterization ofg minimal realizations]
Data una strictly prtoper rational matrix $W(s)\in\mathbb R(s)^{p\times m}$  ed una $n$-dimensional realization $\Sigma=(F,G,H)$ di $W(s)$ i seguenti sono equivalenti:
- $\Sigma$ è una [[Realization Theory#Definition [minimal realization|minimal realization]] di $W(s)$
- $\Sigma$ è un reachable and observable realization di $W(s)$
## Proof
#### $1\Rightarrow 2$ Counter positive
Supponiamo che $\Sigma$ non sia reachable allora $\exists T\in \mathbb R^{n\times n}$ non singular square che riduce $\Sigma$ in [[SRF Standard Reachability Form]] ottenendo $\Sigma_1=(F_{11},G_1,H_1)$ con $\dim \Sigma_1=\rho<n$
Ma abbiamo già visto che  $W(s)\equiv H_1(sI_\rho-F_{11}^{-1})G_1$
$\Sigma_1$ è una realization di $W(s)$ di dimensione $\rho<n=\dim \Sigma\Rightarrow \Sigma$ non è minima
Lo stesso vale nel caso non sia observable, con l'unica differenza che si utilizza la [[SOF Standard Observability Form]]

#### $2\Rightarrow 1$ Omessa
