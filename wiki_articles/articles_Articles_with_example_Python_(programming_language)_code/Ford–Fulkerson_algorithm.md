# Ford–Fulkerson algorithm

## Article Metadata

- **Last Updated:** 2024-12-14T19:37:16.475123+00:00
- **Original Article:** [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)
- **Language:** en
- **Page ID:** 53777

## Summary

The Ford–Fulkerson method or Ford–Fulkerson algorithm (FFA) is a greedy algorithm that computes the maximum flow in a flow network. It is sometimes called a "method" instead of an "algorithm" as the approach to finding augmenting paths in a residual graph is not fully specified or it is specified in several implementations with different running times. It was published in 1956 by L. R. Ford Jr. and D. R. Fulkerson. The name "Ford–Fulkerson" is often also used for the Edmonds–Karp algorithm, whic

## Categories

- Category:All Wikipedia articles written in American English
- Category:Articles with example Python (programming language) code
- Category:Articles with example pseudocode
- Category:Articles with short description
- Category:CS1 maint: multiple names: authors list
- Category:Commons category link from Wikidata
- Category:Graph algorithms
- Category:Network flow problem
- Category:Short description is different from Wikidata
- Category:Use American English from April 2019

## Table of Contents

- Algorithm
- Complexity
- Integer flow example
- Non-terminating example
- Python implementation of the Edmonds–Karp algorithm
- See also
- Notes
- References
- External links

## Content

The Ford–Fulkerson method or Ford–Fulkerson algorithm (FFA) is a greedy algorithm that computes the maximum flow in a flow network. It is sometimes called a "method" instead of an "algorithm" as the approach to finding augmenting paths in a residual graph is not fully specified or it is specified in several implementations with different running times. It was published in 1956 by L. R. Ford Jr. and D. R. Fulkerson. The name "Ford–Fulkerson" is often also used for the Edmonds–Karp algorithm, which is a fully defined implementation of the Ford–Fulkerson method.
The idea behind the algorithm is as follows: as long as there is a path from the source (start node) to the sink (end node), with available capacity on all edges in the path, we send flow along one of the paths. Then we find another path, and so on. A path with available capacity is called an augmenting path.

Algorithm
Let 
  
    
      
        G
        (
        V
        ,
        E
        )
      
    
    {\displaystyle G(V,E)}
  
 be a graph, and for each edge from u to v, let 
  
    
      
        c
        (
        u
        ,
        v
        )
      
    
    {\displaystyle c(u,v)}
  
 be the capacity and 
  
    
      
        f
        (
        u
        ,
        v
        )
      
    
    {\displaystyle f(u,v)}
  
 be the flow. We want to find the maximum flow from the source s to the sink t. After every step in the algorithm the following is maintained:

This means that the flow through the network is a legal flow after each round in the algorithm. We define the residual network 
  
    
      
        
          G
          
            f
          
        
        (
        V
        ,
        
          E
          
            f
          
        
        )
      
    
    {\displaystyle G_{f}(V,E_{f})}
  
 to be the network with capacity 
  
    
      
        
          c
          
            f
          
        
        (
        u
        ,
        v
        )
        =
        c
        (
        u
        ,
        v
        )
        −
        f
        (
        u
        ,
        v
        )
      
    
    {\displaystyle c_{f}(u,v)=c(u,v)-f(u,v)}
  
 and no flow. Notice that it can happen that a flow from v to u is allowed in the residual
network, though disallowed in the original network: if 
  
    
      
        f
        (
        u
        ,
        v
        )
        >
        0
      
    
    {\displaystyle f(u,v)>0}
  
 and 
  
    
      
        c
        (
        v
        ,
        u
        )
        =
        0
      
    
    {\displaystyle c(v,u)=0}
  
 then 
  
    
      
        
          c
          
            f
          
        
        (
        v
        ,
        u
        )
        =
        c
        (
        v
        ,
        u
        )
        −
        f
        (
        v
        ,
        u
        )
        =
        f
        (
        u
        ,
        v
        )
        >
        0
      
    
    {\displaystyle c_{f}(v,u)=c(v,u)-f(v,u)=f(u,v)>0}
  
.

The path in step 2 can be found with, for example, breadth-first search (BFS) or depth-first search in 
  
    
      
        
          G
          
            f
          
        
        (
        V
        ,
        
          E
          
            f
          
        
        )
      
    
    {\displaystyle G_{f}(V,E_{f})}
  
. The former is known as the Edmonds–Karp algorithm.
When no more paths in step 2 can be found, s will not be able to reach t in the residual
network. If S is the set of nodes reachable by s in the residual network, then the total
capacity in the original network of edges from S to the remainder of V is on the one hand
equal to the total flow we found from s to t,
and on the other hand serves as an upper bound for all such flows.
This proves that the flow we found is maximal. See also Max-flow Min-cut theorem.
If the graph 
  
    
      
        G
        (
        V
        ,
        E
        )
      
    
    {\displaystyle G(V,E)}
  
 has multiple sources and sinks, we act as follows:
Suppose that 
  
    
      
        T
        =
        {
        t
        ∣
        t
        
           is a sink
        
        }
      
    
    {\displaystyle T=\{t\mid t{\text{ is a sink}}\}}
  
 and 
  
    
      
        S
        =
        {
        s
        ∣
        s
        
           is a source
        
        }
      
    
    {\displaystyle S=\{s\mid s{\text{ is a source}}\}}
  
. Add a new source 
  
    
      
        
          s
          
            ∗
          
        
      
    
    {\displaystyle s^{*}}
  
 with an edge 
  
    
      
        (
        
          s
          
            ∗
          
        
        ,
        s
        )
      
    
    {\displaystyle (s^{*},s)}
  
 from 
  
    
      
        
          s
          
            ∗
          
        
      
    
    {\displaystyle s^{*}}
  
 to every node 
  
    
      
        s
        ∈
        S
      
    
    {\displaystyle s\in S}
  
, with capacity 
  
    
      
        c
        (
        
          s
          
            ∗
          
        
        ,
        s
        )
        =
        
          d
          
            s
          
        
        =
        
          ∑
          
            (
            s
            ,
            u
            )
            ∈
            E
          
        
        c
        (
        s
        ,
        u
        )
      
    
    {\displaystyle c(s^{*},s)=d_{s}=\sum _{(s,u)\in E}c(s,u)}
  
. And add a new sink 
  
    
      
        
          t
          
            ∗
          
        
      
    
    {\displaystyle t^{*}}
  
 with an edge 
  
    
      
        (
        t
        ,
        
          t
          
            ∗
          
        
        )
      
    
    {\displaystyle (t,t^{*})}
  
 from every node 
  
    
      
        t
        ∈
        T
      
    
    {\displaystyle t\in T}
  
 to 
  
    
      
        
          t
          
            ∗
          
        
      
    
    {\displaystyle t^{*}}
  
, with capacity 
  
    
      
        c
        (
        t
        ,
        
          t
          
            ∗
          
        
        )
        =
        
          d
          
            t
          
        
        =
        
          ∑
          
            (
            v
            ,
            t
            )
            ∈
            E
          
        
        c
        (
        v
        ,
        t
        )
      
    
    {\displaystyle c(t,t^{*})=d_{t}=\sum _{(v,t)\in E}c(v,t)}
  
. Then apply the Ford–Fulkerson algorithm.

Also, if a node u has capacity constraint 
  
    
      
        
          d
          
            u
          
        
      
    
    {\displaystyle d_{u}}
  
, we replace this node with two nodes 
  
    
      
        
          u
          
            
              i
              n
            
          
        
        ,
        
          u
          
            
              o
              u
              t
            
          
        
      
    
    {\displaystyle u_{\mathrm {in} },u_{\mathrm {out} }}
  
, and an edge 
  
    
      
        (
        
          u
          
            
              i
              n
            
          
        
        ,
        
          u
          
            
              o
              u
              t
            
          
        
        )
      
    
    {\displaystyle (u_{\mathrm {in} },u_{\mathrm {out} })}
  
, with capacity 
  
    
      
        c
        (
        
          u
          
            
              i
              n
            
          
        
        ,
        
          u
          
            
              o
              u
              t
            
          
        
        )
        =
        
          d
          
            u
          
        
      
    
    {\displaystyle c(u_{\mathrm {in} },u_{\mathrm {out} })=d_{u}}
  
. Then apply the Ford–Fulkerson algorithm.

Complexity
By adding the flow augmenting path to the flow already established in the graph, the maximum flow will be reached when no more flow augmenting paths can be found in the graph.  However, there is no certainty that this situation will ever be reached, so the best that can be guaranteed is that the answer will be correct if the algorithm terminates.  In the case that the algorithm runs forever, the flow might not even converge towards the maximum flow.  However, this situation only occurs with irrational flow values.  When the capacities are integers, the runtime of Ford–Fulkerson is bounded by 
  
    
      
        O
        (
        E
        f
        )
      
    
    {\displaystyle O(Ef)}
  
 (see big O notation), where 
  
    
      
        E
      
    
    {\displaystyle E}
  
 is the number of edges in the graph and 
  
    
      
        f
      
    
    {\displaystyle f}
  
 is the maximum flow in the graph.  This is because each augmenting path can be found in 
  
    
      
        O
        (
        E
        )
      
    
    {\displaystyle O(E)}
  
 time and increases the flow by an integer amount of at least 
  
    
      
        1
      
    
    {\displaystyle 1}
  
, with the upper bound 
  
    
      
        f
      
    
    {\displaystyle f}
  
.
A variation of the Ford–Fulkerson algorithm with guaranteed termination and a runtime independent of the maximum flow value is the Edmonds–Karp algorithm, which runs in 
  
    
      
        O
        (
        V
        
          E
          
            2
          
        
        )
      
    
    {\displaystyle O(VE^{2})}
  
 time.

Integer flow example
The following example shows the first steps of Ford–Fulkerson in a flow network with 4 nodes, source 
  
    
      
        A
      
    
    {\displaystyle A}
  
 and sink 
  
    
      
        D
      
    
    {\displaystyle D}
  
. This example shows the worst-case behaviour of the algorithm. In each step, only a flow of 
  
    
      
        1
      
    
    {\displaystyle 1}
  
 is sent across the network. If breadth-first-search were used instead, only two steps would be needed.

Non-terminating example
Consider the flow network shown on the right, with source 
  
    
      
        s
      
    
    {\displaystyle s}
  
, sink 
  
    
      
        t
      
    
    {\displaystyle t}
  
, capacities of edges 
  
    
      
        
          e
          
            1
          
        
        =
        1
      
    
    {\displaystyle e_{1}=1}
  
, 
  
    
      
        
          e
          
            2
          
        
        =
        r
        =
        (
        
          
            5
          
        
        −
        1
        )
        
          /
        
        2
      
    
    {\displaystyle e_{2}=r=({\sqrt {5}}-1)/2}
  
 and 
  
    
      
        
          e
          
            3
          
        
        =
        1
      
    
    {\displaystyle e_{3}=1}
  
, and the capacity of all other edges some integer 
  
    
      
        M
        ≥
        2
      
    
    {\displaystyle M\geq 2}
  
. The constant 
  
    
      
        r
      
    
    {\displaystyle r}
  
 was chosen so, that 
  
    
      
        
          r
          
            2
          
        
        =
        1
        −
        r
      
    
    {\displaystyle r^{2}=1-r}
  
. We use augmenting paths according to the following table, where 
  
    
      
        
          p
          
            1
          
        
        =
        {
        s
        ,
        
          v
          
            4
          
        
        ,
        
          v
          
            3
          
        
        ,
        
          v
          
            2
          
        
        ,
        
          v
          
            1
          
        
        ,
        t
        }
      
    
    {\displaystyle p_{1}=\{s,v_{4},v_{3},v_{2},v_{1},t\}}
  
, 
  
    
      
        
          p
          
            2
          
        
        =
        {
        s
        ,
        
          v
          
            2
          
        
        ,
        
          v
          
            3
          
        
        ,
        
          v
          
            4
          
        
        ,
        t
        }
      
    
    {\displaystyle p_{2}=\{s,v_{2},v_{3},v_{4},t\}}
  
 and 
  
    
      
        
          p
          
            3
          
        
        =
        {
        s
        ,
        
          v
          
            1
          
        
        ,
        
          v
          
            2
          
        
        ,
        
          v
          
            3
          
        
        ,
        t
        }
      
    
    {\displaystyle p_{3}=\{s,v_{1},v_{2},v_{3},t\}}
  
.

Note that after step 1 as well as after step 5, the residual capacities of edges 
  
    
      
        
          e
          
            1
          
        
      
    
    {\displaystyle e_{1}}
  
, 
  
    
      
        
          e
          
            2
          
        
      
    
    {\displaystyle e_{2}}
  
 and 
  
    
      
        
          e
          
            3
          
        
      
    
    {\displaystyle e_{3}}
  
 are in the form 
  
    
      
        
          r
          
            n
          
        
      
    
    {\displaystyle r^{n}}
  
, 
  
    
      
        
          r
          
            n
            +
            1
          
        
      
    
    {\displaystyle r^{n+1}}
  
 and 
  
    
      
        0
      
    
    {\displaystyle 0}
  
, respectively, for some 
  
    
      
        n
        ∈
        
          N
        
      
    
    {\displaystyle n\in \mathbb {N} }
  
. This means that we can use augmenting paths 
  
    
      
        
          p
          
            1
          
        
      
    
    {\displaystyle p_{1}}
  
, 
  
    
      
        
          p
          
            2
          
        
      
    
    {\displaystyle p_{2}}
  
, 
  
    
      
        
          p
          
            1
          
        
      
    
    {\displaystyle p_{1}}
  
 and 
  
    
      
        
          p
          
            3
          
        
      
    
    {\displaystyle p_{3}}
  
 infinitely many times and residual capacities of these edges will always be in the same form. Total flow in the network after step 5 is 
  
    
      
        1
        +
        2
        (
        
          r
          
            1
          
        
        +
        
          r
          
            2
          
        
        )
      
    
    {\displaystyle 1+2(r^{1}+r^{2})}
  
. If we continue to use augmenting paths as above, the total flow converges to 
  
    
      
        
          1
          +
          2
          
            ∑
            
              i
              =
              1
            
            
              ∞
            
          
          
            r
            
              i
            
          
          =
          3
          +
          2
          r
        
      
    
    {\displaystyle \textstyle 1+2\sum _{i=1}^{\infty }r^{i}=3+2r}
  
.  However, note that there is a flow of value 
  
    
      
        2
        M
        +
        1
      
    
    {\displaystyle 2M+1}
  
, by sending 
  
    
      
        M
      
    
    {\displaystyle M}
  
 units of flow along 
  
    
      
        s
        
          v
          
            1
          
        
        t
      
    
    {\displaystyle sv_{1}t}
  
, 1 unit of flow along 
  
    
      
        s
        
          v
          
            2
          
        
        
          v
          
            3
          
        
        t
      
    
    {\displaystyle sv_{2}v_{3}t}
  
, and 
  
    
      
        M
      
    
    {\displaystyle M}
  
 units of flow along 
  
    
      
        s
        
          v
          
            4
          
        
        t
      
    
    {\displaystyle sv_{4}t}
  
. Therefore, the algorithm never terminates and the flow does not even converge to the maximum flow.
Another non-terminating example based on the Euclidean algorithm is given by Backman & Huynh (2018), where they also show that the worst case running-time of the Ford-Fulkerson algorithm on a network 
  
    
      
        G
        (
        V
        ,
        E
        )
      
    
    {\displaystyle G(V,E)}
  
 in ordinal numbers is 
  
    
      
        
          ω
          
            Θ
            (
            
              |
            
            E
            
              |
            
            )
          
        
      
    
    {\displaystyle \omega ^{\Theta (|E|)}}
  
.

Python implementation of the Edmonds–Karp algorithm
See also
Berge's theorem
Approximate max-flow min-cut theorem
Turn restriction routing
Dinic's algorithm

Notes
References
Cormen, Thomas H.; Leiserson, Charles E.; Rivest, Ronald L.; Stein, Clifford (2001). "Section 26.2: The Ford–Fulkerson method". Introduction to Algorithms (Second ed.). MIT Press and McGraw–Hill. pp. 651–664. ISBN 0-262-03293-7.
George T. Heineman; Gary Pollice; Stanley Selkow (2008). "Chapter 8:Network Flow Algorithms". Algorithms in a Nutshell. Oreilly Media. pp. 226–250. ISBN 978-0-596-51624-6.
Jon Kleinberg; Éva Tardos (2006). "Chapter 7:Extensions to the Maximum-Flow Problem". Algorithm Design. Pearson Education. pp. 378–384. ISBN 0-321-29535-8.
Samuel Gutekunst (2019). ENGRI 1101. Cornell University.
Backman, Spencer; Huynh, Tony (2018). "Transfinite Ford–Fulkerson on a finite network". Computability. 7 (4): 341–347. arXiv:1504.04363. doi:10.3233/COM-180082. S2CID 15497138.

External links
A tutorial explaining the Ford–Fulkerson method to solve the max-flow problem
Another Java animation
Java Web Start application
 Media related to Ford-Fulkerson's algorithm at Wikimedia Commons

## Related Articles

### Internal Links

- [Approximate max-flow min-cut theorem](https://en.wikipedia.org/wiki/Approximate_max-flow_min-cut_theorem)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Assignment (computer science)](https://en.wikipedia.org/wiki/Assignment_(computer_science))
- [Flow network](https://en.wikipedia.org/wiki/Flow_network)
- [Berge's theorem](https://en.wikipedia.org/wiki/Berge%27s_theorem)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Canadian Journal of Mathematics](https://en.wikipedia.org/wiki/Canadian_Journal_of_Mathematics)
- [Charles E. Leiserson](https://en.wikipedia.org/wiki/Charles_E._Leiserson)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Clifford Stein](https://en.wikipedia.org/wiki/Clifford_Stein)
- [D. R. Fulkerson](https://en.wikipedia.org/wiki/D._R._Fulkerson)
- [Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search)
- [Dinic's algorithm](https://en.wikipedia.org/wiki/Dinic%27s_algorithm)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Edmonds–Karp algorithm](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm)
- [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Flow network](https://en.wikipedia.org/wiki/Flow_network)
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Introduction to Algorithms](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)
- [Jon Kleinberg](https://en.wikipedia.org/wiki/Jon_Kleinberg)
- [L. R. Ford Jr.](https://en.wikipedia.org/wiki/L._R._Ford_Jr.)
- [Max-flow min-cut theorem](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem)
- [Maximum flow problem](https://en.wikipedia.org/wiki/Maximum_flow_problem)
- [Ordinal number](https://en.wikipedia.org/wiki/Ordinal_number)
- [O'Reilly Media](https://en.wikipedia.org/wiki/O%27Reilly_Media)
- [Ron Rivest](https://en.wikipedia.org/wiki/Ron_Rivest)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Theoretical Computer Science (journal)](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_(journal))
- [Thomas H. Cormen](https://en.wikipedia.org/wiki/Thomas_H._Cormen)
- [Turn restriction routing](https://en.wikipedia.org/wiki/Turn_restriction_routing)
- [Uri Zwick](https://en.wikipedia.org/wiki/Uri_Zwick)
- [Éva Tardos](https://en.wikipedia.org/wiki/%C3%89va_Tardos)
- [Template:Cite book](https://en.wikipedia.org/wiki/Template:Cite_book)
- [Category:CS1 maint: multiple names: authors list](https://en.wikipedia.org/wiki/Category:CS1_maint:_multiple_names:_authors_list)
- [Category:Use American English from April 2019](https://en.wikipedia.org/wiki/Category:Use_American_English_from_April_2019)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:37:16.475123+00:00_