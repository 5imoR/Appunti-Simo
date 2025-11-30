---
tags:
---
#ST-L24-2
## Theorem \[Existence of DBC]
Dato un paio $(F,G)$ con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$   che rappresenta un DT system ciò che segue è equivalente:
- $(F,G)$ ammette [[DBC Dead Beat Controller]] ($\exists k\in\mathbb R^{m\times n}$ s.t. $F+GK$ sia [[Nilpotent matrix|nilpotent]].)
- $(F,G)$ è [[Controllability DT|controllable to zero]] 
- che $(F,G)$ sia [[Reachability DT|reachable]] o meno la matrice $F_{22}$ non è reachable
- se il rango di [[PHB Reachability Test]] $(\lambda In-F|G]<n$ allora $\lambda=0$ 

## Proof
#### $(1)\Rightarrow(2)$
supponiamo  $\exists k\in\mathbb R^{m\times n}$ s.t. $F+GK$ sia [[Nilpotent matrix|nilpotent]].
Questo implica che: $\Delta_{F+GK}(z)=z^n$  quindi per [[Cayley-Hamilton's theorem]]  possiamo dire che:
$$\Delta_{F+GK}(F+GK)={\color{lightgreen}(F+GK)^n=0}$$
Ora vogliamo provare che  $(F,G)$ è zero controllable![[Controllability DT#Definition]]
settiamo $u(t)=K(F+GK)^tx_0\quad t=0\dots n-1$ 
allora:
$$
\begin{align}
x(1)&=Fx(0)+Gu(0)&&=Fx_0+Gx_0 &&=(F+GK)x_0\\
x(2)&=Fx(1)+Gu(1)&&=F(F+GK)x_0+GK(F+GK)x_0 &&=(F+GK)^2x_0\\
\vdots\\
x(n)&&&\dots &&={\color{lightgreen}(F+GK)^n}x_0=\color{lightgreen}0\\
\end{align}
$$

#### $(2)\Rightarrow(3)$
Assumiamo che un paio $(F,G)$ sia  controllabile a zero che significa che $Im F^n\subseteq Im \mathcal R$ 
Se $(F,G)$ è reachable non c'è niente da provare dato che avremmo che $(F,G)$ ha una proprietà più potente di quella dell'assunzione.
Supponiamo che $(F,G)$ non sia reachable, questo non è seguito da perdita di generalità assumendo  che $(F,G)$ sia in [[SRF Standard Reachability Form]] ![[SRF Standard Reachability Form#Riassunto]]
dato che il sistema è controllabile significa che $Im F^n\subseteq Im \mathcal R$ ovvero:
$$
Im
\begin{bmatrix}
F_{11}^n & * \\
0 & F_{22}^n \\
\end{bmatrix}\subseteq
Im\begin{bmatrix}
G_1 & F_{11}G_1 & \dots & F_{11}^{n-1}G_1 \\
0 & 0 &  & 0 \\
\end{bmatrix}
\begin{array}{c}\}\rho\phantom{ssss} \\\}n-\rho\end{array}
\equiv <e_1,e_2,\dots,e_\rho>
$$
Siccome $Im\mathcal R=<e_1,e_2,\dots,e_\rho>$ allora le colonne di $F^n$ devono appartenereanche loro a $<e_1,e_2,\dots,e_\rho>$. In particolare questo deve essere vero per le ultime $n-\rho$ colonne ma questo implica che le ultime $n-\rho$ entries devono essere $\underline 0$. Questo implica che  $_{22}^n=0\Rightarrow F_{22}$ è nilpotent
#### $(3)\Rightarrow(1)$
Segue dall'analisi del [[CEAP Complete Eigenvalue Allocation Problem]]

#### $(3)\iff(4)$
Segue dal [[PHB Reachability Test]]
