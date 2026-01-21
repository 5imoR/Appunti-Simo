#CO-L12 

## Ex1
Dato
$I$ ground set
$F$ famiglia di sotto insiemi di $I$
Si vuole eguagliare $I$ con il minor numero di sottoinsiemi, come si modella il sistema?
1. si definisce il set
2. si definiscono i dati in input/i parametri
3. si definiscono le variabili
4. si definisce l'object function
5. si mettono i constraint

Si aggiunge la variabile $x_j=\begin {cases}1\quad \text {if Fj è usato }\\0\quad \text{altrimenti}\end{cases}$ 

Si sceglie l'obj.fun. $\min\sum_{j=1}^nx_j$ 

$$
\begin{cases}
\min\sum_{j=1}^nx_j\\
\sum_{j=i\in F_j}x_j\ge 1\qquad \forall i\in I\\
x_j\in \set{0,1}\qquad \forall j\in\set 1\dots n
\end{cases}
$$
E spiega quali sono i vincoli e compagnia
## Ex2
Prendi l'esempio di un atlante, bisogna colorare ogni stato e 2 stati adiacenti non possono avere lo stesso colore, quanti colori servono

$G(V,E)$
$k$ numero di colori
$x_j=\begin {cases}1\quad \text {se e è }\\0\quad \text{altrimenti}\end{cases}$

$$
\begin{cases}
\min\sum_\\
\sum_{j=i\in F_j}x_j\ge 1\qquad \forall i\in I\\
x_j\in \set{0,1}\qquad \forall j\in\set 1\dots n
\end{cases}
$$