#ML-L14
### Binary Classification
![[Drawing 2025-11-06 11.07.56.excalidraw]]
- $y_i\in\set{0,1}$
- $(x_i,y_i)\quad i=1\dots m$
- $w^Tx+b=\begin{bmatrix}w& b\end{bmatrix}\begin{bmatrix}x \\ 1\end{bmatrix}=w^Tx$
- 
Assumption: i dati sono linearmente separabili
# Perceptron alg.
Computiamo una sequenza $w^{(0)},w^{(1)},\dots$ 

Inizializzazione $w^{(0)}=0$ 
while $\exists$ missclassified point $(x_i,y_i)$:
- Prendi un $j$ (s.t. $(x_j,y_j)$ sia missclassified) in modo randomico
- $w^{(k+1)}=w^{(k)}+y_jx_j$
#### Remark lez precedente
$(x_i,y_i)$ è errato se $y_i\ w^Tx_i<0$

### Theorem
Se i dati sono linearmente separabili    $\exists w_0$ s.t. $y_iw_0^Tx_i>0\quad \forall i$
Allora il perceptron alg. termina in  $k=B^2M^2$ steps
- $B=\max_{i\in[m]}||X||$        $[m]$ sono gli indici di $S$
- $M=\min_{w}||W||$           s.t. $y_iw^Tx_i\ge 1\quad \forall i\in [m]$ 
#### Remark 
 Questo implica che $\exists c>0$ s.t.
 $y_i{w_0^T} x_i\ge c$  $\to$ $y_i\frac{w_0^T}c x_i\ge 1$
 - $\bar {w_0}=\frac{w_0^T}c$     $c=\min y_iw_0^Tx_i>0$ 

##### Proof
$w^{(k+1)}=w^{(k)}+y_ix_i$   dove $i$ è l'index di un istanza misclassified a causa di $w^{(k)}$
Procediamo per  step:
1. $||w^{(k+1)}||$ non cresce troppo velocemente
2. $<w^{(k+1)},w_0>$ cresce veloce abbastanza

###### 1 
$$
\begin{align}
||w^{(k+1)}||^2&=(w^{(k)}+y_ix_i)^T(w^{(k)}+y_ix_i)\\
&=||w^{(k)}||^2+ \underbrace{||x_i||^2}_{\substack{\le B^2\\y=\set{-1,1}}}+\underbrace{2y_i(w^{(k)})^Tx_i}_{<0}\\
\\
||w^{(k+1)}||^2&\le ||w^{(k)}||^2+B^2\\\\&\Rightarrow \Large ||w^{(k)}||^2\le kB^2
\end{align}
$$
###### 2
$$
\begin{align}
<w^{(k)}+y_ix_i,w_0>\ &=\ <w^{(k)},w_0>+ y_iw_0^Tx_i\\
<w^{(k+1)},w_0>\ &\ge\ <w^{(k)},w_0>+1
\\\\\Rightarrow\Large\ <w^{(k)},w_0>\ &\Large\ge\ k 
\end{align}
$$
######
$$\frac{<w^{(k)},w_0>}{\underbrace{||w_0||}_M\ ||w^{(k)}||}\ge \frac k{M\underbrace{||w^{(k)}||}_{\sqrt{kB^2}}}\ge\frac k{M\ \sqrt{kB^2}}=\frac {\sqrt k}{MB}$$
 Inoltre possiamo dire per *cauchy-swartz*(non ho capito)
 $$\left|\frac{<w^{(k)},w_0>}{||w_0||||w^{(k)}}\right|\le1\Rightarrow \frac {\sqrt k}
{BM}\le 1\Rightarrow k\le M^2B^2 $$ 