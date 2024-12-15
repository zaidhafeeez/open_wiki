# Off-side rule

## Article Metadata

- **Last Updated:** 2024-12-15T04:40:29.187245+00:00
- **Original Article:** [Off-side rule](https://en.wikipedia.org/wiki/Off-side_rule)
- **Language:** en
- **Page ID:** 605595

## Summary

The off-side rule describes syntax of a computer programming language that defines the bounds of a code block via indentation.
The term was coined by Peter Landin, possibly as a pun on the offside law in association football.
An off-side rule language is contrasted with a free-form language in which indentation has no syntactic meaning, and indentation is strictly a matter of style.
An off-side rule language is also described as having significant indentation.

## Categories

- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles needing additional references from December 2011
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from June 2012
- Category:Programming language topics
- Category:Short description is different from Wikidata
- Category:Use mdy dates from July 2022

## Table of Contents

- Definition
- Example
- Implementation
- Alternatives
- Productivity
- Notable programming languages
- Other file formats
- See also

## Content

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

## Related Articles

### Internal Links

- [ABC (programming language)](https://en.wikipedia.org/wiki/ABC_(programming_language))
- [ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60)
- [ALGOL 68](https://en.wikipedia.org/wiki/ALGOL_68)
- [Agda (programming language)](https://en.wikipedia.org/wiki/Agda_(programming_language))
- [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- [Association football](https://en.wikipedia.org/wiki/Association_football)
- [BASIC](https://en.wikipedia.org/wiki/BASIC)
- [Bash (Unix shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
- [Block (programming)](https://en.wikipedia.org/wiki/Block_(programming))
- [Boo (programming language)](https://en.wikipedia.org/wiki/Boo_(programming_language))
- [Bourne shell](https://en.wikipedia.org/wiki/Bourne_shell)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Cobra (programming language)](https://en.wikipedia.org/wiki/Cobra_(programming_language))
- [Code folding](https://en.wikipedia.org/wiki/Code_folding)
- [CoffeeScript](https://en.wikipedia.org/wiki/CoffeeScript)
- [Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM)
- [Comparison of web template engines](https://en.wikipedia.org/wiki/Comparison_of_web_template_engines)
- [Compiled language](https://en.wikipedia.org/wiki/Compiled_language)
- [Computer](https://en.wikipedia.org/wiki/Computer)
- [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- [Context-free grammar](https://en.wikipedia.org/wiki/Context-free_grammar)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Bracket](https://en.wikipedia.org/wiki/Bracket)
- [Curry (programming language)](https://en.wikipedia.org/wiki/Curry_(programming_language))
- [Dangling else](https://en.wikipedia.org/wiki/Dangling_else)
- [Debugging](https://en.wikipedia.org/wiki/Debugging)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Elm (programming language)](https://en.wikipedia.org/wiki/Elm_(programming_language))
- [Esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language)
- [F Sharp (programming language)](https://en.wikipedia.org/wiki/F_Sharp_(programming_language))
- [Fifth-generation programming language](https://en.wikipedia.org/wiki/Fifth-generation_programming_language)
- [First-generation programming language](https://en.wikipedia.org/wiki/First-generation_programming_language)
- [For loop](https://en.wikipedia.org/wiki/For_loop)
- [Formal grammar](https://en.wikipedia.org/wiki/Formal_grammar)
- [Fortran](https://en.wikipedia.org/wiki/Fortran)
- [Fourth-generation programming language](https://en.wikipedia.org/wiki/Fourth-generation_programming_language)
- [Free-form language](https://en.wikipedia.org/wiki/Free-form_language)
- [G-code](https://en.wikipedia.org/wiki/G-code)
- [Godot (game engine)](https://en.wikipedia.org/wiki/Godot_(game_engine))
- [Unreachable code](https://en.wikipedia.org/wiki/Unreachable_code)
- [Haml](https://en.wikipedia.org/wiki/Haml)
- [Haskell](https://en.wikipedia.org/wiki/Haskell)
- [High-level programming language](https://en.wikipedia.org/wiki/High-level_programming_language)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [ISWIM](https://en.wikipedia.org/wiki/ISWIM)
- [Indentation style](https://en.wikipedia.org/wiki/Indentation_style)
- [Inform](https://en.wikipedia.org/wiki/Inform)
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
- [Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language))
- [LiveScript (programming language)](https://en.wikipedia.org/wiki/LiveScript_(programming_language))
- [Low-level programming language](https://en.wikipedia.org/wiki/Low-level_programming_language)
- [Machine code](https://en.wikipedia.org/wiki/Machine_code)
- [Make (software)](https://en.wikipedia.org/wiki/Make_(software))
- [Miranda (programming language)](https://en.wikipedia.org/wiki/Miranda_(programming_language))
- [Modula-2](https://en.wikipedia.org/wiki/Modula-2)
- [Nemerle](https://en.wikipedia.org/wiki/Nemerle)
- [Nim (programming language)](https://en.wikipedia.org/wiki/Nim_(programming_language))
- [Occam (programming language)](https://en.wikipedia.org/wiki/Occam_(programming_language))
- [Offside (association football)](https://en.wikipedia.org/wiki/Offside_(association_football))
- [Offside](https://en.wikipedia.org/wiki/Offside)
- [PROMAL](https://en.wikipedia.org/wiki/PROMAL)
- [Pascal (programming language)](https://en.wikipedia.org/wiki/Pascal_(programming_language))
- [Peter Landin](https://en.wikipedia.org/wiki/Peter_Landin)
- [Prettyprint](https://en.wikipedia.org/wiki/Prettyprint)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming language generations](https://en.wikipedia.org/wiki/Programming_language_generations)
- [Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- [Programming style](https://en.wikipedia.org/wiki/Programming_style)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python syntax and semantics](https://en.wikipedia.org/wiki/Python_syntax_and_semantics)
- [ReStructuredText](https://en.wikipedia.org/wiki/ReStructuredText)
- [Reserved word](https://en.wikipedia.org/wiki/Reserved_word)
- [S-expression](https://en.wikipedia.org/wiki/S-expression)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Sass (style sheet language)](https://en.wikipedia.org/wiki/Sass_(style_sheet_language))
- [Scala (programming language)](https://en.wikipedia.org/wiki/Scala_(programming_language))
- [Scheme (programming language)](https://en.wikipedia.org/wiki/Scheme_(programming_language))
- [Scheme Requests for Implementation](https://en.wikipedia.org/wiki/Scheme_Requests_for_Implementation)
- [Second-generation programming language](https://en.wikipedia.org/wiki/Second-generation_programming_language)
- [Source-code editor](https://en.wikipedia.org/wiki/Source-code_editor)
- [Parallax Propeller](https://en.wikipedia.org/wiki/Parallax_Propeller)
- [Stylus (style sheet language)](https://en.wikipedia.org/wiki/Stylus_(style_sheet_language))
- [Switch statement](https://en.wikipedia.org/wiki/Switch_statement)
- [Syntax (programming languages)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
- [Syntax highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting)
- [ISWIM](https://en.wikipedia.org/wiki/ISWIM)
- [Third-generation programming language](https://en.wikipedia.org/wiki/Third-generation_programming_language)
- [Very high-level programming language](https://en.wikipedia.org/wiki/Very_high-level_programming_language)
- [Whitespace character](https://en.wikipedia.org/wiki/Whitespace_character)
- [Christophe de Dinechin](https://en.wikipedia.org/wiki/Christophe_de_Dinechin)
- [YAML](https://en.wikipedia.org/wiki/YAML)
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Types of programming languages](https://en.wikipedia.org/wiki/Template:Types_of_programming_languages)
- [Template talk:Types of programming languages](https://en.wikipedia.org/wiki/Template_talk:Types_of_programming_languages)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from December 2011](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_December_2011)
- [Category:Articles with unsourced statements from June 2012](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_June_2012)
- [Category:Use mdy dates from July 2022](https://en.wikipedia.org/wiki/Category:Use_mdy_dates_from_July_2022)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:40:29.187245+00:00_