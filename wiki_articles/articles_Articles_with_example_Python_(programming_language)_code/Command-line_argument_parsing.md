# Command-line argument parsing

_Last updated: 2024-12-14T15:40:28.673169_

**Original Article:** [Command-line argument parsing](https://en.wikipedia.org/wiki/Command-line_argument_parsing)

**Summary:** Different command-line argument parsing methods are used by different programming languages to parse command-line arguments.

## Categories
- Category:Articles with example Java code
- Category:Articles with example PHP code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Racket code
- Category:Articles with short description
- Category:Command shells
- Category:Short description matches Wikidata

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