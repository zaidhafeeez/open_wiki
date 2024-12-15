# One-liner program

## Metadata
- **Last Updated:** 2024-12-03 06:54:41 UTC
- **Original Article:** [One-liner program](https://en.wikipedia.org/wiki/One-liner_program)
- **Language:** en
- **Page ID:** 898917

## Summary
In computer programming, a one-liner program originally was textual input to the command line of an operating system shell that performed some function in just one line of input. In the present day, a one-liner can be

an expression written in the language of the shell;
the invocation of an interpreter together with program source for the interpreter to run;
the invocation of a compiler together with source to compile and instructions for executing the compiled program.
Certain dynamic languages for scripting, such as AWK, sed, and Perl, have traditionally been adept at expressing one-liners.
Shell interpreters such as Unix shells or Windows PowerShell allow for the construction of powerful one-liners.
The use of the phrase one-liner has been widened to also include program-source for any language that does something useful in one line.

## Categories
This article belongs to the following categories:

- Category:All articles needing additional references
- Category:Articles needing additional references from May 2019
- Category:Articles with example C code
- Category:Articles with example Haskell code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Racket code
- Category:Articles with short description
- Category:Computer programming
- Category:Pages using Sister project links with default search
- Category:Short description is different from Wikidata

## Table of Contents

- History
- Examples
- See also
- References
- External links

## Content

In computer programming, a one-liner program originally was textual input to the command line of an operating system shell that performed some function in just one line of input. In the present day, a one-liner can be

an expression written in the language of the shell;
the invocation of an interpreter together with program source for the interpreter to run;
the invocation of a compiler together with source to compile and instructions for executing the compiled program.
Certain dynamic languages for scripting, such as AWK, sed, and Perl, have traditionally been adept at expressing one-liners.
Shell interpreters such as Unix shells or Windows PowerShell allow for the construction of powerful one-liners.
The use of the phrase one-liner has been widened to also include program-source for any language that does something useful in one line.

History
The concept of a one-liner program has been known since the 1960s with the release of the APL programming language. With its terse syntax and powerful mathematical operators, APL allowed useful programs to be represented in a few symbols.
In the 1970s, one-liners became associated with the rise of the home computer and BASIC. Computer magazines published type-in programs in many dialects of BASIC. Some magazines devoted regular columns solely to impressive short and one-line programs.
The word One-liner also has two references in the index of the book The AWK Programming Language (the book is often referred to by the abbreviation TAPL). It explains the programming language AWK, which is part of the Unix operating system. The authors explain the birth of the one-liner paradigm with their daily work on early Unix machines:

The 1977 version had only a few built-in variables and predefined functions. It was designed for writing short programs […] Our model was that an invocation would be one or two lines long, typed in and used immediately. Defaults were chosen to match this style […] We, being the authors, knew how the language was supposed to be used, and so we only wrote one-liners.
Notice that this original definition of a one-liner implies immediate execution of the program without any compilation. So, in a strict sense, only source code for interpreted languages qualifies as a one-liner. But this strict understanding of a one-liner was broadened in 1985 when the IOCCC introduced the category of Best One Liner for C, which is a compiled language.

Examples
One-liners are also used to show off the differential expressive power of programming languages. Frequently, one-liners are used to demonstrate programming ability. Contests are often held to see who can create the most exceptional one-liner.

BASIC
A single line of BASIC can typically hold up to 255 characters, and one liners ranged from simple games to graphical demos. One of the better-known demo one-liners is colloquially known as 10PRINT, written for the Commodore 64:

C
The following example is a C program (a winning entry in the "Best one-liner" category of the IOCCC).

This one-liner program is a glob pattern matcher. It understands the glob characters *, meaning zero or more characters, and ?, meaning exactly one character, just like most Unix shells.
Run it with two args, the string and the glob pattern. The exit status is 0 (shell true) when the pattern matches, 1 otherwise. The glob pattern must match the whole string, so you may want to use * at the beginning and end of the pattern if you are looking for something in the middle. Examples:

AWK
The book The AWK Programming Language contains 20 examples of one-liners at the end of the book's first chapter.
Here are the very first of them:

Print the total number of input lines (like wc -l): 
Print the tenth input line: 
Print the last field of every input line:

J
Here are examples in J:

A function avg to return the average of a list of numbers: 
Quicksort:

Perl
Here are examples in the Perl programming language:

Look for duplicate words
perl -0777 -ne 'print "$.: doubled $_\n" while /\b(\w+)\b\s+\b\1\b/gi' 

Find Palindromes in /usr/dict/words
perl -lne 'print if $_ eq reverse' /usr/dict/words

in-place edit of *.c files changing all foo to bar
perl -p -i.bak -e 's/\bfoo\b/bar/g' *.c

Many one-liners are practical. For example, the following Perl one-liner will reverse all the bytes in a file:

While most Perl one-liners are imperative, Perl's support for anonymous functions, closures, map, filter (grep) and fold (List::Util::reduce) allows the creation of 'functional' one-liners.
This one-liner creates a function that can be used to return a list of primes up to the value of the first parameter:

It can be used on the command line, like this:

perl -e'$,=",";print sub { grep { $a=$_; !grep { !($a % $_) } (2..$_-1)} (2..$_[0]) }->(shift)' number

to print out a comma-separated list of primes in the range 2 - number.

Haskell
The following Haskell program is a one-liner: it sorts its input lines ASCIIbetically.

An even shorter version:

Usable on the command line like:

Racket
The following Racket program is equivalent to the above Haskell example:

and this can be used on the command line as follows:

racket -e '(for-each displayln (sort (port->lines) string<?))'

Python
Performing one-liners directly on the Unix command line can be accomplished by using Python's -cmd flag (-c for short), and typically requires the import of one or more modules. Statements are separated using ";" instead of newlines. For example, to print the last field of unix long listing:

ls -l | python -c "import sys;[sys.stdout.write(' '.join([line.split(' ')[-1]])) for line in sys.stdin]"

Python wrappers
Several open-source scripts have been developed to facilitate the construction of Python one-liners. Scripts such as 
pyp or Pyline import commonly used modules and provide more human-readable variables in an attempt to make Python functionality more accessible on the command line. Here is a redo of the above example (printing the last field of a unix long listing):

Executable libraries
The Python CGIHTTPServer module for example is also an executable library that performs as a web server with CGI. To start the web server enter:

Tcl
Tcl (Tool Command Language) is a dynamic programming/scripting language based on concepts of Lisp, C, and Unix shells. It can be used interactively, or by running scripts (programs) which can use a package system for structuring.
Many strings are also well-formed lists. Every simple word is a list of length one, and elements of longer lists are separated by whitespace. For instance, a string that corresponds to a list of three elements:

Strings with unbalanced quotes or braces, or non-space characters directly following closing braces, cannot be parsed as lists directly. You can explicitly split them to make a list.
The "constructor" for lists is of course called list. It's recommended to use when elements come from variable or command substitution (braces won't do that). As Tcl commands are lists anyway, the following is a full substitute for the list command:

Windows PowerShell
Finding palindromes in file words.txt

Piping semantics in PowerShell help enable complex scenarios with one-liner programs. This one-liner in PowerShell script takes a list of names and counts from a comma-separated value file, and returns the sum of the counts for each name.

See also
Bookmarklet
Tcl

References
External links

Perl Programming links
Wikibooks Free Tcl Programming introduction & download pdf
SourceForge, download website and also Multiple computer languages
Tcl Sources, main Tcl and Tk source code download website
Tcler's Wiki, Tcl/Tk scripts and reference clearing house
TkDocs, Tcl/Tk Official documentation and archives

## Archive Info
- **Archived on:** 2024-12-15 21:05:35 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 7733 bytes
- **Word Count:** 1240 words
