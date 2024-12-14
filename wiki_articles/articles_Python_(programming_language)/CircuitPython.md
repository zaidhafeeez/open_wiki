# CircuitPython

## Article Metadata

- **Last Updated:** 2024-12-14T19:29:02.365368+00:00
- **Original Article:** [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
- **Language:** en
- **Page ID:** 57294217

## Summary

CircuitPython is an open-source derivative of the MicroPython programming language targeted toward students and beginners. Development of CircuitPython is supported by Adafruit Industries. It is a software implementation of the Python 3 programming language, written in C. It has been ported to run on several modern microcontrollers.
CircuitPython consists of a Python compiler to bytecode and a runtime interpreter of that bytecode that runs on the microcontroller hardware. The user is presented w

## Categories

- Category:All articles lacking reliable references
- Category:All stub articles
- Category:Articles lacking reliable references from August 2019
- Category:Articles with short description
- Category:Free software programmed in C
- Category:Microcontroller software
- Category:Programming language topic stubs
- Category:Python (programming language)
- Category:Short description is different from Wikidata
- Category:Software using the MIT license

## Table of Contents

- Usage
- Community
- Hardware support
- References
- External links

## Content

CircuitPython is an open-source derivative of the MicroPython programming language targeted toward students and beginners. Development of CircuitPython is supported by Adafruit Industries. It is a software implementation of the Python 3 programming language, written in C. It has been ported to run on several modern microcontrollers.
CircuitPython consists of a Python compiler to bytecode and a runtime interpreter of that bytecode that runs on the microcontroller hardware. The user is presented with an interactive prompt (the REPL) to execute supported commands immediately. Included are a selection of core Python libraries. CircuitPython includes modules which give the programmer access to the low-level hardware of supported products as well as higher-level libraries for beginners.
CircuitPython is a fork of MicroPython, originally created by Damien George. The MicroPython community continues to discuss forks of MicroPython into variants such as CircuitPython.
CircuitPython is targeted to be compliant with CPython, the reference implementation of the Python programming language. Programs written for CircuitPython-compatible boards may not run unmodified on other platforms such as the Raspberry Pi.

Usage
CircuitPython is being used as an emerging alternative solution for microcontroller programming, which is usually done in C, C++, or assembly. The language has also seen uptake in making small, handheld video game devices. Developer Chris Young has ported his infrared transmit-and-receive software to CircuitPython to provide interactivity and to aid those with accessibility issues.

Community
The user community support includes a Discord chat room and product support forums. A Twitter account dedicated to CircuitPython news was established in 2018. A newsletter, Python on Microcontrollers, is published weekly since 15 November, 2016 by Adafruit to provide news and information on CircuitPython, MicroPython, and Python on single board computers. A Reddit subreddit, r/CircuitPython, provides news on CircuitPython and related news and projects and has about 4,300 members.

Hardware support
The version 9.1.0 supports a range of architectures, called "ports":

atmel-samd: Microchip SAMD21, SAMx5x
cxd56: Sony Spresense
espressif: Espressif ESP32, ESP32-S2, ESP32-S3, ESP32-C2, ESP32-C3, ESP32-C6
nordic: Nordic nRF52840, nRF52833
raspberrypi: Raspberry Pi RP2040, RP2350
stm: ST STM32F4 chip family
These ports are considered alpha and will have bugs and missing functionality:

broadcom: Raspberry Pi boards such as RPi 4, RPi Zero 2W (bare metal)
litex: fomu
mimxrt10xx: NXP i.MX RT10xxx
renode: hardware simulator
silabs: Silicon Labs MG24 family
stm: ST non-STM32F4 chip families
Previous versions supported the ESP8266 microcontroller, but its support was dropped in version 4.

Blinka Software Abstraction Layer
CircuitPython code may run on MicroPython or CPython using the Adafruit written Blinka compatibility layer. It acts as a translation layer between CircuitPython code and underlying code. This allows CircuitPython code to run on many more devices including a wide range of single-board computers which are listed on circuitpython.org. It is a pip installable Python library. The CircuitPython runtime is not used, as documented in the guide CircuitPython Libraries on Linux and Raspberry Pi.

Modules (Libraries)
Adafruit has fostered a community which has contributed software libraries for more than 488 sensors and drivers.

References
External links
CircuitPython on GitHub
MicroPython playlist on YouTube • Tutorials by Tony DiCola / Adafruit

## Related Articles

### Internal Links

- [Accessibility](https://en.wikipedia.org/wiki/Accessibility)
- [Adafruit Industries](https://en.wikipedia.org/wiki/Adafruit_Industries)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [Bare machine](https://en.wikipedia.org/wiki/Bare_machine)
- [CLPython](https://en.wikipedia.org/wiki/CLPython)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [Discord](https://en.wikipedia.org/wiki/Discord)
- [ESP8266](https://en.wikipedia.org/wiki/ESP8266)
- [Eric (software)](https://en.wikipedia.org/wiki/Eric_(software))
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- [Handheld game console](https://en.wikipedia.org/wiki/Handheld_game_console)
- [IDLE](https://en.wikipedia.org/wiki/IDLE)
- [Infrared](https://en.wikipedia.org/wiki/Infrared)
- [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
- [IronPython](https://en.wikipedia.org/wiki/IronPython)
- [Jython](https://en.wikipedia.org/wiki/Jython)
- [List of Python software](https://en.wikipedia.org/wiki/List_of_Python_software)
- [Comparison of integrated development environments](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
- [Microcontroller](https://en.wikipedia.org/wiki/Microcontroller)
- [Ninja-IDE](https://en.wikipedia.org/wiki/Ninja-IDE)
- [Numba](https://en.wikipedia.org/wiki/Numba)
- [Pip (package manager)](https://en.wikipedia.org/wiki/Pip_(package_manager))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Programming language](https://en.wikipedia.org/wiki/Programming_language)
- [Programming language implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
- [Psyco](https://en.wikipedia.org/wiki/Psyco)
- [PyCharm](https://en.wikipedia.org/wiki/PyCharm)
- [PyDev](https://en.wikipedia.org/wiki/PyDev)
- [PyPy](https://en.wikipedia.org/wiki/PyPy)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Conference](https://en.wikipedia.org/wiki/Python_Conference)
- [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- [Python for S60](https://en.wikipedia.org/wiki/Python_for_S60)
- [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi)
- [Read the Docs](https://en.wikipedia.org/wiki/Read_the_Docs)
- [Read–eval–print loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
- [Reddit](https://en.wikipedia.org/wiki/Reddit)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Shed Skin](https://en.wikipedia.org/wiki/Shed_Skin)
- [Single-board computer](https://en.wikipedia.org/wiki/Single-board_computer)
- [Software](https://en.wikipedia.org/wiki/Software)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software development](https://en.wikipedia.org/wiki/Software_development)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spyder (software)](https://en.wikipedia.org/wiki/Spyder_(software))
- [Stackless Python](https://en.wikipedia.org/wiki/Stackless_Python)
- [Twitter](https://en.wikipedia.org/wiki/Twitter)
- [CPython](https://en.wikipedia.org/wiki/CPython)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [YouTube](https://en.wikipedia.org/wiki/YouTube)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Wikipedia:Stub](https://en.wikipedia.org/wiki/Wikipedia:Stub)
- [Template:Prog-lang-stub](https://en.wikipedia.org/wiki/Template:Prog-lang-stub)
- [Template:Python (programming language)](https://en.wikipedia.org/wiki/Template:Python_(programming_language))
- [Template talk:Prog-lang-stub](https://en.wikipedia.org/wiki/Template_talk:Prog-lang-stub)
- [Template talk:Python (programming language)](https://en.wikipedia.org/wiki/Template_talk:Python_(programming_language))
- [Category:Articles lacking reliable references from August 2019](https://en.wikipedia.org/wiki/Category:Articles_lacking_reliable_references_from_August_2019)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:29:02.365368+00:00_