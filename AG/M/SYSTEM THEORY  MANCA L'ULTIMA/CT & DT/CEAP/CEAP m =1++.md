#ST-L18-2
## Step 2 m>1
Se partiamo con un paio $(F,G)$ reachable con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$ con $m>1$
ed $\exists i\in\set{1,\dots,m}$ s.t. $(F,g_i)$ dove $g_i$ rappresenta l'i-esima colonna di $G$ allora $\forall$ polinomio monico $p(s)\in\mathbb R[s]$ di grado $n$  $\exists k_i\in \mathbb R^{1\times n}$ s.t. $\Delta_{F+g_ik_i}(s)\equiv p(s)$ 
	Ovvero possiamo modellare la matrice del feedback per andare ad "attivare" solo la colonna $g_i$ interessata se $(F,g_i)$ è reachable

IDEA: Proviamo che se un paio $(F,G)$ è reachable da $m$ input possiamo sempre renderlo raggiungibile per un singolo input tramite uno state feedback preliminario e sucessivamente applicare a quell' single input un secondo state feedback per ottenere il polinomio caratteristico desiderato.
![[Heymann's Lemma#Theorem]]
![[Heymann's Lemma#Proof]]

# Conclusion
#ST-L19-1
$$\begin{align}
(F,G)\text{ reachable}&\color{lightblue}\qquad
\phantom{s}\xrightarrow[\text{Heymann's Lemma}]{\Large\exists M_i\in\mathbb R^{m\times n}\ g_i\ne \underline0}
&\begin{array}{c}
(F+GM_i,G)\ \text{ reachable}\\
(F+GM_i,g_i)\ \text{ reachable}\\
\end{array}\\
\\\color{lightblue}\Huge\downarrow
&&{\color{lightblue}\Huge\downarrow
\substack{
{\Large\forall p(s)\in \mathbb R[s]}\large\text{monic grado n}\\
\Large\exists K_i \in \mathbb R^{1\times n}
}}\\
\\
&\color{lightblue}\phantom{s}\xrightarrow
[
\Large\exists K_i \in \mathbb R^{m\times n}\text{s.t.} \Delta_{F+GK}(s)\equiv p(s)
]{\forall p(s)\in \mathbb R(s)\text{monic grado n}
}&
\begin{array}{c}
(F+GM_i+g_iK_i,G)\ \text{ reachable}\\
(F+GM_i+g_iK_i,g_i)\ \text{ reachable}\\
\end{array}
\end{align}$$
Il passaggio diretto equivale a dire che:
$F+GM_i+g_iK_i=F+GM_i+\begin{bmatrix}g_1 & \dots & g_i & \dots \\\end{bmatrix}\begin{bmatrix}0 \\\vdots \\k_i \\\vdots \\\end{bmatrix} =F+G\underbrace{\left[M_i+\begin{bmatrix}0 \\\vdots \\k_i \\\vdots \\\end{bmatrix} \right]}_K$  
### Proposition
 Sia $(F,G)$ un paio con  $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$  
 - Il CEAP è risolvibile $\iff$ $(F,G)$ è reachable
 - Se $(F,G)$ non è reachable dato $p(s)\in\mathbb R[s]$ monico di grado $n$ $\exists  K\in \mathbb R ^{m\times n}$ s.t. $\Delta_{F+GK}(s)=p(s)$ 
	$\iff p(s)$ è un multiplo di $\Delta _{F_{22}}$ (il polinomio caratteristico del non reachable subsystem)

## Ex 
Considera CT ssm
$$\dot x(t)=Fx(t)+Gu(t)=\begin{bmatrix}
2 & 0 & 0 \\
1 & 1 & -1 \\
0 & 0 & 1 \\
\end{bmatrix}x(t)+
\begin{bmatrix}
1 & 0 \\
0 & 0 \\
0 & 1 \\
\end{bmatrix}u(t)

$$
Determina se possibile $K\in \mathbb R^{2\times 3}$ s.t. $\Delta_{F+GK}(s)=(s+1)^3$ 
### Sol
#### Percorso Meccanico

- controlliamo se raggiungibile
$$\mathcal R=[g_1|g_2||Fg_1|Fg_2||F^2g_1|F^2g_2]=\begin{bmatrix}
1 & 0 & || & 2 & 0 & || & 4 & 0 \\
0 & 0 & || & 1 & -1 & || & 3 & -2 \\
0 & 1 & || & 0 & 1 & || & 0 & 1 \\
\end{bmatrix}$$
ha rango 3 quindi è raggiungibile e di conseguenza il problema è risolvibile.
Il sistema è reachable per un singolo input?
$$\begin{align}
i=1\quad \mathcal R_1\triangleq[g_1|Fg_1|F^2g_1]=
\begin{bmatrix}
1 & 2 & 4 \\
0 & 1 & 3 \\
0 & 0 & 0 \\
\end{bmatrix}
\text{rango 2$\to$ non reachable}\\
i=2\quad \mathcal R_2\triangleq[g_2|Fg_2|F^2g_2]=
\begin{bmatrix}
0 & 0 & 0 \\
0 & -1 & -2 \\
1 & 1 & 1 \\
\end{bmatrix}
\text{rango 2$\to$ non reachable}
\end{align}$$
Applichiamo [[Heymann's Lemma]]  e rendiamo il sistema reachable per il secondo input:
$$g_2=
\begin{bmatrix}
0 \\ 0 \\ 1 \\
\end{bmatrix}\quad
Fg_2=
\begin{bmatrix}
0 \\ -1 \\ 1 \\
\end{bmatrix}
\quad \nu_1=2
\qquad
g_1=
\begin{bmatrix}
1 \\ 0 \\ 0 \\
\end{bmatrix}\quad
\nu_2=1
$$
$$
Q=[g_2|Fg_2||g_1]=
\begin{bmatrix}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 1 & 0 \\
\end{bmatrix}
$$
$$
S=
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}
$$
$$M_2=SQ^{-1}=\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
0 & 1 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0 \\
\end{bmatrix}=
\begin{bmatrix}
0 & -1 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}
$$
$$
F+GM_2=\begin{bmatrix}
2 & 0 & 0 \\
1 & 1 & -1 \\
0 & 0 & 1 \\
\end{bmatrix}+
\begin{bmatrix}
1 & 0 \\
0 & 0 \\
0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
0 & -1 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}=
\begin{bmatrix}
2 & -1 & 0 \\
1 & 1 & -1 \\
0 & 0 & 1 \\
\end{bmatrix}
$$
Controlliamo se la matrice appena ottenuta è reachable per $g_2$
$$
\mathcal R_2=
\begin{bmatrix}
0 & 0 & 1 \\
0 & -1 & -2 \\
1 & 1 & 1 \\
\end{bmatrix}
\text{reachable}
$$
Ora introduciamo $k_2=[a\ b\ c] \in \mathbb R^{1\times 3}$ s.t. $\Delta_{F+GM_2+g_2k_2}(s)=(s+1)^3=s^3+3s^2+3s+1$
$$
{F+GM_2+g_2k_2}=\begin{bmatrix}
2 & -1 & 0 \\
1 & 1 & -1 \\
0 & 0 & 1 \\
\end{bmatrix}+
\begin{bmatrix}
0 \\ 0 \\ 1 \\
\end{bmatrix}
\begin{bmatrix}
a & b & c \\
\end{bmatrix}=
\begin{bmatrix}
2 & -1 & 0 \\
1 & 1 & -1 \\
a & b & c+1 \\
\end{bmatrix}
$$

$$
\Delta_{F+GM_2+g_2k_2}(s)=s^3+(-4-c)s^2+(6+b+3c)s+(-3-a-2b-3c)
$$
$$
\begin{cases}
-4-c=3\\
6+b+3c=3\\
-3-a-2b-3c=1
\end{cases}
\begin{cases}
c=-7\\
b=18\\
a=-19
\end{cases}
$$
$$K_2=[-19 ||18||-7]\quad K=M_2+\begin{bmatrix}
0 \\ k_2 \\
\end{bmatrix}
=
\begin{bmatrix}
0 & -1 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}+
\begin{bmatrix}
0 & 0 & 0 \\
-19 &18 &-7 \\
\end{bmatrix}=
\begin{bmatrix}
0 & -1 & 0 \\
-19 &18 &-7 \\
\end{bmatrix}
$$
#### Percorso Veloce
Sappiamo che $(F,G)$ è reachable e quindi risolvibile,
settiamo 
$$K=\begin{bmatrix}
a_1 & b_1 & c_1 \\
a_2 & b_2 & c_2 \\
\end{bmatrix}\text{ then }
F+GK=\begin{bmatrix}
2 & 0 & 0 \\
1 & 1 & -1 \\
0 & 0 & 1 \\
\end{bmatrix}+
\begin{bmatrix}
1 & 0 \\
0 & 0 \\
0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
a_1 & b_1 & c_1 \\
a_2 & b_2 & c_2 \\
\end{bmatrix}=
\begin{bmatrix}
2+a_1 & b_1 & c_1 \\
1 & 1 & -1 \\
a_2 & b_2 & c_2+1 \\
\end{bmatrix}
$$
- mettiamo $a_2, b_2= 0$ ottenendo una matrice triangolare a blocchi( quindi il polinomio caratteristico  è dato  dai blocchi sulla diagonale)
- $c_1= 0$ non ci serve, potrebbe essere qualunque valore ma gli $0$ sono belli
$$
\begin{bmatrix}
2+a_1 & b_1 & 0 \\
1 & 1 & -1 \\
0 & 0 & c_2+1 \\
\end{bmatrix}
$$
$(s-2-a_1)(s-1)-b_1=s^2+(-3-a_1)s+(2+a_1-b_1)\equiv s^2+2s+1$ 
$c_2+1=-1\to c_2=-2$

$$
K=
\begin{bmatrix}
-5 & -4 & 0 \\
0 & 0 & -2 \\
\end{bmatrix}
$$ 