#ST-L28-1
Dato un [[Observability & Reconstructability DT|observation, reconstruction problem]] del quale conosciamo:
- $\Sigma=(F,G,H)$ 
- $u(t)\quad t\in [0,T]$
- $y(t)\quad t\in [0,T]$
Per calcolare $x(0)$ e $x(T)$ si collezionano dati e poi si fanno i conti.
Quello che vogliamo fare è esattamente questo ma in maniera dinamica in un qualunque momento $t$:

# State Observer
Conosciamo:
- $\Sigma=(F,G,H)$ 
- $u(t)\quad t\ge0$
- $y(t)\quad t\ge0$
Vogliamo fare il design di un nuovo ssm $\hat\Sigma$ che riceve come input i segnali $u(\cdot)$ e $y(\cdot)$  e produce come output una stime $\hat x(\cdot)$ dello stato di $\Sigma$

Chiamiamo $\hat \Sigma$  Asymptotic Observer(asymptotic state observer) di $\Sigma$ se una volta calcolata la stima dell'errore vediamo che :
$e(t)\triangleq x(t)-\hat x(t)$  
allora:   $\displaystyle\lim_{t\to+\infty}e(t)=0$ 


**ORA FACCIAMO TUTTI I CONTI IN DT MA TUTTO QUANTO VALE ANCHE IN CT**

![[Linear discrete time s.s.m.#Strictly Proper]]

Esploreremo tre soluzioni:
- Full order Observer:$(dim \hat \Sigma=dim\Sigma = n)$
	- Open Loop Observer
	- Closed Loop Observer
- Reduced order Observer:$(dim \hat \Sigma<dim\Sigma)$

## Full Order Open Loop Observer
$$
\hat\Sigma_{OL}:
\begin{cases}
\hat x(t+1)=F\hat x(t)+Gu(t)\\
\hat y(t)=H\hat x(t) \qquad t\in\mathbb Z+
\end{cases}
$$
Non possiamo dire che $x(t)=\hat x(t)$ perchè non conosciamo le condizioni iniziali
Quello che conosciamo è solo $\Sigma$ e $u(t)$ 

Se definiamo $e(t)=x(t)-\hat x(t)$
allora   
$$
\begin{align}
e(t+1)&=x(t+1)-\hat x(t+1)\\&=[Fx(t)+\cancel{Gu(t)}]-[F\hat x(t)+\cancel{Gu(t)}]\\
&=F(x(t)-\hat x(t))=Fe(t)\\
\\
e(t+1)&=Fe(t)
\end{align}
$$
Inoltre $\hat \Sigma_{OL}$ è un asymptotic observer  allora:
$$
\lim_{t\to+\infty}e(t)=0\iff F\text { is asymptoticaly stable}
$$
#### CT case
L'unica differenza è che si ha $\dot e(t)=Fe(t)$ 
#### Remark
Dato che $x(t)=x_l(t)+x_f(t)$ e $x_f(t)$ è conosciuto allora possiamo sempre scegliere:
$\hat x(0)=0\Rightarrow \hat x(t)=x_f(t)$ ed il problema diventa assicurare che $e(t)=x_l(t)\to_{t\to+\infty}0$ che succede se e solo se  $\Sigma è asintoticamente stabile

## Full Orded Closed Loop Observer
IDEA:   $\Sigma_{OL}$ usa solo l'input, che succede se utilizzassimo anche l'output?
IDEA:   Se cibisci $e(t)$ usando $x(t)\hat x(t)+e(t)$ potrei correggere la mia stima e identificare subito il vero valore di $x(t)$. Dato che $e(t)$ non è disponibile serve trovare un altra via per correggere la stima dello stato.
Un possibile modo è quello di usare l' output estimation error (che è disponibile)

$$e_y(t)\triangleq y(t)-\hat y(t)=y(t)-H\hat x(t)=He(t)$$
$$
\hat\Sigma_{CL}:
\begin{cases}
\hat x(t+1)=F\hat x(t)+Gu(t)- Le_y(t)\\
\hat y(t)=H\hat x(t) \qquad t\in\mathbb Z+
\end{cases}\quad=\quad
\begin{cases}
 F\hat x(t)+Gu(t)+L[H\hat x(t)-y(t)]\\
\hat y(t)=H\hat x(t) \qquad t\in\mathbb Z+
\end{cases}
$$
![[observer]]
Se definiamo $e(t)=x(t)-\hat x(t)$  allora
$$
\begin{align}
e(t+1)&=x(t+1)-\hat x(t+1)\\
&=[Fx(t)+\cancel{Gu(t)}]-[F\hat x(t)+\cancel{Gu(t)}]+L[H\hat x(t)-Hx(t)]\\
&=(F+LH)\ x(t)-(F+LH)\  \hat x(t)\\
&=(F+LH)e(t)\\
\\
e(t+1)&=(F+LH)e(t)
\end{align}
$$
La matrice $L$ che abbiamo introdotto è un parametro libero chiamato Observer gain usato per rendere $\hat x(t)$ (dimensione $n$ ) e $e_y(t)$ (dimensione p) compatibili.
Inoltre $\hat \Sigma_{CL}$ è un asymptotic observer  allora:
$$
\lim_{t\to+\infty}e(t)=0\iff F+LH\text { is asymptoticaly stable}
$$
Per quali condizioni esiste $L\in\mathbb R^{n\times p}$ s.t. $F+LH$ è asintoticamente stabile?

$$
\begin{align}
\exists L\in \mathbb R^{n\times p} s.t. F+LH \text{ asimptoticaly stable}\\\\
\Updownarrow\phantom{ssssssssssssssssssss}\\\\
\exists L\in \mathbb R^{n\times p} s.t. F^T+H^TL^T \text{ asimptoticaly stable}\\\\
\Updownarrow\phantom{ssssssssssssssssssss}\\\\
\exists K\in \mathbb R^{p\times n} s.t. F^T+H^TK\text{ asimptoticaly stable}\\
(\text{stabilization problem for} \Sigma_d=(F^T,H^T,G^T))\\\\
\Updownarrow\phantom{ssssssssssssssssssss}\\\\
\text{is reachable OR isn't reachable but the matrix $F_{22}$}\\
\text{ of the non reachable subsystem is asimptoticaly stable}\\\\
\Updownarrow\ \text{duality}\phantom{sssssssssssss}\\\\
\text{is observable OR isn't observable but the matrix $F_{22}$}\\
\text{ of the unobservable subsystem is asimptoticaly stable}\\
\end{align}
$$
Di conseguenza per la [[AG/M/SYSTEM THEORY/CT & DT/Duality|Duality]]  possiamo ereditare questi risultati:
### Proposition: 
Dato un paio $(F,H)$ con $F\in\mathbb R^{n\times n}$ e $L\in\mathbb R^{n\times p}$  che rappresentano sia un DT che un CT system quello che segue è equivalente:
- $\exists L\in \mathbb R^{n\times p}$  s.t. $F+LH$ è asintoticamente stabile (ovvero il paio ammette un A.C.L.Observer)
- O $(F,H)$ è osservabile oppure $F_{22}$ dell' unobservable subsystem è asintoticamente stabile $\triangleq (F,H)$ è detectable
- $rank\begin{bmatrix} \lambda In-F \\ H \end{bmatrix} =n$  
	- CT $\forall \lambda \in\mathbb C\quad Re(\lambda)\ge 0$
	- DT $\forall \lambda \in\mathbb C\quad |\lambda|\ge 1$ 

#### Remark
Stabilizability è duale con la detectability 
![[DBO Dead Beat Observer (Full Order Closed Loop)#Proposition [caracterization of the existence of a DBO]]

## Reduced order Observer
IDEA: Supponiamo  che nel nostro ssm $\Sigma=(F,G,H)$ la matrice $H$ prende la forma seguente $H=[0|I_p]$ 
Questo  significa che $y(t)=[0|Ip]\ [x(t)]$ quindi se facciamo una block partition su $x(t)=\begin{bmatrix}x_1(t) \\x_2(t) \\\end{bmatrix}\begin{array}{c}\}n-p \\\}p\phantom{ssss}\end{array}$
allora $x_2(t)=y(t)$  quindi il mio problema diventa stimare $x_1(t)$ 

### Problem
Vogliamo vedere se è sempre possibile ritornare alla situazione orecedente nella quale l'output coincide con una parte delle variabili di stato.
Se così vogliamo vedere se è possibile sviluppare un observer di $dim<n$  per stimare solo le variabili di stato rimaste.
Hypotesis
$[H]\in\mathbb R^{p\times n}$
se full row rank$= p$
possiamo sempre ridurci a questo caso liberandoci delle righe di $H$ che sono linearmente dipendenti dalle altre (i.e. misure ridondanti nell'output)
se rank$=p$ 
allora $\exists V \in \mathbb R^{(n-p)\times n}$ s.t. $\begin{bmatrix} V \\ H \end{bmatrix}$ è non singular square $\Rightarrow$ $T\triangleq\begin{bmatrix} V \\ H \end{bmatrix}^{-1}$ esiste ed è non singular square

se usiamo T come matrice di cambiamento di base  allora la descrizione del sistema w.r.t. la nuova base di $X$ è:
$$
\bar x(t)=T^{-1}x(t)=\begin{bmatrix} V \\ H \end{bmatrix}x(t)\triangleq\begin{bmatrix} W(t) \\ y(t) \end{bmatrix}\begin{array}{c}\}n-p \\\}p\phantom{ssss}\end{array}\qquad w(t)\triangleq Vx(t)
$$
$$
\begin{align}
A\triangleq T^{-1}FT=\begin{bmatrix}A_{11}&A_{12}\\A_{21}& A_{22}\\\end{bmatrix}
\begin{array}{c}\}n-p \\\}p\phantom{ssss}\end{array}\qquad B\triangleq T^{-1}G=\begin{bmatrix} B_1 \\ B_2 \end{bmatrix}\begin{array}{c}\}n-p \\\}p\phantom{ssss}\end{array}\qquad C\triangleq HT=\begin{bmatrix} 0 & I_p\end{bmatrix}\ \ \\
\underbrace{}_{n-p}\underbrace{}_{p}\phantom{sssssssssssssssssssssssssssss}\phantom{sssssssssssssssasssss}\underbrace{}_\rho\underbrace{}_{n-\rho}
\end{align}
$$
#ST-L29-1
Di conseguenza il sistema è rappresentato  w.r.t. la nuova base come:
$$
\begin{cases}
W(t+1) = A_{11} W(t) + A_{12} y(t) + B_1 u(t) \\
y(t+1) = A_{21} W(t) + A_{22} y(t) + B_2 u(t) 
\end{cases}
$$
Introduciamo una nuova variabile di stato $v(t)\triangleq W(t)+Ly(t)$ dove  $L\in \mathbb R^{(n-p)\times p}$ è una design matrix parameter
$$
\begin{align*}
v(t+1) &= W(t+1) + L y(t+1) \\
&= [A_{11} W(t) + A_{12} y(t) + B_1 u(t)] + L [A_{21} W(t) + A_{22} y(t) + B_2 u(t)]\\
&= [A_{11} + L A_{21}] W(t) + [A_{12} + L A_{22}] y(t) + [B_1 + L B_2] u(t) \\\\
W(t+1) &= v(t+1) - L y(t+1) \\
W(t+1) &= [A_{11} + L A_{21}] W(t) + \underbrace{[[A_{12} + L A_{22}] - [A_{11} + L A_{21}] L]}_{\triangleq M} y(t) + \underbrace{[B_1 + L B_2]}_{\triangleq N} u(t)
\end{align*}
$$
$$
\begin{align*}
v(t+1) &= W(t+1) + L y(t+1) \\
&= [ {\color{lightgreen}A_{11}} W(t) + {\color{lightblue}A_{12}} y(t) + {\color{orange}B_1} u(t)] + L [ {\color{lightgreen}A_{21}} W(t) + {\color{lightblue}A_{22}} y(t) + {\color{orange}B_2} u(t)]\\
&= [{\color{lightgreen}A_{11} + L A_{21}}] W(t) + [{\color{lightblue}A_{12} + L A_{22}}] y(t) + [{\color{orange}B_1 + L B_2}] u(t) \\\\
W(t+1) &= v(t+1) - L y(t+1) \\\\
&= [{\color{lightgreen}A_{11} + L A_{21}}] v(t) + \underbrace{[ [ {\color{lightblue}A_{12} + L A_{22}}] - [ {\color{lightgreen}A_{11} + L A_{21}}] L]}_{\triangleq M} y(t) + \underbrace{[ {\color{orange}B_1 + L B_2}]}_{\triangleq N} u(t)
\end{align*}$$
$\Rightarrow v(t+1)=[A_{11}+LA_{21}]v(t)+\begin{bmatrix} M & N \end{bmatrix}\begin{bmatrix} y(t) \\ u(t) \end{bmatrix}$ 

Introduciamo ora un [[State Observer#Full Order Open Loop Observer|FOOLO]]  per $v(t)$
$$
\hat v(t+1)=[A_{11}+LA_{21}]\hat v(t)+\begin{bmatrix} M & N \end{bmatrix}\begin{bmatrix} y(t) \\ u(t) \end{bmatrix}\qquad \blacktriangleleft
$$
L'estimation error è 
$$
e_v(t)\triangleq v(t)-\hat v(t)\qquad e_v(t+1)=(A_{11}+LA_{21})e_v(t)
$$
Sappiamo che  
$$
e_v(t)_{\forall e_v(0)} \underset{t\to+\infty}{\longrightarrow} 0\iff A_{11}+LA_{21} \text{ aspymptoticaly stable}
$$
Usando la teoria del [[State Observer#Full Orded Closed Loop Observer|FOCLO]]  possiamo dire che 
$$
\begin{gather}
\exists L\in\mathbb R^{(n-p)\times p}s.t. A_{11}+LA_{21} \text{ is asymptotically stable}\\
\Updownarrow\\
<A_{11},A_{21}>\text{ is detectable}\\
\Updownarrow\\
rank
\begin{bmatrix} \lambda I_{n-p}-A_{11} \\ A_{21} \end{bmatrix}
=n-p\qquad \forall\lambda\in\mathbb C\quad |\lambda|\ge 1
\end{gather}
$$
![[Lemma Equivalenza di Osservabilità#Lemma]]
![[Lemma Equivalenza di Osservabilità#Conseguenze]]

Block Diagram of reduced order observer
![[reducedOrderObserver|600]]
#### Ex
Dato un DT sys. 
$$
\begin{align}
&\Sigma:
\begin{cases}
x(t+1)&=Fx(t)=
\begin{bmatrix}
1 & 2 & 0 \\
0 & 2 & 0 \\
1 & 1 & 0 \\
\end{bmatrix}x(t)\\
y(t)&=Hx(t)=
\ \begin{bmatrix}
1 & 0 & 0 \\
\end{bmatrix}x(t)
\end{cases}\\
&n=3\qquad p=1\\
\end{align}
$$
- Design if possible a full order closed loop DBO
Il paio può $(F,H)$ lo si può vedere come:
$$
F=\begin{bmatrix}
F_{11} & 0 \\
F_{21} & F_{22} \\
\end{bmatrix}\qquad
H=\begin{bmatrix}
H_1 & H_2 \\
\end{bmatrix}
$$
Possiamo dire che:
$\mathcal O=\begin{bmatrix}H_1\\H_1F_{11}\end{bmatrix}=\begin{bmatrix}1 & 0 \\1 & 2 \\\end{bmatrix}$ has full column rank $= 2$
$\Rightarrow (F_{11},H_1)$ is observable
$\Rightarrow(F,H)$ è in [[AG/M/SYSTEM THEORY/CT & DT/Duality#3 Standard Observability Form SOB|SOF]] e $F_{22}=[0_{1\times 1}]$ 
Questo assicura che esiste un DBO
Set $L=\begin{bmatrix} L_1 \\ L_2 \end{bmatrix}=\begin{bmatrix} a \\ b \\ c \end{bmatrix}$ 
$$
F+LH=
\begin{bmatrix}
1+a & 2 & 0 \\
b & 2 & 0 \\
1+c & 1 & 0 \\
\end{bmatrix}
$$
Per far si che $F+LH$ sia [[Nilpotent matrix|nilpotent]] è sufficiente imporre che  $F_{11}+L_1H{1}=\begin{bmatrix}1+a & 2 \\b & 2 \\\end{bmatrix}$ sia nilpotent ovvero:
$$
\begin{align}
&\det
\begin{bmatrix}
z-1-a & -2 \\
-b & z-2 \\
\end{bmatrix}=z^2\\\\
&=(z-1-a)(z-2)-2b\\
&=z^2+(-3-a)z+(2+2a-2b)\\
&L=\begin{bmatrix} -3 \\ -2 \\ c \end{bmatrix}\quad c\in \mathbb R
\end{align}
$$
- Design if possible a reduced order observer whose estimation error converges as $(\frac 12)^t$ for almost all initial conditions
Che vuol dire: $\exists L\in \mathbb R^{2\times 1}$ s.t. $\frac 12\in\sigma(A_{11}+LA_{21})$. Qualunque altro autovalore di $A_{11}+LA_{21}\ge 1$  ha modulo minore di $\frac 12$ 

Questo è possibile perchè:
- $A_{11}+LA_{21}$ ha dimensione $2$ e quindi ha $2$ autovalori. uno di questi è vincolato e deve valere $0$   ($F_{22}$)
- l'altro può essere assegnato liberamente e in particolare può essere settato come $\frac 12$ 

$$\sigma(A_{11}+LA_{21})=\set{0,\frac 12}$$
dato che $H=\ \begin{bmatrix}1 & 0 & 0 \\\end{bmatrix}$ full row rank allora:
$$
\begin{align}
&T^{-1}=\begin{bmatrix} V \\ H \end{bmatrix}=
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
\end{bmatrix}\equiv T\\\\
&A=T^{-1}FT=\begin{bmatrix}
0 & 1 & 1 \\
0 & 2 & 0 \\
0 & 2 & 1 \\
\end{bmatrix}
\begin{array}{c}\left.\begin{array}{c}\ \\\ \end{array}\right\}n-\rho \\  \}\rho\phantom{sss}
\end{array}\\
&A_{11}=\begin{bmatrix} 0 & 1 \\ 0 & 2 \end{bmatrix}\qquad
A_{21}=\begin{bmatrix} 0 & 2 \end{bmatrix}\qquad
L=\begin{bmatrix} a \\ b\end{bmatrix}\\
&A_{11}+LA_{21}=\begin{bmatrix} 0 & 1+2a \\ 0 & 2+2b \end{bmatrix}=
\begin{bmatrix} 0 & * \\ 0 & \frac12 \end{bmatrix}\\
&L=\begin{bmatrix} a \\ -\frac 34\end{bmatrix}\quad a\in\mathbb R
\end{align}
$$
