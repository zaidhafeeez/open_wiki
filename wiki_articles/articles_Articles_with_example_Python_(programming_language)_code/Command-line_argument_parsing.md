# Command-line argument parsing

## Article Metadata

- **Last Updated:** 2024-12-14T19:35:07.868804+00:00
- **Original Article:** [Command-line argument parsing](https://en.wikipedia.org/wiki/Command-line_argument_parsing)
- **Language:** en
- **Page ID:** 27256520

## Summary

Different command-line argument parsing methods are used by different programming languages to parse command-line arguments.

## Categories

- Category:Articles with example Java code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Racket code
- Category:Articles with short description
- Category:Command shells
- Category:Short description matches Wikidata

## Table of Contents

- Programming languages

## Content

Different command-line argument parsing methods are used by different programming languages to parse command-line arguments.

Programming languages
C
C uses argv to process command-line arguments.
An example of C argument parsing would be:

C also has functions called getopt and getopt_long.

C#
An example of C# argument parsing would be:

Java
An example of Java argument parsing would be:

Kotlin
Here are some possible ways to print arguments in Kotlin:

Perl
Perl uses @ARGV.

FT
or

AWK
AWK uses ARGV also.

PHP
PHP uses argc as a count of arguments and argv as an array containing the values of the arguments. To create an array from command-line arguments in the -foo:bar format, the following might be used:

PHP can also use getopt().

Python
Python uses sys.argv, e.g.:

Python also has a module called argparse in the standard library for parsing command-line arguments.

Racket
Racket uses a current-command-line-arguments parameter, and provides a racket/cmdline library for parsing these arguments.  Example:

The library parses long and short flags, handles arguments, allows combining short flags, and handles -h and --help automatically:

Rexx
Rexx uses arg, e.g.:

Rust
The args are in env::args().

JavaScript
Node.js
JavaScript programs written for Node.js use the process.argv global variable.

Node.js programs are invoked by running the interpreter node interpreter with a given file, so the first two arguments will be node and the name of the JavaScript source file. It is often useful to extract the rest of the arguments by slicing a sub-array from process.argv.

Bun
JavaScript written for Bun use Bun.argv and the util.parseArgs function.

Deno
JavaScript written for Deno use Deno.args and the parseArgs function.


== References ==

## Related Articles

### Internal Links

- [AWK](https://en.wikipedia.org/wiki/AWK)
- [Array (data structure)](https://en.wikipedia.org/wiki/Array_(data_structure))
- [Bun (software)](https://en.wikipedia.org/wiki/Bun_(software))
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [C syntax](https://en.wikipedia.org/wiki/C_syntax)
- [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface)
- [Deno (software)](https://en.wikipedia.org/wiki/Deno_(software))
- [Getopt](https://en.wikipedia.org/wiki/Getopt)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java (programming language)](https://en.wikipedia.org/wiki/Java_(programming_language))
- [Kotlin (programming language)](https://en.wikipedia.org/wiki/Kotlin_(programming_language))
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Rexx](https://en.wikipedia.org/wiki/Rexx)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:35:07.868804+00:00_