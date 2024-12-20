---
title: Weisfeiler Leman graph isomorphism test
url: https://en.wikipedia.org/wiki/Weisfeiler_Leman_graph_isomorphism_test
language: en
categories: ["Category:All articles covered by WikiProject Wikify", "Category:All articles needing additional references", "Category:All articles needing references cleanup", "Category:All articles that are excessively detailed", "Category:All articles with style issues", "Category:Articles covered by WikiProject Wikify from December 2023", "Category:Articles needing additional references from December 2023", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Graph theory", "Category:Short description is different from Wikidata", "Category:Wikipedia articles that are excessively detailed from December 2023", "Category:Wikipedia articles with style issues from December 2023", "Category:Wikipedia references cleanup from December 2023"]
references: 0
last_modified: 2024-12-19T15:06:46Z
---

# Weisfeiler Leman graph isomorphism test

## Summary

In graph theory, the Weisfeiler Leman graph isomorphism test is a heuristic test for the existence of an isomorphism between two graphs G and H. It is a generalization of the color refinement algorithm and has been first described by Weisfeiler and Leman in 1968. The original formulation is based on graph canonization, a normal form for graphs, while there is also a combinatorial interpretation in the spirit of color refinement and a connection to logic.
There are several versions of the test  (

## Full Content

In graph theory, the Weisfeiler Leman graph isomorphism test is a heuristic test for the existence of an isomorphism between two graphs G and H. It is a generalization of the color refinement algorithm and has been first described by Weisfeiler and Leman in 1968. The original formulation is based on graph canonization, a normal form for graphs, while there is also a combinatorial interpretation in the spirit of color refinement and a connection to logic.
There are several versions of the test  (e.g. k-WL and k-FWL) referred to in the literature by various names, which easily leads to confusion. Additionally, Andrey Leman is spelled `Lehman' in several older articles.

Weisfeiler-Leman-based Graph Isomorphism heuristics
All variants of color refinement are one-sided heuristics that take as input two graphs G and H and  output a certificate that they are different or 'I don't know'. This means that if the heuristic is able to tell G and H apart, then they are definitely different, but the other direction does not hold: for every variant of the WL-test (see below) there are non-isomorphic graphs where the difference is not detected. Those graphs are highly symmetric graphs such as regular graphs for 1-WL/color refinement.

1-dimensional Weisfeiler-Leman (1-WL)
The 1-dimensional graph isomorphism test is essentially the same as the color refinement algorithm (the difference has to do with non-edges and is irrelevant for all practical purposes as it is trivial to see that graphs with a different number of nodes are non-isomorphic). The algorithm proceeds as follows:
Initialization All nodes are initialized with the same color 0
Refinement Two nodes u,v get a different color if a) they had a different color before or b) there is a color c such that u and v have a different number of c-colored neighbors
Termination The algorithm ends if the partition induced by two successive refinement steps is the same.
In order to use this algorithm as a graph isomorphism test, one runs the algorithm on two input graphs G and H in parallel, i.e. using the colors when splitting such that some color c (after one iteration) might mean `a node with exactly 5 neighbors of color 0'. In practice this is achieved by running color refinement on the disjoint union graph of G and H. One can then look at the histogram of colors of both graphs (counting the number of nodes after color refinement stabilized) and if they differ, this is a certificate that both graphs are not isomorphic.
The algorithm terminates after at most 
  
    
      
        n
        −
        1
      
    
    {\displaystyle n-1}
  
 rounds where 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is the number of nodes of the input graph as it has to split one partition in every refinement step and this can happen at most until every node has its own color. Note that there are graphs for which one needs this number of iterations, although in practice the number of rounds until terminating tends to be very low (<10).
The refinement of the partition in each step is by processing for each node its label and the labels of its nearest neighbors. Therefore WLtest can be viewed as a message passing algorithm which also connects it to graph neural networks.

Higher-order Weisfeiler-Leman
This is the place where the aforementioned two variants of the WL algorithm appear. Both the k-dimensional Weisfeiler-Leman (k-WL) and the k-dimensional folklore Weisfeiler-Leman algorithm (k-FWL) are extensions of 1-WL from above operating on k-tuples instead of individual nodes. While their difference looks innocent on the first glance, it can be shown that k-WL and (k-1)-FWL (for k>2) distinguish the same pairs of graphs.

k-WL (k>1)
Input: a graph G = (V,E)
# initialize

  
    
      
        
          c
          
            0
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        =
        
          Hash
        
        (
        
          type
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        )
      
    
    {\displaystyle c^{0}({\bar {v}})={\text{Hash}}({\text{type}}({\bar {v}}))}
  
 for all 
  
    
      
        
          
            
              v
              ¯
            
          
        
        ∈
        
          V
          
            k
          
        
      
    
    {\displaystyle {\bar {v}}\in V^{k}}
  

repeat
   
  
    
      
        
          c
          
            i
          
          
            ℓ
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        =
        {
        
        {
        
          c
          
            ℓ
            −
            1
          
        
        (
        
          
            
              w
              ¯
            
          
        
        )
        :
        
          
            
              w
              ¯
            
          
        
        ∈
        
          
            
              N
            
          
          
            i
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        }
        
        }
      
    
    {\displaystyle c_{i}^{\ell }({\bar {v}})=\{\!\{c^{\ell -1}({\bar {w}}):{\bar {w}}\in {\mathcal {N}}_{i}({\bar {v}})\}\!\}}
  
 for all 
  
    
      
        
          
            
              v
              ¯
            
          
        
        ∈
        
          V
          
            k
          
        
        ,
        i
        ∈
        [
        k
        ]
      
    
    {\displaystyle {\bar {v}}\in V^{k},i\in [k]}
  

   
  
    
      
        
          c
          
            ℓ
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        =
        
          Hash
        
        (
        
          c
          
            ℓ
            −
            1
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        ,
        
          c
          
            1
          
          
            ℓ
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        ,
        …
        ,
        
          c
          
            k
          
          
            ℓ
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        )
      
    
    {\displaystyle c^{\ell }({\bar {v}})={\text{Hash}}(c^{\ell -1}({\bar {v}}),c_{1}^{\ell }({\bar {v}}),\dots ,c_{k}^{\ell }({\bar {v}}))}
  

until 
  
    
      
        
          c
          
            ℓ
          
        
        ≡
        
          c
          
            ℓ
            −
            1
          
        
      
    
    {\displaystyle c^{\ell }\equiv c^{\ell -1}}
  
 (both colorings induce identical partitions of 
  
    
      
        
          V
          
            k
          
        
      
    
    {\displaystyle V^{k}}
  
)
return 
  
    
      
        
          c
          
            ℓ
          
        
      
    
    {\displaystyle c^{\ell }}
  

Here the neighborhood 
  
    
      
        
          
            
              N
            
          
          
            i
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
      
    
    {\displaystyle {\mathcal {N}}_{i}({\bar {v}})}
  
 of a k-tuple 
  
    
      
        
          
            
              v
              ¯
            
          
        
      
    
    {\displaystyle {\bar {v}}}
  
 is given by the set of all k-tuples reachable by exchanging the i-th position of 
  
    
      
        
          
            
              v
              ¯
            
          
        
      
    
    {\displaystyle {\bar {v}}}
  
:

  
    
      
        
          
            
              N
            
          
          
            i
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        =
        {
        (
        
          v
          
            1
          
        
        ,
        …
        ,
        
          v
          
            i
            −
            1
          
        
        ,
        w
        ,
        
          v
          
            i
            +
            1
          
        
        ,
        …
        ,
        
          v
          
            k
          
        
        )
        :
        w
        ∈
        V
        }
      
    
    {\displaystyle {\mathcal {N}}_{i}({\bar {v}})=\{(v_{1},\dots ,v_{i-1},w,v_{i+1},\dots ,v_{k}):w\in V\}}
  

The atomic type 
  
    
      
        
          type
        
        (
        
          
            
              v
              ¯
            
          
        
        )
      
    
    {\displaystyle {\text{type}}({\bar {v}})}
  
of a tuple encodes the edge information between all pairs of nodes from 
  
    
      
        
          
            
              v
              ¯
            
          
        
      
    
    {\displaystyle {\bar {v}}}
  
. For example, a 2-tuple has only two possible atomic types, namely the two nodes may share an edge, or they do not. Note that if the graph has multiple (different) edge relations or additional node features, membership in those is also represented in 
  
    
      
        
          type
        
        (
        
          
            
              v
              ¯
            
          
        
        )
      
    
    {\displaystyle {\text{type}}({\bar {v}})}
  
.
The key idea of k-WL is to expand the neighborhood notion to k-tuples and then effectively run color refinement on the resulting graph.

k-FWL (k>1)
Input: a graph G = (V,E)
# initialize

  
    
      
        
          c
          
            0
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        =
        
          Hash
        
        (
        
          type
        
        (
        
          
            
              v
              ¯
            
          
        
        )
      
    
    {\displaystyle c^{0}({\bar {v}})={\text{Hash}}({\text{type}}({\bar {v}})}
  
) for all 
  
    
      
        
          
            
              v
              ¯
            
          
        
        ∈
        
          V
          
            k
          
        
      
    
    {\displaystyle {\bar {v}}\in V^{k}}
  

repeat
  
  
    
      
        
          c
          
            w
          
          
            ℓ
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        =
        
          
            (
          
        
        
          c
          
            ℓ
            −
            1
          
        
        (
        
          
            
              v
              ¯
            
          
        
        [
        1
        ]
        
        
        ←
        
        w
        )
        ,
        …
        ,
        
          c
          
            ℓ
            −
            1
          
        
        (
        
          
            
              v
              ¯
            
          
        
        [
        k
        ]
        
        
        ←
        
        w
        )
        
          
            )
          
        
      
    
    {\displaystyle c_{w}^{\ell }({\bar {v}})={\big (}c^{\ell -1}({\bar {v}}[1]\!\!\leftarrow \!w),\dots ,c^{\ell -1}({\bar {v}}[k]\!\!\leftarrow \!w){\big )}}
  
 for all 
  
    
      
        
          
            
              v
              ¯
            
          
        
        ∈
        
          V
          
            k
          
        
        ,
        w
        ∈
        V
      
    
    {\displaystyle {\bar {v}}\in V^{k},w\in V}
  

  
  
    
      
        
          c
          
            ℓ
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        =
        
          Hash
        
        
          
            (
          
        
        
          c
          
            ℓ
            −
            1
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        ,
        {
        
        {
        
          c
          
            w
          
          
            ℓ
          
        
        (
        
          
            
              v
              ¯
            
          
        
        )
        :
        w
        ∈
        V
        }
        
        }
        
          
            )
          
        
      
    
    {\displaystyle c^{\ell }({\bar {v}})={\text{Hash}}{\big (}c^{\ell -1}({\bar {v}}),\{\!\{c_{w}^{\ell }({\bar {v}}):w\in V\}\!\}{\big )}}
  

until 
  
    
      
        
          c
          
            ℓ
          
        
        ≡
        
          c
          
            ℓ
            −
            1
          
        
      
    
    {\displaystyle c^{\ell }\equiv c^{\ell -1}}
  
 (both colorings induce identical partitions of 
  
    
      
        
          V
          
            k
          
        
      
    
    {\displaystyle V^{k}}
  
)
return 
  
    
      
        
          c
          
            ℓ
          
        
      
    
    {\displaystyle c^{\ell }}
  

Here 
  
    
      
        
          
            
              v
              ¯
            
          
        
        [
        i
        ]
        
        
        ←
        
        w
      
    
    {\displaystyle {\bar {v}}[i]\!\!\leftarrow \!w}
  
 is the tuple 
  
    
      
        
          
            
              v
              ¯
            
          
        
      
    
    {\displaystyle {\bar {v}}}
  
 where the i-th position is exchanged to be 
  
    
      
        w
      
    
    {\displaystyle w}
  
.
Note that there is one major difference between k-WL and k-FWL: k-FWL checks what happens if a single node w is placed at any position of the k-tuple (and then computes the multiset of these k-tuples) while k-WL looks at the multisets that you get when changing the i-th component only of the original k-tuple. It then uses all those multisets in the hash that computes the new color.
It can be shown (although only through the connection to logic) that k-FWL and (k+1)-WL are equivalent (for 
  
    
      
        k
        ≥
        2
      
    
    {\displaystyle k\geq 2}
  
). Since both algorithms scale exponentially in k (both iterate over all k-tuples), the use of k-FWL is much more efficient than using the equivalent (k+1)-WL.

Examples and Code for 1-WL
Code
Here is some actual Python code which includes the description of the first examples.

Examples
The first three examples are for graphs of order 5.

WLpair takes 3 rounds on 'G0' and 'G1'. The test succeeds as the certificates agree. 
WLpair takes 4 rounds on 'G0' and 'G2'. The test fails as the certificates disagree. Indeed 'G0' has a cycle of length 5, while 'G2' doesn't, thus 'G0' and 'G2' cannot be isomorphic.
WLpair takes 4 rounds on 'G1' and 'G2'. The test fails as the certificates disagree. From the previous two instances we already know 
  
    
      
        
          G
          
            1
          
        
        ≅
        
          G
          
            0
          
        
        ≇
        
          G
          
            2
          
        
      
    
    {\displaystyle G_{1}\cong G_{0}\not \cong G_{2}}
  
.

Indeed G0 and G1 are isomorphic. Any isomorphism must respect the components and therefore the labels. This can be used for kernelization of the graph isomorphism problem. Note that not every map of vertices that respects the labels gives an isomorphism. Let 
  
    
      
        φ
        :
        
          G
          
            0
          
        
        →
        
          G
          
            1
          
        
      
    
    {\displaystyle \varphi :G_{0}\rightarrow G_{1}}
  
 and 
  
    
      
        ψ
        :
        
          G
          
            0
          
        
        →
        
          G
          
            1
          
        
      
    
    {\displaystyle \psi :G_{0}\rightarrow G_{1}}
  
 be maps given by 
  
    
      
        φ
        (
        a
        )
        =
        D
        ,
        φ
        (
        b
        )
        =
        C
        ,
        φ
        (
        c
        )
        =
        B
        ,
        φ
        (
        d
        )
        =
        E
        ,
        φ
        (
        e
        )
        =
        A
      
    
    {\displaystyle \varphi (a)=D,\varphi (b)=C,\varphi (c)=B,\varphi (d)=E,\varphi (e)=A}
  
 resp. 
  
    
      
        ψ
        (
        a
        )
        =
        B
        ,
        ψ
        (
        b
        )
        =
        C
        ,
        ψ
        (
        c
        )
        =
        D
        ,
        ψ
        (
        d
        )
        =
        E
        ,
        ψ
        (
        e
        )
        =
        A
      
    
    {\displaystyle \psi (a)=B,\psi (b)=C,\psi (c)=D,\psi (d)=E,\psi (e)=A}
  
. While 
  
    
      
        φ
      
    
    {\displaystyle \varphi }
  
 is not an isomorphism 
  
    
      
        ψ
      
    
    {\displaystyle \psi }
  
 constitutes an isomorphism.
When applying WLpair to G0 and G2 we get for G0 the certificate 7_7_8_9_9. But the isomorphic G1 gets the certificate 7_7_8_8_9 when applying WLpair to G1 and G2. This illustrates the phenomenon about labels depending on the execution order of the WLtest on the nodes. Either one finds another relabeling method that keeps uniqueness of labels, which becomes rather technical, or one skips the relabeling altogether and keeps the label strings, which blows up the length of the certificate significantly, or one applies WLtest to the union of the two tested graphs, as we did in the variant WLpair. Note that although G1 and G2 can get distinct certificates when WLtest is executed on them separately, they do get the same certificate by WLpair.
The next example is about regular graphs. WLtest cannot distinguish regular graphs of equal order,: 31  but WLpair can distinguish regular graphs of distinct degree even if they have the same order. In fact WLtest terminates after a single round as seen in these examples of order 8, which are all 3-regular except the last one which is 5-regular.
All four graphs are pairwise non-isomorphic. G8_00 has two connected components, while the others do not. G8_03 is 5-regular, while the others are 3-regular. G8_01 has no 3-cycle while G8_02 does have 3-cycles.

Another example of two non-isomorphic graphs that WLpair cannot distinguish is given here.

Applications
The theory behind the Weisfeiler Leman test is applied in graph neural networks.

Weisfeiler Leman graph kernels
In machine learning of nonlinear data one uses kernels to represent the data in a high dimensional feature space after which linear techniques such as support vector machines can be applied. Data represented as graphs often behave nonlinear. Graph kernels are method to preprocess such graph based nonlinear data to simplify subsequent learning methods. Such graph kernels can be constructed by partially executing a Weisfeiler Leman test and processing the partition that has been constructed up to that point. These Weisfeiler Leman graph kernels have attracted considerable research in the decade after their publication. They are also implemented in dedicated libraries for graph kernels such as GraKeL.
Note that kernels for artificial neural network in the context of machine learning such as graph kernels are not to be confused  with kernels applied in heuristic algorithms to reduce the computational cost for solving problems of high complexity such as instances of NP-hard problems in the field of complexity theory. As stated above the Weisfeiler Leman test can also be applied in the later context.

See also
Graph isomorphism
Graph neural network


== References ==
