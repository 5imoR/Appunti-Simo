#ST-L16 #DTCT [[State Feedback]]
Sia $F\in \mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$ 
Sotto quali condizioni sul paio $(F,G)$  io posso , per qualunque $n$ numeri complessi (non necessariamente distinti) $\lambda_1\dots\lambda_n\in\mathbb C$  posso sempre determinare una matrice $K$ di dimensioni $m\times n$ s.t. $$\sigma(F+GK)=\set{\lambda_1\dots\lambda_n}$$   
	Dato che $F+GK$ è reale e quindi $\Delta_{F+GK}(s)\in \mathbb R[s]$. Chiaramente non ogni *n-tupla* di numeri complessi può essere proposta:
	Se $\lambda_i\in\mathbb C \setminus \mathbb R$  ed appare $k$ volte nella sequenza $\set{\lambda_1\dots\lambda_n}$  allora
	$\exists j\ s.t.\ \lambda_j=\lambda_i$ ed inoltre  $\lambda_j$ appare $k$ volte in $\set{\lambda_1\dots\lambda_n}$
Una formulazione equivalente:
Sia $F\in \mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$
Sotto quali condizioni $\forall$ monic polynomial $p(s)$ con coefficenti reali di grado $n$ $p(s)\in \mathbb R[s]$ 

$\exists k\in \mathbb R^{m\times n}\ s.t.\ \Delta _{F+GK}(s)\equiv p(s)$ (?)


# From [[State Feedback#Proposition 2|Prop2]]

Se il CEAP è risolvibile allora $\Rightarrow (F,G)$ è reachable

## Proof
Facciamo 2 step:
- Proviamo che il risultato è vero per un *single input system* $(m=1)$  [[CEAP m=1]]
- Estendiamo il caso a $(m>1)$  [[CEAP m =1++]]


