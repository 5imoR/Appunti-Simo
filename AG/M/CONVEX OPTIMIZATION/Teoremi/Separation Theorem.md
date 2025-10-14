#CO-L3


Molto utile in convex optimization.
Dati:
- $C, D$  non empty, convex set
- $C\cap D=\emptyset$ 
Allora esiste un iperpiano $a\in \mathbb{R}^n\quad a\neq 0$ e $b\in \mathbb{R}$  tali che:
$$
\begin{align}
a^Tx\leq b \quad \forall x\in C\\
a^Tx\geq b \quad \forall x\in D\\
\end{align}
$$
#### Dimostrazione
##### L1
Definiamo
- $A\subseteq\mathbb{R}^n$ non empty set
- $f:\mathbb{R}^n\rightarrow \mathbb{R}$
$$
f(x)=d(x,A)=\inf_{y\in A}||x-y||
$$
dove $d$ è la distanza tra $x$ ed il set $A$. Allora è una funzione continua
	infimum è come il minimo ma se l'insieme è $A=(2,7]$ l'infimum è  2
###### Proof
- $x,y\in \mathbb{R}^n$ 
- $z\in A$ 
per definizione della distanza si ha:$$d(x,A)\leq d(x,z)\leq d(x,y)+d(y,z)$$
	la distanza tra due punti sarà sempre $\leq$ se si aggiunge un punto in mezzo ai due
se $z$ è l'infimum di $A$ allora possiamo dire che:
$$
\begin{align}
d(x,A)\leq d(x,y)+d(y,A)\\
d(y,A)\leq d(x,y)+d(x,A)\\
\end{align}
$$
Unendole si ottiene:
$$
||d(x,A)-d(y,A)||\leq d(x,y)
$$
Essendo che $d(x,y)\rightarrow 0$  lo stesso vale per $||f(x)-f(y)||$ di conseguenza $f$ è continua.
##### L2
Definiamo
- $A\subseteq \mathbb R^n$ non empty, closed set
- $y\notin A$  
Allora esiste $\overline x \in A$ alla distanza minima    $d(y,\overline x)\leq d(y,A)$
###### Proof
- $\exists \hat x\in A\ s.t.\ d(y,A)\leq d(y,\hat x)$ 
- $A'=A\cap\{x| d(x,y)\leq d(y,\hat x)\}$
	![[A']]
A' è *closed* e *bounded* (*compact*) inoltre $f(x)=d(x,A')$ è continua.
Per il [Teorema di Weierstrass](Teoremi.md#Weierstrass)  possiamo dire che:
$$
\exists \overline x\in A'\subseteq A\ s.t.\ d(y,\overline x)=d(y,A')=d(y,A)
$$
##### L3
Definiamo
- $C$ è closed
- $D$ è compact (closed e bounded)
e sono entrambi non vuoti, allora esiste $x\in C$ e $y\in D$ s.t. $d(x,y)=d(C,D)$
###### Proof
- $f:D\rightarrow\mathbb R$ definita come $f(z)=d(z,C)$ 
dato che $D$ è compatto ed $f$ è continua per il [Teorema di Weierstrass](Teoremi.md#Weierstrass)  si può dire che 
$\exists y\in D$ s.t. $d(D,C)=d(y,C)$ 
Da **L2** possiamo dire che 
$$
d(x,y)=d(y,C)=d(C,D)
$$

#### Caso speciale
- $C,D$ non empty, closed, convex sets che non si intersecano ed uno di questi è compact
Allora esiste un hyperplane che li separa
$$
\begin{align}
a^Tx\leq b \quad \forall x\in C\\
a^Tx\geq b \quad \forall x\in D\\
\end{align}
$$
##### Proof
Da **L3** esiste $c\in C$ e $d\in D$ s.t. $d(c,d)=d(C,D)$.
	$d(c,d)\geq 0$ perchè sennò $C\cap D=\emptyset$ 
Ora definiamo:
- $a=d-c$
- $b=\large\frac{(d-c)^T(d+c)}{2}=\frac{|d|^2-|c|^2}{2}$ 
![[caso speciale]]
#####
Dimostriamo che $a^Tx\geq b \quad \forall x\in D$
$$
\begin{align}
f(x)&=a^Tx-b\\
&=(d-c)^T\left(x-\frac{d+c}{2}\right)\\
&=(d-c)^T\left(x-d+d-\frac{d+c}{2}\right)\\
&=(d-c)^T(x-d)+\frac{1}{2}||d-c||^2\\
\end{align}
$$

###### Proof
 $f(x)\geq0\forall x\in D$ per contraddizione.
- $\exists u\in D$ s.t. $f(u)<0$ 
visto che $\frac{1}{2}||d-c||^2$ è sempre positivo allora $(d-c)^T(u-d)<0$ 
Notiamo che:
$$2(d-c)^T(u-d)=\frac{d}{dt}||d+t(u-d)-c||^2|_{t=0}<0$$
Prendendo un $t>0$ abbiamo che 
- $||d+t(u-d)-c||<||d-c||$ 
che implica:   
- $y=d+t(u-d)$ è più vicina a $c$ che a $d$  
questa però è una contraddizione dato che $y,d,u$ sono convex combination e quindi appartengono al convex set $D$. Quindi non possono essere più vicini a $c$ che a $d$ 

#### Caso generale
Consideriamo $C-D$ (convex perchè C e D lo erano al loro volta) e $0\notin C-D$ 
questo ci porta a 2 casi:
1. $C-D$ è closed: 
	questo è il [[Convex Set#Separation Theorem#Caso speciale|caso speciale]] e di conseguenza possiamo dividere$C-D$ da $0$.
	- $a$ è l' hyperplane corrispondente  mentre $b=0$ 
	$$
	a^T(x-y)\leq0\qquad \forall x\in C \quad\forall y\in D
	$$
	Possiamo quindi costruire un hyperplane separatore tra $C$ e $D$  come:
	$$
	a^Tx\leq\underbrace{\max_{x\in C} a^Tx\leq \min_{y\in D} a^Ty}_{\text{b è qua dentro}}\leq a^Ty
	$$
2. $C-D$ non è closed: 
	1. Se $0\notin cl(C-D)$  allora possiamo ripetere i passaggi del caso precedente e separare $0$ da $cl(C-D)$ e quindi $C$ da $D$.
	2. Se $0\in cl(C-D)$ uguale a dire $0\in bd(C-D)$
		Consideriamo
		- $\{x_k\}\rightarrow 0$   la sequenza di punti che converge a $0$ dall'esterno di $(C- D)$.  
		- ${y_k}$ i punti corrispondenti di minima distanza di $x_k$ da $cl(C-D)$
		Ogni punto $x_k$ è separato da $cl(C-D)$ perchè può essere visto come il [[Convex Set#Separation Theorem#Caso speciale|caso speciale]] 
		![[SeptemGeomRepGen|200]]
		Il vettore normalizzato del hyperplane separatore sarà:
		$$
		a_k=\frac{y_k-x_k}{||y_k-x_k||}
		$$
		$\{a_k\}\rightarrow a$  per alcuni $a$ . 
		Adesso per ogni $z\in cl(C-D)$:
		$$
		\begin{align}
		a^Tz&=\lim_{k\rightarrow+\infty} a_kz\qquad &\{a_k\}\rightarrow a\\
		&\leq\lim_{k\rightarrow+\infty} a_k^Tx_k & a_k \text{ are sequently hyperplanes of $x_k$}\\
		&=0&{x_k}\rightarrow 0
		\end{align}
		$$
		Di conseguenza:
		se un set $C$ è non empty e convex allora esiste un *supporting hyperplane*$(a,b)$ per ogni punto $x\in bd(C)$ 

