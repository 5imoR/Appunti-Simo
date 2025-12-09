

### Newton global convergence lemma
Assumiamo [[Newton Method#Newton method|newton method]] con [[Unconstrained Optimization#Line search (backtracking)|backtracking line search]] $\exists 0<\eta\le \frac {m^2}L\qquad \gamma>0$ s.t. iniziando con $t=1$ 
- se $||\nabla f(x^k)||\ge\eta\qquad\Rightarrow f(x^{k+1})\le f(x^k)-\gamma$      (diminuisce di $\gamma$)
- se $||\nabla f(x^k)||<\eta\qquad\Rightarrow \frac L{2m^2}||\nabla f(x^{k+1})||\le(\frac L{m^2}||\nabla f(x^k)||)^2$  e $t_k=1$  (dininuisce exp.)

### Proof
$$
\begin{align}
\cancel{\frac{L}{2m^2}}||\nabla f(x^{k+1})||&\le\frac{L}{2m^2}^{\cancel2}\underbrace{||\nabla f(x^k)||^2}_{<\eta^2}\\
||\nabla f(x^{k+1})||&\le\frac{L}{2m^2}\eta^2=\frac{\cancel L}{2\cancel m^2}\cancel{\frac{m^2}L}\eta \\
&\le\frac \eta2\le\eta
\end{align}
$$
###