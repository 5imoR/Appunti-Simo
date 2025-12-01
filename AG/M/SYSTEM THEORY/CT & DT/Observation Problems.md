#ST-L25-2
In generale non è detto che un DT ssm sia accessibile (in particolare non è detto che sia disponibile per state feedback) quindi il primpo problema che vogliamo investigare è il seguente:
Supponiamo di conoscere la descrizione del sistema $\Sigma=(F,G,H)$  ed abbiamo misurato gli input $u(\cdot)$ e gli output $y(\cdot)$  (corrispondenti all'input) in una finestra di tempo $[0,T]$ 
- **Q1** Possiamo identificare in modo univoco $x(0)$? \[Observation Problem in $[0,T]$  ] 
- **Q2** Possiamo identificare in modo univoco $x(T)$? \[Reconstruction Problem in $[0,T]$  ] 

Se l'Observation problem  in $[0,T]$  è risolvibile allora possiamo determinare $x(0)$ e quindi tramite $x(0),u(t)\quad t\in[0,T]$ possiamo determinare $x(t)$ e quindi il reconstruction problem.
## Observability of DT ssm
Consideriamo
![[Linear discrete time s.s.m.#Strictly Proper]]

### Definition \[undistinguishable]
Dati due stati $x_1,x_2\in X=\mathbb R^n$ e un integer non negativo $k$ diciamo che $x_1$ è *undistinguishable* da $x_2$ in $[0,k]=\set{0.1\dots k}$ ($x_1\mathop{\simeq}\limits_{[0,k]}x_2$)  se per ogni sequenza di input $u(t)\quad t\in[0,k-1]$ andando a prendere i valori in $U=\mathbb R^m$ se chiamiamo $y_i(t)$ gli output del sistema che inizia da $x(0)=x_i$  e corrispondente all'input $u(\cdot)$ per $i=1,2$ allora $y_1(t)=y_2(t)\quad \forall t\in[0,k]$ 
#### Osserva
$$
\begin{align}
y_1(t)=y_{1l}(t)+y_{1f}(t)\\
y_2(t)=y_{2l}(t)+y_{2f}(t)\\
\end{align}
$$
$y_{1f}(t)$ e $y_{2f}(t)$ coincidono sempre dato che sono guidate dallo stesso input.
allora:
$$
\begin{align}
x_1\mathop{\simeq}\limits_{[0,k]}x_2&\iff y_{1l}(t)=y_{2l}(t)\quad &\forall t\in[0,k]\\
&\iff HF^tx_1\equiv HF^tx_2\quad&\forall t\in[0,k]\\
&\iff
\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k \end{bmatrix}x_1=
\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k \end{bmatrix}x_2
\end{align}
$$
$O_{[0,k]}=\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k \end{bmatrix}$ è chiamata  observability matrix in $[0,k]$ 

### Definition \[unobservable]
Uno stato è detto unobservable in $[0,k]$ se è undistinguishable da $\underline 0$ in $[0,k]$
$$
x_1\mathop{\simeq}\limits_{[0,k]}\underline 0
$$

Quindi $x_0$ non  è osservabile in 
$$
\begin{align}
[0,k]\triangleq x_1\mathop{\simeq}\limits_{[0,k]}\underline 0&\iff O_{[0,k]}x_0=O_{[0,k]}\underline0_n= \underline 0_{p(k+1)}\\
&\iff x_0\in\ker O_{[0,k]}
\end{align}
$$
se chiamiamo $X^{no}_{[0,k]}$ il set di stati unobservable in $[0,k]$  allora:
$$
X^{no}_{[0,k]}=\ker O_{[0,k]}=\ker\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k \end{bmatrix}\equiv \bigcap_{i=0}^k\ker(HF^i)
$$
ciò significa che $X^{no}_{[0,k]}$ è un sottospazio vettoriale di $X=\mathbb R^n$

#### Relazione tra $X^{no}_{[0,k]}$ e $X^{no}_{[0,k+1]}$
$$
X^{no}_{[0,k]}=\ker\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k \\\phantom{}\end{bmatrix}\supseteq \ker\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k\\ HF^{k+1} \end{bmatrix}=X^{no}_{[0,k+1]}
$$
$$
\begin{align}
\mathbb R^n=X\supseteq X^{no}_{[0,0]}\supseteq X^{no}_{[0,1]}\supseteq\dots\supseteq X^{no}_{[0,k]}\dots\\
\end{align}
$$
dato che ogni sottospazio vettoriale è incluso in $\mathbb R^n$ e vale la condizione $X^{no}_{[0,k]}\supsetneq X^{no}_{[0,k+1]}$ 
$\Rightarrow \dim X^{no}_{[0,k+1]}\le \dim X^{no}_{[0,k]}-1$ 
questo implica che $\exists \bar k\in\mathbb Z_+$ s.t. $X^{no}_{[0,\bar k]}=X^{no}_{[0,k]}\quad \forall k\ge \bar k$.

Può essere provato che:
-  Se $X^{no}_{[0,k]}=X^{no}_{[0,k+1]}$    allora   $X^{no}_{[0,k+1]}=X^{no}_{[0,k+2]}$ $$\Rightarrow X^{no}_{[0,k]}=X^{no}_{[0,k+i]}\quad\forall i\ge 0$$ 
- $\bar k\triangleq\min\set{k\in \mathbb Z_+:X^{no}_{[0,\bar k-1]}=X^{no}_{[0,k]}}=n$ $$
X\supset X^{no}_{[0,0]}\supset X^{no}_{[0,1]}\supset\dots \supset X^{no}_{[0,\bar k-1]}= X^{no}_{[0,\bar k]}=\dots$$  
Quindi definiamo uno sottospazio unobservable del sistema $\Sigma$ (paio $(F,H)$ ) come il set di stati che sono undistiguishable da $\underline 0$  in ogni $[0,k]$.
$k\in\mathbb Z_+$ e chiamiamo $X^{no}$ allora: 
$$
X^{no}= X^{no}_{[0,\bar k]}\equiv X^{no}_{[0,k-1]}=\ker\begin{bmatrix} H \\ HF \\ \vdots \\ HF^{n-1}\end{bmatrix}= O\in \mathbb R^{np\times n}
$$
$O$= observability matrix of the pair $(F,H)$

### Definition \[observable]
Diciamo che $\Sigma$ (il paio $(F,H)$ ) è observable se $X^{no}\equiv \set{0}$ 
#### First observability criterion

$$
(F,H)\text{ observable }\iff\ker O=\set{\underline 0}\iff rank\ O=n 
$$
Se $(F,H)$ è osservabile allora quello che chiamiamo $\bar k$ diventa l' observability index e coincide con:
$$
\min\set{k:X^{no}_{[0,k-1]=n}}
$$


# Ex
Dato:
$$
\begin{align}
x(t+1)&=Fx(t)=
\begin{bmatrix}
1 & 0 & 1 & 0 \\
0 & 1 & 0 & -1 \\
2 & 0 & 1 & 0 \\
0 & 2 & 0 & 2 \\
\end{bmatrix}x(t)\\
\\
y(t)&=Hx(t)=
\begin{bmatrix}
1 & 2 & 0 & -1 \\
\end{bmatrix}x(t)
\end{align}
$$
determinare $X^{no}_{[0,k]}$ 

$X^{no}_{[0,0]}=\ker H= \ker \begin{bmatrix}1 & 2 & 0 & -1 \\\end{bmatrix}=<\begin{bmatrix}0 \\0 \\1 \\0 \\\end{bmatrix},\begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix},\begin{bmatrix} 2 \\ -1 \\ 0 \\ 0 \end{bmatrix}>$
