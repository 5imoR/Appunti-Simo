#CO-L13-2
Se la funzione da ottimizzare è convessa allora abbiamo:
$$f(x^{k+1})\ge f(x^k)+\nabla f(x^k)^T(x^{k+1}-x^k)$$
quindi se vogliamo trovare la direzione lungo la quale scendiamo:
$$\nabla f(x^k)^T\Delta x^k<0$$
La scelta più ovvia è $\Delta x=-\nabla f(x)$ quindi equivale al gradiente negativo. Otteniamo così:
$$\nabla f(x^k)^T \Delta x^k=-||\nabla f(x^k)||^2<0$$
a meno che il gradiente non sia nullo, ma in quel caso vuol dire che abbiamo raggiunto il minimo.


![[Descent Lemma#Descent Lemma]]

#CO-L14-2
La descent lemma implica un upper bound quadratico  sulla funzione $f$  che è minimizzato per:
$$\displaystyle\hat y=x-\frac 1 M\nabla f(x)\ \ \text{ e quindi }\ \ t^k=\frac 1M$$
#### Proof
Abbiamo $t=\frac 1M$ e la direzione $-\nabla f(x)$ allora:
$$x^{k+1}-x^{k}=-\frac 1M\nabla f(x^k)$$
se lo inseriamo nella disequazione della Descend Lemma:
$$
\begin{align}
f(x^{k*1})&\le f(x^k)+\nabla f(x^k)^T{\color{orange}(x^{k+1}-x^k)}+\frac 1 2M {\color{orange}||x^{k+1}-x^{k}||^2}\\
&=f(x^k){\color{orange}-\frac 1M||\nabla f(x^k)||^2}+\frac M2{\color{orange}\frac1{M^2}||\nabla f(x^k)||^2}\\
&=f(x^k)-\underbrace{\frac 1{2M}||\nabla f(x^k)||^2}_{\text{fattore di miglioramento}}
\end{align}
$$
####
Possiamo dire:
$$
\begin{align}
&||\nabla f(x^k)||^2\le 2M(f(x^k)-f(x^{k+1}))\\
&\frac 1s\underbrace{\sum_{k=0}^{s-1}||\nabla f(x^k)||^2}_\text{il min da un lower bound}\le
\frac {2M}s\underbrace{\sum_{k=0}^{s-1}(f(x^k)-f(x^{k+1}))}_\text{telescopic sum}\\
\\
&\min_{k=0\dots s-1}||\nabla f(x^k)||^2\le\frac {2M}s(f(x_0)-\overbrace{f(x^s)}^{p^*})
\end{align}
$$
Quindi troviamo che  è $O(\frac 1s)$. 
$$
\min_{k=0\dots s-1}||\nabla f(x^k)||^2\le\frac {2M(f(x_0)-f(p^*))}s\quad \frac{\text{costante}}{\text{se aumenta tutto diminuisce}}
$$
Noi vogliamo trovare un valore di $s$ per il quale sia minore di un certo $\varepsilon$ quindi:
$$
s\ge \frac{2M(f(x_0)-f(p^*))}\varepsilon
$$
Il problema è che per passare da una precisione di $0.1$ a $0.01$ mi servono 10 volte tanti valori
- Questo si applica anche al caso non convesso, ma non garantisce che quello che otteniamo sia un minimo globale
Esiste una soluzione migliore data da ![[PL Inequality#Polyak-Lojasiewicz Inequality]]
Tramite conti e PL inequaliti possiamo arrivare a:
$$
\Large
s\ge \frac{\frac{\log(f(x^0)-p^*)}\varepsilon}{\log\frac 1\rho}=O\left(\log\frac1\varepsilon\right)
$$
