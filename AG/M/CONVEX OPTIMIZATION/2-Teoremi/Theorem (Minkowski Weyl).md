### Theorem (Minkowski Weyl)
Ogni punto del polytope può essere espresso come convex combination dei suoi vertici
	Questo non si applica ai polyhedron

In altre parole un polytope può essere descritto in due modi diversi:
- $H$: ovvero l'intersezione dei suoi linear constraint 
- $V$: dai suoi vertici

#### Corollary
Se il feasible set $P$ di un linear program è bounded e non empty allora esiste almeno un optimal vertex.

### Proof
- $x_1\dots x_k$ i vertici
- $y\in P$ una feasible solution arbitraria
- $z^*=\min \{c^T x^i : i=1\dots k\}$ 

$$
\begin{align}
c^Ty&=c^T\left(\sum_{i=1}^k\lambda_ix^i\right)\\
&=\sum_{i=1}^k\lambda_i(c^Tx^i)\geq\sum_{i=1}^k\lambda_iz^*\\
\end{align}
$$
- $\sum_{i=1}^k\lambda_i$  è pari a $1$ dato che siamo in un caso particolare di *convex program*
$$
c^Ty\geq z^*
$$
