# Shamir's secret sharing

## Article Metadata

- **Last Updated:** 2024-12-14T19:44:53.067213+00:00
- **Original Article:** [Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing)
- **Language:** en
- **Page ID:** 10948177

## Summary

Shamir's secret sharing (SSS) is an efficient secret sharing algorithm for distributing private information (the "secret") among a group. The secret cannot be revealed unless a quorum of the group acts together to pool their knowledge. To achieve this, the secret is mathematically divided into parts (the "shares") from which the secret can be reassembled only when a sufficient number of shares are combined. SSS has the property of information-theoretic security, meaning that even if an attacker 

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1: long volume value
- Category:Information-theoretically secure algorithms
- Category:Secret sharing
- Category:Short description is different from Wikidata

## Table of Contents

- High-level explanation
- Properties and weaknesses
- History
- Mathematical principle
- Mathematical formulation
- Example calculation
- Python code
- See also
- References
- Further reading
- External links

## Content

Shamir's secret sharing (SSS) is an efficient secret sharing algorithm for distributing private information (the "secret") among a group. The secret cannot be revealed unless a quorum of the group acts together to pool their knowledge. To achieve this, the secret is mathematically divided into parts (the "shares") from which the secret can be reassembled only when a sufficient number of shares are combined. SSS has the property of information-theoretic security, meaning that even if an attacker steals some shares, it is impossible for the attacker to reconstruct the secret unless they have stolen the quorum number of shares.
Shamir's secret sharing is used in some applications to share the access keys to a master secret.

High-level explanation
SSS is used to secure a secret in a distributed form, most often to secure encryption keys. The secret is split into multiple shares, which individually do not give any information about the secret.
To reconstruct a secret secured by SSS, a number of shares is needed, called the threshold. No information about the secret can be gained from any number of shares below the threshold (a property called perfect secrecy). In this sense, SSS is a generalisation of the one-time pad (which can be viewed as SSS with a two-share threshold and two shares in total).

Application example
A company needs to secure their vault. If a single person knows the code to the vault, the code might be lost or unavailable when the vault needs to be opened. If there are several people who know the code, they may not trust each other to always act honestly.
SSS can be used in this situation to generate shares of the vault's code which are distributed to authorized individuals in the company. The minimum threshold and number of shares given to each individual can be selected such that the vault is accessible only by (groups of) authorized individuals. If fewer shares than the threshold are presented, the vault cannot be opened.

By accident, coercion or as an act of opposition, some individuals might present incorrect information for their shares. If the total of correct shares fails to meet the minimum threshold, the vault remains locked.

Use cases
Shamir's secret sharing can be used to

share a key for decrypting the root key of a password manager,
recover a user key for encrypted email access and
share the passphrase used to recreate a master secret, which is in turn used to access a cryptocurrency wallet.

Properties and weaknesses
SSS has useful properties, but also weaknesses that means that it is unsuited to some uses.
Useful properties include:

Secure: The scheme has information-theoretic security.
Minimal: The size of each piece does not exceed the size of the original data.
Extensible: For any given threshold, shares can be dynamically added or deleted without affecting existing shares
Dynamic: Security can be enhanced without changing the secret, but by changing the polynomial occasionally (keeping the same free term) and constructing a new share for each of the participants.
Flexible: In organizations where hierarchy is important, each participant can be issued different numbers of shares according to their importance inside the organization. For instance, with a threshold of 3, the president could unlock the safe alone if given three shares, while three secretaries with one share each must combine their shares to unlock the safe.
Weaknesses include:

No verifiable secret sharing: During the share reassembly process, SSS does not provide a way to verify the correctness of each share being used. Verifiable secret sharing aims to verify that shareholders are honest and not submitting fake shares.
Single point of failure: The secret must exist in one place when it is split into shares, and again in one place when it is reassembled. These are attack points, and other schemes including multisignature eliminate at least one of these single points of failure.

History
Adi Shamir, an Israeli scientist, first formulated the scheme in 1979.

Mathematical principle
The scheme exploits the Lagrange interpolation theorem, specifically that 
  
    
      
        k
      
    
    {\displaystyle k}
  
 points on the polynomial uniquely determines a polynomial of degree less than or equal to 
  
    
      
        k
        −
        1
      
    
    {\displaystyle k-1}
  
. For instance, 2 points are sufficient to define a line, 3 points are sufficient to define a parabola, 4 points to define a cubic curve and so forth.

Mathematical formulation
Shamir's secret sharing is an ideal and perfect 
  
    
      
        
          (
          
            k
            ,
            n
          
          )
        
      
    
    {\displaystyle \left(k,n\right)}
  
-threshold scheme based on polynomial interpolation over finite fields. In such a scheme, the aim is to divide a secret 
  
    
      
        S
      
    
    {\displaystyle S}
  
 (for example, the combination to a safe) into 
  
    
      
        n
      
    
    {\displaystyle n}
  
 pieces of data 
  
    
      
        
          S
          
            1
          
        
        ,
        …
        ,
        
          S
          
            n
          
        
      
    
    {\displaystyle S_{1},\ldots ,S_{n}}
  
 (known as shares) in such a way that:

Knowledge of any 
  
    
      
        k
      
    
    {\displaystyle k}
  
 or more shares 
  
    
      
        
          S
          
            i
          
        
      
    
    {\displaystyle S_{i}}
  
 makes 
  
    
      
        S
      
    
    {\displaystyle S}
  
 computable. That is, the entire secret 
  
    
      
        S
      
    
    {\displaystyle S}
  
 can be reconstructed from any combination of 
  
    
      
        k
      
    
    {\displaystyle k}
  
 shares.
Knowledge of any 
  
    
      
        k
        −
        1
      
    
    {\displaystyle k-1}
  
 or fewer shares 
  
    
      
        
          S
          
            i
          
        
      
    
    {\displaystyle S_{i}}
  
 leaves 
  
    
      
        S
      
    
    {\displaystyle S}
  
 completely undetermined, in the sense that the possible values for 
  
    
      
        S
      
    
    {\displaystyle S}
  
 remain as likely with knowledge of up to 
  
    
      
        k
        −
        1
      
    
    {\displaystyle k-1}
  
 shares as with knowledge of 
  
    
      
        0
      
    
    {\displaystyle 0}
  
 shares. The secret 
  
    
      
        S
      
    
    {\displaystyle S}
  
 cannot be reconstructed with fewer than 
  
    
      
        k
      
    
    {\displaystyle k}
  
 shares.
If 
  
    
      
        n
        =
        k
      
    
    {\displaystyle n=k}
  
, then all of the shares are needed to reconstruct the secret 
  
    
      
        S
      
    
    {\displaystyle S}
  
.
Assume that the secret 
  
    
      
        S
      
    
    {\displaystyle S}
  
 can be represented as an element 
  
    
      
        
          a
          
            0
          
        
      
    
    {\displaystyle a_{0}}
  
 of a finite field 
  
    
      
        
          G
          F
        
        (
        q
        )
      
    
    {\displaystyle \mathrm {GF} (q)}
  
 (where 
  
    
      
        q
      
    
    {\displaystyle q}
  
 is greater than the number 
  
    
      
        n
      
    
    {\displaystyle n}
  
 of shares being generated). Randomly choose 
  
    
      
        k
        −
        1
      
    
    {\displaystyle k-1}
  
 elements, 
  
    
      
        
          a
          
            1
          
        
        ,
        ⋯
        ,
        
          a
          
            k
            −
            1
          
        
      
    
    {\displaystyle a_{1},\cdots ,a_{k-1}}
  
, from 
  
    
      
        
          G
          F
        
        (
        q
        )
      
    
    {\displaystyle \mathrm {GF} (q)}
  
 and construct the polynomial 
  
    
      
        f
        
          (
          x
          )
        
        =
        
          a
          
            0
          
        
        +
        
          a
          
            1
          
        
        x
        +
        
          a
          
            2
          
        
        
          x
          
            2
          
        
        +
        
          a
          
            3
          
        
        
          x
          
            3
          
        
        +
        ⋯
        +
        
          a
          
            k
            −
            1
          
        
        
          x
          
            k
            −
            1
          
        
      
    
    {\displaystyle f\left(x\right)=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots +a_{k-1}x^{k-1}}
  
. Compute any 
  
    
      
        n
      
    
    {\displaystyle n}
  
 points out on the curve, for instance set 
  
    
      
        i
        =
        1
        ,
        …
        ,
        n
      
    
    {\displaystyle i=1,\ldots ,n}
  
 to find points 
  
    
      
        
          (
          
            i
            ,
            f
            
              (
              i
              )
            
          
          )
        
      
    
    {\displaystyle \left(i,f\left(i\right)\right)}
  
. Every participant is given a point (a non-zero input to the polynomial, and the corresponding output). Given any subset of 
  
    
      
        k
      
    
    {\displaystyle k}
  
 of these pairs, 
  
    
      
        
          a
          
            0
          
        
      
    
    {\displaystyle a_{0}}
  
 can be obtained using interpolation, with one possible formula for doing so being 
  
    
      
        
          a
          
            0
          
        
        =
        f
        (
        0
        )
        =
        
          ∑
          
            j
            =
            0
          
          
            k
            −
            1
          
        
        
          y
          
            j
          
        
        
          ∏
          
            
              
                
                  
                    m
                    
                    =
                    
                    0
                  
                
                
                  
                    m
                    
                    ≠
                    
                    j
                  
                
              
            
          
          
            k
            −
            1
          
        
        
          
            
              x
              
                m
              
            
            
              
                x
                
                  m
                
              
              −
              
                x
                
                  j
                
              
            
          
        
      
    
    {\displaystyle a_{0}=f(0)=\sum _{j=0}^{k-1}y_{j}\prod _{\begin{smallmatrix}m\,=\,0\\m\,\neq \,j\end{smallmatrix}}^{k-1}{\frac {x_{m}}{x_{m}-x_{j}}}}
  
, where the list of points on the polynomial is given as 
  
    
      
        k
      
    
    {\displaystyle k}
  
 pairs of the form 
  
    
      
        (
        
          x
          
            i
          
        
        ,
        
          y
          
            i
          
        
        )
      
    
    {\displaystyle (x_{i},y_{i})}
  
. Note that 
  
    
      
        f
        (
        0
        )
      
    
    {\displaystyle f(0)}
  
 is equal to the first coefficient of polynomial 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
.

Example calculation
The following example illustrates the basic idea. Note, however, that calculations in the example are done using integer arithmetic rather than using finite field arithmetic to make the idea easier to understand. Therefore, the example below does not provide perfect secrecy and is not a proper example of Shamir's scheme. The next example will explain the problem.

Preparation
Suppose that the secret to be shared is 1234 
  
    
      
        (
        S
        =
        1234
        )
      
    
    {\displaystyle (S=1234)}
  
.
In this example, the secret will be split into 6 shares 
  
    
      
        (
        n
        =
        6
        )
      
    
    {\displaystyle (n=6)}
  
, where any subset of 3 shares 
  
    
      
        (
        k
        =
        3
        )
      
    
    {\displaystyle (k=3)}
  
 is sufficient to reconstruct the secret. 
  
    
      
        k
        −
        1
        =
        2
      
    
    {\displaystyle k-1=2}
  
 numbers are taken at random. Let them be 166 and 94.

This yields coefficients 
  
    
      
        (
        
          a
          
            0
          
        
        =
        1234
        ;
        
          a
          
            1
          
        
        =
        166
        ;
        
          a
          
            2
          
        
        =
        94
        )
        ,
      
    
    {\displaystyle (a_{0}=1234;a_{1}=166;a_{2}=94),}
  
 where 
  
    
      
        
          a
          
            0
          
        
      
    
    {\displaystyle a_{0}}
  
 is the secret
The polynomial to produce secret shares (points) is therefore:

  
    
      
        f
        (
        x
        )
        =
        1234
        +
        166
        x
        +
        94
        
          x
          
            2
          
        
      
    
    {\displaystyle f(x)=1234+166x+94x^{2}}
  

Six points 
  
    
      
        
          D
          
            x
            −
            1
          
        
        =
        (
        x
        ,
        f
        (
        x
        )
        )
      
    
    {\displaystyle D_{x-1}=(x,f(x))}
  
 from the polynomial are constructed as:

  
    
      
        
          D
          
            0
          
        
        =
        (
        1
        ,
        1494
        )
        ;
        
          D
          
            1
          
        
        =
        (
        2
        ,
        1942
        )
        ;
        
          D
          
            2
          
        
        =
        (
        3
        ,
        2578
        )
        ;
        
          D
          
            3
          
        
        =
        (
        4
        ,
        3402
        )
        ;
        
          D
          
            4
          
        
        =
        (
        5
        ,
        4414
        )
        ;
        
          D
          
            5
          
        
        =
        (
        6
        ,
        5614
        )
      
    
    {\displaystyle D_{0}=(1,1494);D_{1}=(2,1942);D_{2}=(3,2578);D_{3}=(4,3402);D_{4}=(5,4414);D_{5}=(6,5614)}
  

Each participant in the scheme receives a different point (a pair of 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
). Because 
  
    
      
        
          D
          
            x
            −
            1
          
        
      
    
    {\displaystyle D_{x-1}}
  
 is used instead of 
  
    
      
        
          D
          
            x
          
        
      
    
    {\displaystyle D_{x}}
  
 the points start from 
  
    
      
        (
        1
        ,
        f
        (
        1
        )
        )
      
    
    {\displaystyle (1,f(1))}
  
 and not 
  
    
      
        (
        0
        ,
        f
        (
        0
        )
        )
      
    
    {\displaystyle (0,f(0))}
  
. This is necessary because 
  
    
      
        f
        (
        0
        )
      
    
    {\displaystyle f(0)}
  
 is the secret.

Reconstruction
In order to reconstruct the secret, any 3 points are sufficient
Consider using the 3 points
  
    
      
        
          (
          
            
              x
              
                0
              
            
            ,
            
              y
              
                0
              
            
          
          )
        
        =
        
          (
          
            2
            ,
            1942
          
          )
        
        ;
        
          (
          
            
              x
              
                1
              
            
            ,
            
              y
              
                1
              
            
          
          )
        
        =
        
          (
          
            4
            ,
            3402
          
          )
        
        ;
        
          (
          
            
              x
              
                2
              
            
            ,
            
              y
              
                2
              
            
          
          )
        
        =
        
          (
          
            5
            ,
            4414
          
          )
        
      
    
    {\displaystyle \left(x_{0},y_{0}\right)=\left(2,1942\right);\left(x_{1},y_{1}\right)=\left(4,3402\right);\left(x_{2},y_{2}\right)=\left(5,4414\right)}
  
.
Computing the Lagrange basis polynomials:

  
    
      
        
          ℓ
          
            0
          
        
        (
        x
        )
        =
        
          
            
              x
              −
              
                x
                
                  1
                
              
            
            
              
                x
                
                  0
                
              
              −
              
                x
                
                  1
                
              
            
          
        
        ⋅
        
          
            
              x
              −
              
                x
                
                  2
                
              
            
            
              
                x
                
                  0
                
              
              −
              
                x
                
                  2
                
              
            
          
        
        =
        
          
            
              x
              −
              4
            
            
              2
              −
              4
            
          
        
        ⋅
        
          
            
              x
              −
              5
            
            
              2
              −
              5
            
          
        
        =
        
          
            1
            6
          
        
        
          x
          
            2
          
        
        −
        
          
            3
            2
          
        
        x
        +
        
          
            10
            3
          
        
      
    
    {\displaystyle \ell _{0}(x)={\frac {x-x_{1}}{x_{0}-x_{1}}}\cdot {\frac {x-x_{2}}{x_{0}-x_{2}}}={\frac {x-4}{2-4}}\cdot {\frac {x-5}{2-5}}={\frac {1}{6}}x^{2}-{\frac {3}{2}}x+{\frac {10}{3}}}
  

  
    
      
        
          ℓ
          
            1
          
        
        (
        x
        )
        =
        
          
            
              x
              −
              
                x
                
                  0
                
              
            
            
              
                x
                
                  1
                
              
              −
              
                x
                
                  0
                
              
            
          
        
        ⋅
        
          
            
              x
              −
              
                x
                
                  2
                
              
            
            
              
                x
                
                  1
                
              
              −
              
                x
                
                  2
                
              
            
          
        
        =
        
          
            
              x
              −
              2
            
            
              4
              −
              2
            
          
        
        ⋅
        
          
            
              x
              −
              5
            
            
              4
              −
              5
            
          
        
        =
        −
        
          
            1
            2
          
        
        
          x
          
            2
          
        
        +
        
          
            7
            2
          
        
        x
        −
        5
      
    
    {\displaystyle \ell _{1}(x)={\frac {x-x_{0}}{x_{1}-x_{0}}}\cdot {\frac {x-x_{2}}{x_{1}-x_{2}}}={\frac {x-2}{4-2}}\cdot {\frac {x-5}{4-5}}=-{\frac {1}{2}}x^{2}+{\frac {7}{2}}x-5}
  

  
    
      
        
          ℓ
          
            2
          
        
        (
        x
        )
        =
        
          
            
              x
              −
              
                x
                
                  0
                
              
            
            
              
                x
                
                  2
                
              
              −
              
                x
                
                  0
                
              
            
          
        
        ⋅
        
          
            
              x
              −
              
                x
                
                  1
                
              
            
            
              
                x
                
                  2
                
              
              −
              
                x
                
                  1
                
              
            
          
        
        =
        
          
            
              x
              −
              2
            
            
              5
              −
              2
            
          
        
        ⋅
        
          
            
              x
              −
              4
            
            
              5
              −
              4
            
          
        
        =
        
          
            1
            3
          
        
        
          x
          
            2
          
        
        −
        2
        x
        +
        
          
            8
            3
          
        
      
    
    {\displaystyle \ell _{2}(x)={\frac {x-x_{0}}{x_{2}-x_{0}}}\cdot {\frac {x-x_{1}}{x_{2}-x_{1}}}={\frac {x-2}{5-2}}\cdot {\frac {x-4}{5-4}}={\frac {1}{3}}x^{2}-2x+{\frac {8}{3}}}
  

Using the formula for polynomial interpolation, 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
 is:

  
    
      
        
          
            
              
                f
                (
                x
                )
              
              
                
                =
                
                  ∑
                  
                    j
                    =
                    0
                  
                  
                    2
                  
                
                
                  y
                  
                    j
                  
                
                ⋅
                
                  ℓ
                  
                    j
                  
                
                (
                x
                )
              
            
            
              
              
                
                =
                
                  y
                  
                    0
                  
                
                
                  ℓ
                  
                    0
                  
                
                (
                x
                )
                +
                
                  y
                  
                    1
                  
                
                
                  ℓ
                  
                    1
                  
                
                (
                x
                )
                +
                
                  y
                  
                    2
                  
                
                
                  ℓ
                  
                    2
                  
                
                (
                x
                )
              
            
            
              
              
                
                =
                1942
                
                  (
                  
                    
                      
                        1
                        6
                      
                    
                    
                      x
                      
                        2
                      
                    
                    −
                    
                      
                        3
                        2
                      
                    
                    x
                    +
                    
                      
                        10
                        3
                      
                    
                  
                  )
                
                +
                3402
                
                  (
                  
                    −
                    
                      
                        1
                        2
                      
                    
                    
                      x
                      
                        2
                      
                    
                    +
                    
                      
                        7
                        2
                      
                    
                    x
                    −
                    5
                  
                  )
                
                +
                4414
                
                  (
                  
                    
                      
                        1
                        3
                      
                    
                    
                      x
                      
                        2
                      
                    
                    −
                    2
                    x
                    +
                    
                      
                        8
                        3
                      
                    
                  
                  )
                
              
            
            
              
              
                
                =
                1234
                +
                166
                x
                +
                94
                
                  x
                  
                    2
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}f(x)&=\sum _{j=0}^{2}y_{j}\cdot \ell _{j}(x)\\[6pt]&=y_{0}\ell _{0}(x)+y_{1}\ell _{1}(x)+y_{2}\ell _{2}(x)\\[6pt]&=1942\left({\frac {1}{6}}x^{2}-{\frac {3}{2}}x+{\frac {10}{3}}\right)+3402\left(-{\frac {1}{2}}x^{2}+{\frac {7}{2}}x-5\right)+4414\left({\frac {1}{3}}x^{2}-2x+{\frac {8}{3}}\right)\\[6pt]&=1234+166x+94x^{2}\end{aligned}}}
  

Recalling that the secret is the free coefficient, which means that 
  
    
      
        S
        =
        1234
      
    
    {\displaystyle S=1234}
  
, and the secret has been recovered.

Computationally efficient approach
Using polynomial interpolation to find a coefficient in a source polynomial 
  
    
      
        S
        =
        f
        (
        0
        )
      
    
    {\displaystyle S=f(0)}
  
 using Lagrange polynomials is not efficient, since unused constants are calculated.
Considering this, an optimized formula to use Lagrange polynomials to find 
  
    
      
        f
        (
        0
        )
      
    
    {\displaystyle f(0)}
  
 is defined as follows:

  
    
      
        f
        (
        0
        )
        =
        
          ∑
          
            j
            =
            0
          
          
            k
            −
            1
          
        
        
          y
          
            j
          
        
        
          ∏
          
            
              
                
                  
                    m
                    
                    =
                    
                    0
                  
                
                
                  
                    m
                    
                    ≠
                    
                    j
                  
                
              
            
          
          
            k
            −
            1
          
        
        
          
            
              x
              
                m
              
            
            
              
                x
                
                  m
                
              
              −
              
                x
                
                  j
                
              
            
          
        
      
    
    {\displaystyle f(0)=\sum _{j=0}^{k-1}y_{j}\prod _{\begin{smallmatrix}m\,=\,0\\m\,\neq \,j\end{smallmatrix}}^{k-1}{\frac {x_{m}}{x_{m}-x_{j}}}}

Problem of using integer arithmetic
Although the simplified version of the method demonstrated above, which uses integer arithmetic rather than finite field arithmetic, works, there is a security problem: Eve gains information about 
  
    
      
        S
      
    
    {\displaystyle S}
  
 with every 
  
    
      
        
          D
          
            i
          
        
      
    
    {\displaystyle D_{i}}
  
 that she finds.
Suppose that she finds the 2 points 
  
    
      
        
          D
          
            0
          
        
        =
        (
        1
        ,
        1494
        )
      
    
    {\displaystyle D_{0}=(1,1494)}
  
 and 
  
    
      
        
          D
          
            1
          
        
        =
        (
        2
        ,
        1942
        )
      
    
    {\displaystyle D_{1}=(2,1942)}
  
. She still does not have 
  
    
      
        k
        =
        3
      
    
    {\displaystyle k=3}
  
 points, so in theory she should not have gained any more information about 
  
    
      
        S
      
    
    {\displaystyle S}
  
. But she  could combine the information from the 2 points with the public information: 
  
    
      
        n
        =
        6
        ,
        k
        =
        3
        ,
        f
        (
        x
        )
        =
        
          a
          
            0
          
        
        +
        
          a
          
            1
          
        
        x
        +
        ⋯
        +
        
          a
          
            k
            −
            1
          
        
        
          x
          
            k
            −
            1
          
        
        ,
        
          a
          
            0
          
        
        =
        S
        ,
        
          a
          
            i
          
        
        ∈
        
          Z
        
      
    
    {\displaystyle n=6,k=3,f(x)=a_{0}+a_{1}x+\cdots +a_{k-1}x^{k-1},a_{0}=S,a_{i}\in \mathbb {Z} }
  
. Doing so, Eve could perform the following algebra:

Fill the formula for 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
 with 
  
    
      
        S
      
    
    {\displaystyle S}
  
 and the value of 
  
    
      
        k
        :
        f
        (
        x
        )
        =
        S
        +
        
          a
          
            1
          
        
        x
        +
        ⋯
        +
        
          a
          
            k
            −
            1
          
        
        
          x
          
            k
            −
            1
          
        
        ⇒
        

        
        f
        (
        x
        )
        =
        S
        +
        
          a
          
            1
          
        
        x
        +
        
          a
          
            2
          
        
        
          x
          
            2
          
        
      
    
    {\displaystyle k:f(x)=S+a_{1}x+\cdots +a_{k-1}x^{k-1}\Rightarrow {}f(x)=S+a_{1}x+a_{2}x^{2}}
  

Fill (1) with the values of 
  
    
      
        
          D
          
            0
          
        
      
    
    {\displaystyle D_{0}}
  
's 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and 
  
    
      
        f
        (
        x
        )
        :
        1494
        =
        S
        +
        
          a
          
            1
          
        
        1
        +
        
          a
          
            2
          
        
        
          1
          
            2
          
        
        ⇒
        

        
        1494
        =
        S
        +
        
          a
          
            1
          
        
        +
        
          a
          
            2
          
        
      
    
    {\displaystyle f(x):1494=S+a_{1}1+a_{2}1^{2}\Rightarrow {}1494=S+a_{1}+a_{2}}
  

Fill  (1) with the values of 
  
    
      
        
          D
          
            1
          
        
      
    
    {\displaystyle D_{1}}
  
's 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and 
  
    
      
        f
        (
        x
        )
        :
        1942
        =
        S
        +
        
          a
          
            1
          
        
        2
        +
        
          a
          
            2
          
        
        
          2
          
            2
          
        
        ⇒
        

        
        1942
        =
        S
        +
        2
        
          a
          
            1
          
        
        +
        4
        
          a
          
            2
          
        
      
    
    {\displaystyle f(x):1942=S+a_{1}2+a_{2}2^{2}\Rightarrow {}1942=S+2a_{1}+4a_{2}}
  

Subtract (3)-(2): 
  
    
      
        (
        1942
        −
        1494
        )
        =
        (
        S
        −
        S
        )
        +
        (
        2
        
          a
          
            1
          
        
        −
        
          a
          
            1
          
        
        )
        +
        (
        4
        
          a
          
            2
          
        
        −
        
          a
          
            2
          
        
        )
        ⇒
        

        
        448
        =
        
          a
          
            1
          
        
        +
        3
        
          a
          
            2
          
        
      
    
    {\displaystyle (1942-1494)=(S-S)+(2a_{1}-a_{1})+(4a_{2}-a_{2})\Rightarrow {}448=a_{1}+3a_{2}}
  
 and rewrite this as 
  
    
      
        
          a
          
            1
          
        
        =
        448
        −
        3
        
          a
          
            2
          
        
      
    
    {\displaystyle a_{1}=448-3a_{2}}
  
.
Now, Eve can replace the result from (4) into (2): 
  
    
      
        1494
        =
        S
        +
        (
        448
        −
        3
        
          a
          
            2
          
        
        )
        +
        
          a
          
            2
          
        
        ⇒
        

        
        S
        =
        1046
        +
        2
        
          a
          
            2
          
        
      
    
    {\displaystyle 1494=S+(448-3a_{2})+a_{2}\Rightarrow {}S=1046+2a_{2}}
  
 which leads her to the information that S is even.

Solution using finite field arithmetic
The above attack exploits constraints on the values that the polynomial may take by virtue of how it was constructed: the polynomial must have coefficients that are integers, and the polynomial must take an integer as value when evaluated at each of the coordinates used in the scheme. This reduces its possible values at unknown points, including the resultant secret, given fewer than 
  
    
      
        k
      
    
    {\displaystyle k}
  
 shares.
This problem can be remedied by using finite field arithmetic.  A finite field always has size 
  
    
      
        q
        =
        
          p
          
            r
          
        
      
    
    {\displaystyle q=p^{r}}
  
, where 
  
    
      
        p
      
    
    {\displaystyle p}
  
 is a prime and 
  
    
      
        r
      
    
    {\displaystyle r}
  
 is a positive integer.  The size 
  
    
      
        q
      
    
    {\displaystyle q}
  
 of the field must satisfy 
  
    
      
        q
        >
        n
      
    
    {\displaystyle q>n}
  
, and that 
  
    
      
        q
      
    
    {\displaystyle q}
  
 is greater than the number of possible values for the secret, though the latter condition may be circumvented by splitting the secret into smaller secret values, and applying the scheme to each of these.  In our example below, we use a prime field (i.e. r = 1). The figure shows a polynomial curve over a finite field.
In practice this is only a small change. The order q of the field (i.e. the number of values that it has) must be chosen to be greater than the number of participants and the number of values that the secret 
  
    
      
        
          a
          
            0
          
        
        =
        S
      
    
    {\displaystyle a_{0}=S}
  
 may take. All calculations involving the polynomial must also be calculated over the field (mod p in our example, in which 
  
    
      
        p
        =
        q
      
    
    {\displaystyle p=q}
  
 is taken to be a prime) instead of over the integers.  Both the choice of the field and the mapping of the secret to a value in this field are considered to be publicly known.
For this example, choose 
  
    
      
        p
        =
        1613
      
    
    {\displaystyle p=1613}
  
, so the polynomial becomes 
  
    
      
        f
        (
        x
        )
        =
        1234
        +
        166
        x
        +
        94
        
          x
          
            2
          
        
        
          mod
          
            1613
          
        
      
    
    {\displaystyle f(x)=1234+166x+94x^{2}{\bmod {1613}}}
  
 which gives the points: 
  
    
      
        (
        1
        ,
        1494
        )
        ;
        (
        2
        ,
        329
        )
        ;
        (
        3
        ,
        965
        )
        ;
        (
        4
        ,
        176
        )
        ;
        (
        5
        ,
        1188
        )
        ;
        (
        6
        ,
        775
        )
      
    
    {\displaystyle (1,1494);(2,329);(3,965);(4,176);(5,1188);(6,775)}
  

This time Eve doesn't gain any information when she finds a 
  
    
      
        
          D
          
            x
          
        
      
    
    {\displaystyle D_{x}}
  
 (until she has 
  
    
      
        k
      
    
    {\displaystyle k}
  
 points).
Suppose again that Eve finds 
  
    
      
        
          D
          
            0
          
        
        =
        
          (
          
            1
            ,
            1494
          
          )
        
      
    
    {\displaystyle D_{0}=\left(1,1494\right)}
  
 and 
  
    
      
        
          D
          
            1
          
        
        =
        
          (
          
            2
            ,
            329
          
          )
        
      
    
    {\displaystyle D_{1}=\left(2,329\right)}
  
, and the public information is: 
  
    
      
        n
        =
        6
        ,
        k
        =
        3
        ,
        p
        =
        1613
        ,
        f
        (
        x
        )
        =
        
          a
          
            0
          
        
        +
        
          a
          
            1
          
        
        x
        +
        ⋯
        +
        
          a
          
            k
            −
            1
          
        
        
          x
          
            k
            −
            1
          
        
        
        mod
        
        
        p
        ,
        
          a
          
            0
          
        
        =
        S
        ,
        
          a
          
            i
          
        
        ∈
        
          N
        
      
    
    {\displaystyle n=6,k=3,p=1613,f(x)=a_{0}+a_{1}x+\dots +a_{k-1}x^{k-1}\mod {p},a_{0}=S,a_{i}\in \mathbb {N} }
  
. Attempting the previous attack, Eve can:

Fill the 
  
    
      
        f
        (
        x
        )
      
    
    {\displaystyle f(x)}
  
-formula with 
  
    
      
        S
      
    
    {\displaystyle S}
  
 and the value of 
  
    
      
        k
      
    
    {\displaystyle k}
  
 and 
  
    
      
        p
      
    
    {\displaystyle p}
  
: 
  
    
      
        f
        (
        x
        )
        =
        S
        +
        
          a
          
            1
          
        
        x
        +
        ⋯
        +
        
          a
          
            3
            −
            1
          
        
        
          x
          
            3
            −
            1
          
        
        
        mod
        
        
        1613
      
    
    {\displaystyle f(x)=S+a_{1}x+\dots +a_{3-1}x^{3-1}\mod 1613}
  

Fill (1) with the values of 
  
    
      
        
          D
          
            0
          
        
      
    
    {\displaystyle D_{0}}
  
's 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and 
  
    
      
        f
        (
        x
        )
        :
        1494
        ≡
        S
        +
        
          a
          
            1
          
        
        1
        +
        
          a
          
            2
          
        
        
          1
          
            2
          
        
        
          
          (
          mod
          
          1613
          )
        
        ⇒
        

        
        1494
        ≡
        S
        +
        
          a
          
            1
          
        
        +
        
          a
          
            2
          
        
        
          
          (
          mod
          
          1613
          )
        
      
    
    {\displaystyle f(x):1494\equiv S+a_{1}1+a_{2}1^{2}{\pmod {1613}}\Rightarrow {}1494\equiv S+a_{1}+a_{2}{\pmod {1613}}}
  

Fill (1) with the values of 
  
    
      
        
          D
          
            1
          
        
      
    
    {\displaystyle D_{1}}
  
's 
  
    
      
        x
      
    
    {\displaystyle x}
  
 and 
  
    
      
        f
        (
        x
        )
        :
        1942
        ≡
        S
        +
        
          a
          
            1
          
        
        2
        +
        
          a
          
            2
          
        
        
          2
          
            2
          
        
        
          
          (
          mod
          
          1613
          )
        
        ⇒
        

        
        1942
        ≡
        S
        +
        2
        
          a
          
            1
          
        
        +
        4
        
          a
          
            2
          
        
        
          
          (
          mod
          
          1613
          )
        
      
    
    {\displaystyle f(x):1942\equiv S+a_{1}2+a_{2}2^{2}{\pmod {1613}}\Rightarrow {}1942\equiv S+2a_{1}+4a_{2}{\pmod {1613}}}
  

Subtract (3)-(2): 
  
    
      
        (
        1942
        −
        1494
        )
        ≡
        (
        S
        −
        S
        )
        +
        (
        2
        
          a
          
            1
          
        
        −
        
          a
          
            1
          
        
        )
        +
        (
        4
        
          a
          
            2
          
        
        −
        
          a
          
            2
          
        
        )
        
          
          (
          mod
          
          1613
          )
        
        ⇒
        

        
        448
        ≡
        
          a
          
            1
          
        
        +
        3
        
          a
          
            2
          
        
        
          
          (
          mod
          
          1613
          )
        
      
    
    {\displaystyle (1942-1494)\equiv (S-S)+(2a_{1}-a_{1})+(4a_{2}-a_{2}){\pmod {1613}}\Rightarrow {}448\equiv a_{1}+3a_{2}{\pmod {1613}}}
  
 and rewrite this as 
  
    
      
        
          a
          
            1
          
        
        ≡
        448
        −
        3
        
          a
          
            2
          
        
        
          
          (
          mod
          
          1613
          )
        
      
    
    {\displaystyle a_{1}\equiv 448-3a_{2}{\pmod {1613}}}
  

There are 
  
    
      
        p
      
    
    {\displaystyle p}
  
 possible values for 
  
    
      
        
          a
          
            1
          
        
      
    
    {\displaystyle a_{1}}
  
. She knows that 
  
    
      
        [
        448
        ,
        445
        ,
        442
        ,
        …
        ]
      
    
    {\displaystyle [448,445,442,\ldots ]}
  
 always decreases by 3, so if 
  
    
      
        p
      
    
    {\displaystyle p}
  
 were divisible by 
  
    
      
        3
      
    
    {\displaystyle 3}
  
 she could conclude 
  
    
      
        
          a
          
            1
          
        
        ∈
        [
        1
        ,
        4
        ,
        7
        ,
        …
        ]
      
    
    {\displaystyle a_{1}\in [1,4,7,\ldots ]}
  
. However, 
  
    
      
        p
      
    
    {\displaystyle p}
  
 is prime, so she can not conclude this. Thus, using a finite field avoids this possible attack.
Also, even though Eve can conclude that 
  
    
      
        S
        ≡
        1046
        +
        2
        
          a
          
            2
          
        
        
          
          (
          mod
          
          1613
          )
        
      
    
    {\displaystyle S\equiv 1046+2a_{2}{\pmod {1613}}}
  
, it does not provide any additional information, since the "wrapping around" behavior of modular arithmetic prevents the leakage of "S is even", unlike the example with integer arithmetic above.

Python code
For purposes of keeping the code clearer, a prime field is used here. In practice, for convenience a scheme constructed using a smaller binary field may be separately applied to small substrings of bits of the secret (e.g. GF(256) for byte-wise application), without loss of security.  The strict condition that the size of the field must be larger than the number of shares must still be respected (e.g., if the number of shares could exceed 255, the field GF(256) might be replaced by say GF(65536)).

See also
Secret sharing
Secure multi-party computation
Lagrange polynomial
Homomorphic secret sharing – a simplistic decentralized voting protocol
Two-person rule
Partial Password

References
Further reading
Dawson, E.; Donovan, D. (1994), "The breadth of Shamir's secret-sharing scheme", Computers & Security, 13: 69–78, doi:10.1016/0167-4048(94)90097-3.
Benzekki, K. (2017). "A Verifiable Secret Sharing Approach for Secure MultiCloud Storage". Ubiquitous Networking. Lecture Notes in Computer Science. Vol. 10542. Casablanca: Springer. pp. 225–234. doi:10.1007/978-3-319-68179-5_20. ISBN 978-3-319-68178-8..

External links
Shamir's Secret Sharing in the Crypto++ library
Shamir's Secret Sharing Scheme (ssss) – a GNU GPL implementation
sharedsecret – implementation in Go
s4 - online shamir's secret sharing tool utilizing HashiCorp's shamir secret sharing algorithm
Shamir39 - webversion on iancoleman.io
kn Secrets - webversion on a dedicated website, aiming to make Shamir's secret sharing as accessible as possible

## Related Articles

### Internal Links

- [Adi Shamir](https://en.wikipedia.org/wiki/Adi_Shamir)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Alice and Bob](https://en.wikipedia.org/wiki/Alice_and_Bob)
- [Constant term](https://en.wikipedia.org/wiki/Constant_term)
- [Crypto++](https://en.wikipedia.org/wiki/Crypto%2B%2B)
- [Cryptocurrency wallet](https://en.wikipedia.org/wiki/Cryptocurrency_wallet)
- [Cubic function](https://en.wikipedia.org/wiki/Cubic_function)
- [Degree of a polynomial](https://en.wikipedia.org/wiki/Degree_of_a_polynomial)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)
- [Algorithmic efficiency](https://en.wikipedia.org/wiki/Algorithmic_efficiency)
- [Email encryption](https://en.wikipedia.org/wiki/Email_encryption)
- [Key (cryptography)](https://en.wikipedia.org/wiki/Key_(cryptography))
- [Finite field](https://en.wikipedia.org/wiki/Finite_field)
- [Finite field arithmetic](https://en.wikipedia.org/wiki/Finite_field_arithmetic)
- [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Go (programming language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- [HashiCorp](https://en.wikipedia.org/wiki/HashiCorp)
- [Homomorphic secret sharing](https://en.wikipedia.org/wiki/Homomorphic_secret_sharing)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Information-theoretic security](https://en.wikipedia.org/wiki/Information-theoretic_security)
- [Interpolation](https://en.wikipedia.org/wiki/Interpolation)
- [Israel](https://en.wikipedia.org/wiki/Israel)
- [Lagrange polynomial](https://en.wikipedia.org/wiki/Lagrange_polynomial)
- [Lagrange polynomial](https://en.wikipedia.org/wiki/Lagrange_polynomial)
- [Line (geometry)](https://en.wikipedia.org/wiki/Line_(geometry))
- [Cryptocurrency wallet](https://en.wikipedia.org/wiki/Cryptocurrency_wallet)
- [One-time pad](https://en.wikipedia.org/wiki/One-time_pad)
- [PCMag](https://en.wikipedia.org/wiki/PCMag)
- [Parabola](https://en.wikipedia.org/wiki/Parabola)
- [Partial password](https://en.wikipedia.org/wiki/Partial_password)
- [Password manager](https://en.wikipedia.org/wiki/Password_manager)
- [Point (geometry)](https://en.wikipedia.org/wiki/Point_(geometry))
- [Polynomial](https://en.wikipedia.org/wiki/Polynomial)
- [Polynomial interpolation](https://en.wikipedia.org/wiki/Polynomial_interpolation)
- [Quorum](https://en.wikipedia.org/wiki/Quorum)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Safe](https://en.wikipedia.org/wiki/Safe)
- [Secret sharing](https://en.wikipedia.org/wiki/Secret_sharing)
- [Secure multi-party computation](https://en.wikipedia.org/wiki/Secure_multi-party_computation)
- [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
- [The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)
- [Secret sharing](https://en.wikipedia.org/wiki/Secret_sharing)
- [Two-person rule](https://en.wikipedia.org/wiki/Two-person_rule)
- [Verifiable secret sharing](https://en.wikipedia.org/wiki/Verifiable_secret_sharing)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:44:53.067213+00:00_