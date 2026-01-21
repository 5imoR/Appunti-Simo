[[UnconstrainedOptimization.pdf]]
#CO-L14-3
### Polyak-Lojasiewicz Inequality

$$\frac 12 ||\nabla f(x)||^2\ge m(f(x)-p^*)\quad \forall x\in S\ \text{some } m>0$$
- Se non appartiene a $\mathbb C^2$ strong convexity può essere definita come: $f(x)-\frac m2||x||^2$ 
- Per funzioni in $\mathbb C^2$, strong convexity implica la PL inequality con la stessa costante $m$
$$\nabla^2 f(x)\succeq m I$$
Assumendo la PL Inequality: *un po di conti e si ottiene la formula*
$$f(x^{k+1})-p^*\le (f(x^k)-p^*)\underbrace{\left(1-\frac mM\right)}_\rho$$

- In un'iterazione si riduce l'errore di $\rho$ più piccolo è mi si riduce
