# Sunrise equation

## Metadata
- **Last Updated:** 2024-12-11 19:17:46 UTC
- **Original Article:** [Sunrise equation](https://en.wikipedia.org/wiki/Sunrise_equation)
- **Language:** en
- **Page ID:** 4517642

## Summary
The sunrise equation or sunset equation can be used to derive the time of sunrise or sunset for any solar declination and latitude in terms of local solar time when sunrise and sunset actually occur.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:Articles needing additional references from June 2018
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Dynamics of the Solar System
- Category:Equations
- Category:Short description matches Wikidata
- Category:Time in astronomy

## Table of Contents

- Formulation
- Principles
- Expressions for the solar hour angle
- Generalized equation
- Complete calculation on Earth
- See also
- References
- External links

## Content

The sunrise equation or sunset equation can be used to derive the time of sunrise or sunset for any solar declination and latitude in terms of local solar time when sunrise and sunset actually occur.

Formulation
It is formulated as:

  
    
      
        cos
        ⁡
        
          ω
          
            ∘
          
        
        =
        −
        tan
        ⁡
        ϕ
        ×
        tan
        ⁡
        δ
      
    
    {\displaystyle \cos \omega _{\circ }=-\tan \phi \times \tan \delta }
  

where:

  
    
      
        
          ω
          
            ∘
          
        
      
    
    {\displaystyle \omega _{\circ }}
  
 is the solar hour angle at either sunrise (when negative value is taken) or sunset (when positive value is taken);

  
    
      
        ϕ
      
    
    {\displaystyle \phi }
  
 is the latitude of the observer on the Earth;

  
    
      
        δ
      
    
    {\displaystyle \delta }
  
 is the sun declination.

Principles
The Earth rotates at an angular velocity of 15°/hour. Therefore, the expression 
  
    
      
        
          ω
          
            ∘
          
        
        
          /
        
        
          
            15
          
          
            ∘
          
        
      
    
    {\displaystyle \omega _{\circ }/\mathrm {15} ^{\circ }}
  
, where 
  
    
      
        
          ω
          
            ∘
          
        
      
    
    {\displaystyle \omega _{\circ }}
  
 is in degree, gives the interval of time in hours from sunrise to local solar noon or from local solar noon to sunset.
The sign convention is typically that the observer latitude 
  
    
      
        ϕ
      
    
    {\displaystyle \phi }
  
 is 0 at the equator, positive for the Northern Hemisphere and negative for the Southern Hemisphere, and the solar declination 
  
    
      
        δ
      
    
    {\displaystyle \delta }
  
 is 0 at the vernal and autumnal equinoxes when the sun is exactly above the equator, positive during the Northern Hemisphere summer and negative during the Northern Hemisphere winter.
The expression above is always applicable for latitudes between the Arctic Circle and Antarctic Circle. North of the Arctic Circle or south of the Antarctic Circle, there is at least one day of the year with no sunrise or sunset. Formally, there is a sunrise or sunset when 
  
    
      
        −
        
          90
          
            ∘
          
        
        +
        δ
        <
        ϕ
        <
        
          90
          
            ∘
          
        
        −
        δ
      
    
    {\displaystyle -90^{\circ }+\delta <\phi <90^{\circ }-\delta }
  
 during the Northern Hemisphere summer, and when 
  
    
      
        −
        
          90
          
            ∘
          
        
        −
        δ
        <
        ϕ
        <
        
          90
          
            ∘
          
        
        +
        δ
      
    
    {\displaystyle -90^{\circ }-\delta <\phi <90^{\circ }+\delta }
  
 during the Northern Hemisphere winter. For locations outside these latitudes, it is either 24-hour daytime or 24-hour nighttime.

Expressions for the solar hour angle
In the equation given at the beginning, the cosine function on the left side gives results in the range [-1, 1], but the value of the expression on the right side is in the range 
  
    
      
        [
        −
        ∞
        ,
        ∞
        ]
      
    
    {\displaystyle [-\infty ,\infty ]}
  
. An applicable expression for 
  
    
      
        
          ω
          
            ∘
          
        
      
    
    {\displaystyle \omega _{\circ }}
  
 in the format of Fortran 90 is as follows:

omegao = acos(max(min(-tan(delta*rpd)*tan(phi*rpd), 1.0), -1.0))*dpr
where omegao is 
  
    
      
        
          ω
          
            ∘
          
        
      
    
    {\displaystyle \omega _{\circ }}
  
 in degree, delta is 
  
    
      
        δ
      
    
    {\displaystyle \delta }
  
 in degree, phi is 
  
    
      
        ϕ
      
    
    {\displaystyle \phi }
  
 in degree, rpd is equal to 
  
    
      
        
          
            π
            180
          
        
      
    
    {\displaystyle {\frac {\pi }{180}}}
  
, and dpr is equal to 
  
    
      
        
          
            180
            π
          
        
      
    
    {\displaystyle {\frac {180}{\pi }}}
  
.
The above expression gives results in degree in the range 
  
    
      
        [
        
          0
          
            ∘
          
        
        ,
        
          180
          
            ∘
          
        
        ]
      
    
    {\displaystyle [0^{\circ },180^{\circ }]}
  
. When 
  
    
      
        
          ω
          
            ∘
          
        
        =
        
          0
          
            ∘
          
        
      
    
    {\displaystyle \omega _{\circ }=0^{\circ }}
  
, it means it is polar night, or 0-hour daylight; when 
  
    
      
        
          ω
          
            ∘
          
        
        =
        
          180
          
            ∘
          
        
      
    
    {\displaystyle \omega _{\circ }=180^{\circ }}
  
, it means it is polar day, or 24-hour daylight.

Hemispheric relation
Suppose 
  
    
      
        
          ϕ
          
            N
          
        
      
    
    {\displaystyle \phi _{N}}
  
 is a given latitude in Northern Hemisphere, and 
  
    
      
        
          ω
          
            ∘
            N
          
        
      
    
    {\displaystyle \omega _{\circ N}}
  
 is the corresponding sunrise hour angle that has a negative value, and similarly, 
  
    
      
        
          ϕ
          
            S
          
        
      
    
    {\displaystyle \phi _{S}}
  
 is the same latitude but in Southern Hemisphere, which means 
  
    
      
        
          ϕ
          
            S
          
        
        =
        −
        
          ϕ
          
            N
          
        
      
    
    {\displaystyle \phi _{S}=-\phi _{N}}
  
, and 
  
    
      
        
          ω
          
            ∘
            S
          
        
      
    
    {\displaystyle \omega _{\circ S}}
  
 is the corresponding sunrise hour angle, then it is apparent that

  
    
      
        cos
        ⁡
        
          ω
          
            ∘
            S
          
        
        =
        −
        cos
        ⁡
        
          ω
          
            ∘
            N
          
        
        =
        cos
        ⁡
        (
        −
        
          180
          
            ∘
          
        
        −
        
          ω
          
            ∘
            N
          
        
        )
      
    
    {\displaystyle \cos \omega _{\circ S}=-\cos \omega _{\circ N}=\cos(-180^{\circ }-\omega _{\circ N})}
  
,
which means 

  
    
      
        
          ω
          
            ∘
            N
          
        
        +
        
          ω
          
            ∘
            S
          
        
        =
        −
        
          180
          
            ∘
          
        
      
    
    {\displaystyle \omega _{\circ N}+\omega _{\circ S}=-180^{\circ }}
  
.
The above relation implies that on the same day, the lengths of daytime from sunrise to sunset at 
  
    
      
        
          ϕ
          
            N
          
        
      
    
    {\displaystyle \phi _{N}}
  
 and 
  
    
      
        
          ϕ
          
            S
          
        
      
    
    {\displaystyle \phi _{S}}
  
 sum to 24 hours if 
  
    
      
        
          ϕ
          
            S
          
        
        =
        −
        
          ϕ
          
            N
          
        
      
    
    {\displaystyle \phi _{S}=-\phi _{N}}
  
, and this also applies to regions where polar days and polar nights occur. This further suggests that the global average of length of daytime on any given day is 12 hours without considering the effect of atmospheric refraction.

Generalized equation
The equation above neglects the influence of atmospheric refraction (which lifts the solar disc — i.e. makes the solar disc appear higher in the sky — by approximately 0.6° when it is on the horizon) and the non-zero angle subtended by the solar disc — i.e. the apparent diameter of the sun — (about 0.5°). The times of the rising and the setting of the upper solar limb as given in astronomical almanacs correct for this by using the more general equation

  
    
      
        cos
        ⁡
        
          ω
          
            ∘
          
        
        =
        
          
            
              
                sin
                ⁡
                a
                −
                sin
                ⁡
                ϕ
                ×
                sin
                ⁡
                δ
              
              
                cos
                ⁡
                ϕ
                ×
                cos
                ⁡
                δ
              
            
          
        
      
    
    {\displaystyle \cos \omega _{\circ }={\dfrac {\sin a-\sin \phi \times \sin \delta }{\cos \phi \times \cos \delta }}}
  

with the altitude angle (a) of the center of the solar disc set to about −0.83° (or −50 arcminutes).
The above general equation can be also used for any other solar altitude. The NOAA provides additional approximate expressions for refraction corrections at these other altitudes. There are also alternative formulations, such as a non-piecewise expression by G.G. Bennett used in the U.S. Naval Observatory's "Vector Astronomy Software".

Complete calculation on Earth
The generalized equation relies on a number of other variables which need to be calculated before it can itself be calculated. These equations have the solar-earth constants substituted with angular constants expressed in degrees.

Calculate current Julian day
n
        =
        ⌈
        
          J
          
            date
          
        
        −
        2451545.0
        +
        0.0008
        ⌉
      
    
    {\displaystyle n=\lceil J_{\text{date}}-2451545.0+0.0008\rceil }
  

where:

  
    
      
        n
      
    
    {\displaystyle n}
  
 is the number of days since Jan 1st, 2000 12:00.

  
    
      
        
          J
          
            date
          
        
      
    
    {\displaystyle J_{\text{date}}}
  
 is the Julian date;
2451545.0 is the equivalent Julian year of Julian days for Jan-01-2000, 12:00:00.
0.0008 is the fractional Julian Day for leap seconds and terrestrial time (TT).
TT was set to 32.184 sec lagging TAI on 1 January 1958. By 1972, when the leap second was introduced, 10 sec were added. By 1 January 2017, 27 more seconds were added coming to a total of 69.184 sec. 0.0008=69.184 / 86400 without DUT1.
The 
  
    
      
        ⌈
        ⋅
        ⌉
      
    
    {\displaystyle \lceil \cdot \rceil }
  
 operation rounds up to the next integer day number n.

Mean solar time
J
          
            ⋆
          
        
        =
        n
        −
        
          
            
              
                l
                
                  w
                
              
              
                360
                
                  ∘
                
              
            
          
        
      
    
    {\displaystyle J^{\star }=n-{\dfrac {l_{w}}{360^{\circ }}}}
  

where:

  
    
      
        
          J
          
            ⋆
          
        
      
    
    {\displaystyle J^{\star }}
  
 is an approximation of mean solar time at integer 
  
    
      
        n
      
    
    {\displaystyle n}
  
 expressed as a Julian day with the day fraction.

  
    
      
        
          l
          
            ω
          
        
      
    
    {\displaystyle l_{\omega }}
  
 is the longitude (west is negative, east is positive) of the observer on the Earth;

Solar mean anomaly
M
        =
        (
        357.5291
        +
        0.98560028
        ×
        
          J
          
            ⋆
          
        
        )
        
          mod
          
            3
          
        
        60
      
    
    {\displaystyle M=(357.5291+0.98560028\times J^{\star }){\bmod {3}}60}
  

where:

M is the solar mean anomaly used in the next three equations.

Equation of the center
C
        =
        1.9148
        sin
        ⁡
        (
        M
        )
        +
        0.0200
        sin
        ⁡
        (
        2
        M
        )
        +
        0.0003
        sin
        ⁡
        (
        3
        M
        )
      
    
    {\displaystyle C=1.9148\sin(M)+0.0200\sin(2M)+0.0003\sin(3M)}
  

where:

C is the Equation of the center value needed to calculate lambda (see next equation).
1.9148 is the coefficient of the Equation of the Center for the planet the observer is on (in this case, Earth)

Ecliptic longitude
λ
        =
        (
        M
        +
        C
        +
        180
        +
        102.9372
        )
        
          mod
          
            3
          
        
        60
      
    
    {\displaystyle \lambda =(M+C+180+102.9372){\bmod {3}}60}
  

where:

λ is the ecliptic longitude.
102.9372 is a value for the argument of perihelion.

Solar transit
J
          
            t
            r
            a
            n
            s
            i
            t
          
        
        =
        2451545.0
        +
        
          J
          
            ⋆
          
        
        +
        0.0053
        sin
        ⁡
        M
        −
        0.0069
        sin
        ⁡
        
          (
          
            2
            λ
          
          )
        
      
    
    {\displaystyle J_{transit}=2451545.0+J^{\star }+0.0053\sin M-0.0069\sin \left(2\lambda \right)}
  

where:

Jtransit is the Julian date for the local true solar transit (or solar noon).
2451545.0 is noon of the equivalent Julian year reference.

  
    
      
        0.0053
        sin
        ⁡
        M
        −
        0.0069
        sin
        ⁡
        
          (
          
            2
            λ
          
          )
        
      
    
    {\displaystyle 0.0053\sin M-0.0069\sin \left(2\lambda \right)}
  
 is a simplified version of the equation of time. The coefficients are fractional days.

Declination of the Sun
sin
        ⁡
        δ
        =
        sin
        ⁡
        λ
        ×
        sin
        ⁡
        
          23.4397
          
            ∘
          
        
      
    
    {\displaystyle \sin \delta =\sin \lambda \times \sin 23.4397^{\circ }}
  

where:

  
    
      
        δ
      
    
    {\displaystyle \delta }
  
 is the declination of the sun.
23.4397° is Earth's maximum axial tilt toward the sun 
Alternatively, the Sun's declination could be approximated  as:

  
    
      
        δ
        =
        23.45
        ∗
        sin
        ⁡
        (
        (
        360
        ×
        d
        
          /
        
        365.25
        
          )
          
            ∘
          
        
        
          )
          
            ∘
          
        
      
    
    {\displaystyle \delta =23.45*\sin((360\times d/365.25)^{\circ })^{\circ }}
  

where:

d is the number of days after the spring equinox (usually March 21st).

Hour angle
This is the equation from above with corrections for atmospherical refraction and solar disc diameter.

  
    
      
        cos
        ⁡
        
          ω
          
            ∘
          
        
        =
        
          
            
              
                sin
                ⁡
                (
                −
                
                  0.833
                  
                    ∘
                  
                
                )
                −
                sin
                ⁡
                ϕ
                ×
                sin
                ⁡
                δ
              
              
                cos
                ⁡
                ϕ
                ×
                cos
                ⁡
                δ
              
            
          
        
      
    
    {\displaystyle \cos \omega _{\circ }={\dfrac {\sin(-0.833^{\circ })-\sin \phi \times \sin \delta }{\cos \phi \times \cos \delta }}}
  

where:

ωo is the hour angle from the observer's meridian;

  
    
      
        ϕ
      
    
    {\displaystyle \phi }
  
 is the north latitude of the observer (north is positive, south is negative) on the Earth.
For observations on a sea horizon needing an elevation-of-observer correction, add 
  
    
      
        −
        
          1.15
          
            ∘
          
        
        
          
            elevation in feet
          
        
        
          /
        
        60
      
    
    {\displaystyle -1.15^{\circ }{\sqrt {\text{elevation in feet}}}/60}
  
, or 
  
    
      
        −
        
          2.076
          
            ∘
          
        
        
          
            elevation in metres
          
        
        
          /
        
        60
      
    
    {\displaystyle -2.076^{\circ }{\sqrt {\text{elevation in metres}}}/60}
  
 to the −0.833° in the numerator's sine term. This corrects for both apparent dip and terrestrial refraction. For example, for an observer at 10,000 feet, add (−115°/60) or about −1.92° to −0.833°.

Calculate sunrise and sunset
J
          
            rise
          
        
        =
        
          J
          
            transit
          
        
        −
        
          
            
              
                ω
                
                  ∘
                
              
              
                360
                
                  ∘
                
              
            
          
        
      
    
    {\displaystyle J_{\text{rise}}=J_{\text{transit}}-{\dfrac {\omega _{\circ }}{360^{\circ }}}}
  

  
    
      
        
          J
          
            set
          
        
        =
        
          J
          
            transit
          
        
        +
        
          
            
              
                ω
                
                  ∘
                
              
              
                360
                
                  ∘
                
              
            
          
        
      
    
    {\displaystyle J_{\text{set}}=J_{\text{transit}}+{\dfrac {\omega _{\circ }}{360^{\circ }}}}
  

where:

Jrise is the actual Julian date of sunrise;
Jset is the actual Julian date of sunset.

Example of implementation in Python
See also
Day length
Equation of time

References
External links
Sunrise, sunset, or sun position for any location – U.S. only
Sunrise, sunset and day length for any location – Worldwide
Rise/Set/Transit/Twilight Data – U.S. only
Astronomical Information Center
Converting Between Julian Dates and Gregorian Calendar Dates
Approximate Solar Coordinates
Algorithms for Computing Astronomical Phenomena
Astronomy Answers: Position of the Sun
A Simple Expression for the Equation of Time
The Equation of Time
Equation of Time
Long-Term Almanac for Sun, Moon, and Polaris V1.11
Evaluating the Effectiveness of Current Atmospheric Refraction Models in Predicting Sunrise and Sunset Times

## Archive Info
- **Archived on:** 2024-12-15 21:06:16 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 19918 bytes
- **Word Count:** 1812 words
