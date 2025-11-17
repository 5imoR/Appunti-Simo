Assumiamo di avere  un paio $(F,G)$ reachable con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$  reachable e di conseguenza  $\forall p(s)\in \mathbb R[s]$ monic di grado $n$ $\exists K\in \mathbb R^{m\times n}$ s.t. $\Delta_{F+GK}(s)\equiv p(s)$ 
### Q1
Cosa possiamo dire della [[R3 Jordan Form]] di $F+GK$ ?
In generale non molto. Unica cosa conosciamo i blocchi ma non il partizionamento in miniblocchi.
Ci sono alcune ecezzioni:
- Se tutti gli zero di $p(s)=\Delta_{F+GK}(s)$ sono distinti ($\lambda_i$ ha molt. alg. unitaria) si ottiene: $J_{F+GK}=\begin{bmatrix}\lambda_1 \\ & \lambda_2 \\ & & \ddots \\ &  &  & \lambda_r \\\end{bmatrix}$ 
- se iniziamo con un single input reachable system $(m=1)$  sappiamo che:
	se $(F,g)$ è reachable  $\to$  $(F+gK,g)$ è reachable e $\Delta_{F+gK}=p(s)$
	$M$ è  [[Cyclic matrix|cyclic]] $\iff \exists g\in \mathbb R^n$ s.t. $(M,g)$ è reachable
- Siccome $(F+gK,g)$ è raggiungiblie la matrice $F+gK$  è cyclica ma questo significa che la sua forma di jordan ha un singolo miniblocco per ogni valore. Di conseguenza se:
	$p(s)=(s-\lambda_1)^{n_1}\dots(s-\lambda_r)^{n_r}\quad \lambda i\ne \lambda_j\quad i\ne j\quad n_i>0$ allora:
	$$
	J_{F+GK}=
	\begin{bmatrix}
\begin{bmatrix}
\lambda_1 & 1 \\
 & \lambda_1 & 1 \\
 &  & \lambda_1 \\
\end{bmatrix}\\
& \begin{bmatrix}
\lambda_2 & 1 \\
 & \lambda_2 & \ddots \\
 &  & \ddots & 1 \\
 &  &  & \lambda_2 \\
\end{bmatrix}\\
&&\begin{bmatrix}
\lambda_r & 1 \\
 & \lambda_r & \ddots \\
 &  & \ddots & 1 \\
 &  &  & \lambda_r \\
\end{bmatrix}
\end{bmatrix}
	$$
Questo è ciò che succede se ad un paio $(F,G)$ con $m$ input applico [[Heymann's Lemma]] e poi faccio feedback da un singolo input a partire dal Reachable single input pair
$(F+GM_i,g_i)\longrightarrow(F+GM_i+g_ik_i)$ è ciclica perchè $F(+GM_i+g_ik_i,g_i)$ è raggiungibile
(Si vedrà che è la soluzione peggiore in alcuni casi)
### Problem
Dato un paio  $(F,G)$ reachable con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$ reachable 
	Control invariant $k_1,k_2\dots k_q$
Quali sono le possibili $J$ [[R3 Jordan Form]] che posso ottenere dalle matrici $F+GK$ con $K\in R^{m\times n}$
	Invariant polynomials $\Psi_1(s),\dots,\Psi_c(s)$ 
#ST-L20-1
(Quello che andiamo a fare è trovare dei vincoli su $\Psi_i$ basati su $k_i$)
Per introdurre control invariant e invariant polynomials serve un ripasso di ![[R8 Equivalence Relations]]
### Example 1
Assumiamo $S=\mathbb C^{n\times n}$  scegliamo come equivalence relation in $S$ la similitudine tra le matrici:
$$A,B\in S=\mathbb C^{n\times n} \Rightarrow A\sim B\ \text{ if } \exists T\in\mathbb C^{n\times n}\ s.t.\ B=T^{-1}AT$$
Flexibility e symmetry sono trivial
Transitivity:$A\sim B\to B=T^{-1}AT\quad B\sim C\to C=S^{-1}BS \Rightarrow C=S^{-1}T^{-1}ATS$ 
Il polinomio caratteristico  è un invariante per la similarity relationship dato che: $B=T^{-1}AT\Rightarrow \Delta_A(s)=\Delta_B(s)$ 
	Non è completa dato che l'inverso non vale

La Jordan Form è sia un invariant che un complete invariant per la similarity, dato  $A,B\in S=\mathbb C^{n\times n}\Rightarrow A\sim J_A\ B\sim J_B$ allora se $A\sim B$ per transitività $J_A\sim J_B$ 

Ma $J_A\sim J_B$ equivale a dire che sono la stessa matrice di Jordan di conseguenza per la transitività $A\sim B$ 
Vogliamo associare una famiglia di polinomi ad una matrice $J\in S$
![[R3 Jordan Form#Jordan Form]]
Definiamo gli invariant polinomials associati a $J$ come seguono:
- $\Psi_1(s)=(s-\lambda_1)^{n_{11}}(s-\lambda_2)^{n_{21}}\dots(s-\lambda_r)^{n_{r1}}$
$\qquad \qquad\vdots$
- $\Psi_c(s)=(s-\lambda_1)^{n_{1c}}(s-\lambda_2)^{n_{2c}}\dots(s-\lambda_r)^{n_{rc}}$ 
	questo è l'ultimo polinomio ottenuto con grado $\ge 1$ 
#### Remark
- Sono tutti polinomi monici. Se usiamo $a(s) | b(s)$ per dire che $a(s)$ è un divisore di $b(s)$ allora:$\Psi_c(s)|\Psi_{c-1}(s)|\dots|\Psi_2(s)|\Psi_1(s)$
- il minimal annihilating polynomial $\Psi_1(s)\equiv\Psi_J(s)$
- il caratteristic polynomial  $\Psi_1(s)\cdot\Psi_2(s)\cdot\dots\cdot\Psi_c(s)\equiv \Delta_J(s)$ 
- $c=\max_i s_i=\max_i(\#\text{ di Jordan miniblock associati a } \lambda_i)=\max_i(\text{geom. mult. di }\lambda_i)$
$c$ è detto cyclicity index               $J$ è ciclica se $c=1$
#### Esempi
##### 1
$$
\begin{bmatrix}
\begin{bmatrix}
2 & 1 \\
 & 2 \\
 &  & 2 & 1 \\
 &  &  & 2 \\
\end{bmatrix}\\
&
\begin{bmatrix}
1 & 1 \\
 & 1 & 1 \\
 &  & 1 \\
 &  &  & 1 \\
 &  &  &  & 1 \\
\end{bmatrix}
\end{bmatrix}
$$
$c= \max_i(s_i)= 3$
- $\Psi_1(s)= (s-2)^2(s-1)^3$
- $\Psi_2(s)= (s-2)^2(s-1)$
- $\Psi_3(s)=(s-1)$ 
##### 2
$$\begin{bmatrix}
0 \\
 & 2 \\
 &  & 1 & 1 \\
 &  &  & 1 \\
 &  &  &  & 2 & 1 \\
 &  &  &  &  & 2 \\
 &  &  &  &  &  & 0 & 1 \\
 &  &  &  &  &  &  & 0 & 1 \\
 &  &  &  &  &  &  &  & 0 \\
\end{bmatrix}$$
$c= \max_i(s_i)= 2$
- $\Psi_1(s)= s^3(s-1)^2(s-2)^2$
- $\Psi_2(s)= s(s-2)$

##### 3
- $\Psi_1(s)= s^2(s+1)^3(s-2)$
- $\Psi_2(s)= s(s+1)$
- $\Psi_3(s)=s$ 
$$\begin{bmatrix}
2 \\
 & 0 & 1 \\
 &  & 0 \\
 &  &  & 0 \\
 &  &  &  & 0 \\
 &  &  &  &  & -1 & 1 \\
 &  &  &  &  &  & -1 & 1 \\
 &  &  &  &  &  &  & -1 \\
 &  &  &  &  &  &  &  & -1 \\
\end{bmatrix}$$
####
E' immediato vedere che si tratta di una corrispondenza biiettiva
$J \longleftrightarrow\set {\Psi_1(s) \dots \Psi_c(s)}$
$\Rightarrow$ La famiglia di invarianti è un invariante completo per la similarità.
### Example 2
Assumiamo: $S\triangleq\set{(F,G):F\in\mathbb R^{n\times n}\ G\in\mathbb R^{n\times m}\ (F,G)\text{ reachable}}$ e consideriamo [[R7 Basis of vector spaces and algebraically equivalent system|equivalenza algebrica]]  tra i paii $(F_1,G_1)\sim(F_2,G_2)$ se $\exists T\in \mathbb R^{n\times n}$ s.t. $(F_2=T^{-1}F_1T)$