#ST-L2
[[SYSTEM THEORY]]
![[Jordan Form#Jordan Form]]

## Power of a Jordan mini-block
#ST-L3
Tramite gli esempi precedenti possiamo dire che:
- il numero di $\lambda_i$ presenti nella matrice ci da la sua molteplicità algebrica
- il numero di mini-block relativi allo stesso $\lambda_i$ ci da la sua molteplicità geometrica
- la dimensione del primo mini-block ($n_{i1}$) è pari all'esponente relativo allo stesso $\lambda_i$ in $\Psi_J(s)$

Ora consideriamo di avere un mini-block $J$  di grandezza $\nu$ con un qualche autovalore complesso
$$
J_\lambda=\begin{bmatrix}
\lambda&1\\
&\lambda&1\\
&&\ddots&\ddots\\
&&&\lambda&1
\end{bmatrix}
$$
### Caso $\lambda=0$ 
$$
J_0=\begin{bmatrix}
0&1\\
&0&1\\
&&\ddots&\ddots\\
&&&0&1
\end{bmatrix}
$$
Le varie potenze saranno:
$$
\begin{align}
J_0^0&=I   &J_o^1&=J_0 \\
J_0^2&=\begin{bmatrix}
0&0&1\\
&0&0&1\\
&&\ddots&\ddots&\ddots\\
&&&0&0&1
\end{bmatrix}
&J_0^\nu&=\begin{bmatrix}
0&0&0&\cdots&0&1\\
&0&0&0&\cdots&0\\
&&\ddots&\ddots&\ddots&\vdots\\
&&&0&0&0
\end{bmatrix}
\end{align}
$$

Si può rappresentare $J^t$ in maniera compatta tramite segnali discreti( $\delta(t)$ )
	Si usa $\delta(t)$ perchè vale 1 solo quando $t=0$
$$
J_\lambda^t=\begin{bmatrix}
\delta(t)&\delta(t-1)&\delta(t-2)&\delta(t-\nu+1)\\
&\delta(t)&\ddots&\delta(t-2)\\
&&\ddots&\delta(t-1)\\
&&&\delta(t)\\
\end{bmatrix}
$$
$\delta(t),\delta(t-1),...,\delta(t-\nu+1)$ sono le *elementary modes* associate al mini-block $J_k$

### Caso $\lambda\neq0$ 
$$
J_\lambda=\begin{bmatrix}
\lambda&1\\
&\lambda&1\\
&&\ddots&\ddots\\
&&&\lambda&1
\end{bmatrix}=\lambda I_\nu+J_0\quad\text{(non importa il verso della moltiplicazione in questo caso)}
$$
 **Newton's binomial formula**
 $\displaystyle(a+b)^t=\sum_{i=0}^t\binom{t}{i}a^{t-i}b^i$  dove $\displaystyle\binom{t}{i}=\frac{n!}{k!(n-k)!}$ 

Possiamo usare questa formula in questo caso per calcolare $J_\lambda^t$ perche se considero
$$
\begin{align}
&(\lambda I_\nu)J_0=J_0(\lambda I_\nu)\\
\Rightarrow J_\lambda^t&=(\lambda I+J_0)^t=\sum_{i=0}^t\binom{t}{i}(\lambda I)^{t-i}J_o^i\\
&=\lambda^tI+\binom{t}{1}\lambda^{t-1}J_0+\binom{t}{2}\lambda^{t-2}J_0^2\dots+\binom{t}{\nu}\lambda^{t-\nu+1}J_0^\nu\\\\\\
&J_\lambda^t=
\begin{bmatrix}
\lambda^t&\binom{t}{1}\lambda^{t-1}&\binom{t}{2}\lambda^{t-2}&\binom{t}{\nu-1}\lambda^{t-\nu+1}\\
&\lambda^t&\ddots&\binom{t}{2}\lambda^{t-2}\\
&&\ddots&\binom{t}{1}\lambda^{t-1}\\
&&&\lambda^t\\
\end{bmatrix}
\end{align}
$$
$\lambda^t,\binom{t}{1}\lambda^{t-1},\binom{t}{2}\lambda^{t-2},\binom{t}{\nu-1}\lambda^{t-\nu+1}$ sono le *elementary modes* associate a $\lambda$.
Sono presenti $\nu$ *dinstinct elementary modes* associate a $\lambda$ 


Guardando al generico $J$ block è chiaro che il numero di *elementary modes* distinte associate coicide con la dimensione del mini-block più grande associato a $\lambda_i$ dato che e quindi sono:
$n_{i1}$ che corrisponde anche alla molteplicità di $\lambda_i$ in $\Psi_J(s)$.

Il numero di elementary modes distinte associate a tutti gli autovalori di $J$ è: $n_{11}+n_{21}+...+n_{r1}=deg(\Psi_J)$ 

#### Esempio 1
$$
J=
\begin{bmatrix}
{\color{orange}\begin{bmatrix}
2&1\\
&2
\end{bmatrix}}\\
&2\\
&&2\\
&&&{\color{lightgreen}\begin{bmatrix}
1&1\\
&1&1\\
&&1
\end{bmatrix}}\\
&&&&\color{lightblue}0
\end{bmatrix}
$$
le elementary modes saranno:
- ${\color{orange} 2^t},{\color{orange}\binom{t}{1}2^{t-1}}$ 
- ${\color{lightgreen}1^t},{\color{lightgreen}\binom{t}{1}1^{t-1}},\color{lightgreen}\binom{t}{2}1^{t-2}$
- $\color{lightblue}\delta(t)$ 
### Preposition
Per ogni $f\in \mathbb{C^{n\times n}}$ in particolare $F\in \mathbb{R}^{n\times n}$ esiste $T\in \mathbb{R}^{n\times n}$  *non singular* tale che $T^{-1}F\ T=J$ e $F= T\ J\ T^{-1}$.

$F^t=(T\ J\ \cancel{T^{-1}})(\cancel{T}\ J\ \cancel{T^{-1}})...(\cancel{T}\ J\ T^{-1}) = T\ J^t\ T^{-1}$ 
Questo implica che le entries di $F^t$ sono combinazioni lineari delle elementary modes di $J$.
Questo implica che tutte le elementary modes associate a $J$ compaiono in $F^t$ e nessun altra quindo possiamo anche chiamarle elementary modes di $F^t$
NOTA: $\Psi_J(s)=\Psi_F(s)$ perchè sono matrici simili