# Waydroid

## Metadata
- **Last Updated:** 2024-12-03 08:04:53 UTC
- **Original Article:** [Waydroid](https://en.wikipedia.org/wiki/Waydroid)
- **Language:** en
- **Page ID:** 76530735

## Summary
Waydroid is a container-based method that enables Android to run in a containerized environment on Linux systems. By using Linux namespaces, Waydroid keeps Android isolated but allows it to access the host system's hardware. Built on a customized version of LineageOS (Android 11), it enables Android applications to function alongside Linux applications on desktops and Linux-based mobile devices.

## Categories
This article belongs to the following categories:

- Category:Android (operating system) software
- Category:Articles with short description
- Category:Linux emulation software
- Category:Linux software
- Category:Python (programming language) software
- Category:Short description is different from Wikidata

## Table of Contents

- Background
- Technical overview
- Qualities
- Limitations

## Content

Waydroid is a container-based method that enables Android to run in a containerized environment on Linux systems. By using Linux namespaces, Waydroid keeps Android isolated but allows it to access the host system's hardware. Built on a customized version of LineageOS (Android 11), it enables Android applications to function alongside Linux applications on desktops and Linux-based mobile devices.

Background
Waydroid was created to facilitate the use of Android applications on Linux-based platforms. It is based on ideas from previous projects, such as Anbox, which also aimed to run Android using containerization techniques. Although primarily developed for Halium-based Linux phones, Waydroid is compatible with any device using a Linux kernel.

Technical overview
To isolate and operate an entire Android system inside a container, Waydroid utilizes Linux namespaces such as: user, pid, uts, net, mount, and ipc. This method leverages the functionalities of the Linux kernel to provide Android applications with a contained system environment. The Android operating environment comes along with a basic modified Android system image that is built on LineageOS.

Vanilla: A simple picture devoid of Google functionality.
GApps: includes Google services.

System requirements
Waydroid allows Android applications connect with a Linux system's hardware, including the network and display capabilities. Waydroid enables Android applications to access network services through the host system's Internet connection and appear directly on the Linux desktop, integrating with the rest of the system.

The CPU requirements for Waydroid vary based on architecture. To verify compatibility, users can inspect their CPU's specifications using:
Waydroid is optimized for use with Intel GPUs, which usually function without requiring additional setup. It also supports AMD GPUs. However, in certain cases, users might need to create a custom Waydroid image if they experience compatibility issues.

Qualities
With support for desktops like Fedora, Arch Linux, and Ubuntu, Waydroid allows users to integrate Android applications into Linux environments. Waydroid includes commands for adjusting the size and location of the application window to match the Linux desktop experience, users may choose to run Android applications in different screen modes.
Waydroid's graphical range is augmented by the ability to transfer files between the Android container and the host Linux system. Linux users can transfer documents or video assets into the Android environment by connecting host directories.

Limitations
Waydroid does not include an emulation layer. As a result, devices can only run Android applications that match their specific hardware architecture. Personal computers (x86) are limited to x86 Android applications, while most phones and tablets (which use ARM64) can only run ARM64-compatible applications. The developers are considering adding an emulation layer in the future, potentially utilizing components of the Android system built for Windows 11.


== Sources ==

## Archive Info
- **Archived on:** 2024-12-15 21:08:57 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 3075 bytes
- **Word Count:** 443 words
