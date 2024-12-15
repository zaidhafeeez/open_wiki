# Gabor filter

## Metadata
- **Last Updated:** 2024-12-15 12:05:20 UTC
- **Original Article:** [Gabor filter](https://en.wikipedia.org/wiki/Gabor_filter)
- **Language:** en
- **Page ID:** 1579200

## Summary
In image processing, a Gabor filter, named after Dennis Gabor, who first proposed it as a 1D filter. 
The Gabor filter was first generalized to 2D by Gösta Granlund, by adding a reference direction.
The Gabor filter is a linear filter used for texture analysis, which essentially means that it analyzes whether there is any specific frequency content in the image in specific directions in a localized region around the point or region of analysis. Frequency and orientation representations of Gabor filters are claimed by many contemporary vision scientists to be similar to those of the human visual system. They have been found to be particularly appropriate for texture representation and discrimination. In the spatial domain, a 2D Gabor filter is a Gaussian kernel function modulated by a sinusoidal plane wave (see Gabor transform).
Some authors claim that simple cells in the visual cortex of mammalian brains can be modeled by Gabor functions. Thus, image analysis with Gabor filters is thought by some to be similar to perception in the human visual system.

## Categories
This article belongs to the following categories:

- Category:Accuracy disputes from February 2013
- Category:All accuracy disputes
- Category:All articles that are too technical
- Category:Articles with example Haskell code
- Category:Articles with example MATLAB/Octave code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 maint: multiple names: authors list
- Category:Image processing
- Category:Linear filters
- Category:Pattern recognition
- Category:Short description is different from Wikidata
- Category:Webarchive template wayback links
- Category:Wikipedia articles that are too technical from February 2017

## Table of Contents

- Definition
- Wavelet space
- Time-causal analogue of the Gabor filter
- Extraction of features from images
- Applications of 2D Gabor filters in image processing
- Example implementations
- See also
- References
- External links
- Further reading

## Content

In image processing, a Gabor filter, named after Dennis Gabor, who first proposed it as a 1D filter. 
The Gabor filter was first generalized to 2D by Gösta Granlund, by adding a reference direction.
The Gabor filter is a linear filter used for texture analysis, which essentially means that it analyzes whether there is any specific frequency content in the image in specific directions in a localized region around the point or region of analysis. Frequency and orientation representations of Gabor filters are claimed by many contemporary vision scientists to be similar to those of the human visual system. They have been found to be particularly appropriate for texture representation and discrimination. In the spatial domain, a 2D Gabor filter is a Gaussian kernel function modulated by a sinusoidal plane wave (see Gabor transform).
Some authors claim that simple cells in the visual cortex of mammalian brains can be modeled by Gabor functions. Thus, image analysis with Gabor filters is thought by some to be similar to perception in the human visual system.

Definition
Its impulse response is defined by a sinusoidal wave (a plane wave for 2D Gabor filters) multiplied by a Gaussian function.
Because of the multiplication-convolution property (Convolution theorem), the Fourier transform of a Gabor filter's impulse response is the convolution of the Fourier transform of the harmonic function (sinusoidal function) and the Fourier transform of the Gaussian function.  The filter has a real and an imaginary component representing orthogonal directions.  The two components may be formed into a complex number or used individually.
Complex

  
    
      
        g
        (
        x
        ,
        y
        ;
        λ
        ,
        θ
        ,
        ψ
        ,
        σ
        ,
        γ
        )
        =
        exp
        ⁡
        
          (
          
            −
            
              
                
                  
                    x
                    
                      ′
                      
                        2
                      
                    
                  
                  +
                  
                    γ
                    
                      2
                    
                  
                  
                    y
                    
                      ′
                      
                        2
                      
                    
                  
                
                
                  2
                  
                    σ
                    
                      2
                    
                  
                
              
            
          
          )
        
        exp
        ⁡
        
          (
          
            i
            
              (
              
                2
                π
                
                  
                    
                      x
                      ′
                    
                    λ
                  
                
                +
                ψ
              
              )
            
          
          )
        
      
    
    {\displaystyle g(x,y;\lambda ,\theta ,\psi ,\sigma ,\gamma )=\exp \left(-{\frac {x'^{2}+\gamma ^{2}y'^{2}}{2\sigma ^{2}}}\right)\exp \left(i\left(2\pi {\frac {x'}{\lambda }}+\psi \right)\right)}
  

Real

  
    
      
        g
        (
        x
        ,
        y
        ;
        λ
        ,
        θ
        ,
        ψ
        ,
        σ
        ,
        γ
        )
        =
        exp
        ⁡
        
          (
          
            −
            
              
                
                  
                    x
                    
                      ′
                      
                        2
                      
                    
                  
                  +
                  
                    γ
                    
                      2
                    
                  
                  
                    y
                    
                      ′
                      
                        2
                      
                    
                  
                
                
                  2
                  
                    σ
                    
                      2
                    
                  
                
              
            
          
          )
        
        cos
        ⁡
        
          (
          
            2
            π
            
              
                
                  x
                  ′
                
                λ
              
            
            +
            ψ
          
          )
        
      
    
    {\displaystyle g(x,y;\lambda ,\theta ,\psi ,\sigma ,\gamma )=\exp \left(-{\frac {x'^{2}+\gamma ^{2}y'^{2}}{2\sigma ^{2}}}\right)\cos \left(2\pi {\frac {x'}{\lambda }}+\psi \right)}
  

Imaginary

  
    
      
        g
        (
        x
        ,
        y
        ;
        λ
        ,
        θ
        ,
        ψ
        ,
        σ
        ,
        γ
        )
        =
        exp
        ⁡
        
          (
          
            −
            
              
                
                  
                    x
                    
                      ′
                      
                        2
                      
                    
                  
                  +
                  
                    γ
                    
                      2
                    
                  
                  
                    y
                    
                      ′
                      
                        2
                      
                    
                  
                
                
                  2
                  
                    σ
                    
                      2
                    
                  
                
              
            
          
          )
        
        sin
        ⁡
        
          (
          
            2
            π
            
              
                
                  x
                  ′
                
                λ
              
            
            +
            ψ
          
          )
        
      
    
    {\displaystyle g(x,y;\lambda ,\theta ,\psi ,\sigma ,\gamma )=\exp \left(-{\frac {x'^{2}+\gamma ^{2}y'^{2}}{2\sigma ^{2}}}\right)\sin \left(2\pi {\frac {x'}{\lambda }}+\psi \right)}
  

where 
  
    
      
        
          x
          ′
        
        =
        x
        cos
        ⁡
        θ
        +
        y
        sin
        ⁡
        θ
      
    
    {\displaystyle x'=x\cos \theta +y\sin \theta }
  
 and 
  
    
      
        
          y
          ′
        
        =
        −
        x
        sin
        ⁡
        θ
        +
        y
        cos
        ⁡
        θ
      
    
    {\displaystyle y'=-x\sin \theta +y\cos \theta }
  
.
In this equation, 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
 represents the wavelength of the sinusoidal factor, 
  
    
      
        θ
      
    
    {\displaystyle \theta }
  
 represents the orientation of the normal to the parallel stripes of a Gabor function, 
  
    
      
        ψ
      
    
    {\displaystyle \psi }
  
 is the phase offset, 
  
    
      
        σ
      
    
    {\displaystyle \sigma }
  
 is the sigma/standard deviation of the Gaussian envelope and 
  
    
      
        γ
      
    
    {\displaystyle \gamma }
  
 is the spatial aspect ratio, and specifies the ellipticity of the support of the Gabor function.

Wavelet space
Gabor filters are directly related to Gabor wavelets, since they can be designed for a number of dilations and rotations. However, in general, expansion is not applied for Gabor wavelets, since this requires computation of bi-orthogonal wavelets, which may be very time-consuming. Therefore, usually, a filter bank consisting of Gabor filters with various scales and rotations is created. The filters are convolved with the signal, resulting in a so-called Gabor space. This process is closely related to processes in the primary visual cortex.
Jones and Palmer showed that the real part of the complex Gabor function is a good fit to the receptive field weight functions found in simple cells in a cat's striate cortex.

Time-causal analogue of the Gabor filter
When processing temporal signals, data from the future cannot be accessed, which leads to problems if attempting to use Gabor functions for processing real-time signals that depend on the temporal dimension. A time-causal analogue of the Gabor filter has been developed in  based on replacing the Gaussian kernel in the Gabor function with a time-causal and time-recursive kernel referred to as the time-causal limit kernel. In this way, time-frequency analysis based on the resulting complex-valued extension of the time-causal limit kernel makes it possible to capture essentially similar transformations of a temporal signal as the Gabor filter can, and as can  be described by the Heisenberg group, see  for further details.

Extraction of features from images
A set of Gabor filters with different frequencies and orientations may be helpful for extracting useful features from an image. In the discrete domain, two-dimensional Gabor filters are given by,

  
    
      
        
          G
          
            c
          
        
        [
        i
        ,
        j
        ]
        =
        B
        
          e
          
            −
            
              
                
                  (
                  
                    i
                    
                      2
                    
                  
                  +
                  
                    j
                    
                      2
                    
                  
                  )
                
                
                  2
                  
                    σ
                    
                      2
                    
                  
                
              
            
          
        
        cos
        ⁡
        (
        2
        π
        f
        (
        i
        cos
        ⁡
        θ
        +
        j
        sin
        ⁡
        θ
        )
        )
      
    
    {\displaystyle G_{c}[i,j]=Be^{-{\frac {(i^{2}+j^{2})}{2\sigma ^{2}}}}\cos(2\pi f(i\cos \theta +j\sin \theta ))}
  

  
    
      
        
          G
          
            s
          
        
        [
        i
        ,
        j
        ]
        =
        C
        
          e
          
            −
            
              
                
                  (
                  
                    i
                    
                      2
                    
                  
                  +
                  
                    j
                    
                      2
                    
                  
                  )
                
                
                  2
                  
                    σ
                    
                      2
                    
                  
                
              
            
          
        
        sin
        ⁡
        (
        2
        π
        f
        (
        i
        cos
        ⁡
        θ
        +
        j
        sin
        ⁡
        θ
        )
        )
      
    
    {\displaystyle G_{s}[i,j]=Ce^{-{\frac {(i^{2}+j^{2})}{2\sigma ^{2}}}}\sin(2\pi f(i\cos \theta +j\sin \theta ))}
  

where B and C are normalizing factors to be determined.
2D Gabor filters have rich applications in image processing, especially in feature extraction for texture analysis and segmentation. 
  
    
      
        f
      
    
    {\displaystyle f}
  
 defines the frequency being looked for in the texture. By varying 
  
    
      
        θ
      
    
    {\displaystyle \theta }
  
, we can look for texture oriented in a particular direction. By varying 
  
    
      
        σ
      
    
    {\displaystyle \sigma }
  
, we change the support of the basis or the size of the image region being analyzed.

Applications of 2D Gabor filters in image processing
In document image processing, Gabor features are ideal for identifying the script of a word in a multilingual document. Gabor filters with different frequencies and with orientations in different directions have been used to localize and extract text-only regions from complex document images (both gray and colour), since text is rich in high frequency components, whereas pictures are relatively smooth in nature. It has also been applied for facial expression recognition 
Gabor filters have also been widely used in pattern analysis applications. For example, it has been used to study the directionality distribution inside the porous spongy trabecular bone in the spine. The Gabor space is very useful in image processing applications such as optical character recognition, iris recognition and fingerprint recognition. Relations between activations for a specific spatial location are very distinctive between objects in an image. Furthermore, important activations can be extracted from the Gabor space in order to create a sparse object representation.

Example implementations
Python
This is an example implementation in Python:

For an implementation on images, see [1].

MATLAB
This is an example implementation in MATLAB/Octave:

Code for Gabor feature extraction from images in MATLAB can be found at http://www.mathworks.com/matlabcentral/fileexchange/44630.

Haskell
This is another example implementation in Haskell:

See also
Gabor transform
Gabor wavelet
Gabor atom
Log Gabor filter

References
External links
MATLAB code for Gabor filters and Gabor feature extraction
3D Gabor demonstrated with Mathematica
python implementation of log-Gabors for still images
Gabor filter for image processing and computer vision (demonstration) Archived 2018-05-29 at the Wayback Machine

Further reading
Feichtinger, Hans G.; Strohmer, Thomas, eds. (1998). Gabor analysis and algorithms : theory and applications. Boston: Birkhäuser. ISBN 0-8176-3959-4. LCCN 97032252. OCLC 37761814. OL 685385M.
Gröchenig, Karlheinz (2001). Foundations of time-frequency analysis : with 15 figures. Applied and Numerical Harmonic Analysis. Boston: Birkhäuser. doi:10.1007/978-1-4612-0003-1. ISBN 0-8176-4022-3. LCCN 00044508. OCLC 44420790. OL 8074618M.
Daugman, J.G. (1988). "Complete discrete 2-D Gabor transforms by neural networks for image analysis and compression" (PDF). IEEE Transactions on Acoustics, Speech, and Signal Processing. 36 (7): 1169–1179. CiteSeerX 10.1.1.371.5847. doi:10.1109/29.1644. ISSN 0096-3518.
"Online Gabor filter demo". Archived from the original on 2009-06-15. Retrieved 2009-05-25.
Movellan, Javier R. "Tutorial on Gabor Filters" (PDF). Archived from the original (PDF) on 2009-04-19. Retrieved 2008-05-14.
Lagae, Ares; Lefebvre, Sylvain; Drettakis, George; Dutré, Philip (2009). "Procedural Noise using Sparse Gabor Convolution". ACM Transactions on Graphics. 28 (3): 1. CiteSeerX 10.1.1.232.5566. doi:10.1145/1531326.1531360. Retrieved 2009-09-12.
Steerable Pyramids:
Eero Simoncelli's page on Steerable Pyramids
Manduchi, R.; Perona, P.; Shy, D. (April 1998). "Efficient deformable filter banks" (PDF). IEEE Transactions on Signal Processing. 46 (4): 1168–1173. Bibcode:1998ITSP...46.1168M. doi:10.1109/78.668570. ISSN 1053-587X. OCLC 926890247. (PDF Archived 2021-11-12 at the Wayback Machine) (Code Archived 2010-06-13 at the Wayback Machine)
Fischer, Sylvain; Šroubek, Filip; Perrinet, Laurent; Redondo, Rafael; Cristóbal, Gabriel (2007). "Self-Invertible 2D Log-Gabor Wavelets" (PDF). International Journal of Computer Vision. 75 (2): 231–246. CiteSeerX 10.1.1.329.6283. doi:10.1007/s11263-006-0026-8. ISSN 0920-5691. S2CID 1452724.

## Archive Info
- **Archived on:** 2024-12-15 21:04:32 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 16200 bytes
- **Word Count:** 1488 words
