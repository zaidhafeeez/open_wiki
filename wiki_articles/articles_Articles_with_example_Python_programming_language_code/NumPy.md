# NumPy

## Article Metadata

- **Last Updated:** 2024-12-15T04:37:37.170538+00:00
- **Original Article:** [NumPy](https://en.wikipedia.org/wiki/NumPy)
- **Language:** en
- **Page ID:** 381782

## Summary

NumPy (pronounced  NUM-py) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. The predecessor of NumPy, Numeric, was originally created by Jim Hugunin with contributions from several other developers. In 2005, Travis Oliphant created NumPy by incorporating features of the competing Numarray into Numeric, with extensive modifications. NumPy

## Categories

- Category:All articles with unsourced statements
- Category:All articles with vague or ambiguous time
- Category:Array programming languages
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from December 2023
- Category:Free mathematics software
- Category:Free science software
- Category:Numerical analysis software for Linux
- Category:Numerical analysis software for Windows
- Category:Numerical analysis software for macOS
- Category:Numerical programming languages
- Category:Pages using Sister project links with hidden wikidata
- Category:Python (programming language) scientific libraries
- Category:Short description is different from Wikidata
- Category:Software using the BSD license
- Category:Vague or ambiguous time from October 2013
- Category:Wikipedia articles needing clarification from April 2020

## Table of Contents

- History
- Features
- Examples
- See also
- References
- Further reading
- External links

## Content

NumPy (pronounced  NUM-py) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. The predecessor of NumPy, Numeric, was originally created by Jim Hugunin with contributions from several other developers. In 2005, Travis Oliphant created NumPy by incorporating features of the competing Numarray into Numeric, with extensive modifications. NumPy is open-source software and has many contributors. NumPy is a NumFOCUS fiscally sponsored project.

History
matrix-sig
The Python programming language was not originally designed for numerical computing, but attracted the attention of the scientific and engineering community early on. In 1995 the special interest group (SIG) matrix-sig was founded with the aim of defining an array computing package; among its members was Python designer and maintainer Guido van Rossum, who extended Python's syntax (in particular the indexing syntax) to make array computing easier.

Numeric
An implementation of a matrix package was completed by Jim Fulton, then generalized by Jim Hugunin and called Numeric (also variously known as the "Numerical Python extensions" or "NumPy"), with influences from the APL family of languages, Basis, MATLAB, FORTRAN, S and S+, and others.
Hugunin, a graduate student at the Massachusetts Institute of Technology (MIT),: 10  joined the Corporation for National Research Initiatives (CNRI) in 1997 to work on JPython, leaving Paul Dubois of Lawrence Livermore National Laboratory (LLNL) to take over as maintainer.: 10  Other early contributors include David Ascher, Konrad Hinsen and Travis Oliphant.: 10

Numarray
A new package called Numarray was written as a more flexible replacement for Numeric. Like Numeric, it too is now deprecated. Numarray had faster operations for large arrays, but was slower than Numeric on small ones, so for a time both packages were used in parallel for different use cases. The last version of Numeric (v24.2) was released on 11 November 2005, while the last version of numarray (v1.5.2) was released on 24 August 2006.
There was a desire to get Numeric into the Python standard library, but Guido van Rossum decided that the code was not maintainable in its state then.

NumPy
In early 2005, NumPy developer Travis Oliphant wanted to unify the community around a single array package and ported Numarray's features to Numeric, releasing the result as NumPy 1.0 in 2006. This new project was part of SciPy. To avoid installing the large SciPy package just to get an array object, this new package was separated and called NumPy. Support for Python 3 was added in 2011 with NumPy version 1.5.0.
In 2011, PyPy started development on an implementation of the NumPy API for PyPy. As of 2023, it is not yet fully compatible with NumPy.

Features
NumPy targets the CPython reference implementation of Python, which is a non-optimizing bytecode interpreter. Mathematical algorithms written for this version of Python often run much slower than compiled equivalents due to the absence of compiler optimization. NumPy addresses the slowness problem partly by providing multidimensional arrays and functions and operators that operate efficiently on arrays; using these requires rewriting some code, mostly inner loops, using NumPy.
Using NumPy in Python gives functionality comparable to MATLAB since they are both interpreted, and they both allow the user to write fast programs as long as most operations work on arrays or matrices instead of scalars. In comparison, MATLAB boasts a large number of additional toolboxes, notably Simulink, whereas NumPy is intrinsically integrated with Python, a more modern and complete programming language. Moreover, complementary Python packages are available; SciPy is a library that adds more MATLAB-like functionality and Matplotlib is a plotting package that provides MATLAB-like plotting functionality. Although matlab can perform sparse matrix operations, numpy alone cannot perform such operations and requires the use of the scipy.sparse library. Internally, both MATLAB and NumPy rely on BLAS and LAPACK for efficient linear algebra computations.
Python bindings of the widely used computer vision library OpenCV utilize NumPy arrays to store and operate on data.
Since images with multiple channels are simply represented as three-dimensional arrays, indexing, slicing or masking with other arrays are very efficient ways to access specific pixels of an image.
The NumPy array as universal data structure in OpenCV for images, extracted feature points, filter kernels and many more vastly simplifies the programming workflow and debugging.
Importantly, many NumPy operations release the global interpreter lock, which allows for multithreaded processing.
NumPy also provides a C API, which allows Python code to interoperate with external libraries written in low-level languages.

The ndarray data structure
The core functionality of NumPy is its "ndarray", for n-dimensional array, data structure. These arrays are strided views on memory. In contrast to Python's built-in list data structure, these arrays are homogeneously typed: all elements of a single array must be of the same type.
Such arrays can also be views into memory buffers allocated by C/C++, Python, and Fortran extensions to the CPython interpreter without the need to copy data around, giving a degree of compatibility with existing numerical libraries. This functionality is exploited by the SciPy package, which wraps a number of such libraries (notably BLAS and LAPACK). NumPy has built-in support for memory-mapped ndarrays.

Limitations
Inserting or appending entries to an array is not as trivially possible as it is with Python's lists.
The np.pad(...) routine to extend arrays actually creates new arrays of the desired shape and padding values, copies the given array into the new one and returns it.
NumPy's np.concatenate([a1,a2]) operation does not actually link the two arrays but returns a new one, filled with the entries from both given arrays in sequence.
Reshaping the dimensionality of an array with np.reshape(...) is only possible as long as the number of elements in the array does not change.
These circumstances originate from the fact that NumPy's arrays must be views on contiguous memory buffers.
Algorithms that are not expressible as a vectorized operation will typically run slowly because they must be implemented in "pure Python", while vectorization may increase memory complexity of some operations from constant to linear, because temporary arrays must be created that are as large as the inputs. Runtime compilation of numerical code has been implemented by several groups to avoid these problems; open source solutions that interoperate with NumPy include numexpr and Numba. Cython and Pythran are static-compiling alternatives to these.
Many modern large-scale scientific computing applications have requirements that exceed the capabilities of the NumPy arrays.
For example, NumPy arrays are usually loaded into a computer's memory, which might have insufficient capacity for the analysis of large datasets.
Further, NumPy operations are executed on a single CPU.
However, many linear algebra operations can be accelerated by executing them on clusters of CPUs or of specialized hardware, such as GPUs and TPUs, which many deep learning applications rely on.
As a result, several alternative array implementations have arisen in the scientific python ecosystem over the recent years, such as Dask for distributed arrays and TensorFlow or JAX for computations on GPUs.
Because of its popularity, these often implement a subset of NumPy's API or mimic it, so that users can change their array implementation with minimal changes to their code required. A library named CuPy, accelerated by Nvidia's CUDA framework, has also shown potential for faster computing, being a 'drop-in replacement' of NumPy.

Examples
Basic operations
Universal functions
Linear algebra
Multidimensional arrays
Incorporation with OpenCV
Nearest-neighbor search
Iterative Python algorithm and vectorized NumPy version.

F2PY
Quickly wrap native code for faster scripts.

See also
Array programming
List of numerical-analysis software
Theano (software)
Matplotlib
Fortran
Row- and column-major order
f2c

References
Further reading
McKinney, Wes (2022). Python for Data Analysis (3rd ed.). O'Reilly. ISBN 978-1098104030.
Bressert, Eli (2012). Scipy and Numpy: An Overview for Developers. O'Reilly. ISBN 978-1-4493-0546-8.
VanderPlas, Jake (2016). "Introduction to NumPy". Python Data Science Handbook: Essential Tools for Working with Data. O'Reilly. pp. 33–96. ISBN 978-1-4919-1205-8.

External links

Official website 
NumPy tutorials
History of NumPy

## Related Articles

### Internal Links

- [API](https://en.wikipedia.org/wiki/API)
- [APL (programming language)](https://en.wikipedia.org/wiki/APL_(programming_language))
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Array](https://en.wikipedia.org/wiki/Array)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Array (data type)](https://en.wikipedia.org/wiki/Array_(data_type))
- [Array programming](https://en.wikipedia.org/wiki/Array_programming)
- [Array slicing](https://en.wikipedia.org/wiki/Array_slicing)
- [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses)
- [Basic Linear Algebra Subprograms](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Big data](https://en.wikipedia.org/wiki/Big_data)
- [Bytecode](https://en.wikipedia.org/wiki/Bytecode)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [CUDA](https://en.wikipedia.org/wiki/CUDA)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language)
- [Central processing unit](https://en.wikipedia.org/wiki/Central_processing_unit)
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Computer cluster](https://en.wikipedia.org/wiki/Computer_cluster)
- [Computer vision](https://en.wikipedia.org/wiki/Computer_vision)
- [Corporation for National Research Initiatives](https://en.wikipedia.org/wiki/Corporation_for_National_Research_Initiatives)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [CuPy](https://en.wikipedia.org/wiki/CuPy)
- [Dask (software)](https://en.wikipedia.org/wiki/Dask_(software))
- [Data buffer](https://en.wikipedia.org/wiki/Data_buffer)
- [Data set](https://en.wikipedia.org/wiki/Data_set)
- [Data structure](https://en.wikipedia.org/wiki/Data_structure)
- [Debugger](https://en.wikipedia.org/wiki/Debugger)
- [Deep learning](https://en.wikipedia.org/wiki/Deep_learning)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Drop-in replacement](https://en.wikipedia.org/wiki/Drop-in_replacement)
- [F2c](https://en.wikipedia.org/wiki/F2c)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics))
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Global interpreter lock](https://en.wikipedia.org/wiki/Global_interpreter_lock)
- [Graphics processing unit](https://en.wikipedia.org/wiki/Graphics_processing_unit)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [High-level programming language](https://en.wikipedia.org/wiki/High-level_programming_language)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Inner loop](https://en.wikipedia.org/wiki/Inner_loop)
- [Feature (computer vision)](https://en.wikipedia.org/wiki/Feature_(computer_vision))
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [Jim Hugunin](https://en.wikipedia.org/wiki/Jim_Hugunin)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [Kernel (image processing)](https://en.wikipedia.org/wiki/Kernel_(image_processing))
- [LAPACK](https://en.wikipedia.org/wiki/LAPACK)
- [Language binding](https://en.wikipedia.org/wiki/Language_binding)
- [Lawrence Livermore National Laboratory](https://en.wikipedia.org/wiki/Lawrence_Livermore_National_Laboratory)
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [Linear algebra](https://en.wikipedia.org/wiki/Linear_algebra)
- [List of algorithms](https://en.wikipedia.org/wiki/List_of_algorithms)
- [List of numerical-analysis software](https://en.wikipedia.org/wiki/List_of_numerical-analysis_software)
- [MATLAB](https://en.wikipedia.org/wiki/MATLAB)
- [Mask (computing)](https://en.wikipedia.org/wiki/Mask_(computing))
- [Massachusetts Institute of Technology](https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology)
- [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [Matrix (mathematics)](https://en.wikipedia.org/wiki/Matrix_(mathematics))
- [MayaVi](https://en.wikipedia.org/wiki/MayaVi)
- [Memory-mapped file](https://en.wikipedia.org/wiki/Memory-mapped_file)
- [Nature (journal)](https://en.wikipedia.org/wiki/Nature_(journal))
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [Numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis)
- [Nvidia](https://en.wikipedia.org/wiki/Nvidia)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [OpenCV](https://en.wikipedia.org/wiki/OpenCV)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_(software))
- [Plot (graphics)](https://en.wikipedia.org/wiki/Plot_(graphics))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python syntax and semantics](https://en.wikipedia.org/wiki/Python_syntax_and_semantics)
- [Reference implementation](https://en.wikipedia.org/wiki/Reference_implementation)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Row- and column-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order)
- [S-PLUS](https://en.wikipedia.org/wiki/S-PLUS)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [S (programming language)](https://en.wikipedia.org/wiki/S_(programming_language))
- [Scalar processor](https://en.wikipedia.org/wiki/Scalar_processor)
- [SciPy](https://en.wikipedia.org/wiki/SciPy)
- [Scikit-image](https://en.wikipedia.org/wiki/Scikit-image)
- [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
- [Simulink](https://en.wikipedia.org/wiki/Simulink)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Space complexity](https://en.wikipedia.org/wiki/Space_complexity)
- [Special interest group](https://en.wikipedia.org/wiki/Special_interest_group)
- [Stride of an array](https://en.wikipedia.org/wiki/Stride_of_an_array)
- [Subset](https://en.wikipedia.org/wiki/Subset)
- [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow)
- [Tensor Processing Unit](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)
- [Theano (software)](https://en.wikipedia.org/wiki/Theano_(software))
- [Travis Oliphant](https://en.wikipedia.org/wiki/Travis_Oliphant)
- [Volatile memory](https://en.wikipedia.org/wiki/Volatile_memory)
- [Wikidata](https://en.wikipedia.org/wiki/Wikidata)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Manual of Style/Dates and numbers](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers)
- [Wikipedia:Please clarify](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)
- [Wikipedia:Wikimedia sister projects](https://en.wikipedia.org/wiki/Wikipedia:Wikimedia_sister_projects)
- [Template:SciPy ecosystem](https://en.wikipedia.org/wiki/Template:SciPy_ecosystem)
- [Template talk:SciPy ecosystem](https://en.wikipedia.org/wiki/Template_talk:SciPy_ecosystem)
- [Help:IPA/English](https://en.wikipedia.org/wiki/Help:IPA/English)
- [Help:Pronunciation respelling key](https://en.wikipedia.org/wiki/Help:Pronunciation_respelling_key)
- [Category:Articles with unsourced statements from December 2023](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_December_2023)
- [Category:Python (programming language) scientific libraries](https://en.wikipedia.org/wiki/Category:Python_(programming_language)_scientific_libraries)
- [Category:Vague or ambiguous time from October 2013](https://en.wikipedia.org/wiki/Category:Vague_or_ambiguous_time_from_October_2013)
- [Category:Wikipedia articles needing clarification from April 2020](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_April_2020)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:37:37.170538+00:00_