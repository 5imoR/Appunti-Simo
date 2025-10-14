#ST-L7
### Definition
Un non linear continuous time time-invariant s.s.m. è descritto come segue:

$$
\begin {align}
&t\in \mathbb R+\\
&\begin{cases}
\dot x(t)=f(x(t),u(t))&f:\mathbb R^n\times \mathbb R^m\rightarrow\mathbb R^n\\
y(t)=h(x(t),u(t))&h:\mathbb R^n\times \mathbb R^m\rightarrow\mathbb R^p\\
\end{cases}
\end{align}
$$
$dim\ x=n\quad dim\ u=m\quad dim\ y=p\quad$ 
### Equilibrium Point
Uno stato $x_e\in\mathbb R^n$ è detto in un punto d'equilibrio del sistema in corrispondenta ad un $u(t)=\overline{u}$ costante.

$$
\begin{align}
&se:&&allora:\\
&x(0)=x_e &\qquad\qquad &x(t)=x_e\ \forall t\in \mathbb R+\\ 
&u(t)=\overline{u}\quad \forall t\in \mathbb R+
\end{align}
$$
E' immediato vedere che $x_e$ è il punto di equilibrio corrispondente a $u(t)=\overline{u}\Leftrightarrow x_e=f(x_e, \overline u)$ 
Se $x_e$ è un punto di equilibrio anche $y_e$ sarà constante per qualunque valore di $t>0$  

### Autonomous system
Se il n.l c.t. s.s.m. non è affetto da alcun input allora è detto sistema autonomo ed ha la seguente forma:

$$
\begin {align}
&t\in \mathbb R+\\
&\begin{cases}
\dot x(t)=f(x(t))\quad (A)\ autonomous\\
y(t)=h(x(t))\\
\end{cases}
\end{align}
$$
$dim\ x=n\quad dim\ y=p\quad$ 

### Definition of equilibrium point
Diciamo che $x_e$ è un punto di equilibrio di un s.s.m autonomo se:
$$\begin {align}
&x(0)=x_e\Rightarrow x(t)=x_e\quad \forall t\in \mathbb R+\\
&x_e \text{è un punto di equilibrio} \Leftrightarrow x_e=f(x_e)
\end{align}
$$
Se $x_e$ è un punto di equilibrio anche $y_e$ sarà constante per qualunque valore di $t$ 

![[Equilibrium points type#Definition of equilibrium point types]]


