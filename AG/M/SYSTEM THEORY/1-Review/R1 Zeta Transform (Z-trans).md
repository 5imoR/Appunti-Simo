**E il suo uso per studiare discrete time state space models**
[[SYSTEM THEORY]] #ST-L3
Sia $v(t),\ t\in\mathbb{Z}_t$ una ( possibilmente un valore vettoriale o matriciale) sequenza a tempo discreto. 
Definiamo la sua *Zeta Transform*(se esiste) la funzione a valori complessi (vettoriali o matriciali) di $z\in \mathbb{C}$ definita come:
$$
\begin{align}
V(z)=\mathcal{Z}[v(t)]\triangleq\sum_{t=0}^{+\infty}v(t)z^{-t}&=v(0)\quad\ \ + v(1)z^{-1}\quad\ \ \ \ +v(2)z^{-2}\quad\ \ \ +...\\\\
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
#ST-L4 
soddisfano:
$$
\begin{align}
&X(z)=\underbrace{(zIn-F)^{-1}z\ x_0}_{x_l}+\underbrace{(zIn-F)^{-1}GU(z)}_{x_f}\\
&Y(z)=\underbrace{H(zIn-F)^{-1}z\ x_0}_{y_l}+\underbrace{[(zIn-F)^{-1}G+D]U(z)}_{y_f}\\
\end{align}
$$
Siccome il sistema è lineare ad abbiamo visto che:
$$
\begin{align}
&x(t)=x_l(t)+x_f(t)\\
&y(t)=y_l(t)+y_f(t)
\end{align}
$$

Per composizione possiamo definire che:
$$
\begin{align}
&(zIn-F)^{-1}z\ x_0 &=X_l(z)=\mathcal{Z}[x_l(t)]\\
&(zIn-F)^{-1}GU(z) &=X_f(z)=\mathcal{Z}[x_f(t)]\\
&H(zIn-F)^{-1}z\ x_0 &=Y_l(z)=\mathcal{Z}[y_l(t)]\\
&[(zIn-F)^{-1}G+D]U(z) &=Y_f(z)=\mathcal{Z}[y_f(t)]\\
\end{align}
$$
Definiamo la matrice di trasferimento dello s.s.m. $\Sigma=(F,G,H,D)$ :
$$
W(z)\triangleq H(zIn-F)^{-1}G+D
$$

Sappiamo che questa matrice è invertibile quindi:$$(zI_1-F)^{-1}=\frac{1}{\det(zI_1-F)}\cdot adj(zI_1-F)=\frac{1}{\Delta_F(z)}{\color {orange}adj}(zIn-F)$$
	- $\Delta_F(z)$ è un polinomio monico di grado $n$ (polinomio caratteristico)
	- $adj(zI_1-F)$ è una matrice $n\times n$  polinomiale nella quale le entry hanno il grado $\leq n-1$ 
	$adj(M)=(-1)^{i+j}det(M\text{ colonna i e riga j})$ 
$\color{orange}\text{quindi }v_i\in \{1,...,m\}v_j\in \{1,...,p\}$

quindi:
$$
[W(z)]_{ij}=W_{ij}(z)=\frac{e^T_iH\ adj(zIn-F)Ge_j}{\Delta_F(z)}+d_{ij}
$$
che è la somma di una *strictly proper* function in $\mathbb R(z)$  ed una costante $d_{ij}$.
Di conseguenza:
- $W_{ij}(z)$ è una *proper rational function*
- $W$ è una *proper rational matrix* $\in \mathbb R(z)^{p\times n}$ 
- $w(t)$ è l'implulse response $w(t)=D\delta(t)+HF^{t-1}G\delta_{-1}(t-1)$ 

Diciamo che $\lambda\in \mathbb C$ è un polo di $W(z)$ se è un polo per alcune entries quindi:
$$
\begin{align}
\{\text{poli di }W(z)\}&\triangleq\bigcup_{\substack{i \in \{1, \dots, p\} \\ j \in \{1, \dots, m\}}}\ \{\text{poli di } W_{ij}(z)\}\\
&\subseteq\{\text{zeri di }\Delta_F(z)\}\\
&=\sigma(F)&\text{spectrum di F(il set dei suoi autovalori)}
\end{align}
$$

#GEMINI

| **Segnale nel tempo v(t) (per t≥0)**                 | **Trasformata V(z)**                 | **Riferimento nell'Esercizio**                   |
| ---------------------------------------------------- | ------------------------------------ | ------------------------------------------------ |
| **Impulso unitario** $\delta(t)$                     | $1$                                  | Es. 4a                                           |
| **Gradino unitario** $\delta_{-1}(t)$ oppure $1$     | $\displaystyle\frac{z}{z-1}$         | Es. 4a                                           |
| **Esponenziale** $a^t$                               | $\displaystyle\frac{z}{z-a}$         | Es. 4a (con $a=1/2$)  <br><br>Es. 4b (con $a=3$) |
| **Rampa** $t$                                        | $\displaystyle\frac{z}{(z-1)^2}$     | Es. 4b                                           |
| **Binomiale** $\displaystyle\binom{t}{k}$ (parabola) | $\displaystyle\frac{z}{(z-1)^{k+1}}$ | Es. 4c                                           |
### Proprietà fondamentali usate

Oltre alle tabelle, gli esercizi sfruttano queste proprietà chiave:

- **Linearità:** $Z[a \cdot v(t) + b \cdot w(t)] = a V(z) + b W(z)$ 
    
- **Ritardo temporale:** $Z[v(t-k)] = z^{-k} V(z)$
    
- **Moltiplicazione per $a^t$:** Cambia la scala in $z$.
    
- **Derivata rispetto a $z$:** Usata per ricavare la trasformata di $t \cdot a^t$ (citata implicitamente nella soluzione 4i dove compare l'operatore derivata $\frac{d}{dz}$ 