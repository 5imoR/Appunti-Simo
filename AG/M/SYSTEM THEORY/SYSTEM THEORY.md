


# Ripasso

![[Cloesed Loop#Closed System]]

---
#ST-L1
##### Esempio (Mass Spring Dumper Model)

| ![[carE]] | Una buona rappresentazione di una macchina.<br>Serve usare gli State Space Models per modellare e controllare<br> |
| --------- | ----------------------------------------------------------------------------------------------------------------- |

--- 






--- 





--- 
#




# Inizio
#ST-L5 
Sono presenti sistemi a tempo discreto e a tempo continuo che a loro volta possono essere lineari o meno. A noi dei sistemi non lineari ci interessa come renderli lineari.
[[Non linear discrete time s.s.m.]]
[[Non linear continuous time s.s.m.]]


#ST-L6
## Riassunto
- $x_e=\underline 0$ è sempre un punto di equilibrio
- $\exists x_e\neq\underline 0 \iff \ker(In-F)\neq\{\underline0\}\iff \lambda=1\in\sigma(F)$ (e $x_e$ è l'autovettore corrispondente)
- $x_e=\underline 0$  è un attractive eq. point $\iff$  tutte le elementary modes associate ad $F$ convergono a $\underline 0\iff\forall\lambda\in\sigma(F)\quad |\lambda|<1$  F è chiamata *Shur Stable*
- se $x_e=\underline0$ è un attractive eq. point  allora è anche stabile equindi è asymptotically stable
- $x_e=\underline0$a  è stabile$\iff$ tutte le elementary modes associate ad $F$ sono bounded $\quad\qquad\qquad\qquad\iff\forall\lambda\in\sigma(F)$  se $|\lambda|<1$ o $|\lambda|=1$  e tutti i $J$ mini-block associati sono scalari.
	 Vuol dire che la molteplicità di $\lambda$ come uno zero di $\Psi_F(z)$ è $1$ 
- Un l.d.t.s.s.m. è asintoticamente stabile$\iff x_e=\underline0$ è un punto d'equilibrio asintoticamente stabile 

