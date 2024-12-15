# IIf

## Article Metadata

- **Last Updated:** 2024-12-15T04:29:32.493899+00:00
- **Original Article:** [IIf](https://en.wikipedia.org/wiki/IIf)
- **Language:** en
- **Page ID:** 4106394

## Summary

In computing, IIf (an abbreviation for Immediate if) is a function in several editions of the Visual Basic programming language and ColdFusion Markup Language (CFML), and on spreadsheets that returns the second or third parameter based on the evaluation of the first parameter.  It is an example of a conditional expression, which is similar to a conditional statement.

## Categories

- Category:All articles with topics of unclear notability
- Category:Articles with example BASIC code
- Category:Articles with example Python (programming language) code
- Category:Articles with topics of unclear notability from February 2021
- Category:BASIC programming language
- Category:Conditional constructs
- Category:Microsoft Visual Studio

## Table of Contents

- Syntax
- Examples
- Criticisms
- Alternatives to IIf
- IIf in other programming languages
- References
- External links

## Content

In computing, IIf (an abbreviation for Immediate if) is a function in several editions of the Visual Basic programming language and ColdFusion Markup Language (CFML), and on spreadsheets that returns the second or third parameter based on the evaluation of the first parameter.  It is an example of a conditional expression, which is similar to a conditional statement.

Syntax
The syntax of the IIf function is as follows:

IIf(expr, truepart, falsepart)

All three parameters are required:

eexpr is the expression that is to be evaluated.
truepart defines what the IIf function returns if the evaluation of expr returns true.
falsepart defines what the IIf function returns if the evaluation of expr returns false.
Many languages have an operator to accomplish the same purpose, generally referred to as a conditional operator (or, less precisely, as a ternary operator); the best known is ?:, as used in C, C++, and related languages. Some of the problems with the IIf function, as discussed later, do not exist with a conditional operator, because the language is free to examine the type and delay evaluation of the operands, as opposed to simply passing them to a library function.

Examples
These examples evaluate mathematical expressions and return one of two strings depending on the outcome.

result = IIf(5 < 10, "Yes it is", "No it isn't")     ' Returns "Yes it is"

result = IIf(2 + 2 = 5, "Correct", "Wrong")          ' Returns "Wrong"

Criticisms
Efficiency
Because IIf is a library function, it will always require the overhead of a function call, whereas a conditional operator will more likely produce inline code.
Furthermore, the data type of its arguments is Variant. If the function is called with arguments of other types (variables or literals), there will be additional overhead to convert these to Variant. There may also be additional overhead to check the argument types and convert one of them if they do not have the same type.

Side effects
Another issue with IIf arises because it is a library function: unlike the C-derived conditional operator, both truepart and the falsepart will be evaluated regardless of which one is actually returned. In the following code snippet:

value = 10
result = IIf(value = 10, TrueFunction, FalseFunction)
although TrueFunction is the function intended to be called, IIf will call both TrueFunction and FalseFunction. Similarly,

While the intent may be to avoid a division by zero, whenever b is zero the error will actually happen. This is because the code in the snippet is executed as if by

This issue makes the IIf() call less useful than the conditional operator. To solve this issue, Microsoft developers had considered converting IIf to an intrinsic function; had this happened, the compiler would have been able to perform type inference and short-circuiting by replacing the function call with inline code.

Alternatives to IIf
In Visual Basic, IIf is not the sole way to evaluate and perform actions based on whether an expression is true or false.
The following example uses IIf:

result = IIf(x = y, value1, value2)

It could also be written in the following way, using standard conditionals:

The above example would also eliminate the problem of IIf evaluating both its truepart and falsepart parameters.
Visual Basic 2008 (VB 9.0) introduced a true conditional operator, called simply "If", which also eliminates this problem. Its syntax is similar to the IIf function's syntax:

IIf in other programming languages
$iif() is present in mIRC script, with similar syntax. 

alias testiif { 
  %testiif = 0
  echo -a $iif(1,$testiif2,$testiif2) %testiif execution(s)
  unset %testiif
}
alias testiif2 { inc %testiif | return testing $!iif: }

Calling /testiif will print out "testing $iif: 1 execution(s)". mIRC's $iif acts more like C's ?: than IIf() in VB since it won't pre-evaluate both.
IIF() is a function in dBase and xBase (1992 and older).
iif() is also a compiler magic function of Oxygene. It is not a real function and is at compile time unrolled to conditional statements.

In this example a new strong type string named "someString" is created (using Type inference) and the iif function will fill it depending on the outcome of the boolean expression.
SQL Server 2012 and newer implements the IIF() function (Transact-SQL):

IIf in C (and its variants) and Perl is the ?: conditional operator:

IIf in Python:

IIf (either) in Red and Rebol:

References
External links
MSDN Documentation for IIf

## Related Articles

### Internal Links

- [Ternary conditional operator](https://en.wikipedia.org/wiki/Ternary_conditional_operator)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [ColdFusion Markup Language](https://en.wikipedia.org/wiki/ColdFusion_Markup_Language)
- [Computing](https://en.wikipedia.org/wiki/Computing)
- [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
- [Conditional operator](https://en.wikipedia.org/wiki/Conditional_operator)
- [DBase](https://en.wikipedia.org/wiki/DBase)
- [Data type](https://en.wikipedia.org/wiki/Data_type)
- [Function (computer programming)](https://en.wikipedia.org/wiki/Function_(computer_programming))
- [IIF](https://en.wikipedia.org/wiki/IIF)
- [If and only if](https://en.wikipedia.org/wiki/If_and_only_if)
- [MIRC](https://en.wikipedia.org/wiki/MIRC)
- [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server)
- [Operator (computer programming)](https://en.wikipedia.org/wiki/Operator_(computer_programming))
- [Oxygene (programming language)](https://en.wikipedia.org/wiki/Oxygene_(programming_language))
- [Parameter (computer programming)](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Rebol](https://en.wikipedia.org/wiki/Rebol)
- [Red (programming language)](https://en.wikipedia.org/wiki/Red_(programming_language))
- [Short-circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation)
- [Spreadsheet](https://en.wikipedia.org/wiki/Spreadsheet)
- [Syntax (logic)](https://en.wikipedia.org/wiki/Syntax_(logic))
- [Transact-SQL](https://en.wikipedia.org/wiki/Transact-SQL)
- [Type inference](https://en.wikipedia.org/wiki/Type_inference)
- [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic)
- [Visual Basic (.NET)](https://en.wikipedia.org/wiki/Visual_Basic_(.NET))
- [XBase](https://en.wikipedia.org/wiki/XBase)
- [Wikipedia:Deletion policy](https://en.wikipedia.org/wiki/Wikipedia:Deletion_policy)
- [Wikipedia:Independent sources](https://en.wikipedia.org/wiki/Wikipedia:Independent_sources)
- [Wikipedia:Merging](https://en.wikipedia.org/wiki/Wikipedia:Merging)
- [Wikipedia:Notability](https://en.wikipedia.org/wiki/Wikipedia:Notability)
- [Wikipedia:Redirect](https://en.wikipedia.org/wiki/Wikipedia:Redirect)
- [Wikipedia:Reliable sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Category:Articles with topics of unclear notability from February 2021](https://en.wikipedia.org/wiki/Category:Articles_with_topics_of_unclear_notability_from_February_2021)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:29:32.493899+00:00_