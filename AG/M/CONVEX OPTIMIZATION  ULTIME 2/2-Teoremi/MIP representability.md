#CO-L10
### MIP representability
Un set $S\subseteq \mathbb R^n$  è MIP-rapresentable se esiste un set di constraint nella forma:
$$
P=
\begin{cases}
Ax+Bu+Dy\le b\\
x\in \mathbb R^n, u\in \mathbb R^m, y_k\in \set{0,1}\forall k
\end{cases}
$$
tale che la sua projection del suo feasible set su $x$ è $S$     $S=projection(P)$ 
![[MIP]]
$\textcolor{red}{■}$ non è MIP rappresentable
$\textcolor{cyan}{■}$ con l'aggiunta di $y$ è MIP rappresentable
### By Jeroslow
Un set $S\in \mathbb R^n$ è MIP-rapresentable se e solo se è l'unione di un numer finito di polyhedra con lo stesso recession cone