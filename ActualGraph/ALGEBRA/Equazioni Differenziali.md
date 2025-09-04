[[Esponenziale]]
Bisogna trovare la funzione incognita a partire da qualcosa
- caso semplice 
$$
\begin{align}
&y=y(x) funzione\ incognita\\
&\begin{cases}
y'=a\cdot y\\
y(0)=\overline{y}
\end{cases}
\end{align}
$$
questo equivale a $y(x)=e^{ax}\cdot \overline{y}$  

- caso più complesso
$$
y''' + 3y''-2y'-y=0\; ;\; y=y(x)
$$
ci si ricava un sistema di equazioni differenziali
$$
\begin{align}
&y_1 = y\\
&y_2=y_1' =y'\\
&y_3 =y_2'=y''\\
&y_3'=y'''\\\\
&\begin{cases}
y_3'+3y_3-2y_2-y_1=0\\
y_1'=y_2\\
y_2'=y_3
\end{cases}
\end{align}
$$
###### Esempio
$$
\begin{align}
&y_1(x) \quad y_2(x)\quad funzioni\ incognite\\
&\begin{cases}
y_1'=5y_1-6y_2\\
y_2'=2y_1-2y_2
\end{cases}\\
&Y=
\begin{bmatrix}
y_1 \\y_2 \\
\end{bmatrix}
\quad
Y'=
\begin{bmatrix}
y_1' \\y_2' \\
\end{bmatrix}\\
&\begin{bmatrix}
y_1' \\y_2' \\
\end{bmatrix}
=
\begin{bmatrix}
5 & -6 \\
2 & -2 \\
\end{bmatrix}
\begin{bmatrix}
y_1 \\y_2 \\
\end{bmatrix}
\end{align}
$$
che equivale a $Y' =A\cdot Y$ 
La soluzione è: $Y(x)=e^{Ax}\cdot \overline{y}\qquad \overline{y} =costante$ 


- Calcolo $e^{Ax}$ 
$$
\begin{align}
det(A)
&=det
\begin{bmatrix}
5-\lambda & -6 \\
2 & -2-\lambda \\
\end{bmatrix}\\
&=
(5-\lambda)(-2-\lambda)+12\\
&=
\lambda^2-3\lambda+2=0\\\\
&\lambda_1 =2\qquad\lambda_2=1 \qquad (autovalori\ reali\ distinti)\\
\end{align}
$$
- Autovettori:
$$
\begin{align}
\lambda_1 =2\\
&\begin{bmatrix}
5-2 & -6 \\
2 & -2-2 \\
\end{bmatrix}=\begin{bmatrix}
3 & -6 \\
2 & -4 \\
\end{bmatrix}\\
&
\begin{bmatrix}
3 & -6 \\
2 & -4 \\
\end{bmatrix}\cdot
\begin{bmatrix}
x_1  \\
x_2  \\
\end{bmatrix}=
\begin{bmatrix}
0 \\
0  \\
\end{bmatrix}
\end{align}
$$
Al quale corrispondono infinite soluzioni con $x_1 = 2x_2$ 
quindi un autovettore relativo $\lambda_1 =2$  è $v_1=(2,1)$ 
$$
\begin{align}
\lambda_2 =1\\
&\begin{bmatrix}
5-1 & -6 \\
2 & -2-1 \\
\end{bmatrix}=\begin{bmatrix}
4 & -6 \\
2 & -3 \\
\end{bmatrix}\\
&
\begin{bmatrix}
4 & -6 \\
2 & -3 \\
\end{bmatrix}\cdot
\begin{bmatrix}
x_1  \\
x_2  \\
\end{bmatrix}=
\begin{bmatrix}
0 \\
0  \\
\end{bmatrix}
\end{align}
$$
Al quale corrispondono infinite soluzioni con $x_1 = \frac{3}{2}x_2$ 
quindi un autovettore relativo $\lambda_2 =2$  è $v_2=(3,2)$ 

Quindi si ha:
$$
D=
\begin{bmatrix}
2 & 0 \\
0 & 1 \\
\end{bmatrix}\; ;\;
S=
\begin{bmatrix}
2 & 3 \\
1 & 2 \\
\end{bmatrix}\; ;\;
S^{-1}=
\begin{bmatrix}
2 & -3 \\
-1 & 2 \\
\end{bmatrix}
$$

Infine $e^{Ax}$ vale:
$$
\begin{align}
e^{Ax} &= Se^{Dx}S^{-1}=\\
&=S\cdot e^{
\begin{bmatrix}
2x & 0 \\
0 & x \\
\end{bmatrix}
}
\cdot
S^{-1}=\\
&=S\cdot
\begin{bmatrix}
e^{2x} & 0 \\
0 & e^x \\
\end{bmatrix}
\cdot S^{-1}=\\
&=
\begin{bmatrix}
4e^{2x}-3e^x & -6e^{2x}+ 6e^x \\
2e^{2x}-2e^x & -3e^{2x}+4e^x \\
\end{bmatrix}
\end{align}
$$
La soluzione è:
$$
\begin{bmatrix}
y_1(x)  \\
y_2(x)  \\
\end{bmatrix}
=e^{Ax}\cdot
\begin{bmatrix}
\overline y_1  \\
\overline y_2  \\
\end{bmatrix} = 
\begin{bmatrix}
(4e^{2x}-3e^x)\overline y_1 & (-6e^{2x}+ 6e^x)\overline y_2 \\
(2e^{2x}-2e^x)\overline y_1 & (-3e^{2x}+4e^x)\overline y_2 \\
\end{bmatrix}
$$