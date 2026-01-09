### KL divergence (kulback lieber)
Date due funzioni di densità di probabilità $p(x)$ e $q(x)$  s.t. $q(x)>0\quad\forall x$  s.t. $p(x)>0$  definiamo:
$$
KL(p||q):=\int \log\left(\frac{p(x)}{q(x)}\right)p(x)\ dx= E_p \log\left(\frac{p(x)}{q(x)}\right)
$$
E' un metodo per misurare quanto differiscono $p$ e $q$ 
### Theorem 
$$
KL(p||q)\ge 0\qquad KL(p||q)=0\iff p(x)=q(x)\quad a.e.\ w.r.t.\  p(x)
$$
### Proof
$$\begin{aligned} KL(p||q) &= \int \log\left(\frac{p(x)}{q(x)}\right) p(x) dx \\ &= -\int \log\left(\frac{q(x)}{p(x)}\right) p(x) dx \\ &\ge \int\left(1 - \frac{q(x)}{p(x)}\right) p(x) dx \\ &= \int (p(x) - q(x)) dx = 0 \end{aligned}  $$

In aggiunta se  $p(x)=q(x),\ \forall x s.t.\ p(x)>0$ si ha:
$$KL(p||q) = \int \log\left(\frac{p(x)}{q(x)}\right) p(x) dx = \int \log(1) p(x) dx = 0$$