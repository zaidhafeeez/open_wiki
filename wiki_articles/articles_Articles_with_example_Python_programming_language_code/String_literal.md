# String literal

## Metadata
- **Last Updated:** 2024-12-15 13:20:22 UTC
- **Original Article:** [String literal](https://en.wikipedia.org/wiki/String_literal)
- **Language:** en
- **Page ID:** 199706

## Summary
A string literal or anonymous string is a literal for a string value in the source code of a computer program. Modern programming languages commonly use a quoted sequence of characters, formally "bracketed delimiters", as in x = "foo", where , "foo" is a string literal with value foo. Methods such as escape sequences can be used to avoid the problem of delimiter collision (issues with brackets) and allow the delimiters to be embedded in a string. There are many alternate notations for specifying string literals especially in complicated cases. The exact notation depends on the programming language in question. Nevertheless, there are general guidelines that most modern programming languages follow.

## Categories
This article belongs to the following categories:

- Category:All articles with unsourced statements
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from February 2012
- Category:Articles with unsourced statements from March 2011
- Category:Short description matches Wikidata
- Category:Source code
- Category:String (computer science)

## Table of Contents

- Syntax
- Delimiter collision
- Escape sequences
- Multiline string literals
- String literal concatenation
- Different kinds of strings
- String interpolation
- Embedding source code in string literals
- See also
- Notes
- References
- External links

## Content

A string literal or anonymous string is a literal for a string value in the source code of a computer program. Modern programming languages commonly use a quoted sequence of characters, formally "bracketed delimiters", as in x = "foo", where , "foo" is a string literal with value foo. Methods such as escape sequences can be used to avoid the problem of delimiter collision (issues with brackets) and allow the delimiters to be embedded in a string. There are many alternate notations for specifying string literals especially in complicated cases. The exact notation depends on the programming language in question. Nevertheless, there are general guidelines that most modern programming languages follow.

Syntax
Bracketed delimiters
Most modern programming languages use bracket delimiters (also balanced delimiters)
to specify string literals. Double quotations are the most common quoting delimiters used:

 "Hi There!"

An empty string is literally written by a pair of quotes with no character at all in between:

 ""

Some languages either allow or mandate the use of single quotations instead of double quotations (the string must begin and end with the same kind of quotation mark and the type of quotation mark may or may not give slightly different semantics):

 'Hi There!'

These quotation marks are unpaired (the same character is used as an opener and a closer), which is a hangover from the typewriter technology which was the precursor of the earliest computer input and output devices.
In terms of regular expressions, a basic quoted string literal is given as:

"[^"]*"

This means that a string literal is written as: a quote, followed by zero, one, or more non-quote characters, followed by a quote. In practice this is often complicated by escaping, other delimiters, and excluding newlines.

Paired delimiters
A number of languages provide for paired delimiters, where the opening and closing delimiters are different. These also often allow nested strings, so delimiters can be embedded, so long as they are paired, but still result in delimiter collision for embedding an unpaired closing delimiter. Examples include PostScript, which uses parentheses, as in (The quick (brown fox)) and m4, which uses the backtick (`) as the starting delimiter, and the apostrophe (') as the ending delimiter. Tcl allows both quotes (for interpolated strings) and braces (for raw strings), as in "The quick brown fox" or {The quick {brown fox}}; this derives from the single quotations in Unix shells and the use of braces in C for compound statements, since blocks of code is in Tcl syntactically the same thing as string literals – that the delimiters are paired is essential for making this feasible.
The Unicode character set includes paired (separate opening and closing) versions of both single and double quotations:

 “Hi There!”
 ‘Hi There!’
 „Hi There!“
 «Hi There!»

These, however, are rarely used, as many programming languages will not register them (one exception is the paired double quotations which can be used in Visual Basic .NET). Unpaired marks are preferred for compatibility, as they are easier to type on a wide range of keyboards, and so even in languages where they are permitted, many projects forbid their use for source code.

Whitespace delimiters
String literals might be ended by newlines.
One example is MediaWiki template parameters.

 {{Navbox
 |name=Nulls
 |title=[[wikt:Null|Nulls]] in [[computing]]
 }}
There might be special syntax for multi-line strings.
In YAML, string literals may be specified by the relative positioning of whitespace and
indentation.

No delimiters
Some programming languages, such as Perl and PHP, allow string literals without any delimiters in some contexts. In the following Perl program, for example, red, green, and blue are string literals, but are unquoted:

   
Perl treats non-reserved sequences of alphanumeric characters as string literals in most contexts. For example, the following two lines of Perl are equivalent:

Declarative notation
In the original FORTRAN programming language (for example), string literals were written in so-called Hollerith notation, where a decimal count of the number of characters was followed by the letter H, and then the characters of the string:

  
This declarative notation style is contrasted with bracketed delimiter quoting, because it does
not require the use of balanced "bracketed" characters on either side of the string.
Advantages:

eliminates text searching (for the delimiter character) and therefore requires significantly less overhead
avoids the problem of delimiter collision
enables the inclusion of metacharacters that might otherwise be mistaken as commands
can be used for quite effective data compression of plain text strings
Drawbacks:

this type of notation is error-prone if used as manual entry by programmers
special care is needed in case of multi byte encodings
This is however not a drawback when the prefix is generated by an algorithm as is most likely the case.

Constructor functions
C++ has two styles of string, one inherited from C (delimited by "), and the safer std::string in the C++ Standard Library. The std::string class is frequently used in the same way a string literal would be used in other languages, and is often preferred to C-style strings for its greater flexibility and safety. But it comes with a performance penalty for string literals, as std::string usually allocates memory dynamically, and must copy the C-style string literal to it at run time.
Before C++11, there was no literal for C++ strings (C++11 allows "this is a C++ string"s with the s at the end of the literal), so the normal constructor syntax was used, for example:

std::string str = "initializer syntax";
std::string str("converting constructor syntax");
std::string str = string("explicit constructor syntax");
all of which have the same interpretation. Since C++11, there is also new constructor syntax:

std::string str{"uniform initializer syntax"};
auto str = "constexpr literal syntax"s;

Delimiter collision
When using quoting, if one wishes to represent the delimiter itself in a string literal, one runs into the problem of delimiter collision. For example, if the delimiter is a double quote, one cannot simply represent a double quote itself by the literal """ as the second quote is interpreted as the end of the string literal, not as the value of the string, and similarly one cannot write "This is "in quotes", but invalid." as the middle quoted portion is instead interpreted as outside of quotes. There are various solutions, the most general-purpose of which is using escape sequences, such as "\"" or "This is \"in quotes\" and properly escaped.", but there are many other solutions.
Paired quotes, such as braces in Tcl, allow nested strings, such as {foo {bar} zork} but do not otherwise solve the problem of delimiter collision, since an unbalanced closing delimiter cannot simply be included, as in {}}.

Doubling up
A number of languages, including Pascal, BASIC, DCL, Smalltalk, SQL, J, and Fortran, avoid delimiter collision by doubling up on the quotation marks that are intended to be part of the string literal
itself:

Dual quoting
Some languages, such as Fortran, Modula-2, JavaScript, Python, and PHP allow more than one quoting delimiter; in the case of two possible delimiters, this is known as dual quoting. Typically, this consists of allowing the programmer to use either single quotations or double quotations interchangeably – each literal must use one or the other.

This does not allow having a single literal with both delimiters in it, however. This can be worked around by using several literals and using string concatenation:

Python has string literal concatenation, so consecutive string literals are concatenated even without an operator, so this can be reduced to:

Delimiter quoting
C++11 introduced so-called raw string literals. They consist, essentially of

R" end-of-string-id ( content ) end-of-string-id ",
that is, after R" the programmer can enter up to 16 characters except whitespace characters, parentheses, or backslash, which form the end-of-string-id (its purpose is to be repeated to signal the end of the string, eos id for short), then an opening parenthesis (to denote the end of the eos id) is required. Then follows the actual content of the literal: Any sequence characters may be used (except that it may not contain a closing parenthesis followed by the eos id followed a quote), and finally – to terminate the string – a closing parenthesis, the eos id, and a quote is required.
The simplest case of such a literal is with empty content and empty eos id: R"()".
The eos id may itself contain quotes: R""(I asked, "Can you hear me?")"" is a valid literal (the eos id is " here.)
Escape sequences don't work in raw string literals.
D supports a few quoting delimiters, with such strings starting with q" plus an opening delimiter and ending with the respective closing delimiter and ". Available delimiter pairs are (), <>, {}, and []; an unpaired non-identifier delimiter is its own closing delimiter. The paired delimiters nest, so that q"(A pair "()" of parens in quotes)" is a valid literal; an example with the non-nesting / character is q"/I asked, "Can you hear me?"/".
Similar to C++11, D allows here-document-style literals with end-of-string ids:

q" end-of-string-id newline content newline end-of-string-id "
In D, the end-of-string-id must be an identifier (alphanumeric characters).
In some programming languages, such as sh and Perl, there are different delimiters that are treated differently, such as doing string interpolation or not, and thus care must be taken when choosing which delimiter to use; see different kinds of strings, below.

Multiple quoting
A further extension is the use of multiple quoting, which allows the author to choose which characters should specify the bounds of a string literal.
For example, in Perl:

all produce the desired result. Although this notation is more flexible, few languages support it; other than Perl, Ruby (influenced by Perl) and C++11 also support these. A variant of multiple quoting is the use of here document-style strings.
Lua (as of 5.1) provides a limited form of multiple quoting, particularly to allow nesting of long comments or embedded strings. Normally one uses [[ and ]] to delimit literal strings (initial newline stripped, otherwise raw), but the opening brackets can include any number of equal signs, and only closing brackets with the same number of signs close the string. For example:

Multiple quoting is particularly useful with regular expressions that contain usual delimiters such as quotes, as this avoids needing to escape them. An early example is sed, where in the substitution command s/regex/replacement/ the default slash / delimiters can be replaced by another character, as in s,regex,replacement, .

Constructor functions
Another option, which is rarely used in modern languages, is to use a function to construct a string, rather than representing it via a literal. This is generally not used in modern languages because the computation is done at run time, rather than at parse time.
For example, early forms of BASIC did not include escape sequences or any other workarounds listed here, and thus one instead was required to use the CHR$ function, which returns a string containing the character corresponding to its argument. In ASCII the quotation mark has the value 34, so to represent a string with quotes on an ASCII system one would write

In C, a similar facility is available via sprintf and the %c "character" format specifier, though in the presence of other workarounds this is generally not used:

These constructor functions can also be used to represent nonprinting characters, though escape sequences are generally used instead. A similar technique can be used in C++ with the std::string stringification operator.

Escape sequences
Escape sequences are a general technique for representing characters that are otherwise difficult to represent directly, including delimiters, nonprinting characters (such as backspaces), newlines, and whitespace characters (which are otherwise impossible to distinguish visually), and have a long history. They are accordingly widely used in string literals, and adding an escape sequence (either to a single character or throughout a string) is known as escaping.
One character is chosen as a prefix to give encodings for characters that are difficult or impossible to include directly. Most commonly this is backslash; in addition to other characters, a key point is that backslash itself can be encoded as a double backslash \\ and for delimited strings the delimiter itself can be encoded by escaping, say by \" for ". A regular expression for such escaped strings can be given as follows, as found in the ANSI C specification:

"(\\.|[^\\"])*"
meaning "a quote; followed by zero or more of either an escaped character (backslash followed by something, possibly backslash or quote), or a non-escape, non-quote character; ending in a quote" – the only issue is distinguishing the terminating quote from a quote preceded by a backslash, which may itself be escaped. Multiple characters can follow the backslash, such as \uFFFF, depending on the escaping scheme.
An escaped string must then itself be lexically analyzed, converting the escaped string into the unescaped string that it represents. This is done during the evaluation phase of the overall lexing of the computer language: the evaluator of the lexer of the overall language executes its own lexer for escaped string literals.
Among other things, it must be possible to encode the character that normally terminates the string constant, plus there must be some way to specify the escape character itself. Escape sequences are not always pretty or easy to use, so many compilers also offer other means of solving the common problems. Escape sequences, however, solve every delimiter problem and most compilers interpret escape sequences. When an escape character is inside a string literal, it means "this is the start of the escape sequence".  Every escape sequence specifies one character which is to be placed directly into the string.  The actual number of characters required in an escape sequence varies.  The escape character is on the top/left of the keyboard, but the editor will translate it, therefore it is not directly tapeable into a string. The backslash is used to represent the escape character in a string literal.
Many languages support the use of metacharacters inside string literals. Metacharacters have varying interpretations depending on the context and language, but are generally a kind of 'processing command' for representing printing or nonprinting characters.
For instance, in a C string literal, if the backslash is followed by a letter such as "b", "n" or "t", then this represents a nonprinting backspace, newline or tab character respectively. Or if the backslash is followed by 1-3 octal digits, then this sequence is interpreted as representing the arbitrary code unit with the specified value in the literal's encoding (for example, the corresponding ASCII code for an ASCII literal). This was later extended to allow more modern hexadecimal character code notation:

Note:  Not all sequences in the list are supported by all parsers, and there may be other escape sequences which are not in the list.

Nested escaping
When code in one programming language is embedded inside another, embedded strings may require multiple levels of escaping. This is particularly common in regular expressions and SQL query within other languages, or other languages inside shell scripts. This double-escaping is often difficult to read and author.
Incorrect quoting of nested strings can present a security vulnerability. Use of untrusted data, as in data fields of an SQL query, should use prepared statements to prevent a code injection attack. In PHP 2 through 5.3, there was a feature called magic quotes which automatically escaped strings (for convenience and security), but due to problems was removed from version 5.4 onward.

Raw strings
A few languages provide a method of specifying that a literal is to be processed without any language-specific interpretation. This avoids the need for escaping, and yields more legible strings.
Raw strings are particularly useful when a common character needs to be escaped, notably in regular expressions (nested as string literals), where backslash \ is widely used, and in DOS/Windows paths, where backslash is used as a path separator. The profusion of backslashes is known as leaning toothpick syndrome, and can be reduced by using raw strings. Compare escaped and raw pathnames in C#:

Extreme examples occur when these are combined – Uniform Naming Convention paths begin with \\, and thus an escaped regular expression matching a UNC name begins with 8 backslashes, "\\\\\\\\", due to needing to escape the string and the regular expression. Using raw strings reduces this to 4 (escaping in the regular expression), as in C# @"\\\\".
In XML documents, CDATA sections allows use of characters such as & and < without an XML parser attempting to interpret them as part of the structure of the document itself. This can be useful when including literal text and scripting code, to keep the document well formed.

Multiline string literals
In many languages, string literals can contain literal newlines, spanning several lines. Alternatively, newlines can be escaped, most often as \n. For example:

and

are both valid bash, producing:

foo
bar

Languages that allow literal newlines include bash, Lua, Perl, PHP, R, and Tcl. In some other languages string literals cannot include newlines.
Two issues with multiline string literals are leading and trailing newlines, and indentation. If the initial or final delimiters are on separate lines, there are extra newlines, while if they are not, the delimiter makes the string harder to read, particularly for the first line, which is often indented differently from the rest. Further, the literal must be unindented, as leading whitespace is preserved – this breaks the flow of the code if the literal occurs within indented code.
The most common solution for these problems is here document-style string literals. Formally speaking, a here document is not a string literal, but instead a stream literal or file literal. These originate in shell scripts and allow a literal to be fed as input to an external command. The opening delimiter is <<END where END can be any word, and the closing delimiter is END on a line by itself, serving as a content boundary – the << is due to redirecting stdin from the literal. Due to the delimiter being arbitrary, these also avoid the problem of delimiter collision. These also allow initial tabs to be stripped via the variant syntax <<-END though leading spaces are not stripped. The same syntax has since been adopted for multiline string literals in a number of languages, most notably Perl, and are also referred to as here documents, and retain the syntax, despite being strings and not involving redirection. As with other string literals, these can sometimes have different behavior specified, such as variable interpolation.
Python, whose usual string literals do not allow literal newlines, instead has a special form of string, designed for multiline literals, called triple quoting. These use a tripled delimiter, either ''' or """. These literals are especially used for inline documentation, known as docstrings.
Tcl allows literal newlines in strings and has no special syntax to assist with multiline strings, though delimiters can be placed on lines by themselves and leading and trailing newlines stripped via string trim, while string map can be used to strip indentation.

String literal concatenation
A few languages provide string literal concatenation, where adjacent string literals are implicitly joined into a single literal at compile time. This is a feature of C, C++, D, Ruby, and Python, which copied it from C. Notably, this concatenation happens at compile time, during lexical analysis (as a phase following initial tokenization), and is contrasted with both run time string concatenation (generally with the + operator) and concatenation during constant folding, which occurs at compile time, but in a later phase (after phrase analysis or "parsing"). Most languages, such as C#, Java and Perl, do not support implicit string literal concatenation, and instead require explicit concatenation, such as with the + operator (this is also possible in D and Python, but illegal in C/C++ – see below); in this case concatenation may happen at compile time, via constant folding, or may be deferred to run time.

Motivation
In C, where the concept and term originate, string literal concatenation was introduced for two reasons:

To allow long strings to span multiple lines with proper indentation in contrast to line continuation, which destroys the indentation scheme; and
To allow the construction of string literals by macros (via stringizing).
In practical terms, this allows string concatenation in early phases of compilation ("translation", specifically as part of lexical analysis), without requiring phrase analysis or constant folding. For example, the following are valid C/C++:

However, the following are invalid:

This is because string literals have array type, char [n] (C) or const char [n] (C++), which cannot be added; this is not a restriction in most other languages.
This is particularly important when used in combination with the C preprocessor, to allow strings to be computed following preprocessing, particularly in macros. As a simple example:

will (if the file is called a.c) expand to:

which is then concatenated, being equivalent to:

A common use case is in constructing printf or scanf format strings, where format specifiers are given by macros.
A more complex example uses stringification of integers (by the preprocessor) to define a macro that expands to a sequence of string literals, which are then concatenated to a single string literal with the file name and line number:

Beyond syntactic requirements of C/C++, implicit concatenation is a form of syntactic sugar, making it simpler to split string literals across several lines, avoiding the need for line continuation (via backslashes) and allowing one to add comments to parts of strings. For example, in Python, one can comment a regular expression in this way:

Problems
Implicit string concatenation is not required by modern compilers, which implement constant folding, and causes hard-to-spot errors due to unintentional concatenation from omitting a comma, particularly in vertical lists of strings, as in:

Accordingly, it is not used in most languages, and it has been proposed for deprecation from D and Python. However, removing the feature breaks backwards compatibility, and replacing it with a concatenation operator introduces issues of precedence – string literal concatenation occurs during lexing, prior to operator evaluation, but concatenation via an explicit operator occurs at the same time as other operators, hence precedence is an issue, potentially requiring parentheses to ensure desired evaluation order.
A subtler issue is that in C and C++, there are different types of string literals, and concatenation of these has implementation-defined behavior, which poses a potential security risk.

Different kinds of strings
Some languages provide more than one kind of literal, which have different behavior. This is particularly used to indicate raw strings (no escaping), or to disable or enable variable interpolation, but has other uses, such as distinguishing character sets. Most often this is done by changing the quoting character or adding a prefix or suffix. This is comparable to prefixes and suffixes to integer literals, such as to indicate hexadecimal numbers or long integers.
One of the oldest examples is in shell scripts, where single quotes indicate a raw string or "literal string", while double quotes have escape sequences and variable interpolation.
For example, in Python, raw strings are preceded by an r or R – compare 'C:\\Windows' with r'C:\Windows' (though, a Python raw string cannot end in an odd number of backslashes). Python 2 also distinguishes two types of strings: 8-bit ASCII ("bytes") strings (the default), explicitly indicated with a b or B prefix, and Unicode strings, indicated with a u or U prefix. while in Python 3 strings are Unicode by default and bytes are a separate bytes type that when initialized with quotes must be prefixed with a b.
C#'s notation for raw strings is called @-quoting.

While this disables escaping, it allows double-up quotes, which allow one to represent quotes within the string:

C++11 allows raw strings, unicode strings (UTF-8, UTF-16, and UTF-32), and wide character strings, determined by prefixes. It also adds literals for the existing C++ string, which is generally preferred to the existing C-style strings.
In Tcl, brace-delimited strings are literal, while quote-delimited strings have escaping and interpolation.
Perl has a wide variety of strings, which are more formally considered operators, and are known as quote and quote-like operators. These include both a usual syntax (fixed delimiters) and a generic syntax, which allows a choice of delimiters; these include:

REXX uses suffix characters to specify characters or strings using their hexadecimal or binary code. E.g.,

all yield the space character, avoiding the function call X2C(20).

String interpolation
In some languages, string literals may contain placeholders referring to variables or expressions in the current context, which are evaluated (usually at run time). This is referred to as variable interpolation, or more generally string interpolation. Languages that support interpolation generally distinguish strings literals that are interpolated from ones that are not. For example, in sh-compatible Unix shells (as well as Perl and Ruby), double-quoted (quotation-delimited, ") strings are interpolated, while single-quoted (apostrophe-delimited, ') strings are not. Non-interpolated string literals are sometimes referred to as "raw strings", but this is distinct from "raw string" in the sense of escaping. For example, in Python, a string prefixed with r or R has no escaping or interpolation, a normal string (no prefix) has escaping but no interpolation, and a string prefixed with f or F has escaping and interpolation.
For example, the following Perl code:

produces the output:

Nancy said Hello World to the crowd of people.

In this case, the metacharacter character ($) (not to be confused with the sigil in the variable assignment statement) is interpreted to indicate variable interpolation, and requires some escaping if it needs to be outputted literally.
This should be contrasted with the printf function, which produces the same output using notation such as:

but does not perform interpolation: the %s is a placeholder in a printf format string, but the variables themselves are outside the string.
This is contrasted with "raw" strings:

which produce output like:

$name said $greeting to the crowd of people.

Here the $ characters are not metacharacters, and are not interpreted to have any meaning other than plain text.

Embedding source code in string literals
Languages that lack flexibility in specifying string literals make it particularly cumbersome to write programming code that generates other programming code. This is particularly true when the generation language is the same or similar to the output language.
For example:

writing code to produce quines
generating an output language from within a web template;
using XSLT to generate XSLT, or SQL to generate more SQL
generating a PostScript representation of a document for printing purposes, from within a document-processing application written in C or some other language.
Nevertheless, some languages are particularly well-adapted to produce this sort of self-similar output, especially those that support multiple options for avoiding delimiter collision.
Using string literals as code that generates other code may have adverse security implications, especially if the output is based at least partially on untrusted user input. This is particularly acute in the case of Web-based applications, where malicious users can take advantage of such weaknesses to subvert the operation of the application, for example by mounting an SQL injection attack.

See also
Character literal
XML Literals
Sigil (computer programming)

Notes
References
External links
Literals In Programming

## Archive Info
- **Archived on:** 2024-12-15 20:38:49 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 28819 bytes
- **Word Count:** 4514 words
