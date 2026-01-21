#CO-L6
# Primal Simplex
L'idea dietro questo algoritmo è:
- Si parte da una feasible base $B$ del problema lineare
- Ci si sposta sulle basi adiacenti(o vertici) finche non raggiungiamo una optimal basis
	Per spostarci di base simette una colonna a 0 e se ne aggiunge un altre con costo migliore, si rivede più avanti
	
Al caso peggiore è esponenziale ma si è dimostrato che nella maggior parte dei casi risulta polinomiale o anche lineare, per questo è molto usato.
![[PrimalSimplex|500]]
 [[Convex Set#Global optimality theorem|Essendo convesso se trovi un minimo locale è un minimo globale]]

Per formalizzare l'algorimo serve trovare:
- come riconoscere una base ottimale (optimality conditions)
- come muoverci su una base adiacente migliore

## Optimality conditions
Dalla [[Linear Programming#Bases|definizione di base]] possiamo scrivere l'object function $z$:
$$
\begin{align}
z&=c_B^Tx_B+c_R^Tx_R\\
&=\underbrace{c_B^TB^{-1}}_{\pi^T}b+\underbrace{(c_R^T-c_B^TB^{-1}R)}_{d_j}x_R\\
&=\underbrace{\pi^Tb}_{costant}+\underbrace{d_jx_R}_{\text{lin. fun.}}
\end{align}
$$
Quindi ora l'objective function è espressa come un termine costante più una funzione lineare delle variabili non appartenenti alla base
$\pi^T=c_B^TB^{-1}$ è detto *vector of multiplierism* e permette la definizione del coefficente $d_j=c_R^T-\pi^TR$ chiamato *reduced cost*.
- Il reduced cost di variabili appartenenti alla base è sempre $0$.
- Il reduced cost di variabili non appartenenti alla base  da un *optimality condition* per la base corrente

Dato che $z= costante+d_jx_R$ si può vedere che $z$ cresce o diminuisce se $d_j > o < 0$ . 

Per capire il concetto:
$z=\pi^Tb+\sum_{j\in N}d_jx_j$  dove:
- $d_j$ sono tutte le possibili direzioni che possiamo prendere
- $x_j$ è a 0 a meno che non decido di seguire quella direzione
- $\pi^Tb$  è la base attuale
![[spostamentobasi|300]]

Possiamo concludere che se $d_j\geq0\quad\forall j\in \mathcal R$  non c'è modo di ridurre $z$ e quindi la base in cui ci troviamo è ottima

## Finding a better basis
Se la base corrente non soddisfa l'*optimality condition* allora esiste una variabile $x_q$ non appartenente alla base  con un reduced cost negativo $d_q<0$. 
Possiamo quindi aumentare $x_q$  finchè
	Più è grande $x_q$ più piccola sarà $z$ e quindi migliore
- continuiamo a soddisfare $Bx_B+Rx_R=b$
- le variabili della base sono non negative

Chiamiamo $t\geq0$ il valore di $x_q$. Sapendo che tutte le variabili non appartenenti alla base rimangono a 0 possiamo scrivere:
$$
Bx_B(t)+tA_q=b
$$
$$
\begin{align}
x_B(t)&=B^{-1}b-tb^{-1}A_q\\
&=\beta-t\alpha_q
\end{align}
$$
dove:
- $\beta=B^{-1}b$
- $\alpha_q=B^{-1}A_q$ 
### Quanto può aumentare?
Volendo mantenere la fattibilità delle variabili della base serve che:
$$x_B^i(t)=\beta_i-t\alpha_q^i\geq 0$$
#### Ratio test
Dato:$$\mathcal I =\{i\in\set{1,\dots,m}|x_q^i>0\}$$
possiamo calcolare il massimo valore di $t$ come:
$$
\theta=\frac {\beta_p}{\alpha_q^p}=\min_{i\in\mathcal I}\set {\frac {\beta_i}{\alpha_q^i}}
$$
La p-esima variabile è la *blocking variable* ed $\alpha_q^p$ è detto *pivot element*.
Per $t=\theta$ la blocking variable diventa $0$ quindi possiamo sostituirla con $x_q$ andando ad ottenere una nuova base
![[basispostate|700]]
Se $\mathcal I=\emptyset$ vuol dire che il problema è unbounded e che possiamo aumentare quanto vogliamo $x_q$ 
Se c'è una base degenerata il ratio test può dare 0 di conseguenza c'è il rischio di cambiare base ma rimanere sullo stesso vertice rischiando a sua volta di creare un loop. Queste sono chiamate *degenerate simplex interations* 

## Pseudocodice
#CO-L7
- step 0:
	- input $B$: matrice composta dalle colonne della base
	- compute $B^{-1}$ 
	- $\beta=B^{-1}b$ : basic solution
	- $z=c_B^TB^{-1}b=c_B^T \beta=c_B^Tx_B$ : objective function
- step 1:
	$\pi^T=c_B^TB^{-1}$: vector of multiplierism
- step 2: \[ pricing ]
	- $d_j=c_j-\pi^TA_j \quad \forall j\in\mathcal R$ : reduced cost
	
	if $d_j\geq0\quad \forall j\in\mathcal R$: 
		mi fermo
	else: 
		$x_q$ è la variabile della colonna
		prendo $x_q$ con $d_q<0$ 
- step 3:
	- $\alpha_q=B^{-1}A_q$
- step 4: \[ Pivot/Ratio ]
	- $\mathcal I =\set{i:\alpha_q^i>0}$ 
		if $\mathcal I=\emptyset$ caso unbounded
	- $\theta= \min_{i\in \mathcal I}\{\frac {\beta_i}{\alpha_q^i}\}$ 
	- $x_{kp}$ variabile che viene rimossa dalla base
- step 5: \[ update ]
	si aggiornano  $B$, $B^{-1}$ e poi $\beta$ e $z$
	$\begin{cases}\beta_i=\beta_i-\theta\alpha_q^i\quad i\neq p\\\beta_p=\theta\\z=z+\theta d_q\quad \theta d_q\leq 0\end{cases}$ 

## Initialization
Finora abbiamo sempre avuto una base di partenza, cosa si fa se  la base non è disponibile da subito?
Si usa il *two-phase simplex method* ovvero nella prima fase  si risolve un altro sistema allo scopo di ottenere una feasible basis che verrà usata nella seconda fase.
$$
\begin{cases}
\min\ c^Tx\\
Ax=b\\
x\geq0
\end{cases}
\longrightarrow
\begin{cases}
\min\ e^Ty=\sum_{i=1}^my_i\\
Ax+Iy=b\\
x\geq0\quad y\geq0
\end{cases}
$$
Consideriamo $w^*=(x^*,y^*)$
	il valore di $w^*$ è il risultato della sommatoria, è presente anche $x$ perchè è dentro il sistema
- $w^*>0$  vuol dire che non c'è un minimo con $y=0$ e di conseguenza il sistema iniziale non era feasible.
- $w^*=0$ 
	- $\forall y$ non fanno parte della base allora abbiamo trovato $B$
	- $\exists y$ che sono della base (succede nel caso di una base degenerate) allora tramite dei *degenerate pivot* li rendiamo diversi dalla vase

## Convergence
Questo algoritmo  riscontra un problema nel caso di basi degeneri, dato che corre il rischio di entrare in loop infiniti.
Esistono 2 soluzioni:
- *Bland's rule*: si cedono 2 gradi di liberta (la possibilità di scegliere $x_q$ e $x_{kp}$  quando sono prensenti più valori ugualmente validi) andando a scegliere sempre quello con indice minimo. Così fancendo si ha la certezza di  convergere.
	Nella pratica è inutile ma è utilizzato per delle dimostrazioni
- *Perturbation* Quando viene individuato un loop vengono aggiunte delle perturbazioni al sistema andando a rompere il ciclo. Sucessivamente si vanno a rimuovere tornando al problema iniziale
# Ex 1
![[SIMPLEEX|300]]

$$
\begin{cases}
\max\quad x_1+x_2\\
6x_1+4x_2\leq 24\\
3x_1-2x_2\leq 6\\
x_1, x_2\geq 0
\end{cases}
\qquad A=\begin{bmatrix}6&4\\3&-2\end{bmatrix}\quad x=\begin{bmatrix}x_1\\x_2\end{bmatrix}\quad 
c=\begin{bmatrix}1\\1\end{bmatrix}
b=\begin{bmatrix}24\\6\end{bmatrix}
$$

Lo si trasforma il [[Linear Programming#Standard form|standard form]] 
$$
\begin{cases}
\min\quad -x_1-x_2\\
6x_1+4x_2+x_3= 24\\
3x_1-2x_2+x_4= 6\\
x_1, x_2,x_3, x_4\geq 0
\end{cases}
\qquad A=\begin{bmatrix}6&4&1&0\\3&-2&0&1\end{bmatrix}\quad x=\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}\quad 
c=\begin{bmatrix}-1\\-1\\0\\0\end{bmatrix}
b=\begin{bmatrix}24\\6\end{bmatrix}
$$
#### Prima iterazione:

| $\mathcal B$    | $B$                                    | $B^{-1}$                               | $\beta$ | $\pi^T$ | $d_1$ | $d_2$ | $\alpha$ | $\theta$ | $z$ |
| --------------- | -------------------------------------- | -------------------------------------- | ------- | ------- | ----- | ----- | -------- | -------- | --- |
| $\set{x_3,x_4}$ | $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ | $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ |         |         |       |       |          |          | $0$ |

- $\beta=B^{-1}b=\begin{bmatrix}1&0\\0&1\end{bmatrix}\begin{bmatrix}24\\6\end{bmatrix}=\begin{bmatrix}24\\6\end{bmatrix}$ 
- $\pi^T=c_B^TB^{-1}=\begin{bmatrix}0&0\end{bmatrix}\begin{bmatrix}1&0\\0&1\end{bmatrix}= \begin{bmatrix}0&0\end{bmatrix}$ 
- $d_1=c_1-\cancel{\pi^TA_1}=-1$ 
- $d_2=c_2-\cancel{\pi^TA_2}=-1$
Scelgo $d_1$ entra $x_1$
- $\alpha=B^{-1}A_1=\begin{bmatrix}6\\3\end{bmatrix}$ $\rightarrow \begin{cases}x_3=24-6x_1\geq0\\x_4=6-3x_1\geq0\end{cases}$  
- $\theta=\min\set{\frac {24} 6, \frac 6 3}$ 
$x_4$ è la prima ad arrivare a $0$ quindi non è più una base
- $\mathcal B=\set{x_3, x_1}$
- $\beta=B^{-1}b=\begin{bmatrix}1&-2\\0&\frac 1 3\end{bmatrix}\begin{bmatrix}24\\6\end{bmatrix}=\begin{bmatrix}12\\2\end{bmatrix}$
- $z=c_B^TB^{-1}b=c_B^T\beta=\begin{bmatrix}0&-1\end{bmatrix}\begin{bmatrix}12\\2\end{bmatrix}=-2$ 

| $\mathcal B$    | $B$                                    | $B^{-1}$                                        | $\beta$                             | $\pi^T$                           | $d_1$ | $d_2$ | $\alpha$                           | $\theta$ | $z$  |
| --------------- | -------------------------------------- | ----------------------------------------------- | ----------------------------------- | --------------------------------- | ----- | ----- | ---------------------------------- | -------- | ---- |
| $\set{x_3,x_1}$ | $\begin{bmatrix}1&6\\0&3\end{bmatrix}$ | $\begin{bmatrix}1&-2\\0&\frac 1 3\end{bmatrix}$ | $\begin{bmatrix}12\\2\end{bmatrix}$ | $\begin{bmatrix}0&0\end{bmatrix}$ | $-1$  | $-1$  | $\begin{bmatrix}6\\3\end{bmatrix}$ | $2$      | $-2$ |
#### Seconda iterazione:


| $\mathcal B$    | $B$                                    | $B^{-1}$                                        | $\beta$                             | $\pi^T$                           | $d_1$ | $d_2$ | $\alpha$                           | $\theta$ | $z$  |
| --------------- | -------------------------------------- | ----------------------------------------------- | ----------------------------------- | --------------------------------- | ----- | ----- | ---------------------------------- | -------- | ---- |
| $\set{x_3,x_1}$ | $\begin{bmatrix}1&6\\0&3\end{bmatrix}$ | $\begin{bmatrix}1&-2\\0&\frac 1 3\end{bmatrix}$ | $\begin{bmatrix}12\\2\end{bmatrix}$ | $\begin{bmatrix}0&0\end{bmatrix}$ | $-1$  | $-1$  | $\begin{bmatrix}6\\3\end{bmatrix}$ | $2$      | $-2$ |
$\downarrow$

| $\mathcal B$    | $B$                                     | $B^{-1}$                                                                                | $\beta$                                    | $\pi^T$                                   | $d_2$                   | $d_4$                   | $\alpha$                                   | $\theta$                | $z$  |
| --------------- | --------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------- | ----------------------- | ----------------------- | ------------------------------------------ | ----------------------- | ---- |
| $\set{x_2,x_1}$ | $\begin{bmatrix}4&6\\-2&3\end{bmatrix}$ | $\begin{bmatrix} \frac{1}{8} & -\frac{1}{4}\\ \frac{1}{12} & \frac{1}{6} \end{bmatrix}$ | $\begin{bmatrix}\frac 3 2\\3\end{bmatrix}$ | $\begin{bmatrix}0&-\frac 13\end{bmatrix}$ | $\displaystyle-\frac53$ | $\displaystyle\frac 13$ | $\begin{bmatrix}8\\-\frac 23\end{bmatrix}$ | $\displaystyle\frac 32$ | $-2$ |
$x=[3\ \frac 32\ 0\ 0]$ 
#### Terza iterazione:

| $\mathcal B$    | $B$                                     | $B^{-1}$                                                                                | $\beta$                                    | $\pi^T$                                   | $d_2$                   | $d_4$                   | $\alpha$                                   | $\theta$                 | $z$          |
| --------------- | --------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------- | ----------------------- | ----------------------- | ------------------------------------------ | ------------------------ | ------------ |
| $\set{x_2,x_1}$ | $\begin{bmatrix}4&6\\-2&3\end{bmatrix}$ | $\begin{bmatrix} \frac{1}{8} & -\frac{1}{4}\\ \frac{1}{12} & \frac{1}{6} \end{bmatrix}$ | $\begin{bmatrix}\frac 3 2\\3\end{bmatrix}$ | $\begin{bmatrix}0&-\frac 13\end{bmatrix}$ | $\displaystyle-\frac53$ | $\displaystyle\frac 13$ | $\begin{bmatrix}8\\-\frac 23\end{bmatrix}$ | $-\displaystyle\frac 92$ | $-\frac 9 2$ |
$\downarrow$

| $\mathcal B$    | $B$ | $B^{-1}$ | $\beta$                              | $\pi^T$                                                | $d_3$                      | $d_4$                       | $\alpha$                                           | $\theta$ | $z$ |
| --------------- | --- | -------- | ------------------------------------ | ------------------------------------------------------ | -------------------------- | --------------------------- | -------------------------------------------------- | -------- | --- |
| $\set{x_2,x_4}$ |     |          | $\begin{bmatrix}6 \\18\end{bmatrix}$ | $\begin{bmatrix}-\frac 5{24}&\frac 1{12}\end{bmatrix}$ | $\displaystyle-\frac5{24}$ | $\displaystyle-\frac 1{12}$ | $\begin{bmatrix}-\frac 1 4\\\frac 16\end{bmatrix}$ | $18$     |     |
$x=[0\ 6\ 0\ 18]$  
#### Quarta iterazione:
tramite i calcoli si vede che $d_1, d_3\geq 0$ quindi l'algoritmo termina
$x=[0\ 6]$  $x_3, x_4$ possono essere riposse dato che erano artificiali

# Ex 2
#CO-L9
$$
\begin{cases}
\min x_1-2x_2\\
2x_1+3x_3=1\\
3x_1+2x_2-x_3=5
\end{cases}
\qquad
\begin{align}
&\mathcal B=\set{x_1,x_2}\\
&B=\begin{bmatrix}2&0\\3 &2\end{bmatrix}\\
&B^{-1}=\begin{bmatrix}0.5&0\\-0.75 &0.5\end{bmatrix}\\
\end{align}
$$

$$
\beta=B^{-1}b=
\begin{bmatrix}
\frac12 \\
\frac74 \\
\end{bmatrix}
\qquad 
\begin{align}
&\text{se uno di questi valori è 0} \\
&\text{significa che la base è degenere.}\end{align}
$$
- $\pi^T=c_BB^{-1}=\begin{bmatrix}2 & -1 \\\end{bmatrix}$
- $d_3=c_3-\pi^TA_3=-7$ significa che c'è una base migliore per $x_3$
$x_3$ entra a far parte della base
- $\alpha_3=B^{-1}A_3=\begin{bmatrix}\frac32 \\-\frac{11}4 \\\end{bmatrix}$
dato che $x_1$ raggiunge $0$ per prima la togliamo dalla base

$\mathcal B=\set{x_3,x_2}$
$\Delta_z=d_3\theta=-\frac 73$ 
se c'erano più iterazioni?
	si sommavano i vari $\theta$ e $d$
Se la base non è degenere allora l'iterazine non sara degenere
	$\theta$ non sarà $0$
# Ex 3
$$
\begin{cases}
\min x_1+x_2+2x_3+4x_4\\
2x_2-3x_4=1\\
x_1-x_4=0\\
-x_1-x_3=1
\end{cases}
$$
1. $\mathcal B=\set{x_2,x_1,x_3}$ è ottima?
2. che valore ha $x$ nella best fesible solution?
3. è degenerate?

$$
B\vdots I
\begin{bmatrix}
2 & 0 & 0 & \vdots & 1 & 0 & 0 \\
0 & 1 & 0 & \vdots & 0 & 1 & 0 \\
0 & -1 & 1 & \vdots & 0 & 0 & 1 \\
\end{bmatrix}\rightarrow
\begin{bmatrix}
1 & 0 & 0 & \vdots & \frac12 & 0 & 0 \\
0 & 1 & 0 & \vdots & 0 & 1 & 0 \\
0 & 0 & 1 & \vdots & 0 & 1 & 1 \\
\end{bmatrix}
=I\vdots B^{-1}
$$
$$
\beta=B^{-1}b=\begin{bmatrix}
x_2 \\
x_1 \\
x_3 \\
\end{bmatrix}=
\begin{bmatrix}
\frac12 \\
0 \\
1 \\
\end{bmatrix}\geq 0
$$
 i tre valori sono $\geq$ quindi fesible
- $\pi^T=c_B^TB^{-1}=[1\ 1\ 2]B^{-1} = \big[\frac 12\ 3\ 2\big]$ 
- $d_4=c_4-\pi^TA_4=\frac {17}2\geq 0$ 
 è la miglior base
1. si
2. $x=\big[0\ \frac12\ 1\ 0\big]$ 
3. si, in $\beta$ c'è uno zero


 