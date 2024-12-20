---
title: Programming style
url: https://en.wikipedia.org/wiki/Programming_style
language: en
categories: ["Category:All articles needing additional references", "Category:Articles needing additional references from June 2016", "Category:Articles with example C code", "Category:Articles with example Haskell code", "Category:Articles with example PHP code", "Category:Articles with example Python (programming language) code", "Category:Articles with example pseudocode", "Category:Articles with short description", "Category:Programming language comparisons", "Category:Short description is different from Wikidata", "Category:Source code"]
references: 0
last_modified: 2024-12-19T13:43:24Z
---

# Programming style

## Summary

Programming style, also known as coding style, refers to the conventions and patterns used in writing source code, resulting in a consistent and readable codebase. These conventions often encompass aspects such as indentation, naming conventions, capitalization, and comments. Consistent programming style is generally considered beneficial for code readability and maintainability, particularly in collaborative environments.
Maintaining a consistent style across a codebase can improve readability 

## Full Content

Programming style, also known as coding style, refers to the conventions and patterns used in writing source code, resulting in a consistent and readable codebase. These conventions often encompass aspects such as indentation, naming conventions, capitalization, and comments. Consistent programming style is generally considered beneficial for code readability and maintainability, particularly in collaborative environments.
Maintaining a consistent style across a codebase can improve readability and ease of software maintenance. It allows developers to quickly understand code written by others and reduces the likelihood of errors during modifications. Adhering to standardized coding guidelines ensures that teams follow a uniform approach, making the codebase easier to manage and scale. Many organizations and open-source projects adopt specific coding standards to facilitate collaboration and reduce cognitive load.
Style guidelines can be formalized in documents known as coding conventions, which dictate specific formatting and naming rules. These conventions may be prescribed by official standards for a programming language or developed internally within a team or project. For example, Python's PEP 8 is a widely recognized style guide that outlines best practices for writing Python code. In contrast, languages like C or Java may have industry standards that are either formally documented or adhered to by convention.

Automation
Adherence to coding style can be enforced through automated tools, which format code according to predefined guidelines. These tools reduce the manual effort required to maintain style consistency, allowing programmers to focus on logic and functionality. For instance, tools such as Black for Python and clang-format for C++ automatically reformat code to comply with specified coding standards.

Style guidelines
Common elements of coding style include:

Indentation and whitespace character use – Ensures consistent block structures and improves readability.
Naming conventions – Standardizes how variables, functions, and classes are named, typically adhering to camelCase, snake case, or PascalCase, depending on the language.
Capitalization – Dictates whether keywords and identifiers are capitalized or lowercase, in line with language syntax.
Comment use – Provides context and explanations within code without affecting its execution.

Indentation
Indentation style can assist a reader in various way including: identifying control flow and blocks of code. In some programming languages, indentation is used to delimit blocks of code and therefore is not matter of style. In languages that ignore whitespace, indentation can affect readability.
For example, formatted in a commonly-used style:

Arguably, poorly formatted:

Notable indenting styles
ModuLiq
The ModuLiq Zero Indentation Style groups by empty line rather than indenting.
Example:

Lua
Lua does not use the traditional curly braces or parentheses; rather, the expression in a conditional statement must be followed by then, and the block must be closed with end.

Indenting is optional in Lua. and, or, and not function as logical operators.

Python
Python relies on the off-side rule, using indenting to indicate and implement control structure, thus eliminating the need for bracketing (i.e., { and }). However, copying and pasting indented code can cause problems, because the indent level of the pasted code may not be the same as the indent level of the target line. Such reformatting by hand is tedious and error prone, but some text editors and integrated development environments (IDEs) have features to do it automatically. There are also problems when indented code is rendered unusable when posted on a forum or web page that removes whitespace, though this problem can be avoided where it is possible to enclose code in whitespace-preserving tags such as "<pre> ... </pre>" (for HTML), "[code]" ... "[/code]" (for bbcode), etc.

Python starts a block with a colon (:).
Python programmers tend to follow a commonly agreed style guide known as PEP8. There are tools designed to automate PEP8 compliance.

Haskell
Haskell, like Python, has the off-side rule. It has a two-dimension syntax where indenting is meaningful to define blocks (although, an alternate syntax uses curly braces and semicolons).
Haskell is a declarative language, there are statements, but declarations within a Haskell script.
Example:

may be written in one line as:

Haskell encourages the use of literate programming, where extended text explains the genesis of the code. In literate Haskell scripts (named with the lhs extension), everything is a comment except blocks marked as code. The program can be written in LaTeX, in such case the code environment marks what is code. Also, each active code paragraph can be marked by preceding and ending it with an empty line, and starting each line of code with a greater than sign and a space. Here an example using LaTeX markup:

And an example using plain text:

Vertical alignment
Some programmers consider it valuable to align similar elements vertically (as tabular, in columns), citing that it can make typo-generated bugs more obvious.
For example, unaligned:

aligned:

Unlike the unaligned code, the aligned code implies that the search and replace values are related since they have corresponding elements. As there is one more value for search than replacement, if this is a bug, it is more likely to be spotted via visual inspection.
Cited disadvantages of vertical alignment include:

Dependencies across lines which leads to maintenance load. For example, if a long column value is added that requires a wider column, then all lines of the table must be modified (to maintain the tabular form) which is a larger change which leads to more effort to review and to understand the change at a later date
Brittleness: if a programmer does not correctly format the table when making a change, the result is a visual mess that is harder to read than unaligned code. Simple refactoring operations, such as renaming, can break the formatting.
More effort to maintain which may discourage a programmer from making a beneficial change, such as improving the name of an identifier, because doing so would require significant formatting effort
Requirement to use a fixed-width fonts; not proportional fonts
Maintaining alignment can be alleviated by a tool that provides support (i.e. for elastic tabstops), although that creates a reliance on such tools.
As an example, simple refactoring operations to rename "$replacement" to "$r" and "$anothervalue" to "$a" results in:

With unaligned formatting, these changes do not have such a dramatic, inconsistent or undesirable effect:

Whitespace
A free-format language ignores whitespace characters: spaces, tabs and new lines so the programmer is free to style the code in different ways without affecting the meaning of the code. Generally, the programmer uses style that is considered to enhance readability.
The two code snippets below are the same logically, but differ in whitespace.

versus 

The use of tabs for whitespace is debatable. Alignment issues arise due to differing tab stops in different environments and mixed use of tabs and spaces.
As an example, one programmer prefers tab stops of four and has their toolset configured this way, and uses these to format their code.

Another programmer prefers tab stops of eight, and their toolset is configured this way. When someone else examines the original person's code, they may well find it difficult to read.

One widely used solution to this issue may involve forbidding the use of tabs for alignment or rules on how tab stops must be set. Note that tabs work fine provided they are used consistently, restricted to logical indentation, and not used for alignment:

See also
MISRA C – Software development standard for the C programming language
Naming convention (programming) – Set of rules for naming entities in source code and documentation


== References ==
