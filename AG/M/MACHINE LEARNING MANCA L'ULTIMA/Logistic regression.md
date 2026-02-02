#ML-L14-2 
### Classification rule

$$h_{w,b}=sign\set{w^Tx}$$
Possiamo vedere la funzione $w^Tx$ come un punteggio che può essere usato per la classificazione
$\Rightarrow$ Definiamo un probabilistic labeling
- $P_w[y=+1|x]\propto e^{w^Tx}$$\quad\quad\Rightarrow\quad$$P_w[y=+1|x]=ce^{w^Tx}$ 
- $P_w[y=-1|x]\propto e^{-w^Tx}$ $\quad\Rightarrow\quad$ $P_w[y=-1|x]=ce^{-w^Tx}$
Dove $c$ è una costante take che:
$$P[P_w[y=1|x]+P_w[y=-1|x]=1$$

Prendiamo come valore di $c$:
$$c=e^{w^Tx}+e^{-w^Tx}$$
- $\displaystyle P_w[y=+1|x]=\frac {e^{w^Tx}}{e^{w^Tx}+e^{-w^Tx}}\cdot \frac {e^{-w^Tx}}{e^{-w^Tx}}=\frac 1 {1+ {e^{-2w^Tx}}}$ 

- $\displaystyle P_w[y=-1|x]=\frac {e^{-w^Tx}}{e^{w^Tx}+e^{-w^Tx}}\cdot \frac {e^{w^Tx}}{e^{w^Tx}}=\frac 1 {1+ {e^{2w^Tx}}}$ 

Andando a rinominare $w=2w$ otteniamo:
- $\displaystyle P_w[y=+1|x]=\frac 1 {1+ {e^{-w^Tx}}}$
- $\displaystyle P_w[y=-1|x]=\frac 1 {1+ {e^{w^Tx}}}$

In maniera più compatta possiamo scrivere:
$$\large P_w[y|x]=\frac 1 {1+ {e^{-y\ w^Tx}}}$$
#### Remark
"Possiamo vedere la funzione $w^Tx$ come un punteggio che può essere usato per la classificazione"

si ottiene $P_w[y|x]$ andando a mappare $w^Tx(\in P)$ nell' intervallo $[0,1]$ 
	(andando ad ottenere una probabilità)

$P_w[y|x]=\sigma(z)\ \circ\ yw^Tx$   ottenendo:             $\large\displaystyle\sigma(z)= \frac1 {1+e^z}$             $z=-y\ w^Tx$ 

![[mapping logistic]]
$\Rightarrow$ possiamo calcolare la probabilità come segue:
- $\displaystyle P_w[y=+1|x]=\frac 1 {1+ {e^{-w^Tx}}}$ 
- $\displaystyle P_w[y=-1|x]=1-P_w[y=+1|x]$ 