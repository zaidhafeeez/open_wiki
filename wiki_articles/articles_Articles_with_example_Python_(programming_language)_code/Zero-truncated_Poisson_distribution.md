# Zero-truncated Poisson distribution

## Article Metadata

- **Last Updated:** 2024-12-14T19:47:18.647058+00:00
- **Original Article:** [Zero-truncated Poisson distribution](https://en.wikipedia.org/wiki/Zero-truncated_Poisson_distribution)
- **Language:** en
- **Page ID:** 40180359

## Summary

In probability theory, the zero-truncated Poisson distribution (ZTP distribution) is a certain discrete probability distribution whose support is the set of positive integers.  This distribution is also known as the conditional Poisson distribution or the positive Poisson distribution. It is the conditional probability distribution of a Poisson-distributed random variable, given that the value of the random variable is not zero. Thus it is impossible for a ZTP random variable to be zero. Conside

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from August 2013
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Discrete distributions
- Category:Poisson distribution
- Category:Short description is different from Wikidata

## Table of Contents

- Parameter estimation
- Examples
- Generating zero-truncated Poisson-distributed random variables

## Content

In probability theory, the zero-truncated Poisson distribution (ZTP distribution) is a certain discrete probability distribution whose support is the set of positive integers.  This distribution is also known as the conditional Poisson distribution or the positive Poisson distribution. It is the conditional probability distribution of a Poisson-distributed random variable, given that the value of the random variable is not zero. Thus it is impossible for a ZTP random variable to be zero. Consider for example the random variable of the number of items in a shopper's basket at a supermarket checkout line.  Presumably a shopper does not stand in line with nothing to buy (i.e., the minimum purchase is 1 item), so this phenomenon may follow a ZTP distribution.
Since the ZTP is a truncated distribution with the truncation stipulated as k > 0, one can derive the probability mass function g(k;λ) from a standard Poisson distribution f(k;λ) as follows:

  
    
      
        g
        (
        k
        ;
        λ
        )
        =
        P
        (
        X
        =
        k
        ∣
        X
        >
        0
        )
        =
        
          
            
              f
              (
              k
              ;
              λ
              )
            
            
              1
              −
              f
              (
              0
              ;
              λ
              )
            
          
        
        =
        
          
            
              
                λ
                
                  k
                
              
              
                e
                
                  −
                  λ
                
              
            
            
              k
              !
              
                (
                
                  1
                  −
                  
                    e
                    
                      −
                      λ
                    
                  
                
                )
              
            
          
        
        =
        
          
            
              λ
              
                k
              
            
            
              (
              
                e
                
                  λ
                
              
              −
              1
              )
              k
              !
            
          
        
      
    
    {\displaystyle g(k;\lambda )=P(X=k\mid X>0)={\frac {f(k;\lambda )}{1-f(0;\lambda )}}={\frac {\lambda ^{k}e^{-\lambda }}{k!\left(1-e^{-\lambda }\right)}}={\frac {\lambda ^{k}}{(e^{\lambda }-1)k!}}}
  

The mean is

  
    
      
        E
        ⁡
        [
        X
        ]
        =
        
          
            λ
            
              1
              −
              
                e
                
                  −
                  λ
                
              
            
          
        
        =
        
          
            
              λ
              
                e
                
                  λ
                
              
            
            
              
                e
                
                  λ
                
              
              −
              1
            
          
        
      
    
    {\displaystyle \operatorname {E} [X]={\frac {\lambda }{1-e^{-\lambda }}}={\frac {\lambda e^{\lambda }}{e^{\lambda }-1}}}
  

and the variance is

  
    
      
        Var
        ⁡
        [
        X
        ]
        =
        
          
            
              λ
              +
              
                λ
                
                  2
                
              
            
            
              1
              −
              
                e
                
                  −
                  λ
                
              
            
          
        
        −
        
          
            
              λ
              
                2
              
            
            
              (
              1
              −
              
                e
                
                  −
                  λ
                
              
              
                )
                
                  2
                
              
            
          
        
        =
        E
        ⁡
        [
        X
        ]
        (
        1
        +
        λ
        −
        E
        ⁡
        [
        X
        ]
        )
      
    
    {\displaystyle \operatorname {Var} [X]={\frac {\lambda +\lambda ^{2}}{1-e^{-\lambda }}}-{\frac {\lambda ^{2}}{(1-e^{-\lambda })^{2}}}=\operatorname {E} [X](1+\lambda -\operatorname {E} [X])}

Parameter estimation
The method of moments estimator 
  
    
      
        
          
            
              λ
              ^
            
          
        
      
    
    {\displaystyle {\widehat {\lambda }}}
  
 for the parameter 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
 is obtained by solving

  
    
      
        
          
            
              
                λ
                ^
              
            
            
              1
              −
              
                e
                
                  −
                  
                    
                      
                        λ
                        ^
                      
                    
                  
                
              
            
          
        
        =
        
          
            
              x
              ¯
            
          
        
      
    
    {\displaystyle {\frac {\widehat {\lambda }}{1-e^{-{\widehat {\lambda }}}}}={\bar {x}}}
  

where 
  
    
      
        
          
            
              x
              ¯
            
          
        
      
    
    {\displaystyle {\bar {x}}}
  
 is the sample mean.
This equation has a solution in terms of the Lambert W function. In practice, a solution may be found using numerical methods.

Examples
Insurance claims:
Imagine navigating the intricate landscape of auto insurance claims, where each claim signifies a unique event – an accident or damage occurrence. The ZTP distribution seamlessly aligns with this scenario, excluding the possibility of policyholders with zero claims.
Let X denote the random variable representing the number of insurance claims. If λ is the average rate of claims, the ZTP probability mass function takes the form:

  
    
      
        P
        (
        X
        =
        k
        )
        =
        
          
            
              
                λ
                
                  k
                
              
              
                e
                
                  −
                  λ
                
              
            
            
              k
              !
              
                (
                
                  1
                  −
                  
                    e
                    
                      −
                      λ
                    
                  
                
                )
              
            
          
        
      
    
    {\displaystyle P(X=k)={\frac {\lambda ^{k}e^{-\lambda }}{k!\left(1-e^{-\lambda }\right)}}}
  
 for k= 1,2,3,...
This formula encapsulates the probability of observing k claims given that at least one claim has transpired. The denominator ensures the exclusion of the improbable zero-claim scenario. By utilizing the zero-truncated Poisson distribution, the manufacturing company can analyze and predict the frequency of defects in their products while focusing on instances where defects exist. This distribution helps in understanding and improving the quality control process, especially when it's crucial to account for at least one defect.

Generating zero-truncated Poisson-distributed random variables
Random variables sampled from the zero-truncated Poisson distribution may be achieved using algorithms derived from Poisson distribution sampling algorithms.

init:
    Let k ← 1, t ← e−λ / (1 - e−λ) * λ, s ← t.
    Generate uniform random number u in [0,1].
while s < u do:
    k ← k + 1.
    t ← t * λ / k.
    s ← s + t.
return k.

The cost of the procedure above is linear in k, which may be large for large values of 
  
    
      
        λ
      
    
    {\displaystyle \lambda }
  
. Given access to an efficient sampler for non-truncated Poisson random variates, a non-iterative approach involves sampling from a truncated exponential distribution representing the time of the first event in a Poisson point process, conditional on such an event existing.
A simple NumPy implementation is:


== References ==

## Related Articles

### Internal Links

- [(a,b,0) class of distributions](https://en.wikipedia.org/wiki/(a,b,0)_class_of_distributions)
- [ARGUS distribution](https://en.wikipedia.org/wiki/ARGUS_distribution)
- [Arcsine distribution](https://en.wikipedia.org/wiki/Arcsine_distribution)
- [Asymmetric Laplace distribution](https://en.wikipedia.org/wiki/Asymmetric_Laplace_distribution)
- [Balding–Nichols model](https://en.wikipedia.org/wiki/Balding%E2%80%93Nichols_model)
- [Bates distribution](https://en.wikipedia.org/wiki/Bates_distribution)
- [Benford's law](https://en.wikipedia.org/wiki/Benford%27s_law)
- [Benini distribution](https://en.wikipedia.org/wiki/Benini_distribution)
- [Benktander type II distribution](https://en.wikipedia.org/wiki/Benktander_type_II_distribution)
- [Benktander type I distribution](https://en.wikipedia.org/wiki/Benktander_type_I_distribution)
- [Bernoulli distribution](https://en.wikipedia.org/wiki/Bernoulli_distribution)
- [Beta-binomial distribution](https://en.wikipedia.org/wiki/Beta-binomial_distribution)
- [Beta distribution](https://en.wikipedia.org/wiki/Beta_distribution)
- [Beta negative binomial distribution](https://en.wikipedia.org/wiki/Beta_negative_binomial_distribution)
- [Beta prime distribution](https://en.wikipedia.org/wiki/Beta_prime_distribution)
- [Beta rectangular distribution](https://en.wikipedia.org/wiki/Beta_rectangular_distribution)
- [Bingham distribution](https://en.wikipedia.org/wiki/Bingham_distribution)
- [Binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution)
- [Bivariate von Mises distribution](https://en.wikipedia.org/wiki/Bivariate_von_Mises_distribution)
- [Borel distribution](https://en.wikipedia.org/wiki/Borel_distribution)
- [Burr distribution](https://en.wikipedia.org/wiki/Burr_distribution)
- [Cantor distribution](https://en.wikipedia.org/wiki/Cantor_distribution)
- [Categorical distribution](https://en.wikipedia.org/wiki/Categorical_distribution)
- [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy_distribution)
- [Chi-squared distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution)
- [Chi distribution](https://en.wikipedia.org/wiki/Chi_distribution)
- [Circular distribution](https://en.wikipedia.org/wiki/Circular_distribution)
- [Circular uniform distribution](https://en.wikipedia.org/wiki/Circular_uniform_distribution)
- [Complex Wishart distribution](https://en.wikipedia.org/wiki/Complex_Wishart_distribution)
- [Compound Poisson distribution](https://en.wikipedia.org/wiki/Compound_Poisson_distribution)
- [Continuous Bernoulli distribution](https://en.wikipedia.org/wiki/Continuous_Bernoulli_distribution)
- [Continuous uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution)
- [Conway–Maxwell–Poisson distribution](https://en.wikipedia.org/wiki/Conway%E2%80%93Maxwell%E2%80%93Poisson_distribution)
- [Dagum distribution](https://en.wikipedia.org/wiki/Dagum_distribution)
- [Davis distribution](https://en.wikipedia.org/wiki/Davis_distribution)
- [Degenerate distribution](https://en.wikipedia.org/wiki/Degenerate_distribution)
- [Delaporte distribution](https://en.wikipedia.org/wiki/Delaporte_distribution)
- [Dirac delta function](https://en.wikipedia.org/wiki/Dirac_delta_function)
- [Directional statistics](https://en.wikipedia.org/wiki/Directional_statistics)
- [Dirichlet-multinomial distribution](https://en.wikipedia.org/wiki/Dirichlet-multinomial_distribution)
- [Dirichlet distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution)
- [Discrete Weibull distribution](https://en.wikipedia.org/wiki/Discrete_Weibull_distribution)
- [Discrete phase-type distribution](https://en.wikipedia.org/wiki/Discrete_phase-type_distribution)
- [Probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Discrete uniform distribution](https://en.wikipedia.org/wiki/Discrete_uniform_distribution)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Elliptical distribution](https://en.wikipedia.org/wiki/Elliptical_distribution)
- [Erlang distribution](https://en.wikipedia.org/wiki/Erlang_distribution)
- [Ewens's sampling formula](https://en.wikipedia.org/wiki/Ewens%27s_sampling_formula)
- [Expected value](https://en.wikipedia.org/wiki/Expected_value)
- [Exponential-logarithmic distribution](https://en.wikipedia.org/wiki/Exponential-logarithmic_distribution)
- [Exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution)
- [Exponential family](https://en.wikipedia.org/wiki/Exponential_family)
- [Extended negative binomial distribution](https://en.wikipedia.org/wiki/Extended_negative_binomial_distribution)
- [F-distribution](https://en.wikipedia.org/wiki/F-distribution)
- [Fisher's z-distribution](https://en.wikipedia.org/wiki/Fisher%27s_z-distribution)
- [Flory–Schulz distribution](https://en.wikipedia.org/wiki/Flory%E2%80%93Schulz_distribution)
- [Folded normal distribution](https://en.wikipedia.org/wiki/Folded_normal_distribution)
- [Fréchet distribution](https://en.wikipedia.org/wiki/Fr%C3%A9chet_distribution)
- [Gamma/Gompertz distribution](https://en.wikipedia.org/wiki/Gamma/Gompertz_distribution)
- [Gamma distribution](https://en.wikipedia.org/wiki/Gamma_distribution)
- [Gaussian q-distribution](https://en.wikipedia.org/wiki/Gaussian_q-distribution)
- [Gauss–Kuzmin distribution](https://en.wikipedia.org/wiki/Gauss%E2%80%93Kuzmin_distribution)
- [Generalised hyperbolic distribution](https://en.wikipedia.org/wiki/Generalised_hyperbolic_distribution)
- [Generalized Dirichlet distribution](https://en.wikipedia.org/wiki/Generalized_Dirichlet_distribution)
- [Generalized Pareto distribution](https://en.wikipedia.org/wiki/Generalized_Pareto_distribution)
- [Generalized beta distribution](https://en.wikipedia.org/wiki/Generalized_beta_distribution)
- [Generalized chi-squared distribution](https://en.wikipedia.org/wiki/Generalized_chi-squared_distribution)
- [Generalized extreme value distribution](https://en.wikipedia.org/wiki/Generalized_extreme_value_distribution)
- [Generalized gamma distribution](https://en.wikipedia.org/wiki/Generalized_gamma_distribution)
- [Generalized inverse Gaussian distribution](https://en.wikipedia.org/wiki/Generalized_inverse_Gaussian_distribution)
- [Generalized normal distribution](https://en.wikipedia.org/wiki/Generalized_normal_distribution)
- [Geometric distribution](https://en.wikipedia.org/wiki/Geometric_distribution)
- [Geometric stable distribution](https://en.wikipedia.org/wiki/Geometric_stable_distribution)
- [Gompertz distribution](https://en.wikipedia.org/wiki/Gompertz_distribution)
- [Gumbel distribution](https://en.wikipedia.org/wiki/Gumbel_distribution)
- [Half-logistic distribution](https://en.wikipedia.org/wiki/Half-logistic_distribution)
- [Half-normal distribution](https://en.wikipedia.org/wiki/Half-normal_distribution)
- [Holtsmark distribution](https://en.wikipedia.org/wiki/Holtsmark_distribution)
- [Hotelling's T-squared distribution](https://en.wikipedia.org/wiki/Hotelling%27s_T-squared_distribution)
- [Hyper-Erlang distribution](https://en.wikipedia.org/wiki/Hyper-Erlang_distribution)
- [Hyperbolic secant distribution](https://en.wikipedia.org/wiki/Hyperbolic_secant_distribution)
- [Hyperexponential distribution](https://en.wikipedia.org/wiki/Hyperexponential_distribution)
- [Hypergeometric distribution](https://en.wikipedia.org/wiki/Hypergeometric_distribution)
- [Hypoexponential distribution](https://en.wikipedia.org/wiki/Hypoexponential_distribution)
- [Inverse-Wishart distribution](https://en.wikipedia.org/wiki/Inverse-Wishart_distribution)
- [Inverse-chi-squared distribution](https://en.wikipedia.org/wiki/Inverse-chi-squared_distribution)
- [Inverse-gamma distribution](https://en.wikipedia.org/wiki/Inverse-gamma_distribution)
- [Inverse Gaussian distribution](https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution)
- [Inverse matrix gamma distribution](https://en.wikipedia.org/wiki/Inverse_matrix_gamma_distribution)
- [Irwin–Hall distribution](https://en.wikipedia.org/wiki/Irwin%E2%80%93Hall_distribution)
- [JSTOR](https://en.wikipedia.org/wiki/JSTOR)
- [Johnson's SU-distribution](https://en.wikipedia.org/wiki/Johnson%27s_SU-distribution)
- [Joint probability distribution](https://en.wikipedia.org/wiki/Joint_probability_distribution)
- [Kaniadakis Erlang distribution](https://en.wikipedia.org/wiki/Kaniadakis_Erlang_distribution)
- [Kaniadakis exponential distribution](https://en.wikipedia.org/wiki/Kaniadakis_exponential_distribution)
- [Kaniadakis Gamma distribution](https://en.wikipedia.org/wiki/Kaniadakis_Gamma_distribution)
- [Kaniadakis Gaussian distribution](https://en.wikipedia.org/wiki/Kaniadakis_Gaussian_distribution)
- [Kaniadakis logistic distribution](https://en.wikipedia.org/wiki/Kaniadakis_logistic_distribution)
- [Kaniadakis Weibull distribution](https://en.wikipedia.org/wiki/Kaniadakis_Weibull_distribution)
- [Kent distribution](https://en.wikipedia.org/wiki/Kent_distribution)
- [Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)
- [Kumaraswamy distribution](https://en.wikipedia.org/wiki/Kumaraswamy_distribution)
- [Lambert W function](https://en.wikipedia.org/wiki/Lambert_W_function)
- [Landau distribution](https://en.wikipedia.org/wiki/Landau_distribution)
- [Laplace distribution](https://en.wikipedia.org/wiki/Laplace_distribution)
- [Lewandowski-Kurowicka-Joe distribution](https://en.wikipedia.org/wiki/Lewandowski-Kurowicka-Joe_distribution)
- [List of probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)
- [Location–scale family](https://en.wikipedia.org/wiki/Location%E2%80%93scale_family)
- [Log-Cauchy distribution](https://en.wikipedia.org/wiki/Log-Cauchy_distribution)
- [Log-Laplace distribution](https://en.wikipedia.org/wiki/Log-Laplace_distribution)
- [Log-logistic distribution](https://en.wikipedia.org/wiki/Log-logistic_distribution)
- [Log-normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution)
- [Log-t distribution](https://en.wikipedia.org/wiki/Log-t_distribution)
- [Logarithmic distribution](https://en.wikipedia.org/wiki/Logarithmic_distribution)
- [Logistic distribution](https://en.wikipedia.org/wiki/Logistic_distribution)
- [Logit-normal distribution](https://en.wikipedia.org/wiki/Logit-normal_distribution)
- [Lomax distribution](https://en.wikipedia.org/wiki/Lomax_distribution)
- [Lévy distribution](https://en.wikipedia.org/wiki/L%C3%A9vy_distribution)
- [Marchenko–Pastur distribution](https://en.wikipedia.org/wiki/Marchenko%E2%80%93Pastur_distribution)
- [Matrix-exponential distribution](https://en.wikipedia.org/wiki/Matrix-exponential_distribution)
- [Matrix gamma distribution](https://en.wikipedia.org/wiki/Matrix_gamma_distribution)
- [Matrix normal distribution](https://en.wikipedia.org/wiki/Matrix_normal_distribution)
- [Matrix t-distribution](https://en.wikipedia.org/wiki/Matrix_t-distribution)
- [Maximum entropy probability distribution](https://en.wikipedia.org/wiki/Maximum_entropy_probability_distribution)
- [Maxwell–Boltzmann distribution](https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution)
- [Maxwell–Jüttner distribution](https://en.wikipedia.org/wiki/Maxwell%E2%80%93J%C3%BCttner_distribution)
- [Method of moments (statistics)](https://en.wikipedia.org/wiki/Method_of_moments_(statistics))
- [Mittag-Leffler distribution](https://en.wikipedia.org/wiki/Mittag-Leffler_distribution)
- [Mixed Poisson distribution](https://en.wikipedia.org/wiki/Mixed_Poisson_distribution)
- [Mixture distribution](https://en.wikipedia.org/wiki/Mixture_distribution)
- [Multinomial distribution](https://en.wikipedia.org/wiki/Multinomial_distribution)
- [Multivariate Laplace distribution](https://en.wikipedia.org/wiki/Multivariate_Laplace_distribution)
- [Multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)
- [Multivariate stable distribution](https://en.wikipedia.org/wiki/Multivariate_stable_distribution)
- [Multivariate t-distribution](https://en.wikipedia.org/wiki/Multivariate_t-distribution)
- [Nakagami distribution](https://en.wikipedia.org/wiki/Nakagami_distribution)
- [Natural exponential family](https://en.wikipedia.org/wiki/Natural_exponential_family)
- [Negative binomial distribution](https://en.wikipedia.org/wiki/Negative_binomial_distribution)
- [Negative hypergeometric distribution](https://en.wikipedia.org/wiki/Negative_hypergeometric_distribution)
- [Negative multinomial distribution](https://en.wikipedia.org/wiki/Negative_multinomial_distribution)
- [Noncentral F-distribution](https://en.wikipedia.org/wiki/Noncentral_F-distribution)
- [Noncentral beta distribution](https://en.wikipedia.org/wiki/Noncentral_beta_distribution)
- [Noncentral chi-squared distribution](https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution)
- [Noncentral t-distribution](https://en.wikipedia.org/wiki/Noncentral_t-distribution)
- [Normal-Wishart distribution](https://en.wikipedia.org/wiki/Normal-Wishart_distribution)
- [Normal-gamma distribution](https://en.wikipedia.org/wiki/Normal-gamma_distribution)
- [Normal-inverse-Wishart distribution](https://en.wikipedia.org/wiki/Normal-inverse-Wishart_distribution)
- [Normal-inverse-gamma distribution](https://en.wikipedia.org/wiki/Normal-inverse-gamma_distribution)
- [Normal-inverse Gaussian distribution](https://en.wikipedia.org/wiki/Normal-inverse_Gaussian_distribution)
- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
- [NumPy](https://en.wikipedia.org/wiki/NumPy)
- [PERT distribution](https://en.wikipedia.org/wiki/PERT_distribution)
- [Parabolic fractal distribution](https://en.wikipedia.org/wiki/Parabolic_fractal_distribution)
- [Pareto distribution](https://en.wikipedia.org/wiki/Pareto_distribution)
- [Pearson distribution](https://en.wikipedia.org/wiki/Pearson_distribution)
- [Phase-type distribution](https://en.wikipedia.org/wiki/Phase-type_distribution)
- [Poisson binomial distribution](https://en.wikipedia.org/wiki/Poisson_binomial_distribution)
- [Poisson distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
- [Poisson point process](https://en.wikipedia.org/wiki/Poisson_point_process)
- [Poly-Weibull distribution](https://en.wikipedia.org/wiki/Poly-Weibull_distribution)
- [Probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Probability mass function](https://en.wikipedia.org/wiki/Probability_mass_function)
- [Probability theory](https://en.wikipedia.org/wiki/Probability_theory)
- [Q-Gaussian distribution](https://en.wikipedia.org/wiki/Q-Gaussian_distribution)
- [Q-Weibull distribution](https://en.wikipedia.org/wiki/Q-Weibull_distribution)
- [Q-exponential distribution](https://en.wikipedia.org/wiki/Q-exponential_distribution)
- [Rademacher distribution](https://en.wikipedia.org/wiki/Rademacher_distribution)
- [Raised cosine distribution](https://en.wikipedia.org/wiki/Raised_cosine_distribution)
- [Random matrix](https://en.wikipedia.org/wiki/Random_matrix)
- [Random variable](https://en.wikipedia.org/wiki/Random_variable)
- [Rayleigh distribution](https://en.wikipedia.org/wiki/Rayleigh_distribution)
- [Reciprocal distribution](https://en.wikipedia.org/wiki/Reciprocal_distribution)
- [Rectified Gaussian distribution](https://en.wikipedia.org/wiki/Rectified_Gaussian_distribution)
- [Relativistic Breit–Wigner distribution](https://en.wikipedia.org/wiki/Relativistic_Breit%E2%80%93Wigner_distribution)
- [Rice distribution](https://en.wikipedia.org/wiki/Rice_distribution)
- [Sample mean and covariance](https://en.wikipedia.org/wiki/Sample_mean_and_covariance)
- [Scaled inverse chi-squared distribution](https://en.wikipedia.org/wiki/Scaled_inverse_chi-squared_distribution)
- [Shifted Gompertz distribution](https://en.wikipedia.org/wiki/Shifted_Gompertz_distribution)
- [Shifted log-logistic distribution](https://en.wikipedia.org/wiki/Shifted_log-logistic_distribution)
- [Singular distribution](https://en.wikipedia.org/wiki/Singular_distribution)
- [Skellam distribution](https://en.wikipedia.org/wiki/Skellam_distribution)
- [Skew normal distribution](https://en.wikipedia.org/wiki/Skew_normal_distribution)
- [Slash distribution](https://en.wikipedia.org/wiki/Slash_distribution)
- [Soliton distribution](https://en.wikipedia.org/wiki/Soliton_distribution)
- [Stable distribution](https://en.wikipedia.org/wiki/Stable_distribution)
- [Student's t-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution)
- [Tracy–Widom distribution](https://en.wikipedia.org/wiki/Tracy%E2%80%93Widom_distribution)
- [Triangular distribution](https://en.wikipedia.org/wiki/Triangular_distribution)
- [Truncated distribution](https://en.wikipedia.org/wiki/Truncated_distribution)
- [Truncated normal distribution](https://en.wikipedia.org/wiki/Truncated_normal_distribution)
- [Tukey lambda distribution](https://en.wikipedia.org/wiki/Tukey_lambda_distribution)
- [Tweedie distribution](https://en.wikipedia.org/wiki/Tweedie_distribution)
- [Type-2 Gumbel distribution](https://en.wikipedia.org/wiki/Type-2_Gumbel_distribution)
- [U-quadratic distribution](https://en.wikipedia.org/wiki/U-quadratic_distribution)
- [University of California, Los Angeles](https://en.wikipedia.org/wiki/University_of_California,_Los_Angeles)
- [Variance](https://en.wikipedia.org/wiki/Variance)
- [Variance-gamma distribution](https://en.wikipedia.org/wiki/Variance-gamma_distribution)
- [Voigt profile](https://en.wikipedia.org/wiki/Voigt_profile)
- [Von Mises distribution](https://en.wikipedia.org/wiki/Von_Mises_distribution)
- [Von Mises–Fisher distribution](https://en.wikipedia.org/wiki/Von_Mises%E2%80%93Fisher_distribution)
- [Weibull distribution](https://en.wikipedia.org/wiki/Weibull_distribution)
- [Wigner semicircle distribution](https://en.wikipedia.org/wiki/Wigner_semicircle_distribution)
- [Wilks's lambda distribution](https://en.wikipedia.org/wiki/Wilks%27s_lambda_distribution)
- [Wishart distribution](https://en.wikipedia.org/wiki/Wishart_distribution)
- [Wrapped Cauchy distribution](https://en.wikipedia.org/wiki/Wrapped_Cauchy_distribution)
- [Wrapped Lévy distribution](https://en.wikipedia.org/wiki/Wrapped_L%C3%A9vy_distribution)
- [Wrapped asymmetric Laplace distribution](https://en.wikipedia.org/wiki/Wrapped_asymmetric_Laplace_distribution)
- [Wrapped distribution](https://en.wikipedia.org/wiki/Wrapped_distribution)
- [Wrapped exponential distribution](https://en.wikipedia.org/wiki/Wrapped_exponential_distribution)
- [Wrapped normal distribution](https://en.wikipedia.org/wiki/Wrapped_normal_distribution)
- [Yule–Simon distribution](https://en.wikipedia.org/wiki/Yule%E2%80%93Simon_distribution)
- [Zeta distribution](https://en.wikipedia.org/wiki/Zeta_distribution)
- [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law)
- [Zipf–Mandelbrot law](https://en.wikipedia.org/wiki/Zipf%E2%80%93Mandelbrot_law)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Probability distributions](https://en.wikipedia.org/wiki/Template:Probability_distributions)
- [Template talk:Probability distributions](https://en.wikipedia.org/wiki/Template_talk:Probability_distributions)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from August 2013](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_August_2013)
- [Category:Probability distributions](https://en.wikipedia.org/wiki/Category:Probability_distributions)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:47:18.647058+00:00_