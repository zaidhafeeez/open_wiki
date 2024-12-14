# Trial division

## Article Metadata

- **Last Updated:** 2024-12-14T19:46:23.989856+00:00
- **Original Article:** [Trial division](https://en.wikipedia.org/wiki/Trial_division)
- **Language:** en
- **Page ID:** 557660

## Summary

Trial division is the most laborious but easiest to understand of the integer factorization algorithms.  The essential idea behind trial division tests to see if an integer n, the integer to be factored, can be divided by each number in turn that is less than the square root of n. 
For example, to find the prime factors of n = 70, one can try to divide 70 by successive primes: first, 70 / 2 = 35; next, neither 2 nor 3 evenly divides 35; finally, 35 / 5 = 7, and 7 is itself prime. So 70 = 2 × 5 ×

## Categories

- Category:All articles lacking in-text citations
- Category:Articles lacking in-text citations from March 2014
- Category:Articles with Portuguese-language sources (pt)
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Division (mathematics)
- Category:Integer factorization algorithms
- Category:Short description is different from Wikidata

## Table of Contents

- Method
- Speed
- References
- External links

## Content

Trial division is the most laborious but easiest to understand of the integer factorization algorithms.  The essential idea behind trial division tests to see if an integer n, the integer to be factored, can be divided by each number in turn that is less than the square root of n. 
For example, to find the prime factors of n = 70, one can try to divide 70 by successive primes: first, 70 / 2 = 35; next, neither 2 nor 3 evenly divides 35; finally, 35 / 5 = 7, and 7 is itself prime. So 70 = 2 × 5 × 7.
Trial division was first described by Fibonacci in his book Liber Abaci (1202).

Method
Given an integer n (n refers to "the integer to be factored"), the trial division consists of systematically testing whether n is divisible by any smaller number. Clearly, it is only worthwhile to test candidate factors less than n, and in order from two upwards because an arbitrary n is more likely to be divisible by two than by three, and so on. With this ordering, there is no point in testing for divisibility by four if the number has already been determined not divisible by two, and so on for three and any multiple of three, etc.  Therefore, the effort can be reduced by selecting only prime numbers as candidate factors. Furthermore, the trial factors need go no further than 
  
    
      
        
          
            
              n
            
          
        
      
    
    {\displaystyle \scriptstyle {\sqrt {n}}}
  
 because, if n is divisible by some number p, then n = p × q and if q were smaller than p, n would have been detected earlier as being divisible by q or by a prime factor of q.
A definite bound on the prime factors is possible. Suppose Pi is the i'th prime, so that P1 = 2, P2 = 3, P3 = 5, etc. Then the last prime number worth testing as a possible factor of n is Pi where P2i + 1 > n; equality here would mean that Pi + 1 is a factor. Thus, testing with 2, 3, and 5 suffices up to n = 48 not just 25 because the square of the next prime is 49, and below n = 25 just 2 and 3 are sufficient. Should the square root of n be an integer, then it is a factor and n is a perfect square.
An example of the trial division algorithm, using successive integers as trial factors, is as follows (in Python):

This version tests every integer up to the square root of n, not just primes. A more complicated implementation only testing primes would be significantly faster in the worst case.

Speed
In the worst case, trial division is a laborious algorithm. For a base-2 n digit number a, if it starts from two and works up only to the square root of a, the algorithm requires

  
    
      
        π
        (
        
          2
          
            n
            
              /
            
            2
          
        
        )
        ≈
        
          
            
              2
              
                n
                
                  /
                
                2
              
            
            
              
                (
                
                  
                    n
                    2
                  
                
                )
              
              ln
              ⁡
              2
            
          
        
      
    
    {\displaystyle \pi (2^{n/2})\approx {2^{n/2} \over \left({\frac {n}{2}}\right)\ln 2}}
  

trial divisions, where 
  
    
      
        π
        (
        x
        )
      
    
    {\displaystyle \pi (x)}
  
 denotes the prime-counting function, the number of primes less than x. This does not take into account the overhead of primality testing to obtain the prime numbers as candidate factors. A useful table need not be large: P(3512) = 32749, the last prime that fits into a sixteen-bit signed integer and P(6542) = 65521 for unsigned sixteen-bit integers. That would suffice to test primality for numbers up to 655372 = 4,295,098,369. Preparing such a table (usually via the Sieve of Eratosthenes) would only be worthwhile if many numbers were to be tested. If instead a variant is used without primality testing, but simply dividing by every odd number less than the square root the base-2 n digit number a, prime or not, it can take up to about:

  
    
      
        
          2
          
            n
            
              /
            
            2
          
        
      
    
    {\displaystyle 2^{n/2}}
  

In both cases, the required time grows exponentially with the digits of the number.
Even so, this is a quite satisfactory method, considering that even the best-known algorithms have exponential time growth. For a chosen uniformly at random from integers of a given length, there is a 50% chance that 2 is a factor of a and a 33% chance that 3 is a factor of a, and so on. It can be shown that 88% of all positive integers have a factor under 100 and that 92% have a factor under 1000. Thus, when confronted by an arbitrary large a, it is worthwhile to check for divisibility by the small primes, since for 
  
    
      
        a
        =
        1000
      
    
    {\displaystyle a=1000}
  
, in base-2 
  
    
      
        n
        =
        10
      
    
    {\displaystyle n=10}
  
.
However, many-digit numbers that do not have factors in the small primes can require days or months to factor with the trial division. In such cases other methods are used such as the quadratic sieve and the general number field sieve (GNFS). Because these methods also have superpolynomial time growth a practical limit of n digits is reached very quickly. For this reason, in public key cryptography, values for a are chosen to have large prime factors of similar size so that they cannot be factored by any publicly known method in a useful time period on any available computer system or computer cluster such as supercomputers and computer grids. The largest cryptography-grade number that has been factored is RSA-250, a 250-digit number, using the GNFS and resources of several supercomputers. The running time was 2700 core years.

References
Childs, Lindsay N. (2009). A concrete introduction to higher algebra. Undergraduate Texts in Mathematics (3rd ed.). New York, NY: Springer-Verlag. ISBN 978-0-387-74527-5. Zbl 1165.00002.
Crandall, Richard; Pomerance, Carl (2005). Prime numbers. A computational perspective (2nd ed.). New York, NY: Springer-Verlag. ISBN 0-387-25282-7. Zbl 1088.11001.

External links
Wikiversity offers a lesson on prime factorization using trial division with Python.
Fast JavaScript Prime Factor Calculator using trial division. Can handle numbers up to about 253
Trial Division in Java, C and JavaScript (in Portuguese)

## Related Articles

### Internal Links

- [AKS primality test](https://en.wikipedia.org/wiki/AKS_primality_test)
- [Adleman–Pomerance–Rumely primality test](https://en.wikipedia.org/wiki/Adleman%E2%80%93Pomerance%E2%80%93Rumely_primality_test)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Ancient Egyptian multiplication](https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication)
- [Baby-step giant-step](https://en.wikipedia.org/wiki/Baby-step_giant-step)
- [Baillie–PSW primality test](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test)
- [Berlekamp–Rabin algorithm](https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Rabin_algorithm)
- [Binary GCD algorithm](https://en.wikipedia.org/wiki/Binary_GCD_algorithm)
- [Long division](https://en.wikipedia.org/wiki/Long_division)
- [Carl Pomerance](https://en.wikipedia.org/wiki/Carl_Pomerance)
- [Chakravala method](https://en.wikipedia.org/wiki/Chakravala_method)
- [Chunking (division)](https://en.wikipedia.org/wiki/Chunking_(division))
- [Cipolla's algorithm](https://en.wikipedia.org/wiki/Cipolla%27s_algorithm)
- [Continued fraction factorization](https://en.wikipedia.org/wiki/Continued_fraction_factorization)
- [Cornacchia's algorithm](https://en.wikipedia.org/wiki/Cornacchia%27s_algorithm)
- [Discrete logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm)
- [Division algorithm](https://en.wikipedia.org/wiki/Division_algorithm)
- [Dixon's factorization method](https://en.wikipedia.org/wiki/Dixon%27s_factorization_method)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Elliptic curve primality](https://en.wikipedia.org/wiki/Elliptic_curve_primality)
- [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Euclidean division](https://en.wikipedia.org/wiki/Euclidean_division)
- [Euler's factorization method](https://en.wikipedia.org/wiki/Euler%27s_factorization_method)
- [Exponentiation by squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring)
- [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
- [Fermat's factorization method](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method)
- [Fermat primality test](https://en.wikipedia.org/wiki/Fermat_primality_test)
- [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci)
- [Fourier division](https://en.wikipedia.org/wiki/Fourier_division)
- [Function field sieve](https://en.wikipedia.org/wiki/Function_field_sieve)
- [Multiplication algorithm](https://en.wikipedia.org/wiki/Multiplication_algorithm)
- [General number field sieve](https://en.wikipedia.org/wiki/General_number_field_sieve)
- [Generation of primes](https://en.wikipedia.org/wiki/Generation_of_primes)
- [Division algorithm](https://en.wikipedia.org/wiki/Division_algorithm)
- [Greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor)
- [Grid computing](https://en.wikipedia.org/wiki/Grid_computing)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Index calculus algorithm](https://en.wikipedia.org/wiki/Index_calculus_algorithm)
- [Integer factorization](https://en.wikipedia.org/wiki/Integer_factorization)
- [Integer relation algorithm](https://en.wikipedia.org/wiki/Integer_relation_algorithm)
- [Integer square root](https://en.wikipedia.org/wiki/Integer_square_root)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Judges of the International Criminal Court](https://en.wikipedia.org/wiki/Judges_of_the_International_Criminal_Court)
- [Karatsuba algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
- [Korkine–Zolotarev lattice basis reduction algorithm](https://en.wikipedia.org/wiki/Korkine%E2%80%93Zolotarev_lattice_basis_reduction_algorithm)
- [Kunerth's algorithm](https://en.wikipedia.org/wiki/Kunerth%27s_algorithm)
- [Lehmer's GCD algorithm](https://en.wikipedia.org/wiki/Lehmer%27s_GCD_algorithm)
- [Lenstra elliptic-curve factorization](https://en.wikipedia.org/wiki/Lenstra_elliptic-curve_factorization)
- [Lenstra–Lenstra–Lovász lattice basis reduction algorithm](https://en.wikipedia.org/wiki/Lenstra%E2%80%93Lenstra%E2%80%93Lov%C3%A1sz_lattice_basis_reduction_algorithm)
- [Liber Abaci](https://en.wikipedia.org/wiki/Liber_Abaci)
- [Long division](https://en.wikipedia.org/wiki/Long_division)
- [Multiplication algorithm](https://en.wikipedia.org/wiki/Multiplication_algorithm)
- [Lucas primality test](https://en.wikipedia.org/wiki/Lucas_primality_test)
- [Lucas–Lehmer primality test](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test)
- [Lucas–Lehmer–Riesel test](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer%E2%80%93Riesel_test)
- [Mathematical Reviews](https://en.wikipedia.org/wiki/Mathematical_Reviews)
- [Miller–Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [Modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation)
- [Montgomery modular multiplication](https://en.wikipedia.org/wiki/Montgomery_modular_multiplication)
- [Multiplication algorithm](https://en.wikipedia.org/wiki/Multiplication_algorithm)
- [Division algorithm](https://en.wikipedia.org/wiki/Division_algorithm)
- [Number theory](https://en.wikipedia.org/wiki/Number_theory)
- [Pocklington's algorithm](https://en.wikipedia.org/wiki/Pocklington%27s_algorithm)
- [Pocklington primality test](https://en.wikipedia.org/wiki/Pocklington_primality_test)
- [Pohlig–Hellman algorithm](https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm)
- [Pollard's kangaroo algorithm](https://en.wikipedia.org/wiki/Pollard%27s_kangaroo_algorithm)
- [Pollard's p − 1 algorithm](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm)
- [Pollard's rho algorithm](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm)
- [Pollard's rho algorithm for logarithms](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm_for_logarithms)
- [Primality test](https://en.wikipedia.org/wiki/Primality_test)
- [Primality test](https://en.wikipedia.org/wiki/Primality_test)
- [Prime-counting function](https://en.wikipedia.org/wiki/Prime-counting_function)
- [Prime number](https://en.wikipedia.org/wiki/Prime_number)
- [Proth's theorem](https://en.wikipedia.org/wiki/Proth%27s_theorem)
- [Public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Pépin's test](https://en.wikipedia.org/wiki/P%C3%A9pin%27s_test)
- [Quadratic Frobenius test](https://en.wikipedia.org/wiki/Quadratic_Frobenius_test)
- [Quadratic residue](https://en.wikipedia.org/wiki/Quadratic_residue)
- [Quadratic sieve](https://en.wikipedia.org/wiki/Quadratic_sieve)
- [RSA numbers](https://en.wikipedia.org/wiki/RSA_numbers)
- [Rational sieve](https://en.wikipedia.org/wiki/Rational_sieve)
- [Richard Crandall](https://en.wikipedia.org/wiki/Richard_Crandall)
- [Division algorithm](https://en.wikipedia.org/wiki/Division_algorithm)
- [Schoof's algorithm](https://en.wikipedia.org/wiki/Schoof%27s_algorithm)
- [Schönhage–Strassen algorithm](https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm)
- [Shanks's square forms factorization](https://en.wikipedia.org/wiki/Shanks%27s_square_forms_factorization)
- [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm)
- [Short division](https://en.wikipedia.org/wiki/Short_division)
- [Sieve of Atkin](https://en.wikipedia.org/wiki/Sieve_of_Atkin)
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [Sieve of Pritchard](https://en.wikipedia.org/wiki/Sieve_of_Pritchard)
- [Sieve of Sundaram](https://en.wikipedia.org/wiki/Sieve_of_Sundaram)
- [Solovay–Strassen primality test](https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test)
- [Special number field sieve](https://en.wikipedia.org/wiki/Special_number_field_sieve)
- [Springer Science+Business Media](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Square number](https://en.wikipedia.org/wiki/Square_number)
- [Square root](https://en.wikipedia.org/wiki/Square_root)
- [Supercomputer](https://en.wikipedia.org/wiki/Supercomputer)
- [Tonelli–Shanks algorithm](https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm)
- [Toom–Cook multiplication](https://en.wikipedia.org/wiki/Toom%E2%80%93Cook_multiplication)
- [Trachtenberg system](https://en.wikipedia.org/wiki/Trachtenberg_system)
- [Undergraduate Texts in Mathematics](https://en.wikipedia.org/wiki/Undergraduate_Texts_in_Mathematics)
- [Wheel factorization](https://en.wikipedia.org/wiki/Wheel_factorization)
- [Williams's p + 1 algorithm](https://en.wikipedia.org/wiki/Williams%27s_p_%2B_1_algorithm)
- [Best, worst and average case](https://en.wikipedia.org/wiki/Best,_worst_and_average_case)
- [ZbMATH Open](https://en.wikipedia.org/wiki/ZbMATH_Open)
- [Wikipedia:Citing sources](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)
- [Wikipedia:External links](https://en.wikipedia.org/wiki/Wikipedia:External_links)
- [Wikipedia:Further reading](https://en.wikipedia.org/wiki/Wikipedia:Further_reading)
- [Wikipedia:When to cite](https://en.wikipedia.org/wiki/Wikipedia:When_to_cite)
- [Wikipedia:WikiProject Reliability](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Reliability)
- [Template:Number-theoretic algorithms](https://en.wikipedia.org/wiki/Template:Number-theoretic_algorithms)
- [Template talk:Number-theoretic algorithms](https://en.wikipedia.org/wiki/Template_talk:Number-theoretic_algorithms)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles lacking in-text citations from March 2014](https://en.wikipedia.org/wiki/Category:Articles_lacking_in-text_citations_from_March_2014)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:46:23.989856+00:00_