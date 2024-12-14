# MicroPython

_Last updated: 2024-12-14T15:19:03.555590_

**Original Article:** [MicroPython](https://en.wikipedia.org/wiki/MicroPython)

**Summary:** MicroPython is a software implementation of a programming language largely compatible with Python 3, written in C, that is optimized to run on a microcontroller.
MicroPython consists of a Python compiler to bytecode and a runtime interpreter of that bytecode. The user is presented with an interactive prompt (the REPL) to execute supported commands immediately. Included are a selection of core Python libraries; MicroPython includes modules which give the programmer access to low-level hardware.
M

## Categories
- Category:Articles with short description
- Category:BBC computer literacy projects
- Category:Free software programmed in C
- Category:Microcontroller software
- Category:Python (programming language)
- Category:Short description matches Wikidata
- Category:Software using the MIT license
- Category:Use dmy dates from April 2022

## Content

MicroPython is a software implementation of a programming language largely compatible with Python 3, written in C, that is optimized to run on a microcontroller.
MicroPython consists of a Python compiler to bytecode and a runtime interpreter of that bytecode. The user is presented with an interactive prompt (the REPL) to execute supported commands immediately. Included are a selection of core Python libraries; MicroPython includes modules which give the programmer access to low-level hardware.
MicroPython does have an inline assembler, which lets the code run at full speed, but it is not portable across different microcontrollers.
The source code for the project is available on GitHub under the MIT License.

History
MicroPython was originally created by the Australian programmer Damien George, after a successful Kickstarter-backed campaign in 2013. The original Kickstarter campaign released MicroPython with an STM32F4-powered development board "pyboard". In the meantime MicroPython has been developed to support a number of ARM based architectures.
The ports supported in the mainline are ARM Cortex-M (many STM32
boards, RP2040 boards, TI CC3200/WiPy, Teensy boards, Nordic nRF series, SAMD21 and SAMD51), ESP8266, ESP32,
16-bit PIC, Unix, Windows, Zephyr, and JavaScript.
Also, there are many forks for a variety of systems and hardware platforms not supported in the mainline.
In 2016, a version of MicroPython for the BBC Micro Bit was created as part of the Python Software Foundation's contribution to the Micro Bit partnership with the BBC.
In July 2017, MicroPython was forked to create CircuitPython, a version of MicroPython with emphasis on education and ease of use. MicroPython and CircuitPython support somewhat different sets of hardware (e.g. CircuitPython supports Atmel SAM D21 and D51 boards, but dropped support for ESP8266). As of version 4.0, CircuitPython is based on MicroPython version 1.9.4.
In 2017, Microsemi made a MicroPython port for RISC-V (RV32 and RV64) architecture.
In April 2019, a version of MicroPython for the Lego Mindstorms EV3 was created.
In January 2021, a MicroPython port for the RP2040 (ARM Cortex-M0+, on Raspberry Pi Pico and others) was created.

Features
Ability to run Python
MicroPython has the ability to run Python, allowing users to create simple and easy-to-understand programs.  MicroPython supports many standard Python libraries, supporting more than 80% of the features of Python's most used libraries. MicroPython was designed specifically to support the typical performance gap between microcontrollers and Python. Python code is able to directly access and interact with hardware, with increased hardware possibilities that are not available using a normal Python application that is run on an operating system.

Code portability
MicroPython's utilisation of hardware abstraction layer (HAL) technology allows developed code to be portable among different microcontrollers within the same family or platform and on devices that support and can download MicroPython. Programs are often developed and tested on high-performance microcontrollers and distributed with the final application used on lower-performance microcontrollers.

Modules
MicroPython offers functionality, once new code has been written, to create a frozen module and use it as a library which can be a part of developed firmware. This feature assists with avoiding repetitive downloading of the same, already error-free, tested code into a MicroPython environment. This type of module will be saved to a microcontroller's modules directory for compiling and uploading to the microcontroller where the library will be available using Python's import command to be used repeatedly.

Read–eval–print loop
The read–eval–print loop (REPL) allows a developer to enter individual lines of code and have them run immediately on a terminal. Linux-based and macOS systems have terminal emulators that can be used to create a direct connection to a MicroPython device's REPL using a serial USB connection. The REPL assists with the immediate testing of parts of an application as each part of the code can be run and the results visually examined. Once different parts of code are loaded into the REPL, additional REPL features can be used to experiment with that code's functionality.
Helpful REPL commands (once connected to a serial console):

CTRL+C: keyboard interrupt
CTRL+D: reload
help(): help message
help("modules"): lists built-in modules
import board↵ Enterdir(board): lists all the pins on your microcontroller board that are available to be used in a program's code

Limitations
Although MicroPython fully implements Python language version 3.4 and much of 3.5, it does not implement all language features introduced from 3.5 onwards, though some new syntax from 3.6 and more recent features from later versions, e.g. from 3.8 (assignment expressions) and 3.9. It includes a subset of the standard library.
MicroPython has more limited hardware support in the microcontroller market than other popular platforms, like Arduino with a smaller number of microcontroller choices that support the language. MicroPython does not include an integrated development environment (IDE) or specific editor unlike other platforms.

Syntax and semantics
MicroPython's syntax is adopted from Python, due to its clear and easy-to-understand style and power. Unlike most other programming languages less punctuation is used with fewer syntactical machinations in order to prioritise readability.

Code blocks
MicroPython adopts Python's code block style, with code specific to a particular function, condition or loop being indented. This differs from most other languages which typically use symbols or keywords to delimit blocks.  This assists with the readability of MicroPython code as the visual structure mirrors the semantic structure. This key feature is simple but important as misused indentation can result in code executing under a wrong condition or an overall error from the interpreter.
A colon (:) is the key symbol used to indicate the ending of a condition statement. The indent size is equivalent to one tab or 4 spaces.

Operations
MicroPython has the ability to perform various mathematical operations using primitive and logical operations.

Libraries
MicroPython is a lean and efficient implementation of Python with libraries similar to those in Python. Some standard Python libraries have an equivalent library in MicroPython renamed to distinguish between the two. MicroPython libraries are smaller with less popular features removed or modified to save memory.
The three types of libraries in MicroPython:

derived from a standard Python library (built-in libraries)
specific MicroPython libraries
specific libraries to assist with hardware functionality
MicroPython is highly customisable and configurable, with language differing between each board (microcontroller) and the availability of libraries may differ. Some functions and classes in a module or the entire module may be unavailable or altered.

Custom MicroPython libraries
When developers begin to create a new application, standard MicroPython libraries and drivers may not meet the requirements, with insufficient operations or calculations. Similar to Python, there is the possibility of extending MicroPython's functionality with custom libraries which extend the ability of the existing libraries and firmware.
In MicroPython, files ending with .py take preference over other library aliases which allows users to extend the use and implementation of the existing libraries.

Supporting hardware
As MicroPython's implementation and popularity continues to grow, more boards have the ability to run MicroPython. Many developers are building processor specific versions that can be downloaded onto different microcontrollers. Installing MicroPython on microcontrollers is well documented and user-friendly. MicroPython allows interactions between microcontroller hardware and applications to be simple, allowing access to a range of functionality while working in a resource constrained environment, with a strong level of responsiveness.
The two types of boards used to run MicroPython:

MicroPython loaded when manufactured, meaning only MicroPython can be run.
boards that have firmware that allows MicroPython to be installed to the board.

Executing code
To move a program onto a MicroPython board, create a file and copy it onto the microcontroller in order to execute. With the hardware connected to a device, such as a computer, the board's flash drive will appear on the device allowing files to be moved to the flash drive. There will be two existing python files, boot.py and main.py that are typically not modified, main.py may be modified if you wish to run the program every time the microcontroller is booted, otherwise, programs will be run using the REPL console.

Pyboard
The pyboard is the official MicroPython microcontroller board which fully supports MicroPython's software features. The pyboard's hardware features include:

microcontroller (MCU, CPU, flash ROM and RAM)
microUSB connector
micro-SD card slot
IO pins
switches, LEDs, servo ports, real time clock, accelerometer

The booting process
The pyboard contains an internal drive (filesystem) named /flash which is stored within the board's flash memory, additionally, a microSD card can be inserted into a slot and is accessible through /sd. When booted up, a pyboard must select a filesystem to boot from either /flash or /sd with the current directory being set to either /flash or /sd. By default, if an SD card is inserted, /sd will be used, if not, /flash is used. If needed, the use of the SD card for the booting process can be avoided by creating an empty file called /flash/SKIPSD which will remain on the board and exist when the pyboard is booted up and will skip the SD card for the booting process.

Boot modes
When the pyboard is powered up normally or the reset button is pressed then the pyboard is booted in a standard mode, meaning that the boot.py file is executed, then the USB configured and finally the python program will run.
There is an ability to override the standard boot sequence through holding down the user switch whilst the board is in the booting process and then pressing reset as you continue to hold the user switch. The pyboard's LEDs will flick between modes and once the LEDs have reached the mode wanted by the user, they can let go of the user switch and the board will boot in the specific mode.
the boot modes are:

standard boot: green LED only (runs boot.py then python program)
safe boot: orange LED only (does not run any scripts during boot-up)
filesystem reset: green and orange LED together (resets flash drive to factory state and boots in safe mode)
used as a fix when filesystem is corrupted

Errors
if red and green LEDs flash alternatively then the python script has an error, and you must use the REPL to debug.
if all 4 LEDs cycle on and off then there is a hard fault which cannot be recovered from and requires a hard reset.

Programming examples
Hello world program:

Importing + turning on a LED:

Reading a file + loop:

Bytecode
MicroPython includes a cross compiler which generates MicroPython bytecode (file extension .mpy). The Python code can be compiled into the bytecode either directly on a microcontroller or it can be precompiled elsewhere.
MicroPython firmware can be built without the compiler, leaving only the virtual machine which can run the precompiled mpy programs.

Implementation and uses
MicroPython is utilised through firmware being loaded by standard software onto a particular microcontroller into flash memory, communicating using a terminal application loaded onto a computer that emulates a serial interface.
The main uses of MicroPython can be generalised into 3 categories:

educational purposes: using MicroPython's read–eval–print Loop (REPL) to interact with a microcontroller, it is possible to visually explain the concepts of data processing and communicating with boards in a simpler way than more complicated programming languages.
developing and testing device and sensor designs: MicroPython offers verified, bug-free, and thoroughly tested reference implementations of interfaces used in microcontrollers solving a common developer's task of implementing peripheral communication setup and control. MicroPython offers direct and interactive accessibility to device registers which makes it easy to verify functionality and develop and test hardware parts and devices and algorithms for control and acquiring data from a device.
monitoring and configuring tool for design of complex applications: certain applications require specific applications on high performing microcontrollers. MicroPython is able to assist with state monitoring and set-up of system parameters.
Implementation of MicroPython can differ depending on the availability of standard and supporting libraries and the microcontroller's flash memory and RAM size.

See also
Espruino
CircuitPython

References
External links
Official website
micropython on GitHub
GOTO 2016 • MicroPython & the Internet of Things • Damien George on YouTube
MicroPython playlist on YouTube • Tutorials by Tony DiCola / Adafruit