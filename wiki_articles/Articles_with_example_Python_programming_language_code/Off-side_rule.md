---
title: Off-side rule
url: https://en.wikipedia.org/wiki/Off-side_rule
language: en
categories: ["Category:All articles needing additional references", "Category:All articles with unsourced statements", "Category:Articles needing additional references from December 2011", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Articles with unsourced statements from June 2012", "Category:Programming language topics", "Category:Short description is different from Wikidata", "Category:Use mdy dates from July 2022"]
references: 0
last_modified: 2024-12-19T13:44:55Z
---

# Off-side rule

## Summary

The off-side rule describes syntax of a computer programming language that defines the bounds of a code block via indentation.
The term was coined by Peter Landin, possibly as a pun on the offside law in association football.
An off-side rule language is contrasted with a free-form language in which indentation has no syntactic meaning, and indentation is strictly a matter of style.
An off-side rule language is also described as having significant indentation.

## Full Content

The off-side rule describes syntax of a computer programming language that defines the bounds of a code block via indentation.
The term was coined by Peter Landin, possibly as a pun on the offside law in association football.
An off-side rule language is contrasted with a free-form language in which indentation has no syntactic meaning, and indentation is strictly a matter of style.
An off-side rule language is also described as having significant indentation.

Definition
Peter Landin, in his 1966 article "The Next 700 Programming Languages", defined the off-side rule thus: "Any non-whitespace token to the left of the first such token on the previous line is taken to be the start of a new declaration."

Example
The following is an example of indentation blocks in Python; a popular off-side rule language. 
In Python, the rule is taken to define the boundaries of statements rather than declarations.

The body of the function starts on line 2 since it is indented one level (4 spaces) more than the previous line. The if clause body starts on line 3 since it is indented an additional level, and ends on line 4 since line 5 is indented a level less, a.k.a. outdented.
The colon (:) at the end of a control statement line is Python syntax; not an aspect of the off-side rule. The rule can be realized without such colon syntax.

Implementation
The off-side rule can be implemented in the lexical analysis phase, as in Python, where increasing the indenting results in the lexer outputting an INDENT token, and decreasing the indenting results in the lexer outputting a DEDENT token. These tokens correspond to the opening brace { and closing brace } in languages that use braces for blocks, and means that the phrase grammar does not depend on whether braces or indentation are used. This requires that the lexer hold state, namely the current indent level, and thus can detect changes in indentation when this changes, and thus the lexical grammar is not context-free: INDENT and DEDENT depend on the contextual information of the prior indent level.

Alternatives
The primary alternative to delimiting blocks by indenting, popularized by broad use and influence of the language C, is to ignore whitespace characters and mark blocks explicitly with curly brackets (i.e., { and }) or some other delimiter. While this allows for more formatting freedom – a developer might choose not to indent small pieces of code like the break and continue statements – sloppily indented code might lead the reader astray, such as the goto fail bug.
Lisp and other S-expression-based languages do not differentiate statements from expressions, and parentheses are enough to control the scoping of all statements within the language. As in curly bracket languages, whitespace is mostly ignored by the reader (i.e., the read function). Whitespace is used to separate tokens. The explicit structure of Lisp code allows automatic indenting, to form a visual cue for human readers.
Another alternative is for each block to begin and end with explicit keywords. For example, in ALGOL 60 and its descendant Pascal, blocks start with keyword begin and end with keyword end. In some languages (but not Pascal), this means that newlines are important (unlike in curly brace languages), but the indentation is not. In BASIC and Fortran, blocks begin with the block name (such as IF) and end with the block name prepended with END (e.g., END IF). In Fortran, each and every block can also have its own unique block name, which adds another level of explicitness to lengthy code. ALGOL 68 and the Bourne shell (sh, and bash) are similar, but the end of the block is usually given by the name of the block written backward (e.g., case starts a switch statement and it spans until the matching esac; similarly conditionals if...then...[elif...[else...]]fi or for loops for...do...od in ALGOL68 or for...do...done in bash).
An interesting variant of this occurs in Modula-2, a Pascal-like language which does away with the difference between one and multiline blocks. This allows the block opener ({ or BEGIN) to be skipped for all but the function level block, requiring only a block terminating token (} or END). It also fixes dangling else. Custom is for the end token to be placed on the same indent level as the rest of the block, giving a blockstructure that is very readable.
One advantage to the Fortran approach is that it improves readability of long, nested, or otherwise complex code. A group of outdents or closing brackets alone provides no contextual cues as to which blocks are being closed, necessitating backtracking, and closer scrutiny while debugging. Further, languages that allow a suffix for END-like keywords further improve such cues, such as continue versus continue for x, and  end-loop marker specifying the index variable NEXT I versus NEXT, and  uniquely named loops CYCLE X1 versus CYCLE. However, modern source code editors often provide visual indicators, such as syntax highlighting, and features such as code folding to assist with these drawbacks.

Productivity
In the language Scala, early versions allowed curly braces only. Scala 3 added an option to use indenting to structure blocks. Designer Martin Odersky said that this was the single most important way Scala 3 improved his own productivity, that it makes programs over 10% shorter and keeps programmers "in the flow", and advises its use.

Notable programming languages
Notable programming languages with the off-side rule:

ABC
Agda
Boo
BuddyScript
Cobra
CoffeeScript
Converge
Curry
Elm
F#, in early versions, when #light is specified; in later versions when #light "off" is not
GDScript (Godot engine)
Haskell, only for where, let, do, or case ... of clauses when braces are omitted
Inform 7
ISWIM, the abstract language that introduced the rule
LiveScript
Lobster
Miranda
MoonScript
Nemerle, optional mode
Nim
occam
PROMAL
Python
Scala, optional mode
Scheme, when using one of several Scheme Requests for Implementations, the latest of which is SRFI 119
Spin
Woma
XL

Other file formats
Notable non-programming language, text file formats with significant indentation:

GCode, RepRapFirmware dialect 
Haml
Make, tab-indented line signifies a command
Pug (formerly Jade), see Comparison of web template engines
reStructuredText
Sass
Stylus
YAML

See also
Python syntax and semantics § Indentation
Prettyprint


== References ==
