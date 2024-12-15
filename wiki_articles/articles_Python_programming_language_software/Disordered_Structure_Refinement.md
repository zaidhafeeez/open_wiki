# Disordered Structure Refinement

## Metadata
- **Last Updated:** 2024-12-13 15:05:49 UTC
- **Original Article:** [Disordered Structure Refinement](https://en.wikipedia.org/wiki/Disordered_Structure_Refinement)
- **Language:** en
- **Page ID:** 53123871

## Summary
The Disordered Structure Refinement program (DSR), written by Daniel Kratzert, is designed to simplify the modeling of molecular disorder in crystal structures using SHELXL by George M. Sheldrick. It has a database of approximately 120 standard solvent molecules and molecular moieties. These can be inserted into the crystal structure with little effort, while at the same time chemically meaningful binding and angular restraints are set. DSR was developed because the previous description of disorder in crystal structures with SHELXL was very lengthy and error-prone. Instead of editing large text files manually and defining restraints manually, this process is automated with DSR.

## Categories
This article belongs to the following categories:

- Category:CS1 German-language sources (de)
- Category:Crystallography software
- Category:Python (programming language) software

## Table of Contents

- Application
- Graphical user interface
- Programming
- References
- External links

## Content

The Disordered Structure Refinement program (DSR), written by Daniel Kratzert, is designed to simplify the modeling of molecular disorder in crystal structures using SHELXL by George M. Sheldrick. It has a database of approximately 120 standard solvent molecules and molecular moieties. These can be inserted into the crystal structure with little effort, while at the same time chemically meaningful binding and angular restraints are set. DSR was developed because the previous description of disorder in crystal structures with SHELXL was very lengthy and error-prone. Instead of editing large text files manually and defining restraints manually, this process is automated with DSR.

Application
DSR can be started in a command line. The call has the basic form:

dsr [option] (SHELXL file)

DSR is controlled with a special command in the corresponding SHELXL file. This has the following syntax:

REM DSR PUT/REPLACE "fragment" WITH (atoms) ON (atoms or q-peaks) PART 1 OCC -21 =
  RESI DFIX

The DSR command must always start with REM so that SHELXL does not recognize this line as its own command. Which atom of the molecule fragment from the database corresponds to which atom or q-peak in the crystal structure is specified in the list following WITH and ON.
By running

dsr -r file.res 

the fragment fit is performed and the restraints transferred.

Graphical user interface
Since 2016 ShelXle has a graphical interface to DSR. Most commands of the command line version can be executed there.
In order to transfer a fragment into a structure, three atoms / q-peaks have to be selected in ShelXle and in the DSR GUI each to specify the position of the fragment. The 3D view of the fragment then shows a preview of the subsequent fragment fit.

Programming
DSR is only programmed in Python. Therefore, it runs in any Python-supported operating system.
It is under the free Beerware license and can be downloaded free of charge and changed as desired.

References
External links
Official website

## Archive Info
- **Archived on:** 2024-12-15 20:27:54 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2004 bytes
- **Word Count:** 324 words
