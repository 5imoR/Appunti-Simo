---
tags:
---
#ST-L16-3 #DTCT
## Theorem CCF
Assumiamo:
- $F\in\mathbb R^{n\times n}$  
- $g\in\mathbb R^n$ 
Allora $(F,g)$ è reachable $\iff\exists T\in \mathbb R^{n\times n}$ non singular s.t.
$$
T^{-1}FT=F_c
\begin{bmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
0 & 0 & 0 & \ddots & 0 \\
0 & 0 & 0 & \ddots & 1 \\
-a_0 & -a_1 & -a_2 & \dots & -a_{n-1} \\
\end{bmatrix}\qquad
T^{-1}g=g_c=
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0 \\
1 \\
\end{bmatrix}
$$
Questa è detta *Controlleable canonical form*
$F_c$ è detta *Companion Matrix*
## Proof
$\Leftarrow$
se $(F,g)$ è [[R7 Basis of vector spaces and algebraically equivalent system#Definition algebraically equivalent|algebricamente equivalente]]  al paio $(F_c, g_c)$  allora, avendo:
- $\mathcal R_c=[g_c|F_cg_c|\dots|F_c^{n-1}g_c]$ 
- $\mathcal R=[g|Fg|\dots|F^{n-1}g]$
$$
\mathcal R_c=T^{-1}\mathcal R
$$
ed $\mathcal R_c$ sarà qualcosa del tipo:
$$
\begin{bmatrix}
0 & 0 & 0 & \dots &0& 1 \\
0 & 0 & 0 & \dots & 1& * \\
\vdots & \vdots & \vdots & 1 &\dots& \vdots \\
\vdots & \vdots & 1 & * &\dots& \vdots \\
\vdots & 1 & * & * &\dots& \vdots \\
1 & * & * & * &\dots& * \\
\end{bmatrix}
$$
$\Rightarrow rank \mathcal\ R_c=n\Rightarrow\ rank \mathcal\ R=n \Rightarrow(F,g)\text{ è reachable}$


$\Rightarrow$ Abbiamo assunto che se $(F,g)$ è raggiungibile $\Rightarrow\mathcal R$ ha $n$ colonne linearmente indipendenti
Assumiamo:
- $\Delta_F(s)=s^n+a_{n-1}s^{n-1}+\dots+a_1s+a_0\in \mathbb R[s]$ 
Basandoci sulle colonne di $\mathcal R$ e i coefficenti di $\Delta_F(s)$ vogliamo costruire la matrice $T$ in modo tale che sia invertibile e $(T^{-1}FT,T^{-1}g)$  sia in CCF.
mettiamo:
$$
\begin{align}
\color {lightgreen}v_n&=g\\
\color {orange}v_{n-1}&=Fg+a_{n-1}g\\
\color {cyan}v_{n-2}&=F^2g+a_{n-1}Fg+a_{n-2}g\\
&\ \  \vdots\\
\color {magenta}v_2 &=F^{n-2}g+a_{n-1}F^{n-3}+\dots+ a_2g\\
\color {pink}v_1 &=F^{n-1}g+a_{n-1}F^{n-2}+\dots+ a_1g\\
\end{align}
$$
Questa è già una famiglia indipendente
$T=[v_1|v_2|\dots|v_m]\in \mathbb R^{n\times n}$ è invertibile

vogliamo provare che $T^{-1}FT=F_c$  che è equivalente a provare $FT=TF_c$ 
$$
F\ [v_1|v_2|\dots|v_{n-1}|v_n]=[v_1|v_2|\dots|v_{n-1}|v_n]\ F_c
$$

Per fare ciò serve calcolare $Fv_i\quad i=1\dots n$ 
$$
\begin{align}
Fv_n&= Fg\\
&= [Fg+a_{n-1}g]-a_{n-1}g\\
&={\color {orange}v_{n-1}}-a_{n-1}\color{lightgreen}v_n\\
\\
Fv_{n-1} &=F^2g+a_{n-1}Fg\\
&=[F^2g+a_{n-1}Fg]-a_{n-2}g\\
&={\color{cyan} v_{n-2}}-a_{n-2}\color {lightgreen}v_n\\
\\
&\ \ \vdots\\
\\
Fv_2&={\color {pink}v_1}-a_1\color {lightgreen} v_n\\
\\
Fv_1&= F^ng+a_{n-1}F^{n-1}g+\ldots +a_1Fg\\
&=[F^ng+a_{n-1}F^{n-1}g+\ldots+a_0g]-a_0g\\
&=\cancel{[F^n+a_{n-1}F^{n-1}+\ldots+a_0]}g-a_0g\qquad\text{ per Hamilton}\\
&=\Delta_F(F)=0_{n\times n}\\
&= -a_0\color {lightgreen} v_n
\end{align}
$$

[[Cayley-Hamilton's theorem#Cayley-Hamilton's theorem|Hamilton]] 

allora: (sono la stessa cosa sono 2 solo per evidenziare cose diverse)
$$
[F{\color{pink}v_1}|F{\color{cyan}v_2}|\dots|F{\color{orange}v_{n-1}}|F{\color{lightgreen}v_n}]=[v_1|v_2|\dots|v_{n-1}|v_n]
\begin{bmatrix}
0 &\color {pink} 1 && 0 & 0\\
0 &0 &&\vdots &\vdots \\
\vdots &\vdots &\dots &\vdots &\vdots \\
0 & 0& & \color{orange}1&0\\
0 & 0& & 0&\color{lightgreen} 1\\
-a_0&-a_1& &-a_{n-2}&-a_{n-1}
\end{bmatrix}
$$
- $Fv_n={\color {orange}v_{n-1}}-a_{n-1}\color{lightgreen}v_n$ 
- $Fv_{n-1} ={\color{cyan} v_{n-2}}-a_{n-2}\color {lightgreen}v_n$ 
- $Fv_2={\color {pink}v_1}-a_1\color {lightgreen} v_n$ 
- $Fv_1=-a_0\color {lightgreen} v_n$ 

$$
[{\color{pink}Fv_1}|{\color{magenta}Fv_2}|\dots|{\color{orange}Fv_{n-1}}|{\color{lightgreen}Fv_n}]=[v_1|v_2|\dots|v_{n-1}|v_n]
\begin{bmatrix}
\color {pink}0 &\color {magenta} 1 && \color{orange}0 & \color{lightgreen}0\\
\color {pink}0 &\color {magenta}0 &&\color{orange}\vdots &\color{lightgreen}\vdots \\
\color {pink}\vdots &\color {magenta}\vdots &\dots &\color{orange}\vdots &\color{lightgreen}\vdots \\
\color {pink}0 &\color {magenta} 0& & \color{orange}1&\color{lightgreen}0\\
\color {pink} &\color {magenta} 0& & \color{orange}0&\color{lightgreen} 1\\
\color {pink}-a_0&\color {magenta}-a_1& &\color{orange}-a_{n-2}&\color{lightgreen}-a_{n-1}
\end{bmatrix}
$$
- $\color {lightgreen}Fv_n={v_{n-1}}-a_{n-1}v_n$ 
- $\color{orange}Fv_{n-1} ={ v_{n-2}}-a_{n-2}v_n$ 
- $\color {magenta}Fv_2={v_1}-a_1 v_n$ 
- $\color {pink}Fv_1=-a_0 v_n$ 

Rimane da provare che 
$T^{-1}g=g_c\iff g=Tg_c=[v_1|v_2|\dots|v_{n-1}|v_n]\begin{bmatrix}0\\\vdots\\ 1\end{bmatrix}$ 
quindi $g=v_n$ 

# Remarks
## 1
Dalla prova possiamo dedurre che se $(F,G)$ è reachable equivalentemente $rank \mathcal R=n$ possiamo calcolare il polinomio caratteristico $\Delta_F(s)=s^n+a_{n-1}s^{n-1}+\dots+a_0$ e dedurre  immediatamente la **CCF** $(F_c,G_c)$ senza dover calcolare $T$. Per trovare $T$ possiamo fare:
$T=\mathcal R\mathcal R^{-1}_c$ 
## 2
Siccome $F_c=T^{-1}FT$ allora $\Delta_{F_c}(s)\equiv \Delta_F(s)=s^n+a_{n-1}s^{n-1}+\dots+a_0$ 
ma questo ci dice che il polinomio caratteristico della matrice $F_c$ può essere letto dall'ultima riga
## 3
$F$ è [[Cyclic matrix|cyclic]] 
$\iff\exists g\in \mathbb R^n\ s.t.\ (F,g)$ è reachable
$\iff \exists g\in \mathbb R^n$ e $T\in \mathbb R^{n\times n}$ invertibile s.t. $T^{-1}FT=F_c$ e $T^{-1}g=g_c$ 
$\iff \exists T\in \mathbb R^n\times n$ invertibile s.t. $T^{-1}FT=F_c$ (in companion form)

