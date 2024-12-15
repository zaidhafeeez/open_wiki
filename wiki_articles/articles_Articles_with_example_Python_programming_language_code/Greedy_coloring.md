# Greedy coloring

## Article Metadata

- **Last Updated:** 2024-12-15T04:26:51.442339+00:00
- **Original Article:** [Greedy coloring](https://en.wikipedia.org/wiki/Greedy_coloring)
- **Language:** en
- **Page ID:** 21051195

## Summary

In the study of graph coloring problems in mathematics and computer science, a greedy coloring or sequential coloring is a coloring of the vertices of a graph formed by a greedy algorithm that considers the vertices of the graph in sequence and assigns each vertex its first available color. Greedy colorings can be found in linear time, but they do not, in general, use the minimum number of colors possible.
Different choices of the sequence of vertices will typically produce different colorings o

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Good articles
- Category:Graph coloring
- Category:Pages using multiple image with auto scaled images
- Category:Short description is different from Wikidata

## Table of Contents

- Algorithm
- Choice of ordering
- Alternative color selection schemes
- Applications
- Notes

## Content

In the study of graph coloring problems in mathematics and computer science, a greedy coloring or sequential coloring is a coloring of the vertices of a graph formed by a greedy algorithm that considers the vertices of the graph in sequence and assigns each vertex its first available color. Greedy colorings can be found in linear time, but they do not, in general, use the minimum number of colors possible.
Different choices of the sequence of vertices will typically produce different colorings of the given graph, so much of the study of greedy colorings has concerned how to find a good ordering. There always exists an ordering that produces an optimal coloring, but although such orderings can be found for many special classes of graphs, they are hard to find in general. Commonly used strategies for vertex ordering involve placing higher-degree vertices earlier than lower-degree vertices, or choosing vertices with fewer available colors in preference to vertices that are less constrained.
Variations of greedy coloring choose the colors in an online manner, without any knowledge of the structure of the uncolored part of the graph, or choose other colors than the first available in order to reduce the total number of colors. Greedy coloring algorithms have been applied to scheduling and register allocation problems, the analysis of combinatorial games, and the proofs of other mathematical results including Brooks' theorem on the relation between coloring and degree.
Other concepts in graph theory derived from greedy colorings include the Grundy number of a graph (the largest number of colors that can be found by a greedy coloring), and the well-colored graphs, graphs for which all greedy colorings use the same number of colors.

Algorithm
The greedy coloring for a given vertex ordering can be computed by an algorithm that runs in linear time. The algorithm processes the vertices in the given ordering, assigning a color to each one as it is processed. The colors may be represented by the numbers 
  
    
      
        0
        ,
        1
        ,
        2
        ,
        …
      
    
    {\displaystyle 0,1,2,\dots }
  
 and each vertex is given the color with the smallest number that is not already used by one of its neighbors.
To find the smallest available color, one may use an array to count the number of neighbors of each color (or alternatively, to represent the set of colors of neighbors), and then scan the array to find the index of its first zero.
In Python, the algorithm can be expressed as:

The first_available subroutine takes time proportional to the length of its argument list, because it performs two loops, one over the list itself and one over a list of counts that has the same length. The time for the overall coloring algorithm is dominated by the calls to this subroutine. Each edge in the graph contributes to only one of these calls, the one for the endpoint of the edge that is later in the vertex ordering. Therefore, the sum of the lengths of the argument lists to first_available, and the total time for the algorithm, are proportional to the number of edges in the graph.
An alternative algorithm, producing the same coloring, is to choose the sets of vertices with each color, one color at a time. In this method, each color class 
  
    
      
        C
      
    
    {\displaystyle C}
  
 is chosen by scanning through the vertices in the given ordering. When this scan encounters an uncolored vertex 
  
    
      
        v
      
    
    {\displaystyle v}
  
 that has no neighbor in 
  
    
      
        C
      
    
    {\displaystyle C}
  
, it adds 
  
    
      
        v
      
    
    {\displaystyle v}
  
 to 
  
    
      
        C
      
    
    {\displaystyle C}
  
. In this way, 
  
    
      
        C
      
    
    {\displaystyle C}
  
 becomes a maximal independent set among the vertices that were not already assigned smaller colors. The algorithm repeatedly finds color classes in this way until all vertices are colored. However, it involves making multiple scans of the graph, one scan for each color class, instead of the method outlined above which uses only a single scan.

Choice of ordering
Different orderings of the vertices of a graph may cause the greedy coloring to use different numbers of colors, ranging from the optimal number of colors to, in some cases, a number of colors that is proportional to the number of vertices in the graph. For instance, a crown graph (a graph formed from two disjoint sets of n/2 vertices {a1, a2, ...} and {b1, b2, ...} by connecting ai to bj whenever i ≠ j) can be a particularly bad case for greedy coloring. With the vertex ordering a1, b1, a2, b2, ..., a greedy coloring will use n/2 colors, one color for each pair (ai, bi). However, the optimal number of colors for this graph is two, one color for the vertices ai and another for the vertices bi. There also exist graphs such that with high probability a randomly chosen vertex ordering leads to a number of colors much larger than the minimum. Therefore, it is of some importance in greedy coloring to choose the vertex ordering carefully.

Good orders
The vertices of any graph may always be ordered in such a way that the greedy algorithm produces an optimal coloring. For, given any optimal coloring, one may order the vertices by their colors. Then when one uses a greedy algorithm with this order, the resulting coloring is automatically optimal. However, because optimal graph coloring is NP-complete, any subproblem that would allow this problem to be solved quickly, including finding an optimal ordering for greedy coloring, is NP-hard.
In interval graphs and chordal graphs, if the vertices are ordered in the reverse of a perfect elimination ordering,
then the earlier neighbors of every vertex will form a clique. This property causes the greedy coloring to produce an optimal coloring, because it never uses more colors than are required for each of these cliques. An elimination ordering can be found in linear time, when it exists.
More strongly, any perfect elimination ordering is hereditarily optimal, meaning that it is optimal both for the graph itself and for all of its induced subgraphs. The perfectly orderable graphs (which include chordal graphs, comparability graphs, and distance-hereditary graphs) are defined as graphs that have a hereditarily optimal ordering. Recognizing perfectly orderable graphs is also NP-complete.

Bad orders
The number of colors produced by the greedy coloring for the worst ordering of a given graph is called its Grundy number.
Just as finding a good vertex ordering for greedy coloring is difficult, so is finding a bad vertex ordering.
It is NP-complete to determine, for a given graph G and number k, whether there exists an ordering of the vertices of G that causes the greedy algorithm to use k or more colors. In particular, this means that it is difficult to find the worst ordering for G.

Graphs for which order is irrelevant
The well-colored graphs are the graphs for which all vertex orderings produce the same number of colors. This number of colors, in these graphs, equals both the chromatic number and the Grundy number. They include the cographs, which are exactly the graphs in which all induced subgraphs are well-colored. However, it is co-NP-complete to determine whether a graph is well-colored.
If a random graph is drawn from the Erdős–Rényi model with constant probability of including each edge, then any vertex ordering that is chosen independently of the graph edges leads to a coloring whose number of colors is close to twice the optimal value, with high probability.
It remains unknown whether there is any polynomial time method for finding significantly better colorings of these graphs.

Degeneracy
Because optimal vertex orderings are hard to find, heuristics have been used that attempt to reduce the number of colors while not guaranteeing an optimal number of colors. A commonly used ordering for greedy coloring is to choose a vertex v of minimum degree, order the subgraph with v removed recursively, and then place v last in the ordering. The largest degree of a removed vertex that this algorithm encounters is called the degeneracy of the graph, denoted d. In the context of greedy coloring, the same ordering strategy is also called the smallest last ordering. This vertex ordering, and the degeneracy, may be computed in linear time.
It can be viewed as an improved version of an earlier vertex ordering method, the largest-first ordering, which sorts the vertices in descending order by their degrees.
With the degeneracy ordering, the greedy coloring will use at most d + 1 colors. This is because, when colored, each vertex will have at most d already-colored neighbors, so one of the first d + 1 colors will be free for it to use. Greedy coloring with the degeneracy ordering can find optimal colorings for certain classes of graphs, including trees, pseudoforests, and crown graphs. Markossian, Gasparian & Reed (1996) define a graph 
  
    
      
        G
      
    
    {\displaystyle G}
  
 to be 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
-perfect if, for 
  
    
      
        G
      
    
    {\displaystyle G}
  
 and every induced subgraph of 
  
    
      
        G
      
    
    {\displaystyle G}
  
, the chromatic number equals the degeneracy plus one. For these graphs, the greedy algorithm with the degeneracy ordering is always optimal.
Every 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
-perfect graph must be an even-hole-free graph, because even cycles have chromatic number two and degeneracy two, not matching the equality in the definition of 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
-perfect graphs. If a graph and its complement graph are both even-hole-free, they are both 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
-perfect. The graphs that are both perfect graphs and 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
-perfect graphs are exactly the chordal graphs. On even-hole-free graphs more generally, the degeneracy ordering approximates the optimal coloring to within at most twice the optimal number of colors; that is, its approximation ratio is 2. On unit disk graphs its approximation ratio is 3. The triangular prism is the smallest graph for which one of its degeneracy orderings leads to a non-optimal coloring, and the square antiprism is the smallest graph that cannot be optimally colored using any of its degeneracy orderings.

Adaptive orders
Brélaz (1979) proposes a strategy, called DSatur, for vertex ordering in greedy coloring that interleaves the construction of the ordering with the coloring process.
In his version of the greedy coloring algorithm, the next vertex to color at each step is chosen as the one with the largest number of distinct colors in its neighborhood. In case of ties, a vertex of maximal degree in the subgraph of uncolored vertices is chosen from the tied vertices. By keeping track of the sets of neighboring colors and their cardinalities at each step, it is possible to implement this method in linear time.
This method can find the optimal colorings for bipartite graphs, all cactus graphs, all wheel graphs, all graphs on at most six vertices, and almost every 
  
    
      
        k
      
    
    {\displaystyle k}
  
-colorable graph. Although Lévêque & Maffray (2005) originally claimed that this method finds optimal colorings for the Meyniel graphs, they later found a counterexample to this claim.

Alternative color selection schemes
It is possible to define variations of the greedy coloring algorithm in which the vertices of the given graph are colored in a given sequence but in which the color chosen for each vertex is not necessarily the first available color. These include methods in which the uncolored part of the graph is unknown to the algorithm, or in which the algorithm is given some freedom to make better coloring choices than the basic greedy algorithm would.

Online selection
Alternative color selection strategies have been studied within the framework of online algorithms. In the online graph-coloring problem, vertices of a graph are presented one at a time in an arbitrary order to a coloring algorithm; the algorithm must choose a color for each vertex, based only on the colors of and adjacencies among already-processed vertices. In this context, one measures the quality of a color selection strategy by its competitive ratio, the ratio between the number of colors it uses and the optimal number of colors for the given graph.
If no additional restrictions on the graph are given, the optimal competitive ratio is only slightly sublinear. However, for interval graphs, a constant competitive ratio is possible, while for bipartite graphs and sparse graphs a logarithmic ratio can be achieved. Indeed, for sparse graphs, the standard greedy coloring strategy of choosing the first available color achieves this competitive ratio, and it is possible to prove a matching lower bound on the competitive ratio of any online coloring algorithm.

Parsimonous coloring
A parsimonious coloring, for a given graph and vertex ordering, has been defined to be a coloring produced by a greedy algorithm that colors the vertices in the given order, and only introduces a new color when all previous colors are adjacent to the given vertex, but can choose which color to use (instead of always choosing the smallest) when it is able to re-use an existing color. The ordered chromatic number is the smallest number of colors that can be obtained for the given ordering in this way, and the ochromatic number is the largest ordered chromatic number among all vertex colorings of a given graph. Despite its different definition, the ochromatic number always equals the Grundy number.

Applications
Because it is fast and in many cases can use few colors, greedy coloring can be used in applications where a good but not optimal graph coloring is needed. One of the early applications of the greedy algorithm was to problems such as course scheduling, in which a collection of tasks must be assigned to a given set of time slots, avoiding incompatible tasks being assigned to the same time slot.
It can also be used in compilers for register allocation, by applying it to a graph whose vertices represent values to be assigned to registers and whose edges represent conflicts between two values that cannot be assigned to the same register. In many cases, these interference graphs are chordal graphs, allowing greedy coloring to produce an optimal register assignment.
In combinatorial game theory, for an impartial game given in explicit form as a directed acyclic graph whose vertices represent game positions and whose edges represent valid moves from one position to another, the greedy coloring algorithm (using the reverse of a topological ordering of the graph) calculates the nim-value of each position. These values can be used to determine optimal play in any single game or any disjunctive sum of games.
For a graph of maximum degree Δ, any greedy coloring will use at most Δ + 1 colors. Brooks' theorem states that with two exceptions (cliques and odd cycles) at most Δ colors are needed. One proof of Brooks' theorem involves finding a vertex ordering in which the first two vertices are adjacent to the final vertex but not adjacent to each other, and each vertex other than the last one has at least one later neighbor. For an ordering with this property, the greedy coloring algorithm uses at most Δ colors.

Notes


== References ==

## Related Articles

### Internal Links

- [ACM Transactions on Programming Languages and Systems](https://en.wikipedia.org/wiki/ACM_Transactions_on_Programming_Languages_and_Systems)
- [Alan M. Frieze](https://en.wikipedia.org/wiki/Alan_M._Frieze)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Algorithmica](https://en.wikipedia.org/wiki/Algorithmica)
- [Almost everywhere](https://en.wikipedia.org/wiki/Almost_everywhere)
- [Approximation algorithm](https://en.wikipedia.org/wiki/Approximation_algorithm)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Bipartite graph](https://en.wikipedia.org/wiki/Bipartite_graph)
- [Brooks' theorem](https://en.wikipedia.org/wiki/Brooks%27_theorem)
- [Bruce Reed (mathematician)](https://en.wikipedia.org/wiki/Bruce_Reed_(mathematician))
- [Cactus graph](https://en.wikipedia.org/wiki/Cactus_graph)
- [Cardinality](https://en.wikipedia.org/wiki/Cardinality)
- [Chordal graph](https://en.wikipedia.org/wiki/Chordal_graph)
- [Claude Berge](https://en.wikipedia.org/wiki/Claude_Berge)
- [Clique (graph theory)](https://en.wikipedia.org/wiki/Clique_(graph_theory))
- [Co-NP-complete](https://en.wikipedia.org/wiki/Co-NP-complete)
- [Cograph](https://en.wikipedia.org/wiki/Cograph)
- [Combinatorial game theory](https://en.wikipedia.org/wiki/Combinatorial_game_theory)
- [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM)
- [Comparability graph](https://en.wikipedia.org/wiki/Comparability_graph)
- [Competitive analysis (online algorithm)](https://en.wikipedia.org/wiki/Competitive_analysis_(online_algorithm))
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Complement graph](https://en.wikipedia.org/wiki/Complement_graph)
- [Complete graph](https://en.wikipedia.org/wiki/Complete_graph)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Crown graph](https://en.wikipedia.org/wiki/Crown_graph)
- [Cycle graph](https://en.wikipedia.org/wiki/Cycle_graph)
- [DSatur](https://en.wikipedia.org/wiki/DSatur)
- [David Matula](https://en.wikipedia.org/wiki/David_Matula)
- [David S. Johnson](https://en.wikipedia.org/wiki/David_S._Johnson)
- [Degeneracy (graph theory)](https://en.wikipedia.org/wiki/Degeneracy_(graph_theory))
- [Degree (graph theory)](https://en.wikipedia.org/wiki/Degree_(graph_theory))
- [Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)
- [Discrete Mathematics (journal)](https://en.wikipedia.org/wiki/Discrete_Mathematics_(journal))
- [Disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets)
- [Disjunctive sum](https://en.wikipedia.org/wiki/Disjunctive_sum)
- [Distance-hereditary graph](https://en.wikipedia.org/wiki/Distance-hereditary_graph)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dominic Welsh](https://en.wikipedia.org/wiki/Dominic_Welsh)
- [Erdős–Rényi model](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model)
- [Even-hole-free graph](https://en.wikipedia.org/wiki/Even-hole-free_graph)
- [George Szekeres](https://en.wikipedia.org/wiki/George_Szekeres)
- [Graph coloring](https://en.wikipedia.org/wiki/Graph_coloring)
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [Grundy number](https://en.wikipedia.org/wiki/Grundy_number)
- [Herbert Wilf](https://en.wikipedia.org/wiki/Herbert_Wilf)
- [Heuristic](https://en.wikipedia.org/wiki/Heuristic)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Impartial game](https://en.wikipedia.org/wiki/Impartial_game)
- [Induced subgraph](https://en.wikipedia.org/wiki/Induced_subgraph)
- [Interval graph](https://en.wikipedia.org/wiki/Interval_graph)
- [Journal of Combinatorial Theory](https://en.wikipedia.org/wiki/Journal_of_Combinatorial_Theory)
- [Journal of Graph Theory](https://en.wikipedia.org/wiki/Journal_of_Graph_Theory)
- [Journal of the ACM](https://en.wikipedia.org/wiki/Journal_of_the_ACM)
- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [László Lovász](https://en.wikipedia.org/wiki/L%C3%A1szl%C3%B3_Lov%C3%A1sz)
- [Mathematical Reviews](https://en.wikipedia.org/wiki/Mathematical_Reviews)
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Maximal independent set](https://en.wikipedia.org/wiki/Maximal_independent_set)
- [Mex (mathematics)](https://en.wikipedia.org/wiki/Mex_(mathematics))
- [Meyniel graph](https://en.wikipedia.org/wiki/Meyniel_graph)
- [Michael Saks (mathematician)](https://en.wikipedia.org/wiki/Michael_Saks_(mathematician))
- [NP-completeness](https://en.wikipedia.org/wiki/NP-completeness)
- [NP-hardness](https://en.wikipedia.org/wiki/NP-hardness)
- [Neighbourhood (graph theory)](https://en.wikipedia.org/wiki/Neighbourhood_(graph_theory))
- [Sprague–Grundy theorem](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
- [Online algorithm](https://en.wikipedia.org/wiki/Online_algorithm)
- [Paul Erdős](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s)
- [Chordal graph](https://en.wikipedia.org/wiki/Chordal_graph)
- [Perfect graph](https://en.wikipedia.org/wiki/Perfect_graph)
- [Perfectly orderable graph](https://en.wikipedia.org/wiki/Perfectly_orderable_graph)
- [Pseudoforest](https://en.wikipedia.org/wiki/Pseudoforest)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Random graph](https://en.wikipedia.org/wiki/Random_graph)
- [Recursion (computer science)](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [Register allocation](https://en.wikipedia.org/wiki/Register_allocation)
- [Renu C. Laskar](https://en.wikipedia.org/wiki/Renu_C._Laskar)
- [Robert Tarjan](https://en.wikipedia.org/wiki/Robert_Tarjan)
- [Robin Wilson (mathematician)](https://en.wikipedia.org/wiki/Robin_Wilson_(mathematician))
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SIAM Journal on Computing](https://en.wikipedia.org/wiki/SIAM_Journal_on_Computing)
- [Society for Industrial and Applied Mathematics](https://en.wikipedia.org/wiki/Society_for_Industrial_and_Applied_Mathematics)
- [Dense graph](https://en.wikipedia.org/wiki/Dense_graph)
- [Square antiprism](https://en.wikipedia.org/wiki/Square_antiprism)
- [The Computer Journal](https://en.wikipedia.org/wiki/The_Computer_Journal)
- [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting)
- [Triangular prism](https://en.wikipedia.org/wiki/Triangular_prism)
- [Graph (discrete mathematics)](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics))
- [Unit disk graph](https://en.wikipedia.org/wiki/Unit_disk_graph)
- [Václav Chvátal](https://en.wikipedia.org/wiki/V%C3%A1clav_Chv%C3%A1tal)
- [Vertex (graph theory)](https://en.wikipedia.org/wiki/Vertex_(graph_theory))
- [Vertex operator algebra](https://en.wikipedia.org/wiki/Vertex_operator_algebra)
- [Well-colored graph](https://en.wikipedia.org/wiki/Well-colored_graph)
- [Wheel graph](https://en.wikipedia.org/wiki/Wheel_graph)
- [William T. Trotter](https://en.wikipedia.org/wiki/William_T._Trotter)
- [With high probability](https://en.wikipedia.org/wiki/With_high_probability)
- [Wikipedia:Good articles](https://en.wikipedia.org/wiki/Wikipedia:Good_articles)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:26:51.442339+00:00_