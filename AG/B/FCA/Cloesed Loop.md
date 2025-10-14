[[FCA]]
### Open System


### Closed System
Un esempio può essere una macchina con un regolatore di velocità.
Se la velocità desiderata è $100km/h$ e la velocità effettiva è $110km/h$ il controller riceverà di dover rallentare di $10\ (100-110)$
![[Closed_System_Car]]
Se creiamo uno schema a blocchi generico sara:
![[Closed_System]]$$
\begin{align}
&r(t)= segnale\ di\ riferimento\\
&e(t)= errore\\
&u(t)= azione\ sul\ sistema\\
&y(t)=risultato\\
&D= controller\\
&G= processo\\
&H=feedback\\
\\
&E=V-H\cdot y\\
&y=E\cdot D\cdot G \Rightarrow E=\frac{y}{D\cdot G}\\
&(DG)(V-Hy)=y\\\\
&DGV= y(1+DGH)\\ or\\ &y=\frac{DG}{1+DGH}
\end{align}
$$