[[Matrici]]
Si possono fare operazioni sulle righe e sulle colonne una dopo l'altra nello stesso svolgimento

$$
A=
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
$$
si vole azzerare tutti gli elementi sotto la diagonale tramite le *operazioni elementari* delle matrici
$$
A=
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
0 & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & a_{m2} & \dots & a_{mn}
\end{bmatrix} 
\rightarrow
\begin{bmatrix}
* & * & \dots & * \\
0 & * & \dots & * \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & *
\end{bmatrix} 
$$
Nella forma a scala il primo coefficiente diverso a $0$ di ogni riga deve essere a destra di quello della riga precendente.
Il rango coincide con il numero di righe non nulle (ovvero il numero di $pivot \neq 0$)

**Facendo i calcoli sulle colonne per non complicarti la vita fai la trasposta e usa le righe**
#### Codice
TODO metti codice che lo fa
#### Esempi ed Esercizi
##### Esempio 1
$$
\begin{align}
A&=
\begin{bmatrix}
2 & -1 & 3 \\
1 & 4 & -2 \\
3 & 0 & 1 \\
\end{bmatrix}
\xrightarrow{\substack{scambio \\riga\; 1 \; e \; 2}}
\begin{bmatrix}
1 & 4 & -2 \\
2 & -1 & 3 \\
3 & 0 & 1 \\
\end{bmatrix}
\xrightarrow{\substack{riga2-2\cdot riga1\\ riga3-3\cdot riga1}}
\begin{bmatrix}
1 & 4 & -2 \\
0 & -9 & 7 \\
0 & -12 & 7 \\
\end{bmatrix}\\\\
&=
\begin{bmatrix}
1 & 4 & -2 \\
0 & -9 & 7 \\
0 & -12 & 7 \\
\end{bmatrix}
\xrightarrow{\substack{riga3-4/3\cdot riga2}}
\begin{bmatrix}
1 & 4 & -2 \\
0 & -9 & 7 \\
0 & 0 & -7/3 \\
\end{bmatrix}
\end{align}
$$
Questo dice che tutte le righe sono linearmente indipendenti
##### Esempio 2
$$
\begin{align}
A&=
\begin{bmatrix}
-2 & 3 & 1 & 0 &4 \\
4 & -6 & -2 & 2 &1 \\
-6 & 9 & 3 & 1 &3 \\
\end{bmatrix}
\xrightarrow{\substack{riga2-(-2)\cdot riga1\\ riga3-3\cdot riga1}}
\begin{bmatrix}
-2 & 3 & 1 & 0 &4 \\
0 & 0 & 0 & 2 &9 \\
0 & 0 & 0 & 1 &-9 \\
\end{bmatrix}
\xrightarrow{\substack{riga3-1/2\cdot riga2}}
\\\\
&=
\begin{bmatrix}
-2 & 3 & 1 & 0 &4 \\
0 & 0 & 0 & 2 &9 \\
0 & 0 & 0 & 0 & 27/2 \\
\end{bmatrix}
\end{align}
$$
3 righe non nulle allora rango = 3
##### Esempio 3
$$
\begin{align}
A&=
\begin{bmatrix}
0 & 2 & -1 & 3\\
1 & -2 & 4 & 1\\
2 & -2 & 7 & 5\\
\end{bmatrix}
\xrightarrow{\substack{scambio \\riga\; 1 \; e \; 2}}
\begin{bmatrix}
1 & -2 & 4 & 1\\
0 & 2 & -1 & 3\\
2 & -2 & 7 & 5\\
\end{bmatrix}
\xrightarrow{\substack{riga3-2\cdot riga1}}
\begin{bmatrix}
1 & -2 & 4 & 1\\
0 & 2 & -1 & 3\\
0 & 2 & -1 & 3\\
\end{bmatrix}
\\\\
&=
\begin{bmatrix}
1 & -2 & 4 & 1\\
0 & 2 & -1 & 3\\
0 & 2 & -1 & 3\\
\end{bmatrix}
\xrightarrow{\substack{riga3- riga2}}
\begin{bmatrix}
1 & -2 & 4 & 1\\
0 & 2 & -1 & 3\\
0 & 0 & 0 & 0\\
\end{bmatrix}
\end{align}
$$
2 righe non nulle allora rango = 2
##### Esercizio
Sia $U$ il sottospazio vettoriale di $\mathbb{R}^5$ generato dai vettori seguenti
$$
\begin{align}
v_1 = 
\begin{bmatrix}
1\\-3\\0\\ 2\\1\\
\end{bmatrix}
v_2 = 
\begin{bmatrix}
3\\ 1\\1\\-1\\2\\
\end{bmatrix}
v_3 = 
\begin{bmatrix}
0\\2\\-2\\ 0\\1\\
\end{bmatrix}
v_4 = 
\begin{bmatrix}
4\\0\\-1\\ 1\\4\\
\end{bmatrix}
v_5 = 
\begin{bmatrix}
2\\-8\\2\\ 4\\1
\end{bmatrix}
\end{align}
$$
Trovare dimensione e base di $U$
###### Soluzione
Prima si faceva con sistemi di equazioni, troppo lungo ora:
$$
\begin{align}
\begin{bmatrix}
1&-3&0& 2&1\\
3& 1&1&-1&2\\
0&2&-2& 0&1\\
4&0&-1& 1&4\\
2&-8&2& 4&1
\end{bmatrix}
\xrightarrow{\substack{riga2-3\cdot riga1\\riga4-4\cdot riga1\\riga5-2\cdot riga1\\ }}
\begin{bmatrix}
1&-3&0& 2&1\\
0& 10&1&-7&1\\
0&2&-2& 0&1\\
0&12&-1& 7&0\\
0&-2&2& 0&-1
\end{bmatrix}\\
\xrightarrow{\substack{scambio \\riga\; 3 \; e \; 2}}
\begin{bmatrix}
1&-3&0& 2&1\\
0&2&-2& 0&1\\
0& 10&1&-7&1\\
0&12&-1& 7&0\\
0&-2&2& 0&-1
\end{bmatrix}
\xrightarrow{\substack{riga3-5\cdot riga2\\riga4-6\cdot riga2\\riga5-2\cdot riga2\\ }}
\begin{bmatrix}
1&-3&0& 2&1\\
0&2&-2& 0&1\\
0& 0&11&-7&-6\\
0&0&11& -7&-6\\
0&0&0& 0&0
\end{bmatrix}\\
\xrightarrow{\substack{riga4- riga3}}
\begin{bmatrix}
1&-3&0& 2&1\\
0&2&-2& 0&1\\
0& 0&11&-7&-6\\
0&0&0& 0&0\\
0&0&0& 0&0
\end{bmatrix}\qquad
\begin{bmatrix}
v_1\\
v_3\\
v_2\\
v_4\\
v_5
\end{bmatrix}
\qquad\qquad\qquad
\end{align}

$$
3 righe non nulle =rango 3
$dim(U) = 3$
per quanto riguarda la base  i vettori indipendenti sono $v_1, v_2, v_3$ quindi sono loro a comporre una base
###

Riprendendo il ragionamento delle operazioni elementari delle matrici :
$$
\begin {align}
\underbrace{S(...)\cdot S(...)\cdot M(...)\cdot P(...)}
_{\text{B}}
\cdot A = A'\\

B\cdot A = A'\quad allora\quad B\cdot(A\ \vdots\ I) =(BA\ \vdots \ B)
\end{align}
$$
##### Esempio
$$
\begin{align}
\begin{bmatrix}
3 & -1 & 4 &\vdots & 1 & 0 & 0 & 0 \\
2 & -2 & 1 &\vdots & 0 & 1 & 0 & 0 \\
0 & 4 & 5  &\vdots & 0 & 0 & 1 & 0 \\
-1 & 3 & 2 &\vdots & 0 & 0 & 0 & 1
\end{bmatrix}
\rightarrow
\begin{bmatrix}
-1 & 3 & 2 &\vdots & 0 & 0 & 0 & 1 \\
0 & 4 & 5 &\vdots & 0 & 1 & 0 & 2 \\
0 & 0 & 0  &\vdots & 0 & -1 & 1 & -2 \\
0 & 0 & 0 &\vdots & 1 & -2 & 0 & -1
\end{bmatrix}
\\
\quad
\underbrace{\hspace{2.7cm}}_{\text{A}}
\quad
\underbrace{\hspace{2.8cm}}_{\text{I}}
\quad\qquad
\underbrace{\hspace{2.4cm}}_{\text{A}}
\quad
\underbrace{\hspace{3.4cm}}_{\text{B}}
\;\;\\
\end{align}
$$
##### Esercizio 1
$U$ sottospazio di $\mathbb{R}^4$  generato da:
$$
u_1=
\begin{bmatrix}
2\\ 0\\ 1 \\ -1
\end{bmatrix}
u_2=
\begin{bmatrix}
1 \\ 1\\2\\0
\end{bmatrix}
u_3=
\begin{bmatrix}
4\\-2 \\ -1\\ -3
\end{bmatrix}
$$
1. Calcolare la dimensione di $U$
$$
\begin{bmatrix}
2 & 0 & 1 & -1\\
1 & 1 & 2 & 0\\
4 & -2 & -1 & -3\\
\end{bmatrix}
\rightarrow
\begin{bmatrix}
* & * & * & *\\
0 & * & * & *\\
0 & 0 & * & *\\
\end{bmatrix}
$$
2. Trovare le relazioni di dipendenza lineare tra i vettori $u_1, u_2, u_3$ 
$$
\begin{align}
\begin{bmatrix}
2 & 0 & 1 & -1   &\vdots & 1 & 0 & 0\\
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0\\\
4 & -2 & -1 & -3 &\vdots & 0 & 0 & 1\\\
\end{bmatrix}
\xrightarrow{\substack{scambio \\riga\; 1 \; e \; 2}}{}
\begin{bmatrix}
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0\\\
2 & 0 & 1 & -1   &\vdots & 1 & 0 & 0\\
4 & -2 & -1 & -3 &\vdots & 0 & 0 & 1\\\
\end{bmatrix}
\xrightarrow{\substack{riga2-2\cdot riga1\\riga3-4\cdot riga1}}\\
\begin{bmatrix}
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0\\\
0 & -2 & -3 & -1   &\vdots & 1 & -2 & 0\\
0 & -6 & -9 & -3 &\vdots & 0 & -4 & 1\\\
\end{bmatrix}
\xrightarrow{\substack{riga3-3\cdot riga2}}
\begin{bmatrix}
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0\\\
0 & -2 & -3 & -1   &\vdots & 1 & -2 & 0\\
0 & 0 & 0 & 0 &\vdots & -3 & -4 & 1\\\
\end{bmatrix}\quad\quad
\end{align}
$$ L'ultima riga di $B$ ci dice che: $-3 u_1 + 3u_2 +u_3 = \vec 0$  quindi $u_3 = 3u_1-2u_2$ 
che è la relazione di dipendenza tra i vettori

##### Esercizio 2
Trovare dim. e base di $U\cap W$ 
$$
\begin{align}
U = <u_1,u_2> \subset \mathbb{R}^4
\qquad \qquad\quad
W = <w_1,w_2,w_3> \subset \mathbb{R}^4\quad
\\
u_1=
\begin{bmatrix}
2\\ 0\\ 1 \\ -1
\end{bmatrix}
u_2=
\begin{bmatrix}
1 \\ 1\\2\\0
\end{bmatrix}
\qquad
w_1=
\begin{bmatrix}
-1\\ 1\\ 0 \\ 0
\end{bmatrix}
w_2=
\begin{bmatrix}
-2 \\ 0\\1\\0
\end{bmatrix}
w_3=
\begin{bmatrix}
0\\0 \\ 0\\ 1
\end{bmatrix}
\end{align}
$$

$$
\begin{align}
&\begin{bmatrix}
2 & 0 & 1 & -1   &\vdots & 1 & 0 & 0& 0 & 0 \\
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0& 0 & 0 \\
-1 & 1 & 0 & 0   &\vdots & 0 & 0 & 1& 0 & 0 \\
-2 & 0 & 1 & 0   &\vdots & 0 & 0 & 0& 1 & 0 \\
0 & 0 & 0 & 1    &\vdots & 0 & 0 & 0& 0 & 1 \\
\end{bmatrix}
\xrightarrow{\substack{scambio \\riga\; 1 \; e \; 2}}
\begin{bmatrix}
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0& 0 & 0 \\
2 & 0 & 1 & -1   &\vdots & 1 & 0 & 0& 0 & 0 \\
-1 & 1 & 0 & 0   &\vdots & 0 & 0 & 1& 0 & 0 \\
-2 & 0 & 1 & 0   &\vdots & 0 & 0 & 0& 1 & 0 \\
0 & 0 & 0 & 1    &\vdots & 0 & 0 & 0& 0 & 1 \\
\end{bmatrix}
\xrightarrow{\substack{riga2-2\cdot riga1\\riga3- riga1\\riga4+2\cdot  riga1}}\\
&\begin{bmatrix}
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0& 0 & 0 \\
0 & -2 & -3 & -1   &\vdots & 1 & -2 & 0& 0 & 0 \\
0 & 2 & 2 & 0   &\vdots & 0 & 1 & 1& 0 & 0 \\
0 & 2 & 5 & 0   &\vdots & 0 & 2 & 0& 1 & 0 \\
0 & 0 & 0 & 1    &\vdots & 0 & 0 & 0& 0 & 1 \\
\end{bmatrix}
\xrightarrow{\substack{riga3+ riga2\\riga4+ riga2}}
\begin{bmatrix}
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0& 0 & 0 \\
0 & -2 & -3 & -1   &\vdots & 1 & -2 & 0& 0 & 0 \\
0 & 0 & -1 & -1   &\vdots & 1 & -1 & 1& 0 & 0 \\
0 & 0 & 2 & -1   &\vdots & 1 & 0 & 0& 1 & 0 \\
0 & 0 & 0 & 1    &\vdots & 0 & 0 & 0& 0 & 1 \\
\end{bmatrix}
\xrightarrow{\substack{riga4+2\cdot riga3}}\\&
\begin{bmatrix}
1 & 1 & 2 & 0    &\vdots & 0 & 1 & 0& 0 & 0 \\
0 & -2 & -3 & -1   &\vdots & 1 & -2 & 0& 0 & 0 \\
0 & 0 & -1 & -1   &\vdots & 1 & 1 & 1& 0 & 0 \\
0 & 0 & 0 & -3   &\vdots & 3 & -2 & 2& 1 & 0 \\
0 & 0 & 0 & 1    &\vdots & 0 & 0 & 0& 0 & 1 \\
\end{bmatrix}
\xrightarrow{\substack{3\cdot riga5+ riga4}}
\begin{bmatrix}
1 & 1 & 2 & 0    &\vdots & 0 & 1  & 0& 0 & 0 \\
0 & -2 & -3 & -1 &\vdots & 1 & -2 & 0& 0 & 0 \\
0 & 0 & -1 & -1  &\vdots & 1 & 1  & 1& 0 & 0 \\
0 & 0 & 0 & -3   &\vdots & 3 & -2 & 2& 1 & 0 \\
0 & 0 & 0 & 1    &\vdots & 3 & -2 & 2& 1 & 3 \\
\end{bmatrix}
\end{align}
$$
Dalla ultima riga possiamo dire che:
$3u_1 -2u_2 +2w_1+1w_2+3w_3 = \vec 0$
Quindi la base sarà:
- $v= 3u_1-2u_2$
oppure
- $v=-2w_1-w_2-3w_3$ 