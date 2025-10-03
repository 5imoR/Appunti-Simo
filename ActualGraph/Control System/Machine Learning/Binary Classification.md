[[MACHINE LEARNING]]
- $x \in X (= \mathbb{R}^d)$
- $y\in \{0,1\}$
- $S=\{z_i\quad i=1 ... n\}$ 

**Assumption on data**
- $x\sim \mathcal{D}_x$ 
- $y|x \sim \mathcal{D}_{y|x}$ 

**Loss Function**
- $l(h,z)\geq 0$
- close to $0$ if it's good
- $l(h,z)=\begin{cases}1\quad h(x) \neq y\\0\quad h(x)=y\end{cases}$ 

**Empirical Loss (Risk)**
Probabilità d'errore considerando solo il training set
- $L_S=1/m\sum_{i=1}^ml(h,z_i)$ 
- $h \in H$
- $S= \{z_i\quad i=1 ...m\}$

**Algorithm(Empirical Risk Minimization)**
- $A\cdot S\rightarrow \hat{h_s}\in H$ 
- $\hat{h_s}= argmin(L_S(h))$

**True Risk**
Probabilità d'errore effettiva
- $L_D(h) =\mathbb{E}[l(h,z)]$ 

#ML-L3

**Remark**
$L_D(h)= 1\cdot P[l(h,z)=1]+0\cdot(1-P(l(h,z)=0)$ 
chance che ciò che è 1 fosse 0 e ciò che è 0 fosse 1

#### Esempio

| ![[binary class.\|300]] | $$\begin{align}&x\in\mathbb{R}^2\\&x\sim D_x\\&x_1\sim u[[0,1]\times[0,1]]\\ &y=f(x)=\begin{cases}1\quad x\in A\\0\quad x\in A\end{cases}\\&A=1/2\end{align}$$ |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
Quello che vediamo noi è:

| ![[binary class.1\|300]] | $$\begin{align}&S^*=\{z_i\quad i=1\dots m\}\\&m=10\\&H=\text{all possible function}\\&h(x):\mathbb{R}^2\longrightarrow\{0,1\}\\&\hat h_s(x)=\begin{cases}1\quad x\in B\\0\quad x\in B\end{cases}\end{align}$$ |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
Bisogna trovare un'area $B$ adatta, un esempio può essere mettere  $y=1$  solo dove sono presenti i valori del data set.
Considerando questa ipotesi possiamo calcolare $L_S$ ed $L_D$ 
- $L_S=0$
- $L_D=1/2$ 

Provando a cambiare ipotesi, si potrebbe dire che $B$ è l'insieme di tutti i rettangoli interni alla nostra area $1\times 1$ che comporta infinite possibilità e quindi non va bene.
Un alternativa valida è prendere 5 aree a piacere ed utilizzare quelle come possibili $B$. 
![[bin class2]]
$L_s(h_{B1})=\frac{4}{10}\quad L_s(h_{B2})=\frac{0}{10}\quad L_s(h_{B3})=\frac{0}{10}\quad L_s(h_{B4})=\frac{0}{10}\quad L_s(h_{B5})=\frac{3}{10}$

Si prendono le ipotesi migliori e si calcola il true Risk:
$L_D(\hat h_s)=1/2 - area\ B$  

Il problema è che la nostra ipotesi si basa sul data set e di conseguenza non è deterministica, perchè cambiando il set potrebbe cambiare il risultato.

### Definition: Realizability
Una model class $H$ è in accordo con la realizability assumption (con la distribuzione $\mathcal D$) se 
$\exists h^*\in H \text{ tale che }L_D(h^*)=0$  ovvero serve che $h=f$ 

### Theorem
Se abbiamo:
- Binary Class Problem con una perdita tra $0-1$ 
- E' data una model class $M$ finita
- $\exists h^*\in H \text{ tale che }L_D(h^*)=0$
- $S=\{z_1,...,z_m\}\qquad z_i\sim \mathcal{D}\quad i.i.d.$  

Se $\displaystyle m>m_M(\epsilon, \delta)=\frac{1}{\epsilon}\ln(\frac{|H|}{\delta})$ 
allora $P[L_D(\hat h_s >\epsilon ]<\delta$ 
dove $\hat h_s\in argmin\ L_S(h)$ 
	Vuol dire che se l'equazione è rispettata  allora la regola ha un errore maggiore di $\epsilon$ con una probabilità minore di $\delta$
