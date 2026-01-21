### Branch and Bound

Consiste in un tree-search dove:
- si parte dal problema iniziale
- si effettua una relaxation
- si trova una soluzione ottima
- se non è un int si esegue una restriction
da capo
![[beb|1200]]
Detto un po meglio:
- Risolvi $R$ e trovi il lowerbound
- trovi $x^*$ che non è un int quindi si rimuove tutto quello che è compreso tra$\Big[\ \lfloor x_j^*\rfloor, \lceil x_j^*\rceil\ \Big]$ 
	$\exists j\in J:\ x_j^*\in \mathbb Z$ 
- Quello che si va a formare è un albero di restriction ma quello che andiamo a considerare sono relaxation

Sia: 
- $F(P)$  un set di feasible solution di $P$
- $c: F(P)\to \mathbb R$ la objective function da minimizzare
- $\bar x\in F(P)$ una feasible solution conosciuta ottenuta da un'euristica

- $z=c(\bar x)$ è detto *incumbent* e da un upper bound alla soluzione ottima di $P$

L'algoritmo segue:
- Creiamo una relaxation $R$ del problema corrente. Risolviamo $R$
	tutto si conclude se:
	- $R$ è infeasible
	- la soluzione ottima è feasible per $P$ 
	- il valore è più grande o pari a $z$ 
![[uperlower beb]]
	I numeri non so se sono giusti
La parte più lunga è provare la soluzione ottimale non trovarla
- L'upper bound è l'incombent
- Il lower bound è il valore minimo presente sulla frontiera

Questo algoritmo da sempre un upper e lower bound anche se interrotto a metà