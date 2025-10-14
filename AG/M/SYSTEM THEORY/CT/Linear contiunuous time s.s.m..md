[[Non linear continuous time s.s.m.]] #ST-L7 
## Autonomous Case
Supponiamo di avere un c.t. s.s.m. lineare autonomo
$\dot x(t)=Fx(t)\quad t\in \mathbb R+\quad dim(x)=n\quad (A)$
Si puo dire che:
1. $x_e$ è un punto di d'equilibrio di $(A)\iff0=Fx_e$ 
2. $x_e=\underline 0$ è sempre un punto di equilibrio
3. $\exists x_e\neq\underline 0$ che è un punto di equilibrio del sistema
	equivale a dire uno di questi
	$\iff \ker F\supsetneq \{\underline 0\}$
	$\iff F$ è singular
	$\iff o\in \sigma(F)$    
4. $x_e=0$ è un punto d'equilibrio attrattivo $\iff \forall x_0\ x_l(t)=e^{Ft}x_0\rightarrow 0$ per $t\to+\infty$ 
	
	equivalentemente tutte le elementary modes associate ad $e^{Ft}$ (come anche $F$)  convergono a $0$ per $t\to+\infty$.
	$\large\displaystyle{\frac{t^k}{k!} e^{\lambda it}}$  $\forall i\quad R_e(\lambda_i)<0\iff\lambda\in\sigma(F), Re(\lambda)<0$
	A tempo discreto  per essere attrattivo deve essere interno al cerchi a tempo continuo deve la parte reale deve essere minore di $0$ ![[ct vs dt]]
5. $x_e$ è un punto d'equilibrio stabile $\iff$ le elementary modes di $F$ sono bounded
	
	Sia in DT che CT puoi avere autovalori sulla boundary se hanno solo un elementary mode
	$\iff \forall i\ Re(\lambda_i)\leq 0$  e se $Re(\lambda_i)=0$ allora c'è solo un elementary mode associata a $\lambda_i$ in altre parole la i miniblock associati sono tutti scalari
6. Il sistema è (asintoticamente) stabile se $x_e=0$ è(asintoticamente) stabile

# Rechability
