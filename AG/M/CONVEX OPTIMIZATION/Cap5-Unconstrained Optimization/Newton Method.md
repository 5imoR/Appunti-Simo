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