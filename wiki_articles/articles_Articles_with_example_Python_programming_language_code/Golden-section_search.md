# Golden-section search

## Article Metadata

- **Last Updated:** 2024-12-15T04:26:53.002692+00:00
- **Original Article:** [Golden-section search](https://en.wikipedia.org/wiki/Golden-section_search)
- **Language:** en
- **Page ID:** 1814209

## Summary

The golden-section search is a technique for finding an extremum (minimum or maximum) of a function inside a specified interval. For a strictly unimodal function with an extremum inside the interval, it will find that extremum, while for an interval containing multiple extrema (possibly including the interval boundaries), it will converge to one of them. If the only extremum on the interval is on a boundary of the interval, it will converge to that boundary point. The method operates by successi

## Categories

- Category:All articles lacking in-text citations
- Category:Articles lacking in-text citations from June 2024
- Category:Articles with example Java code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Fibonacci numbers
- Category:Golden ratio
- Category:Optimization algorithms and methods
- Category:Search algorithms
- Category:Short description is different from Wikidata

## Table of Contents

- Basic idea
- Probe point selection
- Termination condition
- Algorithm
- Related algorithms
- See also
- References

## Content

The golden-section search is a technique for finding an extremum (minimum or maximum) of a function inside a specified interval. For a strictly unimodal function with an extremum inside the interval, it will find that extremum, while for an interval containing multiple extrema (possibly including the interval boundaries), it will converge to one of them. If the only extremum on the interval is on a boundary of the interval, it will converge to that boundary point. The method operates by successively narrowing the range of values on the specified interval, which makes it relatively slow, but very robust. The technique derives its name from the fact that the algorithm maintains the function values for four points whose three interval widths are in the ratio φ:1:φ, where φ is the golden ratio. These ratios are maintained for each iteration and are maximally efficient. Excepting boundary points, when searching for a minimum, the central point is always less than or equal to the outer points, assuring that a minimum is contained between the outer points. The converse is true when searching for a maximum. The algorithm is the limit of Fibonacci search (also described below) for many function evaluations. Fibonacci search and golden-section search were discovered by Kiefer (1953) (see also Avriel and Wilde (1966)).

Basic idea
The discussion here is posed in terms of searching for a minimum (searching for a maximum is similar) of a unimodal function. Unlike finding a zero, where two function evaluations with opposite sign are sufficient to bracket a root, when searching for a minimum, three values are necessary. The golden-section search is an efficient way to progressively reduce the interval locating the minimum. The key is to observe that regardless of how many points have been evaluated, the minimum lies within the interval defined by the two points adjacent to the point with the least value so far evaluated.
The diagram above illustrates a single step in the technique for finding a minimum. The functional values of 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
 are on the vertical axis, and the horizontal axis is the x parameter. The value of 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
 has already been evaluated at the three points: 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
, 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
, and 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
. Since 
  
    
      
        
          f
          
            2
          
        
      
    
    {\displaystyle f_{2}}
  
 is smaller than either 
  
    
      
        
          f
          
            1
          
        
      
    
    {\displaystyle f_{1}}
  
 or 
  
    
      
        
          f
          
            3
          
        
      
    
    {\displaystyle f_{3}}
  
, it is clear that a minimum lies inside the interval from 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
 to 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
.
The next step in the minimization process is to "probe" the function by evaluating it at a new value of x, namely 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
. It is most efficient to choose 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
 somewhere inside the largest interval, i.e. between 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
 and 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
.  From the diagram, it is clear that if the function yields 
  
    
      
        
          f
          
            4
            a
          
        
        >
        f
        (
        
          x
          
            2
          
        
        )
      
    
    {\displaystyle f_{4a}>f(x_{2})}
  
, then a minimum lies between 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
 and 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
, and the new triplet of points will be 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
, 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
, and 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
. However, if the function yields the value 
  
    
      
        
          f
          
            4
            b
          
        
        <
        f
        (
        
          x
          
            2
          
        
        )
      
    
    {\displaystyle f_{4b}<f(x_{2})}
  
, then a minimum lies between 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
 and 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
, and the new triplet of points will be 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
, 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
, and 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
. Thus, in either case, we can construct a new narrower search interval that is guaranteed to contain the function's minimum.

Probe point selection
From the diagram above, it is seen that the new search interval will be either between 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
 and 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
 with a length of a + c, or between 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
 and 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
 with a length of b. The golden-section search requires that these intervals be equal. If they are not, a run of "bad luck" could lead to the wider interval being used many times, thus slowing down the rate of convergence. To ensure that b = a + c, the algorithm should choose 
  
    
      
        
          x
          
            4
          
        
        =
        
          x
          
            1
          
        
        +
        (
        
          x
          
            3
          
        
        −
        
          x
          
            2
          
        
        )
      
    
    {\displaystyle x_{4}=x_{1}+(x_{3}-x_{2})}
  
.
However, there still remains the question of where 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
 should be placed in relation to 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
 and 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
. The golden-section search chooses the spacing between these points in such a way that these points have the same proportion of spacing as the subsequent triple 
  
    
      
        
          x
          
            1
          
        
        ,
        
          x
          
            2
          
        
        ,
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{1},x_{2},x_{4}}
  
 or 
  
    
      
        
          x
          
            2
          
        
        ,
        
          x
          
            4
          
        
        ,
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{2},x_{4},x_{3}}
  
. By maintaining the same proportion of spacing throughout the algorithm, we avoid a situation in which 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
 is very close to 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
 or 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
 and guarantee that the interval width shrinks by the same constant proportion in each step.
Mathematically, to ensure that the spacing after evaluating 
  
    
      
        f
        (
        
          x
          
            4
          
        
        )
      
    
    {\displaystyle f(x_{4})}
  
 is proportional to the spacing prior to that evaluation, if 
  
    
      
        f
        (
        
          x
          
            4
          
        
        )
      
    
    {\displaystyle f(x_{4})}
  
 is 
  
    
      
        
          f
          
            4
            a
          
        
      
    
    {\displaystyle f_{4a}}
  
 and our new triplet of points is 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
, 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
, and 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
, then we want

  
    
      
        
          
            c
            a
          
        
        =
        
          
            a
            b
          
        
        .
      
    
    {\displaystyle {\frac {c}{a}}={\frac {a}{b}}.}
  

However, if 
  
    
      
        f
        (
        
          x
          
            4
          
        
        )
      
    
    {\displaystyle f(x_{4})}
  
 is 
  
    
      
        
          f
          
            4
            b
          
        
      
    
    {\displaystyle f_{4b}}
  
 and our new triplet of points is 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
, 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
, and 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
, then we want

  
    
      
        
          
            c
            
              b
              −
              c
            
          
        
        =
        
          
            a
            b
          
        
        .
      
    
    {\displaystyle {\frac {c}{b-c}}={\frac {a}{b}}.}
  

Eliminating c from these two simultaneous equations yields

  
    
      
        
          
            (
            
              
                b
                a
              
            
            )
          
          
            2
          
        
        −
        
          
            b
            a
          
        
        =
        1
        ,
      
    
    {\displaystyle \left({\frac {b}{a}}\right)^{2}-{\frac {b}{a}}=1,}
  

or

  
    
      
        
          
            b
            a
          
        
        =
        φ
        ,
      
    
    {\displaystyle {\frac {b}{a}}=\varphi ,}
  

where φ is the golden ratio:

  
    
      
        φ
        =
        
          
            
              1
              +
              
                
                  5
                
              
            
            2
          
        
        =
        1.618033988
        …
      
    
    {\displaystyle \varphi ={\frac {1+{\sqrt {5}}}{2}}=1.618033988\ldots }
  

The appearance of the golden ratio in the proportional spacing of the evaluation points is how this search algorithm gets its name.

Termination condition
Any number of termination conditions may be applied, depending upon the application. The interval ΔX = X4 − X1 is a measure of the absolute error in the estimation of the minimum X and may be used to terminate the algorithm. The value of ΔX is reduced by a factor of r = φ − 1 for each iteration, so the number of iterations to reach an absolute error of ΔX is about ln(ΔX/ΔX0) / ln(r), where ΔX0 is the initial value of ΔX. 
Because smooth functions are flat (their first derivative is close to zero) near a minimum, attention must be paid not to expect too great an accuracy in locating the minimum. The termination condition provided in the book Numerical Recipes in C is based on testing the gaps among 
  
    
      
        
          x
          
            1
          
        
      
    
    {\displaystyle x_{1}}
  
, 
  
    
      
        
          x
          
            2
          
        
      
    
    {\displaystyle x_{2}}
  
, 
  
    
      
        
          x
          
            3
          
        
      
    
    {\displaystyle x_{3}}
  
 and 
  
    
      
        
          x
          
            4
          
        
      
    
    {\displaystyle x_{4}}
  
, terminating when within the relative accuracy bounds

  
    
      
        
          |
        
        
          x
          
            3
          
        
        −
        
          x
          
            1
          
        
        
          |
        
        <
        τ
        
          
            (
          
        
        
          |
        
        
          x
          
            2
          
        
        
          |
        
        +
        
          |
        
        
          x
          
            4
          
        
        
          |
        
        
          
            )
          
        
        ,
      
    
    {\displaystyle |x_{3}-x_{1}|<\tau {\big (}|x_{2}|+|x_{4}|{\big )},}
  

where 
  
    
      
        τ
      
    
    {\displaystyle \tau }
  
 is a tolerance parameter of the algorithm, and 
  
    
      
        
          |
        
        x
        
          |
        
      
    
    {\displaystyle |x|}
  
 is the absolute value of 
  
    
      
        x
      
    
    {\displaystyle x}
  
. The check is based on the bracket size relative to its central value, because that relative error in 
  
    
      
        x
      
    
    {\displaystyle x}
  
 is approximately proportional to the squared absolute error in 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
 in typical cases. For that same reason, the Numerical Recipes text recommends that 
  
    
      
        τ
        =
        
          
            ε
          
        
      
    
    {\displaystyle \tau ={\sqrt {\varepsilon }}}
  
, where 
  
    
      
        ε
      
    
    {\displaystyle \varepsilon }
  
 is the required absolute precision of 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
.

Algorithm
Note! The examples here describe an algorithm that is for finding the minimum of a function. For maximum, the comparison operators need to be reversed.

Iterative algorithm
Specify the function to be minimized, ⁠
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
⁠, the interval to be searched as {X1,X4}, and their functional values F1 and F4.
Calculate an interior point and its functional value F2. The two interval lengths are in the ratio c : r or r : c where r = φ − 1; and c = 1 − r, with φ being the golden ratio.
Using the triplet, determine if convergence criteria are fulfilled. If they are, estimate the X at the minimum from that triplet and return.
From the triplet, calculate the other interior point and its functional value. The three intervals will be in the ratio ⁠
  
    
      
        c
        :
        c
        r
        :
        c
      
    
    {\displaystyle c:cr:c}
  
⁠.
The three points for the next iteration will be the one where F is a minimum, and the two points closest to it in X.
Go to step 3.

Recursive algorithm
Related algorithms
Fibonacci search
A very similar algorithm can also be used to find the extremum (minimum or maximum) of a sequence of values that has a single local minimum or local maximum. In order to approximate the probe positions of golden section search while probing only integer sequence indices, the variant of the algorithm for this case typically maintains a bracketing of the solution in which the length of the bracketed interval is a Fibonacci number. For this reason, the sequence variant of golden section search is often called Fibonacci search.
Fibonacci search was first devised by Kiefer (1953) as a minimax search for the maximum (minimum) of a unimodal function in an interval.

Bisection method
The Bisection method is a similar algorithm for finding a zero of a function. Note that, for bracketing a zero, only two points are needed, rather than three. The interval ratio decreases by 2 in each step, rather than by the golden ratio.

See also
Ternary search
Brent's method
Binary search

References

Kiefer, J. (1953), "Sequential minimax search for a maximum", Proceedings of the American Mathematical Society, 4 (3): 502–506, doi:10.2307/2032161, JSTOR 2032161, MR 0055639
Avriel, Mordecai; Wilde, Douglass J. (1966), "Optimality proof for the symmetric Fibonacci search technique", Fibonacci Quarterly, 4 (3): 265–269, doi:10.1080/00150517.1966.12431364, MR 0208812
Press, WH; Teukolsky, SA; Vetterling, WT; Flannery, BP (2007), "Section 10.2. Golden Section Search in One Dimension", Numerical Recipes: The Art of Scientific Computing (3rd ed.), New York: Cambridge University Press, ISBN 978-0-521-88068-8, archived from the original on 2011-08-11, retrieved 2011-08-12

## Related Articles

### Internal Links

- [Absolute value](https://en.wikipedia.org/wiki/Absolute_value)
- [Active-set method](https://en.wikipedia.org/wiki/Active-set_method)
- [Affine scaling](https://en.wikipedia.org/wiki/Affine_scaling)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Approximation algorithm](https://en.wikipedia.org/wiki/Approximation_algorithm)
- [Augmented Lagrangian method](https://en.wikipedia.org/wiki/Augmented_Lagrangian_method)
- [Barrier function](https://en.wikipedia.org/wiki/Barrier_function)
- [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [Berndt–Hall–Hall–Hausman algorithm](https://en.wikipedia.org/wiki/Berndt%E2%80%93Hall%E2%80%93Hall%E2%80%93Hausman_algorithm)
- [Binary search](https://en.wikipedia.org/wiki/Binary_search)
- [Bisection method](https://en.wikipedia.org/wiki/Bisection_method)
- [Borůvka's algorithm](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)
- [Branch and bound](https://en.wikipedia.org/wiki/Branch_and_bound)
- [Branch and cut](https://en.wikipedia.org/wiki/Branch_and_cut)
- [Brent's method](https://en.wikipedia.org/wiki/Brent%27s_method)
- [Broyden–Fletcher–Goldfarb–Shanno algorithm](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)
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
- [Maximum and minimum](https://en.wikipedia.org/wiki/Maximum_and_minimum)
- [Fibonacci Quarterly](https://en.wikipedia.org/wiki/Fibonacci_Quarterly)
- [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
- [Fibonacci search technique](https://en.wikipedia.org/wiki/Fibonacci_search_technique)
- [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
- [Flow network](https://en.wikipedia.org/wiki/Flow_network)
- [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)
- [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [Gauss–Newton algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm)
- [Golden angle](https://en.wikipedia.org/wiki/Golden_angle)
- [Golden ratio](https://en.wikipedia.org/wiki/Golden_ratio)
- [Golden ratio base](https://en.wikipedia.org/wiki/Golden_ratio_base)
- [Golden rectangle](https://en.wikipedia.org/wiki/Golden_rectangle)
- [Golden rhombus](https://en.wikipedia.org/wiki/Golden_rhombus)
- [Golden spiral](https://en.wikipedia.org/wiki/Golden_spiral)
- [Golden triangle (mathematics)](https://en.wikipedia.org/wiki/Golden_triangle_(mathematics))
- [Gradient](https://en.wikipedia.org/wiki/Gradient)
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
- [List of algorithms](https://en.wikipedia.org/wiki/List_of_algorithms)
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix)
- [Heuristic (computer science)](https://en.wikipedia.org/wiki/Heuristic_(computer_science))
- [Hill climbing](https://en.wikipedia.org/wiki/Hill_climbing)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Integer programming](https://en.wikipedia.org/wiki/Integer_programming)
- [Iterative method](https://en.wikipedia.org/wiki/Iterative_method)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Jack Kiefer (statistician)](https://en.wikipedia.org/wiki/Jack_Kiefer_(statistician))
- [Jack Kiefer (statistician)](https://en.wikipedia.org/wiki/Jack_Kiefer_(statistician))
- [Karmarkar's algorithm](https://en.wikipedia.org/wiki/Karmarkar%27s_algorithm)
- [Kepler triangle](https://en.wikipedia.org/wiki/Kepler_triangle)
- [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [Lemke's algorithm](https://en.wikipedia.org/wiki/Lemke%27s_algorithm)
- [Levenberg–Marquardt algorithm](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm)
- [Limited-memory BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS)
- [Line search](https://en.wikipedia.org/wiki/Line_search)
- [Linear programming](https://en.wikipedia.org/wiki/Linear_programming)
- [Local convergence](https://en.wikipedia.org/wiki/Local_convergence)
- [Local search (optimization)](https://en.wikipedia.org/wiki/Local_search_(optimization))
- [Mathematical Reviews](https://en.wikipedia.org/wiki/Mathematical_Reviews)
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Matroid](https://en.wikipedia.org/wiki/Matroid)
- [Metaheuristic](https://en.wikipedia.org/wiki/Metaheuristic)
- [Metallic mean](https://en.wikipedia.org/wiki/Metallic_mean)
- [Minimax](https://en.wikipedia.org/wiki/Minimax)
- [Minimum spanning tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree)
- [Mirror descent](https://en.wikipedia.org/wiki/Mirror_descent)
- [Nelder–Mead method](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method)
- [Newton's method in optimization](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)
- [Nonlinear conjugate gradient method](https://en.wikipedia.org/wiki/Nonlinear_conjugate_gradient_method)
- [Nonlinear programming](https://en.wikipedia.org/wiki/Nonlinear_programming)
- [Numerical Recipes](https://en.wikipedia.org/wiki/Numerical_Recipes)
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Parallel metaheuristic](https://en.wikipedia.org/wiki/Parallel_metaheuristic)
- [Pell number](https://en.wikipedia.org/wiki/Pell_number)
- [Penalty method](https://en.wikipedia.org/wiki/Penalty_method)
- [Pisot–Vijayaraghavan number](https://en.wikipedia.org/wiki/Pisot%E2%80%93Vijayaraghavan_number)
- [Powell's dog leg method](https://en.wikipedia.org/wiki/Powell%27s_dog_leg_method)
- [Powell's method](https://en.wikipedia.org/wiki/Powell%27s_method)
- [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [Proceedings of the American Mathematical Society](https://en.wikipedia.org/wiki/Proceedings_of_the_American_Mathematical_Society)
- [Push–relabel maximum flow algorithm](https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm)
- [Quadratic programming](https://en.wikipedia.org/wiki/Quadratic_programming)
- [Quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method)
- [Revised simplex method](https://en.wikipedia.org/wiki/Revised_simplex_method)
- [Sequence](https://en.wikipedia.org/wiki/Sequence)
- [Sequential quadratic programming](https://en.wikipedia.org/wiki/Sequential_quadratic_programming)
- [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [Shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem)
- [Silver ratio](https://en.wikipedia.org/wiki/Silver_ratio)
- [Simplex algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm)
- [Simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Spiral optimization algorithm](https://en.wikipedia.org/wiki/Spiral_optimization_algorithm)
- [Subgradient method](https://en.wikipedia.org/wiki/Subgradient_method)
- [Successive linear programming](https://en.wikipedia.org/wiki/Successive_linear_programming)
- [Successive parabolic interpolation](https://en.wikipedia.org/wiki/Successive_parabolic_interpolation)
- [Supergolden ratio](https://en.wikipedia.org/wiki/Supergolden_ratio)
- [Supersilver ratio](https://en.wikipedia.org/wiki/Supersilver_ratio)
- [Symmetric rank-one](https://en.wikipedia.org/wiki/Symmetric_rank-one)
- [Tabu search](https://en.wikipedia.org/wiki/Tabu_search)
- [Ternary search](https://en.wikipedia.org/wiki/Ternary_search)
- [Truncated Newton method](https://en.wikipedia.org/wiki/Truncated_Newton_method)
- [Trust region](https://en.wikipedia.org/wiki/Trust_region)
- [Unimodality](https://en.wikipedia.org/wiki/Unimodality)
- [Wolfe conditions](https://en.wikipedia.org/wiki/Wolfe_conditions)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:External links](https://en.wikipedia.org/wiki/Wikipedia:External_links)
- [Wikipedia:Further reading](https://en.wikipedia.org/wiki/Wikipedia:Further_reading)
- [Wikipedia:When to cite](https://en.wikipedia.org/wiki/Wikipedia:When_to_cite)
- [Wikipedia:WikiProject Reliability](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Reliability)
- [Template:Metallic ratios](https://en.wikipedia.org/wiki/Template:Metallic_ratios)
- [Template:Optimization algorithms](https://en.wikipedia.org/wiki/Template:Optimization_algorithms)
- [Template talk:Metallic ratios](https://en.wikipedia.org/wiki/Template_talk:Metallic_ratios)
- [Template talk:Optimization algorithms](https://en.wikipedia.org/wiki/Template_talk:Optimization_algorithms)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles lacking in-text citations from June 2024](https://en.wikipedia.org/wiki/Category:Articles_lacking_in-text_citations_from_June_2024)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:26:53.002692+00:00_