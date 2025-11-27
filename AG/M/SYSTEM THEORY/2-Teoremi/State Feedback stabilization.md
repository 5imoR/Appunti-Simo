---
tags:
---
#ST-L23-4
## Theorem \[State Feedback stabilization]
Dato un paio  $(F,G)$  con $F\in\mathbb R^{n\times n}$ e $G\in\mathbb R^{n\times m}$  i seguenti fatti sono equivalenti:
1. $(F,G)$ è stabilizzabile
2. sia che $(F,G)$ sia reachable o meno $F_{22}$  è asintoticamente stabile
3. se il $rank[\lambda In-F|G]<n$ allora:  $\begin{array}{c}CT&Re(\lambda)<0\\DT&|\lambda|<1\end{array}$ 
 
## Corollary

## Proof
$(1)\iff(2)$  segue dall'analisi del [[CEAP Complete Eigenvalue Allocation Problem]] 
$(2)\iff(3)$ segue dal [[PHB Reachability Test]] 