# Barnsley fern

## Article Metadata

- **Last Updated:** 2024-12-14T19:33:18.402045+00:00
- **Original Article:** [Barnsley fern](https://en.wikipedia.org/wiki/Barnsley_fern)
- **Language:** en
- **Page ID:** 25721564

## Summary

The Barnsley fern is a fractal named after the British mathematician Michael Barnsley who first described it in his book Fractals Everywhere. He made it to resemble the black spleenwort, Asplenium adiantum-nigrum.

## Categories

- Category:Affine geometry
- Category:Articles with example Python (programming language) code
- Category:Articles with example R code
- Category:Articles with short description
- Category:L-systems
- Category:Short description matches Wikidata

## Table of Contents

- History
- Construction
- Pseudocode

## Content

The Barnsley fern is a fractal named after the British mathematician Michael Barnsley who first described it in his book Fractals Everywhere. He made it to resemble the black spleenwort, Asplenium adiantum-nigrum.

History
The fern is one of the basic examples of self-similar sets, i.e. it is a mathematically generated pattern that can be reproducible at any magnification or reduction. Like the Sierpinski triangle, the Barnsley fern shows how graphically beautiful structures can be built from repetitive uses of mathematical formulas with computers. Barnsley's 1988 book Fractals Everywhere is based on the course which he taught for undergraduate and graduate students in the School of Mathematics, Georgia Institute of Technology, called Fractal Geometry. After publishing the book, a second course was developed, called Fractal Measure Theory. Barnsley's work has been a source of inspiration to graphic artists attempting to imitate nature with mathematical models.
The fern code developed by Barnsley is an example of an iterated function system (IFS) to create a fractal. This follows from the collage theorem. He has used fractals to model a diverse range of phenomena
in science and technology, but most specifically plant structures.

IFSs provide models for certain plants, leaves, and ferns, by virtue of the self-similarity which often occurs in branching structures in nature. But nature also exhibits randomness and variation from one level to the next; no two ferns are exactly alike, and the branching fronds become leaves at a smaller scale. V-variable fractals allow for such randomness and variability across scales, while at the same time admitting a continuous dependence on parameters which facilitates geometrical modelling. These factors allow us to make the hybrid biological models...
...we speculate that when a V -variable geometrical fractal model is found that has a good match to the geometry of a given plant, then there is a specific relationship between these code trees and the information stored in the genes of the plant.—Michael Barnsley et al.

Construction
Barnsley's fern uses four affine transformations.  The formula for one transformation is the following:

  
    
      
        
          f
          
            w
          
        
        (
        x
        ,
        y
        )
        =
        
          
            [
            
              
                
                  a
                
                
                  b
                
              
              
                
                  c
                
                
                  d
                
              
            
            ]
          
        
        
          
            [
            
              
                
                  x
                
              
              
                
                  y
                
              
            
            ]
          
        
        +
        
          
            [
            
              
                
                  e
                
              
              
                
                  f
                
              
            
            ]
          
        
      
    
    {\displaystyle f_{w}(x,y)={\begin{bmatrix}a&b\\c&d\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}e\\f\end{bmatrix}}}
  

Barnsley shows the IFS code for his Black Spleenwort fern fractal as a matrix of values shown in a table. In the table, the columns "a" through "f" are the coefficients of the equation, and "p" represents the probability factor.

These correspond to the following transformations:

  
    
      
        
          
            
              
                
                  f
                  
                    1
                  
                
                (
                x
                ,
                y
                )
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.00
                        
                        
                          0.00
                        
                      
                      
                        
                          0.00
                        
                        
                          0.16
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          x
                        
                      
                      
                        
                          y
                        
                      
                    
                    ]
                  
                
              
            
            
              
                
                  f
                  
                    2
                  
                
                (
                x
                ,
                y
                )
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.85
                        
                        
                          0.04
                        
                      
                      
                        
                          −
                          0.04
                        
                        
                          0.85
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          x
                        
                      
                      
                        
                          y
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.00
                        
                      
                      
                        
                          1.60
                        
                      
                    
                    ]
                  
                
              
            
            
              
                
                  f
                  
                    3
                  
                
                (
                x
                ,
                y
                )
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          0.20
                        
                        
                          −
                          0.26
                        
                      
                      
                        
                          0.23
                        
                        
                          0.22
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          x
                        
                      
                      
                        
                          y
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.00
                        
                      
                      
                        
                          1.60
                        
                      
                    
                    ]
                  
                
              
            
            
              
                
                  f
                  
                    4
                  
                
                (
                x
                ,
                y
                )
              
              
                
                =
                
                  
                    [
                    
                      
                        
                          −
                          0.15
                        
                        
                          0.28
                        
                      
                      
                        
                          0.26
                        
                        
                          0.24
                        
                      
                    
                    ]
                  
                
                
                  
                    [
                    
                      
                        
                          x
                        
                      
                      
                        
                          y
                        
                      
                    
                    ]
                  
                
                +
                
                  
                    [
                    
                      
                        
                          0.00
                        
                      
                      
                        
                          0.44
                        
                      
                    
                    ]
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}f_{1}(x,y)&={\begin{bmatrix}0.00&0.00\\0.00&0.16\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}\\[6px]f_{2}(x,y)&={\begin{bmatrix}0.85&0.04\\-0.04&0.85\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}0.00\\1.60\end{bmatrix}}\\[6px]f_{3}(x,y)&={\begin{bmatrix}0.20&-0.26\\0.23&0.22\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}0.00\\1.60\end{bmatrix}}\\[6px]f_{4}(x,y)&={\begin{bmatrix}-0.15&0.28\\0.26&0.24\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}0.00\\0.44\end{bmatrix}}\end{aligned}}}

Computer generation
Though Barnsley's fern could in theory be plotted by hand with a pen and graph paper, the number of iterations necessary runs into the tens of thousands, which makes use of a computer practically mandatory.  Many different computer models of Barnsley's fern are popular with contemporary mathematicians.  As long as math is programmed correctly using Barnsley's matrix of constants, the same fern shape will be produced.
The first point drawn is at the origin (x0 = 0, y0 = 0) and then the new points are iteratively computed by randomly applying one of the following four coordinate transformations:

f1
xn + 1 = 0
yn + 1 = 0.16 yn
This coordinate transformation is chosen 1% of the time and just maps any point to a point in the first line segment at the base of the stem. In the iterative generation, it acts as a reset to the base of the stem. Crucially it does not reset exactly to (0,0) which allows it to fill in the base stem which is translated and serves as a kind of "kernel" from which all other sections of the fern are generated via transformations f2, f3, f4.

f2
xn + 1 = 0.85 xn + 0.04 yn
yn + 1 = −0.04 xn + 0.85 yn + 1.6
This transformation encodes the self-similarity relationship of the entire fern with the sub-structure which consists of the fern with the removal of the section which includes the bottom two leaves. In the matrix representation, it can be seen to be a slight clockwise rotation, scaled to be slightly smaller and translated in the positive y direction. In the iterative generation, this transformation is applied with probability 85% and is intuitively responsible for the generation of the main stem, and the successive vertical generation of the leaves on either side of the stem from their "original" leaves at the base.

f3
xn + 1 = 0.2 xn − 0.26 yn
yn + 1 = 0.23 xn + 0.22 yn + 1.6
This transformation encodes the self-similarity of the entire fern with the bottom left leaf. In the matrix representation, it is seen to be a near-90° counterclockwise rotation, scaled down to approximately 30% size with a translation in the positive y direction. In the iterative generation, it is applied with probability 7% and is intuitively responsible for the generation of the lower-left leaf.

f4
xn + 1 = −0.15 xn + 0.28 yn
yn + 1 = 0.26 xn + 0.24 yn + 0.44
Similarly, this transformation encodes the self-similarity of the entire fern with the bottom right leaf. From its determinant it is easily seen to include a reflection and can be seen as a similar transformation as f3 albeit with a reflection about the y-axis. In the iterative-generation, it is applied with probability 7% and is responsible for the generation of the bottom right leaf.

Mutant varieties
By playing with the coefficients, it is possible to create mutant fern varieties. In his paper on V-variable fractals, Barnsley calls this trait a superfractal.
One experimenter has come up with a table of coefficients to produce another remarkably naturally looking fern however, resembling the Cyclosorus or Thelypteridaceae fern. These are:

Pseudocode


== References ==

## Related Articles

### Internal Links

- [2.5D](https://en.wikipedia.org/wiki/2.5D)
- [2D computer graphics](https://en.wikipedia.org/wiki/2D_computer_graphics)
- [3D computer graphics](https://en.wikipedia.org/wiki/3D_computer_graphics)
- [ASCII art](https://en.wikipedia.org/wiki/ASCII_art)
- [Affine transformation](https://en.wikipedia.org/wiki/Affine_transformation)
- [Aleksandr Lyapunov](https://en.wikipedia.org/wiki/Aleksandr_Lyapunov)
- [Computer animation](https://en.wikipedia.org/wiki/Computer_animation)
- [Anna Ridler](https://en.wikipedia.org/wiki/Anna_Ridler)
- [Apollonian gasket](https://en.wikipedia.org/wiki/Apollonian_gasket)
- [Applications of 3D printing](https://en.wikipedia.org/wiki/Applications_of_3D_printing)
- [Art game](https://en.wikipedia.org/wiki/Art_game)
- [Artfutura](https://en.wikipedia.org/wiki/Artfutura)
- [Artificial intelligence art](https://en.wikipedia.org/wiki/Artificial_intelligence_art)
- [Artmedia](https://en.wikipedia.org/wiki/Artmedia)
- [Asplenium adiantum-nigrum](https://en.wikipedia.org/wiki/Asplenium_adiantum-nigrum)
- [Assouad dimension](https://en.wikipedia.org/wiki/Assouad_dimension)
- [Attractor](https://en.wikipedia.org/wiki/Attractor)
- [Austin Museum of Digital Art](https://en.wikipedia.org/wiki/Austin_Museum_of_Digital_Art)
- [Ben Rubin (artist)](https://en.wikipedia.org/wiki/Ben_Rubin_(artist))
- [Benoit Mandelbrot](https://en.wikipedia.org/wiki/Benoit_Mandelbrot)
- [Bill Gosper](https://en.wikipedia.org/wiki/Bill_Gosper)
- [Blancmange curve](https://en.wikipedia.org/wiki/Blancmange_curve)
- [Brownian motion](https://en.wikipedia.org/wiki/Brownian_motion)
- [Brownian motor](https://en.wikipedia.org/wiki/Brownian_motor)
- [Buddhabrot](https://en.wikipedia.org/wiki/Buddhabrot)
- [Burning Ship fractal](https://en.wikipedia.org/wiki/Burning_Ship_fractal)
- [Camille Utterback](https://en.wikipedia.org/wiki/Camille_Utterback)
- [Cantor set](https://en.wikipedia.org/wiki/Cantor_set)
- [Casey Reas](https://en.wikipedia.org/wiki/Casey_Reas)
- [Chaos: Making a New Science](https://en.wikipedia.org/wiki/Chaos:_Making_a_New_Science)
- [Chaos game](https://en.wikipedia.org/wiki/Chaos_game)
- [Chaos theory](https://en.wikipedia.org/wiki/Chaos_theory)
- [Char Davies](https://en.wikipedia.org/wiki/Char_Davies)
- [Coastline paradox](https://en.wikipedia.org/wiki/Coastline_paradox)
- [Collage theorem](https://en.wikipedia.org/wiki/Collage_theorem)
- [Computer-generated imagery](https://en.wikipedia.org/wiki/Computer-generated_imagery)
- [Computer Arts Society](https://en.wikipedia.org/wiki/Computer_Arts_Society)
- [Computer art](https://en.wikipedia.org/wiki/Computer_art)
- [Computer art scene](https://en.wikipedia.org/wiki/Computer_art_scene)
- [Computer music](https://en.wikipedia.org/wiki/Computer_music)
- [Correlation dimension](https://en.wikipedia.org/wiki/Correlation_dimension)
- [Cory Arcangel](https://en.wikipedia.org/wiki/Cory_Arcangel)
- [Cyberarts](https://en.wikipedia.org/wiki/Cyberarts)
- [Cyclosorus](https://en.wikipedia.org/wiki/Cyclosorus)
- [David Em](https://en.wikipedia.org/wiki/David_Em)
- [De Rham curve](https://en.wikipedia.org/wiki/De_Rham_curve)
- [Desmond Paul Henry](https://en.wikipedia.org/wiki/Desmond_Paul_Henry)
- [Diffusion-limited aggregation](https://en.wikipedia.org/wiki/Diffusion-limited_aggregation)
- [Digital architecture](https://en.wikipedia.org/wiki/Digital_architecture)
- [Digital art](https://en.wikipedia.org/wiki/Digital_art)
- [Digital illustration](https://en.wikipedia.org/wiki/Digital_illustration)
- [Digital imaging](https://en.wikipedia.org/wiki/Digital_imaging)
- [Digital painting](https://en.wikipedia.org/wiki/Digital_painting)
- [Digital photography](https://en.wikipedia.org/wiki/Digital_photography)
- [Digital poetry](https://en.wikipedia.org/wiki/Digital_poetry)
- [Douady rabbit](https://en.wikipedia.org/wiki/Douady_rabbit)
- [Dragon curve](https://en.wikipedia.org/wiki/Dragon_curve)
- [EVA Conferences](https://en.wikipedia.org/wiki/EVA_Conferences)
- [Edmond de Belamy](https://en.wikipedia.org/wiki/Edmond_de_Belamy)
- [Electronic music](https://en.wikipedia.org/wiki/Electronic_music)
- [Eric Millikin](https://en.wikipedia.org/wiki/Eric_Millikin)
- [Evolutionary art](https://en.wikipedia.org/wiki/Evolutionary_art)
- [Felix Hausdorff](https://en.wikipedia.org/wiki/Felix_Hausdorff)
- [Fibonacci word fractal](https://en.wikipedia.org/wiki/Fibonacci_word_fractal)
- [Filled Julia set](https://en.wikipedia.org/wiki/Filled_Julia_set)
- [Fractal](https://en.wikipedia.org/wiki/Fractal)
- [Fractal-generating software](https://en.wikipedia.org/wiki/Fractal-generating_software)
- [Fractal art](https://en.wikipedia.org/wiki/Fractal_art)
- [Fractal canopy](https://en.wikipedia.org/wiki/Fractal_canopy)
- [Fractal dimension](https://en.wikipedia.org/wiki/Fractal_dimension)
- [Fractal landscape](https://en.wikipedia.org/wiki/Fractal_landscape)
- [Fractal string](https://en.wikipedia.org/wiki/Fractal_string)
- [GIF art](https://en.wikipedia.org/wiki/GIF_art)
- [Gaston Julia](https://en.wikipedia.org/wiki/Gaston_Julia)
- [Generative art](https://en.wikipedia.org/wiki/Generative_art)
- [Generative artificial intelligence](https://en.wikipedia.org/wiki/Generative_artificial_intelligence)
- [Generative music](https://en.wikipedia.org/wiki/Generative_music)
- [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor)
- [Georgia Tech](https://en.wikipedia.org/wiki/Georgia_Tech)
- [Glitch art](https://en.wikipedia.org/wiki/Glitch_art)
- [Gosper curve](https://en.wikipedia.org/wiki/Gosper_curve)
- [Graphic art software](https://en.wikipedia.org/wiki/Graphic_art_software)
- [Graphics](https://en.wikipedia.org/wiki/Graphics)
- [H tree](https://en.wikipedia.org/wiki/H_tree)
- [Hamid Naderi Yeganeh](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh)
- [Harold Cohen (artist)](https://en.wikipedia.org/wiki/Harold_Cohen_(artist))
- [Hausdorff dimension](https://en.wikipedia.org/wiki/Hausdorff_dimension)
- [Higuchi dimension](https://en.wikipedia.org/wiki/Higuchi_dimension)
- [Hilbert curve](https://en.wikipedia.org/wiki/Hilbert_curve)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Immersion (virtual reality)](https://en.wikipedia.org/wiki/Immersion_(virtual_reality))
- [Interactive art](https://en.wikipedia.org/wiki/Interactive_art)
- [Internet art](https://en.wikipedia.org/wiki/Internet_art)
- [Iterated function system](https://en.wikipedia.org/wiki/Iterated_function_system)
- [Jake Elwes](https://en.wikipedia.org/wiki/Jake_Elwes)
- [Jesus Dress Up](https://en.wikipedia.org/wiki/Jesus_Dress_Up)
- [Julia set](https://en.wikipedia.org/wiki/Julia_set)
- [Kaleidoscope](https://en.wikipedia.org/wiki/Kaleidoscope)
- [Karl Sims](https://en.wikipedia.org/wiki/Karl_Sims)
- [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)
- [L-system](https://en.wikipedia.org/wiki/L-system)
- [Lebesgue covering dimension](https://en.wikipedia.org/wiki/Lebesgue_covering_dimension)
- [Leptosporangiate fern](https://en.wikipedia.org/wiki/Leptosporangiate_fern)
- [Lewis Fry Richardson](https://en.wikipedia.org/wiki/Lewis_Fry_Richardson)
- [List of fractals by Hausdorff dimension](https://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension)
- [Listening Post (artwork)](https://en.wikipedia.org/wiki/Listening_Post_(artwork))
- [Los Angeles Center for Digital Art](https://en.wikipedia.org/wiki/Los_Angeles_Center_for_Digital_Art)
- [Lumen Prize](https://en.wikipedia.org/wiki/Lumen_Prize)
- [Lyapunov fractal](https://en.wikipedia.org/wiki/Lyapunov_fractal)
- [Lynn Hershman Leeson](https://en.wikipedia.org/wiki/Lynn_Hershman_Leeson)
- [Lévy C curve](https://en.wikipedia.org/wiki/L%C3%A9vy_C_curve)
- [Lévy flight](https://en.wikipedia.org/wiki/L%C3%A9vy_flight)
- [Mandelbox](https://en.wikipedia.org/wiki/Mandelbox)
- [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set)
- [Mandelbulb](https://en.wikipedia.org/wiki/Mandelbulb)
- [Margot Lovejoy](https://en.wikipedia.org/wiki/Margot_Lovejoy)
- [Mario Klingemann](https://en.wikipedia.org/wiki/Mario_Klingemann)
- [Mathematician](https://en.wikipedia.org/wiki/Mathematician)
- [Mauro Martino](https://en.wikipedia.org/wiki/Mauro_Martino)
- [Menger sponge](https://en.wikipedia.org/wiki/Menger_sponge)
- [Michael Barnsley](https://en.wikipedia.org/wiki/Michael_Barnsley)
- [Minkowski sausage](https://en.wikipedia.org/wiki/Minkowski_sausage)
- [Minkowski–Bouligand dimension](https://en.wikipedia.org/wiki/Minkowski%E2%80%93Bouligand_dimension)
- [Misiurewicz point](https://en.wikipedia.org/wiki/Misiurewicz_point)
- [Moore curve](https://en.wikipedia.org/wiki/Moore_curve)
- [Motion graphics](https://en.wikipedia.org/wiki/Motion_graphics)
- [Multibrot set](https://en.wikipedia.org/wiki/Multibrot_set)
- [Multifractal system](https://en.wikipedia.org/wiki/Multifractal_system)
- [Music visualization](https://en.wikipedia.org/wiki/Music_visualization)
- [N-flake](https://en.wikipedia.org/wiki/N-flake)
- [Newton fractal](https://en.wikipedia.org/wiki/Newton_fractal)
- [Niels Fabian Helge von Koch](https://en.wikipedia.org/wiki/Niels_Fabian_Helge_von_Koch)
- [Non-fungible token](https://en.wikipedia.org/wiki/Non-fungible_token)
- [Non-photorealistic rendering](https://en.wikipedia.org/wiki/Non-photorealistic_rendering)
- [Onedotzero](https://en.wikipedia.org/wiki/Onedotzero)
- [Orbit trap](https://en.wikipedia.org/wiki/Orbit_trap)
- [Packing dimension](https://en.wikipedia.org/wiki/Packing_dimension)
- [Paul Lévy (mathematician)](https://en.wikipedia.org/wiki/Paul_L%C3%A9vy_(mathematician))
- [Peano curve](https://en.wikipedia.org/wiki/Peano_curve)
- [Percolation theory](https://en.wikipedia.org/wiki/Percolation_theory)
- [Photograph manipulation](https://en.wikipedia.org/wiki/Photograph_manipulation)
- [Pickover stalk](https://en.wikipedia.org/wiki/Pickover_stalk)
- [Pindar Van Arman](https://en.wikipedia.org/wiki/Pindar_Van_Arman)
- [Pixel art](https://en.wikipedia.org/wiki/Pixel_art)
- [Pythagoras tree (fractal)](https://en.wikipedia.org/wiki/Pythagoras_tree_(fractal))
- [Recursion](https://en.wikipedia.org/wiki/Recursion)
- [Refik Anadol](https://en.wikipedia.org/wiki/Refik_Anadol)
- [Remember To Rise](https://en.wikipedia.org/wiki/Remember_To_Rise)
- [Rendering (computer graphics)](https://en.wikipedia.org/wiki/Rendering_(computer_graphics))
- [SIGGRAPH](https://en.wikipedia.org/wiki/SIGGRAPH)
- [Self-avoiding walk](https://en.wikipedia.org/wiki/Self-avoiding_walk)
- [Self-similarity](https://en.wikipedia.org/wiki/Self-similarity)
- [Sierpiński triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle)
- [Sierpiński carpet](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_carpet)
- [Sierpiński curve](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_curve)
- [Sierpiński triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle)
- [Software art](https://en.wikipedia.org/wiki/Software_art)
- [Sougwen Chung](https://en.wikipedia.org/wiki/Sougwen_Chung)
- [Space-filling curve](https://en.wikipedia.org/wiki/Space-filling_curve)
- [Stephanie Dinkins](https://en.wikipedia.org/wiki/Stephanie_Dinkins)
- [Systems art](https://en.wikipedia.org/wiki/Systems_art)
- [T-square (fractal)](https://en.wikipedia.org/wiki/T-square_(fractal))
- [Texture mapping](https://en.wikipedia.org/wiki/Texture_mapping)
- [The Beauty of Fractals](https://en.wikipedia.org/wiki/The_Beauty_of_Fractals)
- [The Fractal Geometry of Nature](https://en.wikipedia.org/wiki/The_Fractal_Geometry_of_Nature)
- [Thelypteridaceae](https://en.wikipedia.org/wiki/Thelypteridaceae)
- [Trevor Paglen](https://en.wikipedia.org/wiki/Trevor_Paglen)
- [Tricorn (mathematics)](https://en.wikipedia.org/wiki/Tricorn_(mathematics))
- [V&A Digital Futures](https://en.wikipedia.org/wiki/V%26A_Digital_Futures)
- [Vicsek fractal](https://en.wikipedia.org/wiki/Vicsek_fractal)
- [Virtual art](https://en.wikipedia.org/wiki/Virtual_art)
- [Wacław Sierpiński](https://en.wikipedia.org/wiki/Wac%C5%82aw_Sierpi%C5%84ski)
- [Weierstrass function](https://en.wikipedia.org/wiki/Weierstrass_function)
- [Xerox art](https://en.wikipedia.org/wiki/Xerox_art)
- [Z-order curve](https://en.wikipedia.org/wiki/Z-order_curve)
- [Zachary Lieberman](https://en.wikipedia.org/wiki/Zachary_Lieberman)
- [Template:Digital art](https://en.wikipedia.org/wiki/Template:Digital_art)
- [Template:Fractals](https://en.wikipedia.org/wiki/Template:Fractals)
- [Template talk:Digital art](https://en.wikipedia.org/wiki/Template_talk:Digital_art)
- [Template talk:Fractals](https://en.wikipedia.org/wiki/Template_talk:Fractals)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:33:18.402045+00:00_