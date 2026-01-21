---
tags:
---
#CO-L18-3
## Theorem 6.1
Dato il problema:
$$
\begin {cases}
\min f(x)\\
x\ge 1
\end{cases}
$$
dove $f(x)$ è convesso e differenziabile e $C$ è convesso abbiamo che $x^*\in C$ è ottimale se:
$$ 
\nabla f(x^*)^T(y-x)\ge 0 \qquad\forall y\in C
$$

## Proof

#### $\Leftarrow)$ 
Segue dalla convessità
$$
\begin{align}
f(y)&\ge f(x^*)+\underbrace{\nabla f(x^*)^T(y-x)}_{\ge0}\\
&\ge f(x^*)
\end{align}
$$

#### $\Rightarrow)$ 
Per assurdo, sia $y\in C$ tale che 
$$ 
\nabla f(x^*)^T(y-x)< 0
$$
Consideramo la combinazione convessa 
$$z(t)=ty+(1-t)x^*\quad t\in [0,1]\quad z(t)\in C$$
Ora:
$$
\left.\frac{df(z(t))}{dt}\right|_{t=0}=\nabla f(x^*)^T(y-x^*)<0
$$
quindi per una $t>0$ abbastanza piccola si otterrebbe:
$$
f(z(t))<f(x^*)
$$
che è una contraddizione.