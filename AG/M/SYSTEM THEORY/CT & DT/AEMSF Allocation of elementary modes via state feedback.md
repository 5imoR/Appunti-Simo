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


Assumiamo che $(F,G)\in J$ , dato che è reachable ha un reachability index $r=\min\{k:rank[G|FG|\dots|F^{k-1}G]=n\}$
$\Rightarrow$$q\triangleq rank\ G$
$\vdots$ 
$\Rightarrow$$q+\dots+q_2\triangleq rank\ [G|\dots|F^{k-1}G]$ 


#ST-L21-1
$q_1,q_2\dots q_r>0$          $q_1+q_2+\dots+q_r=m$

$k_1,k_2\dots k_q>0$          $k_1+k_2+\dots+k_q=n$

$$
\begin {array}{ccccccc}
\text{Level 1: } &{\color{orange}g_1}& {\color{lightgreen}g_2}&{g_3}&{\color{cyan}g_4}&\dots & {\color{pink}g_{m-1}}&{g_m}\\
\text{Level 2: }  &  {\color{orange}Fg_1}&{\color{lightgreen}Fg_2}&{Fg_3}& {\color{cyan}Fg_4}& \dots & {Fg_{m-1}}&{Fg_m}\\
\text{Level 3: }&{\color{orange}F^2g_1}& {\color{lightgreen}F^2g_2}&{F^2g_3}& {\color{cyan}F^2g_4}& \dots & {F^2g_{m-1}}& {F^2g_m}\\
\vdots\\
\text{Level r: }&{\color{orange}F^{r-1}g_1}& {F^{r-1}g_2}&{F^{r-1}g_3}& {\color{cyan}F^{r-1}g_4}& \dots & {F^{r-1}g_{m-1}}& {F^{r-1}g_m}\\
& k_1=r&k_3=3&&k_2=r&&k_4=1
\end{array}
$$
- Al primo livello si scelgono $q$ colonne linearmente indipendenti e $I_1\triangleq$ {indici delle colonne indipendenti}

- Al secondo livello si scelgono $q_2$  colonne linearmente indipendenti anche con quelle di $I_1$  e quindi si hanno $q+q_2$ colonne lin. ind. $I_2\subseteq I_1$
	Vogliamo provare che posso sempre scegliere $q_2$ colonne sotto le colonne scelte al livello 1 ovvero $I_2\subseteq I_1$  allora:
	$g_i=\sum_{j\in I_1}\alpha_j\ g_j$ 
	$\Rightarrow$$Fg_i=\sum_{j\in I_1} \alpha_j\ Fg_j$ 

- Al terzo livello si scelgono $q_3$  colonne linearmente indipendenti anche con quelle di $I_1, I_2$  e quindi si hanno $q+q_2+q_3$ colonne lin. ind. $I_3\subseteq I_2$ 
	 Vogliamo provare che posso sempre scegliere $I_3\subseteq I_2$, supponendo che $i\notin I_2$ allora:
	$Fg_i\qquad =\sum_{j\in I_1} \alpha_j\ g_j+\sum_{j\in I_1} \beta_j\ Fg_j$ 
	$\Rightarrow$ $F^2g_i\ =\sum_{j\in I_1} \alpha_j\ Fg_j+\sum_{j\in I_1} \beta_j\ F^2g_j$ 

$\dots$  si ripete fino al livello $r$ 

Al livello $r$ si può notare che abbiamo ottenuto $n$ colonne linearmente indipendenti(andando ad unire quelle ottenute ad ogni livello)
Chiamiamo Control invariant e li denomiamo $k_1,\dots k_r$ la lunghezza delle catene verticli ottenute con questo procedimento dalla più grande alla più piccola $k_1\ge k_2\ge\dots\ge k_q$
$k_1,k_2\dots k_q>0$          $k_1+k_2+\dots+k_q=n$

Vogliamo provare che anche se la selezione degli indici ad ogni livello non è unica, quindi la scelta di $I_1\supseteq I_2\supseteq\dots\supseteq I_r$ non è unica, nemmeno le lunghezze delle catene sono unicamente determinate.
#### Proof
Lungezza delle catene $k_1,k_2\dots k_q>0$ 
   $\updownarrow$ Corrispondenza Biiettiva
Numero di catene lunghe $r,r-1,\dots 2,1$  ovvero $q_r,q_{r-1}-q_r,q-q_2$ 
   $\updownarrow$ Corrispondenza Biiettiva
$q_1,q_2\dots q_r>0$ 
#### Ex
Determina il control invariant del seguente paio reachable:
$$
F=
\begin{bmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
1 & 2 & -1 & 0 & 1 \\
0 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 \\
\end{bmatrix}
\qquad G=
\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
1 & -1 & 0 \\
0 & 0 & 0 \\
0 & 2 & 1 \\
\end{bmatrix}
$$

Level 1         $g_1=\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}\quad g_2=\begin{bmatrix} 0 \\ 0 \\ -1 \\ 0 \\ 2 \end{bmatrix}\quad g_3=\begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 1\end{bmatrix}$        $I_1=\set{1,3}\quad q=2$ 

Level 2         $Fg_1=\begin{bmatrix} 0 \\ 1 \\ -1 \\ 0 \\ 0 \end{bmatrix}\quad Fg_2\phantom{=\begin{bmatrix} 0 \\ 0 \\ -1 \\ 0 \\ 2 \end{bmatrix}}\quad Fg_3=\begin{bmatrix} 0 \\ 0 \\ 1 \\ 1 \\ 0\end{bmatrix}$        $I_2=\set{1,3}\quad q=2$ 

Level 3         $F^2g_1=\begin{bmatrix} 1 \\ -1 \\ 3 \\ 0 \\ 1 \end{bmatrix}$  Stop, ho ottenuto $n=5$ colonne indipendenti       $I_3=\set{1}\quad q=1$ 
$k_1= 3\quad k_2 =2$ 
####
Siamo partiti da $S\triangleq\set{(F,G):F\in \mathbb R^{n\times n}, G\in\mathbb R^{n\times m}}$ con $(F,G)$ reachable 
L'[[R8 Equivalence Relations]]  equivale alla [[R7 Basis of vector spaces and algebraically equivalent system|algebric equivalence]]  tra i paii in $S$.
I control invariants sono una famiglia di invarianti per  l'equivalence relation?
Si perchè i control invariant $\set{k_1,k_2\dots k_q}$ sono biiettivi in relazione al rango delle reachability matrices in $1,2\dots r$ steps ma:
$$
(F,G)\sim(\bar F,\bar G)\iff\begin{cases}
\bar F=T^{-1}FT\\\bar G=T^{-1}G\\ \exists T \text{ non singular square}
\end{cases}
$$
$\Rightarrow$ $\forall i =1\dots r\quad rank[\bar G|\bar F\bar G|\dots|\bar F^{i-1}\bar G]=q+q_2+\dots +q_i$ 

**NOTE** I control invariants sono invarianti per lo state feedback che signiufica che se $(F,G)\in S$ allora $\forall K\in \mathbb R^{m\times n} (F+GK,G)\in S$ ha gli stessi control invariants.
Questo segue da: [[State Feedback#Proposition 1|Proposition 1]] 