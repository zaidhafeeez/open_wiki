# Move-to-front transform

## Article Metadata

- **Last Updated:** 2024-12-14T19:41:05.213761+00:00
- **Original Article:** [Move-to-front transform](https://en.wikipedia.org/wiki/Move-to-front_transform)
- **Language:** en
- **Page ID:** 1039739

## Summary

The move-to-front (MTF) transform is an encoding of data (typically a stream of bytes) designed to improve the performance of entropy encoding techniques of compression.  When efficiently implemented, it is fast enough that its benefits usually justify including it as an extra step in data compression algorithm.
This algorithm was first published by Boris Ryabko under the name of "book stack" in 1980. Subsequently, it was rediscovered by J.K. Bentley et al. in 1986, as attested in the explanator

## Categories

- Category:All Wikipedia articles needing clarification
- Category:All articles needing additional references
- Category:All articles needing examples
- Category:Articles needing additional references from May 2011
- Category:Articles needing examples from February 2012
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 interwiki-linked names
- Category:Data compression
- Category:Data compression transforms
- Category:Lossless compression algorithms
- Category:Short description is different from Wikidata
- Category:Wikipedia articles needing clarification from February 2011
- Category:Wikipedia articles needing clarification from July 2015

## Table of Contents

- The transform
- Implementation
- Use in practical data compression algorithms
- Move-to-front linked-list
- References
- External links

## Content

The move-to-front (MTF) transform is an encoding of data (typically a stream of bytes) designed to improve the performance of entropy encoding techniques of compression.  When efficiently implemented, it is fast enough that its benefits usually justify including it as an extra step in data compression algorithm.
This algorithm was first published by Boris Ryabko under the name of "book stack" in 1980. Subsequently, it was rediscovered by J.K. Bentley et al. in 1986, as attested in the explanatory note.

The transform
The main idea is that each symbol in the data is replaced by its index in the stack of “recently used symbols”. For example, long sequences of identical symbols are replaced by as many zeroes, whereas when a symbol that has not been used in a long time appears, it is replaced with a large number. Thus at the end the data is transformed into a sequence of integers; if the data exhibits a lot of local correlations, then these integers tend to be small.
Let us give a precise description. Assume for simplicity that the symbols in the data are bytes.
Each byte value is encoded by its index in a list of bytes, which changes over the course of the algorithm.  The list is initially in order by byte value (0, 1, 2, 3, ..., 255).  Therefore, the first byte is always encoded by its own value.  However, after encoding a byte, that value is moved to the front of the list before continuing to the next byte.
An example will shed some light on how the transform works.  Imagine instead of bytes, we are encoding values in a–z.  We wish to transform the following sequence:

bananaaa

By convention, the list is initially (abcdefghijklmnopqrstuvwxyz).  The first letter in the sequence is b, which appears at index 1 (the list is indexed from 0 to 25).  We put a 1 to the output stream:

1

The b moves to the front of the list, producing (bacdefghijklmnopqrstuvwxyz).  The next letter is a, which now appears at index 1.  So we add a 1 to the output stream. We have:

1,1

and we move the letter a back to the top of the list.  Continuing this way, we find that the sequence is encoded by:

1,1,13,1,1,1,0,0

It is easy to see that the transform is reversible.  Simply maintain the same list and decode by replacing each index in the encoded stream with the letter at that index in the list. Note the difference between this and the encoding method: The index in the list is used directly instead of looking up each value for its index.
i.e. you start again with (abcdefghijklmnopqrstuvwxyz). You take the "1" of the encoded block and look it up in the list, which results in "b". Then move the "b" to front which results in (bacdef...). Then take the next "1", look it up in the list, this results in "a", move the "a" to front ... etc.

Implementation
Details of implementation are important for performance, particularly for decoding.  For encoding, no clear advantage is gained by using a linked list, so using an array to store the list is acceptable, with worst-case performance O(nk), where n is the length of the data to be encoded and k is the number of values (generally a constant for a given implementation).
The typical performance is better because frequently-used symbols are more likely to be at the front and will produce earlier hits. This is also the idea behind a Move-to-front self-organizing list.
However, for decoding, we can use specialized data structures to greatly improve performance.

Python
This is a possible implementation of the move-to-front algorithm in Python.

In this example we can see the MTF code taking advantage of the three repetitive i's in the input word. The common dictionary here, however, is less than ideal since it is initialized with more commonly used ASCII printable characters put after little-used control codes, against the MTF code's design intent of keeping what's commonly used in the front. If one rotates the dictionary to put the more-used characters in earlier places, a better encoding can be obtained:

Use in practical data compression algorithms
The MTF transform takes advantage of local correlation of frequencies to reduce the entropy of a message. Indeed, recently used letters stay towards the front of the list; if use of letters exhibits local correlations, this will result in a large number of small numbers such as "0"'s and "1"'s in the output.
However, not all data exhibits this type of local correlation, and for some messages, the MTF transform may actually increase the entropy.
An important use of the MTF transform is in Burrows–Wheeler transform based compression.  The Burrows–Wheeler transform is very good at producing a sequence that exhibits local frequency correlation from text and certain other special classes of data.  Compression benefits greatly from following up the Burrows–Wheeler transform with an MTF transform before the final entropy-encoding step.

Example
As an example, imagine we wish to compress Hamlet's soliloquy (To be, or not to be...).  We can calculate the size of this message to be 7033 bits.  Naively, we might try to apply the MTF transform directly.  The result is a message with 7807 bits (higher than the original).  The reason is that English text does not in general exhibit a high level of local frequency correlation.  However, if we first apply the Burrows–Wheeler transform, and then the MTF transform, we get a message with 6187 bits.  Note that the Burrows–Wheeler transform does not decrease the entropy of the message; it only reorders the bytes in a way that makes the MTF transform more effective.
One problem with the basic MTF transform is that it makes the same changes for any character, regardless of frequency, which can result in diminished compression as characters that occur rarely may push frequent characters to higher values.  Various alterations and alternatives have been developed for this reason.  One common change is to make it so that characters above a certain point can only be moved to a certain threshold.  Another is to make some algorithm that runs a count of each character's local frequency and uses these values to choose the characters' order at any point.  Many of these transforms still reserve zero for repeat characters, since these are often the most common in data after the Burrows Wheeler Transform.

Move-to-front linked-list
The term Move To Front (MTF) is also used in a slightly different context, as a type of a dynamic linked list. In an MTF list, each element is moved to the front when it is accessed. This ensures that, over time, the more frequently accessed elements are easier to access.

References
External links
"Move to front" by Arturo San Emeterio Campos

## Related Articles

### Internal Links

- [842 (compression algorithm)](https://en.wikipedia.org/wiki/842_(compression_algorithm))
- [A-law algorithm](https://en.wikipedia.org/wiki/A-law_algorithm)
- [ASCII](https://en.wikipedia.org/wiki/ASCII)
- [Adaptive Huffman coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)
- [Adaptive coding](https://en.wikipedia.org/wiki/Adaptive_coding)
- [Adaptive differential pulse-code modulation](https://en.wikipedia.org/wiki/Adaptive_differential_pulse-code_modulation)
- [Algebraic code-excited linear prediction](https://en.wikipedia.org/wiki/Algebraic_code-excited_linear_prediction)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Arithmetic coding](https://en.wikipedia.org/wiki/Arithmetic_coding)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Asymmetric numeral systems](https://en.wikipedia.org/wiki/Asymmetric_numeral_systems)
- [Audio codec](https://en.wikipedia.org/wiki/Audio_codec)
- [Average bitrate](https://en.wikipedia.org/wiki/Average_bitrate)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Bit rate](https://en.wikipedia.org/wiki/Bit_rate)
- [Brotli](https://en.wikipedia.org/wiki/Brotli)
- [Burrows–Wheeler transform](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform)
- [Byte](https://en.wikipedia.org/wiki/Byte)
- [Byte pair encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
- [Bzip2](https://en.wikipedia.org/wiki/Bzip2)
- [Canonical Huffman code](https://en.wikipedia.org/wiki/Canonical_Huffman_code)
- [Chain code](https://en.wikipedia.org/wiki/Chain_code)
- [Chroma subsampling](https://en.wikipedia.org/wiki/Chroma_subsampling)
- [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Code](https://en.wikipedia.org/wiki/Code)
- [Code-excited linear prediction](https://en.wikipedia.org/wiki/Code-excited_linear_prediction)
- [Coding tree unit](https://en.wikipedia.org/wiki/Coding_tree_unit)
- [Color space](https://en.wikipedia.org/wiki/Color_space)
- [Companding](https://en.wikipedia.org/wiki/Companding)
- [Compressed data structure](https://en.wikipedia.org/wiki/Compressed_data_structure)
- [Compressed suffix array](https://en.wikipedia.org/wiki/Compressed_suffix_array)
- [Compression artifact](https://en.wikipedia.org/wiki/Compression_artifact)
- [Constant bitrate](https://en.wikipedia.org/wiki/Constant_bitrate)
- [Context mixing](https://en.wikipedia.org/wiki/Context_mixing)
- [Context tree weighting](https://en.wikipedia.org/wiki/Context_tree_weighting)
- [Convolution](https://en.wikipedia.org/wiki/Convolution)
- [Daniel Sleator](https://en.wikipedia.org/wiki/Daniel_Sleator)
- [Data](https://en.wikipedia.org/wiki/Data)
- [Data compression](https://en.wikipedia.org/wiki/Data_compression)
- [Data compression symmetry](https://en.wikipedia.org/wiki/Data_compression_symmetry)
- [Daubechies wavelet](https://en.wikipedia.org/wiki/Daubechies_wavelet)
- [Deblocking filter](https://en.wikipedia.org/wiki/Deblocking_filter)
- [Deflate](https://en.wikipedia.org/wiki/Deflate)
- [Delta encoding](https://en.wikipedia.org/wiki/Delta_encoding)
- [Delta modulation](https://en.wikipedia.org/wiki/Delta_modulation)
- [Dictionary coder](https://en.wikipedia.org/wiki/Dictionary_coder)
- [Differential pulse-code modulation](https://en.wikipedia.org/wiki/Differential_pulse-code_modulation)
- [Discrete cosine transform](https://en.wikipedia.org/wiki/Discrete_cosine_transform)
- [Discrete sine transform](https://en.wikipedia.org/wiki/Discrete_sine_transform)
- [Discrete wavelet transform](https://en.wikipedia.org/wiki/Discrete_wavelet_transform)
- [Display resolution](https://en.wikipedia.org/wiki/Display_resolution)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dynamic Markov compression](https://en.wikipedia.org/wiki/Dynamic_Markov_compression)
- [Dynamic range](https://en.wikipedia.org/wiki/Dynamic_range)
- [Elias gamma coding](https://en.wikipedia.org/wiki/Elias_gamma_coding)
- [Embedded zerotrees of wavelet transforms](https://en.wikipedia.org/wiki/Embedded_zerotrees_of_wavelet_transforms)
- [Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))
- [Entropy coding](https://en.wikipedia.org/wiki/Entropy_coding)
- [Entropy coding](https://en.wikipedia.org/wiki/Entropy_coding)
- [Exponential-Golomb coding](https://en.wikipedia.org/wiki/Exponential-Golomb_coding)
- [FM-index](https://en.wikipedia.org/wiki/FM-index)
- [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
- [Fibonacci coding](https://en.wikipedia.org/wiki/Fibonacci_coding)
- [Film frame](https://en.wikipedia.org/wiki/Film_frame)
- [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform)
- [Fractal compression](https://en.wikipedia.org/wiki/Fractal_compression)
- [Frame rate](https://en.wikipedia.org/wiki/Frame_rate)
- [Golomb coding](https://en.wikipedia.org/wiki/Golomb_coding)
- [Gordon Cormack](https://en.wikipedia.org/wiki/Gordon_Cormack)
- [Grammar-based code](https://en.wikipedia.org/wiki/Grammar-based_code)
- [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding)
- [Hutter Prize](https://en.wikipedia.org/wiki/Hutter_Prize)
- [Image compression](https://en.wikipedia.org/wiki/Image_compression)
- [Image resolution](https://en.wikipedia.org/wiki/Image_resolution)
- [Incremental encoding](https://en.wikipedia.org/wiki/Incremental_encoding)
- [Information theory](https://en.wikipedia.org/wiki/Information_theory)
- [Interlaced video](https://en.wikipedia.org/wiki/Interlaced_video)
- [Jon Bentley (computer scientist)](https://en.wikipedia.org/wiki/Jon_Bentley_(computer_scientist))
- [Kosambi–Karhunen–Loève theorem](https://en.wikipedia.org/wiki/Kosambi%E2%80%93Karhunen%E2%80%93Lo%C3%A8ve_theorem)
- [Kolmogorov complexity](https://en.wikipedia.org/wiki/Kolmogorov_complexity)
- [LHA (file format)](https://en.wikipedia.org/wiki/LHA_(file_format))
- [LZ4 (compression algorithm)](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm))
- [LZ77 and LZ78](https://en.wikipedia.org/wiki/LZ77_and_LZ78)
- [LZFSE](https://en.wikipedia.org/wiki/LZFSE)
- [Jeff Bonwick](https://en.wikipedia.org/wiki/Jeff_Bonwick)
- [LZRW](https://en.wikipedia.org/wiki/LZRW)
- [LZWL](https://en.wikipedia.org/wiki/LZWL)
- [LZX](https://en.wikipedia.org/wiki/LZX)
- [Lapped transform](https://en.wikipedia.org/wiki/Lapped_transform)
- [Latency (audio)](https://en.wikipedia.org/wiki/Latency_(audio))
- [Lempel–Ziv–Markov chain algorithm](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm)
- [Lempel–Ziv–Oberhumer](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Oberhumer)
- [Lempel–Ziv–Stac](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Stac)
- [Lempel–Ziv–Storer–Szymanski](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Storer%E2%80%93Szymanski)
- [Lempel–Ziv–Welch](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
- [Levenshtein coding](https://en.wikipedia.org/wiki/Levenshtein_coding)
- [Line spectral pairs](https://en.wikipedia.org/wiki/Line_spectral_pairs)
- [Linear predictive coding](https://en.wikipedia.org/wiki/Linear_predictive_coding)
- [Linked list](https://en.wikipedia.org/wiki/Linked_list)
- [List (abstract data type)](https://en.wikipedia.org/wiki/List_(abstract_data_type))
- [Log area ratio](https://en.wikipedia.org/wiki/Log_area_ratio)
- [Lossless compression](https://en.wikipedia.org/wiki/Lossless_compression)
- [Lossy compression](https://en.wikipedia.org/wiki/Lossy_compression)
- [Macroblock](https://en.wikipedia.org/wiki/Macroblock)
- [Mark Adler](https://en.wikipedia.org/wiki/Mark_Adler)
- [Modified Huffman coding](https://en.wikipedia.org/wiki/Modified_Huffman_coding)
- [Modified discrete cosine transform](https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform)
- [Motion compensation](https://en.wikipedia.org/wiki/Motion_compensation)
- [Motion estimation](https://en.wikipedia.org/wiki/Motion_estimation)
- [Motion estimation](https://en.wikipedia.org/wiki/Motion_estimation)
- [Nigel Horspool](https://en.wikipedia.org/wiki/Nigel_Horspool)
- [Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem)
- [PAQ](https://en.wikipedia.org/wiki/PAQ)
- [Peak signal-to-noise ratio](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)
- [Pixel](https://en.wikipedia.org/wiki/Pixel)
- [Plain text](https://en.wikipedia.org/wiki/Plain_text)
- [Prediction by partial matching](https://en.wikipedia.org/wiki/Prediction_by_partial_matching)
- [Prefix code](https://en.wikipedia.org/wiki/Prefix_code)
- [Psychoacoustics](https://en.wikipedia.org/wiki/Psychoacoustics)
- [Pyramid (image processing)](https://en.wikipedia.org/wiki/Pyramid_(image_processing))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Quantization (image processing)](https://en.wikipedia.org/wiki/Quantization_(image_processing))
- [Quantization (signal processing)](https://en.wikipedia.org/wiki/Quantization_(signal_processing))
- [Range coding](https://en.wikipedia.org/wiki/Range_coding)
- [Rate–distortion theory](https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory)
- [Re-Pair](https://en.wikipedia.org/wiki/Re-Pair)
- [Redundancy (information theory)](https://en.wikipedia.org/wiki/Redundancy_(information_theory))
- [Robert Tarjan](https://en.wikipedia.org/wiki/Robert_Tarjan)
- [Ron Rivest](https://en.wikipedia.org/wiki/Ron_Rivest)
- [Run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Sampling (signal processing)](https://en.wikipedia.org/wiki/Sampling_(signal_processing))
- [Self-organizing list](https://en.wikipedia.org/wiki/Self-organizing_list)
- [Sequitur algorithm](https://en.wikipedia.org/wiki/Sequitur_algorithm)
- [Set partitioning in hierarchical trees](https://en.wikipedia.org/wiki/Set_partitioning_in_hierarchical_trees)
- [Shannon coding](https://en.wikipedia.org/wiki/Shannon_coding)
- [Shannon–Fano coding](https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding)
- [Shannon–Fano–Elias coding](https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano%E2%80%93Elias_coding)
- [Silence compression](https://en.wikipedia.org/wiki/Silence_compression)
- [Smallest grammar problem](https://en.wikipedia.org/wiki/Smallest_grammar_problem)
- [Snappy (compression)](https://en.wikipedia.org/wiki/Snappy_(compression))
- [Sound quality](https://en.wikipedia.org/wiki/Sound_quality)
- [Speech coding](https://en.wikipedia.org/wiki/Speech_coding)
- [Standard test image](https://en.wikipedia.org/wiki/Standard_test_image)
- [Sub-band coding](https://en.wikipedia.org/wiki/Sub-band_coding)
- [Texture compression](https://en.wikipedia.org/wiki/Texture_compression)
- [Timeline of information theory](https://en.wikipedia.org/wiki/Timeline_of_information_theory)
- [To be, or not to be](https://en.wikipedia.org/wiki/To_be,_or_not_to_be)
- [Transform coding](https://en.wikipedia.org/wiki/Transform_coding)
- [Tunstall coding](https://en.wikipedia.org/wiki/Tunstall_coding)
- [Unary coding](https://en.wikipedia.org/wiki/Unary_coding)
- [Universal code (data compression)](https://en.wikipedia.org/wiki/Universal_code_(data_compression))
- [Variable bitrate](https://en.wikipedia.org/wiki/Variable_bitrate)
- [Video](https://en.wikipedia.org/wiki/Video)
- [Video codec](https://en.wikipedia.org/wiki/Video_codec)
- [Video compression picture types](https://en.wikipedia.org/wiki/Video_compression_picture_types)
- [Video quality](https://en.wikipedia.org/wiki/Video_quality)
- [Warped linear predictive coding](https://en.wikipedia.org/wiki/Warped_linear_predictive_coding)
- [Wavelet transform](https://en.wikipedia.org/wiki/Wavelet_transform)
- [ZbMATH Open](https://en.wikipedia.org/wiki/ZbMATH_Open)
- [Zstd](https://en.wikipedia.org/wiki/Zstd)
- [Μ-law algorithm](https://en.wikipedia.org/wiki/%CE%9C-law_algorithm)
- [Talk:Move-to-front transform](https://en.wikipedia.org/wiki/Talk:Move-to-front_transform)
- [Wikipedia:Writing better articles](https://en.wikipedia.org/wiki/Wikipedia:Writing_better_articles)
- [Wikipedia:Please clarify](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)
- [Wikipedia:Vagueness](https://en.wikipedia.org/wiki/Wikipedia:Vagueness)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Compression methods](https://en.wikipedia.org/wiki/Template:Compression_methods)
- [Template talk:Compression methods](https://en.wikipedia.org/wiki/Template_talk:Compression_methods)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from May 2011](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_May_2011)
- [Category:Articles needing examples from February 2012](https://en.wikipedia.org/wiki/Category:Articles_needing_examples_from_February_2012)
- [Category:Wikipedia articles needing clarification from February 2011](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_February_2011)
- [Category:Wikipedia articles needing clarification from July 2015](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_July_2015)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:41:05.213761+00:00_