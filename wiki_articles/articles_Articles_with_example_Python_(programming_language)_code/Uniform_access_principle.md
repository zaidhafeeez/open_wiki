# Uniform access principle

## Article Metadata

- **Last Updated:** 2024-12-14T19:46:39.465272+00:00
- **Original Article:** [Uniform access principle](https://en.wikipedia.org/wiki/Uniform_access_principle)
- **Language:** en
- **Page ID:** 2278914

## Summary

The uniform access principle of computer programming was put forth by Bertrand Meyer (originally in his book Object-Oriented Software Construction). It states "All services offered by a module should be available through a uniform notation, which does not betray whether they are implemented through storage or through computation." This principle applies generally to the syntax of object-oriented programming languages. In simpler form, it states that there should be no syntactical difference betw

## Categories

- Category:All Wikipedia articles written in American English
- Category:All articles needing additional references
- Category:Articles needing additional references from January 2010
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Programming paradigms
- Category:Programming principles
- Category:Short description matches Wikidata
- Category:Software design
- Category:Use American English from March 2019

## Table of Contents

- Explanation
- UAP example
- Problems
- Language examples

## Content

The uniform access principle of computer programming was put forth by Bertrand Meyer (originally in his book Object-Oriented Software Construction). It states "All services offered by a module should be available through a uniform notation, which does not betray whether they are implemented through storage or through computation." This principle applies generally to the syntax of object-oriented programming languages. In simpler form, it states that there should be no syntactical difference between working with an attribute, pre-computed property, or method/query of an object.
While most examples focus on the "read" aspect of the principle (i.e., retrieving a value), Meyer shows that the "write" implications (i.e., modifying a value) of the principle are harder to deal with in his monthly column on the Eiffel programming language official website.

Explanation
The problem being addressed by Meyer involves the maintenance of large software projects or software libraries. Sometimes when developing or maintaining software it is necessary, after much code is in place, to change a class or object in a way that transforms what was simply an attribute access into a method call.  Programming languages often use different syntax for attribute access and invoking a method, (e.g., object.something versus object.something()). The syntax change would require, in popular programming languages of the day, changing the source code in all the places where the attribute was used.  This might require changing source code in many different locations throughout a very large volume of source code. Or worse, if the change is in an object library used by hundreds of customers, each of those customers would have to find and change all the places the attribute was used in their own code and recompile their programs.
Going the reverse way (from method to simple attribute) really was not a problem, as one can always just keep the function and have it simply return the attribute value.
Meyer recognized the need for software developers to write code in such a way as to minimize or eliminate cascading changes in code that result from changes which convert an object attribute to a method call or vice versa. For this he developed the Uniform Access Principle.
Many programming languages do not strictly support the UAP but do support forms of it.  Properties, which are provided in a number of programming languages, address the problem Meyer was addressing with his UAP in a different way. Instead of providing a single uniform notation, properties provide a way to invoke a method of an object while using the same notation as is used for attribute access.  The separate method invocation syntax is still available.

UAP example
If the language uses the method invocation syntax it may look something like this.

// Assume print displays the variable passed to it, with or without parens
// Set Foo's attribute 'bar' to  value 5.
Foo.bar(5)
print Foo.bar()

When executed, should display :

5

Whether or not Foo.bar(5) invokes a function or simply sets an attribute is hidden from the caller.
Likewise whether Foo.bar() simply retrieves the value of the attribute, or invokes a function
to compute the value returned, is an implementation detail hidden from the caller.
If the language uses the attribute syntax the syntax may look like this.

Foo.bar = 5
print Foo.bar

Again, whether or not a method is invoked, or the value is simply assigned to an attribute is hidden
from the calling method.

Problems
However, UAP itself can lead to problems, if used in places where the differences between access methods are not negligible, such as when the returned value is expensive to compute or will trigger cache operations.

Language examples
Python
Python properties may be used to allow a method
to be invoked with the same syntax as accessing an attribute.  Whereas Meyer's UAP would have
a single notation for both attribute access and method invocation (method invocation syntax), 
a language with support for properties still supports separate notations for attribute
and method access.  Properties allow the attribute notation to be used, but to hide the
fact that a method is being invoked instead of simply retrieving or setting a value. 
As such, Python leaves the option of adherence to UAP up to the individual programmer. The built-in @property function provides a simple way to decorate any given method in attribute access syntax, thus abstracting away the syntactical difference between method invocations and attribute accesses.
In Python, we may have code that access an Egg object that could be defined such that weight and color are simple attributes as in the following 

Or the Egg object could use properties, and invoke getter and setter methods instead

Regardless of which way Egg is defined, the calling code can remain the same.  The implementation of Egg can switch from one form to the other without affecting code that uses the Egg class. Languages which implement the UAP have this property as well.

Ruby
Consider the following

Now the Egg class could be defined as follows

The above initial code segment would work fine with the Egg being defined as such. The Egg
class could also be defined as below, where color is instead a method. The calling code would
still work, unchanged if Egg were to be defined as follows.

Note how even though color looks like an attribute in one case and a pair of methods
in the next, the interface to the class remains the same.  The person maintaining the Egg class can switch from one form to the other without fear of breaking any caller's code.
Ruby follows the revised UAP, the attr_accessor :color only acts as syntactic sugar for generating accessor/setter methods for color. There is no way in Ruby to retrieve an instance variable from an object without calling a method on it.
Strictly speaking, Ruby does not follow Meyer's original UAP in that the syntax for accessing an attribute is different from the syntax for invoking a method.  But here, the access for an attribute will always actually be through a function which is often automatically generated. So in essence, either type of access invokes a function and the language does follow Meyer's revised Uniform Access Principle.

C#
The C# language supports class properties, which provide a means to define get and set operations (getters and setters) for a member variable. The syntax to access or modify the property is the same as accessing any other class member variable, but the actual implementation for doing so can be defined as either a simple read/write access or as functional code.

In the example above, class Foo contains two properties, Size and Name. The Size property is an integer that can be read (get) and written (set). Similarly, the Name property is a string that can also be read and modified, but its value is stored in a separate (private) class variable _name.
Omitting the set operation in a property definition makes the property read-only, while omitting the get operation makes it write-only.
Use of the properties employs the UAP, as shown in the code below.

C++
C++ has neither the UAP nor properties, when an object is changed such that an attribute (color) becomes a pair of functions (getA, setA). Any place in that uses an instance of the object and either sets or gets the attribute value (x = obj.color or obj.color = x) must be changed to invoke one of the functions. (x = obj.getColor() or obj.setColor(x)). Using templates and operator overloading, it is possible to fake properties, but this is more complex than in languages which directly support properties. This complicates maintenance of C++ programs. Distributed libraries of C++ objects must be careful about how they provide access to member data.

JavaScript
JavaScript has had support for computed properties since 2009.


== References ==

## Related Articles

### Internal Links

- [ACM Computing Classification System](https://en.wikipedia.org/wiki/ACM_Computing_Classification_System)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Algorithm](https://en.wikipedia.org/wiki/Algorithm)
- [Algorithmic efficiency](https://en.wikipedia.org/wiki/Algorithmic_efficiency)
- [Analysis of algorithms](https://en.wikipedia.org/wiki/Analysis_of_algorithms)
- [Application security](https://en.wikipedia.org/wiki/Application_security)
- [Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
- [Attribute (computing)](https://en.wikipedia.org/wiki/Attribute_(computing))
- [Automata theory](https://en.wikipedia.org/wiki/Automata_theory)
- [Automated planning and scheduling](https://en.wikipedia.org/wiki/Automated_planning_and_scheduling)
- [Bertrand Meyer](https://en.wikipedia.org/wiki/Bertrand_Meyer)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C Sharp (programming language)](https://en.wikipedia.org/wiki/C_Sharp_(programming_language))
- [Closure (computer programming)](https://en.wikipedia.org/wiki/Closure_(computer_programming))
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Computability theory](https://en.wikipedia.org/wiki/Computability_theory)
- [Computational biology](https://en.wikipedia.org/wiki/Computational_biology)
- [Computational chemistry](https://en.wikipedia.org/wiki/Computational_chemistry)
- [Computational complexity](https://en.wikipedia.org/wiki/Computational_complexity)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Computational engineering](https://en.wikipedia.org/wiki/Computational_engineering)
- [Computational geometry](https://en.wikipedia.org/wiki/Computational_geometry)
- [Computational mathematics](https://en.wikipedia.org/wiki/Computational_mathematics)
- [Computational physics](https://en.wikipedia.org/wiki/Computational_physics)
- [Computational social science](https://en.wikipedia.org/wiki/Computational_social_science)
- [Computer accessibility](https://en.wikipedia.org/wiki/Computer_accessibility)
- [Computer animation](https://en.wikipedia.org/wiki/Computer_animation)
- [Computer architecture](https://en.wikipedia.org/wiki/Computer_architecture)
- [Computer data storage](https://en.wikipedia.org/wiki/Computer_data_storage)
- [Computer graphics](https://en.wikipedia.org/wiki/Computer_graphics)
- [Computer hardware](https://en.wikipedia.org/wiki/Computer_hardware)
- [Computer network](https://en.wikipedia.org/wiki/Computer_network)
- [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
- [Computer science](https://en.wikipedia.org/wiki/Computer_science)
- [Computer security](https://en.wikipedia.org/wiki/Computer_security)
- [Computer vision](https://en.wikipedia.org/wiki/Computer_vision)
- [Computing](https://en.wikipedia.org/wiki/Computing)
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Concurrency (computer science)](https://en.wikipedia.org/wiki/Concurrency_(computer_science))
- [Concurrent computing](https://en.wikipedia.org/wiki/Concurrent_computing)
- [Control theory](https://en.wikipedia.org/wiki/Control_theory)
- [Control flow](https://en.wikipedia.org/wiki/Control_flow)
- [Cross-validation (statistics)](https://en.wikipedia.org/wiki/Cross-validation_(statistics))
- [Cryptography](https://en.wikipedia.org/wiki/Cryptography)
- [Cyberwarfare](https://en.wikipedia.org/wiki/Cyberwarfare)
- [Data mining](https://en.wikipedia.org/wiki/Data_mining)
- [Database](https://en.wikipedia.org/wiki/Database)
- [Decision support system](https://en.wikipedia.org/wiki/Decision_support_system)
- [Dependability](https://en.wikipedia.org/wiki/Dependability)
- [Digital art](https://en.wikipedia.org/wiki/Digital_art)
- [Digital library](https://en.wikipedia.org/wiki/Digital_library)
- [Digital marketing](https://en.wikipedia.org/wiki/Digital_marketing)
- [Discrete mathematics](https://en.wikipedia.org/wiki/Discrete_mathematics)
- [Distributed artificial intelligence](https://en.wikipedia.org/wiki/Distributed_artificial_intelligence)
- [Distributed computing](https://en.wikipedia.org/wiki/Distributed_computing)
- [Document management system](https://en.wikipedia.org/wiki/Document_management_system)
- [Domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
- [E-commerce](https://en.wikipedia.org/wiki/E-commerce)
- [Educational technology](https://en.wikipedia.org/wiki/Educational_technology)
- [Eiffel (programming language)](https://en.wikipedia.org/wiki/Eiffel_(programming_language))
- [Electronic design automation](https://en.wikipedia.org/wiki/Electronic_design_automation)
- [Electronic publishing](https://en.wikipedia.org/wiki/Electronic_publishing)
- [Electronic voting](https://en.wikipedia.org/wiki/Electronic_voting)
- [Embedded system](https://en.wikipedia.org/wiki/Embedded_system)
- [Enterprise information system](https://en.wikipedia.org/wiki/Enterprise_information_system)
- [Enterprise software](https://en.wikipedia.org/wiki/Enterprise_software)
- [Form factor (design)](https://en.wikipedia.org/wiki/Form_factor_(design))
- [Formal language](https://en.wikipedia.org/wiki/Formal_language)
- [Formal methods](https://en.wikipedia.org/wiki/Formal_methods)
- [Geographic information system](https://en.wikipedia.org/wiki/Geographic_information_system)
- [Graphics processing unit](https://en.wikipedia.org/wiki/Graphics_processing_unit)
- [Green computing](https://en.wikipedia.org/wiki/Green_computing)
- [Hardware acceleration](https://en.wikipedia.org/wiki/Hardware_acceleration)
- [Hardware security](https://en.wikipedia.org/wiki/Hardware_security)
- [Health informatics](https://en.wikipedia.org/wiki/Health_informatics)
- [Human–computer interaction](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Image compression](https://en.wikipedia.org/wiki/Image_compression)
- [Information retrieval](https://en.wikipedia.org/wiki/Information_retrieval)
- [Information security](https://en.wikipedia.org/wiki/Information_security)
- [Information system](https://en.wikipedia.org/wiki/Information_system)
- [Information theory](https://en.wikipedia.org/wiki/Information_theory)
- [Integrated circuit](https://en.wikipedia.org/wiki/Integrated_circuit)
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [Interaction design](https://en.wikipedia.org/wiki/Interaction_design)
- [Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
- [Intrusion detection system](https://en.wikipedia.org/wiki/Intrusion_detection_system)
- [Knowledge representation and reasoning](https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning)
- [Library (computing)](https://en.wikipedia.org/wiki/Library_(computing))
- [List of computer size categories](https://en.wikipedia.org/wiki/List_of_computer_size_categories)
- [Logic in computer science](https://en.wikipedia.org/wiki/Logic_in_computer_science)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Mathematical analysis](https://en.wikipedia.org/wiki/Mathematical_analysis)
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Mathematical software](https://en.wikipedia.org/wiki/Mathematical_software)
- [Method (computer programming)](https://en.wikipedia.org/wiki/Method_(computer_programming))
- [Middleware](https://en.wikipedia.org/wiki/Middleware)
- [Mixed reality](https://en.wikipedia.org/wiki/Mixed_reality)
- [Model of computation](https://en.wikipedia.org/wiki/Model_of_computation)
- [Modeling language](https://en.wikipedia.org/wiki/Modeling_language)
- [Modular programming](https://en.wikipedia.org/wiki/Modular_programming)
- [Multi-task learning](https://en.wikipedia.org/wiki/Multi-task_learning)
- [Multimedia database](https://en.wikipedia.org/wiki/Multimedia_database)
- [Multiprocessing](https://en.wikipedia.org/wiki/Multiprocessing)
- [Multithreading (computer architecture)](https://en.wikipedia.org/wiki/Multithreading_(computer_architecture))
- [Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Network architecture](https://en.wikipedia.org/wiki/Network_architecture)
- [Network performance](https://en.wikipedia.org/wiki/Network_performance)
- [Communication protocol](https://en.wikipedia.org/wiki/Communication_protocol)
- [Network scheduler](https://en.wikipedia.org/wiki/Network_scheduler)
- [Network security](https://en.wikipedia.org/wiki/Network_security)
- [Network service](https://en.wikipedia.org/wiki/Network_service)
- [Networking hardware](https://en.wikipedia.org/wiki/Networking_hardware)
- [Numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis)
- [Object-Oriented Software Construction](https://en.wikipedia.org/wiki/Object-Oriented_Software_Construction)
- [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Operations research](https://en.wikipedia.org/wiki/Operations_research)
- [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)
- [Outline of computer science](https://en.wikipedia.org/wiki/Outline_of_computer_science)
- [Parallel computing](https://en.wikipedia.org/wiki/Parallel_computing)
- [Peripheral](https://en.wikipedia.org/wiki/Peripheral)
- [Philosophy of artificial intelligence](https://en.wikipedia.org/wiki/Philosophy_of_artificial_intelligence)
- [Photograph manipulation](https://en.wikipedia.org/wiki/Photograph_manipulation)
- [Printed circuit board](https://en.wikipedia.org/wiki/Printed_circuit_board)
- [Probability](https://en.wikipedia.org/wiki/Probability)
- [Industrial process control](https://en.wikipedia.org/wiki/Industrial_process_control)
- [Processor (computing)](https://en.wikipedia.org/wiki/Processor_(computing))
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming language theory](https://en.wikipedia.org/wiki/Programming_language_theory)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- [Programming team](https://en.wikipedia.org/wiki/Programming_team)
- [Programming tool](https://en.wikipedia.org/wiki/Programming_tool)
- [Property (programming)](https://en.wikipedia.org/wiki/Property_(programming))
- [Python syntax and semantics](https://en.wikipedia.org/wiki/Python_syntax_and_semantics)
- [Quantum computing](https://en.wikipedia.org/wiki/Quantum_computing)
- [Randomized algorithm](https://en.wikipedia.org/wiki/Randomized_algorithm)
- [Real-time computing](https://en.wikipedia.org/wiki/Real-time_computing)
- [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning)
- [Rendering (computer graphics)](https://en.wikipedia.org/wiki/Rendering_(computer_graphics))
- [Requirements analysis](https://en.wikipedia.org/wiki/Requirements_analysis)
- [Security hacker](https://en.wikipedia.org/wiki/Security_hacker)
- [Security service (telecommunication)](https://en.wikipedia.org/wiki/Security_service_(telecommunication))
- [Semantics (computer science)](https://en.wikipedia.org/wiki/Semantics_(computer_science))
- [Social computing](https://en.wikipedia.org/wiki/Social_computing)
- [Social software](https://en.wikipedia.org/wiki/Social_software)
- [Software configuration management](https://en.wikipedia.org/wiki/Software_configuration_management)
- [Software construction](https://en.wikipedia.org/wiki/Software_construction)
- [Software deployment](https://en.wikipedia.org/wiki/Software_deployment)
- [Software design](https://en.wikipedia.org/wiki/Software_design)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software development process](https://en.wikipedia.org/wiki/Software_development_process)
- [Software engineering](https://en.wikipedia.org/wiki/Software_engineering)
- [Software framework](https://en.wikipedia.org/wiki/Software_framework)
- [Software maintenance](https://en.wikipedia.org/wiki/Software_maintenance)
- [Software quality](https://en.wikipedia.org/wiki/Software_quality)
- [Software repository](https://en.wikipedia.org/wiki/Software_repository)
- [Solid modeling](https://en.wikipedia.org/wiki/Solid_modeling)
- [Statistics](https://en.wikipedia.org/wiki/Statistics)
- [Stochastic computing](https://en.wikipedia.org/wiki/Stochastic_computing)
- [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning)
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
- [Syntax (programming languages)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
- [System on a chip](https://en.wikipedia.org/wiki/System_on_a_chip)
- [Theoretical computer science](https://en.wikipedia.org/wiki/Theoretical_computer_science)
- [Theory of computation](https://en.wikipedia.org/wiki/Theory_of_computation)
- [Ubiquitous computing](https://en.wikipedia.org/wiki/Ubiquitous_computing)
- [Unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning)
- [Very-large-scale integration](https://en.wikipedia.org/wiki/Very-large-scale_integration)
- [Video game](https://en.wikipedia.org/wiki/Video_game)
- [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine)
- [Virtual reality](https://en.wikipedia.org/wiki/Virtual_reality)
- [Visualization (graphics)](https://en.wikipedia.org/wiki/Visualization_(graphics))
- [Word processor](https://en.wikipedia.org/wiki/Word_processor)
- [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Computer science](https://en.wikipedia.org/wiki/Template:Computer_science)
- [Template:Differentiable computing](https://en.wikipedia.org/wiki/Template:Differentiable_computing)
- [Template:Glossaries of computers](https://en.wikipedia.org/wiki/Template:Glossaries_of_computers)
- [Template talk:Computer science](https://en.wikipedia.org/wiki/Template_talk:Computer_science)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from January 2010](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_January_2010)
- [Category:Computer science](https://en.wikipedia.org/wiki/Category:Computer_science)
- [Category:Use American English from March 2019](https://en.wikipedia.org/wiki/Category:Use_American_English_from_March_2019)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:46:39.465272+00:00_