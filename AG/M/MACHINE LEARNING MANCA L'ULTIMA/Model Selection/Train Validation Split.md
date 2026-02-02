#ML-L13-2 
L'idea è:
Si divide il dataset in 2, una parte per il training, l'altra per  la validation
$$\begin{align}
 &S=\set{x_i,y_i) i\in [1,ms]}\quad &L_S(h) =\frac 1{|S|}\sum_{z\in S} l(h(x,y))\\
 &V=\set{x_i,y_i)\ i\in [ms+1, m]}\qquad & L_V(h)=\frac 1{|V|}\sum_{z\in V} l(h(x,y))
\end{align}$$
![[trainvalidationsplit]]
andando ad aggiungere il validation set si nota che $\hat h_1$ è il migliore

