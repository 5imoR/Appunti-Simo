#ST-L30-1
### Problem
Supponiamo di conoscere la descrizione del sistema $\Sigma=(F,G,H)$ e di avere accesso agli input e agli output ma non agli stati. Ha senso ideare inizialmente uno state observer $\hat \Sigma$  che prodice una "buona" stima degli stati $\hat x(\cdot)$  e successivamente fare [[State Feedback stabilization]] usando $\hat x(\cdot)$ invece che $x(0)$?
![[Drawing 2025-12-23 11.39.07.excalidraw]]
$$
\begin{align}
&\begin{array}{c}
\text{system}\\
\Sigma
\end{array}\ 
\begin{cases}
\dot x(t)=Fx(t)+Gu(t)\\
y(t) =Hx(t)
\end{cases}\\
\\\\
&\begin{array}{c}
\text{observer}\\
\hat\Sigma
\end{array}\ 
\dot{\hat  x}(t)=F\hat x(t)+Gu(t)+L[H\hat x(t)-y(t)]\\
\\\\
&\begin{array}{c}
\text{feedback}\\
\end{array}\ u(t)=v(t)+K\hat x(t)
\end{align}
$$
State Vector di $\Sigma_{tot}$ è $\begin{bmatrix}  x(t) \\ \hat  x(t) \end{bmatrix}$ ($dim\ \Sigma_{tot}=2m$)
Vogliamo dedurre lo state model che rappresenta $\Sigma_{tot}$
$$
\Sigma_{tot}=\begin{cases}
\begin{bmatrix} \dot x(t) \\ \hat  x(t) \end{bmatrix}=
\underbrace{\begin{bmatrix}
F&GK \\
-LH & F+LH 
\end{bmatrix}}_{F_{tot}}
\begin{bmatrix}  x(t) \\ \hat  x(t) \end{bmatrix}
+
\underbrace{\begin{bmatrix} G \\ G \end{bmatrix}}_{G_{tot}}v(t)\\
y(t)=\underbrace{\begin{bmatrix} H & 0 \end{bmatrix}}_{H_{tot}}\begin{bmatrix}  x(t) \\ \hat  x(t) \end{bmatrix}
\end{cases}
$$
Vogliamo introdurre un cambio di base nello state space $\mathbb R^{2m}$ questo ci permette di rendere più comprensibile la struttura delle proprietà del sistema complessivo.
Introduciamo l'estimation error:
$$e(t)\triangleq x(t)-\hat x(t)$$
e vogliamo trovare la nuova base rispetto la quale lo state vector è:$\begin{bmatrix}  x(t) \\ e(t) \end{bmatrix}$
$$
\underbrace{\begin{bmatrix}  x(t) \\ e(t) \end{bmatrix}}_\text{New State Vector}=
\underbrace{\begin{bmatrix}
I_n & 0 \\
I_n & -I_n \\
\end{bmatrix}}_{T^{-1}}
\underbrace{\begin{bmatrix}  x(t) \\ \hat  x(t) \end{bmatrix}}_{\text{Old State Vector}}\qquad \Rightarrow T=T^{-1}
$$

Vogliamo determinare le matrici $\bar F_{tot}, \bar G_{tot}, \bar H_{tot}$ che rappresentano il sistema rispetto la nuova base:
$$
\begin{align}
\bar F_{tot}&=T^{-1}F_{tot}T\\
&=
\begin{bmatrix}
I_n & 0 \\
I_n & -I_n \\
\end{bmatrix}
\begin{bmatrix}
F&GK \\
-LH & F+LH 
\end{bmatrix}
\begin{bmatrix}
I_n & 0 \\
I_n & -I_n \\
\end{bmatrix}\\\\
&=
\begin{bmatrix}
I_n & 0 \\
I_n & -I_n \\
\end{bmatrix}
\begin{bmatrix}
F+GK   & -GK \\
F+GK & -(F+LH+GK) 
\end{bmatrix}\\\\
&=
\begin{bmatrix}
F+GK   & -GK \\
0 & F+LH 
\end{bmatrix}\\\\\\
\bar G_{tot}&=T^{-1}G_{tot}T\\
&=
\begin{bmatrix}
I_n & 0 \\
I_n & -I_n \\
\end{bmatrix}
\begin{bmatrix}
G \\
G \\
\end{bmatrix}\\\\
&=
\begin{bmatrix}
G \\
0 \\
\end{bmatrix}\\\\\
\bar H_{tot}&=T^{-1}H_{tot}T\\
&=
\begin{bmatrix}
H &
0 \\
\end{bmatrix}
\end{align}
$$
Forse ho scritto delle T in più in H e G

## Separation Principle
E facile vedere che:
$$
\sigma(F_{tot})=\sigma (\bar F_{tot})=\sigma(F+GK)\cup\sigma(F+LH)
$$
dove:
- $\sigma(F+GK)$: state feedback senza observer
- $\sigma(F+LH)$: observer senza state feedback

Di conseguenza
$$
\begin{align}
\begin{array}{c}
\exists \text{observer based controller}\\
\text{that makes $\Sigma_{tot}$ async. stable}
\end{array}
&\iff
\begin{cases}
\exists K \ s.t.\ F+GK \text{ is asinc. stable}\\
\exists L \ s.t.\ F+LH \text{ is async. stable}\\
\end{cases}\\
\Updownarrow  \qquad\qquad&\qquad\qquad\qquad  \Updownarrow\\
\begin{cases}
(F,G) \text{ is stabilizable}\\
(F,H) \text{ is detectable}
\end{cases}
&\iff
\begin{cases}
\exists\text{ stabilizing state feedback}\\
\exists \text{ asymptotic state observer}
\end{cases}\\
\end{align}
$$

Per DT ssm
$$
\begin{align}
\begin{array}{c}
\exists\text{ observer based controller}\\
\text{that makes $\Sigma_{tot}$ finite memory}
\end{array}
&\iff
\begin{cases}
\exists K\ s.t.\ F+GK \text{ is nilpotent ($\exists$DBC)}\\
\exists L\ s.t.\ F+LH \text{ is nilpotent ($\exists$DBO)}
\end{cases}\\
  \qquad\qquad&\qquad\qquad\qquad  \Updownarrow\\
&\iff
\begin{cases}
(F,G) \text{is controllable}\\
(F,H) \text{is reconstructable}
\end{cases}\\
\end{align}
$$
Qual'è la transfer matrix di $\Sigma_{tot}$? 
$$
\begin{align}
W_{tot}(s)&\equiv \bar H_{tot}(sI-\bar F_{tot})\bar G_{tot}\\
&=\begin{bmatrix}
H &
0 \\
\end{bmatrix}
\begin{bmatrix}
sI-(F+GK)   & GK \\
0 & sI-(F+LH) 
\end{bmatrix}^{-1}
\begin{bmatrix}
G \\
0 \\
\end{bmatrix}\\
&=
H(sI-F-GK)^{-1} G
\end{align}
$$
Questa è la stessa matrice che si sarebbe ottenuta se non ci fosse stato l'observer e lo state feedback fosse stato fatto direttamente sullo stato reale $x(t)$
### Ex
Dato un CT sys.
$$
\begin{cases}
\dot x(t)=Fx(t)+gu(t)=&\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
3 & 2 & 1 \\
\end{bmatrix}x(t)
+\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}u(t)\\
y(t)=Hx(t)=&\begin{bmatrix} 0 & 1 & 0 \end{bmatrix}x(t)
\end{cases}
$$
Design if possible an observer based controller that majes the resulting sys. $\Sigma_{tot}$ asymptotically stable
#### Remark
$$\sigma(F_{tot})=\sigma (\bar F_{tot})=\sigma(F+GK)\cup\sigma(F+LH)$$
####
Osserviamo che  $(F,g)$ è in CCF$\Rightarrow$ $(F,g)$ reachable $\Rightarrow(F,g)$ stabilizable
consideriamo ora il paio $(F,H)$:
$$
\mathcal O=\begin{bmatrix} H \\ HF \\ HF^2 \end{bmatrix}=
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
3 & 2 & 1 \\
\end{bmatrix}\quad rank\ \mathcal O=3
$$
$\Rightarrow(F,G)$ è observable
$\Rightarrow(F,H)$ è detectable

$\Rightarrow$ il problema è risolvibile
Se vogliamo  $\Delta_{F+gK}(s)=(s+1)^3$ ed assumiamo $K=\begin{bmatrix}k_o &k_1 & k_2\end{bmatrix}$  dobbiamo solo imporre che :
$$
F+gK=
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
3+k_0 & 2+k_1 & 1+k_2 \\
\end{bmatrix}=
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
-1 & -3 & -3 \\
\end{bmatrix}\qquad K=\begin{bmatrix}
-4 & -5 & -4
\end{bmatrix}
$$
Se vogliamo  $\Delta_{F+LH}(s)=(s+1)^3$ ed assumiamo $L=\begin{bmatrix}l_0 \\l_1 \\ l_2\end{bmatrix}$  dobbiamo solo imporre che :
$$
F+LH=\begin{bmatrix}
0 & 1+a & 0 \\
0 & b & 1 \\
3 & 2+c & 1 \\
\end{bmatrix}\quad \Delta_{F+LH}(s)=\det
\begin{bmatrix}
s-0 & -1-a & -0 \\
-0 & s-b & -1 \\
-3 & -2-c & s-1 \\
\end{bmatrix}
$$
$$
s^3+(-b+1)s^2+(b-2+c)s-(3+3a)=(s+1)^3 \quad L=\begin{bmatrix}-\frac 43 \\-4 \\ -9\end{bmatrix}
$$
