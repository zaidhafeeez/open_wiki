# TPK algorithm

## Article Metadata

- **Last Updated:** 2024-12-14T19:46:02.852076+00:00
- **Original Article:** [TPK algorithm](https://en.wikipedia.org/wiki/TPK_algorithm)
- **Language:** en
- **Page ID:** 1149596

## Summary

The TPK algorithm is a simple program introduced by Donald Knuth and Luis Trabb Pardo to illustrate the evolution of computer programming languages. In their 1977 work "The Early Development of Programming Languages", Trabb Pardo and Knuth introduced a small program that involved arrays, indexing, mathematical functions, subroutines, I/O, conditionals and iteration. They then wrote implementations of the algorithm in several early programming languages to show how such concepts were expressed.
T

## Categories

- Category:1977 in computing
- Category:Articles with example ALGOL 60 code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Computer programming folklore
- Category:Donald Knuth
- Category:Short description matches Wikidata
- Category:Test items in computer languages

## Table of Contents

- The algorithm
- Implementations
- References
- External links

## Content

The TPK algorithm is a simple program introduced by Donald Knuth and Luis Trabb Pardo to illustrate the evolution of computer programming languages. In their 1977 work "The Early Development of Programming Languages", Trabb Pardo and Knuth introduced a small program that involved arrays, indexing, mathematical functions, subroutines, I/O, conditionals and iteration. They then wrote implementations of the algorithm in several early programming languages to show how such concepts were expressed.
To explain the name "TPK", the authors referred to Grimm's law (which concerns the consonants 't', 'p', and 'k'), the sounds in the word "typical", and their own initials (Trabb Pardo and Knuth). In a talk based on the paper, Knuth said:

You can only appreciate how deep the subject is by seeing how good people struggled with it and how the ideas emerged one at a time. In order to study this—Luis I think was the main instigator of this idea—we take one program—one algorithm—and we write it in every language. And that way from one example we can quickly psych out the flavor of that particular language. We call this the TPK program, and well, the fact that it has the initials of Trabb Pardo and Knuth is just a funny coincidence.

The algorithm
Knuth describes it as follows:

We introduced a simple procedure called the “TPK algorithm,” and gave the flavor of each language by expressing TPK in each particular style. […] The TPK algorithm inputs eleven numbers 
  
    
      
        
          a
          
            0
          
        
        ,
        
          a
          
            1
          
        
        ,
        …
        ,
        
          a
          
            10
          
        
      
    
    {\displaystyle a_{0},a_{1},\ldots ,a_{10}}
  
; then it outputs a sequence of eleven pairs 
  
    
      
        (
        10
        ,
        
          b
          
            10
          
        
        )
        ,
        (
        9
        ,
        
          b
          
            9
          
        
        )
        ,
        …
        ,
        (
        0
        ,
        
          b
          
            0
          
        
        )
        ,
      
    
    {\displaystyle (10,b_{10}),(9,b_{9}),\ldots ,(0,b_{0}),}
  
 where

  
    
      
        
          b
          
            i
          
        
        =
        
          
            {
            
              
                
                  f
                  (
                  
                    a
                    
                      i
                    
                  
                  )
                  ,
                
                
                  
                    if 
                  
                  f
                  (
                  
                    a
                    
                      i
                    
                  
                  )
                  ≤
                  400
                  ;
                
              
              
                
                  999
                  ,
                
                
                  
                    if 
                  
                  f
                  (
                  
                    a
                    
                      i
                    
                  
                  )
                  >
                  400
                  ;
                
              
            
            
          
        
        
        f
        (
        x
        )
        =
        
          
            
              |
            
            x
            
              |
            
          
        
        +
        5
        
          x
          
            3
          
        
        .
      
    
    {\displaystyle b_{i}={\begin{cases}f(a_{i}),&{\text{if }}f(a_{i})\leq 400;\\999,&{\text{if }}f(a_{i})>400;\end{cases}}\quad f(x)={\sqrt {|x|}}+5x^{3}.}
  

This simple task is obviously not much of a challenge, in any decent computer language.
In pseudocode:

ask for 11 numbers to be read into a sequence S
reverse sequence S
for each item in sequence S
    call a function to do an operation
    if result overflows
        alert user
    else
        print result

The algorithm reads eleven numbers from an input device, stores them in an array, and then processes them in reverse order, applying a user-defined function to each value and reporting either the value of the function or a message to the effect that the value has exceeded some threshold.

Implementations
Implementations in the original paper
In the original paper, which covered "roughly the first decade" of the development of high-level programming languages (from 1945 up to 1957), they gave the following example implementation "in a dialect of ALGOL 60", noting that ALGOL 60 was a later development than the languages actually discussed in the paper:

As many of the early high-level languages could not handle the TPK algorithm exactly, they allow the following modifications:

If the language supports only integer variables, then assume that all inputs and outputs are integer-valued, and that sqrt(x) means the largest integer not exceeding 
  
    
      
        
          
            x
          
        
      
    
    {\displaystyle {\sqrt {x}}}
  
.
If the language does not support alphabetic output, then instead of the string 'TOO LARGE', output the number 999.
If the language does not allow any input and output, then assume that the 11 input values 
  
    
      
        
          a
          
            0
          
        
        ,
        
          a
          
            1
          
        
        ,
        …
        ,
        
          a
          
            10
          
        
      
    
    {\displaystyle a_{0},a_{1},\ldots ,a_{10}}
  
 have been supplied by an external process somehow, and the task is to compute the 22 output values 
  
    
      
        10
        ,
        f
        (
        10
        )
        ,
        9
        ,
        f
        (
        9
        )
        ,
        …
        ,
        0
        ,
        f
        (
        0
        )
      
    
    {\displaystyle 10,f(10),9,f(9),\ldots ,0,f(0)}
  
 (with 999 replacing too-large values of 
  
    
      
        f
        (
        i
        )
      
    
    {\displaystyle f(i)}
  
).
If the language does not allow programmers to define their own functions, then replace f(a[i]) with an expression equivalent to 
  
    
      
        
          
            
              |
            
            
              a
              
                i
              
            
            
              |
            
          
        
        +
        5
        
          x
          
            3
          
        
      
    
    {\displaystyle {\sqrt {|a_{i}|}}+5x^{3}}
  
.
With these modifications when necessary, the authors implement this algorithm in Konrad Zuse's Plankalkül, in Goldstine and von Neumann's flow diagrams, in Haskell Curry's proposed notation, in Short Code of John Mauchly and others, in the Intermediate Program Language of Arthur Burks, in the notation of Heinz Rutishauser, in the language and compiler by Corrado Böhm in 1951–52, in Autocode of Alick Glennie, in the A-2 system of Grace Hopper, in the Laning and Zierler system, in the earliest proposed Fortran (1954) of John Backus, in the Autocode for Mark 1 by Tony Brooker, in ПП-2 of Andrey Ershov, in BACAIC of Mandalay Grems and R. E. Porter, in Kompiler 2 of A. Kenton Elsworth and others, in ADES of E. K. Blum, the Internal Translator of Alan Perlis, in Fortran of John Backus, in ARITH-MATIC and MATH-MATIC from Grace Hopper's lab, in the system of Bauer and Samelson, and (in addenda in 2003 and 2009) PACT I and TRANSCODE. They then describe what kind of arithmetic was available, and provide a subjective rating of these languages on parameters of "implementation", "readability", "control structures", "data structures", "machine independence" and "impact", besides mentioning what each was the first to do.

Implementations in more recent languages
C implementation
This shows a C implementation equivalent to the above ALGOL 60.

Python implementation
This shows a Python implementation.

Rust implementation
This shows a Rust implementation.

References
External links
Implementations in many languages at Rosetta Code
Implementations in several languages

## Related Articles

### Internal Links

- ["Hello, World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [-yllion](https://en.wikipedia.org/wiki/-yllion)
- [1951 USAF resolution test chart](https://en.wikipedia.org/wiki/1951_USAF_resolution_test_chart)
- [3DBenchy](https://en.wikipedia.org/wiki/3DBenchy)
- [3D computer graphics](https://en.wikipedia.org/wiki/3D_computer_graphics)
- [A-0 System](https://en.wikipedia.org/wiki/A-0_System)
- [ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60)
- [AMS Euler](https://en.wikipedia.org/wiki/AMS_Euler)
- [ARITH-MATIC](https://en.wikipedia.org/wiki/ARITH-MATIC)
- [Acid1](https://en.wikipedia.org/wiki/Acid1)
- [Acid2](https://en.wikipedia.org/wiki/Acid2)
- [Acid3](https://en.wikipedia.org/wiki/Acid3)
- [Alan Perlis](https://en.wikipedia.org/wiki/Alan_Perlis)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Alick Glennie](https://en.wikipedia.org/wiki/Alick_Glennie)
- [Allen Kent](https://en.wikipedia.org/wiki/Allen_Kent)
- [Andrey Yershov](https://en.wikipedia.org/wiki/Andrey_Yershov)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Arthur Burks](https://en.wikipedia.org/wiki/Arthur_Burks)
- [Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
- [Autocode](https://en.wikipedia.org/wiki/Autocode)
- [Bad Apple!!](https://en.wikipedia.org/wiki/Bad_Apple!!)
- [Web (programming system)](https://en.wikipedia.org/wiki/Web_(programming_system))
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Calgary corpus](https://en.wikipedia.org/wiki/Calgary_corpus)
- [Canterbury corpus](https://en.wikipedia.org/wiki/Canterbury_corpus)
- [Chinese room](https://en.wikipedia.org/wiki/Chinese_room)
- [Computer History Museum](https://en.wikipedia.org/wiki/Computer_History_Museum)
- [Computer Modern](https://en.wikipedia.org/wiki/Computer_Modern)
- [Computer language](https://en.wikipedia.org/wiki/Computer_language)
- [Computer program](https://en.wikipedia.org/wiki/Computer_program)
- [Computers and Typesetting](https://en.wikipedia.org/wiki/Computers_and_Typesetting)
- [Concrete Mathematics](https://en.wikipedia.org/wiki/Concrete_Mathematics)
- [Concrete Roman](https://en.wikipedia.org/wiki/Concrete_Roman)
- [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- [Cornell box](https://en.wikipedia.org/wiki/Cornell_box)
- [Corrado Böhm](https://en.wikipedia.org/wiki/Corrado_B%C3%B6hm)
- [Dancing Links](https://en.wikipedia.org/wiki/Dancing_Links)
- [Data compression](https://en.wikipedia.org/wiki/Data_compression)
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)
- [EBU colour bars](https://en.wikipedia.org/wiki/EBU_colour_bars)
- [EIA 1956 resolution chart](https://en.wikipedia.org/wiki/EIA_1956_resolution_chart)
- [EICAR test file](https://en.wikipedia.org/wiki/EICAR_test_file)
- [ETP-1](https://en.wikipedia.org/wiki/ETP-1)
- [EURion constellation](https://en.wikipedia.org/wiki/EURion_constellation)
- [Etaoin shrdlu](https://en.wikipedia.org/wiki/Etaoin_shrdlu)
- [Filler text](https://en.wikipedia.org/wiki/Filler_text)
- [Film leader](https://en.wikipedia.org/wiki/Film_leader)
- [Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)
- [Flowchart](https://en.wikipedia.org/wiki/Flowchart)
- [Font](https://en.wikipedia.org/wiki/Font)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Friedrich L. Bauer](https://en.wikipedia.org/wiki/Friedrich_L._Bauer)
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [Gian-Carlo Rota](https://en.wikipedia.org/wiki/Gian-Carlo_Rota)
- [GTUBE](https://en.wikipedia.org/wiki/GTUBE)
- [Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper)
- [Grimm's law](https://en.wikipedia.org/wiki/Grimm%27s_law)
- [Hamburgevons](https://en.wikipedia.org/wiki/Hamburgevons)
- [Harvard sentences](https://en.wikipedia.org/wiki/Harvard_sentences)
- [Haskell Curry](https://en.wikipedia.org/wiki/Haskell_Curry)
- [Heinz Rutishauser](https://en.wikipedia.org/wiki/Heinz_Rutishauser)
- [Herman Goldstine](https://en.wikipedia.org/wiki/Herman_Goldstine)
- [Hutter Prize](https://en.wikipedia.org/wiki/Hutter_Prize)
- [Input/output](https://en.wikipedia.org/wiki/Input/output)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ImageNet](https://en.wikipedia.org/wiki/ImageNet)
- [Indian-head test pattern](https://en.wikipedia.org/wiki/Indian-head_test_pattern)
- [Iteration](https://en.wikipedia.org/wiki/Iteration)
- [Jack Howlett](https://en.wikipedia.org/wiki/Jack_Howlett)
- [John Backus](https://en.wikipedia.org/wiki/John_Backus)
- [John Mauchly](https://en.wikipedia.org/wiki/John_Mauchly)
- [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Klaus Samelson](https://en.wikipedia.org/wiki/Klaus_Samelson)
- [Knuth's Algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
- [Knuth's Simpath algorithm](https://en.wikipedia.org/wiki/Knuth%27s_Simpath_algorithm)
- [Knuth's up-arrow notation](https://en.wikipedia.org/wiki/Knuth%27s_up-arrow_notation)
- [Knuth Prize](https://en.wikipedia.org/wiki/Knuth_Prize)
- [Knuth reward check](https://en.wikipedia.org/wiki/Knuth_reward_check)
- [Knuth–Bendix completion algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Bendix_completion_algorithm)
- [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)
- [Konrad Zuse](https://en.wikipedia.org/wiki/Konrad_Zuse)
- [Laning and Zierler system](https://en.wikipedia.org/wiki/Laning_and_Zierler_system)
- [Lenna](https://en.wikipedia.org/wiki/Lenna)
- [List of BBC test cards](https://en.wikipedia.org/wiki/List_of_BBC_test_cards)
- [List of common 3D test models](https://en.wikipedia.org/wiki/List_of_common_3D_test_models)
- [List of datasets for machine-learning research](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research)
- [Literate programming](https://en.wikipedia.org/wiki/Literate_programming)
- [Lorem ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)
- [MATH-MATIC](https://en.wikipedia.org/wiki/MATH-MATIC)
- [MIX (abstract machine)](https://en.wikipedia.org/wiki/MIX_(abstract_machine))
- [MMIX](https://en.wikipedia.org/wiki/MMIX)
- [MNIST database](https://en.wikipedia.org/wiki/MNIST_database)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Man or boy test](https://en.wikipedia.org/wiki/Man_or_boy_test)
- [Manchester Mark 1](https://en.wikipedia.org/wiki/Manchester_Mark_1)
- [Metafont](https://en.wikipedia.org/wiki/Metafont)
- [Nicholas Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis)
- [Pangram](https://en.wikipedia.org/wiki/Pangram)
- [Philips PM5540](https://en.wikipedia.org/wiki/Philips_PM5540)
- [Philips circle pattern](https://en.wikipedia.org/wiki/Philips_circle_pattern)
- [Plankalkül](https://en.wikipedia.org/wiki/Plankalk%C3%BCl)
- [Potrzebie](https://en.wikipedia.org/wiki/Potrzebie)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quater-imaginary base](https://en.wikipedia.org/wiki/Quater-imaginary_base)
- [Quine (computing)](https://en.wikipedia.org/wiki/Quine_(computing))
- [Reference implementation](https://en.wikipedia.org/wiki/Reference_implementation)
- [Robinson–Schensted–Knuth correspondence](https://en.wikipedia.org/wiki/Robinson%E2%80%93Schensted%E2%80%93Knuth_correspondence)
- [Rosetta Code](https://en.wikipedia.org/wiki/Rosetta_Code)
- [Rust (programming language)](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [SMPTE color bars](https://en.wikipedia.org/wiki/SMPTE_color_bars)
- [Sanity check](https://en.wikipedia.org/wiki/Sanity_check)
- [Selected papers series of Knuth](https://en.wikipedia.org/wiki/Selected_papers_series_of_Knuth)
- [Shakedown (testing)](https://en.wikipedia.org/wiki/Shakedown_(testing))
- [Short Code (computer language)](https://en.wikipedia.org/wiki/Short_Code_(computer_language))
- [Snell & Wilcox Zone Plate](https://en.wikipedia.org/wiki/Snell_%26_Wilcox_Zone_Plate)
- [Software](https://en.wikipedia.org/wiki/Software)
- [Standard test image](https://en.wikipedia.org/wiki/Standard_test_image)
- [Stanford bunny](https://en.wikipedia.org/wiki/Stanford_bunny)
- [Stanford dragon](https://en.wikipedia.org/wiki/Stanford_dragon)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [Surreal number](https://en.wikipedia.org/wiki/Surreal_number)
- [TVE test card](https://en.wikipedia.org/wiki/TVE_test_card)
- [TeX](https://en.wikipedia.org/wiki/TeX)
- [Telefunken FuBK](https://en.wikipedia.org/wiki/Telefunken_FuBK)
- [Test Card F](https://en.wikipedia.org/wiki/Test_Card_F)
- [Test Card F](https://en.wikipedia.org/wiki/Test_Card_F)
- [Test Card F](https://en.wikipedia.org/wiki/Test_Card_F)
- [Test Card F](https://en.wikipedia.org/wiki/Test_Card_F)
- [Test card](https://en.wikipedia.org/wiki/Test_card)
- [Test functions for optimization](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
- [The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)
- [The Complexity of Songs](https://en.wikipedia.org/wiki/The_Complexity_of_Songs)
- [The North Wind and the Sun](https://en.wikipedia.org/wiki/The_North_Wind_and_the_Sun)
- [The quick brown fox jumps over the lazy dog](https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog)
- [Things a Computer Scientist Rarely Talks About](https://en.wikipedia.org/wiki/Things_a_Computer_Scientist_Rarely_Talks_About)
- [Tom's Diner](https://en.wikipedia.org/wiki/Tom%27s_Diner)
- [Tony Brooker](https://en.wikipedia.org/wiki/Tony_Brooker)
- [TPK algorithm](https://en.wikipedia.org/wiki/TPK_algorithm)
- [Turing test](https://en.wikipedia.org/wiki/Turing_test)
- [Typography](https://en.wikipedia.org/wiki/Typography)
- [Universal Electronic Test Chart](https://en.wikipedia.org/wiki/Universal_Electronic_Test_Chart)
- [Utah teapot](https://en.wikipedia.org/wiki/Utah_teapot)
- [Web (programming system)](https://en.wikipedia.org/wiki/Web_(programming_system))
- [Webdriver Torso](https://en.wikipedia.org/wiki/Webdriver_Torso)
- [Template:Donald Knuth](https://en.wikipedia.org/wiki/Template:Donald_Knuth)
- [Template:Standard test item](https://en.wikipedia.org/wiki/Template:Standard_test_item)
- [Template talk:Donald Knuth](https://en.wikipedia.org/wiki/Template_talk:Donald_Knuth)
- [Template talk:Standard test item](https://en.wikipedia.org/wiki/Template_talk:Standard_test_item)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:46:02.852076+00:00_