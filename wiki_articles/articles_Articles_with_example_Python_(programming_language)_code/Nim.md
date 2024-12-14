# Nim

## Article Metadata

- **Last Updated:** 2024-12-14T19:41:34.845675+00:00
- **Original Article:** [Nim](https://en.wikipedia.org/wiki/Nim)
- **Language:** en
- **Page ID:** 21885

## Summary

Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. Depending on the version being played, the goal of the game is either to avoid taking the last object or to take the last object.
Nim is fundamental to the Sprague–Grundy theorem, which essentially says that every impartial

## Categories

- Category:Articles containing Chinese-language text
- Category:Articles containing German-language text
- Category:Articles containing proofs
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1: long volume value
- Category:Combinatorial game theory
- Category:Commons category link from Wikidata
- Category:Mathematical games
- Category:Pages containing links to subscription-only content
- Category:Short description matches Wikidata
- Category:Solved games

## Table of Contents

- History
- Game play and illustration
- Winning positions
- Mathematical theory
- Proof of the winning formula
- Variations
- See also
- References
- Further reading
- External links

## Content

Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. Depending on the version being played, the goal of the game is either to avoid taking the last object or to take the last object.
Nim is fundamental to the Sprague–Grundy theorem, which essentially says that every impartial game is equivalent to a nim game with a single pile.

History
Variants of nim have been played since ancient times. The game is said to have originated in China—it closely resembles the Chinese game of jiǎn-shízi (捡石子), or "picking stones"—but the origin is uncertain; the earliest European references to nim are from the beginning of the 16th century. Its current name was coined by Charles L. Bouton of Harvard University, who also developed the complete theory of the game in 1901, but the origins of the name were never fully explained. The Oxford English Dictionary derives the name from the German verb nimm, meaning "take".
At the 1939 New York World's Fair Westinghouse displayed a machine, the Nimatron, that played nim. From May 11 to October 27, 1940, only a few people were able to beat the machine in that six-month period; if they did, they were presented with a coin that said "Nim Champ". It was also one of the first-ever electronic computerized games. Ferranti built a nim-playing computer which was displayed at the Festival of Britain in 1951. In 1952, Herbert Koppel, Eugene Grant and Howard Bailer, engineers from the W. L. Maxson Corporation, developed a machine weighing 23 kilograms (50 lb) which played nim against a human opponent and regularly won. A nim playing machine has been described made from tinkertoys.
The game of nim was the subject of Martin Gardner's February 1958 Mathematical Games column in Scientific American. A version of nim is played—and has symbolic importance—in the French New Wave film Last Year at Marienbad (1961).

Game play and illustration
Nim is typically played as a misère game, in which the player to take the last object loses. Nim can also be played as a "normal play" game whereby the player taking the last object wins.  In either normal play or a misère game, when there is exactly one heap with at least two objects, the player who takes next can easily win. If this removes either all or all but one objects from the heap that has two or more, then no heaps will have more than one object, so the players are forced to alternate removing exactly one object until the game ends. If the player leaves an even number of non-zero heaps (as the player would do in normal play), the player takes last; if the player leaves an odd number of heaps (as the player would do in misère play), then the other player takes last.
The normal game is between two players and is played with three heaps of any number of objects. The two players alternate taking any number of objects from any one of the heaps. The goal is to be the last to take an object. In misère play, the goal is instead to ensure that the opponent is forced to take the last remaining object.
The following example of a normal game is played between fictional players Bob and Alice, who start with heaps of three, four and five objects.

Winning positions
The practical strategy to win at the game of nim is for a player to get the other into one of the following positions, and every successive turn afterwards they should be able to make one of the smaller positions. Only the last move changes between misère and normal play.

For the generalisations, n and m can be any value > 0, and they may be the same.

Mathematical theory
Normal-play nim (or more precisely the system of nimbers) is fundamental to the Sprague–Grundy theorem, which essentially says that in normal play every impartial game is equivalent to a nim heap that yields the same outcome when played in parallel with other normal play impartial games (see disjunctive sum).
While all normal-play impartial games can be assigned a nim value, that is not the case under the misère convention. Only tame games can be played using the same strategy as misère nim.
Nim is a special case of a poset game where the poset consists of disjoint chains (the heaps).
The evolution graph of the game of nim with three heaps is the same as three branches of the evolution graph of the Ulam–Warburton automaton.
Nim has been mathematically solved for any number of initial heaps and objects, and there is an easily calculated way to determine which player will win and which winning moves are open to that player.
The key to the theory of the game is the binary digital sum of the heap sizes, i.e., the sum (in binary), neglecting all carries from one digit to another. This operation is also known as "bitwise xor" or "vector addition over GF(2)" (bitwise addition modulo 2). Within combinatorial game theory it is usually called the nim-sum, as it will be called here. The nim-sum of x and y is written x ⊕ y to distinguish it from the ordinary sum, x + y. An example of the calculation with heaps of size 3, 4, and 5 is as follows:

Binary Decimal
 
  0112    310    Heap A
  1002    410    Heap B
  1012    510    Heap C
  ---
  0102    210    The nim-sum of heaps A, B, and C, 3 ⊕ 4 ⊕ 5 = 2

An equivalent procedure, which is often easier to perform mentally, is to express the heap sizes as sums of distinct powers of 2, cancel pairs of equal powers, and then add what is left:

3 = 0 + 2 + 1 =     2   1      Heap A
4 = 4 + 0 + 0 = 4              Heap B
5 = 4 + 0 + 1 = 4       1      Heap C
--------------------------------------------------------------------
2 =                 2          What is left after canceling 1s and 4s

In normal play, the winning strategy is to finish every move with a nim-sum of 0. This is always possible if the nim-sum is not zero before the move. If the nim-sum is zero, then the next player will lose if the other player does not make a mistake. To find out which move to make, let X be the nim-sum of all the heap sizes. Find a heap where the nim-sum of X and heap-size is less than the heap-size; the winning strategy is to play in such a heap, reducing that heap to the nim-sum of its original size with X. In the example above, taking the nim-sum of the sizes is X = 3 ⊕ 4 ⊕ 5 = 2. The nim-sums of the heap sizes A=3, B=4, and C=5 with X=2 are

A ⊕ X = 3 ⊕ 2 = 1      [Since (011) ⊕ (010) = 001 ]
B ⊕ X = 4 ⊕ 2 = 6
C ⊕ X = 5 ⊕ 2 = 7
The only heap that is reduced is heap A, so the winning move is to reduce the size of heap A to 1 (by removing two objects).
As a particular simple case, if there are only two heaps left, the strategy is to reduce the number of objects in the bigger heap to make the heaps equal. After that, no matter what move the opponent makes, the player can make the same move on the other heap, guaranteeing that they take the last object.
When played as a misère game, nim strategy is different only when the normal play move would leave only heaps of size one. In that case, the correct move is to leave an odd number of heaps of size one (in normal play, the correct move would be to leave an even number of such heaps).
These strategies for normal play and a misère game are the same until the number of heaps with at least two objects is exactly equal to one. At that point, the next player removes either all objects (or all but one) from the heap that has two or more, so no heaps will have more than one object (in other words, so all remaining heaps have exactly one object each), so the players are forced to alternate removing exactly one object until the game ends. In normal play, the player leaves an even number of non-zero heaps, so the same player takes last; in misère play, the player leaves an odd number of non-zero heaps, so the other player takes last.
In a misère game with heaps of sizes three, four and five, the strategy would be applied like this:

Proof of the winning formula
The soundness of the optimal strategy described above was demonstrated by C. Bouton.
Theorem. In a normal nim game, the player making the first move has a winning strategy if and only if the nim-sum of the sizes of the heaps is not zero. Otherwise, the second player has a winning strategy.
Proof: Notice that the nim-sum (⊕) obeys the usual associative and commutative laws of addition (+) and also satisfies an additional property, x ⊕ x = 0.
Let x1, ..., xn be the sizes of the heaps before a move, and y1, ..., yn the corresponding sizes after a move. Let s = x1 ⊕ ... ⊕ xn and t = y1 ⊕ ... ⊕ yn. If the move was in heap k, we have xi = yi for all i ≠ k, and xk > yk. By the properties of ⊕ mentioned above, we have

  
    
      
        
          
            
              
                t
              
              
                
                =
                0
                ⊕
                t
              
            
            
              
              
                
                =
                s
                ⊕
                s
                ⊕
                t
              
            
            
              
              
                
                =
                s
                ⊕
                (
                
                  x
                  
                    1
                  
                
                ⊕
                ⋯
                ⊕
                
                  x
                  
                    n
                  
                
                )
                ⊕
                (
                
                  y
                  
                    1
                  
                
                ⊕
                ⋯
                ⊕
                
                  y
                  
                    n
                  
                
                )
              
            
            
              
              
                
                =
                s
                ⊕
                (
                
                  x
                  
                    1
                  
                
                ⊕
                
                  y
                  
                    1
                  
                
                )
                ⊕
                ⋯
                ⊕
                (
                
                  x
                  
                    n
                  
                
                ⊕
                
                  y
                  
                    n
                  
                
                )
              
            
            
              
              
                
                =
                s
                ⊕
                0
                ⊕
                ⋯
                ⊕
                0
                ⊕
                (
                
                  x
                  
                    k
                  
                
                ⊕
                
                  y
                  
                    k
                  
                
                )
                ⊕
                0
                ⊕
                ⋯
                ⊕
                0
              
            
            
              
              
                
                =
                s
                ⊕
                
                  x
                  
                    k
                  
                
                ⊕
                
                  y
                  
                    k
                  
                
              
            
            
              
                (
                ∗
                )
                
                t
              
              
                
                =
                s
                ⊕
                
                  x
                  
                    k
                  
                
                ⊕
                
                  y
                  
                    k
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}t&=0\oplus t\\&=s\oplus s\oplus t\\&=s\oplus (x_{1}\oplus \cdots \oplus x_{n})\oplus (y_{1}\oplus \cdots \oplus y_{n})\\&=s\oplus (x_{1}\oplus y_{1})\oplus \cdots \oplus (x_{n}\oplus y_{n})\\&=s\oplus 0\oplus \cdots \oplus 0\oplus (x_{k}\oplus y_{k})\oplus 0\oplus \cdots \oplus 0\\&=s\oplus x_{k}\oplus y_{k}\\[10pt](*)\quad t&=s\oplus x_{k}\oplus y_{k}\end{aligned}}}
  

The theorem follows by induction on the length of the game from these two lemmas.
Lemma 1. If s = 0, then t ≠ 0 no matter what move is made.
Proof: If there is no possible move, then the lemma is vacuously true (and the first player loses the normal play game by definition). Otherwise, any move in heap k will produce t = xk ⊕ yk from (*). This number is nonzero, since xk ≠ yk.
Lemma 2. If s ≠ 0, it is possible to make a move so that t = 0.
Proof: Let d be the position of the leftmost (most significant) nonzero bit in the binary representation of s, and choose k such that the dth bit of xk is also nonzero. (Such a k must exist, since otherwise the dth bit of s would be 0.)
Then letting yk = s ⊕ xk, we claim that yk < xk: all bits to the left of d are the same in xk and yk, bit d decreases from 1 to 0 (decreasing the value by 2d), and any change in the remaining bits will amount to at most 2d−1. The first player can thus make a move by taking xk − yk objects from heap k, then

t = s ⊕ xk ⊕ yk           (by (*))
  = s ⊕ xk ⊕ (s ⊕ xk)
  = 0.

The modification for misère play is demonstrated by noting that the modification first arises in a position that has only one heap of size 2 or more. Notice that in such a position s ≠ 0, and therefore this situation has to arise when it is the turn of the player following the winning strategy. The normal play strategy is for the player to reduce this to size 0 or 1, leaving an even number of heaps with size 1, and the misère strategy is to do the opposite. From that point on, all moves are forced.

Variations
The subtraction game
In another game which is commonly known as nim (but is better called the subtraction game), an upper bound is imposed on the number of objects that can be removed in a turn. Instead of removing arbitrarily many objects, a player can only remove 1 or 2 or ... or k at a time. This game is commonly played in practice with only one heap.
Bouton's analysis carries over easily to the general multiple-heap version of this game. The only difference is that as a first step, before computing the nim-sums we must reduce the sizes of the heaps modulo k + 1. If this makes all the heaps of size zero (in misère play), the winning move is to take k objects from one of the heaps. In particular, in ideal play from a single heap of n objects, the second player can win if and only if

0 = n (mod k + 1) (in normal play), or
1 = n (mod k + 1) (in misère play).
This follows from calculating the nim-sequence of S(1, 2, ..., k),

  
    
      
        0.123
        …
        k
        0123
        …
        k
        0123
        …
        =
        
          
            
              0
              ˙
            
          
        
        .123
        …
        
          
            
              k
              ˙
            
          
        
        ,
      
    
    {\displaystyle 0.123\ldots k0123\ldots k0123\ldots ={\dot {0}}.123\ldots {\dot {k}},}
  

from which the strategy above follows by the Sprague–Grundy theorem.

The 21 game
The game "21" is played as a misère game with any number of players who take turns saying a number. The first player says "1" and each player in turn increases the number by 1, 2, or 3, but may not exceed 21; the player forced to say "21" loses. This can be modeled as a subtraction game with a heap of 21 − n objects. The winning strategy for the two-player version of this game is to always say a multiple of 4; it is then guaranteed that the other player will ultimately have to say 21; so in the standard version, wherein the first player opens with "1", they start with a losing move.
The 21 game can also be played with different numbers, e.g., "Add at most 5; lose on 34".
A sample game of 21 in which the second player follows the winning strategy:

The 100 game
A similar version is the "100 game": Two players start from 0 and alternately add a number from 1 to 10 to the sum. The player who reaches 100 wins. The winning strategy is to reach a number in which the digits are subsequent (e.g., 01, 12, 23, 34,...) and control the game by jumping through all the numbers of this sequence. Once a player reaches 89, the opponent can only choose numbers from 90 to 99, and the next answer can in any case be 100.

A multiple-heap rule
In another variation of nim, besides removing any number of objects from a single heap, one is permitted to remove the same number of objects from each heap.

Circular nim
Yet another variation of nim is "circular nim", wherein any number of objects are placed in a circle and two players alternately remove one, two or three adjacent objects. For example, starting with a circle of ten objects,

. . . . . . . . . .

three objects are taken in the first move

_ . . . . . . . _ _

then another three

_ . _ _ _ . . . _ _

then one

_ . _ _ _ . . _ _ _

but then three objects cannot be taken out in one move.

Grundy's game
In Grundy's game, another variation of nim, a number of objects are placed in an initial heap and two players alternately divide a heap into two nonempty heaps of different sizes. Thus, six objects may be divided into piles of 5+1 or 4+2, but not 3+3. Grundy's game can be played as either misère or normal play.

Greedy nim
Greedy nim is a variation wherein the players are restricted to choosing stones from only the largest pile. It is a finite impartial game. Greedy nim misère has the same rules as greedy nim, but the last player able to make a move loses.
Let the largest number of stones in a pile be m and the second largest number of stones in a pile be n. Let pm be the number of piles having m stones and pn be the number of piles having n stones. Then there is a theorem that game positions with pm even are P positions.
 This theorem can be shown by considering the positions where pm is odd. If pm is larger than 1, all stones may be removed from this pile to reduce pm by 1 and the new pm will be even. If pm = 1 (i.e. the largest heap is unique), there are two cases:

If pn is odd, the size of the largest heap is reduced to n (so now the new pm is even).
If pn is even, the largest heap is removed entirely, leaving an even number of largest heaps.
Thus, there exists a move to a state where pm is even. Conversely, if pm is even, if any move is possible (pm ≠ 0), then it must take the game to a state where pm is odd. The final position of the game is even (pm = 0). Hence, each position of the game with pm even must be a P position.

Index-k nim
A generalization of multi-heap nim was called "nim
  
    
      
        
          

          
          
            k
          
        
      
    
    {\displaystyle {}_{k}}
  
" or "index-k" nim by E. H. Moore, who analyzed it in 1910. In index-k nim, instead of removing objects from only one heap, players can remove objects from at least one but up to k different heaps. The number of elements that may be removed from each heap may be either arbitrary or limited to at most r elements, like in the "subtraction game" above.
The winning strategy is as follows: Like in ordinary multi-heap nim, one considers the binary representation of the heap sizes (or heap sizes modulo r + 1). In ordinary nim one forms the XOR-sum (or sum modulo 2) of each binary digit, and the winning strategy is to make each XOR sum zero. In the generalization to index-k nim, one forms the sum of each binary digit modulo k + 1.
Again, the winning strategy is to move such that this sum is zero for every digit. Indeed, the value thus computed is zero for the final position, and given a configuration of heaps for which this value is zero, any change of at most k heaps will make the value non-zero. Conversely, given a configuration with non-zero value, one can always take from at most k heaps, carefully chosen, so that the value will become zero.

Building nim
Building nim is a variant of nim wherein the two players first construct the game of nim. Given n stones and s empty piles, the players, alternating turns, place exactly one stone into a pile of their choice. Once all the stones are placed, a game of Nim begins, starting with the next player that would move. This game is denoted BN(n,s).

Higher-dimensional nim
n-d nim is played on a 
  
    
      
        
          k
          
            1
          
        
        ×
        ⋯
        ×
        
          k
          
            n
          
        
      
    
    {\displaystyle k_{1}\times \dots \times k_{n}}
  
 board, whereon any number of continuous pieces can be removed from any hyper-row. The starting position is usually the full board, but other options are allowed.

Graph nim
The starting board is a disconnected graph, and players take turns to remove adjacent vertices.

Candy nim
Candy nim is a version of normal-play nim in which players try to achieve two goals at the same time: taking the last object (in this case, candy) and taking the maximum number of candies by the end of the game.

See also
References
Further reading
W. W. Rouse Ball: Mathematical Recreations and Essays, The Macmillan Company, 1947.
John D. Beasley: The Mathematics of Games, Oxford University Press, 1989.
Elwyn R. Berlekamp, John H. Conway, and Richard K. Guy: Winning Ways for your Mathematical Plays, Academic Press, Inc., 1982.
Manfred Eigen and Ruthild Winkler: Laws of the Game, Princeton University Press, 1981.
Walter R. Fuchs: Computers: Information Theory and Cybernetics, Rupert Hart-Davis Educational Publications, 1971.
G. H. Hardy and E. M. Wright: An Introduction to the Theory of Numbers, Oxford University Press, 1979.
Edward Kasner and James Newman: Mathematics and the Imagination, Simon and Schuster, 1940.
M. Kaitchik: Mathematical Recreations, W. W. Norton, 1942.
Donald D. Spencer: Game Playing with Computers, Hayden Book Company, Inc., 1968.

External links

"50-pound computer plays Nim" – The New Yorker - "Talk of the Town" August, 1952 (subscription required)
The hot game of Nim – Nim theory and connections with other games at cut-the-knot
Nim and 2-dimensional SuperNim at cut-the-knot

## Related Articles

### Internal Links

- [1939 New York World's Fair](https://en.wikipedia.org/wiki/1939_New_York_World%27s_Fair)
- [21 (drinking game)](https://en.wikipedia.org/wiki/21_(drinking_game))
- [Abstract strategy game](https://en.wikipedia.org/wiki/Abstract_strategy_game)
- [Alain Robbe-Grillet](https://en.wikipedia.org/wiki/Alain_Robbe-Grillet)
- [American Mathematical Society](https://en.wikipedia.org/wiki/American_Mathematical_Society)
- [Android Nim](https://en.wikipedia.org/wiki/Android_Nim)
- [Annals of Mathematics](https://en.wikipedia.org/wiki/Annals_of_Mathematics)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Associative property](https://en.wikipedia.org/wiki/Associative_property)
- [Binary number](https://en.wikipedia.org/wiki/Binary_number)
- [Bitwise operation](https://en.wikipedia.org/wiki/Bitwise_operation)
- [Alice and Bob](https://en.wikipedia.org/wiki/Alice_and_Bob)
- [Charles L. Bouton](https://en.wikipedia.org/wiki/Charles_L._Bouton)
- [China](https://en.wikipedia.org/wiki/China)
- [Chomp](https://en.wikipedia.org/wiki/Chomp)
- [Combinatorial game theory](https://en.wikipedia.org/wiki/Combinatorial_game_theory)
- [Commutative property](https://en.wikipedia.org/wiki/Commutative_property)
- [Alexander Bogomolny](https://en.wikipedia.org/wiki/Alexander_Bogomolny)
- [Decimal](https://en.wikipedia.org/wiki/Decimal)
- [Digital sum in base b](https://en.wikipedia.org/wiki/Digital_sum_in_base_b)
- [Disjunctive sum](https://en.wikipedia.org/wiki/Disjunctive_sum)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dr. Nim](https://en.wikipedia.org/wiki/Dr._Nim)
- [E. H. Moore](https://en.wikipedia.org/wiki/E._H._Moore)
- [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)
- [Ferranti](https://en.wikipedia.org/wiki/Ferranti)
- [Festival of Britain](https://en.wikipedia.org/wiki/Festival_of_Britain)
- [Fibonacci nim](https://en.wikipedia.org/wiki/Fibonacci_nim)
- [Finite field](https://en.wikipedia.org/wiki/Finite_field)
- [French New Wave](https://en.wikipedia.org/wiki/French_New_Wave)
- [Fuzzy game](https://en.wikipedia.org/wiki/Fuzzy_game)
- [Strategy game](https://en.wikipedia.org/wiki/Strategy_game)
- [Genus theory](https://en.wikipedia.org/wiki/Genus_theory)
- [Grundy's game](https://en.wikipedia.org/wiki/Grundy%27s_game)
- [Hackenbush](https://en.wikipedia.org/wiki/Hackenbush)
- [Harvard University](https://en.wikipedia.org/wiki/Harvard_University)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [If and only if](https://en.wikipedia.org/wiki/If_and_only_if)
- [Impartial game](https://en.wikipedia.org/wiki/Impartial_game)
- [Isaak Yaglom](https://en.wikipedia.org/wiki/Isaak_Yaglom)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Kayles](https://en.wikipedia.org/wiki/Kayles)
- [Last Year at Marienbad](https://en.wikipedia.org/wiki/Last_Year_at_Marienbad)
- [Mathematical Reviews](https://en.wikipedia.org/wiki/Mathematical_Reviews)
- [Manfred Eigen](https://en.wikipedia.org/wiki/Manfred_Eigen)
- [Martin Gardner](https://en.wikipedia.org/wiki/Martin_Gardner)
- [List of Martin Gardner Mathematical Games columns](https://en.wikipedia.org/wiki/List_of_Martin_Gardner_Mathematical_Games_columns)
- [Mathematical game](https://en.wikipedia.org/wiki/Mathematical_game)
- [Mathematics and the Imagination](https://en.wikipedia.org/wiki/Mathematics_and_the_Imagination)
- [Misère](https://en.wikipedia.org/wiki/Mis%C3%A8re)
- [Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)
- [Sprague–Grundy theorem](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
- [NIM](https://en.wikipedia.org/wiki/NIM)
- [Nim (programming language)](https://en.wikipedia.org/wiki/Nim_(programming_language))
- [Nimatron](https://en.wikipedia.org/wiki/Nimatron)
- [Nimber](https://en.wikipedia.org/wiki/Nimber)
- [Nimrod (computer)](https://en.wikipedia.org/wiki/Nimrod_(computer))
- [Notakto](https://en.wikipedia.org/wiki/Notakto)
- [Octal game](https://en.wikipedia.org/wiki/Octal_game)
- [Oxford English Dictionary](https://en.wikipedia.org/wiki/Oxford_English_Dictionary)
- [Partially ordered set](https://en.wikipedia.org/wiki/Partially_ordered_set)
- [Poset game](https://en.wikipedia.org/wiki/Poset_game)
- [Raymond Redheffer](https://en.wikipedia.org/wiki/Raymond_Redheffer)
- [Ruthild Winkler](https://en.wikipedia.org/wiki/Ruthild_Winkler)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Scientific American](https://en.wikipedia.org/wiki/Scientific_American)
- [Sergei Tabachnikov](https://en.wikipedia.org/wiki/Sergei_Tabachnikov)
- [Silvia Heubach](https://en.wikipedia.org/wiki/Silvia_Heubach)
- [Solved game](https://en.wikipedia.org/wiki/Solved_game)
- [Sprague–Grundy theorem](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
- [Star (game theory)](https://en.wikipedia.org/wiki/Star_(game_theory))
- [Subtract a square](https://en.wikipedia.org/wiki/Subtract_a_square)
- [Subtraction game](https://en.wikipedia.org/wiki/Subtraction_game)
- [The New Yorker](https://en.wikipedia.org/wiki/The_New_Yorker)
- [Tinkertoy](https://en.wikipedia.org/wiki/Tinkertoy)
- [Total order](https://en.wikipedia.org/wiki/Total_order)
- [Tri-nim](https://en.wikipedia.org/wiki/Tri-nim)
- [Turing Tumble](https://en.wikipedia.org/wiki/Turing_Tumble)
- [Ulam–Warburton automaton](https://en.wikipedia.org/wiki/Ulam%E2%80%93Warburton_automaton)
- [Vacuous truth](https://en.wikipedia.org/wiki/Vacuous_truth)
- [Westinghouse Electric Corporation](https://en.wikipedia.org/wiki/Westinghouse_Electric_Corporation)
- [Winning Ways for Your Mathematical Plays](https://en.wikipedia.org/wiki/Winning_Ways_for_Your_Mathematical_Plays)
- [Wythoff's game](https://en.wikipedia.org/wiki/Wythoff%27s_game)
- [Zero game](https://en.wikipedia.org/wiki/Zero_game)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:41:34.845675+00:00_