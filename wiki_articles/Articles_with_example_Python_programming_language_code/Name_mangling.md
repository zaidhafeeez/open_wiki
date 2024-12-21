---
title: Name mangling
url: https://en.wikipedia.org/wiki/Name_mangling
language: en
categories: ["Category:All articles needing additional references", "Category:All articles that may contain original research", "Category:All articles to be expanded", "Category:All articles with style issues", "Category:Articles needing additional references from December 2011", "Category:Articles that may contain original research from September 2016", "Category:Articles to be expanded from June 2014", "Category:Articles with example C++ code", "Category:Articles with example C code", "Category:Articles with example Java code", "Category:Articles with example Python (programming language) code", "Category:Articles with multiple maintenance issues", "Category:Articles with short description", "Category:C++", "Category:CS1 maint: numeric names: authors list", "Category:Compiler construction", "Category:Computer libraries", "Category:Java (programming language)", "Category:Short description is different from Wikidata", "Category:Wikipedia articles with style issues from September 2016"]
references: 0
last_modified: 2024-12-21T15:02:28Z
---

# Name mangling

## Summary

In compiler construction, name mangling (also called name decoration) is a technique used to solve various problems caused by the need to resolve unique names for programming entities in many modern programming languages.
It provides means to encode added information in the name of a function, structure, class or another data type, to pass more semantic information from the compiler to the linker.
The need for name mangling arises where a language allows different entities to be named with the s

## Full Content

In compiler construction, name mangling (also called name decoration) is a technique used to solve various problems caused by the need to resolve unique names for programming entities in many modern programming languages.
It provides means to encode added information in the name of a function, structure, class or another data type, to pass more semantic information from the compiler to the linker.
The need for name mangling arises where a language allows different entities to be named with the same identifier as long as they occupy a different namespace (typically defined by a module, class, or explicit namespace directive) or have different type signatures (such as in function overloading). It is required in these uses because each signature might require different, specialized calling convention in the machine code.
Any object code produced by compilers is usually linked with other pieces of object code (produced by the same or another compiler) by a type of program called a linker. The linker needs a great deal of information on each program entity. For example, to correctly link a function it needs its name, the number of arguments and their types, and so on.
The simple programming languages of the 1970s, like C, only distinguished subroutines by their name, ignoring other information including parameter and return types.
Later languages, like C++, defined stricter requirements for routines to be considered "equal", such as the parameter types, return type, and calling convention of a function. These requirements enable method overloading and detection of some bugs (such as using different definitions of a function when compiling different source code files).
These stricter requirements needed to work with extant programming tools and conventions. Thus, added requirements were encoded in the name of the symbol, since that was the only information a traditional linker had about a symbol.

Examples
C
Although name mangling is not generally required or used by languages that do not support function overloading, like C and classic Pascal, they use it in some cases to provide added information about a function.
For example, compilers targeted at Microsoft Windows platforms support a variety of calling conventions, which determine the manner in which parameters are sent to subroutines and results are returned. Because the different calling conventions are incompatible with one another, compilers mangle symbols with codes detailing which convention should be used to call the specific routine.
The mangling scheme for Windows was established by Microsoft and has been informally followed by other compilers including Digital Mars, Borland, and GNU Compiler Collection (GCC) when compiling code for the Windows platforms. The scheme even applies to other languages, such as Pascal, D, Delphi, Fortran, and C#. This allows subroutines written in those languages to call, or be called by, extant Windows libraries using a calling convention different from their default.
When compiling the following C examples:

32-bit compilers emit, respectively:

_f
_g@4
@h@4

In the stdcall and fastcall mangling schemes, the function is encoded as _name@X and @name@X respectively, where X is the number of bytes, in decimal, of the argument(s) in the parameter list (including those passed in registers, for fastcall). In the case of cdecl, the function name is merely prefixed by an underscore.
The 64-bit convention on Windows (Microsoft C) has no leading underscore. This difference may in some rare cases lead to unresolved externals when porting such code to 64 bits. For example, Fortran code can use 'alias' to link against a C method by name as follows:

This will compile and link fine under 32 bits, but generate an unresolved external _f under 64 bits. One workaround for this is not to use 'alias' at all (in which the method names typically need to be capitalized in C and Fortran). Another is to use the BIND option:

In C, most compilers also mangle static functions and variables (and in C++ functions and variables declared static or put in the anonymous namespace) in translation units using the same mangling rules as for their non-static versions. If functions with the same name (and parameters for C++) are also defined and used in different translation units, it will also mangle to the same name, potentially leading to a clash. However, they will not be equivalent if they are called in their respective translation units. Compilers are usually free to emit arbitrary mangling for these functions, because it is illegal to access these from other translation units directly, so they will never need linking between different object code (linking of them is never needed). To prevent linking conflicts, compilers will use standard mangling, but will use so-called 'local' symbols. When linking many such translation units there might be multiple definitions of a function with the same name, but resulting code will only call one or another depending on which translation unit it came from. This is usually done using the relocation mechanism.

C++
C++ compilers are the most widespread users of name mangling. The first C++ compilers were implemented as translators to C source code, which would then be compiled by a C compiler to object code; because of this, symbol names had to conform to C identifier rules. Even later, with the emergence of compilers that produced machine code or assembly directly, the system's linker generally did not support C++ symbols, and mangling was still required.
The C++ language does not define a standard decoration scheme, so each compiler uses its own. C++ also has complex language features, such as classes, templates, namespaces, and operator overloading, that alter the meaning of specific symbols based on context or usage. Meta-data about these features can be disambiguated by mangling (decorating) the name of a symbol. Because the name-mangling systems for such features are not standardized across compilers, few linkers can link object code that was produced by different compilers.

Simple example
A single C++ translation unit might define two functions named f():

These are distinct functions, with no relation to each other apart from the name. The C++ compiler will therefore encode the type information in the symbol name, the result being something resembling:

Even though its name is unique, g() is still mangled: name mangling applies to all C++ symbols (except for those in an extern "C"{} block).

Complex example
The mangled symbols in this example, in the comments below the respective identifier name, are those produced by the GNU GCC 3.x compilers, according to the IA-64 (Itanium) ABI:

All mangled symbols begin with _Z (note that an identifier beginning with an underscore followed by a capital letter is a reserved identifier in C, so conflict with user identifiers is avoided); for nested names (including both namespaces and classes), this is followed by N, then a series of <length, id> pairs (the length being the length of the next identifier), and finally E. For example, wikipedia::article::format becomes:

_ZN9wikipedia7article6formatE

For functions, this is then followed by the type information; as format() is a void function, this is simply v; hence:

_ZN9wikipedia7article6formatEv

For print_to, the standard type std::ostream (which is a typedef for std::basic_ostream<char, std::char_traits<char> >) is used, which has the special alias So; a reference to this type is therefore RSo, with the complete name for the function being:

_ZN9wikipedia7article8print_toERSo

How different compilers mangle the same functions
There isn't a standardized scheme by which even trivial C++ identifiers are mangled, and consequently different compilers (or even different versions of the same compiler, or the same compiler on different platforms) mangle public symbols in radically different (and thus totally incompatible) ways. Consider how different C++ compilers mangle the same functions:

Notes:

The Compaq C++ compiler on OpenVMS VAX and Alpha (but not IA-64) and Tru64 UNIX has two name mangling schemes. The original, pre-standard scheme is known as the ARM model, and is based on the name mangling described in the C++ Annotated Reference Manual (ARM). With the advent of new features in standard C++, particularly templates, the ARM scheme became more and more unsuitable – it could not encode certain function types, or produced identically mangled names for different functions. It was therefore replaced by the newer American National Standards Institute (ANSI) model, which supported all ANSI template features, but was not backward compatible.
On IA-64, a standard application binary interface (ABI) exists (see external links), which defines (among other things) a standard name-mangling scheme, and which is used by all the IA-64 compilers. GNU GCC 3.x has further adopted the name mangling scheme defined in this standard for use on other, non-Intel platforms.
The Visual Studio and Windows SDK include the program undname which prints the C-style function prototype for a given mangled name.
On Microsoft Windows, the Intel compiler and Clang uses the Visual C++ name mangling for compatibility.

Handling of C symbols when linking from C++
The job of the common C++ idiom:

is to ensure that the symbols within are "unmangled" – that the compiler emits a binary file with their names undecorated, as a C compiler would do. As C language definitions are unmangled, the C++ compiler needs to avoid mangling references to these identifiers.
For example, the standard strings library, <string.h>, usually contains something resembling:

Thus, code such as:

uses the correct, unmangled strcmp and memset. If the extern "C" had not been used, the (SunPro) C++ compiler would produce code equivalent to:

Since those symbols do not exist in the C runtime library (e.g. libc), link errors would result.

Standardized name mangling in C++
It would seem that standardized name mangling in the C++ language would lead to greater interoperability between compiler implementations. However, such a standardization by itself would not suffice to guarantee C++ compiler interoperability and it might even create a false impression that interoperability is possible and safe when it isn't. Name mangling is only one of several application binary interface (ABI) details that need to be decided and observed by a C++ implementation. Other ABI aspects like exception handling, virtual table layout, structure, and stack frame padding also cause differing C++ implementations to be incompatible. Further, requiring a particular form of mangling would cause issues for systems where implementation limits (e.g., length of symbols) dictate a particular mangling scheme. A standardized requirement for name mangling would also prevent an implementation where mangling was not required at all – for example, a linker that understood the C++ language.
The C++ standard therefore does not attempt to standardize name mangling. On the contrary, the Annotated C++ Reference Manual (also known as ARM, ISBN 0-201-51459-1, section 7.2.1c) actively encourages the use of different mangling schemes to prevent linking when other aspects of the ABI are incompatible.
Nevertheless, as detailed in the section above, on some platforms the full C++ ABI has been standardized, including name mangling.

Real-world effects of C++ name mangling
Because C++ symbols are routinely exported from DLL and shared object files, the name mangling scheme is not merely a compiler-internal matter. Different compilers (or different versions of the same compiler, in many cases) produce such binaries under different name decoration schemes, meaning that symbols are frequently unresolved if the compilers used to create the library and the program using it employed different schemes. For example, if a system with multiple C++ compilers installed (e.g., GNU GCC and the OS vendor's compiler) wished to install the Boost C++ Libraries, it would have to be compiled multiple times (once for GCC and once for the vendor compiler).
It is good for safety purposes that compilers producing incompatible object codes (codes based on different ABIs, regarding e.g., classes and exceptions) use different name mangling schemes. This guarantees that these incompatibilities are detected at the linking phase, not when executing the software (which could lead to obscure bugs and serious stability issues).
For this reason, name decoration is an important aspect of any C++-related ABI.
There are instances, particularly in large, complex code bases, where it can be difficult or impractical to map the mangled name emitted within a linker error message back to the particular corresponding token/variable-name in the source. This problem can make identifying the relevant source file(s) very difficult for build or test engineers even if only one compiler and linker are in use. Demanglers (including those within the linker error reporting mechanisms) sometimes help but the mangling mechanism itself may discard critical disambiguating information.

Demangle via c++filt
Demangle via builtin GCC ABI
Output: 

Demangled: Map<StringName, Ref<GDScript>, Comparator<StringName>, DefaultAllocator>::has(StringName const&) const

Java
In Java, the signature of a method or a class contains its name and the types of its method arguments and return value, where applicable. The format of signatures is documented, as the language, compiler, and .class file format were all designed together (and had object-orientation and universal interoperability in mind from the start).

Creating unique names for inner and anonymous classes
The scope of anonymous classes is confined to their parent class, so the compiler must produce a "qualified" public name for the inner class, to avoid conflict where other classes with the same name (inner or not) exist in the same namespace. Similarly, anonymous classes must have "fake" public names generated for them (as the concept of anonymous classes only exists in the compiler, not the runtime). So, compiling the following Java program:

will produce three .class files:

foo.class, containing the main (outer) class foo
foo$bar.class, containing the named inner class foo.bar
foo$1.class, containing the anonymous inner class (local to method foo.zark)
All of these class names are valid (as $ symbols are permitted in the JVM specification) and these names are "safe" for the compiler to generate, as the Java language definition advises not to use $ symbols in normal java class definitions.
Name resolution in Java is further complicated at runtime, as fully qualified names for classes are unique only inside a specific classloader instance. Classloaders are ordered hierarchically and each Thread in the JVM has a so-called context class loader, so in cases where two different classloader instances contain classes with the same name, the system first tries to load the class using the root (or system) classloader and then goes down the hierarchy to the context class loader.

Java Native Interface
Java Native Interface, Java's native method support, allows Java language programs to call out to programs written in another language (usually C or C++). There are two name-resolution concerns here, neither of which is implemented in a standardized manner:

JVM to native name translation - this seems to be more stable, since Oracle makes its scheme public.
Normal C++ name mangling - see above.

Python
In Python, mangling is used for class attributes that one does not want subclasses to use which are designated as such by giving them a name with two or more leading underscores and no more than one trailing underscore. For example, __thing will be mangled, as will ___thing and __thing_, but __thing__ and __thing___ will not. Python's runtime does not restrict access to such attributes, the mangling only prevents name collisions if a derived class defines an attribute with the same name.
On encountering name mangled attributes, Python transforms these names by prepending a single underscore and the name of the enclosing class, for example:

Pascal
Turbo Pascal, Delphi
To avoid name mangling in Pascal, use:

Free Pascal
Free Pascal supports function and operator overloading, thus it also uses name mangling to support these features. On the other hand, Free Pascal is capable of calling symbols defined in external modules created with another language and exporting its own symbols to be called by another language. For further information, consult Chapter 6.2 and 7.1 of Free Pascal Programmer's Guide.

Fortran
Name mangling is also necessary in Fortran compilers, originally because the language is case insensitive. Further mangling requirements were imposed later in the evolution of the language because of the addition of modules and other features in the Fortran 90 standard. The case mangling, especially, is a common issue that must be dealt with to call Fortran libraries, such as LAPACK, from other languages, such as C.
Because of the case insensitivity, the name of a subroutine or function FOO must be converted to a standardized case and format by the compiler so that it will be linked in the same way regardless of case. Different compilers have implemented this in various ways, and no standardization has occurred. The AIX and HP-UX Fortran compilers convert all identifiers to lower case foo, while the Cray and Unicos Fortran compilers converted identifiers to all upper case FOO. The GNU g77 compiler converts identifiers to lower case plus an underscore foo_, except that identifiers already containing an underscore FOO_BAR have two underscores appended foo_bar__, following a convention established by f2c. Many other compilers, including Silicon Graphics's (SGI) IRIX compilers, GNU Fortran, and Intel's Fortran compiler (except on Microsoft Windows), convert all identifiers to lower case plus an underscore (foo_ and foo_bar_, respectively). On Microsoft Windows, the Intel Fortran compiler defaults to uppercase without an underscore.
Identifiers in Fortran 90 modules must be further mangled, because the same procedure name may occur in different modules. Since the Fortran 2003 Standard requires that module procedure names not conflict with other external symbols, compilers tend to use the module name and the procedure name, with a distinct marker in between. For example:

In this module, the name of the function will be mangled as __m_MOD_five (e.g., GNU Fortran), m_MP_five_ (e.g., Intel's ifort), m.five_ (e.g., Oracle's sun95), etc. Since Fortran does not allow overloading the name of a procedure, but uses generic interface blocks and generic type-bound procedures instead, the mangled names do not need to incorporate clues about the arguments.
The Fortran 2003 BIND option overrides any name mangling done by the compiler, as shown above.

Rust
Function names are mangled by default in Rust. However, this can be disabled by the #[no_mangle] function attribute. This attribute can be used to export functions to C, C++, or Objective-C. Further, along with the #[start] function attribute or the #[no_main] crate attribute, it allows the user to define a C-style entry point for the program.
Rust has used many versions of symbol mangling schemes that can be selected at compile time with an -Z symbol-mangling-version option. The following manglers are defined:

legacy A C++ style mangling based on the Itanium IA-64 C++ ABI. Symbols begin with _ZN, and filename hashes are used for disambiguation. Used since Rust 1.9.
v0 An improved version of the legacy scheme, with changes for Rust. Symbols begin with _R. Polymorphism can be encoded. Functions don't have return types encoded (Rust does not have overloading). Unicode names use modified punycode. Compression (backreference) use byte-based addressing. Used since Rust 1.37.
Examples are provided in the Rust symbol-names tests.

Objective-C
Essentially two forms of method exist in Objective-C, the class ("static") method, and the instance method. A method declaration in Objective-C is of the following form:

+ (return-type) name0:parameter0 name1:parameter1 ...
– (return-type) name0:parameter0 name1:parameter1 ...

Class methods are signified by +, instance methods use -. A typical class method declaration may then look like:

With instance methods looking like this:

Each of these method declarations have a specific internal representation. When compiled, each method is named according to the following scheme for class methods:

_c_Class_name0_name1_ ...

and this for instance methods:

_i_Class_name0_name1_ ...

The colons in the Objective-C syntax are translated to underscores. So, the Objective-C class method + (id) initWithX: (int) number andY: (int) number;, if belonging to the Point class would translate as _c_Point_initWithX_andY_, and the instance method (belonging to the same class) - (id) value; would translate to _i_Point_value.
Each of the methods of a class are labeled in this way. However, to look up a method that a class may respond to would be tedious if all methods are represented in this fashion. Each of the methods is assigned a unique symbol (such as an integer). Such a symbol is known as a selector. In Objective-C, one can manage selectors directly – they have a specific type in Objective-C – SEL.
During compiling, a table is built that maps the textual representation, such as _i_Point_value, to selectors (which are given a type SEL). Managing selectors is more efficient than manipulating the text representation of a method. Note that a selector only matches a method's name, not the class it belongs to: different classes can have different implementations of a method with the same name. Because of this, implementations of a method are given a specific identifier too, these are known as implementation pointers, and are also given a type, IMP.
Message sends are encoded by the compiler as calls to the id objc_msgSend (id receiver, SEL selector, ...) function, or one of its cousins, where receiver is the receiver of the message, and SEL determines the method to call. Each class has its own table that maps selectors to their implementations – the implementation pointer specifies where in memory the implementation of the method resides. There are separate tables for class and instance methods. Apart from being stored in the SEL to IMP lookup tables, the functions are essentially anonymous.
The SEL value for a selector does not vary between classes. This enables polymorphism.
The Objective-C runtime maintains information about the argument and return types of methods. However, this information is not part of the name of the method, and can vary from class to class.
Since Objective-C does not support namespaces, there is no need for the mangling of class names (that do appear as symbols in generated binaries).

Swift
Swift keeps metadata about functions (and more) in the mangled symbols referring to them. This metadata includes the function's name, attributes, module name, parameter types, return type, and more. For example:
The mangled name for a method func calculate(x: int) -> int of a MyClass class in module test is _TFC4test7MyClass9calculatefS0_FT1xSi_Si, for 2014 Swift. The components and their meanings are as follows:

_T: The prefix for all Swift symbols. Everything will start with this.
F: Non-curried function.
C: Function of a class, i.e. a method
4test: Module name, prefixed with its length.
7MyClass: Name of class the function belongs to, prefixed with its length.
9calculate: Function name, prefixed with its length.
f: The function attribute. In this case ‘f’, which means a normal function.
S0: Designates the type of the first parameter (namely the class instance) as the first in the type stack (here MyClass is not nested and thus has index 0).
_FT: This begins the type list for the parameter tuple of the function.
1x: External name of first parameter of the function.
Si: Indicates builtin Swift type Swift.Int for the first parameter.
_Si: The return type: again Swift.Int.
Mangling for versions since Swift 4.0 is documented officially. It retains some similarity to Itanium.

See also
Application programming interface (API)
Application binary interface (ABI)
Calling convention
Comparison of application virtualization software (i.e. VMs)
Foreign function interface (FFI)
Java Native Interface (JNI)
Language binding
Stropping
SWIG

References
External links
Linux Itanium ABI for C++, including name mangling scheme.
Macintosh C/C++ ABI Standard Specification
c++filt – filter to demangle encoded C++ symbols for GNU/Intel compilers
undname – msvc tool to demangle names.
demangler.com – An online tool for demangling GCC and MSVC C++ symbols
The Objective-C Runtime System – From Apple's The Objective-C Programming Language 1.0
Calling conventions for different C++ compilers by Agner Fog contains detailed description of name mangling schemes for various x86 and x64 C++ compilers (pp. 24–42 in 2011-06-08 version)
C++ Name Mangling/Demangling Quite detailed explanation of Visual C++ compiler name mangling scheme
PHP UnDecorateSymbolName a php script that demangles Microsoft Visual C's function names.
Mixing C and C++ Code
Levine, John R. (2000) [October 1999]. "Chapter 5: Symbol management". Linkers and Loaders. The Morgan Kaufmann Series in Software Engineering and Programming (1 ed.). San Francisco, USA: Morgan Kaufmann. ISBN 1-55860-496-0. OCLC 42413382. Archived from the original on 2012-12-05. Retrieved 2020-01-12. Code: [1][2] Errata: [3]
Name mangling demystified by Fivos Kefallonitis
