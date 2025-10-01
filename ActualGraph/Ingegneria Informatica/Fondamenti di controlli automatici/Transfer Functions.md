[[FCA]]
E' la trasformata di Laplace dell'impulso della risposta di un sistema LTI quando le condizioni iniziali sono pari a 0

Laplace Transform Table

| f(t)        | F(s)                  |
| ----------- | --------------------- |
| $\delta(t)$ | 1                     |
| $X(t)$      | $X(s)$                |
| $X'(t)$     | $SX(s)-X(0)$          |
| $X''(t)$    | $S^2X(s)-SX(0)-X'(0)$ |
Avendo l'input $u$, l'impulse response $g$ e l'output $y$  la convoluzione è: 
- $y(t)=u(t) * g(t)$ 
- $y(t)=\int_0^tu(\tau)g(t-\tau)d\tau$ 
- $Y(s)=u(s)G(s)$
