#CO-L13-1 

### Unconstrained Optimization
- E' [[Convex Set|Convex]]
- Non [[Linear Programming|Linear]]
- Non [[Integral Programming|Integral]] 
Un esempio può essere:
$$\min_{x\in\mathbb R^n}f(x)$$
Questo però non è computabile da un pc.
Possiamo dire però:
- $\exists x^*$ soluzione ottima s.t. $p^*=f(x^*)$ 
	Questo ci permette di togliere casi brutti come avere il minimo che tende ad un valore ma non lo raggiunge mai
- Il gradiente $\nabla f$ no può cambiare arbitrariamente veloce, più formalmente:
	ad esempio $e^x$ non va bene perchè il gradiente cresce esponenzialmente
$$||\nabla f(x)-\nabla(f(y)||\le M||x-y||\forall x,y\qquad \text{Lipschitz continuous}$$
	- $M\ge 0$ è la  Lipschits constant (per conoscerla serve avere già la soluzione del problema). Se $f\in\mathbb C^2$ questo è equivalente a $\nabla^2f(x)\preceq MI$ 
	- $\nabla f(x)= 0$
A trovare la $x$ esatta non è possibile quindi si va ad utilizzare una sequenza di punti  $x_0,x_1\dots$ e si cerca di farla convergere alla soluzione:
$$
\lim_{k\to+\infty}\nabla f(x^k)=0\qquad\lim_{k\to+\infty}\nabla x^k=x^*
$$

### Descent methods
C'è un miglioramento ad ogni step  
- $f(x^{k+1})<f(x^k)\quad \forall k$  
### Subset
Equivalentemente possiamo creare un subset w.l.o.g.
$S=\set{x\in dom f|f(x)\le f(x^0)}$     
	$x^0$ punto di partenza
	andremo ad assumere che sia compact, closed, bounded
Questo subset ci semplifica la vita perchè basta che la nostra funzione soddisfi i valori all'interno di $S$. 

### Metodi iterativi

Tutti i metodi iterativi devono seguire lo stesso pattern:
$$
x^{k+1}=x^k+t^k\Delta x^k
$$
In parole povere: Lo step sucessivo è ottenuto dal punto attuale($x^k$) e prendendo uno step di lunghezza $t^k\ge 0$ lungo la direzione di ricerca $\Delta x^k$ 
Questo continua a  iterare finchè non viene raggiunto uno *stopping criterion*, solitamente sarà qualcosa del tipo $||\nabla f(x)||\le\varepsilon$  
#### Pseudocodice generico
Vale anche per il gradient descend

1|  let $x\in dom\ f$ be a starting point
2|  while $||\nabla f(x)||>\varepsilon$ do:
3|   	Determine direction $\Delta x$ 
4|  	Choose step size $t$
5|  	Update $x\leftarrow x+t\Delta_x$ 
6|  return $x$ 

L'unico problema sono riga 3 e 4.
#### Scelta della step lenght $t$ 
Supponiamo di avere già $\Delta x^k$ 
Non lo vogliamo troppo piccolo, senno è necessario troppo tempo, ne troppo grande perchè genera errori.

##### Exact line search
risolve one dimensional optimization problems
$$
t=\arg\min_{s\ge 0}f(x+s\Delta_x)
$$
Questo si usa quando $t$ può essere calcolato analiticamente oppure se è meno costoso rispetto a trovare $\Delta x$ 
##### Line search (backtracking)
Non punta a trovare la $t$ ottima ma cerca di ridurre $f$ abbastanza
Un esempio è chiamato backtracking e consiste nel prendere uno step, usarlo, non appena diventa troppo grande lo riduco.
- $0< \alpha<\frac12$
- $0<\beta<1$ 

###### Pseudocodice
1|  let $t=1$
2|  while $f(x+t\Delta_x)>\overbrace{f(x)+\alpha t{\underbrace{\nabla f(x)^T\Delta_x}_{\text{lower bound}}}}^{\text{upper bound}}$   
3| 	$t\leftarrow\beta t$
4|  return $t$ 
###### ![[backtracking]]
Se $t$ è maggiore di $t_0$ viene ridotto di un fattore $\beta$ di conseguenza il risultato di $t$ sarà sempre $t=\min\set{\beta t_0,1}$ 

![[UNB Gradient Descent]]
ddd