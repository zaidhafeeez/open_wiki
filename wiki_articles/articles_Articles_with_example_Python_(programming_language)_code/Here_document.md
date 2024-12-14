# Here document

## Article Metadata

- **Last Updated:** 2024-12-14T19:38:08.371147+00:00
- **Original Article:** [Here document](https://en.wikipedia.org/wiki/Here_document)
- **Language:** en
- **Page ID:** 1426425

## Summary

In computing, a here document (here-document, here-text, heredoc, hereis, here-string or here-script) is a file literal or input stream literal: it is a section of a source code file that is treated as if it were a separate file. The term is also used for a form of multiline string literals that use similar syntax, preserving line breaks and other whitespace (including indentation) in the text.
Here documents originate in the Unix shell, and are found in the Bourne shell since 1979, and most sub

## Categories

- Category:Articles with example C++ code
- Category:Articles with example D code
- Category:Articles with example PHP code
- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with example Ruby code
- Category:Articles with short description
- Category:Programming constructs
- Category:Short description is different from Wikidata
- Category:String (computer science)
- Category:Webarchive template wayback links

## Table of Contents

- Overview
- File literals
- Multiline string literals
- See also
- References
- Notes
- External links

## Content

In computing, a here document (here-document, here-text, heredoc, hereis, here-string or here-script) is a file literal or input stream literal: it is a section of a source code file that is treated as if it were a separate file. The term is also used for a form of multiline string literals that use similar syntax, preserving line breaks and other whitespace (including indentation) in the text.
Here documents originate in the Unix shell, and are found in the Bourne shell since 1979, and most subsequent shells. Here document-style string literals are found in various high-level languages, notably the Perl programming language (syntax inspired by Unix shell) and languages influenced by Perl, such as PHP and Ruby. JavaScript also supports this functionality via template literals, a feature added in its 6th revision (ES6). Other high-level languages such as Python, Julia and Tcl have other facilities for multiline strings.
Here documents can be treated either as files or strings. Some shells treat them as a format string literal, allowing variable substitution and command substitution inside the literal.

Overview
The most common syntax for here documents, originating in Unix shells, is << followed by a delimiting identifier (often the word EOF or END), followed, starting on the next line, by the text to be quoted, and then closed by the same delimiting identifier on its own line. This syntax is because here documents are formally stream literals, and the content of the here document is often redirected to stdin (standard input) of the preceding command or current shell script/executable. 
The here document syntax is analogous to the shell syntax for input redirection, which is < followed by the name of the file to be used as input.
Other languages often use substantially similar syntax, but details of syntax and actual functionality can vary significantly. When used simply for string literals, the << does not indicate indirection, but is simply a starting delimiter convention. In some languages, such as Ruby, << is also used for input redirection, thus resulting in << being used twice if one wishes to redirect from a here document string literal.

File literals
Narrowly speaking, here documents are file literals or stream literals. These originate in the Unix shell, though similar facilities are available in some other languages.

Unix shells
Here documents are available in many Unix shells. In the following example, text is passed to the tr command (transliterating lower to upper-case) using a here document. This could be in a shell file, or entered interactively at a prompt.

In this case END was used as the delimiting identifier. It specified the start and end of the here document. The redirect and the delimiting identifier do not need to be separated by a space: <<END or << END both work equally well.
By default, behavior is largely identical to the contents of double quotes: variable names are replaced by their values, commands within backticks are evaluated, etc.

This can be disabled by quoting any part of the label, which is then ended by the unquoted value; the behavior is essentially identical to that if the contents were enclosed in single quotes. Thus for example by setting it in single quotes:

Double quotes may also be used, but this is subject to confusion, because expansion does occur in a double-quoted string, but does not occur in a here document with double-quoted delimiter. Single- and double-quoted delimiters are distinguished in some other languages, notably Perl (see below), where behavior parallels the corresponding string quoting.
In POSIX shell but not csh/tcsh, appending a minus sign to the << (i.e. <<-) has the effect that leading tabs are ignored. This allows indenting here documents in shell scripts (primarily for alignment with existing indentation) without changing their value:
A script containing:

produces:

Another use is to output to a file:

Here strings
A here string (available in bash, ksh, or zsh) is syntactically similar, consisting of <<<, and effects input redirection from a word (a sequence treated as a unit by the shell, in this context generally a string literal). In this case the usual shell syntax is used for the word (“here string syntax”), with the only syntax being the redirection: a here string is an ordinary string used for input redirection, not a special kind of string.
A single word need not be quoted:

In case of a string with spaces, it must be quoted:

This could also be written as:

Multiline strings are acceptable, yielding:

Note that leading and trailing newlines, if present, are included:

The key difference from here documents is that, in here documents, the delimiters are on separate lines; the leading and trailing newlines are stripped. Unlike here documents, here strings do not use delimiters.
Here strings are particularly useful for commands that often take short input, such as the calculator bc:

Note that here string behavior can also be accomplished (reversing the order) via piping and the echo command, as in:

however here strings are particularly useful when the last command needs to run in the current process, as is the case with the read builtin:

yields nothing, while

This happens because in the previous example piping causes read to run in a subprocess, and as such cannot affect the environment of the parent process.

Microsoft NMAKE
In Microsoft NMAKE, here documents are referred to as inline files. Inline files are referenced as << or <<pathname: the first notation creates a temporary file, the second notation creates (or overwrites) the file with the specified pathname.
An inline file is terminated with << on a line by itself, optionally followed by the (case-insensitive) keyword KEEP or NOKEEP to indicate whether the created file should be kept.

R
R does not have file literals, but provides equivalent functionality by combining string literals with a string-to-file function. R allows arbitrary whitespace, including newlines, in strings. A string then can be turned into a file descriptor using the textConnection() function.  For example, the following turns a data table embedded in the source code into a data-frame variable:

Data segment
Perl and Ruby have a form of file literal, which can be considered a form of data segment. In these languages, including the line __DATA__ (Perl) or __END__ (Ruby, old Perl) marks the end of the code segment and the start of the data segment. Only the contents prior to this line are executed, and the contents of the source file after this line are available as a file object: PACKAGE::DATA in Perl (e.g., main::DATA) and DATA in Ruby. As an inline file, these are semantically similar to here documents, though there can be only one per script. However, in these languages the term "here document" instead refers to multiline string literals, as discussed below.

Data URI Scheme
As further explained in Data URI scheme, all major web browsers understand URIs that start with data: as here document.

Multiline string literals
The term "here document" or "here string" is also used for multiline string literals in various programming languages, notably Perl (syntax influenced by Unix shell), and languages influenced by Perl, notably PHP and Ruby. The shell-style << syntax is often retained, despite not being used for input redirection.

Perl-influenced
Perl
In Perl there are several different ways to invoke here docs. The delimiters around the tag have the same effect within the here doc as they would in a regular string literal: For example, using double quotes around the tag allows variables to be interpolated, but using single quotes doesn't, and using the tag without either behaves like double quotes. Using backticks as the delimiters around the tag runs the contents of the heredoc as a shell script. It is necessary to make sure that the end tag is at the beginning of the line or the tag will not be recognized by the interpreter.
Note that the here doc does not start at the tag—but rather starts on the next line. So the statement containing the tag continues on after the tag.
Here is an example with double quotes:

Output:

Here is an example with single quotes:

Output:

And an example with backticks (may not be portable):

It is possible to start multiple heredocs on the same line:

The tag itself may contain whitespace, which may allow heredocs to be used without breaking indentation.

Although since Perl version 5.26, heredocs can include indention:

In addition to these strings, Perl also features file literals, namely the contents of the file following __DATA__ (formerly __END__) on a line by itself. This is accessible as the file object PACKAGE::DATA such as main::DATA, and can be viewed as a form of data segment.

PHP
In PHP, here documents are referred to as heredocs. In PHP heredocs are not string literals. Heredoc text behaves just like a double-quoted string, but without the double quotes. For example, meaning `$` will be parsed as a variable start, and `${` or `{$` as a complex variable start.

Outputs

In PHP versions prior to 7.3, the line containing the closing identifier must not contain any other characters, except an optional ending semicolon.  Otherwise, it will not be considered to be a closing identifier, and PHP will continue looking for one. If a proper closing identifier is not found, a parse error will result at the last line of the script. However, from version 7.3, it is no longer required that the closing identifier be followed by a semicolon or newline. Additionally the closing identifier may be indented, in which case the indentation will be stripped from all lines in the doc string.
In PHP 5.3 and later, like Perl, it is possible to not interpolate variables by surrounding the tag with single quotes; this is called a nowdoc:

In PHP 5.3+ it is also possible to surround the tag with double quotes, which like Perl has the same effect as not surrounding the tag with anything at all.

Ruby
The following Ruby code displays a grocery list by using a here document.

The result:

The << in a here document does not indicate input redirection, but Ruby also uses << for input redirection, so redirecting to a file from a here document involves using << twice, in different senses:

As with Unix shells, Ruby also allows for the delimiting identifier not to start on the first column of a line, if the start of the here document is marked with the slightly different starter <<-.
Besides, Ruby treats here documents as a double-quoted string, and as such, it is possible to use the #{} construct to interpolate code.
The following example illustrates both of these features:

Ruby expands on this by providing the "<<~" syntax for omitting indentation on the here document:

The common indentation of two spaces is omitted from all lines:

Like Perl, Ruby allows for starting multiple here documents in one line:

As with Perl, Ruby features file literals, namely the contents of the file following __END__ on a line by itself. This is accessible as the file object DATA and can be viewed as a form of data segment.

Python
Python supports multi-line strings as a "verbatim" string. They may be enclosed in 3 single (') or double (") quotation marks, the latter is shown in the examples below.

From Python 3.6 onwards, verbatim f-strings support variable and expression interpolation.

Java
Text blocks are supported starting with Java 15 via JEP 378:

C++
Since C++11, C++ supports string literals with custom delimiter ("my_delimiter" in this example):

will print out

Start of string. New line
slash \ quote " ' parens ) ( End of string

D
Since version 2.0, D has support for here document-style strings using the 'q' prefix character. These strings begin with q"IDENT followed immediately by a newline (for an arbitrary identifier IDENT), and end with IDENT" at the start of a line.

D also supports a few quoting delimiters, with similar syntax, with such strings starting with q"[ and ending with ]" or similarly for other delimiter character (any of () <> {} or []).

OS/JCL
On IBM's Job Control Language (JCL) used on its earlier MVS and current z/OS operating systems, data which is inline to a job stream can be identified by an * on a DD statement, such as
//SYSIN DD *
or
//SYSIN DD *,DLM=text
In the first case, the lines of text follow and are combined into a pseudo file with the DD name SYSIN. All records following the command are combined until either another OS/JCL command occurs (any line beginning with //), the default EOF sequence (/*) is found, or the physical end of data occurs. In the second case, the conditions are the same, except the DLM= operand is used to specify the text string signalling end of data, which can be used if a data stream contains JCL (again, any line beginning with //), or the /* sequence (such as comments in C or C++ source code). The following compiles and executes an assembly language program, supplied as in-line data to the assembler.

The //SYSIN DD * statement is the functional equivalent of 
<</*
Indicating s stream of data follows, terminated by /*.

Racket
Racket's here strings start with #<< followed by characters that define a terminator for the string.
The content of the string includes all characters between the #<< line and a line whose only content is the specified terminator. More precisely, the content of the string starts after a newline following #<<, and it ends before a newline that is followed by the terminator.

Outputs:

No escape sequences are recognized between the starting and terminating lines; all characters are included in the string (and terminator) literally.

Outputs:

Here strings can be used normally in contexts where normal strings would:

Outputs:

An interesting alternative is to use the language extension at-exp to write @-expressions.
They look like this:

#lang at-exp racket

(displayln @string-append{
This is a long string,
very convenient when a
long chunk of text is
needed.

No worries about escaping
"quotes" or \escapes. It's
also okay to have λ, γ, θ, ...

Embed code: @(number->string (+ 3 4))
})

Outputs:

An @-expression is not specific nor restricted to strings, it is a syntax form that can be composed with the rest of the language.

Windows PowerShell
In PowerShell, here documents are referred to as here-strings. A here-string is a string which starts with an open delimiter (@" or @') and ends with a close delimiter ("@ or '@) on a line by itself, which terminates the string. All characters between the open and close delimiter are considered the string literal.
Using a here-string with double quotes allows variables to be interpreted, using single quotes doesn't.
Variable interpolation occurs with simple variables (e.g. $x but NOT $x.y or $x[0]).
You can execute a set of statements by putting them in $() (e.g. $($x.y) or $(Get-Process | Out-String)).
In the following PowerShell code, text is passed to a function using a here-string.
The function ConvertTo-UpperCase is defined as follows:

Here is an example that demonstrates variable interpolation and statement execution using a here-string with double quotes:

Using a here-string with single quotes instead, the output would look like this:

DIGITAL Command Language (DCL)
In DCL scripts, any input line which does not begin with a $ symbol is implicitly treated as input to the preceding command - all lines which do not begin with $ are here-documents. The input is either passed to the program, or can be explicitly referenced by the logical name SYS$INPUT (analogous to the Unix concept of stdin).
For instance, explicitly referencing the input as SYS$INPUT:

produces:

Additionally, the DECK command, initially intended for punched card support (hence its name: it signified the beginning of a data deck) can be used to supply input to the preceding command. The input deck is ended either by the command $ EOD, or the character pattern specified by the /DOLLARS parameter to DECK.
Example of a program totalling up monetary values:

Would produce the following output (presuming ADD_SUMS was written to read the values and add them):

Example of using DECK /DOLLARS to create one command file from another:

YAML
YAML primarily relies on whitespace indentation for structure, making it resistant to delimiter collision and capable representing multi-line strings with folded string literals:

See also
CDATA
Pipeline (Unix)

References
Notes
General
External links
Here document. Link to Rosetta Code task with examples of here documents in over 15 languages.

## Related Articles

### Internal Links

- [Bash (Unix shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
- [Bc (programming language)](https://en.wikipedia.org/wiki/Bc_(programming_language))
- [Bourne shell](https://en.wikipedia.org/wiki/Bourne_shell)
- [C++11](https://en.wikipedia.org/wiki/C%2B%2B11)
- [CDATA](https://en.wikipedia.org/wiki/CDATA)
- [Code segment](https://en.wikipedia.org/wiki/Code_segment)
- [Command substitution](https://en.wikipedia.org/wiki/Command_substitution)
- [Computer file](https://en.wikipedia.org/wiki/Computer_file)
- [Computing](https://en.wikipedia.org/wiki/Computing)
- [DIGITAL Command Language](https://en.wikipedia.org/wiki/DIGITAL_Command_Language)
- [D (programming language)](https://en.wikipedia.org/wiki/D_(programming_language))
- [Data URI scheme](https://en.wikipedia.org/wiki/Data_URI_scheme)
- [Data segment](https://en.wikipedia.org/wiki/Data_segment)
- [Delimiter](https://en.wikipedia.org/wiki/Delimiter)
- [Delimiter](https://en.wikipedia.org/wiki/Delimiter)
- [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript)
- [Echo (command)](https://en.wikipedia.org/wiki/Echo_(command))
- [End-of-file](https://en.wikipedia.org/wiki/End-of-file)
- [File descriptor](https://en.wikipedia.org/wiki/File_descriptor)
- [High-level programming language](https://en.wikipedia.org/wiki/High-level_programming_language)
- [Identifier](https://en.wikipedia.org/wiki/Identifier)
- [Indentation style](https://en.wikipedia.org/wiki/Indentation_style)
- [Stream (computing)](https://en.wikipedia.org/wiki/Stream_(computing))
- [JDK Enhancement Proposal](https://en.wikipedia.org/wiki/JDK_Enhancement_Proposal)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Java version history](https://en.wikipedia.org/wiki/Java_version_history)
- [Job Control Language](https://en.wikipedia.org/wiki/Job_Control_Language)
- [Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
- [KornShell](https://en.wikipedia.org/wiki/KornShell)
- [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
- [Literal (computer programming)](https://en.wikipedia.org/wiki/Literal_(computer_programming))
- [MVS](https://en.wikipedia.org/wiki/MVS)
- [Microsoft](https://en.wikipedia.org/wiki/Microsoft)
- [Make (software)](https://en.wikipedia.org/wiki/Make_(software))
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix))
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell)
- [Punched card](https://en.wikipedia.org/wiki/Punched_card)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [R (programming language)](https://en.wikipedia.org/wiki/R_(programming_language))
- [Racket (programming language)](https://en.wikipedia.org/wiki/Racket_(programming_language))
- [Read (Unix)](https://en.wikipedia.org/wiki/Read_(Unix))
- [Redirection (computing)](https://en.wikipedia.org/wiki/Redirection_(computing))
- [Rosetta Code](https://en.wikipedia.org/wiki/Rosetta_Code)
- [Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Source code](https://en.wikipedia.org/wiki/Source_code)
- [Standard streams](https://en.wikipedia.org/wiki/Standard_streams)
- [Standard streams](https://en.wikipedia.org/wiki/Standard_streams)
- [String interpolation](https://en.wikipedia.org/wiki/String_interpolation)
- [String literal](https://en.wikipedia.org/wiki/String_literal)
- [Command-line completion](https://en.wikipedia.org/wiki/Command-line_completion)
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Tr (Unix)](https://en.wikipedia.org/wiki/Tr_(Unix))
- [Unix shell](https://en.wikipedia.org/wiki/Unix_shell)
- [Variable (computer science)](https://en.wikipedia.org/wiki/Variable_(computer_science))
- [String interpolation](https://en.wikipedia.org/wiki/String_interpolation)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Z/OS](https://en.wikipedia.org/wiki/Z/OS)
- [Z shell](https://en.wikipedia.org/wiki/Z_shell)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:38:08.371147+00:00_