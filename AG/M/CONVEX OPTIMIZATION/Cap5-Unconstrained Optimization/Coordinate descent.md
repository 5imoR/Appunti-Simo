#CO-L16-1
E' usato in coordinate friendly functions.
$$
x_{jk}^{k+1}=x_{jk}^{k}-t_k\nabla_{jk}f(x^k)
$$
con un iteration cost di $O(n)$.
### Iteration complexity
Consideriamo la scelta della variabile $x_{jk}$  per aggiornare una scelta a random.
Assumiamo:
Ogni componente è Lipschitz continuous, $\nabla_jf(\cdot)$ è M-Lipschitz continuous
$$|\nabla_j f(x+\gamma e_j) -\nabla_jf(x)|\le M|\gamma|\qquad f\in\mathbb C^n$$
Per $f\in\mathbb C^2$ equivale a: $|\nabla_{jj}^2f(x)|\le M$
	Prima stavamo mettendo restrizioni sull'intera Hessian, ora solo sugli elementi della diagonale( weaker restriction )

#### 1D descent Lemma
$$f(x^{k+1})\le f(x^k)+\nabla_{jk}f(x^k)^T(x^{k+1}-x^k)+\frac M2(x^{k+1}-x^k)^2$$
assumiamo $t_k=\frac 1M$ 
$$
f(x^{k+1})\le f(x^k)-\frac 1{2M}|\nabla_{jk}f(x^k)|^{\color{orange}2}
$$
usiamo il fatto che $j$ è una scelta randomica
$$\begin{align}
E[\ f(x^{k+1})\ ]&\le f(x^k)-\frac 1{2M}E_{j\sim\mathcal U}[\ |\nabla_{jk}f(x^k)|^2\ ]\\
&=f(x^k)-\frac1{2M}\sum_{j=1}^n\frac 1n |\nabla_jf(x^k)|^2\\
&=f(x^k)-\frac1{2Mn}\sum_{j=1}^n |\nabla_jf(x^k)|^2\\
&=f(x^k)-\frac1{2M{\color{orange}n}}|\nabla f(x^k)|^2\\
\end{align}$$
Il gradient descent era: $f(x^{k+1})\le f(x^k)-\frac 1{2M}||\nabla f(x^k)||^2$ quindi ora il progresso è $n$ volte più piccolo. Guadagno $n$  fattori nell'iteration cost ma servono $n$ più iterazioni
Se si assume strong convexiti questo risultato non cambia.

Perchè torna utile in pratica?
Per via di $M$ nella descent lemma. $M$ nel less dimension case è solitamente più piccolo. I vincoli sono più piccoli e possiamo prendere step più grandi.

### Strategie
- cyclic selection: invece che prendere cordinate $x_j\sim \mathcal U$  andiamo a ciclare tutte le coordinate nello stesso ordine
	Nella pratica funziona bene nella teoria è peggio
- random shuffling: (è un mix tra uniformly at random e cycling) prendiamo un termine a random, lo seguiamo e lo cambiamo alla fine
- greedy rule: si prende la coordinata con i più grande coefficiente nel gradiente
	$j_k=\arg\max_j|\nabla_jf(x^k)|$ è garantito del progresso
	$f(x^{k+1})\le f(x^k)-\frac 1{2M}||\nabla f(x^k)||_\infty$  
	ma sarebbe necessario calcolare l'intero gradiente.
	Trick: ci sono funzioni speciali che ci permettono di tener traccia del massimo senza calcolare il gradiente.
- non uniform sampling. Si vuole scegliere le variabili più importanti più spesso. Per ogni variabile si mantiene un'approssimazione di $M_j$ lipschitz constant, calcoliamo $t_k$ con back tracking  e quindi $\displaystyle M_j=\frac 1{t_k}$ . Scegliamo $x_j$ con $\displaystyle P[\ J_k=J\ ]=\frac{M_j}{\sum^n_{i=1}M_i}$ . Si preferiscono coordinate con $M_j$ grand ed è uniforme se tutti gli $M_i$ sono uguali.
	In teoria converge come la versione uniforme ma con vincoli diversi
	