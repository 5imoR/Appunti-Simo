---
tags:
---
#ST-L22-2
## Theorem
Diciamo che un paio $(F_c,G_c)$  con $F\in \mathbb R^{n\times n}, G\in\mathbb R^{n\times m}$   è detto in Multivariable Controllable Canonical Form se $\exists$ una permutation matrix $P\in \mathbb R^{m\times m}$ s.t.:
$$
F_c=\begin{bmatrix}
{\color {orange}\begin{bmatrix}
0 & 1 \\
 & \ddots & \ddots \\
 &  & 0 & 1 \\
x & x & \dots & x \\
\end{bmatrix}}&
\begin{array}{cccc}
 & & & \\
 & & & \\
 & & & \\
 x\ &\ x&\ x&\ x\\
\end{array}&\begin{array}{cccc}\\\\\\ \dots\\\end{array}&
\begin{array}{cccc}
 & & & \\
 & & & \\
 & & & \\
 x\ &\ x&\ x&\ x\\
\end{array}
\\
\begin{array}{cccc}
 & & & \\
 & & & \\
 & & & \\
 x\ &\ x&\ x&\ x\\
\end{array}
&
{\color {lightgreen}\begin{bmatrix}
0 & 1 \\
 & \ddots & \ddots \\
 &  & 0 & 1 \\
x & x & \dots & x \\
\end{bmatrix}}&
\begin{array}{cccc}\\\\\\ \dots\\\end{array}
&\begin{array}{cccc}
 & & & \\
 & & & \\
 & & & \\
 x\ &\ x&\ x&\ x\\
\end{array}\\&&
\ddots\\
\begin{array}{cccc}
 & & & \\
 & & & \\
 & & & \\
 x\ &\ x&\ x&\ x\\
\end{array}&
\begin{array}{cccc}
 & & & \\
 & & & \\
 & & & \\
 x\ &\ x&\ x&\ x\\
\end{array}&
\begin{array}{cccc}\\\\\\ \dots\\\end{array}&
{\color {pink}\begin{bmatrix}
0 & 1 \\
 & \ddots & \ddots \\
 &  & 0 & 1 \\
x & x & \dots & x \\
\end{bmatrix}}
\end{bmatrix}
$$

- $\textcolor{orange}{■}$ ha dimensione $k_1\times k_1$
- $\textcolor{lightgreen}{■}$  ha dimensione $k_2\times k_2$
- $\textcolor{pink}{■}$  ha dimensione $k_q\times k_q$ 

$$
G_cP =
\begin{bmatrix}
\color {orange}0 & \color {orange}0 & \color {orange}\dots & \color {orange}0 &\dots\\
\color {orange}\vdots & \color {orange}\vdots &  & \color {orange}\vdots \\
\color {orange}0 & \color {orange}0 &  & \color {orange}0 \\
\color {orange}1 & \color {orange}* & \color {orange}\dots & \color {orange}* \\
\color {lightgreen}0 & \color {lightgreen}0 & \color {lightgreen}\dots & \color {lightgreen}0 \\
\color {lightgreen}\vdots & \color {lightgreen}\vdots &  & \color {lightgreen}\vdots \\
\color {lightgreen}0 & \color {lightgreen}0 &  & \color {lightgreen}0 \\
\color {lightgreen}0 & \color {lightgreen}1 & \color {lightgreen}\dots & \color {lightgreen}* \\
\vdots &&& \vdots\\
\color {pink}0 & \color {pink}0 & \color {pink}\dots & \color {pink}0 \\
\color {pink}\vdots & \color {pink}\vdots &  & \color {pink}\vdots \\
\color {pink}0 & \color {pink}0 &  & \color {pink}0 \\
\color {pink}0 & \color {pink}0 & \color {pink}\dots & \color {pink}1 &\dots\\
\end{bmatrix}

$$
- $\textcolor{orange}{■}$ ha dimensione $k_1\times q$
- $\textcolor{lightgreen}{■}$  ha dimensione $k_2\times q$
- $\textcolor{pink}{■}$  ha dimensione $k_q\times q$ 
Ci sono altre $m-q$ colonne che però non sono infuenti

${\color {orange}k_1}\ge {\color {lightgreen}k2}\ge\dots \ge \color {pink}k_q$ 
## Corollary

## Proof