# Perfect digit-to-digit invariant

## Article Metadata

- **Last Updated:** 2024-12-14T19:42:48.420139+00:00
- **Original Article:** [Perfect digit-to-digit invariant](https://en.wikipedia.org/wiki/Perfect_digit-to-digit_invariant)
- **Language:** en
- **Page ID:** 24356530

## Summary

In number theory, a perfect digit-to-digit invariant (PDDI; also known as a Munchausen number) is a natural number in a given number base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 that is equal to the sum of its digits each raised to the power of itself. An example in base 10 is 3435, because 
  
    
      
        3435
        =
        
          3
          
            3
          
        
        +
        
          4
          
            4
          
        
   

## Categories

- Category:Arithmetic dynamics
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Base-dependent integer sequences
- Category:Short description is different from Wikidata

## Table of Contents

- Definition
- Perfect digit-to-digit invariants and cycles of Fb for specific b
- Programming examples
- See also
- References
- External links

## Content

In number theory, a perfect digit-to-digit invariant (PDDI; also known as a Munchausen number) is a natural number in a given number base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 that is equal to the sum of its digits each raised to the power of itself. An example in base 10 is 3435, because 
  
    
      
        3435
        =
        
          3
          
            3
          
        
        +
        
          4
          
            4
          
        
        +
        
          3
          
            3
          
        
        +
        
          5
          
            5
          
        
      
    
    {\displaystyle 3435=3^{3}+4^{4}+3^{3}+5^{5}}
  
. The term "Munchausen number" was coined by Dutch mathematician and software engineer Daan van Berkel in 2009, as this evokes the story of Baron Munchausen raising himself up by his own ponytail because each digit is raised to the power of itself.

Definition
Let 
  
    
      
        n
      
    
    {\displaystyle n}
  
 be a natural number which can be written in base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 as the k-digit number 
  
    
      
        
          d
          
            k
            −
            1
          
        
        
          d
          
            k
            −
            2
          
        
        .
        .
        .
        
          d
          
            1
          
        
        
          d
          
            0
          
        
      
    
    {\displaystyle d_{k-1}d_{k-2}...d_{1}d_{0}}
  
 where each digit 
  
    
      
        
          d
          
            i
          
        
      
    
    {\displaystyle d_{i}}
  
 is between 
  
    
      
        0
      
    
    {\displaystyle 0}
  
 and 
  
    
      
        b
        −
        1
      
    
    {\displaystyle b-1}
  
 inclusive, and 
  
    
      
        n
        =
        
          ∑
          
            i
            =
            0
          
          
            k
            −
            1
          
        
        
          d
          
            i
          
        
        
          b
          
            i
          
        
      
    
    {\displaystyle n=\sum _{i=0}^{k-1}d_{i}b^{i}}
  
. We define the function 
  
    
      
        
          F
          
            b
          
        
        :
        
          N
        
        →
        
          N
        
      
    
    {\displaystyle F_{b}:\mathbb {N} \rightarrow \mathbb {N} }
  
 as 
  
    
      
        
          F
          
            b
          
        
        (
        n
        )
        =
        
          ∑
          
            i
            =
            0
          
          
            k
            −
            1
          
        
        
          
            
              d
              
                i
              
            
          
          
            
              d
              
                i
              
            
          
        
      
    
    {\displaystyle F_{b}(n)=\sum _{i=0}^{k-1}{d_{i}}^{d_{i}}}
  
. (As 00 is usually undefined, there are typically two conventions used, one where it is taken to be equal to one, and another where it is taken to be equal to zero.) A natural number 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is defined to be a perfect digit-to-digit invariant in base b if 
  
    
      
        
          F
          
            b
          
        
        (
        n
        )
        =
        n
      
    
    {\displaystyle F_{b}(n)=n}
  
. For example, the number 3435 is a perfect digit-to-digit invariant in base 10 because 
  
    
      
        
          3
          
            3
          
        
        +
        
          4
          
            4
          
        
        +
        
          3
          
            3
          
        
        +
        
          5
          
            5
          
        
        =
        27
        +
        256
        +
        27
        +
        3125
        =
        3435
      
    
    {\displaystyle 3^{3}+4^{4}+3^{3}+5^{5}=27+256+27+3125=3435}
  
. 

  
    
      
        
          F
          
            b
          
        
        (
        1
        )
        =
        1
      
    
    {\displaystyle F_{b}(1)=1}
  
 for all 
  
    
      
        b
      
    
    {\displaystyle b}
  
, and thus 1 is a trivial perfect digit-to-digit invariant in all bases, and all other perfect digit-to-digit invariants are nontrivial. For the second convention where 
  
    
      
        
          0
          
            0
          
        
        =
        0
      
    
    {\displaystyle 0^{0}=0}
  
, both 
  
    
      
        0
      
    
    {\displaystyle 0}
  
 and 
  
    
      
        1
      
    
    {\displaystyle 1}
  
 are trivial perfect digit-to-digit invariants.
A natural number 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is a sociable digit-to-digit invariant if it is a periodic point for 
  
    
      
        
          F
          
            b
          
        
      
    
    {\displaystyle F_{b}}
  
, where 
  
    
      
        
          F
          
            b
          
          
            k
          
        
        (
        n
        )
        =
        n
      
    
    {\displaystyle F_{b}^{k}(n)=n}
  
 for a positive integer 
  
    
      
        k
      
    
    {\displaystyle k}
  
, and forms a cycle of period 
  
    
      
        k
      
    
    {\displaystyle k}
  
. A perfect digit-to-digit invariant is a sociable digit-to-digit invariant with 
  
    
      
        k
        =
        1
      
    
    {\displaystyle k=1}
  
. An amicable digit-to-digit invariant is a sociable digit-to-digit invariant with 
  
    
      
        k
        =
        2
      
    
    {\displaystyle k=2}
  
.
All natural numbers 
  
    
      
        n
      
    
    {\displaystyle n}
  
 are preperiodic points for 
  
    
      
        
          F
          
            b
          
        
      
    
    {\displaystyle F_{b}}
  
, regardless of the base. This is because all natural numbers of base 
  
    
      
        b
      
    
    {\displaystyle b}
  
 with 
  
    
      
        k
      
    
    {\displaystyle k}
  
 digits satisfy 
  
    
      
        
          b
          
            k
            −
            1
          
        
        ≤
        n
        ≤
        (
        k
        )
        
          
            (
            b
            −
            1
            )
          
          
            b
            −
            1
          
        
      
    
    {\displaystyle b^{k-1}\leq n\leq (k){(b-1)}^{b-1}}
  
. However, when 
  
    
      
        k
        ≥
        b
        +
        1
      
    
    {\displaystyle k\geq b+1}
  
, then 
  
    
      
        
          b
          
            k
            −
            1
          
        
        >
        (
        k
        )
        
          
            (
            b
            −
            1
            )
          
          
            b
            −
            1
          
        
      
    
    {\displaystyle b^{k-1}>(k){(b-1)}^{b-1}}
  
, so any 
  
    
      
        n
      
    
    {\displaystyle n}
  
 will satisfy 
  
    
      
        n
        >
        
          F
          
            b
          
        
        (
        n
        )
      
    
    {\displaystyle n>F_{b}(n)}
  
 until 
  
    
      
        n
        <
        
          b
          
            b
            +
            1
          
        
      
    
    {\displaystyle n<b^{b+1}}
  
. There are a finite number of natural numbers less than 
  
    
      
        
          b
          
            b
            +
            1
          
        
      
    
    {\displaystyle b^{b+1}}
  
, so the number is guaranteed to reach a periodic point or a fixed point less than 
  
    
      
        
          b
          
            b
            +
            1
          
        
      
    
    {\displaystyle b^{b+1}}
  
, making it a preperiodic point. This means also that there are a finite number of perfect digit-to-digit invariant and cycles for any given base 
  
    
      
        b
      
    
    {\displaystyle b}
  
.
The number of iterations 
  
    
      
        i
      
    
    {\displaystyle i}
  
 needed for 
  
    
      
        
          F
          
            b
          
          
            i
          
        
        (
        n
        )
      
    
    {\displaystyle F_{b}^{i}(n)}
  
 to reach a fixed point is the 
  
    
      
        b
      
    
    {\displaystyle b}
  
-factorion function's persistence of 
  
    
      
        n
      
    
    {\displaystyle n}
  
, and undefined if it never reaches a fixed point.

Perfect digit-to-digit invariants and cycles of Fb for specific b
All numbers are represented in base 
  
    
      
        b
      
    
    {\displaystyle b}
  
.

Convention 00 = 1
Convention 00 = 0
Programming examples
The following program in Python determines whether an integer number is a Munchausen Number / Perfect Digit to Digit Invariant or not, following the convention 
  
    
      
        
          0
          
            0
          
        
        =
        1
      
    
    {\displaystyle 0^{0}=1}
  
.

The examples below implement the perfect digit-to-digit invariant function described in the definition above to search for perfect digit-to-digit invariants and cycles in Python for the two conventions.

Convention 00 = 1
Convention 00 = 0
See also
Arithmetic dynamics
Dudeney number
Factorion
Happy number
Kaprekar's constant
Kaprekar number
Meertens number
Narcissistic number
Perfect digital invariant
Sum-product number

References
External links
Parker, Matt. "3435". Numberphile. Brady Haran. Archived from the original on 2017-04-13. Retrieved 2013-04-01.

## Related Articles

### Internal Links

- [Zero to the power of zero](https://en.wikipedia.org/wiki/Zero_to_the_power_of_zero)
- [Abundant number](https://en.wikipedia.org/wiki/Abundant_number)
- [Achilles number](https://en.wikipedia.org/wiki/Achilles_number)
- [Persistence of a number](https://en.wikipedia.org/wiki/Persistence_of_a_number)
- [Aliquot sequence](https://en.wikipedia.org/wiki/Aliquot_sequence)
- [Almost perfect number](https://en.wikipedia.org/wiki/Almost_perfect_number)
- [Almost prime](https://en.wikipedia.org/wiki/Almost_prime)
- [Amenable number](https://en.wikipedia.org/wiki/Amenable_number)
- [Amicable numbers](https://en.wikipedia.org/wiki/Amicable_numbers)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Arithmetic dynamics](https://en.wikipedia.org/wiki/Arithmetic_dynamics)
- [Arithmetic function](https://en.wikipedia.org/wiki/Arithmetic_function)
- [Arithmetic number](https://en.wikipedia.org/wiki/Arithmetic_number)
- [Aronson's sequence](https://en.wikipedia.org/wiki/Aronson%27s_sequence)
- [Automorphic number](https://en.wikipedia.org/wiki/Automorphic_number)
- [Ban number](https://en.wikipedia.org/wiki/Ban_number)
- [Baron Munchausen](https://en.wikipedia.org/wiki/Baron_Munchausen)
- [Bell number](https://en.wikipedia.org/wiki/Bell_number)
- [Betrothed numbers](https://en.wikipedia.org/wiki/Betrothed_numbers)
- [Binary number](https://en.wikipedia.org/wiki/Binary_number)
- [Blum integer](https://en.wikipedia.org/wiki/Blum_integer)
- [Brady Haran](https://en.wikipedia.org/wiki/Brady_Haran)
- [Cake number](https://en.wikipedia.org/wiki/Cake_number)
- [Carmichael number](https://en.wikipedia.org/wiki/Carmichael_number)
- [Catalan number](https://en.wikipedia.org/wiki/Catalan_number)
- [Catalan pseudoprime](https://en.wikipedia.org/wiki/Catalan_pseudoprime)
- [Centered cube number](https://en.wikipedia.org/wiki/Centered_cube_number)
- [Centered decagonal number](https://en.wikipedia.org/wiki/Centered_decagonal_number)
- [Centered dodecahedral number](https://en.wikipedia.org/wiki/Centered_dodecahedral_number)
- [Centered heptagonal number](https://en.wikipedia.org/wiki/Centered_heptagonal_number)
- [Centered hexagonal number](https://en.wikipedia.org/wiki/Centered_hexagonal_number)
- [Centered icosahedral number](https://en.wikipedia.org/wiki/Centered_icosahedral_number)
- [Centered nonagonal number](https://en.wikipedia.org/wiki/Centered_nonagonal_number)
- [Centered octagonal number](https://en.wikipedia.org/wiki/Centered_octagonal_number)
- [Centered octahedral number](https://en.wikipedia.org/wiki/Centered_octahedral_number)
- [Centered pentagonal number](https://en.wikipedia.org/wiki/Centered_pentagonal_number)
- [Centered polygonal number](https://en.wikipedia.org/wiki/Centered_polygonal_number)
- [Centered polyhedral number](https://en.wikipedia.org/wiki/Centered_polyhedral_number)
- [Centered square number](https://en.wikipedia.org/wiki/Centered_square_number)
- [Centered tetrahedral number](https://en.wikipedia.org/wiki/Centered_tetrahedral_number)
- [Centered triangular number](https://en.wikipedia.org/wiki/Centered_triangular_number)
- [Colossally abundant number](https://en.wikipedia.org/wiki/Colossally_abundant_number)
- [Congruent number](https://en.wikipedia.org/wiki/Congruent_number)
- [Cube (algebra)](https://en.wikipedia.org/wiki/Cube_(algebra))
- [Cullen number](https://en.wikipedia.org/wiki/Cullen_number)
- [Cycle detection](https://en.wikipedia.org/wiki/Cycle_detection)
- [Cyclic number](https://en.wikipedia.org/wiki/Cyclic_number)
- [Cyclic number (group theory)](https://en.wikipedia.org/wiki/Cyclic_number_(group_theory))
- [Decagonal number](https://en.wikipedia.org/wiki/Decagonal_number)
- [Dedekind number](https://en.wikipedia.org/wiki/Dedekind_number)
- [Deficient number](https://en.wikipedia.org/wiki/Deficient_number)
- [Delannoy number](https://en.wikipedia.org/wiki/Delannoy_number)
- [Descartes number](https://en.wikipedia.org/wiki/Descartes_number)
- [Digit-reassembly number](https://en.wikipedia.org/wiki/Digit-reassembly_number)
- [Digit sum](https://en.wikipedia.org/wiki/Digit_sum)
- [Digital root](https://en.wikipedia.org/wiki/Digital_root)
- [Divisor](https://en.wikipedia.org/wiki/Divisor)
- [Divisor function](https://en.wikipedia.org/wiki/Divisor_function)
- [Dodecagonal number](https://en.wikipedia.org/wiki/Dodecagonal_number)
- [Dodecahedral number](https://en.wikipedia.org/wiki/Dodecahedral_number)
- [Double Mersenne number](https://en.wikipedia.org/wiki/Double_Mersenne_number)
- [Dudeney number](https://en.wikipedia.org/wiki/Dudeney_number)
- [Eighth power](https://en.wikipedia.org/wiki/Eighth_power)
- [Elliptic pseudoprime](https://en.wikipedia.org/wiki/Elliptic_pseudoprime)
- [Equidigital number](https://en.wikipedia.org/wiki/Equidigital_number)
- [Erdős–Nicolas number](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Nicolas_number)
- [Erdős–Woods number](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Woods_number)
- [Euclid number](https://en.wikipedia.org/wiki/Euclid_number)
- [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function)
- [Euler numbers](https://en.wikipedia.org/wiki/Euler_numbers)
- [Euler pseudoprime](https://en.wikipedia.org/wiki/Euler_pseudoprime)
- [Eulerian number](https://en.wikipedia.org/wiki/Eulerian_number)
- [Euler–Jacobi pseudoprime](https://en.wikipedia.org/wiki/Euler%E2%80%93Jacobi_pseudoprime)
- [Evil number](https://en.wikipedia.org/wiki/Evil_number)
- [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)
- [Extravagant number](https://en.wikipedia.org/wiki/Extravagant_number)
- [Factorion](https://en.wikipedia.org/wiki/Factorion)
- [Fermat number](https://en.wikipedia.org/wiki/Fermat_number)
- [Fermat pseudoprime](https://en.wikipedia.org/wiki/Fermat_pseudoprime)
- [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
- [Fifth power (algebra)](https://en.wikipedia.org/wiki/Fifth_power_(algebra))
- [Figurate number](https://en.wikipedia.org/wiki/Figurate_number)
- [Fortunate number](https://en.wikipedia.org/wiki/Fortunate_number)
- [Four-dimensional space](https://en.wikipedia.org/wiki/Four-dimensional_space)
- [Fourth power](https://en.wikipedia.org/wiki/Fourth_power)
- [Friedman number](https://en.wikipedia.org/wiki/Friedman_number)
- [Friendly number](https://en.wikipedia.org/wiki/Friendly_number)
- [Frobenius pseudoprime](https://en.wikipedia.org/wiki/Frobenius_pseudoprime)
- [Frugal number](https://en.wikipedia.org/wiki/Frugal_number)
- [Fuss–Catalan number](https://en.wikipedia.org/wiki/Fuss%E2%80%93Catalan_number)
- [Generation of primes](https://en.wikipedia.org/wiki/Generation_of_primes)
- [Giuga number](https://en.wikipedia.org/wiki/Giuga_number)
- [Graphemics](https://en.wikipedia.org/wiki/Graphemics)
- [Happy number](https://en.wikipedia.org/wiki/Happy_number)
- [Harmonic divisor number](https://en.wikipedia.org/wiki/Harmonic_divisor_number)
- [Harshad number](https://en.wikipedia.org/wiki/Harshad_number)
- [Hemiperfect number](https://en.wikipedia.org/wiki/Hemiperfect_number)
- [Heptagonal number](https://en.wikipedia.org/wiki/Heptagonal_number)
- [Hexagonal number](https://en.wikipedia.org/wiki/Hexagonal_number)
- [Highly abundant number](https://en.wikipedia.org/wiki/Highly_abundant_number)
- [Highly composite number](https://en.wikipedia.org/wiki/Highly_composite_number)
- [Highly cototient number](https://en.wikipedia.org/wiki/Highly_cototient_number)
- [Highly totient number](https://en.wikipedia.org/wiki/Highly_totient_number)
- [Hilbert number](https://en.wikipedia.org/wiki/Hilbert_number)
- [Hyperperfect number](https://en.wikipedia.org/wiki/Hyperperfect_number)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Icosahedral number](https://en.wikipedia.org/wiki/Icosahedral_number)
- [Idoneal number](https://en.wikipedia.org/wiki/Idoneal_number)
- [Integer (computer science)](https://en.wikipedia.org/wiki/Integer_(computer_science))
- [Jacobsthal number](https://en.wikipedia.org/wiki/Jacobsthal_number)
- [Jordan–Pólya number](https://en.wikipedia.org/wiki/Jordan%E2%80%93P%C3%B3lya_number)
- [Kaprekar's routine](https://en.wikipedia.org/wiki/Kaprekar%27s_routine)
- [Kaprekar number](https://en.wikipedia.org/wiki/Kaprekar_number)
- [Keith number](https://en.wikipedia.org/wiki/Keith_number)
- [Knödel number](https://en.wikipedia.org/wiki/Kn%C3%B6del_number)
- [Lah number](https://en.wikipedia.org/wiki/Lah_number)
- [Lazy caterer's sequence](https://en.wikipedia.org/wiki/Lazy_caterer%27s_sequence)
- [Leonardo number](https://en.wikipedia.org/wiki/Leonardo_number)
- [Leyland number](https://en.wikipedia.org/wiki/Leyland_number)
- [Lobb number](https://en.wikipedia.org/wiki/Lobb_number)
- [Löschian number](https://en.wikipedia.org/wiki/L%C3%B6schian_number)
- [Lucas number](https://en.wikipedia.org/wiki/Lucas_number)
- [Lucas pseudoprime](https://en.wikipedia.org/wiki/Lucas_pseudoprime)
- [Lucas–Carmichael number](https://en.wikipedia.org/wiki/Lucas%E2%80%93Carmichael_number)
- [Lucky number](https://en.wikipedia.org/wiki/Lucky_number)
- [Lucky numbers of Euler](https://en.wikipedia.org/wiki/Lucky_numbers_of_Euler)
- [Lychrel number](https://en.wikipedia.org/wiki/Lychrel_number)
- [Meertens number](https://en.wikipedia.org/wiki/Meertens_number)
- [Mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime)
- [Motzkin number](https://en.wikipedia.org/wiki/Motzkin_number)
- [Multiplicative digital root](https://en.wikipedia.org/wiki/Multiplicative_digital_root)
- [Multiplicative digital root](https://en.wikipedia.org/wiki/Multiplicative_digital_root)
- [Multiply perfect number](https://en.wikipedia.org/wiki/Multiply_perfect_number)
- [Narayana number](https://en.wikipedia.org/wiki/Narayana_number)
- [Narcissistic number](https://en.wikipedia.org/wiki/Narcissistic_number)
- [Natural language](https://en.wikipedia.org/wiki/Natural_language)
- [Natural number](https://en.wikipedia.org/wiki/Natural_number)
- [Nonagonal number](https://en.wikipedia.org/wiki/Nonagonal_number)
- [Noncototient](https://en.wikipedia.org/wiki/Noncototient)
- [Nonhypotenuse number](https://en.wikipedia.org/wiki/Nonhypotenuse_number)
- [Nontotient](https://en.wikipedia.org/wiki/Nontotient)
- [Radix](https://en.wikipedia.org/wiki/Radix)
- [Number theory](https://en.wikipedia.org/wiki/Number_theory)
- [Numeral system](https://en.wikipedia.org/wiki/Numeral_system)
- [Numerical digit](https://en.wikipedia.org/wiki/Numerical_digit)
- [Octagonal number](https://en.wikipedia.org/wiki/Octagonal_number)
- [Octahedral number](https://en.wikipedia.org/wiki/Octahedral_number)
- [Odious number](https://en.wikipedia.org/wiki/Odious_number)
- [Ordered Bell number](https://en.wikipedia.org/wiki/Ordered_Bell_number)
- [P-adic number](https://en.wikipedia.org/wiki/P-adic_number)
- [Padovan sequence](https://en.wikipedia.org/wiki/Padovan_sequence)
- [Palindromic number](https://en.wikipedia.org/wiki/Palindromic_number)
- [Pancake sorting](https://en.wikipedia.org/wiki/Pancake_sorting)
- [Pandigital number](https://en.wikipedia.org/wiki/Pandigital_number)
- [Parasitic number](https://en.wikipedia.org/wiki/Parasitic_number)
- [Pell number](https://en.wikipedia.org/wiki/Pell_number)
- [Pentagonal number](https://en.wikipedia.org/wiki/Pentagonal_number)
- [Pentatope number](https://en.wikipedia.org/wiki/Pentatope_number)
- [Perfect digital invariant](https://en.wikipedia.org/wiki/Perfect_digital_invariant)
- [Perfect number](https://en.wikipedia.org/wiki/Perfect_number)
- [Perfect power](https://en.wikipedia.org/wiki/Perfect_power)
- [Perfect totient number](https://en.wikipedia.org/wiki/Perfect_totient_number)
- [Periodic point](https://en.wikipedia.org/wiki/Periodic_point)
- [Periodic sequence](https://en.wikipedia.org/wiki/Periodic_sequence)
- [Permutation](https://en.wikipedia.org/wiki/Permutation)
- [Pernicious number](https://en.wikipedia.org/wiki/Pernicious_number)
- [Perrin number](https://en.wikipedia.org/wiki/Perrin_number)
- [Persistence of a number](https://en.wikipedia.org/wiki/Persistence_of_a_number)
- [Plane (mathematics)](https://en.wikipedia.org/wiki/Plane_(mathematics))
- [Polite number](https://en.wikipedia.org/wiki/Polite_number)
- [Polydivisible number](https://en.wikipedia.org/wiki/Polydivisible_number)
- [Polygonal number](https://en.wikipedia.org/wiki/Polygonal_number)
- [Figurate number](https://en.wikipedia.org/wiki/Figurate_number)
- [Power of 10](https://en.wikipedia.org/wiki/Power_of_10)
- [Power of three](https://en.wikipedia.org/wiki/Power_of_three)
- [Power of two](https://en.wikipedia.org/wiki/Power_of_two)
- [Powerful number](https://en.wikipedia.org/wiki/Powerful_number)
- [Practical number](https://en.wikipedia.org/wiki/Practical_number)
- [Primary pseudoperfect number](https://en.wikipedia.org/wiki/Primary_pseudoperfect_number)
- [Prime number](https://en.wikipedia.org/wiki/Prime_number)
- [Prime number](https://en.wikipedia.org/wiki/Prime_number)
- [Prime omega function](https://en.wikipedia.org/wiki/Prime_omega_function)
- [Prime power](https://en.wikipedia.org/wiki/Prime_power)
- [Primeval number](https://en.wikipedia.org/wiki/Primeval_number)
- [Primitive abundant number](https://en.wikipedia.org/wiki/Primitive_abundant_number)
- [Primorial](https://en.wikipedia.org/wiki/Primorial)
- [Pronic number](https://en.wikipedia.org/wiki/Pronic_number)
- [Proth prime](https://en.wikipedia.org/wiki/Proth_prime)
- [Pseudoprime](https://en.wikipedia.org/wiki/Pseudoprime)
- [Pyramidal number](https://en.wikipedia.org/wiki/Pyramidal_number)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quasiperfect number](https://en.wikipedia.org/wiki/Quasiperfect_number)
- [Recursion](https://en.wikipedia.org/wiki/Recursion)
- [Refactorable number](https://en.wikipedia.org/wiki/Refactorable_number)
- [Regular number](https://en.wikipedia.org/wiki/Regular_number)
- [Repdigit](https://en.wikipedia.org/wiki/Repdigit)
- [Repunit](https://en.wikipedia.org/wiki/Repunit)
- [Riesel number](https://en.wikipedia.org/wiki/Riesel_number)
- [Rough number](https://en.wikipedia.org/wiki/Rough_number)
- [Schröder number](https://en.wikipedia.org/wiki/Schr%C3%B6der_number)
- [Schröder–Hipparchus number](https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Hipparchus_number)
- [Self-descriptive number](https://en.wikipedia.org/wiki/Self-descriptive_number)
- [Self number](https://en.wikipedia.org/wiki/Self_number)
- [Semiperfect number](https://en.wikipedia.org/wiki/Semiperfect_number)
- [Semiprime](https://en.wikipedia.org/wiki/Semiprime)
- [Seventh power](https://en.wikipedia.org/wiki/Seventh_power)
- [Sierpiński number](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_number)
- [Sieve theory](https://en.wikipedia.org/wiki/Sieve_theory)
- [Sixth power](https://en.wikipedia.org/wiki/Sixth_power)
- [Smarandache–Wellin number](https://en.wikipedia.org/wiki/Smarandache%E2%80%93Wellin_number)
- [Smith number](https://en.wikipedia.org/wiki/Smith_number)
- [Smooth number](https://en.wikipedia.org/wiki/Smooth_number)
- [Sociable number](https://en.wikipedia.org/wiki/Sociable_number)
- [Somer–Lucas pseudoprime](https://en.wikipedia.org/wiki/Somer%E2%80%93Lucas_pseudoprime)
- [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Sorting number](https://en.wikipedia.org/wiki/Sorting_number)
- [Sparsely totient number](https://en.wikipedia.org/wiki/Sparsely_totient_number)
- [Sphenic number](https://en.wikipedia.org/wiki/Sphenic_number)
- [Square number](https://en.wikipedia.org/wiki/Square_number)
- [Square pyramidal number](https://en.wikipedia.org/wiki/Square_pyramidal_number)
- [Square triangular number](https://en.wikipedia.org/wiki/Square_triangular_number)
- [Squared triangular number](https://en.wikipedia.org/wiki/Squared_triangular_number)
- [Star number](https://en.wikipedia.org/wiki/Star_number)
- [Stella octangula number](https://en.wikipedia.org/wiki/Stella_octangula_number)
- [Stirling numbers of the first kind](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind)
- [Stirling numbers of the second kind](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind)
- [Strobogrammatic number](https://en.wikipedia.org/wiki/Strobogrammatic_number)
- [Strong pseudoprime](https://en.wikipedia.org/wiki/Strong_pseudoprime)
- [Størmer number](https://en.wikipedia.org/wiki/St%C3%B8rmer_number)
- [Sublime number](https://en.wikipedia.org/wiki/Sublime_number)
- [Sum-product number](https://en.wikipedia.org/wiki/Sum-product_number)
- [Super-Poulet number](https://en.wikipedia.org/wiki/Super-Poulet_number)
- [Superabundant number](https://en.wikipedia.org/wiki/Superabundant_number)
- [Supergolden ratio](https://en.wikipedia.org/wiki/Supergolden_ratio)
- [Superior highly composite number](https://en.wikipedia.org/wiki/Superior_highly_composite_number)
- [Superperfect number](https://en.wikipedia.org/wiki/Superperfect_number)
- [Telephone number (mathematics)](https://en.wikipedia.org/wiki/Telephone_number_(mathematics))
- [Tetrahedral number](https://en.wikipedia.org/wiki/Tetrahedral_number)
- [Thabit number](https://en.wikipedia.org/wiki/Thabit_number)
- [Three-dimensional space](https://en.wikipedia.org/wiki/Three-dimensional_space)
- [Transposable integer](https://en.wikipedia.org/wiki/Transposable_integer)
- [Triangular number](https://en.wikipedia.org/wiki/Triangular_number)
- [Automorphic number](https://en.wikipedia.org/wiki/Automorphic_number)
- [Ulam number](https://en.wikipedia.org/wiki/Ulam_number)
- [Undulating number](https://en.wikipedia.org/wiki/Undulating_number)
- [Untouchable number](https://en.wikipedia.org/wiki/Untouchable_number)
- [Vampire number](https://en.wikipedia.org/wiki/Vampire_number)
- [Wall–Sun–Sun prime](https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime)
- [Wedderburn–Etherington number](https://en.wikipedia.org/wiki/Wedderburn%E2%80%93Etherington_number)
- [Wieferich prime](https://en.wikipedia.org/wiki/Wieferich_prime)
- [Wilson prime](https://en.wikipedia.org/wiki/Wilson_prime)
- [Wolstenholme number](https://en.wikipedia.org/wiki/Wolstenholme_number)
- [Wolstenholme prime](https://en.wikipedia.org/wiki/Wolstenholme_prime)
- [Woodall number](https://en.wikipedia.org/wiki/Woodall_number)
- [Template:Classes of natural numbers](https://en.wikipedia.org/wiki/Template:Classes_of_natural_numbers)
- [Template talk:Classes of natural numbers](https://en.wikipedia.org/wiki/Template_talk:Classes_of_natural_numbers)
- [Portal:Mathematics](https://en.wikipedia.org/wiki/Portal:Mathematics)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:42:48.420139+00:00_