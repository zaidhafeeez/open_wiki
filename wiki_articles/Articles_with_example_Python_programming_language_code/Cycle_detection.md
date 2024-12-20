---
title: Cycle detection
url: https://en.wikipedia.org/wiki/Cycle_detection
language: en
categories: ["Category:All articles that are too technical", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Combinatorial algorithms", "Category:Fixed points (mathematics)", "Category:Short description matches Wikidata", "Category:The Tortoise and the Hare", "Category:Wikipedia articles that are too technical from February 2018"]
references: 0
last_modified: 2024-12-19T13:45:09Z
---

# Cycle detection

## Summary

In computer science, cycle detection or cycle finding is the algorithmic problem of finding a cycle in a sequence of iterated function values.
For any function f that maps a finite set S to itself, and any initial value x0 in S, the sequence of iterated function values

  
    
      
        
          x
          
            0
          
        
        ,
         
        
          x
          
            1
          
        
        =
        f
        (
        
          x
          


## Full Content

In computer science, cycle detection or cycle finding is the algorithmic problem of finding a cycle in a sequence of iterated function values.
For any function f that maps a finite set S to itself, and any initial value x0 in S, the sequence of iterated function values

  
    
      
        
          x
          
            0
          
        
        ,
         
        
          x
          
            1
          
        
        =
        f
        (
        
          x
          
            0
          
        
        )
        ,
         
        
          x
          
            2
          
        
        =
        f
        (
        
          x
          
            1
          
        
        )
        ,
         
        …
        ,
         
        
          x
          
            i
          
        
        =
        f
        (
        
          x
          
            i
            −
            1
          
        
        )
        ,
         
        …
      
    
    {\displaystyle x_{0},\ x_{1}=f(x_{0}),\ x_{2}=f(x_{1}),\ \dots ,\ x_{i}=f(x_{i-1}),\ \dots }
  

must eventually use the same value twice: there must be some pair of distinct indices i and j such that xi = xj. Once this happens, the sequence must continue periodically, by repeating the same sequence of values from xi to xj − 1. Cycle detection is the problem of finding i and j, given f and x0.
Several algorithms are known for finding cycles quickly and with little memory. Robert W. Floyd's tortoise and hare algorithm moves two pointers at different speeds through the sequence of values until they both point to equal values. Alternatively, Brent's algorithm is based on the idea of exponential search. Both Floyd's and Brent's algorithms use only a constant number of memory cells, and take a number of function evaluations that is proportional to the distance from the start of the sequence to the first repetition. Several other algorithms trade off larger amounts of memory for fewer function evaluations.
The applications of cycle detection include testing the quality of pseudorandom number generators and cryptographic hash functions, computational number theory algorithms, detection of infinite loops in computer programs and periodic configurations in cellular automata,  automated shape analysis of linked list data structures, and detection of deadlocks for transactions management in DBMS.

Example
The figure shows a function f that maps the set S = {0,1,2,3,4,5,6,7,8} to itself. If one starts from x0 = 2 and repeatedly applies f, one sees the sequence of values

2, 0, 6, 3, 1, 6, 3, 1, 6, 3, 1, ....
The cycle in this value sequence is 6, 3, 1.

Definitions
Let S be any finite set, f be any endofunction from S to itself, and x0 be any element of S. For any i > 0, let xi = f(xi − 1). Let μ be the smallest index such that the value xμ reappears infinitely often within the sequence of values xi, and let λ (the loop length) be the smallest positive integer such that xμ = xλ + μ. The cycle detection problem is the task of finding λ and μ.
One can view the same problem graph-theoretically, by constructing a functional graph (that is, a directed graph in which each vertex has a single outgoing edge) the vertices of which are the elements of S and the edges of which map an element to the corresponding function value, as shown in the figure. The set of vertices reachable from  starting vertex x0 form a subgraph with a shape resembling the Greek letter rho (ρ): a path of length μ from x0 to a cycle of λ vertices.
Practical cycle-detection algorithms do not find λ and μ exactly.  They usually find lower and upper bounds μl ≤ μ ≤ μh for the start of the cycle, and a more detailed search of the range must be performed if the exact value of μ is needed.  Also, most algorithms do not guarantee to find λ directly, but may find some multiple kλ < μ + λ.  (Continuing the search for an additional kλ/q steps, where q is the smallest prime divisor of kλ, will either find the true λ or prove that k = 1.)

Computer representation
Except in toy examples like the above, f will not be specified as a table of values.  Such a table implies O(|S|) space complexity, and if that is permissible, an associative array mapping xi to i will detect the first repeated value.  Rather, a cycle detection algorithm is given a black box for generating the sequence xi, and the task is to find λ and μ using very little memory.
The black box might consist of an implementation of the recurrence function f, but it might also store additional internal state to make the computation more efficient.  Although xi = f(xi−1) must be true in principle, this might be expensive to compute directly; the function could be defined in terms of the discrete logarithm of xi−1 or some other difficult-to-compute property which can only be practically computed in terms of additional information.  In such cases, the number of black boxes required becomes a figure of merit distinguishing the algorithms.
A second reason to use one of these algorithms is that they are pointer algorithms which do no operations on elements of S other than testing for equality.  An associative array implementation requires computing a hash function on the elements of S, or ordering them.  But cycle detection can be applied in cases where neither of these are possible.
The classic example is Pollard's rho algorithm for integer factorization, which searches for a factor p of a given number n by looking for values xi and xi+λ which are equal modulo p without knowing p in advance.  This is done by computing the greatest common divisor of the difference xi − xi+λ with a known multiple of p, namely n.  If the gcd is non-trivial (neither 1 nor n), then the value is a proper factor of n, as desired.  If n is not prime, it must have at least one factor p ≤ √n, and by the birthday paradox, a random function f has an expected cycle length (modulo p) of √p ≤ 4√n.

Algorithms
If the input is given as a subroutine for calculating f, the cycle detection problem may be trivially solved using only λ + μ function applications, simply by computing the sequence of values xi and using a data structure such as a hash table to store these values and test whether each subsequent value has already been stored. However, the space complexity of this algorithm is proportional to λ + μ, unnecessarily large. Additionally, to implement this method as a pointer algorithm would require applying the equality test to each pair of values, resulting in quadratic time overall. Thus, research in this area has concentrated on two goals: using less space than this naive algorithm, and finding pointer algorithms that use fewer equality tests.

Floyd's tortoise and hare
Floyd's cycle-finding algorithm is a pointer algorithm that uses only two pointers, which move through the sequence at different speeds. It is also called the "tortoise and the hare algorithm", alluding to Aesop's fable of The Tortoise and the Hare.
The algorithm is named after Robert W. Floyd, who was credited with its invention by Donald Knuth. However, the algorithm does not appear in Floyd's published work, and this may be a misattribution: Floyd describes algorithms for listing all simple cycles in a directed graph in a 1967 paper, but this paper does not describe the cycle-finding problem in functional graphs that is the subject of this article. In fact, Knuth's statement (in 1969), attributing it to Floyd, without citation, is the first known appearance in print, and it thus may be a folk theorem, not attributable to a single individual.
The key insight in the algorithm is as follows. If there is a cycle, then, for any integers i ≥ μ and k ≥ 0, xi = xi + kλ, where λ is the length of the loop to be found, μ is the index of the first element of the cycle, and k is a whole integer representing the number of loops. Based on this, it can then be shown that i = kλ ≥ μ for some k if and only if xi = x2i (if xi = x2i in the cycle, then there exists some k such that 2i = i + kλ, which implies that i = kλ; and if there are some i and k such that i = kλ, then 2i = i + kλ and x2i = xi + kλ).  Thus, the algorithm only needs to check for repeated values of this special form, one twice as far from the start of the sequence as the other, to find a period ν of a repetition that is a multiple of λ. Once ν is found, the algorithm retraces the sequence from its start to find the first repeated value xμ in the sequence, using the fact that λ divides ν and therefore that xμ = xμ + v.  Finally, once the value of μ is known it is trivial to find the length λ of the shortest repeating cycle, by searching for the first position μ + λ for which xμ + λ = xμ.
The algorithm thus maintains two pointers into the given sequence, one (the tortoise) at xi, and the other (the hare) at x2i. At each step of the algorithm, it increases i by one, moving the tortoise one step forward and the hare two steps forward in the sequence, and then compares the sequence values at these two pointers. The smallest value of i > 0 for which the tortoise and hare point to equal values is the desired value ν.
The following Python code shows how this idea may be implemented as an algorithm.

This code only accesses the sequence by storing and copying pointers, function evaluations, and equality tests; therefore, it qualifies as a pointer algorithm. The algorithm uses O(λ + μ) operations of these types, and O(1) storage space.

Brent's algorithm
Richard P. Brent described an alternative cycle detection algorithm that, like the tortoise and hare algorithm, requires only two pointers into the sequence. However, it is based on a different principle: searching for the smallest power of two 2i that is larger than both λ and μ. For i = 0, 1, 2, ..., the algorithm compares x2i−1 with each subsequent sequence value up to the next power of two, stopping when it finds a match. It has two advantages compared to the tortoise and hare algorithm: it finds the correct length λ of the cycle directly, rather than needing to search for it in a subsequent stage, and its steps involve only one evaluation of the function f rather than three.
The following Python code shows how this technique works in more detail.

Like the tortoise and hare algorithm, this is a pointer algorithm that uses O(λ + μ) tests and function evaluations and O(1) storage space. It is not difficult to show that the number of function evaluations can never be higher than for Floyd's algorithm. Brent claims that, on average, his cycle finding algorithm runs around 36% more quickly than Floyd's and that it speeds up the Pollard rho algorithm by around 24%. He also performs an average case analysis for a randomized version of the algorithm in which the sequence of indices traced by the slower of the two pointers is not the powers of two themselves, but rather a randomized multiple of the powers of two. Although his main intended application was in integer factorization algorithms, Brent also discusses applications in testing pseudorandom number generators.

Gosper's algorithm
R. W. Gosper's algorithm finds the period 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
, and the lower and upper bound of the starting point, 
  
    
      
        
          μ
          
            l
          
        
      
    
    {\displaystyle \mu _{l}}
  
 and 
  
    
      
        
          μ
          
            u
          
        
      
    
    {\displaystyle \mu _{u}}
  
, of the first cycle. The difference between the lower and upper bound is of the same order as the period, i.e. 
  
    
      
        
          μ
          
            l
          
        
        +
        λ
        ≈
        
          μ
          
            h
          
        
      
    
    {\displaystyle \mu _{l}+\lambda \approx \mu _{h}}
  
.
The algorithm maintains an array of tortoises 
  
    
      
        
          T
          
            j
          
        
      
    
    {\displaystyle T_{j}}
  
.  For each 
  
    
      
        
          x
          
            i
          
        
      
    
    {\displaystyle x_{i}}
  
:

For each 
  
    
      
        0
        ≤
        j
        ≤
        
          log
          
            2
          
        
        ⁡
        i
        ,
      
    
    {\displaystyle 0\leq j\leq \log _{2}i,}
  
 compare 
  
    
      
        
          x
          
            i
          
        
      
    
    {\displaystyle x_{i}}
  
 to 
  
    
      
        
          T
          
            j
          
        
      
    
    {\displaystyle T_{j}}
  
.
If 
  
    
      
        
          x
          
            i
          
        
        =
        
          T
          
            j
          
        
      
    
    {\displaystyle x_{i}=T_{j}}
  
, a cycle has been detected, of length 
  
    
      
        λ
        =
        (
        i
        −
        
          2
          
            j
          
        
        )
        
          
            mod
            
              2
            
          
          
            j
            +
            1
          
        
        +
        1.
      
    
    {\displaystyle \lambda =(i-2^{j}){\bmod {2}}^{j+1}+1.}
  

If no match is found, set 
  
    
      
        
          T
          
            k
          
        
        ←
        
          x
          
            i
          
        
      
    
    {\displaystyle T_{k}\leftarrow x_{i}}
  
, where 
  
    
      
        k
      
    
    {\displaystyle k}
  
 is the number of trailing zeros in the binary representation of 
  
    
      
        i
        +
        1
      
    
    {\displaystyle i+1}
  
.  I.e. the greatest power of 2 which divides 
  
    
      
        i
        +
        1
      
    
    {\displaystyle i+1}
  
.
If it is inconvenient to vary the number of comparisons as 
  
    
      
        i
      
    
    {\displaystyle i}
  
 increases, you may initialize all of the 
  
    
      
        
          T
          
            j
          
        
        =
        
          x
          
            0
          
        
      
    
    {\displaystyle T_{j}=x_{0}}
  
, but must then return 
  
    
      
        λ
        =
        i
      
    
    {\displaystyle \lambda =i}
  
 if 
  
    
      
        
          x
          
            i
          
        
        =
        
          T
          
            j
          
        
      
    
    {\displaystyle x_{i}=T_{j}}
  
 while 
  
    
      
        i
        <
        
          2
          
            j
          
        
      
    
    {\displaystyle i<2^{j}}
  
.

Advantages
The main features of Gosper's algorithm are that it is economical in space, very economical in evaluations of the generator function, and always finds the exact cycle length (never a multiple). The cost is a large number of equality comparisons.  It could be roughly described as a concurrent version of Brent's algorithm. While Brent's algorithm uses a single tortoise, repositioned every time the hare passes a power of two, Gosper's algorithm uses several tortoises (several previous values are saved), which are roughly exponentially spaced. According to the note in HAKMEM item 132, this algorithm will detect repetition before the third occurrence of any value, i.e. the cycle will be iterated at most twice. HAKMEM also states that it is sufficient to store 
  
    
      
        ⌈
        
          log
          
            2
          
        
        ⁡
        λ
        ⌉
      
    
    {\displaystyle \lceil \log _{2}\lambda \rceil }
  
 previous values; however, this only offers a saving if we know a priori that 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
 is significantly smaller than 
  
    
      
        μ
      
    
    {\displaystyle \mu }
  
.  The standard implementations store 
  
    
      
        ⌈
        
          log
          
            2
          
        
        ⁡
        (
        μ
        +
        2
        λ
        )
        ⌉
      
    
    {\displaystyle \lceil \log _{2}(\mu +2\lambda )\rceil }
  
 values. For example, assume the function values are 32-bit integers, so 
  
    
      
        μ
        +
        λ
        ≤
        
          2
          
            32
          
        
      
    
    {\displaystyle \mu +\lambda \leq 2^{32}}
  
 and 
  
    
      
        μ
        +
        2
        λ
        ≤
        
          2
          
            33
          
        
        .
      
    
    {\displaystyle \mu +2\lambda \leq 2^{33}.}
  
  Then Gosper's algorithm will find the cycle after less than 
  
    
      
        μ
        +
        2
        λ
      
    
    {\displaystyle \mu +2\lambda }
  
 function evaluations (in fact, the most possible is 
  
    
      
        3
        ⋅
        
          2
          
            31
          
        
        −
        1
      
    
    {\displaystyle 3\cdot 2^{31}-1}
  
), while consuming the space of 33 values (each value being a 32-bit integer).

Complexity
Upon the 
  
    
      
        i
      
    
    {\displaystyle i}
  
-th evaluation of the generator function, the algorithm compares the generated value with 
  
    
      
        
          log
          
            2
          
        
        ⁡
        i
      
    
    {\displaystyle \log _{2}i}
  
 previous values; observe that 
  
    
      
        i
      
    
    {\displaystyle i}
  
 goes up to at least 
  
    
      
        μ
        +
        λ
      
    
    {\displaystyle \mu +\lambda }
  
 and at most 
  
    
      
        μ
        +
        2
        λ
      
    
    {\displaystyle \mu +2\lambda }
  
. Therefore, the time complexity of this algorithm is 
  
    
      
        O
        (
        (
        μ
        +
        λ
        )
        ⋅
        log
        ⁡
        (
        μ
        +
        λ
        )
        )
      
    
    {\displaystyle O((\mu +\lambda )\cdot \log(\mu +\lambda ))}
  
. Since it stores 
  
    
      
        
          log
          
            2
          
        
        ⁡
        (
        μ
        +
        2
        λ
        )
      
    
    {\displaystyle \log _{2}(\mu +2\lambda )}
  
 values, its space complexity is 
  
    
      
        Θ
        (
        log
        ⁡
        (
        μ
        +
        λ
        )
        )
      
    
    {\displaystyle \Theta (\log(\mu +\lambda ))}
  
. This is under the usual transdichotomous model, assumed throughout this article, in which the size of the function values is constant. Without this assumption, we know it requires 
  
    
      
        Ω
        (
        log
        ⁡
        (
        μ
        +
        λ
        )
        )
      
    
    {\displaystyle \Omega (\log(\mu +\lambda ))}
  
 space to store 
  
    
      
        μ
        +
        λ
      
    
    {\displaystyle \mu +\lambda }
  
 distinct values, so the overall space complexity is 
  
    
      
        Ω
        (
        
          log
          
            2
          
        
        ⁡
        (
        μ
        +
        λ
        )
        )
        .
      
    
    {\displaystyle \Omega (\log ^{2}(\mu +\lambda )).}

Time–space tradeoffs
A number of authors have studied techniques for cycle detection that use more memory than Floyd's and Brent's methods, but detect cycles more quickly. In general these methods store several previously-computed sequence values, and test whether each new value equals one of the previously-computed values. In order to do so quickly, they typically use a hash table or similar data structure for storing the previously-computed values, and therefore are not pointer algorithms: in particular, they usually cannot be applied to Pollard's rho algorithm. Where these methods differ is in how they determine which values to store. Following Nivasch, we survey these techniques briefly.

Brent already describes variations of his technique in which the indices of saved sequence values are powers of a number R other than two. By choosing R to be a number close to one, and storing the sequence values at indices that are near a sequence of consecutive powers of R, a cycle detection algorithm can use a number of function evaluations that is within an arbitrarily small factor of the optimum λ + μ.
Sedgewick, Szymanski, and Yao  provide a method that uses M memory cells and requires in the worst case only 
  
    
      
        (
        λ
        +
        μ
        )
        (
        1
        +
        c
        
          M
          
            −
            1
            
              /
            
            2
          
        
        )
      
    
    {\displaystyle (\lambda +\mu )(1+cM^{-1/2})}
  
 function evaluations, for some constant c, which they show to be optimal. The technique involves maintaining a numerical parameter d, storing in a table only those positions in the sequence that are multiples of d, and clearing the table and doubling d whenever too many values have been stored.
Several authors have described distinguished point methods that store function values in a table based on a criterion involving the values, rather than (as in the method of Sedgewick et al.) based on their positions. For instance, values equal to zero modulo some value d might be stored. More simply, Nivasch credits D. P. Woodruff with the suggestion of storing a random sample of previously seen values, making an appropriate random choice at each step so that the sample remains random.
Nivasch describes an algorithm that does not use a fixed amount of memory, but for which the expected amount of memory used (under the assumption that the input function is random) is logarithmic in the sequence length. An item is stored in the memory table, with this technique, when no later item has a smaller value. As Nivasch shows, the items with this technique can be maintained using a stack data structure, and each successive sequence value need be compared only to the top of the stack. The algorithm terminates when the repeated sequence element with smallest value is found. Running the same algorithm with multiple stacks, using random permutations of the values to reorder the values within each stack, allows a time–space tradeoff similar to the previous algorithms. However, even the version of this algorithm with a single stack is not a pointer algorithm, due to the comparisons needed to determine which of two values is smaller.
Any cycle detection algorithm that stores at most M values from the input sequence must perform at least 
  
    
      
        (
        λ
        +
        μ
        )
        
          (
          
            1
            +
            
              
                1
                
                  M
                  −
                  1
                
              
            
          
          )
        
      
    
    {\displaystyle (\lambda +\mu )\left(1+{\frac {1}{M-1}}\right)}
  
 function evaluations.

Applications
Cycle detection has been used in many applications.

Determining the cycle length of a pseudorandom number generator is one measure of its strength. This is the application cited by Knuth in describing Floyd's method. Brent describes the results of testing a linear congruential generator in this fashion; its period turned out to be significantly smaller than advertised. For more complex generators, the sequence of values in which the cycle is to be found may not represent the output of the generator, but rather its internal state.
Several number-theoretic algorithms are based on cycle detection, including Pollard's rho algorithm for integer factorization and his related kangaroo algorithm for the discrete logarithm problem.
In cryptographic applications, the ability to find two distinct values xμ−1 and xλ+μ−1 mapped by some cryptographic function ƒ to the same value xμ may indicate a weakness in ƒ. For instance, Quisquater and Delescaille apply cycle detection algorithms in the search for a message and a pair of Data Encryption Standard keys that map that message to the same encrypted value; Kaliski, Rivest, and Sherman also use cycle detection algorithms to attack DES. The technique may also be used to find a collision in a cryptographic hash function.
Cycle detection may be helpful as a way of discovering infinite loops in certain types of computer programs.
Periodic configurations in cellular automaton simulations may be found by applying cycle detection algorithms to the sequence of automaton states.
Shape analysis of linked list data structures is a technique for verifying the correctness of an algorithm using those structures. If a node in the list incorrectly points to an earlier node in the same list, the structure will form a cycle that can be detected by these algorithms. In Common Lisp, the S-expression printer, under control of the *print-circle* variable, detects circular list structure and prints it compactly.
Teske describes applications in computational group theory: determining the structure of an Abelian group from a set of its generators. The cryptographic algorithms of Kaliski et al. may also be viewed as attempting to infer the structure of an unknown group.
Fich (1981) briefly mentions an application to computer simulation of celestial mechanics, which she attributes to William Kahan. In this application, cycle detection in the phase space of an orbital system may be used to determine whether the system is periodic to within the accuracy of the simulation.
In Mandelbrot Set fractal generation some performance techniques are used to speed up the image generation. One of them is called "period checking", which consists of finding the cycles in a point orbit. This article describes the "period checking" technique. You can find another explanation here. Some cycle detection algorithms have to be implemented in order to implement this technique.

References
External links
Gabriel Nivasch, The Cycle Detection Problem and the Stack Algorithm
Tortoise and Hare, Portland Pattern Repository
Floyd's Cycle Detection Algorithm (The Tortoise and the Hare)
Brent's Cycle Detection Algorithm (The Teleporting Turtle)
