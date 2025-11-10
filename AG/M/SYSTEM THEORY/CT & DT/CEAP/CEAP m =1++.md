#ST-L18-2
## Step 2 m>1
Se partiamo con un paio $(F,G)$ reachable con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$ con $m>1$
ed $\exists i\in\set{1,\dots,m}$ s.t. $(F,g_i)$ dove $g_i$ rappresente l'i-esima colonna di $G$ allora $\forall$ polinomio monico $p(s)\in\mathbb R[s]$ di grado $n$  $\exists k_i\in \mathbb R^{1\times n}$ s.t. $\Delta_{F+g_ik_i}(s)\equiv p(s)$ 
	Ovvero possiamo modellare la matrice del feedback per andare ad "attivare" solo la colonna $g_i$ interessata se $(F,g_i)$ è reachable

IDEA: Proviamo che se un paio $(F,G)$ è reachable da $m$ input possiamo sempre renderlo raggiungibile per un singolo input tramite uno state feedback preliminario e sucessivamente applicare a quell' single input un secondo state feedback per ottenere il polinomio caratteristico desiderato.
