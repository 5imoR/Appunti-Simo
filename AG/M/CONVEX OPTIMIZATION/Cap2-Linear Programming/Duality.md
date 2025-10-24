#CO-L8
Un problema di ottimizzazione $P$ è considerato un problema di ricerca, ovvero trovare la suluzione ottima $x^*$ 
Alternativamente lo stesso problema può essere interpretato come un inference problem ovvero trovare il miglior lowerbound possibile dell'oggetto
In [[Linear Programming]] ci permette di trovare una prova che dimostra che il nostro punto di minimo sia corretto. E' quindi utile sia dal lato teorico che pratico

Considerando un LP in standard form:
![[Linear Programming#Standard form#Problem]]
- Denotiamo con $P$ la feasible region definita dai vincoli $Ax=b, x\geq 0$ 
## Definition 
Dato un set $C\subset \mathbb R^n$ diciamo che una *linear inequality* $\alpha^Tx\geq \beta$ è valida per $C$ se è soddisfata per ogni punto in $C$.
$$\alpha^Tx\geq \beta\quad \forall x\in C$$

Il *dual point of view* consiste nel trovare il vincolo $Ax=b, x\geq 0$  definendo la feasible region $P$ del problema più stretta possibile. 
![[Drawing 2025-10-24 15.30.43.excalidraw|300]]
Questo equivale a: $c^Tx\geq c_0 \forall x\in P$ possiamo quindi scriverlo come un problema di massimizzazione nella forma:
$$
\begin{cases}
\max c_0\\
c^Tx\geq c_0 \forall x\in P
\end{cases}
$$
Questo problema ha una singola variabile ed infiniti vincoli, uno per ogni punto di P.
Usando il [[Theorem (Minkowski Weyl)|Minkowski theorem]]  possiamo già semplificarlo notevolmente
$$
\begin{cases}
\max c_0\\
c^Tv^j\geq c_0\quad \forall v_j\ \text{vertex}\in P
\end{cases}
$$
Siamo passato ad avere un numero esponenziale di  vincoli. Abbiamo quindi bisogno di trovare una caratterizzazione differente dei vincoli validi di $P$ 


Si va a modificare il problema facendo modifiche su $Ax=b$ che la facciano rimanere valida, aggiungiamo un vettore di moltiplicatori$\rightarrow u^TAx=u^Tb$ 
Ora possiamo:
- sistituire $=$ con $\geq$ $\rightarrow u^TAx\geq u^Tb$
- ridurre il lato destro
- aumentare i coefficienti di $x$ a piacere dato che $x\geq 0$ 
Per mostrare che $\alpha^Tx\geq \beta$ è valida per $P$ serve trovare un vettore di moltiplicatori $u\in \mathbb R^m$ tale che:
$$\alpha^T\geq u^TA\quad u^Tb\geq \beta$$
![[Theorem (Farka's Lemma)#Theorem (Farka's Lemma)]]

Sia $x^*$ la soluzione ottimale computata dal [[Primal Simplex Algorithm]] associato alla base $B$
Una volta partizionate le variabili in basic e non basic possiamo definire un vettore di moltiplicatori $u=\alpha_BB^{-1}$ che soddisfa 
- $\alpha^T\geq u^TA$  ovvero tutti i reduced cost $d_j$ sono positivi
- $u^Tb\geq \beta$ è ottenuta come: $\beta\leq z^*=\alpha^Tx=\alpha_B^TB^{-1}b=u^Tb$ 
![[Theorem (Farka's Lemma)#Corollary (Farka's Lemma)]] 
Non solo ha una dimensione polinomiale ma ha anche la stessa dimensione del LP originale con la matrice $A$ trasposta e l'objective e right-hand vectors scambiati di ruolo
![[Linear Programming#Standard form#Problem]]