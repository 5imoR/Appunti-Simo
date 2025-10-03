**E il suo uso per studiare discrete time state space models**
[[SYSTEM THEORY]] #ST-L3
Sia $v(t),\ t\in\mathbb{Z}_t$ una ( possibilmente un valore vettoriale o matriciale) sequenza a tempo discreto. 
Definiamo la sua *Zeta Transform*(se esiste) la funzione a valori complessi (vettoriali o matriciali) di $z\in \mathbb{C}$ definita come:
$$
\begin{align}
V(z)=\mathcal{Z}[v(t)]\triangleq\sum_{t=0}^{+\infty}v(t)z^-t&=v(0)\quad\ \ + v(1)z^{-1}\quad\ \ \ \ +v(2)z^{-2}\quad\ \ \ +...\\\\
\{v(t)\}_{t\in\mathbb{C+}}&=v(0)\delta(t)+v(1)\delta(t-1)+v(2)\delta(t-2)+...
\end{align}
$$
## Proprietà 
### Linearity 
Se $V_i(z)\ i=1,2\ \ e\ \ \alpha_1,\alpha_2 \in \mathbb{C}$

allora $Z[\alpha_1v_1(t)+\alpha_2v_2(t)]=\alpha_1V_1(z)+\alpha_2V_2(z)$ 
### One Step Advance
| Se $V(2)=\mathcal{Z}[v(t)]$<br><br>allora $Z[v(t+1)]=zV(z)-zV(0)$ | ![[onestepadvance]] |
| ----------------------------------------------------------------- | ------------------- |
##
Supponiamo di avere un *d.t.s.s.m.*(discrete time state space model) 
$$
\begin{align}
&x(t+1)=Fx(t)+Gu(t) \\
&y(t)\quad\ \ \ =Hx(t)+Du(t)   
\end{align}
$$
e sapendo che:
- $x(0)=X_0\in\mathbb{X}=\mathbb{R}^{n\times n}$ 
- Input: $u(t)$ e che $U(z)=\mathcal{Z}[u(t)]$ 
vogliamo determinare:
$$
\begin{align}
X(z)\triangleq \mathcal{Z}[x(t)]\\
Y(z)\triangleq \mathcal{Z}[y(t)]
\end{align}
$$
$\color{orange}\text{Lo rivediamo la volta dopo manca la parte finale ma non l'ho capita}$

applicando$\mathcal{Z}[\ \cdot\ ]$  ad entrambi i lati delle equazioni si ottiene:
$$
\begin{align}
zX(z)-z\ x_o=FX(z)+GU(z)\longrightarrow (zI-F)X(z)=z\ x_0+GU(z)\\

\end{align}
$$