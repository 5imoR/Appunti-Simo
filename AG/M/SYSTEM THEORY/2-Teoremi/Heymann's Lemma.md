---
tags:
---
#ST-L18-3
## Theorem
Consideriamo un paio $(F,G)$ raggiungibile con $F\in\mathbb R^{n\times n}$ e $G=[g_1|g_2|\dots|g_m]\in\mathbb R^{n\times m}$ 
Allora $\forall i\in \set{1\dots m}$ tali che $g_i\ne \underline 0$  $\exists$ una state feedback matrix $M_i\in\mathbb R^{m\times n}$ s.t.
$$(F+GM_i,g_i)\text{ è raggiungibile con rispetto a $g_i$}$$

## Corollary

## Proof
Siccome $(F,G)$ è reachable la sua reachability matrix è:
$$\mathcal R=[g_1|g_2|\dots|g_m||Fg_1|Fg_2|\dots|Fg_m||\dots||F^{n-1}g_1|F^{n-1}g_2|\dots|F^{n-1}g_m]$$
ha rango $n$ e quindi ha $n$ colonne linearmente indipendenti. Scegliamo queste $n$ colonne seguendo questo criterio:
- $g_1, Fg_1,\dots,F^{\nu_1-1}g_1$  dove $\nu_1=\min\set{k:F^kg_1\text{è linearmente dipendente di }g_1, Fg_1,\dots,F^{k-1}g_1}$   
- $g_2, Fg_2,\dots,F^{\nu_2-1}g_2$  dove $\nu_2=\min\set{k:F^kg_1\text{è linearmente dipendente di }g_1, Fg_1,\dots,F^{\nu_1-1}g_1\qquad g_2, Fg_2,\dots,F^{k-1}g_2}$   
- $g_r, Fg_r,\dots,F^{\nu_r-1}g_r$  Continuo finche non ottengo $n$ vettori linearmente indipendenti

Mettiamo:
$Q\triangleq[g_1|Fg_1|\dots|F^{\nu_1-1}g_1||g_2|Fg_2|\dots|F^{\nu_2-2}g_2||g_4|\dots||\dots||g_r|Fg_r|\dots|F^{\nu_r-1}g_r]$ 
$S\triangleq[0|0|\dots|e_2||0|0|\dots|e_4||0|\dots||\dots||0|0|\dots|0]$ 
E diciamo che $M_1\triangleq SQ^{-1}$ quindi $M_1Q=S$
$$
\begin{align}
&{\color{orange}M_1}[g_1|{\color{orange}Fg_1}|\dots|F^{\nu_1-1}g_1||g_2|Fg_2|\dots|F^{\nu_2-2}g_2||g_4|\dots||\dots||g_r|Fg_r|\dots|F^{\nu_r-1}g_r]\\
&=[{\color{orange}0}|0|\dots|e_2||0|0|\dots|e_4||0|\dots||\dots||0|0|\dots|0]
\end{align}
$$
Ora dimostriamo che  le colonne della reachability matrix sono linearmente indipendenti
$g_1\ne 0$ 
$(F+GM_1)g_1=F{g_1}+G\cancel{\color{orange}M_1g_1}=Fg_1$ linearmente indipendente da  $g_1$ 
$(F+GM_1)^2g_1=(F+GM_1)[(F+GM_1)g_1]=(F+GM_1)Fg_1=F^2g_1$ L.I. da  $g_1, Fg_1$ 
$\quad\vdots$
$(F+GM_1)^{\nu_1-1}g_1=F^{\nu_1-1}g_1$        L.I. dai vettori precedenti
$(F+GM_1)^{\nu_1}g_1=(F+GM_1)[(F+GM_1)^{\nu_1-1}g_1]=(F+GM_1)F^{\nu_1-1}g_1$ 
$\phantom{(F+GM_1)^{\nu}g_1}=F^{\nu_1}g_1+G\underbrace{M_1F^{\nu_1-1}g_1}_{e_2}=F^{\nu_1}g_1+g_2$   L.I. dai vettori precedenti

