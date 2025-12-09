---
tags:
---
#CO-L13-3
## Descent Lemma
 [[Lipscitz continuity|Lipschitz continuous]]: ($M$ è una costante che non sappiamo)
$$||\nabla f(x)-\nabla(f(y)||\le M||x-y||\forall x,y\qquad \text{Lipschitz continuous}$$
implica la descend lemma:
$$f(y)\le \overbrace{\underbrace{f(x)+\nabla f(x)^T(y-x)}_{\text{lower bound}}+\frac 1 2M||y-x||^2}^{\text{upper bound}}$$
![[Drawing 2025-11-14 11.46.49.excalidraw]]

## Proof
#CO-L14-1
$$
\begin{align}
f(y)&=f(x)+
\int_0^1\nabla f(x+a(y-x))^T(y-x)da
&\text{fund. T. calculus}
\\
&=f(x){\color{orange}+\nabla f(x)^T}(y-x)+
\int_0^1(\nabla f(x+a(y-x)){\color{orange}-\nabla f(x)})^T\ (y-x)\ da
\quad&\text{$\pm$ costant}
\\
&\le f(x)+\nabla f(x)^T(y-x)+
\int_0^1||\nabla f(x+a(y-x))-\nabla f(x)||\ ||y-x||\ da
\quad&\text{Cauchy-Schwarz}
\\
&\le f(x)+\nabla f(x)^T(y-x)+
\int_0^1{\color{orange}M}||\cancel{x}+a(y-x)\cancel{-x}||\ ||y-x||\ da
&\text{Lipschitz}
\\
&= f(x)+\nabla f(x)^T(y-x)+
\int_0^1aM||y-x||^2\ da
&\text{factor out}
\\
&= f(x)+\nabla f(x)^T(y-x)+\frac 12M||y-x||^2
\end{align}
$$
