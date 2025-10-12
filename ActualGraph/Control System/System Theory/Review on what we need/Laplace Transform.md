[[SYSTEM THEORY#Ripasso di State Space Models a tempo continuo]] #ST-L5

Usata in s.s.m. a tempo continuo:
$$
\begin{cases}
\dot{x}(t)&=Fx(t)+Gu(t)\\
y(t)&=Hx(t)+Du(t)  \\
\end{cases}
$$
$X(s)=\mathcal L[x(t)]\quad U(s)=\mathcal L[u(t)]\quad Y(s)=\mathcal L[y(t)]$ 

Applicando la trasformata di Laplace ad entrambi i lati otteniamo:
$$
\begin{align}
\mathcal L[\dot x(t)]=&sX(s)-x(0)=FX(s)+GU(s)\\
&(sIn-F)X(s)=x_0+GU(s)\\
\\
&X(s)=\underbrace{(sIn-F)^{-1}x_0}_{x_l}+
\underbrace{(sIn-F)^{-1}GU(s)}_{x_f}\\
&Y(s)=\underbrace{H(sIn-F)^{-1}x_0}_{y_l}+
\underbrace{[(sIn-F)^{-1}G+D]U(s)}_{y_f}
\end{align}
$$
(si può notare che l'unica differenza dalla z transform è in $x_l, y_l$ )
	$$\begin{align}
	&X(z)=\underbrace{(zIn-F)^{-1}{\color{orange}z}\ x_0}_{x_l}+\underbrace{(zIn-F)^{-1}GU(z)}_{x_f}\\
	&Y(z)=\underbrace{H(zIn-F)^{-1}{\color{orange}z}\ x_0}_{y_l}+\underbrace{[(zIn-F)^{-1}G+D]U(z)}_{y_f}\\
	\end{align}$$


Definiamo la matrice di trasferimento del sitema $\Sigma=(F,G,H,D)$ :
$$
W(s)\triangleq H(sIn-F)^{-1}G+D\quad\in\ \mathbb R(s)^{p\times n} 
$$
E' proper, se $D=0$ allora diventa strictly proper

$$
\{\text{poli di }W(z)\}\triangleq\bigcup_{\substack{i \in \{1, \dots, p\} \\ j \in \{1, \dots, m\}}}\ \{\text{poli di } W_{ij}(z)\}\subseteq \sigma(F) (\text{set degli autovettori di F})
$$
