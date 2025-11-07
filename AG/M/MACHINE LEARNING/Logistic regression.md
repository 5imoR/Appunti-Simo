### Classification rule

$$h_{w,b}=sign\set{w^Tx}$$
Possiamo vedere la funzione $w^Tx$ come un punteggio che può essere usato per la classificazione
$\Rightarrow$ Definiamo un probabilistic labeling
- $P_w[y=1|x]\propto e^{w^Tx}$$\Rightarrow$$P_w[y=1|x]=ce^{w^Tx}$ 
- $P_w[y=-1|x]\propto e^{-w^Tx}$ $\Rightarrow$ $P_w[y=-1|x]=ce^{-w^Tx}$
