# Biopython

## Article Metadata

- **Last Updated:** 2024-12-14T19:34:00.797100+00:00
- **Original Article:** [Biopython](https://en.wikipedia.org/wiki/Biopython)
- **Language:** en
- **Page ID:** 559868

## Summary

The Biopython project is an open-source collection of non-commercial Python tools for computational biology and bioinformatics, created by an international association of developers. It contains classes to represent biological sequences and sequence annotations, and it is able to read and write to a variety of file formats. It also allows for a programmatic means of accessing online databases of biological information, such as those at NCBI. Separate modules extend Biopython's capabilities to se

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Bioinformatics software
- Category:Computational science
- Category:Free bioinformatics software
- Category:Module:Wd reference errors
- Category:Official website different in Wikidata and Wikipedia
- Category:Python (programming language) scientific libraries
- Category:Short description is different from Wikidata

## Table of Contents

- History
- Design
- Key features and examples
- See also
- References
- External links

## Content

The Biopython project is an open-source collection of non-commercial Python tools for computational biology and bioinformatics, created by an international association of developers. It contains classes to represent biological sequences and sequence annotations, and it is able to read and write to a variety of file formats. It also allows for a programmatic means of accessing online databases of biological information, such as those at NCBI. Separate modules extend Biopython's capabilities to sequence alignment, protein structure, population genetics, phylogenetics, sequence motifs, and machine learning. Biopython is one of a number of Bio* projects designed to reduce code duplication in computational biology.

History
Biopython development began in 1999 and it was first released in July 2000. It was developed during a similar time frame and with analogous goals to other projects that added bioinformatics capabilities to their respective programming languages, including BioPerl, BioRuby and BioJava. Early developers on the project included Jeff Chang, Andrew Dalke and Brad Chapman, though over 100 people have made contributions to date. In 2007, a similar Python project, namely PyCogent, was established.
The initial scope of Biopython involved accessing, indexing and processing biological sequence files. While this is still a major focus, over the following years added modules have extended its functionality to cover additional areas of biology (see Key features and examples).
As of version 1.77, Biopython no longer supports Python 2.

Design
Wherever possible, Biopython follows the conventions used by the Python programming language to make it easier for users familiar with Python. For example, Seq and SeqRecord objects can be manipulated via slicing, in a manner similar to Python's strings and lists. It is also designed to be functionally similar to other Bio* projects, such as BioPerl.
Biopython is able to read and write most common file formats for each of its functional areas, and its license is permissive and compatible with most other software licenses, which allow Biopython to be used in a variety of software projects.

Key features and examples
Sequences
A core concept in Biopython is the biological sequence, and this is represented by the Seq class.  A Biopython Seq object is similar to a Python string in many respects: it supports the Python slice notation, can be concatenated with other sequences and is immutable. In addition, it includes sequence-specific methods and specifies the particular biological alphabet used.

Sequence annotation
The SeqRecord class describes sequences, along with information such as name, description and features in the form of SeqFeature objects.  Each SeqFeature object specifies the type of the feature and its location. Feature types can be ‘gene’, ‘CDS’ (coding sequence), ‘repeat_region’, ‘mobile_element’ or others, and the position of features in the sequence can be exact or approximate.

Input and output
Biopython can read and write to a number of common sequence formats, including FASTA, FASTQ, GenBank, Clustal, PHYLIP and NEXUS.  When reading files, descriptive information in the file is used to populate the members of Biopython classes, such as SeqRecord.  This allows records of one file format to be converted into others.
Very large sequence files can exceed a computer's memory resources, so Biopython provides various options for accessing records in large files.  They can be loaded entirely into memory in Python data structures, such as lists or dictionaries, providing fast access at the cost of memory usage.  Alternatively, the files can be read from disk as needed, with slower performance but lower memory requirements.

Accessing online databases
Through the Bio.Entrez module, users of Biopython can download biological data from NCBI databases.  Each of the functions provided by the Entrez search engine is available through functions in this module, including searching for and downloading records.

Phylogeny
The Bio.Phylo module provides tools for working with and visualising phylogenetic trees.  A variety of file formats are supported for reading and writing, including Newick, NEXUS and phyloXML.  Common tree manipulations and traversals are supported via the Tree and Clade objects.  Examples include converting and collating tree files, extracting subsets from a tree, changing a tree's root, and analysing branch features such as length or score.
Rooted trees can be drawn in ASCII or using matplotlib (see Figure 1), and the Graphviz library can be used to create unrooted layouts (see Figure 2).

Genome diagrams
The GenomeDiagram module provides methods of visualising sequences within Biopython.  Sequences can be drawn in a linear or circular form (see Figure 3), and many output formats are supported, including PDF and PNG.  Diagrams are created by making tracks and then adding sequence features to those tracks.  By looping over a sequence's features and using their attributes to decide if and how they are added to the diagram's tracks, one can exercise much control over the appearance of the final diagram.  Cross-links can be drawn between different tracks, allowing one to compare multiple sequences in a single diagram.

Macromolecular structure
The Bio.PDB module can load molecular structures from PDB and mmCIF files, and was added to Biopython in 2003.  The Structure object is central to this module, and it organises macromolecular structure in a hierarchical fashion: Structure objects contain Model objects which contain Chain objects which contain Residue objects which contain Atom objects.  Disordered residues and atoms get their own classes, DisorderedResidue and DisorderedAtom, that describe their uncertain positions.
Using Bio.PDB, one can navigate through individual components of a macromolecular structure file, such as examining each atom in a protein.  Common analyses can be carried out, such as measuring distances or angles, comparing residues and calculating residue depth.

Population genetics
The Bio.PopGen module adds support to Biopython for Genepop, a software package for statistical analysis of population genetics.  This allows for analyses of Hardy–Weinberg equilibrium, linkage disequilibrium and other features of a population's allele frequencies.
This module can also carry out population genetic simulations using coalescent theory with the fastsimcoal2 program.

Wrappers for command line tools
Many of Biopython's modules contain command line wrappers for commonly used tools, allowing these tools to be used from within Biopython.  These wrappers include BLAST, Clustal, PhyML, EMBOSS and SAMtools.  Users can subclass a generic wrapper class to add support for any other command line tool.

See also
Open Bioinformatics Foundation
BioPerl
BioRuby
BioJS
BioJava

References
External links
Official website
Biopython Tutorial and Cookbook (PDF)
Biopython source code on GitHub

## Related Articles

### Internal Links

- [ASCII art](https://en.wikipedia.org/wiki/ASCII_art)
- [Allele frequency](https://en.wikipedia.org/wiki/Allele_frequency)
- [Array slicing](https://en.wikipedia.org/wiki/Array_slicing)
- [Associative array](https://en.wikipedia.org/wiki/Associative_array)
- [BLAST (biotechnology)](https://en.wikipedia.org/wiki/BLAST_(biotechnology))
- [BioJS](https://en.wikipedia.org/wiki/BioJS)
- [BioJava](https://en.wikipedia.org/wiki/BioJava)
- [BioPerl](https://en.wikipedia.org/wiki/BioPerl)
- [BioRuby](https://en.wikipedia.org/wiki/BioRuby)
- [Bioinformatics](https://en.wikipedia.org/wiki/Bioinformatics)
- [Biological database](https://en.wikipedia.org/wiki/Biological_database)
- [Biomolecular structure](https://en.wikipedia.org/wiki/Biomolecular_structure)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Clustal](https://en.wikipedia.org/wiki/Clustal)
- [Coalescent theory](https://en.wikipedia.org/wiki/Coalescent_theory)
- [Computational biology](https://en.wikipedia.org/wiki/Computational_biology)
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Crystallographic Information File](https://en.wikipedia.org/wiki/Crystallographic_Information_File)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Duplicate code](https://en.wikipedia.org/wiki/Duplicate_code)
- [EMBOSS](https://en.wikipedia.org/wiki/EMBOSS)
- [Entrez](https://en.wikipedia.org/wiki/Entrez)
- [FASTA format](https://en.wikipedia.org/wiki/FASTA_format)
- [FASTQ format](https://en.wikipedia.org/wiki/FASTQ_format)
- [Graphviz](https://en.wikipedia.org/wiki/Graphviz)
- [Hardy–Weinberg principle](https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle)
- [Linkage disequilibrium](https://en.wikipedia.org/wiki/Linkage_disequilibrium)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [National Center for Biotechnology Information](https://en.wikipedia.org/wiki/National_Center_for_Biotechnology_Information)
- [Newick format](https://en.wikipedia.org/wiki/Newick_format)
- [Nexus file](https://en.wikipedia.org/wiki/Nexus_file)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Open Bioinformatics Foundation](https://en.wikipedia.org/wiki/Open_Bioinformatics_Foundation)
- [PubMed Central](https://en.wikipedia.org/wiki/PubMed_Central)
- [PubMed](https://en.wikipedia.org/wiki/PubMed)
- [PhyloXML](https://en.wikipedia.org/wiki/PhyloXML)
- [Phylogenetic tree](https://en.wikipedia.org/wiki/Phylogenetic_tree)
- [Phylogenetics](https://en.wikipedia.org/wiki/Phylogenetics)
- [Population genetics](https://en.wikipedia.org/wiki/Population_genetics)
- [PDF](https://en.wikipedia.org/wiki/PDF)
- [PNG](https://en.wikipedia.org/wiki/PNG)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Protein Data Bank (file format)](https://en.wikipedia.org/wiki/Protein_Data_Bank_(file_format))
- [Protein structure](https://en.wikipedia.org/wiki/Protein_structure)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SAMtools](https://en.wikipedia.org/wiki/SAMtools)
- [Sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment)
- [Sequence motif](https://en.wikipedia.org/wiki/Sequence_motif)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Template:Cite Q](https://en.wikipedia.org/wiki/Template:Cite_Q)
- [Template:Cite web](https://en.wikipedia.org/wiki/Template:Cite_web)
- [Module:Wd/doc](https://en.wikipedia.org/wiki/Module:Wd/doc)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:34:00.797100+00:00_