# CircuitPython

_Last updated: 2024-12-14T15:02:44.952905_

**Original Article:** [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)

**Summary:** CircuitPython is an open-source derivative of the MicroPython programming language targeted toward students and beginners. Development of CircuitPython is supported by Adafruit Industries. It is a software implementation of the Python 3 programming language, written in C. It has been ported to run on several modern microcontrollers.
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