# Push–relabel maximum flow algorithm

## Article Metadata

- **Last Updated:** 2024-12-15T04:42:31.766460+00:00
- **Original Article:** [Push–relabel maximum flow algorithm](https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm)
- **Language:** en
- **Page ID:** 3444072

## Summary

In mathematical optimization, the push–relabel algorithm (alternatively, preflow–push algorithm) is an algorithm for computing maximum flows in a flow network. The name "push–relabel" comes from the two basic operations used in the algorithm. Throughout its execution, the algorithm maintains a "preflow" and gradually converts it into a maximum flow by moving flow locally between neighboring nodes using push operations under the guidance of an admissible network maintained by relabel operations. 

## Categories

- Category:All articles with unsourced statements
- Category:Articles with example C code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from December 2024
- Category:Graph algorithms
- Category:Network flow problem
- Category:Short description is different from Wikidata

## Table of Contents

- History
- Concepts
- The generic push–relabel algorithm
- Practical implementations
- Sample implementations

## Content

In mathematical optimization, the push–relabel algorithm (alternatively, preflow–push algorithm) is an algorithm for computing maximum flows in a flow network. The name "push–relabel" comes from the two basic operations used in the algorithm. Throughout its execution, the algorithm maintains a "preflow" and gradually converts it into a maximum flow by moving flow locally between neighboring nodes using push operations under the guidance of an admissible network maintained by relabel operations. In comparison, the Ford–Fulkerson algorithm performs global augmentations that send flow following paths from the source all the way to the sink.
The push–relabel algorithm is considered one of the most efficient maximum flow algorithms. The generic algorithm has a strongly polynomial O(V 2E) time complexity, which is asymptotically more efficient than the O(VE 2) Edmonds–Karp algorithm. Specific variants of the algorithms achieve even lower time complexities. The variant based on the highest label node selection rule has O(V 2√E) time complexity and is generally regarded as the benchmark for maximum flow algorithms. Subcubic O(VElog(V 2/E)) time complexity can be achieved using dynamic trees, although in practice it is less efficient.
The push–relabel algorithm has been extended to compute minimum cost flows. The idea of distance labels has led to a more efficient augmenting path algorithm, which in turn can be incorporated back into the push–relabel algorithm to create a variant with even higher empirical performance.

History
The concept of a preflow was originally designed by Alexander V. Karzanov and was published in 1974 in Soviet Mathematical Dokladi 15. This pre-flow algorithm also used a push operation; however, it used distances in the auxiliary network to determine where to push the flow instead of a labeling system.
The push-relabel algorithm was designed by Andrew V. Goldberg and Robert Tarjan. The algorithm was initially presented in November 1986 in STOC '86: Proceedings of the eighteenth annual ACM symposium on Theory of computing, and then officially in October 1988 as an article in the Journal of the ACM. Both papers detail a generic form of the algorithm terminating in O(V 2E) along with a O(V 3) sequential implementation, a O(VE log(V 2/E)) implementation using dynamic trees, and parallel/distributed implementation. As explained in, Goldberg-Tarjan introduced distance labels by incorporating them into the parallel maximum flow algorithm of Yossi Shiloach and Uzi Vishkin.

Concepts
Definitions and notations
Let:

G = (V, E) be a network with capacity function c: V × V → 
  
    
      
        
          R
        
      
    
    {\displaystyle \mathbb {R} }
  
∞,
F = (G, c, s, t) a flow network, where s ∈ V and t ∈ V are chosen source and sink vertices respectively,
f : V × V → 
  
    
      
        
          R
        
      
    
    {\displaystyle \mathbb {R} }
  
 denote a pre-flow in F,
xf : V → 
  
    
      
        
          R
        
      
    
    {\displaystyle \mathbb {R} }
  
 denote the excess function with respect to the flow f, defined by xf (u) = Σv ∈ V f (v, u) − Σv ∈ V f (u, v),
cf : V × V → 
  
    
      
        
          R
        
      
    
    {\displaystyle \mathbb {R} }
  
∞ denote the residual capacity function with respect to the flow f, defined by cf (e) = c(e) − f (e),
Ef ⊂ E being the edges where f < c,
and

Gf (V, Ef ) denote the residual network of G with respect to the flow f.
The push–relabel algorithm uses a nonnegative integer valid labeling function which makes use of distance labels, or heights, on nodes to determine which arcs should be selected for the push operation. This labeling function is denoted by 𝓁 : V → 
  
    
      
        
          N
        
      
    
    {\displaystyle \mathbb {N} }
  
. This function must satisfy the following conditions in order to be considered valid:

Valid labeling:
𝓁(u) ≤ 𝓁(v) + 1 for all (u, v) ∈ Ef
Source condition:
𝓁(s) = | V |
Sink conservation:
𝓁(t) = 0
In the algorithm, the label values of s and t are fixed. 𝓁(u) is a lower bound of the unweighted distance from u to t in Gf  if t is reachable from u. If u has been disconnected from t, then 𝓁(u) − | V | is a lower bound of the unweighted distance from u to s. As a result, if a valid labeling function exists, there are no s-t paths in Gf  because no such paths can be longer than | V | − 1.
An arc (u, v) ∈ Ef  is called admissible if 𝓁(u) = 𝓁(v) + 1. The admissible network G̃f (V, Ẽf ) is composed of the set of arcs e ∈ Ef   that are admissible. The admissible network is acyclic.
For a fixed flow f, a vertex v ∉ {s, t}  is called active if it has positive excess with respect to f, i.e., xf (u) > 0.

Operations
Initialization
The algorithm starts by creating a residual graph, initializing the preflow values to zero and performing a set of saturating push operations on residual arcs (s, v) exiting the source, where v ∈ V \ {s}. Similarly, the labels are initialized such that the label at the source is the number of nodes in the graph, 𝓁(s) = | V |, and all other nodes are given a label of zero. Once the initialization is complete the algorithm repeatedly performs either the push or relabel operations against active nodes until no applicable operation can be performed.

Push
The push operation applies on an admissible out-arc (u, v) of an active node u in Gf. It moves min{xf (u), cf (u,v)} units of flow from u to v.

push(u, v):
    assert xf[u] > 0 and 𝓁[u] == 𝓁[v] + 1
    Δ = min(xf[u], c[u][v] - f[u][v])
    f[u][v] += Δ
    f[v][u] -= Δ
    xf[u] -= Δ
    xf[v] += Δ

A push operation that causes f (u, v) to reach c(u, v) is called a saturating push since it uses up all the available capacity of the residual arc. Otherwise, all of the excess at the node is pushed across the residual arc. This is called an unsaturating or non-saturating push.

Relabel
The relabel operation applies on an active node u which is neither the source nor the sink without any admissible out-arcs in Gf. It modifies 𝓁(u) to be the minimum value such that an admissible out-arc is created. Note that this always increases 𝓁(u) and never creates a steep arc, which is an arc (u, v) such that cf (u, v) > 0, and 𝓁(u) > 𝓁(v) + 1.

relabel(u):
    assert xf[u] > 0 and 𝓁[u] <= 𝓁[v] for all v such that cf[u][v] > 0
    𝓁[u] = 1 + min(𝓁[v] for all v such that cf[u][v] > 0)

Effects of push and relabel
After a push or relabel operation, 𝓁 remains a valid labeling function with respect to f.
For a push operation on an admissible arc (u, v), it may add an arc (v, u) to Ef, where 𝓁(v) = 𝓁(u) − 1 ≤ 𝓁(u) + 1; it may also remove the arc (u, v) from Ef, where it effectively removes the constraint 𝓁(u) ≤ 𝓁(v) + 1.
To see that a relabel operation on node u preserves the validity of 𝓁(u), notice that this is trivially guaranteed by definition for the out-arcs of u in Gf. For the in-arcs of u in Gf, the increased 𝓁(u) can only satisfy the constraints less tightly, not violate them.

The generic push–relabel algorithm
The generic push–relabel algorithm is used as a proof of concept only and does not contain implementation details on how to select an active node for the push and relabel operations. This generic version of the algorithm will terminate in O(V2E).
Since 𝓁(s) = | V |, 𝓁(t) = 0, and there are no paths longer than | V | − 1 in Gf, in order for 𝓁(s) to satisfy the valid labeling condition s must be disconnected from t. At initialisation, the algorithm fulfills this requirement by creating a pre-flow f that saturates all out-arcs of s, after which 𝓁(v) = 0 is trivially valid for all v ∈ V \ {s, t}. After initialisation, the algorithm repeatedly executes an applicable push or relabel operation until no such operations apply, at which point the pre-flow has been converted into a maximum flow.

generic-push-relabel(G, c, s, t):
    create a pre-flow f that saturates all out-arcs of s
    let 𝓁[s] = |V|
    let 𝓁[v] = 0 for all v ∈ V \ {s}
    while there is an applicable push or relabel operation do
        execute the operation

Correctness
The algorithm maintains the condition that 𝓁 is a valid labeling during its execution. This can be proven true by examining the effects of the push and relabel operations on the label function 𝓁. The relabel operation increases the label value by the associated minimum plus one which will always satisfy the 𝓁(u) ≤ 𝓁(v) + 1 constraint. The push operation can send flow from u to v if 𝓁(u) = 𝓁(v) + 1. This may add (v, u) to Gf  and may delete (u, v) from Gf . The addition of (v, u) to Gf  will not affect the valid labeling since 𝓁(v) = 𝓁(u) − 1.  The deletion of (u, v) from Gf  removes the corresponding constraint since the valid labeling property 𝓁(u) ≤ 𝓁(v) + 1 only applies to residual arcs in Gf .
If a preflow f and a valid labeling 𝓁 for f exists then there is no augmenting path from s to t in the residual graph Gf . This can be proven by contradiction based on inequalities which arise in the labeling function when supposing that an augmenting path does exist. If the algorithm terminates, then all nodes in V \ {s, t} are not active. This means all v ∈ V \ {s, t} have no excess flow, and with no excess the preflow f obeys the flow conservation constraint and can be considered a normal flow. This flow is the maximum flow according to the max-flow min-cut theorem since there is no augmenting path from s to t.
Therefore, the algorithm will return the maximum flow upon termination.

Time complexity
In order to bound the time complexity of the algorithm, we must analyze the number of push and relabel operations which occur within the main loop. The numbers of relabel, saturating push and nonsaturating push operations are analyzed separately.
In the algorithm, the relabel operation can be performed at most (2| V | − 1)(| V | − 2) < 2| V |2 times. This is because the labeling 𝓁(u) value for any node u can never decrease, and the maximum label value is at most 2| V | − 1 for all nodes. This means the relabel operation could potentially be performed 2| V | − 1  times for all nodes V \ {s, t} (i.e.  | V | − 2). This results in a bound of O(V 2) for the relabel operation.
Each saturating push on an admissible arc (u, v) removes the arc from Gf . For the arc to be reinserted into Gf  for another saturating push, v must first be relabeled, followed by a push on the arc (v, u), then u must be relabeled. In the process, 𝓁(u) increases by at least two. Therefore, there are O(V) saturating pushes on (u, v), and the total number of saturating pushes is at most 2| V || E |. This results in a time bound of O(VE) for the saturating push operations.
Bounding the number of nonsaturating pushes can be achieved via a potential argument. We use the potential function Φ = Σ[u ∈ V ∧ xf (u) > 0] 𝓁(u) (i.e. Φ is the sum of the labels of all active nodes). It is obvious that Φ is 0 initially and stays nonnegative throughout the execution of the algorithm. Both relabels and saturating pushes can increase Φ. However, the value of Φ must be equal to 0 at termination since there cannot be any remaining active nodes at the end of the algorithm's execution. This means that over the execution of the algorithm, the nonsaturating pushes must make up the difference of the relabel and saturating push operations in order for Φ to terminate with a value of 0.
The relabel operation can increase Φ by at most (2| V | − 1)(| V | − 2). A saturating push on (u, v) activates v if it was inactive before the push, increasing Φ by at most 2| V | − 1. Hence, the total contribution of all saturating pushes operations to Φ is at most (2| V | − 1)(2| V || E |). A nonsaturating push on (u, v) always deactivates u, but it can also activate v as in a saturating push. As a result, it decreases Φ by at least 𝓁(u) − 𝓁(v) = 1. Since relabels and saturating pushes increase Φ, the total number of nonsaturating pushes must make up the difference of (2| V | − 1)(| V | − 2) + (2| V | − 1)(2| V || E |) ≤ 4| V |2| E |. This results in a time bound of O(V 2E) for the nonsaturating push operations.
In sum, the algorithm executes O(V 2) relabels, O(VE) saturating pushes and O(V 2E) nonsaturating pushes. Data structures can be designed to pick and execute an applicable operation in O(1) time. Therefore, the time complexity of the algorithm is O(V 2E).

Example
The following is a sample execution of the generic push-relabel algorithm, as defined above, on the following simple network flow graph diagram.

In the example, the h and e values denote the label 𝓁 and excess xf , respectively, of the node during the execution of the algorithm. Each residual graph in the example only contains the residual arcs with a capacity larger than zero. Each residual graph may contain multiple iterations of the perform operation loop.

The example (but with initial flow of 0) can be run here interactively.

Practical implementations
While the generic push–relabel algorithm has O(V 2E) time complexity, efficient implementations achieve O(V 3) or lower time complexity by enforcing appropriate rules in selecting applicable push and relabel operations. The empirical performance can be further improved by heuristics.

"Current-arc" data structure and discharge operation
The "current-arc" data structure is a mechanism for visiting the in- and out-neighbors of a node in the flow network in a static circular order. If a singly linked list of neighbors is created for a node, the data structure can be as simple as a pointer into the list that steps through the list and rewinds to the head when it runs off the end.
Based on the "current-arc" data structure, the discharge operation can be defined. A discharge operation applies on an active node and repeatedly pushes flow from the node until it becomes inactive, relabeling it as necessary to create admissible arcs in the process.

discharge(u):
    while xf[u] > 0 do
        if current-arc[u] has run off the end of neighbors[u] then
            relabel(u)
            rewind current-arc[u]
        else
            let (u, v) = current-arc[u]
            if (u, v) is admissible then
                push(u, v)
            let current-arc[u] point to the next neighbor of u

Finding the next admissible edge to push on has 
  
    
      
        O
        (
        1
        )
      
    
    {\displaystyle O(1)}
  
 amortized complexity. The current-arc pointer only moves to the next neighbor when the edge to the current neighbor is saturated or non-admissible, and neither of these two properties can change until the active node 
  
    
      
        u
      
    
    {\displaystyle u}
  
 is relabelled. Therefore, when the pointer runs off, there are no admissible unsaturated edges and we have to relabel the active node 
  
    
      
        u
      
    
    {\displaystyle u}
  
, so having moved the pointer 
  
    
      
        O
        (
        V
        )
      
    
    {\displaystyle O(V)}
  
 times is paid for by the 
  
    
      
        O
        (
        V
        )
      
    
    {\displaystyle O(V)}
  
 relabel operation.

Active node selection rules
Definition of the discharge operation reduces the push–relabel algorithm to repeatedly selecting an active node to discharge. Depending on the selection rule, the algorithm exhibits different time complexities. For the sake of brevity, we ignore s and t when referring to the nodes in the following discussion.

FIFO selection rule
The FIFO push–relabel algorithm organizes the active nodes into a queue. The initial active nodes can be inserted in arbitrary order. The algorithm always removes the node at the front of the queue for discharging. Whenever an inactive node becomes active, it is appended to the back of the queue.
The algorithm has O(V 3) time complexity.

Relabel-to-front selection rule
The relabel-to-front push–relabel algorithm organizes all nodes into a linked list and maintains the invariant that the list is topologically sorted with respect to the admissible network. The algorithm scans the list from front to back and performs a discharge operation on the current node if it is active. If the node is relabeled, it is moved to the front of the list, and the scan is restarted from the front.
The algorithm also has O(V 3) time complexity.

Highest label selection rule
The highest-label push–relabel algorithm organizes all nodes into buckets indexed by their labels. The algorithm always selects an active node with the largest label to discharge.
The algorithm has O(V 2√E) time complexity. If the lowest-label selection rule is used instead, the time complexity becomes O(V 2E).

Implementation techniques
Although in the description of the generic push–relabel algorithm above, 𝓁(u) is set to zero for each node u other than s and t at the beginning, it is preferable to perform a backward breadth-first search from t to compute exact labels.
The algorithm is typically separated into two phases. Phase one computes a maximum pre-flow by discharging only active nodes whose labels are below n. Phase two converts the maximum preflow into a maximum flow by returning excess flow that cannot reach t to s. It can be shown that phase two has O(VE) time complexity regardless of the order of push and relabel operations and is therefore dominated by phase one. Alternatively, it can be implemented using flow decomposition.
Heuristics are crucial to improving the empirical performance of the algorithm. Two commonly used heuristics are the gap heuristic and the global relabeling heuristic. The gap heuristic detects gaps in the labeling function. If there is a label 0 < 𝓁' < | V | for which there is no node u such that 𝓁(u) = 𝓁', then any node u with 𝓁' < 𝓁(u) < | V | has been disconnected from t and can be relabeled to (| V | + 1) immediately. The global relabeling heuristic periodically performs backward breadth-first search from t in Gf  to compute the exact labels of the nodes. Both heuristics skip unhelpful relabel operations, which are a bottleneck of the algorithm and contribute to the ineffectiveness of dynamic trees.

Sample implementations


== References ==

## Related Articles

### Internal Links

- [Active-set method](https://en.wikipedia.org/wiki/Active-set_method)
- [Affine scaling](https://en.wikipedia.org/wiki/Affine_scaling)
- [Alexander V. Karzanov](https://en.wikipedia.org/wiki/Alexander_V._Karzanov)
- [Amortized analysis](https://en.wikipedia.org/wiki/Amortized_analysis)
- [Andrew V. Goldberg](https://en.wikipedia.org/wiki/Andrew_V._Goldberg)
- [Approximation algorithm](https://en.wikipedia.org/wiki/Approximation_algorithm)
- [Augmented Lagrangian method](https://en.wikipedia.org/wiki/Augmented_Lagrangian_method)
- [Barrier function](https://en.wikipedia.org/wiki/Barrier_function)
- [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [Berndt–Hall–Hall–Hausman algorithm](https://en.wikipedia.org/wiki/Berndt%E2%80%93Hall%E2%80%93Hall%E2%80%93Hausman_algorithm)
- [Borůvka's algorithm](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)
- [Branch and bound](https://en.wikipedia.org/wiki/Branch_and_bound)
- [Branch and cut](https://en.wikipedia.org/wiki/Branch_and_cut)
- [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Broyden–Fletcher–Goldfarb–Shanno algorithm](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Charles E. Leiserson](https://en.wikipedia.org/wiki/Charles_E._Leiserson)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Clifford Stein](https://en.wikipedia.org/wiki/Clifford_Stein)
- [Combinatorial optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization)
- [Comparison of optimization software](https://en.wikipedia.org/wiki/Comparison_of_optimization_software)
- [Convex optimization](https://en.wikipedia.org/wiki/Convex_optimization)
- [Convex optimization](https://en.wikipedia.org/wiki/Convex_optimization)
- [Criss-cross algorithm](https://en.wikipedia.org/wiki/Criss-cross_algorithm)
- [Cutting-plane method](https://en.wikipedia.org/wiki/Cutting-plane_method)
- [Davidon–Fletcher–Powell formula](https://en.wikipedia.org/wiki/Davidon%E2%80%93Fletcher%E2%80%93Powell_formula)
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Dinic's algorithm](https://en.wikipedia.org/wiki/Dinic%27s_algorithm)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Edmonds–Karp algorithm](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm)
- [Ellipsoid method](https://en.wikipedia.org/wiki/Ellipsoid_method)
- [Evolutionary algorithm](https://en.wikipedia.org/wiki/Evolutionary_algorithm)
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [FIFO (computing and electronics)](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics))
- [Flow network](https://en.wikipedia.org/wiki/Flow_network)
- [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)
- [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [Gauss–Newton algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm)
- [Golden-section search](https://en.wikipedia.org/wiki/Golden-section_search)
- [Gradient](https://en.wikipedia.org/wiki/Gradient)
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
- [List of algorithms](https://en.wikipedia.org/wiki/List_of_algorithms)
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix)
- [Heuristic (computer science)](https://en.wikipedia.org/wiki/Heuristic_(computer_science))
- [Hill climbing](https://en.wikipedia.org/wiki/Hill_climbing)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Integer programming](https://en.wikipedia.org/wiki/Integer_programming)
- [Introduction to Algorithms](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)
- [Iterative method](https://en.wikipedia.org/wiki/Iterative_method)
- [Karmarkar's algorithm](https://en.wikipedia.org/wiki/Karmarkar%27s_algorithm)
- [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [Lemke's algorithm](https://en.wikipedia.org/wiki/Lemke%27s_algorithm)
- [Levenberg–Marquardt algorithm](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm)
- [Limited-memory BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS)
- [Line search](https://en.wikipedia.org/wiki/Line_search)
- [Linear programming](https://en.wikipedia.org/wiki/Linear_programming)
- [Link/cut tree](https://en.wikipedia.org/wiki/Link/cut_tree)
- [Local convergence](https://en.wikipedia.org/wiki/Local_convergence)
- [Local search (optimization)](https://en.wikipedia.org/wiki/Local_search_(optimization))
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Matroid](https://en.wikipedia.org/wiki/Matroid)
- [Max-flow min-cut theorem](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem)
- [Maximum flow problem](https://en.wikipedia.org/wiki/Maximum_flow_problem)
- [Metaheuristic](https://en.wikipedia.org/wiki/Metaheuristic)
- [Minimum-cost flow problem](https://en.wikipedia.org/wiki/Minimum-cost_flow_problem)
- [Minimum spanning tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree)
- [Mirror descent](https://en.wikipedia.org/wiki/Mirror_descent)
- [Nelder–Mead method](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method)
- [Newton's method in optimization](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)
- [Nonlinear conjugate gradient method](https://en.wikipedia.org/wiki/Nonlinear_conjugate_gradient_method)
- [Nonlinear programming](https://en.wikipedia.org/wiki/Nonlinear_programming)
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Parallel metaheuristic](https://en.wikipedia.org/wiki/Parallel_metaheuristic)
- [Penalty method](https://en.wikipedia.org/wiki/Penalty_method)
- [Potential method](https://en.wikipedia.org/wiki/Potential_method)
- [Powell's dog leg method](https://en.wikipedia.org/wiki/Powell%27s_dog_leg_method)
- [Powell's method](https://en.wikipedia.org/wiki/Powell%27s_method)
- [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quadratic programming](https://en.wikipedia.org/wiki/Quadratic_programming)
- [Quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method)
- [Revised simplex method](https://en.wikipedia.org/wiki/Revised_simplex_method)
- [Robert Tarjan](https://en.wikipedia.org/wiki/Robert_Tarjan)
- [Ron Rivest](https://en.wikipedia.org/wiki/Ron_Rivest)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Sequential quadratic programming](https://en.wikipedia.org/wiki/Sequential_quadratic_programming)
- [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [Shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem)
- [Simplex algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm)
- [Simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Spiral optimization algorithm](https://en.wikipedia.org/wiki/Spiral_optimization_algorithm)
- [Strongly-polynomial time](https://en.wikipedia.org/wiki/Strongly-polynomial_time)
- [Subgradient method](https://en.wikipedia.org/wiki/Subgradient_method)
- [Successive linear programming](https://en.wikipedia.org/wiki/Successive_linear_programming)
- [Successive parabolic interpolation](https://en.wikipedia.org/wiki/Successive_parabolic_interpolation)
- [Symmetric rank-one](https://en.wikipedia.org/wiki/Symmetric_rank-one)
- [Tabu search](https://en.wikipedia.org/wiki/Tabu_search)
- [Thomas H. Cormen](https://en.wikipedia.org/wiki/Thomas_H._Cormen)
- [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting)
- [Truncated Newton method](https://en.wikipedia.org/wiki/Truncated_Newton_method)
- [Trust region](https://en.wikipedia.org/wiki/Trust_region)
- [Uzi Vishkin](https://en.wikipedia.org/wiki/Uzi_Vishkin)
- [Wolfe conditions](https://en.wikipedia.org/wiki/Wolfe_conditions)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Template:Optimization algorithms](https://en.wikipedia.org/wiki/Template:Optimization_algorithms)
- [Template talk:Optimization algorithms](https://en.wikipedia.org/wiki/Template_talk:Optimization_algorithms)
- [Category:Articles with unsourced statements from December 2024](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_December_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:42:31.766460+00:00_