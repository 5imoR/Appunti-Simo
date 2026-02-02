#ML-L13-3 

%%## Binary Classification%%
![[classification]]
Nel caso di Binary classification si parla di trovare  l'iperpiano che va a separare le $x$ dagli $o$
- $x\in\mathbb R^2$
- $x_i\in\mathbb R^d$ 
- $[x_i]_j\quad j\in[1\dots d]$ 

### Classification Rule
$$h_{w,b}=sign\set{w^Tx+b}$$
$$\qquad \qquad=\begin{cases}
+1\quad w^Tx+b>0\\
-1\quad w^Tx+b<0
\end{cases}$$
### Geometry of linear classification
![[geometryoflinclass]]
- $x\in \mathbb R^d\qquad \color{orange} x_\perp+x_\parallel=x$ 
- $w\in \mathbb R^d$ 
essendo $x_\perp$ costante anche $w^Tx_\perp+b$ lo sarà

possiamo scrivere:
$$w^Tx+b=w^T(x_\perp+x_\parallel)+b=0$$
allora:
$$w^Tx_\perp+b=-w^Tx_\parallel= 0$$
$w^Tx_\parallel$ da sempre $0$ perchè sono 2 vettori ortogonali tra loro

$w^Tx_\perp=-b$ 
$<w,x_\perp>=\pm ||w||\cdot||x_\perp||\cdot \cos 0$ 
$\displaystyle||x_\perp||=\pm \frac b {||w||}$ 

![[perppartild]]
$$w^Tx+b=w^T(x_\perp+x_\parallel+\tilde x)+b=0$$
$$
\cancel{w^T(x_\perp+x_\parallel)+b}_{=0}+w^T\tilde x=<w,\tilde x>=\pm ||w||\cdot||\tilde x||
$$
$$\displaystyle\Rightarrow ||\tilde x||=d(x,line)=\pm \frac{w^Tx+b}{||w||}$$ 
#### Remark
![[Linear Classification#Classification Rule]] 
Quindi se 
- $y_i\hat y_i> 0$ è classificato correttamente
- $y_i\hat y_i< 0$ è classificato incorrettamente