#CO-L16-2
Prima definiamo lo steepest descent.
Consideriamo una funzione $f$ e la sua approssimazione di primo ordine:
$f(x+v)\simeq f(x)+\underbrace{\nabla f(x)^Tv}_\text{derivata direzionale lungo v}$  
Vogliamo prendere $v$  tale che ci permetta di ottenere il maggior progresso, ma ogni direzione più essere sempre scalata tramite una costante positiva per rendere $\nabla f(x)^Tv$ più grande, noi consideriamo direzioni normalizzate.
Data una norma $||\cdot||$ la normalized steepest descent direction $\Delta x_{nsd}$ è:
$$
\Delta x_{nsd}=\arg\min_v\set{\nabla f(x)^Tv\ |\ ||v||=1}
$$
Noi in realtà andiamo ad usare: 
$$
\Delta x_{sd}=\Delta x_{nsd}\cdot||\nabla f(x)||_*
$$
	$||\nabla f(x)||_*$ è la norma duale del gradiente, non ci interessa
1. Considera:
	$||\cdot||_2\triangleq$ norma euclidea, può essere dimostrato che $\Delta x_{sd}=-\nabla f(x)$ 
		$-\nabla f(x)$ steepest descent direction w.r.t. la norma euclidea
2. Considera
	$||\cdot||_p\triangleq$ norma quadratica
	$||z||_p=(z^TPz)^{\frac 12}=||P^\frac12z||_2$ 
		$P$ è positive definite matrix
La generalizzazione della standard euclidian norm (con $P=I$) è la versione pesata di $||\cdot||_2$ dobbiamo scegliere $P$ 
$$\Delta x_{sd}=-P^{-1}\nabla f(x)$$
Otteniamo il gradiente ma dopo una modifica alle coordinate.
Otteniamo però la stessa convergenza del Gradient Descent, se scegliamo $P$ e lo manteniamo, ma la velocità del GD dipende dai *condition numbers* ed è quindi affetta da una modifica sulle coordinate.
Se $P$ non è fisso si ottengono risultati migliori.

### Newton step/direction
$$
\begin{align}
\Delta x_{nt}&=-\nabla^2f(x)^{-1}\nabla f(x)\\
&=P^{-1}\nabla f(x)
\end{align}
$$
Perchè $P=\nabla^2f(x)$ ?
Questa scelta minimizza la second order apprioximation
$$f(x+v)\simeq f(x)+\nabla f(x)^Tv+\frac 12v^T\nabla^2f(x)v$$
Se f è strongly convex allora $\nabla^2f(x)$ è Positive Definite e $v=\nabla^2 f(x)\nabla f(x)$ 
##### esempio 
$f(x)=\frac 12 x^Tax+p^Tx+c$
con  $a$ positive definite
possiamo raggiungere il minimo direttamente con questa scelta.

Possiamo costruire la quadratic approximation e saltare al minimo della quadratic approximation.
$\nabla f(x)=0$ sui punti stazionari. Possiamo approssimare $\nabla f(x)$ come:
$$\nabla f(x+v)\simeq\nabla f(x)+\nabla^2 f(x)v$$ 
### Newton method
#CO-L17-2
$$
\begin{align}
x^{k+1}=x^k-t_k\nabla^2f(x^k)^{-1}\nabla f(x^k)\\
\Delta x_{nt}=-\nabla^2f(x^k)^{-1}\nabla f(x^k)
\end{align}
$$
E' molto costoso:
- $\nabla^2f(x^k)^{-1}$ ha complessità $O(n^2)$
- $\nabla f(x^k)$ ha complessità $O(n)$

**NOTA** se la funzione è quadratica ci mette una singola iterazione a trovare il minimo

Possiamo dire che il newton method è [[Affine invariance|affine invariant]] e quindi non dipende dalle cordinate scelte.
##### Proof
$$
\begin{align}
\Delta y_{nt}&=-\nabla^2g(y)\nabla g(y)\\
&=-(A^T\nabla^2f(Ax)\cancel A)^{-1}\cancel A^T\nabla f(Ax)\\
&=A^{-1}\nabla^2f(Ax)^{-1}\nabla f(Ax)\\
&=A^{-1}\Delta x_{nt}
\end{align}
$$
Quindi possiamo dire che il metodo non dipende dalle coordinate.
### Analisi di Convergenza del Newton method
Assumiamo $f$  strongly convex   ([[Unconstrained Optimization#Subset|cos'è S]])
$$
\begin{align}
&m I\preceq\nabla^2f(x)\preceq MI\quad \forall x\in S\\&
0< m\le M
\end{align}
$$
$\nabla^2f(x)$ è [[Lipscitz continuity|Lipschitz continuous]] $\forall x\in S$
$$||\nabla^2f(x)-\nabla^2 f(y)||\le L||x-y||$$
Non conosciamo $m,\ M,\ L$ ma ci torna utile per fare l'analisi.
![[Newton global convergence lemma#Newton global convergence lemma]]

Si può dire che sia l'opposto dei descent methods infatti questo inizia lentamente e converge molto velocemente mentre per i descent era l'opposto e si convergeva $\to+\infty$.


### Iteration complexity
#### Fase 1

$\displaystyle\frac{f(x^0)-p^*}\gamma=\frac{\text{distanza dall'arrivo}}{\text{distanza fatta ad ogni iter.}}$ ci dà un upper bound al numero di iterazioni
	Nella pratica solitamente questo non richiede più di 100 iterazioni.
#### Fase 2
$$
\begin{align}
\frac L{2m^2}||\nabla f(x^{l})||&\le\left(\frac L{m^2}||\nabla f(x^k)||\right)^{2^{l-k}}\\
&\le\left(\frac L{m^2}\eta\right)^{2^{l-k}}\\
&\le0.5^{2^{l-k}}
\end{align}
$$
Se lo combiniamo con [[PL Inequality]] otteniamo:
$$
\begin{align}
(f(x^l)-p^*)&\le\frac 1{2m} ||\nabla f(x^l)||^2 \qquad\qquad &\text{PL inequality}\\
&\le\frac{2m^3}L(0.5^{2^{l-k+1}})&\text{sostituisco } ||\nabla f(x^l)||\\
&\le \varepsilon
\end{align}
$$
quindi ad ogni iterazione il nostro valore si riduce di un fattore doppiamente esponenziale.
Il numero di iterazioni per la fase 2 è:$$l<\log_2\log_2\left(\frac{2m^3}L\frac1\varepsilon\right)\le 7$$
	Il 7 è un numero detto dal prof(non è matematicamente vero) però se provi a prendere un numero tipo $10^{20}$ e fai 2 volte il logaritmo capisci che non è poi sbagliato

Quest'analisi non è affine invariant dato che dipende da $L,m$ eccetera

