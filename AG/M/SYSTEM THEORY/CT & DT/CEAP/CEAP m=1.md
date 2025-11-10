## Step 1 m=1
![[CCF Controlled Canonical Form#Theorem]]
![[CCF Controlled Canonical Form#Remarks]]
## Se CCF allora [[CEAP Complete Eigenvalue Allocation Problem|CEAP]] è risolvibile
Dato un paio $(F_c,g_c)$ in *CCF* il CEAP è sempre risolvibile
Assumiamo:
$$
F_c
\begin{bmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
0 & 0 & 0 & \ddots & 0 \\
0 & 0 & 0 & \ddots & 1 \\
-a_0 & -a_1 & -a_2 & \dots & -a_{n-1} \\
\end{bmatrix}\qquad
g_c
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0 \\
1 \\
\end{bmatrix}
$$
vogliamo il polinomio caratteristico nella seguente forma:
$$p(s)=s^n+p_{n-1}s^{n-1}+\dots+ p_0$$ allora:
$$
\begin{align}
F_c+g_cK_c&=
\begin{bmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
0 & 0 & 0 & \ddots & 0 \\
0 & 0 & 0 & \ddots & 1 \\
-a_0 & -a_1 & -a_2 & \dots & -a_{n-1} \\
\end{bmatrix}+
\begin{bmatrix}
0&0&\dots&0  \\
0&0&\dots&0  \\
\vdots &\vdots&&\vdots\\
0&0&\dots&0 \\
k_0&k_1&\dots&k_{n-1} \\
\end{bmatrix}\\
&=
\begin{bmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
0 & 0 & 0 & \ddots & 0 \\
0 & 0 & 0 & \ddots & 1 \\
-(a_0-k_0) & -(a_1-k_1) &-(a_2-k_2) & \dots & -(a_{n-1}-k_{n-1}) \\
\end{bmatrix}
\end{align}
$$
Quindi posso mettere$(a_i-k_i)=+\bar a_i\quad \forall i$  ed ottenere:
$$
\begin{align}
\Delta_{Fc+gc+Kc}(s)&=s^n+(a_{n-1}-k_{n-1})s^{n-1}+\dots+a_0-k_0    \\
&=s^n+\qquad p_{n-1}s^{n-1}\qquad+\dots+ p_0
\end{align}
$$

##### Come generalizzo il risultato di un qualunque paio $(F,g)$?
#ST-L17
$$
\begin{align}
(F,g)\text{ reachable}&\color{lightblue}\qquad
\phantom{s}\xrightarrow[det\ T\ne 0]{\large T\in\mathbb R^{n\times n}}\phantom{s}
&\underbrace{(F_c,g_c)}_{CCF}=(T^{-1}FT,T^{-1}g)\\
\\\color{lightblue}\Huge\downarrow
\substack{
\Large\forall p(s)\in \mathbb R[s]\\
\Large\exists k \in \mathbb R^{1\times n}
}
&&{\color{lightblue}\Huge\downarrow
\substack{
\Large\forall p(s)\in \mathbb R[s]\\
\Large\exists k_c \in \mathbb R^{1\times n}
}}\\
\\
(F+gk,g)\text{ reachable} &\color{lightblue}
\phantom{s}\qquad \xleftarrow[]{\large T^{-1}}\phantom{s}
&\underbrace{(F_c+g_ck_c,g_c)}_{CCF}\phantom{ssssss}
\\
\Delta_{F+gk}=p(s)&& \Delta_{F_c+g_ck_c}=p(s)\phantom{ssssss}
\end{align}
$$

$F_c+g_ck_c\quad=\quad T^{-1}FT+T^{-1}gk_c\quad=\quad T^{-1}[F+g\underbrace{k_cT^{-1}}_{\Huge k}]T$

### Proposition
Consideriamo un paio $(F,g)$ con $F\in \mathbb R^{n\times m}$ e $g\in\mathbb R^n$ 
- $\forall p(s)\in\mathbb R[s]$ monico di grado $n$  $\exists k\in\mathbb R^{1\times n}$    s.t.         $\Delta_{F+gk}(s)\equiv p(s)\iff(F,g)$ è reachable

Se $(F,g)$ non è reachable e $F_{22}$ è la matrice del non reachable subsystem allora:
- dato $p(s)\in\mathbb R[s]$  monico di grado $n$ $\exists k\in \mathbb R^{1\times n}$s.t. $\Delta_{F+gk}(s)\equiv p(s)\iff$                                  $p(s)$ è un multiplo di $\Delta_{F_{22}}(s)$  ($p(s)=\Delta_{F_{22}}(s)\cdot \bar p(s)$)
#### Proof
$\Rightarrow$ deriva da [[State Feedback#Proposition 2|P2]] 
$\Leftarrow$ visto che $(F,g)$ non è raggiungibile w.l.o.g. possiamo assumere che: ([[SRF Standard Reachability Form|SRF]])
$$\bar F=\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}
\qquad
\bar g=\begin{bmatrix}g_1\\ 0\end{bmatrix}
\qquad (F_{11},g_1)\text{ è reachable}$$
Allora esiste $k=[k_1|0]$ 
$$
\bar F=\begin{bmatrix}F_{11}+g_1k_1&F_{12}\\0& F_{22}\\\end{bmatrix}
$$
Per   [[State Feedback#Proposition 1|P1]]  possiamo  dire che è polynomial equivalent a $\bar p(s)$ 
Allora:
$$\Delta_{F+gk}(s)= p(s))=\Delta_{F_{22}}(s)\cdot \bar p(s)$$

#### Ex 1
Dentro quaderno rosso prima lezione nera
#### Ex 2
Dentro quaderno rosso prima lezione nera


## SISO Reachable system: the effect of state Feedback
#ST-L18-1
Consideriamo un sistema SISO di dimensione $n$ in CCF
![[CCF Controlled Canonical Form#Theorem]]
Con l'aggiunta di $H_c$
$$
H_c=\begin{bmatrix}
b_0&b_1 &\dots b_{k-1}
\end{bmatrix}
$$
 **Qual'è la funzione di trasferimento di $\Sigma_c=(F_c,g_c,H_c)$?**$$ \begin{align} W_c(s)&=H_c(sIn-F_c)^{-1}g_c\\ &=H_c{\color{lightblue}\left[\frac {adj(sIn-F_c)}{\det(sIn-F_c)}\right]}g_c\\&=\frac1{s^n+a_{n-1}s^{n-1}+\ldots+a_1s+a_0}\cdot\begin{bmatrix}b_0&b_1 &\dots b_{k-1}\end{bmatrix}\cdot adj(sIn-F_c)\cdot\begin{bmatrix}0 \\0 \\\vdots \\0 \\1 \\\end{bmatrix} \end{align}$$
	$\textcolor{lightblue}{■}$ Data una matrice quadrata $M$ di dimensione $n\times n$ l'adjoint di $M$ è definita come:
	$$[adj\ M]_{ij}=(-1)^{i+j}\det \underbrace{M_{-j-i}}_{\substack{\text{M senza}\\\text{ j riga}\\\text{i colonna}}}\qquad \forall i,j \in \set {1,\dots n}$$
	Mentre $det(sIn-F_c)$ è il polinomio caratteristico  $\Delta_{Fc}(s)$ 
Vogliamo calcolare solo l'ultima colonna di $adj(sIn-F_c)$: 
$$
\begin{align}
adj(sIn-F_c) =adj&=
\begin{bmatrix}
s & -1 & 0 & \dots & 0 \\
0 & s & -1 & \dots & 0 \\
0 & 0 & s & \ddots & 0 \\
0 & 0 & 0 & \ddots & -1 \\
a_0 & a_1 & a_2 & \dots & s+a_{n-1} \\
\end{bmatrix}\\&=
\begin{bmatrix}
* & * & * & \dots & 1 \\
* & * & * & \dots & s \\
* & * & * & \ddots & s^2\\
* & * & * & \ddots & s^{n-2} \\
* & * & * & \dots & s^{n-1} \\
\end{bmatrix}
\Huge\substack{
\leftarrow\ \ (-1)^{1+n}(-1)^{n-1}\\\\\\\\\\
\leftarrow\ \ (-1)^{2+n}s(-1)^{n-2}\\\\\\\\\\
\leftarrow\ \ (-1)^{3+n}s(-1)^{n-3}\\\\\\\\\\
\\\\\\\\\\
\leftarrow\ \ (-1)^{n+n}s^{n-1}\quad
}
\end{align}
$$
Di conseguenza:

$$\begin{align}
W_c(s)&=H_c(sIn-F_c)^{-1}g_c\\
&=\frac1{s^n+a_{n-1}s^{n-1}\ldots+a_1s_1+s_0}
\cdot\begin{bmatrix}b_0&b_1 &\dots b_{k-1}\end{bmatrix}
\cdot adj(sIn-F_c)
\cdot\begin{bmatrix}1 \\s \\\vdots \\s^{n-2} \\s^{n-1} \\\end{bmatrix} \\\\
W_c(s)&=\frac {b_{n-1}s^{n-1}+\ldots+b_1s+b_0}   {s^n+a_{n-1}s^{n-1}+\ldots+a_1s+a_0}
\end{align}$$

Possiamo rispondere alla domanda dicendo che:
Per un sistema SISO in CCF la funzione di trasferimento è:
$$W_c(s)=\frac {b_{n-1}s^{n-1}+\ldots+b_1s+b_0}   {s^n+a_{n-1}s^{n-1}+\ldots+a_1s+a_0}$$
- $H_c$ fornisce il numeratore
- $F_c$ fornisce il denominatore


Se applichiamo lo state feedback con $K=\begin{bmatrix}k_0 & k_1 & \dots & k_{n-1} \\\end{bmatrix}$  allora:
$$
\Sigma_{kc}=W_c(s)=\frac 
{b_{n-1}s^{n-1}+\ldots+b_1s+b_0}
{s^n+(a_{n-1}-k_{n-1})s^{n-1}+\ldots+(a_1-k_1)s+a_0-k_0}
$$
- $H_c$ fornisce il numeratore
- $F_c+g_ck_c$ fornisce il denominatore

#### Conclusione
- Se parto da un sistema SISO in CCF $\Sigma_c=(F_c,g_c,H_c)$ dove applico lo state feedback ad esso ($K_c\in \mathbb R^{1\times n}$)  ottengouna funzione di trasferimento dove il numeratore coincide al numeratore della funzione di trasferimento iniziale($W_c$) mentre il denominatoreè un polinomio monico arbitrario di grado $n$. Questo vale PRIMA delle cancellazioni, non DOPO
	Quindi abbiamo sempre da riferirci alla rapresentazione della funzione di trasferimento nella quale il denominatore coincide con il polinomio caratteristico della system matrix

- Il risultato si estende per ogni SISO Reachable system $\Sigma=(F,g,H)$ dato che sono sempre [[R7 Basis of vector spaces and algebraically equivalent system|algebricamente equivalenti]]  ad un SISO in CCF e due sistemi algebraicamente equivalenti hanno la stessa funzione di trasferimento
# Ex 1
Assumiamo $\Sigma_c=(F_c,g_c,H_c)$ con
$$
F_c=\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 2 & 3 \\
\end{bmatrix}
g_c=\begin{bmatrix}
0 \\ 0 \\ 1 \\
\end{bmatrix}
H_c=\begin{bmatrix}
4 & 5 & 6 \\
\end{bmatrix}
$$
E' possibile trovare $K_c\in \mathbb R^{1\times 3}$ s.t. la funzione di trasferimento $\Sigma_{kc}$ sia $\displaystyle\frac 1{s+1}$ ?

$$
\begin{align}
W_c(s)=\frac{6s^{2} + 5s + 4}{s^{3} - 3s^{2} - 2s - 1}=\frac 1{s+1}\\
({6s^{2} + 5s + 4})({s+1})=1({s^{3} - 3s^{2} - 2s - 1})
\end{align}
$$
Si vede facilmente che non è possibile perchè $s^2$ al numeratore ha coefficiente $6$ e diventerebbe $6s^3$ 
Facciamo finta di voler ottenere $\displaystyle\frac 6{s+1}$
$$
\left(\frac{6s^{2} + 5s + 4}6\right)({s+1})=s^3+\frac{11}6s^2+\frac3 2s+\frac 23
$$
Per trovare $K$ deve essere che:
$$
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1+k_0 & 2+k_1 & 3+k_2 \\
\end{bmatrix}=
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
-\frac 23 &\frac32 &-\frac{11}6 \\
\end{bmatrix}
$$
