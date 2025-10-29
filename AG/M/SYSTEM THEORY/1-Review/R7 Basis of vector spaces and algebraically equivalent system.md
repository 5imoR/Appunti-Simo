#ST_L9
### Definition algebraically equivalent
Dati due s.s.m. $\Sigma (F,G,H,D)$ e $\bar \Sigma(\bar F,\bar G,\bar H,\bar D)$ 
- con stessa dimensione
- con lo stesso numero di input e output
Diciamo che $\Sigma$ e $\bar\Sigma$ sono algebricamente equivalenti  se rappresentano lo stesso stistema w.r.t. a 2 basi differenti in $X$ che significa che $\exists n\times n$ matrice non singolare $T$ s.t.
- $\bar F =T^{-1}FT$
- $\bar G =TG$
- $\bar H = HT$
- $\bar D=D$

### Basis of vector spaces
#ST-L8
Consideriamo l'esempio di
![[Linear discrete time s.s.m.#Linear DT ssm#General]]

In generale possiamo sempre assumere che  abbiamo basi fissate in ognuno dei nostri tre spazi vettoriali $X=\mathbb R^n\qquad U=\mathbb R^m\qquad Y=\mathbb R^p$  ovvero $\mathcal B_x\quad \mathcal B_u\quad \mathcal B_y$
 quindi $x(t)\quad u(t)\quad y(t)$ sono:
 -  le cordinate degli stati al tempo $t$ rispetto a $\mathcal B_x$ 
 - le cordinate del input al tempo $t$ rispetto a $\mathcal B_u$ 
 - le cordinate del output al tempo $t$ rispetto a $\mathcal B_y$
 Cosa significa?
 Assumendo che $\mathcal B_x=\set{v_1,v_2,\ldots v_m}$ questo significa che lo stato al tempo $t$ è:
 $$
 \sum_{i=1}^m x_i(t)v_i=[v_1|v_2|\ldots|v_n]\begin{bmatrix}x_1(t)\\x_2(t)\\
 \vdots\\x_n(t)\end{bmatrix}_{=x(t)}
 $$
 Cosa succede alla rappresentazione del sistema se cambiamo la base di $X$ 
 - da: $\mathcal B_x=\set{v_1,\ldots,v_m}$
 - a:  $\bar{\mathcal B_x}=\set{\bar v_1,\ldots,\bar v_m}$
 
 #ST-L9
 $$
 \begin{align}
 &\bar v_j=\sum_{i=1}^mv_it_{ij}=
 \begin{bmatrix}
 v_1&v_2&\dots &v_n
 \end{bmatrix}
 \begin{bmatrix}
 t_{1j}\\t_{2j}\\\vdots\\t_{nj}
 \end{bmatrix}\\
 &\Rightarrow 
 \begin{bmatrix}
 \bar v_1&\bar v_2&\dots &\bar v_n
 \end{bmatrix}=
 \begin{bmatrix}
 v_1&v_2&\dots &v_n
 \end{bmatrix}
 \begin{bmatrix}
 t_{11}&t_{12}&\dots&t_{1n}\\t_{21}&t_{22}&\dots&t_{2n}\\\vdots&\vdots&\ddots&\vdots\\t_{1n}&t_{2n}&\dots&t_{nn}
 \end{bmatrix}
 \end{align}
 $$ 
 - $T\in\mathbb C^{n \times n}$ matrice non singolare quadrata
 
 Di conseguenza possiamo anche dire l'opposto:
 $$
\begin{align}
 \begin{bmatrix}
 v_1&v_2&\dots &v_n
 \end{bmatrix}=
 \begin{bmatrix}
 \bar v_1&\bar v_2&\dots &\bar v_n
 \end{bmatrix}
 \begin{bmatrix}
 s_{11}&s_{12}&\dots&s_{1n}\\s_{21}&s_{22}&\dots&s_{2n}\\\vdots&\vdots&\ddots&\vdots\\s_{1n}&s_{2n}&\dots&s_{nn}
 \end{bmatrix}
 \end{align}
 
 $$ 
 - $S\in\mathbb C^{n \times n}$ matrice non singolare quadrata

Quindi possiamo dire che 
$\begin{bmatrix}v_1&v_2&\dots &v_n\end{bmatrix}=\begin{bmatrix}v_1&v_2&\dots &v_n\end{bmatrix}\Big[T\Big]\Big[S\Big]$ 
Questo implica che  $T\ S=Im\quad T=S^{-1}$  


Se $\bar x(t)$ è il vettore delle coordinate dello stato al tempo $t$ w.r.t. la nuova base $\bar {\mathcal B_x}$ si vuole sapere la relazione tra $\bar x(t)$ e $x(t)$ 

$\begin{bmatrix}\bar v_1&\bar v_2&\dots &\bar v_n\end{bmatrix}\Big[\bar X(t)\Big]=$ stato al tempo $t$ $= \begin{bmatrix}v_1&v_2&\dots &v_n\end{bmatrix}\Big[X(t)\Big]$
$\Rightarrow\begin{bmatrix}\bar v_1&\bar v_2&\dots &\bar v_n\end{bmatrix}\Big[\bar X(t)\Big]=\begin{bmatrix}v_1&v_2&\dots &v_n\end{bmatrix}\Big[T\Big]\Big[\bar X(t)\Big]$ 
Quindi si può capire che:
$\Big[T\Big]\Big[\bar X(t)\Big]=\Big[X(t)\Big]\qquad\Rightarrow \qquad\Big[\bar X(t)\Big]=\Big[T\Big]^{-1}\Big[ X(t)\Big]$

Come risultato otteniamo:
$$
\begin{align}
\bar x(t+1)&=T^{-1}x(t+1)\\&=T^{-1}Fx(t)+T^{-1}Gu(t)\\&=T^{-1}FTx(t)+T^{-1}Gu(t)\\
\end{align}
$$$$
\begin{cases}
\bar x(t+1)=T^{-1}FxT(t)+T^{-1}Gu(t)\\\\
y(t)=HT\bar x(t)+Du(t)
\end{cases}
$$

| Vecchia base                    | Nuova base                                                                                |
| ------------------------------- | ----------------------------------------------------------------------------------------- |
| $\mathcal B_x\{v_1,\dots v_n\}$ | $\bar{\mathcal B_x}\{\bar v_1,\dots\bar v_n\}$                                            |
| $x(t)$                          | $\bar x(t)=T^{-1}x(t)$                                                                    |
| $\Sigma (F,G,H,D)$              | $\begin{align}&\bar \Sigma(\bar F,\bar G,\bar H,\bar D)\\&=(T^{-1}FT,TG,HT,D)\end{align}$ |
