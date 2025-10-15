[[Affine Combinations]] #CO-L2 
## Convex Combination
Una combinazione convessa è simile ad una affine ma con l'aggiunta che $\theta_1,_2$ devono essere positivi. 
$$
\begin{align}
&y=\theta_1x_1+\theta_2x_2\\
&\theta_1+\theta_2=1 \qquad \theta_1,\theta_2 \in \mathbb R+
\end{align}
$$
L'unica differenza da un affine set è che ora: $\theta_1,\theta_2\in \mathbb{R}+$  questo vuol dire che adesso la combinazione è il segmento interno a $x_1,x_2$ e non più la linea intera
![[convexcomb|200]]

In generale dati $m$ punti e $m$ moltiplicatori la convex combination è:
	(uguale ad affine) cambia solo il dominio dei moltiplicatori
$$y=\sum_{i=1}^m\theta_ix_i  \qquad\qquad  \sum_{i=1}^m\theta_i=1$$
## Convex Set 
Un set è convex se contiene tutte le combinazioni convesse dei suoi punti
![[convexSet|600]]

### Convex hull
Dato un set $C$ definiamo il convex hull $conv(C)$ il set di tutti i punti che possono essere ottenuti come *convex combinations* degli elementi di $C$.


Alcuni esempi di convex set:
- $\emptyset\ and\ \mathbb R$
- qualunque affine set
- hyperplanes: $\{x|a^T x=b\}\qquad \forall a\in\mathbb R^n,\ a\neq0,b\in\mathbb R$  
	il piano ortogonale ad un vettore
- halfspaces: $\{x|a^T x\leq b\}\qquad \forall a\in\mathbb R^n,\ a\neq0,b\in\mathbb R$ 
	quello che è sopra o sotto l'iperpiano
- Euclidean balls:$B(x_c,r)=\{x|\ \lVert{x-x_c}\rVert\leq r\} \qquad \forall x_c\in\mathbb R^n,\  r>0$ 
- Ellipsoids:$\xi(x_c, P,r)=\{x| (x-x_c)^T P^{-1}(x-x_c)\leq r\}$
	per ogni $P\succ 0$ con centro in $x_c\in \mathbb{R}^n$ e raggio $r>0$ 
- polyhedra $P=\{x| A_x\leq b,Cx=d\}$


### Calculus of convex sets
Per provare che un set sia convesso lo si deve ottenere da un set più semplice(convesso) tramite delle operazioni che lo tengano convesso.
- **Intersection** Data una famiglia $\mathcal A$ di convex sets la loro intersezione$$C=\bigcap_{\alpha\in\mathcal A} C_\alpha$$
	Esempio: The positive semidefinite cone $S_+^n$ può essere espresso come:
	$$
	\bigcap_{z\neq0}\{X\in S^n|z^\perp Xz\geq 0\}
	$$
- **Affine Functions** Sia $f:\mathbb R^n\rightarrow\mathbb R^m$ una funzione affine per esempio $f(x)=Ax+b$  per una qualche $A\in\mathbb{R}^{m\times n}$ e $b\in\mathbb R^m$. Allora se $S$ è un convex set lo sono anche:$$f(S)=\{f(x)|x\in S\}f^{-1}(S)=\{x|f(x)\in S\}$$
- **Product** Dati $C_1\subseteq \mathbb R^{n_1}$ e $C_2\subseteq \mathbb R^{n_2}$ convex sets il loro prodotto cartesiano $C_1 \times C_2\subseteq\mathbb R^{n_1+n_2}$ è anchesso convesso
	![[Product|200]]
- **Linear Combinations** Dati $M_1\dots M_k$ convex sets in $\mathbb R^n$ e moltiplicatori arbitrari $\lambda_1\dots\lambda_k$ il set $\sum_{i=1}^k\lambda_iM_i$ è un set convesso
- **Projection** Sia $S\in\mathbb R^m\times\mathbb R^n$ un convex set. La sua proiezione è un convex set$$T=proj_{R^m}(S)=\{x\in \mathbb R^m|(x,y)\in S \text{ per qualche } y\in \mathbb R^n\}$$
	![[Projection|200]]
### Topological properties
Per ogni  subset $M\subseteq \mathbb R^n$ possiamo dire che:
$$relint(M)\subseteq M\subseteq cl(M)$$
Per i convex set la situazione è migliore. Se $M$ è un convex set allora:
- $relint(M),int(M),cl(M)$ sono convex set
- $M\neq\emptyset\Rightarrow relint(M)\neq\emptyset$
- $cl(M)=cl(relint(M))$
- $relint(M)=relint(cl(M))$
Dalla quale si deduce:
Se M è un convex set $x\in relint(M)$ e $y\in cl(M)$ allora abbiamo che l'intero segmento$[x,y)\subseteq relint(M)$ 

## Separation Theorem
![[Separation Theorem]]
## Convex Functions
Una funzione $f:\mathbb R^n \rightarrow\mathbb R$ si dice convessa se il suo domino $dom(f)$ è un convex set e per ogni $x,y\in dom(f)$ e per tutti $0\leq \theta\leq 1$ abbiamo:
$$
f(\theta x+(1-\theta)y)\leq\theta f(x)+(1-\theta)f(y)
$$
![[convex function]]
In alernativa si può dire che $f(x)$ è convessa se:
(se quello che sta sopra la funzione è un convex set)
$$
epi(f)=\{(x,t)\in\mathbb{R}^{n+1}|x\in dom(f), t\geq f(x)\}
$$
è un convex set.

**Definition** Una funzione $f:\mathbb R^n \rightarrow\mathbb R$ è concave se se $-f$ è convessa
Una qualunque affine function è sia concava che convessa


Alcuni esempi di convex/concave functions:
-  $e^{ax}\rightarrow$ convex $\forall a\in \mathbb R$
-  $x^{a}\rightarrow$ convex $a\geq 1 \wedge a\leq 0$              $\rightarrow$ concave $0\leq 1\leq 1$
-  $|x|^p\rightarrow$ convex $p\geq 1$ 
-  $\log x\rightarrow$ concave 
-  qualunque norm in $\mathbb R^n\rightarrow$ convex
-  la funzione max$\rightarrow$ convex

### Calculus of convex functions
Come per i convex set spesso conviene dimostrare che la funzione è convessa perchè deriva da funzioni convesse più semplici tramite opportune operazioni

- **Non-negative weighted sum** Date $n$ convex function e $n$ non-negative weights la funzione  è una funzione convessa $$f=\sum_{i=1}^nw_if_i$$
- **Composition with affine mappings** Se $f:\mathbb R^n \rightarrow\mathbb R$ è una funzione convessa, $A\in \mathbb R^{n\times m}$ e $b\in\mathbb R^n$ allora è una funzione convessa
$$
f(Ax+b)
$$
- **Positive maximum and supremum** Se $f_1$ e $f_2$ sono funzioni convesse il loro *pointwise maximum* $f(x)=\max\{f_1,f_2\}$ è una funzione convessa.Questo si espende and un numero finito di $k$ funzioni o infinito se si considera il supremum.In altre parole data una famiglia di convex function $\mathcal A$  il *pointwise supremum* è:$$g(x)=\sup_{a\in\mathcal A}f_a(x)$$
	![[pwmax]]
- **Partial munimization** Se $f(x,y)$ è convessa e $C$ è un convex set allora è una funzione convessa $$g(x)=\inf_{y\in C}f(x,y)$$
#CO-L4
### First order condition
Se $f$ è differenziabile e quindi il gradiente $\nabla f(x)$ esiste per ogni punto $x\in dom(f)$  allora:
$f$ è convessa se e solo se:
$$
f(y)\geq f(x)+\nabla f(x)^T(y-x)\qquad \forall x,y\in dom(f)
$$
![[second order|300]]
La funzione $f$ è sempre sopra la sua approssimazione
#### Proof
##### n=1 Caso unidimensionale
$$
f(y)\geq f(x)+ f'(x)(y-x)\qquad \forall x,y\in dom(f)
$$
Prendiamo 2 punti $x, y$  e dato che $f$ è convessa vale $(1-\theta)x+\theta y\in domf$
$$\begin{align}
&f((1-\theta)x+\theta y)\leq(1-\theta)f(x)+\theta f(y)\\
&f(x+\theta(y-x))\leq(1-\theta)f(x)+\theta f(y)\\
\\
&\frac{f(x+\theta(y-x))-f(x)}{\theta}\leq f(y)-f(x)\\
&f(y)\geq f(x)+\frac{f(x+\theta(y-x))-f(x)}{\theta}\\
&f(y)\geq f(x)+{f'(x)(y-x)}\qquad \theta\rightarrow 0\\
\end{align}
$$
Prrendiamo altri 2 puntie consideriamo
$z=\theta x+(1-\theta)y$ 
Applicando la condizione richesta si ottiene:
$$
\begin{align}
f(x)\geq f(z)+ f'(z)(x-z)\\
f(y)\geq f(z)+ f'(z)(y-z)\\
\end{align}
$$
Possiamo moltiplicarli per $\theta$ e $(1-\theta)$ ottenendo:
$$
\begin{align}
&\theta f(x)\geq f(z)+ f'(z)(x-z)\\
&(1-\theta)f(y)\geq f(z)+ f'(z)(y-z)\\
\\
&\theta f(x)+(1-\theta)f(y)\geq f(z)+f(z)'\underbrace{[\theta(x-z)+(1-\theta)(y-z)]}_{\theta x+(1-\theta)y-z=0}
\end{align}
$$
quindi $f$ è convessa.

##### Caso multidimensionale
Il prof ha detto che non è importante,(BALZATO)
$$
\begin{align}
&g(t)=f(ty+1-t)x)\\
&g'(t)=\nabla f(ty+(1-t)x)^T(y-x)
\end{align}
$$
###
$$
\begin{align}
&\nabla f(x^*)=0\\
&f(x)\geq f(x^*)+\cancel{\nabla f(x^*)^T(y-x)}
\end{align}
$$
Sei nel punto ottimale, minimo 
### Second order Condition
Se la funzione è doppiamente differenziabile allora possiamo dire che:
*Una funzione è convessa  se e solo se $\nabla^2 f(x)\succeq0 \quad \forall x\in dom(f)$* 
- $\nabla^2f(x)$ si chiama Hessian matrix di $f$ nel punto $x$
- se $succ$ allora è strictly convex
	Non posso dire l'opposto esempio: $x^4$ 
### Global optimality theorem
Prendendo in considerazione 
- $C$ convex set
- $f(x)$ convex function
$$\min_x\{f(x)|x\ in\ C\}$$
Ogni minimo locale è considerato un minimo globale
#### Proof
- $\hat x$ una soluzione locale ottima
- esiste $\epsilon>0$ per definizione tale che:
$$
f(\hat x)\leq f(z)\quad \forall z\in B(\tilde{x},\epsilon)\cap C=\mathcal N_\epsilon(\tilde{x})
$$
Prendiamo un punto $y$ qualunque in $C$ e scegliamo $z=\lambda\tilde{x}+(1-\lambda)y$  qualunque sia $\lambda$ c'è sempre un valore $z$ interno a $N_\epsilon(\tilde{x})$ 
$$
f(\tilde{x})\leq f(z) =f(\lambda\tilde{x}+(1-\lambda)y)\leq \lambda f(\tilde x) +(1-\lambda)f(y)
$$
Dal quale si può facilmente ottenere:
$$
\cancel{(1-\lambda)}f(\tilde x) \leq \cancel{(1-\lambda)} f(y)
$$
![[global min]]

## Problem type
