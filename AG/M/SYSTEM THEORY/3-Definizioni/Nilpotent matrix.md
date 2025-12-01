#ST-L23-6
### Definition \[Nilpotent matrix]
Una matrice $F\in\mathbb R^{n\times n}$ è detta nil potent se $\exists\bar k\in\mathbb Z\quad \bar k>0$ s.t. $F^\bar k=0_{n\times n}$ 

### Preposition \[Characterization of nilpotency]
Data $F\in\mathbb R^{n\times n}$ quanto segue è equivalente:
- $F$ è nilpotent
- $p(s)=s^k\quad\exists \bar k\in\mathbb Z,\quad k>0$  è un annihilating polynomial di $F$ 
- $\exists m\in \mathbb Z,\quad m>0$  s.t. $\Psi_F(s)=s^m$ (min. annihi. poly.)
- $\Delta_F(s)=s^n$
- $\sigma(F)=(0,0,\dots,0)$ 


### Definition \[Nilpotency index]
Data una nilpotent matrix $F\in\mathbb R^{n\times n}$ definiamo come nilpotency index il più piccolo valore di $\bar k\in\mathbb Z,\quad k>0$ s.t. $F^\bar k=0_{n\times n}$ 

Nilpotency index di $F$ $\equiv$ $\deg \Psi_F(s)=\deg\Psi_1(s)\equiv$ dimensione del più largo miniblock in $J_F$ (associato con $\lambda =0$)

##### NI x SRF
$$
\text{nil.index}=\max\set{\text{nil. index di } F_{22},\ \ \text{reach. index di }(F_{11},G_1) }
$$
