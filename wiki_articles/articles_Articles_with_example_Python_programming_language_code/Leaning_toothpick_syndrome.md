# Leaning toothpick syndrome

## Metadata
- **Last Updated:** 2024-12-03 07:03:42 UTC
- **Original Article:** [Leaning toothpick syndrome](https://en.wikipedia.org/wiki/Leaning_toothpick_syndrome)
- **Language:** en
- **Page ID:** 5552846

## Summary
In computer programming, leaning toothpick syndrome (LTS) is the situation in which a quoted expression becomes unreadable because it contains a large number of escape characters, usually backslashes ("\"), to avoid delimiter collision.
The official Perl documentation introduced the term to wider usage; there, the phrase is used to describe regular expressions that match Unix-style paths, in which the elements are separated by slashes /. The slash is also used as the default regular expression delimiter, so to be used literally in the expression, it must be escaped with a backslash  \, leading to frequent escaped slashes represented as \/. If doubled, as in URLs, this yields \/\/ for an escaped //. A similar phenomenon occurs for DOS/Windows paths, where the backslash is used as a path separator, requiring a doubled backslash \\ – this can then be re-escaped for a regular expression inside an escaped string, requiring \\\\ to match a single backslash. In extreme cases, such as a regular expression in an escaped string, matching a Uniform Naming Convention path (which begins \\) requires 8 backslashes \\\\\\\\ due to 2 backslashes each being double-escaped.
LTS appears in many programming languages and in many situations, including in patterns that match Uniform Resource Identifiers (URIs) and in programs that output quoted text. Many quines fall into the latter category.

## Categories
This article belongs to the following categories:

- Category:Articles with example Perl code
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:PHP
- Category:Perl
- Category:Regular expressions
- Category:Short description matches Wikidata
- Category:Software engineering folklore

## Table of Contents

- Pattern example
- Quoted-text example
- Other languages
- See also

## Content

In computer programming, leaning toothpick syndrome (LTS) is the situation in which a quoted expression becomes unreadable because it contains a large number of escape characters, usually backslashes ("\"), to avoid delimiter collision.
The official Perl documentation introduced the term to wider usage; there, the phrase is used to describe regular expressions that match Unix-style paths, in which the elements are separated by slashes /. The slash is also used as the default regular expression delimiter, so to be used literally in the expression, it must be escaped with a backslash  \, leading to frequent escaped slashes represented as \/. If doubled, as in URLs, this yields \/\/ for an escaped //. A similar phenomenon occurs for DOS/Windows paths, where the backslash is used as a path separator, requiring a doubled backslash \\ – this can then be re-escaped for a regular expression inside an escaped string, requiring \\\\ to match a single backslash. In extreme cases, such as a regular expression in an escaped string, matching a Uniform Naming Convention path (which begins \\) requires 8 backslashes \\\\\\\\ due to 2 backslashes each being double-escaped.
LTS appears in many programming languages and in many situations, including in patterns that match Uniform Resource Identifiers (URIs) and in programs that output quoted text. Many quines fall into the latter category.

Pattern example
Consider the following Perl regular expression intended to match URIs that identify files under the pub directory of an FTP site:

Perl, like sed before it, solves this problem by allowing many other characters to be delimiters for a regular expression. For example, the following three examples are equivalent to the expression given above:

m{ftp://[^/]*/pub/}
m#ftp://[^/]*/pub/#
m!ftp://[^/]*/pub/!

Or this common translation to convert backslashes to forward slashes:

may be easier to understand when written like this:

Quoted-text example
A Perl program to print an HTML link tag, where the URL and link text are stored in variables $url and $text respectively, might look like this. Notice the use of backslashes to escape the quoted double-quote characters:

Using single quotes to delimit the string is not feasible, as Perl does not expand variables inside single-quoted strings.  The code below, for example, would not work as intended:

Using the printf function is a viable solution in many languages (Perl, C, PHP):

The qq operator in Perl allows for any delimiter:

Here documents are especially well suited for multi-line strings; however, Perl here documents hadn't allowed for proper indentation before v5.26. This example shows the Perl syntax:

Other languages
C#
The C# programming language handles LTS by the use of the @ symbol at the start of string literals, before the initial quotation marks, e.g.

rather than otherwise requiring:

C++
The C++11 standard adds raw strings:

If the string contains the characters )", an optional delimiter can be used, such as d in the following example:

Go
Go indicates that a string is raw by using the backtick as a delimiter:

Raw strings may contain any character except backticks; there is no escape code for a backtick in a raw string. Raw strings may also span multiple lines, as in this example, where the strings s and t are equivalent:

Python
Python has a similar construct using r:

One can also use them together with triple quotes:

R
R has a similar construct using r or R with various bracket deliminators ((, [, {):

For raw strings that contain ( instances

For additional flexibility, a number of dashes can be placed between the opening quote and the opening delimiter, as long as the same number of dashes appear between the closing delimiter and the closing quote.

Ruby
Ruby uses single quote to indicate raw string:

It also has regex percent literals with choice of delimiter like Perl:

Rust
Rust uses a variant of the r prefix:

The literal starts with r followed by any number of #, followed by one ". Further " contained in the literal are considered part of the literal, unless followed by at least as many # as used after the opening r. As such, a string literal opened with r#" cannot have "# in its content.

Scala
Scala allows usage of triple quotes in order to prevent escaping confusion:

The triple quotes also allow for multiline strings, as shown here:

Sed
Sed regular expressions, particularly those using the "s" operator, are much similar to Perl (sed is a predecessor to Perl).  The default delimiter is "/", but any delimiter can be used; the default is s/regexp/replacement/, but s:regexp:replacement: is also a valid form. For example, to match a "pub" directory (as in the Perl example) and replace it with "foo", the default (escaping the slashes) is

Using an exclamation point ("!") as delimiter instead yields

See also
Magic quotes
String literal


== References ==

## Archive Info
- **Archived on:** 2024-12-15 20:38:23 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 4897 bytes
- **Word Count:** 797 words
