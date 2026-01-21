#CO-L2
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
