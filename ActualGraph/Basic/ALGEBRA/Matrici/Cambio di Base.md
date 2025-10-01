[[Matrici]]

#### Cambio di base
$A$ è la matrice corrispondente alla funzione $f:V \rightarrow W$ quindi per fare un cambio di base dal vettore $v$ al vettore $w$ basterà fare $A\cdot v =w$ 
$$
\begin{bmatrix}
\mu_1 \\
\mu_2 \\
\vdots \\
\mu_n
\end{bmatrix}^\underline{W}
= 
M^{\underline{W}}_{\underline{V}}(f)
\begin{bmatrix}
\lambda_1 \\
\lambda_2 \\
\vdots \\
\lambda_n
\end{bmatrix}^\underline{V}
$$
#### Matrici di cambiamento di base
Basi di $V$
$\underline{v}=\{v_1,...,v_n\}$
$\underline{v'}=\{v'_1,...,v'_n\}$
$v \in V$ 
$v$ si può scrivere tramite entrambe le basi, vanno entrambe bene, cambiano i coefficenti
$$
\begin{bmatrix}
\lambda_1 \\
\lambda_2 \\
\vdots \\
\lambda_n
\end{bmatrix}^{\underline{v}}
\qquad
\begin{bmatrix}
\lambda'_1 \\
\lambda'_2 \\
\vdots \\
\lambda'_n
\end{bmatrix}^{\underline{v'}}
$$
$$
id:V\rightarrow V
\quad
v_i = \sum_{h=1}^n p_{hi}\cdot v_h'
\qquad \qquad
P=(p_{hi})= M^{\underline{v'}}_{\underline{v}}(id)
\quad
n\times n
$$
In $P$ le colonne corrispondono ai coefficienti per passare da $v_i$ a $v_i'$
Se $Q$ è la matrice di cambiamento di base da  da $v_i'$ a $v_i$ allora $Q\cdot P$ è la matrice identica $I$
$P$ e $Q$ sono matrici $n\times n$ invertibili

##### Effetto delle matrici di cambiamento di base sulle coordinate dei vettori
$$
\begin{aligned}
v &= \sum_i \lambda_i v_i
= \sum_i \lambda_i\left(\sum_h p_{hi}\cdot v_h'\right) \\
&= \sum_{i,h}\left(p_{hi}\cdot \lambda_i \right)v_h'
= \sum_h\left(\sum_i p_{hi}\cdot\lambda_i\right)v_h' \\
&= \sum_h \lambda_h' \cdot v_h'
\end{aligned}
$$
e quindi:
- La matrice $P$, se moltiplicata alle coordinate del vettore, trasforma le coordinate di $v$ rispetto alla base $\underline v$ nelle coordinate dello stesso valore $v$ rispetto alla base $\underline v'$ 
$$
\begin{bmatrix}
\lambda'_1 \\
\lambda'_2 \\
\vdots \\
\lambda'_n
\end{bmatrix}^{\underline{v'}}
=
P\cdot
\begin{bmatrix}
\lambda_1 \\
\lambda_2 \\
\vdots \\
\lambda_n
\end{bmatrix}^{\underline{v}}
$$
- La matrice P, se moltiplicata per i vettori di base, trasforma i vettori di $\underline v'$ nei vettori di $\underline v$ 

$$
\{v_1,...,v_n\} = P\cdot 
\{v'_1,...,v'_n\}
$$
$$
\underline{v} = P \cdot 
\underline{v'}
$$
Nel codominio vige la stessa regola e quindi, chiamata $S$ la matrice di cambiamento di base del codominio si ha:
$S$ matrice $n\times n$ 
$$
\begin{bmatrix}
\mu'_1 \\
\mu'_2 \\
\vdots \\
\mu'_m
\end{bmatrix}^{\underline{w'}}
=
S\cdot
\begin{bmatrix}
\mu_1 \\
\mu_2 \\
\vdots \\
\mu_m
\end{bmatrix}^{\underline{w}}
$$

#### Ricapitolando

$$
\begin{aligned}
\begin{bmatrix}
\mu'_1 \\
\mu'_2 \\
\vdots \\
\mu'_m
\end{bmatrix}^{\underline{w'}}
&= A'\cdot
\begin{bmatrix}
\lambda_1 \\
\lambda_2 \\
\vdots \\
\lambda_n
\end{bmatrix}^{\underline{v'}}
= A'\cdot P\cdot
\begin{bmatrix}
\lambda_1 \\
\lambda_2 \\
\vdots \\
\lambda_n
\end{bmatrix}^{\underline{v}}
\\[1em] % <-- spazio tra le due righe
&= S\cdot
\begin{bmatrix}
\mu_1 \\
\mu_2 \\
\vdots \\
\mu_m
\end{bmatrix}^{\underline{w}}
= S\cdot A\cdot
\begin{bmatrix}
\lambda_1 \\
\lambda_2 \\
\vdots \\
\lambda_n
\end{bmatrix}^{\underline{v}}
\end{aligned}
$$
#matrici_cambiamento_di_base
Questo comporta che
$$
S\cdot A = A' \cdot P
$$
$$
A = S^{-1}\cdot A' \cdot P
\qquad
A' = S\cdot A \cdot P^{-1}
$$

# Esempi
### Cambio di base: Calcolare $A$
####  Data la funzione:
$$
f
\begin{bmatrix}
x \\ y\\ z
\end{bmatrix} =
\begin{bmatrix}
3x &-2y &z\\
x &&2z
\end{bmatrix}
 \qquad f:V \rightarrow W
$$
##### E le seguenti basi (canoniche)
$$

v_1=
\begin{bmatrix}
1 \\ 0\\ 0
\end{bmatrix}
v_2=
\begin{bmatrix}
0 \\ 1\\ 0
\end{bmatrix}
v_3=
\begin{bmatrix}
0 \\ 0\\ 1
\end{bmatrix}
\qquad
w_1=
\begin{bmatrix}
1 \\ 0
\end{bmatrix}
w_2=
\begin{bmatrix}
0 \\ 1
\end{bmatrix}
$$

###### Calcolo prima colonna
$$
f(v_1)=
f\begin{bmatrix}
1 \\ 0\\ 0
\end{bmatrix}=
3 \cdot\begin{bmatrix}
1 \\ 0
\end{bmatrix}+
1 \cdot\begin{bmatrix}
0 \\ 1
\end{bmatrix}=
\begin{bmatrix}
3 \\ 1
\end{bmatrix}
$$
###### Calcolo seconda colonna
$$
f(v_1)=
f\begin{bmatrix}
0 \\ 1\\ 0
\end{bmatrix}=
-2 \cdot\begin{bmatrix}
1 \\ 0
\end{bmatrix}+
0 \cdot\begin{bmatrix}
0 \\ 1
\end{bmatrix}=
\begin{bmatrix}
-2 \\ 0
\end{bmatrix}
$$
###### Calcolo terza colonna
$$
f(v_1)=
f\begin{bmatrix}
0 \\ 0\\ 1
\end{bmatrix}=
1 \cdot\begin{bmatrix}
1 \\ 0
\end{bmatrix}+
2 \cdot\begin{bmatrix}
0 \\ 1
\end{bmatrix}=
\begin{bmatrix}
1 \\ 2
\end{bmatrix}
$$
###### Risultato
$$
A=
\begin{bmatrix}
3 & -2 & 1 \\
1 & 0 & 2 \\
\end{bmatrix}
$$
##### E le seguenti basi (codominio canonico)
$$

v_1=
\begin{bmatrix}
1 \\ 0\\ 2
\end{bmatrix}
v_2=
\begin{bmatrix}
-1 \\ 1\\ 1
\end{bmatrix}
v_3=
\begin{bmatrix}
0 \\ -1\\ 3
\end{bmatrix}
\qquad
w_1=
\begin{bmatrix}
1 \\ 0
\end{bmatrix}
w_2=
\begin{bmatrix}
0 \\ 1
\end{bmatrix}
$$

###### Calcolo prima colonna
$$
f(v_1)=
f\begin{bmatrix}
1 \\ 0\\ 2
\end{bmatrix}=
[(3\cdot 1) +0+(2\cdot1)] 
\cdot\begin{bmatrix}
1 \\ 0
\end{bmatrix}+
 [(1\cdot 1) +0+(2\cdot2)] 
\cdot\begin{bmatrix}
0 \\ 1
\end{bmatrix}=
\begin{bmatrix}
5 \\ 5
\end{bmatrix}
$$
###### Calcolo seconda colonna
$$
f(v_1)=
f\begin{bmatrix}
-1 \\ 1\\ 1
\end{bmatrix}=
-4 \cdot\begin{bmatrix}
1 \\ 0
\end{bmatrix}+
1 \cdot\begin{bmatrix}
0 \\ 1
\end{bmatrix}=
\begin{bmatrix}
-4 \\ 1
\end{bmatrix}
$$
###### Calcolo terza colonna
$$
f(v_1)=
f\begin{bmatrix}
0 \\ -1\\ 3
\end{bmatrix}=
5 \cdot\begin{bmatrix}
1 \\ 0
\end{bmatrix}+
6 \cdot\begin{bmatrix}
0 \\ 1
\end{bmatrix}=
\begin{bmatrix}
5 \\ 6
\end{bmatrix}
$$
###### Risultato
$$
A=
\begin{bmatrix}
5 & -4 & 5 \\
5 & 1  &  6 \\
\end{bmatrix}
$$

##### E le seguenti basi (niente canonico)
$$

v_1=
\begin{bmatrix}
1 \\ 0\\ 2
\end{bmatrix}
v_2=
\begin{bmatrix}
-1 \\ 1\\ 1
\end{bmatrix}
v_3=
\begin{bmatrix}
0 \\ -1\\ 3
\end{bmatrix}
\qquad
w_1=
\begin{bmatrix}
2 \\ 3
\end{bmatrix}
w_2=
\begin{bmatrix}
-1 \\ 1
\end{bmatrix}
$$

###### Calcolo prima colonna
$$
f(v_1)=
f\begin{bmatrix}
1 \\ 0\\ 2
\end{bmatrix}=

\begin{bmatrix}
5 \\ 5
\end{bmatrix} = 
\alpha_1\cdot
\begin{bmatrix}
2 \\ 3
\end{bmatrix}

 +\alpha_2\cdot
\begin{bmatrix}
-1 \\ 1
\end{bmatrix} = 
\begin{bmatrix}
2 \\ -1
\end{bmatrix} 
$$
###### Calcolo seconda colonna
$$
f(v_1)=
f\begin{bmatrix}
-1 \\ 1\\ 1
\end{bmatrix}=

\begin{bmatrix}
-4 \\ 1
\end{bmatrix} = 
\alpha_1\cdot
\begin{bmatrix}
2 \\ 3
\end{bmatrix}

 +\alpha_2\cdot
\begin{bmatrix}
-1 \\ 1
\end{bmatrix} = 
\begin{bmatrix}
-\frac{3}{5}  \\ \frac{14}{5}
\end{bmatrix} 
$$
###### Calcolo terza colonna
$$
f(v_1)=
f\begin{bmatrix}
0 \\ -1\\ 3
\end{bmatrix}=

\begin{bmatrix}
5 \\ 6
\end{bmatrix} = 
\alpha_1\cdot
\begin{bmatrix}
2 \\ 3
\end{bmatrix}

 +\alpha_2\cdot
\begin{bmatrix}
-1 \\ 1
\end{bmatrix} = 
\begin{bmatrix}
\frac{11}{5}  \\ -\frac{3}{5}
\end{bmatrix} 
$$
###### Risultato
$$
A=
\begin{bmatrix}
2 & -\frac{3}{5} & \frac{11}{5} \\
-1 & \frac{14}{5}  & -\frac{3}{5}  \\
\end{bmatrix}
$$


##### Con le formule del cambiamento di base
###### Matrice di cambiamento di base in $V$ sono:
Si ottine moltiplicando i valori della matrice formata da $\underline v'$ e $\underline v$
$$
M^{\underline{v}}_{\underline{v'}}(id)
=
\begin{bmatrix}
1 &-1 &0\\
0 & 1 &-1\\
2 & 1 & 3
\end{bmatrix}
$$
è la matrice le cui colonne sono le cordinate dei vettori $v'_1, v'_2, v'_3$ (della base $\underline{v'}$) rispetto alla base $\underline{v} = \{v_1,v_2,v_3\}$.

$M^{\underline{v'}}_{\underline{v}}(id)$ è più complicata, è l'inversa di sua sorella
- Attualmente per calcolare l'inversa si deve fare un sistema di equazioni del tipo: $v_1 =\alpha \cdot v_1'+ \alpha' \cdot v_2'+\alpha'' \cdot v_3'$  dove $\alpha, \alpha', \alpha''$ sono la prima colonna della matrice
$$
\begin{cases}
 v_1 =\alpha \cdot v_1'+ \alpha' \cdot v_2'+\alpha'' \cdot v_3'\\
 v_2 =\beta \cdot v_1'+ \beta' \cdot v_2'+\beta'' \cdot v_3'\\
 v_3 =\gamma \cdot v_1'+ \gamma' \cdot v_2'+\gamma'' \cdot v_3'
\end{cases}
\qquad
M^{\underline{v'}}_{\underline{v}}(id)=
\begin{bmatrix}
\alpha   & \beta   & \gamma\\
\alpha'  & \beta'  & \gamma'\\
\alpha'' & \beta'' & \gamma''
\end{bmatrix}
$$
###### Matrice di cambiamento di base in $W$ sono:
Si ottine moltiplicando i valori della matrice formata da $\underline w'$ e $\underline w$
$$
M^{\underline{w}}_{\underline{w'}}(id)
=
\begin{bmatrix}
2 &-1 \\
3 & 1 
\end{bmatrix}
$$
è la matrice le cui colonne sono le cordinate dei vettori $w'_1, w'_2$ (della base $\underline{w'}$) rispetto alla base $\underline{w} = \{w_1,w_2\}$.

$M^{\underline{w'}}_{\underline{w}}(id)$ è più complicata, è l'inversa di sua sorella
- Attualmente per calcolare l'inversa si deve fare un sistema di equazioni del tipo: $v_1 =\alpha \cdot w_1'+ \alpha' \cdot w_2'$  dove $\alpha, \alpha'$ sono la prima colonna della matrice
$$
\begin{cases}
 w_1 =\alpha \cdot w_1'+ \alpha' \cdot w_2'\\
 w_2 =\beta \cdot w_1'+ \beta' \cdot w_2'\\
\end{cases}
\qquad
M^{\underline{w'}}_{\underline{w}}(id)=
\begin{bmatrix}
\alpha   & \beta\\
\alpha'  & \beta'  

\end{bmatrix}
$$



###### V e W canoniche
$$
A=M^{\underline{w}}_{\underline{v}}(f) =
\begin{bmatrix}
3 &-2 &1\\
1 & 0 &2
\end{bmatrix}
$$

Si moltipoltiplica la prima colonna per $v_1$ la seconda per $v_2$ e la terza per $v_3$ 

###### W canonica
$$
A=M^{\underline{w}}_{\underline{v'}}(f) 
=
M^{\underline{w}}_{\underline{v}}(f) \cdot M^{\underline{v}}_{\underline{v'}}(id)  
=
\begin{bmatrix}
3 &-2 &1\\
1 & 0 &2
\end{bmatrix}
\cdot
\begin{bmatrix}
1 &-1 &0\\
0 & 1 &-1\\
2 & 1 & 3
\end{bmatrix}
=
\begin{bmatrix}
5 & -4 & 5 \\
5 & 1  &  6 \\
\end{bmatrix}
$$
###### Niente di canonico
$$
\begin{align}
A
&=
M^{\underline{w'}}_{\underline{v'}}(f) 
=
M^{\underline{w'}}_{\underline{w}}(id) 
\cdot
M^{\underline{w}}_{\underline{v}}(f) 
\cdot
M^{\underline{v}}_{\underline{v'}}(id)  \\
&=
\begin{bmatrix}
2 &-1 \\
3 & 1 
\end{bmatrix}^{-1}
\cdot
\begin{bmatrix}
3 &-2 &1\\
1 & 0 &2
\end{bmatrix}
\cdot
\begin{bmatrix}
1 &-1 &0\\
0 & 1 &-1\\
2 & 1 & 3
\end{bmatrix}
=
\begin{bmatrix}
2 & -\frac{3}{5} & \frac{11}{5} \\
-1 & \frac{14}{5}  & -\frac{3}{5}  \\
\end{bmatrix}
\end{align}
$$

