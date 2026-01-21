  #CO-L14-4
$f(x)=\frac 1{|D|}\sum_{i\in D}f_i(x)$ 
$f:\mathbb R^n\to\mathbb R\quad |D|>>n$ 

Nel gradient descend si ha:
$$
\nabla f(x)=\frac 1{|D|}\sum_{i\in D}\nabla f_i(x)
$$
il quale necessita troppi conti, una soluzione è usare un singolo campione per volta (On Line SGD, più avanti si vede il minibatch SGD) .

### On Line SGD
$$
\begin{align}
E[\nabla f_{ik}(x)]&=\sum_{i\in D} p[i_k=i]\nabla f_i(x)\\
&=\frac 1{|D|}\sum_{i\in D}\nabla f_i(x)\\\\
&=\nabla f(x)\\

\end{align}
$$

Vogliamo ridurre la cost iteration in SGD e nel coordinate descend
$f(x)=\frac 1 {|D|}\sum_{i\in D}f_i(x)\quad O(n\cdot|D|)$  può succedere che $|D|>>n$ 
	- $|D|$ numero di campioni
	- $n$ numero di features
### Proof
[[Unconstrained.pdf#page=7|SGD.pdf]] 

$$
\begin{align}
f(x^{k+1})&\le f(x^k)+\nabla f(x^k)^T(x^{k+1}-x^k)+\frac M2||x^{k+1}-x^k||^2\\
&\downarrow \text{guarda il pdf}\\
E[f(x^{k+1})]&\le f(x^k)-t_k||\nabla f(x^k)||^2 +{\color {orange}t_k^2\frac M2E[\ ||\nabla f_{ik}(x^k)||^2]}
\end{align}
$$
$\textcolor{orange}{■}$ parte che fa crescere l'equazione, si rischia di non convergere
si deve avere che $t_k>>t_k^2$ 

Assumiamo ci sia una varianza finita e quindi:
$$
E[\ ||\nabla f_{ik}(x^k)||^2] \le\sigma^2
$$
quindi riprendendo i conti di prima e andando a sostituire con $\sigma^2$ si arriva ad ottenere:
$$
\begin{align}
\sum_{k=0}^st_k \underbrace{E[\ ||\nabla f(x^k)||^2]}_\text{lower bounded by min.} &\le
\sum_{k=0}^s\underbrace{(E[f(x^k)]-E[f(x^{k+1})])}_\text{telescopic sum.}+\frac M2\sigma^2 \sum_{k=0}^st_k^2\\\\
\min_{k=0\dots s}E[\ ||\nabla f(x^k)||^2]&\le \frac {f(x^0)-p^*}{\sum_{k=0}^st_k}+\frac M2\sigma^2\frac{\sum_{k=0}^st_k^2}{\sum_{k=0}^st_k}
\end{align}
$$
Quindi per avere il gradiente che tende a zero è necessario avere
- $\sum_{k=0}t_k\to+\infty$
- $\sum_{k=0}t_k^2\to O(1)$
Prendiamo $t_k=\frac ak$ per una qualche costante $a$ si ottiene:
- $\sum_{k=0}^s\frac ak=O(\log s)$  
- $\sum_{k=0}^s\frac{a^2}{k^2}=O(1)$ 
Dopo $s$ iterazioni l'errore è: $O(\frac 1{\log s})$ questo è peggio di $\displaystyle O(\frac 1 \epsilon)$   

Prendiamo $t_k=a$  si ottiene:
- errore di $O(\frac 1s)+O(a)$ che non converge a zero per $k\to\infty$ 
Per strongly convex function:
- $t_k=\frac 1{mk}$ ci dà: $O(\frac 1s)$ 
- $t_k=a<\frac 12m$ ci dà: $O(\rho^s)+O(a)$ 

Da questo si può notare che con uno stepsize costante si ottene una convergenza più rapida ma limitata dal valore di $a$
![[probleminside]]
### Mini-batch SGD
Si prende più di un campione(solitamente si sceglie il numero in base alle statistiche della macchina che si usa) ad ogni terazione in modo da avere una approssimazione migliore del vero gradiente a $x^k$.
I campioni vengono scelti randomicamente e vanno a formare $B^k$ (cambia ad ogni iterazione)
La $k$-esima iterazione può essere scritta come:
$$
\begin{align}
\Large x^{k+1}&\Large=x^k-t_k\frac 1{|B|}\sum_{i\in B^k}\nabla f_i(x^k)\\
\end{align}
$$
Consideramo la direzione del mini-batch come il vero gradiente $\nabla f(x^k)$ più del rumore $e^k$  che dipende dai campioni scelti.
Scegliendo una step size costante $t_k=\frac 1M$ e ripetendo i passaggi della [[Descent Lemma]] si ottiene:
$$
f(x^{k+1})\le f(x^k)-\underbrace{\frac 1{2M}||\nabla f(x^k)||^2}_\text{good term} +\underbrace{\frac 1 {2M}||e^k||^2}_\text {bad term} 
$$
$||e^k||^2$ cambia in base a $|B^k|$. Più precisamente assumendo una varianza finita e un campionamento con rimpiazzo si ottiene: $\displaystyle E[\ ||e^k||^2]=\frac 1{|B^k|}\sigma^2$ quindi diminuisce all'aumentare dei campioni.
Più generalmente, se prendiamo  senza rimpiazzo dall'intero set di $d$ gradienti otteniamo:
$$
\Large E[\ ||e^k||^2 \ ]=\frac{d-|B^k|}d\frac 1{|B^k|}\sigma^2
$$
che tende a zero per $|B^k|\to d$

Si possono sviluppare delle regola per andare ad aumentare $|B^k|$ poichè vanno ad aumentare la dimensione di $B$ troppo in fretta. In pratica si raddoppia la dimensione di $B$ quando viene rilevato uno stallo.