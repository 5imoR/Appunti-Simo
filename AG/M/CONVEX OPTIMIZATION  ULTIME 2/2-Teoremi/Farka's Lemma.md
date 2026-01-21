---
tags:
  - CO-L8
---
## Theorem (Farka's Lemma)
Una disuguaglianza $\alpha^Tx\geq \beta$ è valida per il poliedo in [[Linear Programming#Standard form|standard form]] $P=\set{Ax=b,x\geq 0}$ se e solo se esiste un vettore $u\in \mathbb R^m$ tale che:
- $\alpha^T\geq u^TA$
- $\beta\leq u^Tb$ 
## Corollary  (Farka's Lemma)
Il dual problem può essere riscritto come:
$$
\begin{cases}
\max u^Tb\\
c^T\geq u^TA
\end{cases}
$$

## Proof
$$\alpha^T\geq u^TA=u^Tb\geq\beta $$
Perchè l'uguaglianza sia valida serve che:
$$\beta \leq z^* \min\{\alpha^Tx:x\in P\}$$
