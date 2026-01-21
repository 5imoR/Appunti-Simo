### Theorem Bases=Vertex
Un punto $x\in\mathbb R^n$ è il vertice di un non empty polyhedron:
$$P=\{x|Ax=b,x\geq0\} \iff x \text{ è una b.f.s. del sistema } Ax=b$$
#CO-L6
#### Corollario
Se il feasible set $P$ di un linear program è bounded e non empty allora esiste almeno una b.f.s.
### Proof
- $x$ è una b.f.s. associata ad una base $B$
	è un set di variabili(non vettori)
- possiamo fare permutazioni sulle colonne di $B$ senza perdere generalità facendo in modo di avere valori positivi nelle prime k posizioni 
$$
x=[x_1\dots x_k,0\dots 0]^T
$$
- $x_i$... sono i valori della colonna non vettori
- dato che $k<m$  una variabile della base può essere 0. Quando questo succede si dice che la base è *degenerate* 
	ATTENZIONE è una variabile ( $x_B$ ) non la colonna
- Siano $A_1\dots A_K$  le colonne associate ad $x_1\dots x_k$  che fanno parte della base, sono linearmente indipendenti.
	$A_1x_1+A_2x_2+\dots+A_kx_k=b$ 


$\Leftarrow$ ) Ora per contraddizione diciamo che $x$ non è un vertice
ovvero $\exists y,z \in P$ e $\lambda\in(0,1)$  tale che
$$
x=\lambda y+(1-\lambda)z
$$
Siccome tutte le variabili di $y,z$ devono essere non negative e la loro convex combination deve essere $x$ abbiamo che gli ultimi $n-k$ componenti di $y,z$ sono a 0
$$
y=[y_1\dots y_k,0\dots 0]^T
\qquad
z=[z_1\dots z_k,0\dots 0]^T
$$
Ed esendo soluzioni del sistema lineare:
$$
\begin{align}
&A_1y_1+A_2y_2+\ldots+A_ky_k=b\\
&A_1z_1+A_2z_2+\ldots+A_kz_k=b\\
\\
&A_1(y_1-z_1)+\ldots+A_k(y_k-z_k)=b\\
&A_1\alpha_1+\ldots+A_k\alpha_k=b\\

\end{align}
$$
Quindi abbiamo trovato un vettore $\alpha\neq0$ che prova che $A_1,\ldots,A_k$ sono linearmente dipendenti che è una contraddizione di quello che stavamo cercando  

$\Rightarrow$ ) Supponiamo che $x$ sia un vertice e come prima con delle permutazioni lo otteniamo nella seguente formula:
$$
x=[x_1\dots x_k,0\dots 0]^T
$$
La differenza da prima è che ora non possiamo assumere che $k\leq m$  al momento.
Siccome un vertice è una feasible solution del sistema abbiamo:
$$A_1x_1+A_2x_2+\dots+A_kx_k=b$$
Ora abbiamo due casi:
- Le colonne $A_1,\ldots,A_k$ sono linearmente indipendenti ( $k=0$ ).
	In questo caso abbiamo che $k\leq m$ e scegliendo altre $m-k$  colonne linearmente indipendenti (sepre possibile perchè $A$ ha rango $m$) possiamo formare una base
	$B=[A_1,\ldots,A_k,A_{k+1},\ldots,A_m]$ 
	e la b.f.s. è esattamente $x$  
- Le colonne $A_1,\ldots,A_k$ sono linearmente dipendenti
	Quindi esiste $\alpha\neq 0$ tale che: $A_1\alpha_1+\ldots+A_k\alpha_k=b$
	 Ora andiamo a sommare e sottrarre questa equazione moltiplicata per $\varepsilon$ ottenendo:
	 $$
	\begin{align} A_1(x_1+\varepsilon\alpha_1)+A_2(x_2+\varepsilon\alpha_2)+\dots+A_k(x_k+\varepsilon\alpha_k)=b\\
	A_1(x_1-\varepsilon\alpha_1)+A_2(x_2-\varepsilon\alpha_2)+\dots+A_k(x_k-\varepsilon\alpha_k)=b\\
	\end{align}
	 $$
	$\varepsilon$ serve ad assicurarci che $x_i\pm\alpha_i>0$  e quindi ridimensioniamo $\alpha_i$
	procedendo si ottene che
	- $x+\varepsilon\alpha=y$	 
	- $x-\varepsilon\alpha=z$	 
	Questo comporterebbe che $x=\frac1 2 y+\frac 1 2 z$ che è impossibile dato che $x$ è un vertice. Questo secondo caso non può succedere e questo conclude la prova
