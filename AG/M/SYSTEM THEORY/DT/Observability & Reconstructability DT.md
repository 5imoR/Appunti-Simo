# Observation Problems DT
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
$\mathcal O_{[0,k]}=\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k \end{bmatrix}$ è chiamata  observability matrix in $[0,k]$ 

### Definition \[unobservable]
Uno stato è detto unobservable in $[0,k]$ se è undistinguishable da $\underline 0$ in $[0,k]$
$$
x_1\mathop{\simeq}\limits_{[0,k]}\underline 0
$$

Quindi $x_0$ non  è osservabile in 
$$
\begin{align}
[0,k]\triangleq x_1\mathop{\simeq}\limits_{[0,k]}\underline 0&\iff \mathcal O_{[0,k]}x_0=\mathcal O_{[0,k]}\underline0_n= \underline 0_{p(k+1)}\\
&\iff x_0\in\ker \mathcal O_{[0,k]}
\end{align}
$$
se chiamiamo $X^{no}_{[0,k]}$ il set di stati unobservable in $[0,k]$  allora:
$$
X^{no}_{[0,k]}=\ker \mathcal O_{[0,k]}=\ker\begin{bmatrix} H \\ HF \\ \vdots \\ HF^k \end{bmatrix}\equiv \bigcap_{i=0}^k\ker(HF^i)
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
X^{no}= X^{no}_{[0,\bar k]}\equiv X^{no}_{[0,k-1]}=\ker\begin{bmatrix} H \\ HF \\ \vdots \\ HF^{n-1}\end{bmatrix}=\mathcal O\in \mathbb R^{np\times n}
$$
$\mathcal O$= observability matrix of the pair $(F,H)$

### Definition \[observable]
Diciamo che $\Sigma$ (il paio $(F,H)$ ) è observable se $X^{no}\equiv \set{0}$ 
#### First observability criterion

$$
(F,H)\text{ observable }\iff\ker \mathcal O=\set{\underline 0}\iff rank\ \mathcal O=n 
$$
Se $(F,H)$ è osservabile allora quello che chiamiamo $\bar k$ diventa l' observability index e coincide con:
$$
\min\set{k:X^{no}_{[0,k-1]=n}}
$$


### Ex
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

$X^{no}_{[0,1]}=\ker \begin{bmatrix} H \\ HF \end{bmatrix}= \ker \begin{bmatrix}1 & 2 & 0 & -1 \\1 & 0 & 1&0\end{bmatrix}=<\begin{bmatrix}-1 \\0 \\1 \\-1 \\\end{bmatrix},\begin{bmatrix} -1 \\ 1/2 \\ 1 \\ 0 \end{bmatrix}>$

$X^{no}_{[0,2]}=\ker \begin{bmatrix} H \\ HF \\ HF^2\end{bmatrix}= \ker \begin{bmatrix}1 & 2 & 0 & -1 \\1 & 0 & 1&0\\3&0&2&0\end{bmatrix}=<\begin{bmatrix}0 \\1 \\0 \\2 \\\end{bmatrix}>$ 

$X^{no}_{[0,3]}=\ker \begin{bmatrix} H \\ HF \\ HF^2\\ HF^3\end{bmatrix}= \ker \begin{bmatrix}1 & 2 & 0 & -1 \\1 & 0 & 1&0\\3&0&2&0\\7&0&5&0\end{bmatrix}=X^{no}_{[0,2]}$ 
$\Rightarrow(F,H)$ Non è osservabile

$X^{no}=X^{no}_{[0,k]}\quad \forall k\ge 2=<\begin{bmatrix}0 \\1 \\0 \\2 \\\end{bmatrix}>$ 
Continua ...
### Soluzione del observation problem in \[0,k]
#ST-L26-1
Dato un [[Linear discrete time s.s.m.#Strictly Proper|DT system strictly proper]] e supponiamo di conoscere:
- $u(1)\dots u(k-1)$
- $y(0)\dots y(k)$ 
Cosa possiamo dire  di $x(0)$?
E' possibile identificare in modo univoco la "real initial condition" $x_o$  dalla quale è partito il sistema?
Da $(F,G,H)$ e $u(t)\quad t=0,\dots, k-1$ possiamo determinare la forced output evolution $y_f(t) \quad t=0,\dots ,k$ e di conseguenza anche la unforced output evolution $y_l(t)\quad t=1,\dots ,k$ 

Il problema sta nel determinare $x(0)$ da $y(t) \quad t=0,\dots ,k$ 
$$
Y_K\triangleq
\begin{bmatrix}y_l(0) \\y_l(1) \\\vdots \\y_l(k) \\\end{bmatrix}=
\begin{bmatrix} H \\ HF \\ \vdots\\ HF^k\end{bmatrix}x(0)=\mathcal O_{[0,k]}x(0)\qquad (1)
$$
L'unica cosa che non conosciamo di $(1)$ è $x(0)$ 
#### Case 1: $rank\ \mathcal O_{[0.k]}=n$
$\iff$ il sistema è osservabile e $k\ge$ observability index
In questo caso si ha che $\mathcal O_{[0,k]}^T\mathcal O_{[0,k]}$  è invertibile e quindi possiamo ottenere la soluzione di $(1)$: $x(0)=x_0$  in questo modo otteniamo:
$$
\mathcal O_{[0,k]}^TY_K=\mathcal O_{[0,k]}^T\mathcal O_{[0,k]}x(0)\qquad (2)
$$
$$
\rightarrow x(0)=x_0=\left[\mathcal O_{[0,k]}^T\mathcal O_{[0,k]}\right]^{-1}\mathcal O_{[0,k]}^TY_K
$$
#### Case 2: $rank\ \mathcal O_{[0,k]}<n$
$\Rightarrow X_{[0,k]}^{no}$ è un non trivial sottospazio vettoriale di $X$.
Se possiamo chiamare $\hat x_0$  una qualunque soluzione di  $(1)$  allora l'unica cosa che si può dire è:
$$
x_0\in\hat x_0+X_{[0,k]}^{no}\triangleq\set{\hat x_0+v\quad v\in X_{[0,k]}^{no}}
$$
### Continuo Ex
Determinare se possibile la condizione $x(0)$  corrispondente all' unforced output evolution $y_l(0)=0\quad y_l(1)=1\quad y_l(2)=3$ 
Siamo nel secondo caso dato che $\mathcal O_{[0,2]}<n=4$  e $X_{[0,2]}^{no} =<\begin{bmatrix}0 \\1 \\0 \\2 \\\end{bmatrix}>$ 

Se vogliamo risolvere $(1)$ :
$$
\begin{bmatrix}0 \\1 \\3 \end{bmatrix}=
\begin{bmatrix}y_l(0) \\y_l(1)  \\y_l(2) \\\end{bmatrix}=
O_{[0,2]}x_0=\begin{bmatrix}1 & 2 & 0 & -1 \\1 & 0 & 1&0\\3&0&2&0\end{bmatrix}x(0)
$$
quindi per ottenere $\begin{bmatrix}0 \\1 \\3 \end{bmatrix}$ basta andare ad usare la prima e l'ultima colonna sommandole tra loro
$$
\to \hat x_0=\begin{bmatrix}1 \\0 \\0 \\1 \\\end{bmatrix}\to
x_0\in \hat x_0+X_{[0,2]}^{no}=\left\{
\begin{bmatrix}1 \\0 \\0 \\1 \\\end{bmatrix}+
\alpha\begin{bmatrix}0 \\1 \\0 \\2 \\\end{bmatrix}\quad \alpha\in\mathbb R
\right\}
$$

## Reconstructability of DT ssm
Dato un [[Linear discrete time s.s.m.#Strictly Proper|DT system strictly proper]] e supponiamo di conoscere:
- $u(1)\dots u(k-1)$
- $y(0)\dots y(k)$ 
Come abbiamo [[Observation Problems DT#Soluzione del observation problem in [0,k|già visto]] possiamo identificare  la "real initial condition" $x_0$.
Nel primo caso  potevamo identificare $x_0$ e di conseguenza anche $x(k)$.
E' possibile fare lo stesso nel secondo caso?$$x(k)=F^kx(0)+\mathcal R_k\begin{bmatrix}u(k-1)\\u(k-2)\\\vdots\\u(0)\end{bmatrix}$$
	Si conosce sia $F^k$ che $\small\mathcal R_k\begin{bmatrix}u(k-1)\\u(k-2)\\\vdots\\u(0)\end{bmatrix}$  mentre $x(0)$ è un qualunque vettore in $\hat x_0+X_{[0,k]}^{no}$ 
E' facive vedere che:
$$
\begin{align}
x(k)\text{ uniquely determined} &\iff F^kx_0=F^k(x_0+v)&\forall v\in X_{[0,k]}^{no}\\
&\iff F^k v=0&\forall v\in X_{[0,k]}^{no}\\
&\iff X_{[0,k]}^{no}\subseteq \ker F^k
\end{align}
$$

In conclusione( comprendendo anche il caso 1, dato che si ha $\ker\mathcal O_{[0,k]}=\set\underline 0$) possiamo dire che il reconstruction problem è risolvibile in $[0,k]$ se:
$$
\ker \mathcal O_{[0,k]}\subseteq\ker(F^k)
$$
Questa è detta **reconstructability condition** ed è indipendente da $x_0$ 
Se la condizione è soddisfatta allora $(F,H)$ è ricostruibile in $[0,k]$ 

#### Remark
1. Se $(F,H)$ è ricostruibile in $[0,k]$ allora $(F,H)$ è ricostriuibile in $[0,k+1]$ 
2. Diciamo che  $(F,H)$ è ricostruibile se  $\exists k\ge 0$ s.t.  $(F,H)$ è ricostruibile in $[0,k]$ e questo è il caso se e solo se  $(F,H)$ è ricostruibile in $[0,n]$.
	Quindi:
	$$
	\begin{align}
	(F,H) \text{ ricostruibile}&\iff \ker \mathcal O_{[0,k]}\subseteq\ker F^n\\&\iff\ker \mathcal O\subset \ker F^n
	\end{align}
	$$
	Questo assomiglia alla controlalbilità
3. $(F,G)$ observable $\Rightarrow$ $(F,H)$ reconstructable
4. $(F,H)$ reconstructable $\Rightarrow$ (se $F$ è non singular) $(F,H)$ observable
### Ex
Dato un DT ssm:
$$
\begin{align}
x(t+1)=Fx(t)&=
\begin{bmatrix}
0 & 1 & 1 \\
1 & -1 & 1 \\
2 & -2 & 2 \\
\end{bmatrix}
x(t)\\
y(t)=Hx(t)&=
\begin{bmatrix} 0 & 1 & 1 \end{bmatrix}x(t)\\
\end{align}
$$
Controlla per ogni $k\in \mathbb Z+$  la reconstructiability in $[0,k]$ del sistema

Osserviamo che se $k=0$ la recons. in $[0,0]$ è equivalente all'observ. in $[0,0]$  quindi
$$\mathcal O_{[0,0]}=\ker H=\ker \begin{bmatrix} 0 & 1 & 1 \end{bmatrix}=<
\begin{bmatrix}1 \\0 \\0 \\\end{bmatrix},
\begin{bmatrix}0 \\1 \\-1 \\\end{bmatrix}
>$$
Di conseguenza il sistema non è recons. in $[0,0]$.
Consideriamo ora $k=1$  Abbiamo che la recons. in $[0,1]$ se e solo se 
$$
\ker \mathcal O_{[0,1]} = \ker \begin{bmatrix} H \\ HF \end{bmatrix}=\ker 
\begin{bmatrix}
0 & 1 & 1 \\
3 & -3 & 3 \\
\end{bmatrix}=<
\begin{bmatrix}2 \\1 \\-1 \\\end{bmatrix}>\ \subseteq \ker F
$$
Dato che appartiene al $\ker F$ abbiamo recons. in $[0,1]$ e per ogni $k\ge 1$ 