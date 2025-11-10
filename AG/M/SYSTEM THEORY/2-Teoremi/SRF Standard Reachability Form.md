#ST-L13 #DTCT
E'  una forma alla quale possiamo ridurre tutti i CT e DT non reachable tramite un cambio di base in $X$
Il risultato sulla qualesi basa questa forma è il fatto che $X^R=Im\mathcal R$ (The reachability subspace) è F-invariant ed include $Im\ G$
![[Linear discrete time s.s.m.#Linear DT ssm#General]]
 
Assumiamo che $\Sigma(F,G,H,D)$ è la rappresentazione del sistema rispetto le basi $\mathcal B_x,\mathcal B_u,\mathcal B_y$  in $X=\mathbb R^n, U=\mathbb R^m,Y=\mathbb R^p$ 
Assumiamo che il sistema (0 il paio $(F,G)$)non sia raggiungibile e lasciamo $\rho=dim [Im\mathcal R]=rank \mathcal<n$
Vogliamo ch costruire una matrice $T\in \mathbb R^{n\times n}$ non singular che rappresenta il [[R7 Basis of vector spaces and algebraically equivalent system#Definition algebraically equivalent|cambiamento di base]]  in $X$ quindi w.r.t. la nuova base $\bar {\mathcal B_x}$ del sistema.

Il sistema $\begin{align}&\bar \Sigma(\bar F,\bar G,\bar H,\bar D)=(T^{-1}FT,TG,HT,D)\end{align}$  è in SRF
Iniziamo scegliendo  $\rho$ colonne linearmente indipendenti di $\mathcal R$ che chiamiamo $v_1,v_2,\dots,v_\rho\in \mathbb R^n$ 
possiamo sempre aggiungere $n-\rho$ vettori in $\mathbb R^n$ che chiamiamiamo $w_{\rho+1},\dots,w_n$ s.t.
$\set{v_1,v_2,\dots,v_\rho,w_{rho+1},\dots,w_n}$ sia una base di $\mathbb R^n$e quindi:
$$
T=[v_1|v_2|\dots|v_\rho|w_{\rho+1}|\dots|w_{n-1}]\in \mathbb R^{n\times n} \text{non singular} 
$$
#### Vogliamo capire come sono fatte $\bar F$ e $\bar G$

 Partiamo da $\bar F=T^{-1}FT$ dalla quale deduciamo $T\bar F =FT$ 
$T=[Fv_1|Fv_2|\dots|Fv_\rho|Fw_{\rho+1}|\dots|Fw_{n-1}]=FT=T\bar F=[v_1|v_2|\dots|v_\rho|w_{\rho+1}|\dots|w_{n-1}]\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}$ 
siccome $X^R=Im \mathcal R=<v_1,\dots,v_\rho>$ è F-invariant
allora $Fv_i\in X=<v_1\dots v_\rho>$ i.e.
$Fv_i=\sum_{j=1}^\rho[\bar F]_{ji} v_j$ 
Di conseguenza abbiamo:
$$
\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}

$$

- $F_{11}, 0: \rho$ colonne
- $F_{12},F_{22}: n-\rho$ colonne

- $F_{11},F_{12}:\rho$ righe
- $0,F_22:n-\rho$ righe


Partiamo da $\bar G=T^{-1}G$ dalla quale deduciamo $G=T\bar G$
$\Rightarrow[g_1|g_2|\dots |g_m]=[v_1|v_2|\dots|v_\rho|w_{\rho+1}|\dots|w_{n-1}]\begin{bmatrix}G_1\\ 0\end{bmatrix}$ 
siccome $Im\ G=Im\mathcal R$ #boh è F-invariant
allora $\forall i\in\set{1\dots m} g_i\in <v_1,v_2,\dots,v_g>$
Di conseguenza abbiamo 
$$\begin{bmatrix}G_1\\ 0\end{bmatrix}$$

- $G_1:\rho$ righe
- $0:n-\rho$ righe
#### Riassumendo
Facendo uso della matrice $T$ ottenuta in precedenza per cambiare la basse di $X$ abbiamo ottenuto:
$$
\bar F=\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}
\qquad
\bar G=\begin{bmatrix}G_1\\ 0\end{bmatrix}
\qquad (F_{11},G_1)\text{ è reachable}
$$

Siccome $(F,G)$ e $(\bar F,\bar G)$ sono [[R7 Basis of vector spaces and algebraically equivalent system#Definition algebraically equivalent|algebricamente equivalenti]]  sappiamo che $\bar {\mathcal R}=T^{-1}\mathcal R$ 
e quindi $rank\bar{\mathcal R}=rank \mathcal R =\rho<n$
Tramite [[Cayley-Hamilton's theorem]] possiamo dire che da $F_11^{\rho}G_1$ in poi è tutto inutile per la reachability quindi:
$$
\bar{\mathcal R}=
\begin{bmatrix}
G_1 & F_{11}G_1 & F_{11}^2G_1 & \dots & F_{11}^{\rho-1}G_1 & \cancel{\dots} & \cancel{F_{11}^{n-1}G_1} \\
0 & 0 & 0 & \dots & 0&\dots & 0 \\
\end{bmatrix}
$$
Per hemilton il rank della matrice è $\rho$ e di conseguennza $(F_{11}G_1)$ è **raggiungibile**

# Riassunto 
Un paio$(\bar F,\bar G)$ è in S.F.R. è:
$$
\bar F=\begin{bmatrix}F_{11}&F_{12}\\0& F_{22}\\\end{bmatrix}
\qquad
\bar G=\begin{bmatrix}G_1\\ 0\end{bmatrix}
$$
e $(F_{11}G_{1})$ è un paio raggiungibile
Essendo $\bar F$ *block triangular* questo implica che  $\Delta_{F+GK}(s)=\Delta_{F_{11}+G_1K_1}\cdot\Delta_{F_{22}}$  

**NOTA**
Abbiamo quindi dimostrato che qualunque paio $( F,G)$ non raggiungibile è algebricamente equivalente al paio $(\bar F,\bar G)$  in S.R.F. raggiungibile

Gli autovalori di $F_{11} F_{22}$ non dipendono da $T$ mentre $F_{12}$ può essere portato a $0$


# Exercise
Consideriamo un CT s.s.m.
$$
\dot x(t)=Fx(t)+gu(t)=
\begin{bmatrix}
0 & 1 & 1 \\
2 & 1 & 0 \\
1 & 1 & 2 \\
\end{bmatrix}x(t)+
\begin{bmatrix}
0 \\
1 \\
-1 \\
\end{bmatrix}u(t)
$$
Prova  che il sistema non è reachable e derivalo nella sua S.R.F.
$$
\begin{align}
\mathcal R= [g|Fg|F^2g]=
\begin{bmatrix}
0 & 0 & 0 \\
1 & 1 & 1 \\
-1 & -1 & -1 \\
\end{bmatrix}\qquad rank \mathcal R=1=\rho\\

\end{align}
$$
$$
T=
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 1 \\
-1 & 0 & 0 \\
\end{bmatrix}
\qquad T^{-1}=
\begin{bmatrix}
0 & 0 & -1 \\
1 & 0 & 0 \\
0 & 1 & 1 \\
\end{bmatrix}
$$
$$\begin{align}
\bar F=T^{-1}FT&=
\begin{bmatrix}
0 & 0 & -1 \\
1 & 0 & 0 \\
0 & 1 & 1 \\
\end{bmatrix}
\begin{bmatrix}
0 & 1 & 1 \\
2 & 1 & 0 \\
1 & 1 & 2 \\
\end{bmatrix}
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 1 \\
-1 & 0 & 0 \\
\end{bmatrix}\\
&=
\begin{bmatrix}
-1 & -1 & -2 \\
0 & 1 & 1 \\
3 & 2 & 2 \\
\end{bmatrix}
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 1 \\
-1 & 0 & 0 \\
\end{bmatrix}\\
&=\begin{bmatrix}
{\color {orange}1} & -1 & -1 \\
0 & 0 & 1 \\
0 & 3 & 2 \\
\end{bmatrix}
\end{align}
$$

- $F_{11}$ è $\color{orange}1$ 
- $F_{22}$ è $\begin{bmatrix}0 & 1 \\3 & 2 \\\end{bmatrix}$

$$\bar g=T^{-1}g=\begin{bmatrix}
0 & 0 & -1 \\
1 & 0 & 0 \\
0 & 1 & 1 \\
\end{bmatrix}
\begin{bmatrix}
0 \\
1 \\
-1 \\
\end{bmatrix}
=
\begin{bmatrix}
1 \\
0 \\
0 \\
\end{bmatrix}

$$