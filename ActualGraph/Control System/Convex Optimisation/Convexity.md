[[CONVEX OPTIMIZATION]] #CO-L2

Convexity è una proprietà chiave per la soluzione ed ottimizzazione dei problemi.
# Affine Combination
Dati: $x,y \in \mathbb{R}^N$ chiamiamo affine combination 
$$
\begin{align}
&y=\theta_1x_1+\theta_2x_2\\
&\theta_1+\theta_2=1 \qquad \theta_1,\theta_2 \in \mathbb R
\end{align}
$$
Andando a mettere tutto insieme si ottiene:
$$
y=\theta_1x_1+(1-\theta_1)x_2=x_2+\theta_1(x_1+x_2)
$$

| ![[affineComb\|200]] | L'affine combination di $x_1,\ x_2$ è una linea che passa su di loro.<br> |
| -------------------- | ------------------------------------------------------------------------- |
In generale dati $m$ punti e $m$ moltiplicatori ($\theta$) la combinazione affine è:
$$
y=\sum_{i=1}^m\theta_ix_i  \qquad\qquad  \sum_{i=1}^m\theta_i=1
$$
### Affine set
Un set si dice affine se contiene tutte le affine combinations dei suoi punti
In sintesi un affine set è uno sottospazio vettoriale che non necessita di passare nell'origine

Un affine set $C= V+x_0$ dove $x_0 \in C$ e $V$ è un sottospazio vettoriale e possiamo dire che:$dim(C)=dim(V)$ 
![[relIntNonFullDimSet]]
### Affine hull 
Dato un set $C$ si dice affine hull il set $aff(C)$  di tutti i punti ottenuti tramite combinazioni affini degli elementi di $C$. Questo è anche l' affine set più piccolo contenente $C$  
### Relative interior
Il relative interior di $C$ è definito come l'interno di $C$ rispetto al suo affine hull $aff(C)$
$$
relint(C)=\{x\in C\ |\ B(x,r)\cap aff(C)\subseteq C\text{ per alcuni }r>0\}\qquad B(x,r)=\text{sfera di raggio r in x}
$$
Qundi:
- regular interior: sarebbe il volume di sfera interna a $C$, vuoto se il set non è *full dimensional* ad esempio il caso di: $dim(C)<dim(\mathbb{R})$ 
- relative interior: è la sezione della sfera contenuta in $C$ in ogni caso.

Possiamo definire *relative boundary* come $relbd(C)=cl(C)\backslash\ relint(C)$ 

# Convex Combination
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
### Convex Set 
Un set è convex se contiene tutte le combinazioni convesse dei suoi punti
![[convexSet|600]]

### Convex hull
Dato un set $C$ definiamo il convex hull $conv(C)$ il set di tutti i punti che possono essere ottenuti come *convex combinations* degli elementi di $C$.


Alcuni esempi di convex set:
- $\emptyset\ and\ \mathbb R$
- qualunque affine set
- hyperplanes: $\{x|a^\perp x=b\}\qquad \forall a\in\mathbb R^n,\ a\neq0,b\in\mathbb R$  
	il piano ortogonale ad un vettore
- halfspaces: $\{x|a^\perp x\leq b\}\qquad \forall a\in\mathbb R^n,\ a\neq0,b\in\mathbb R$ 
	quello che è sopra o sotto l'iperpiano
- Euclidean balls:$B(x_c,r)=\{x|\ \lVert{x-x_c}\rVert\leq r\} \qquad \forall x_c\in\mathbb R^n,\  r>0$ 
- Ellipsoids:$\xi(x_c, P,r)=\{x| (x-x_c)^\perp P^{-1}(x-x_c)\leq r\}$
	per ogni $P\succ 0$ con centro in $x_c\in \mathbb{R}^n$ e raggio $r>0$ 
- polyhedra $P=\{x| A_x\leq b,Cx=d\}$


## Calculus of convex sets
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
## Topological properties
Per ogni  subset $M\subseteq \mathbb R^n$ possiamo dire che:
$$relint(M)\subseteq M\subseteq cl(M)$$
Per i convex set la situazione è migliore. Se $M$ è un convex set allora:
- $relint(M),int(M),cl(M)$ sono convex set
- $M\neq\emptyset\Rightarrow relint(M)\neq\emptyset$
- $cl(M)=cl(relint(M))$
- $relint(M)=relint(cl(M))$
Dalla quale si deduce:
Se M è un convex set $x\in relint(M)$ e $y\in cl(M)$ allora abbiamo che l'intero segmento$[x,y)\subseteq relint(M)$ 