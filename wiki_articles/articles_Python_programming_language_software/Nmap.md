# Nmap

## Article Metadata

- **Last Updated:** 2024-12-15T03:59:28.573285+00:00
- **Original Article:** [Nmap](https://en.wikipedia.org/wiki/Nmap)
- **Language:** en
- **Page ID:** 401135

## Summary

Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses.
Nmap provides a number of features for probing computer networks, including host discovery and service and operating system detection. These features are extensible by scripts that provide more advanced service detection, vulnerability detection, and other features. Nmap 

## Categories

- Category:All articles with unsourced statements
- Category:Articles with short description
- Category:Articles with unsourced statements from January 2014
- Category:C++ software
- Category:Cross-platform free software
- Category:Free network management software
- Category:Linux security software
- Category:Lua (programming language)-scriptable software
- Category:Network analyzers
- Category:Pentesting software toolkits
- Category:Port scanners
- Category:Python (programming language) software
- Category:Security testing tools
- Category:Short description is different from Wikidata
- Category:Unix network-related software
- Category:Webarchive template wayback links

## Table of Contents

- Features
- User interfaces
- Output
- History
- Legal issues
- License
- In popular culture
- In academia
- Examples
- See also
- Bibliography
- References
- External links

## Content

Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses.
Nmap provides a number of features for probing computer networks, including host discovery and service and operating system detection. These features are extensible by scripts that provide more advanced service detection, vulnerability detection, and other features. Nmap can adapt to network conditions including latency and congestion during a scan.
Nmap started as a Linux utility and was ported to other systems including Windows, macOS, and BSD. It is most popular on Linux, followed by Windows.

Features
Nmap features include:

Fast scan (nmap -F [target]) – Performing a basic port scan for fast result.
Host discovery – Identifying hosts on a network. For example, listing the hosts that respond to TCP and/or ICMP requests or have a particular port open.
Port scanning – Enumerating the open ports on target hosts.
Version detection – Interrogating network services on remote devices to determine application name and version number.
Ping Scan – Check host by sending ping requests.
TCP/IP stack fingerprinting – Determining the operating system and hardware characteristics of network devices based on observations of network activity of said devices.
Scriptable interaction with the target – using Nmap Scripting Engine (NSE) and Lua programming language.
Nmap can provide further information on targets, including reverse DNS names, device types, and MAC addresses.
Typical uses of Nmap:

Auditing the security of a device or firewall by identifying the network connections which can be made to, or through it.
Identifying open ports on a target host in preparation for auditing.
Network inventory, network mapping, maintenance and asset management.
Auditing the security of a network by identifying new servers.
Generating traffic to hosts on a network, response analysis  and response time measurement.
Finding and exploiting vulnerabilities in a network.
DNS queries and subdomain search

User interfaces
NmapFE, originally written by Kanchan, was Nmap's official GUI for Nmap versions 2.2 to 4.22. For Nmap 4.50 (originally in the 4.22SOC development series) NmapFE was replaced with Zenmap, a new official graphical user interface based on UMIT, developed by Adriano Monteiro Marques.
Web-based interfaces exist that allow either controlling Nmap or analysing Nmap results from a web browser, such as IVRE.

Output
Four different output formats are offered by Nmap. Everything is saved to a file except the interactive output. Text processing software can be used to modify Nmap output, allowing the user to customize reports.

Interactive
presented and updated real time when a user runs Nmap from the command line. Various options can be entered during the scan to facilitate monitoring.
XML
a format that can be further processed by XML tools. It can be converted into a HTML report using XSLT.
Grepable
output that is tailored to line-oriented processing tools such as grep, sed, or awk.
Normal
the output as seen while running Nmap from the command line, but saved to a file.
Script kiddie
meant to be an amusing way to format the interactive output replacing letters with their visually alike number representations. For example, Interesting ports becomes Int3rest1ng p0rtz. This is known as Leet.

History
Nmap was first published in September 1997, as an article in Phrack Magazine with source-code included. With help and contributions of the computer security community, development continued. Enhancements included operating system fingerprinting, service fingerprinting, code rewrites (C to C++), additional scan types, protocol support (e.g. IPv6, SCTP) and new programs that complement Nmap's core features.
Major releases include:

Legal issues
Nmap is a tool that can be used to discover services running on Internet connected systems. Like any tool, it could potentially be used for black hat hacking, as a precursor to attempts to gain unauthorized access to computer systems. However, Nmap is also used by security and systems administrators to assess their own networks for vulnerabilities (i.e. white hat hacking).
System administrators can use Nmap to search for unauthorized servers, or for computers that do not conform to security standards.

In 2003 Supreme Court of Finland has ruled that port scanning has amounted to an attempted computer break in, which was illegal under Finnish Penal code at the time:In its ruling the Supreme Court stated that the defendant had systematically carried out port scanning operations to gather information for the purpose of unauthorised break-in to the bank's computer network. This amounted to an attempted computer break in.

License
Nmap was originally distributed under the GNU General Public License (GPL). In later releases, Nmap's authors added clarifications and specific interpretations to the license where they felt the GPL was unclear or lacking. For instance, Nmap 3.50 specifically revoked the license of SCO Group to distribute Nmap software because of their views on the SCO-Linux controversies.
Starting with version 7.90, Nmap transitions to a new custom license NPSL, dual-licensing versions 7.90, 7.91, and 7.92 under both old and new licenses. Several Linux distributions consider the new license non-free.

In popular culture
In The Matrix Reloaded, Trinity is seen using Nmap to access a power plant's computer system, allowing Neo to "physically" break into a building. The appearance of Nmap in the film was widely discussed on Internet forums and hailed as an unusually realistic example of hacking.
Nmap and NmapFE were used in The Listening, a 2006 movie about a former NSA officer who defects and mounts a clandestine counter-listening station high in the Italian alps.
Nmap source code can be seen in the movie Battle Royale, as well as brief views of the command line version of Nmap executing in Live Free or Die Hard and Bourne Ultimatum. In 2013, Nmap continued to make appearances in movies including popular sci-fi movie Elysium.
The film Dredd, a film adaptation of the famous Judge Dredd comics, was released in 2012 and also contains multiple Nmap scenes. Nmap is used for network reconnaissance and exploitation of the slum tower network. It is even seen briefly in the movie's trailer.
The command Nmap is widely used in the video game Hacknet, allowing to probe the network ports of a target system to hack it.
In Snowden, Nmap is used in the aptitude test scene about 14 minutes into the movie.

In academia
Nmap is an integral part of academic activities. It has been used for research involving the TCP/IP protocol suite and networking in general. Besides being a research tool, Nmap has also become a research topic.

Examples
See also
Bibliography
References
External links
Official website

## Related Articles

### Internal Links

- [Aircrack-ng](https://en.wikipedia.org/wiki/Aircrack-ng)
- [AWK](https://en.wikipedia.org/wiki/AWK)
- [BBC News](https://en.wikipedia.org/wiki/BBC_News)
- [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
- [BackBox](https://en.wikipedia.org/wiki/BackBox)
- [BackTrack](https://en.wikipedia.org/wiki/BackTrack)
- [Battle Royale (film)](https://en.wikipedia.org/wiki/Battle_Royale_(film))
- [Black hat (computer security)](https://en.wikipedia.org/wiki/Black_hat_(computer_security))
- [The Bourne Ultimatum (film)](https://en.wikipedia.org/wiki/The_Bourne_Ultimatum_(film))
- [Burglary](https://en.wikipedia.org/wiki/Burglary)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Computer network](https://en.wikipedia.org/wiki/Computer_network)
- [Computerworld](https://en.wikipedia.org/wiki/Computerworld)
- [Conficker](https://en.wikipedia.org/wiki/Conficker)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Dredd](https://en.wikipedia.org/wiki/Dredd)
- [Elysium (film)](https://en.wikipedia.org/wiki/Elysium_(film))
- [English language](https://en.wikipedia.org/wiki/English_language)
- [Exploit (computer security)](https://en.wikipedia.org/wiki/Exploit_(computer_security))
- [Firewall (computing)](https://en.wikipedia.org/wiki/Firewall_(computing))
- [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License)
- [GTK](https://en.wikipedia.org/wiki/GTK)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [Google Summer of Code](https://en.wikipedia.org/wiki/Google_Summer_of_Code)
- [Gordon Lyon](https://en.wikipedia.org/wiki/Gordon_Lyon)
- [Grep](https://en.wikipedia.org/wiki/Grep)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [Hacknet](https://en.wikipedia.org/wiki/Hacknet)
- [Host (network)](https://en.wikipedia.org/wiki/Host_(network))
- [Hping](https://en.wikipedia.org/wiki/Hping)
- [IEEE Security & Privacy](https://en.wikipedia.org/wiki/IEEE_Security_%26_Privacy)
- [IPv6](https://en.wikipedia.org/wiki/IPv6)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Internet Control Message Protocol](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol)
- [Judge Dredd](https://en.wikipedia.org/wiki/Judge_Dredd)
- [Kali Linux](https://en.wikipedia.org/wiki/Kali_Linux)
- [Kevin Poulsen](https://en.wikipedia.org/wiki/Kevin_Poulsen)
- [Kismet (software)](https://en.wikipedia.org/wiki/Kismet_(software))
- [Leet](https://en.wikipedia.org/wiki/Leet)
- [Leet](https://en.wikipedia.org/wiki/Leet)
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [Live Free or Die Hard](https://en.wikipedia.org/wiki/Live_Free_or_Die_Hard)
- [Lua (programming language)](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [MAC address](https://en.wikipedia.org/wiki/MAC_address)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Metasploit](https://en.wikipedia.org/wiki/Metasploit)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Mmap](https://en.wikipedia.org/wiki/Mmap)
- [Netcat](https://en.wikipedia.org/wiki/Netcat)
- [Neo (The Matrix)](https://en.wikipedia.org/wiki/Neo_(The_Matrix))
- [Nessus (software)](https://en.wikipedia.org/wiki/Nessus_(software))
- [Netcat](https://en.wikipedia.org/wiki/Netcat)
- [Network congestion](https://en.wikipedia.org/wiki/Network_congestion)
- [Network delay](https://en.wikipedia.org/wiki/Network_delay)
- [Network mapping](https://en.wikipedia.org/wiki/Network_mapping)
- [Network packet](https://en.wikipedia.org/wiki/Network_packet)
- [Network enumeration](https://en.wikipedia.org/wiki/Network_enumeration)
- [Network security](https://en.wikipedia.org/wiki/Network_security)
- [OpenVAS](https://en.wikipedia.org/wiki/OpenVAS)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Osborne Clarke](https://en.wikipedia.org/wiki/Osborne_Clarke)
- [Phrack](https://en.wikipedia.org/wiki/Phrack)
- [Port scanner](https://en.wikipedia.org/wiki/Port_scanner)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Proprietary software](https://en.wikipedia.org/wiki/Proprietary_software)
- [Pseudonym](https://en.wikipedia.org/wiki/Pseudonym)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [SCO–Linux disputes](https://en.wikipedia.org/wiki/SCO%E2%80%93Linux_disputes)
- [SCO Group](https://en.wikipedia.org/wiki/SCO_Group)
- [Stream Control Transmission Protocol](https://en.wikipedia.org/wiki/Stream_Control_Transmission_Protocol)
- [Script kiddie](https://en.wikipedia.org/wiki/Script_kiddie)
- [Scripting language](https://en.wikipedia.org/wiki/Scripting_language)
- [Sed](https://en.wikipedia.org/wiki/Sed)
- [Shodan (website)](https://en.wikipedia.org/wiki/Shodan_(website))
- [Snowden (film)](https://en.wikipedia.org/wiki/Snowden_(film))
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Subdomain](https://en.wikipedia.org/wiki/Subdomain)
- [Supreme Court of Finland](https://en.wikipedia.org/wiki/Supreme_Court_of_Finland)
- [Internet protocol suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)
- [TCP/IP stack fingerprinting](https://en.wikipedia.org/wiki/TCP/IP_stack_fingerprinting)
- [Port (computer networking)](https://en.wikipedia.org/wiki/Port_(computer_networking))
- [The Listening (film)](https://en.wikipedia.org/wiki/The_Listening_(film))
- [The Matrix Reloaded](https://en.wikipedia.org/wiki/The_Matrix_Reloaded)
- [The Register](https://en.wikipedia.org/wiki/The_Register)
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [Trinity (The Matrix)](https://en.wikipedia.org/wiki/Trinity_(The_Matrix))
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Web service](https://en.wikipedia.org/wiki/Web_service)
- [White hat (computer security)](https://en.wikipedia.org/wiki/White_hat_(computer_security))
- [Wireshark](https://en.wikipedia.org/wiki/Wireshark)
- [XML](https://en.wikipedia.org/wiki/XML)
- [XSLT](https://en.wikipedia.org/wiki/XSLT)
- [ZMap (software)](https://en.wikipedia.org/wiki/ZMap_(software))
- [Wikipedia:Citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)
- [Category:Articles with unsourced statements from January 2014](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_January_2014)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:59:28.573285+00:00_