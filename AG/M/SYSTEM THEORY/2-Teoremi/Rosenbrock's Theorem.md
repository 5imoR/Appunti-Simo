---
tags:
---
#ST-L21-2
## Theorem
Sia $(F,G)$  con $F\in \mathbb R^{n\times n}, G\in\mathbb R^{n\times m}$ un paio reachable e siano $k_1\ge k_2\ge\dots\ge k_q\quad q=rank\ G$ i control invariant del paio $(F,G)$

### Analysis
Per ogni $k\in \mathbb R^{m\times n}$ la matrice $F+GK$  ha $c\le q$  invariant polynomials $\Psi_1(s),\dots,\Psi_c(s)$ ([[Monic polynomial|monic]] ed appartenenti a  $\mathbb R[s]$) che soddisfano:
$$
\begin{align}
\deg \Psi_1(s)&\ge k_1\\
\deg \Psi_1(s)+\deg\Psi_2(s)&\ge k_1+k_2\\
&\ \ \vdots\\
\deg \Psi_1(s)+\dots+\deg\Psi_c(s)&\ge k_1+\dots+k_q=n\\
\end{align}
$$
### Synthesis
Per ogni scelta di $c\le q$ monic polinomials $p_1(s),\dots,p_c(s)\in\mathbb R[s]$ se è soddisfatto:
$$p_c(s)|\dots|p_2(s)|p_s(1)$$
	 ovvero che $p_c(s)$ è un divisore di tutto il resto e via dicendo
e
$$\begin{align}
\deg  p_1(s)&\ge k_1\\
\deg  p_1(s)+\deg p_2(s)&\ge k_1+k_2\\
&\ \ \vdots\\
\deg p_1(s)+\dots+\deg p_c(s)&\ge k_1+\dots+k_q=n\\
\end{align}$$

allora $\exists K \in \mathbb R^{m\times n}$ s.t. gli invariant polinomials $\Psi_i(s)$  di $F+GK$ coincidono con $p_1(s),\dots,p_c(s)$.
$$\Psi_i(s)=p_i(s)\quad \forall i$$
## Riassunto
- Tramite l'analisi partendo da $K$ mi trovo gli invariant polynomials
- Tramite la sintesi partendo dagli invariant polynomials ottengo $K$
## Proof
#ST-L22-1
### Casi limite
- $c=1$
- $(c=q)\wedge(\deg p_i=k_i\quad i=1\dots c_{=q})$  
Saltato un trafilette che non ritengo importante
#### Case 1) c=1
$c=1\iff$ c'è un singolo polinomio invariante $\Psi_1(s)=\Psi_{F+GK}(s)$ con grado: $\deg \Psi_1(s)=n$ allora vuol dire che: [[Cyclic matrix]]
$$\Psi_1(s)=\Delta_{F+GK}(s)=\Psi_{F+GK}(s)\iff F+GK\ \text{  è ciclica}$$ Sappiamo che è sempre così nel caso [[CEAP m=1|m=1]] 
$$\big[(F,g)\text { reachable}\Rightarrow(F_+gk,g)\text{ reachable} \Rightarrow F+gk \text{ cyclic}  \big]$$

Nel caso [[CEAP m =1++|m>1]] andiamo ad applicare Heymann's lemma per rendere il paio reachable per l'$i$-esimo input ed andando ad applicare lo state feedback dall'$i$-esimo input 
$\Rightarrow F+GM_i+g_ik_i$ è cyclic

$(F,G)$ è reachable con i control invariant $k_1\ge k_2\dots k_q\ge 1\quad q= rank\ G$ 

#### Case 2) $(c=q)\wedge(\deg p_i=k_i\quad i=1\dots c_{=q})$ 
Prima risolviamo il problema per un tipo specifico di paia e poi lo generaliziamo per ogni paio raggiungibile.

![[MCCF Multivariable Controllable Canonical Form#Theorem]]
E' facile vedere che il paio $(F_c, G_c)$ in MCCF  è reachable con control invariant pari a $k_1,k_2\dots k_q$  
Vogliamo provare che per questo paio $F_c,G_c$ il *second limit case*  è risolvibile per ogni scelta di $p_1(s),\dots,p_c(s)$
$$
\begin{align}
p_1(s)&=(s-\lambda_1)^{n_{11}}(s-\lambda_2)^{n_{21}}\dots (s-\lambda_r)^{n_{r1}}\quad \sum_{h=1}^r n_{h1}=k_1\\
p_2(s)&=(s-\lambda_1)^{n_{12}}(s-\lambda_2)^{n_{22}}\dots (s-\lambda_r)^{n_{r2}}\quad \sum_{h=1}^r n_{h2}=k_2\\
&\vdots\\
p_q(s)&=(s-\lambda_1)^{n_{1q}}(s-\lambda_2)^{n_{2q}}\dots (s-\lambda_r)^{n_{rq}}\quad \sum_{h=1}^r n_{hq}=k_q\\
\end{align}
$$
La divisibility condition è sempre valida $p_q|\dots|p_2|p_1$ 
$\exists k_c\in \mathbb R^{m\times n}$ s.t. $F_c+G_cK_c$  ha $p_1(s),\dots,p_c(s)$ come invariance polynomial.
Per risolvere il problema dobbiamo prima pulire la matrice $G_cP$, ovvero togliere le colonne superflue. Andiamo quindi a moltiplicare la patrice per $\displaystyle S=\left[\frac{I_q}0\right]$  ottenendo:
$$
G_cPS=
\begin{bmatrix}
0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
\color {orange}1 & \color {orange}* & \color {orange}\dots & \color {orange}* \\
0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
\color {lightgreen}0 & \color {lightgreen}1 & \color {lightgreen}\dots & \color {lightgreen}* \\
\vdots &&& \vdots\\
0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
\color {pink}0 & \color {pink}0 & \dots & \color {pink}1 \\
\end{bmatrix}
$$
Dove le righe $\textcolor{orange}{■}\textcolor{lightgreen}{■}\textcolor{pink}{■}$ sono rispettivamente la $\color {orange}k_1$-esima, $\color {lightgreen}k_1+k_2$-esima . . .  e $\color {pink}k_1+\dots+k_q$-esima e sono le uniche righe non nulle.
Definiamo 
$$\Delta\triangleq
\begin{bmatrix}
1 & * & * & \dots & * \\
0 & 1 & * & \dots & * \\
0 & 0 & \ddots & \ddots & * \\
0 &  \dots &0& 1 &*\\
0  &\dots &0 & 0  &1
\end{bmatrix}
$$
Se applichiamo $\Delta^{-1}$ a destra della nostra matrice otteniamo:
$$
G_cPS\Delta^{-1}=
\begin{bmatrix}
0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
\color {orange}1 & \color {orange}0 & \color {orange}\dots & \color {orange}0\\
0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
\color {lightgreen}0 & \color {lightgreen}1 & \color {lightgreen}\dots & \color {lightgreen}0 \\
\vdots &&& \vdots\\
0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
\color {pink}0 & \color {pink}0 & \dots & \color {pink}1 \\
\end{bmatrix}
$$
Ora sia  $\bar K_c$ tale
$$\bar K_c=
\begin{bmatrix}
k_{11} & k_{12} & \dots & k_{1n} \\
k_{21} & k_{22} & \dots & k_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
k_{q1} & k_{q2} & \dots & k_{qn} \\
\end{bmatrix}
$$ da ottenere:
$$
G_cPS\Delta^{-1}\bar K_c=
G_cPS\Delta^{-1}=
\begin{bmatrix}
0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
k_{11} & k_{12} & \dots & k_{1n} \\0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
k_{21} & k_{22} & \dots & k_{2n} \\
\vdots &&& \vdots\\
0 & 0 & \dots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 &  & 0 \\
k_{q1} & k_{q2} & \dots & k_{qn} \\
\end{bmatrix}
$$
Andando a sommare  $F_c$ con $G_c\underbrace{(PS\Delta^{-1}\bar K_c)}_{\Large K_c}$  otteniamo una matrice con la stessa struttura di $F_c$ e con entry completamente arbitrarie nelle righe con indice $k_1,k_1+k_2\dots,\ \  k_1+\dots+{k_q}{=n}$ 
Quindi scegliamo $\bar K_c$ in modo da ottenere:
- $F_c+G_cK_c$ block diagonal
- il polinomio caratteristico dell' $i$-esimo blocco (di dimensione $k_i\times k_i$) pari a $p_i(s)\ \forall i=1\dots q$ 
Visivamente:
$$
F_c=\begin{bmatrix}
{\color {orange}\begin{bmatrix}
0 & 1 \\
 & \ddots & \ddots \\
 &  & 0 & 1 \\
x & x & \dots & x \\
\end{bmatrix}}&
\\
&
{\color {lightgreen}\begin{bmatrix}
0 & 1 \\
 & \ddots & \ddots \\
 &  & 0 & 1 \\
x & x & \dots & x \\
\end{bmatrix}}&
\\&&\ddots\\&&
&
{\color {pink}\begin{bmatrix}
0 & 1 \\
 & \ddots & \ddots \\
 &  & 0 & 1 \\
x & x & \dots & x \\
\end{bmatrix}}
\end{bmatrix}
$$
Dove nell'ultima riga di ogni  blocco è presente $p_1(s),\dots,p_c(s)$
##### Proof
Vogliamo provare che gli invariant polynomials di $F_C+G_cK_c$ coincidono con $p_1(s),\dots,p_c(s)$ 
	Ripasso [[CCF Controlled Canonical Form]]
- Tutti i blocchi sulla diagonale sono companion matrices e quindi sono cyclic.
Questo Implica che  il polinomio caratteristico dell'$i$-esimo blocco sulla diagonale è $p_i(s)$  allora la Jordan Form di quel blocco sarà del tipo:
$$
{\Large\tilde J_{\color{lightgreen}i}}=
\color{lightgreen}
\begin{bmatrix}
\begin{bmatrix}
\lambda_1 & 1 \\
 & \ddots & \ddots \\
 &  & \ddots & 1 \\
 &  &  & \lambda_1 \\
\end{bmatrix}\\
&
\begin{bmatrix}
\lambda_2 & 1 \\
 & \ddots & \ddots \\
 &  & \ddots & 1 \\
 &  &  & \lambda_2 \\
\end{bmatrix}\\&&\ddots\\
&&&\begin{bmatrix}
\lambda_r & 1 \\
 & \ddots & \ddots \\
 &  & \ddots & 1 \\
 &  &  & \lambda_r \\
\end{bmatrix}
\end{bmatrix}
$$

Di conseguenza la matrice $F_c+G_cK_c$ è simile alla seguente matrice in Jordan form:
$$
F_c+G_cK_c=
\begin{bmatrix}
\color{orange}\tilde J_1\\
&\color{lightgreen}\tilde J_2\\
&&\ddots\\
&&&\color{pink}\tilde J_r\\
\end{bmatrix}
$$

- Dato che  sappiamo che $\forall i n_{i1}\ge n_{i2}\ge\dots\ge n_{iq}$  possiamo affermare che quelli nel primo blocco sono i Jordan miniblock più larghi associati a $\lambda_1,\dots,\lambda_r$ 
$\Rightarrow$ $p_1=\Psi_1(s)$
Questo si può ripetere per ogni  miniblocco.

Do conseguenza $F_c+G_cK_c$ ha esattaamente $p_1(S)\dots p_q(s)$  come invariant polynomials

#ST-L23-1
## Riassunto
Fino ad ora abbiamo visto che:
SE
	$(F_c,G_c)\quad F\in \mathbb R^{n\times n}, G\in\mathbb R^{n\times m}$  in [[MCCF Multivariable Controllable Canonical Form|MCCF]] 
ALLORA
	$\forall$ scelta di $q$ polinomi monici $p_1(s)\dots p_q(s)\in\mathbb R^{n\times m}$ s.t. $p_q|\dots|p_2|p_1$ e $\deg p_i=k_i\ \forall i$  $\exists K_c\in \mathbb R^{m\times n}$ s.t. $F_c+G_cK_c$ abbia $p_1(s)\dots p_q(s)$ come invariant polinomials
