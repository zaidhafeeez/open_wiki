# Borg (backup software)

## Article Metadata

- **Last Updated:** 2024-12-15T03:25:55.131610+00:00
- **Original Article:** [Borg (backup software)](https://en.wikipedia.org/wiki/Borg_(backup_software))
- **Language:** en
- **Page ID:** 46590812

## Summary

Borg (previously called Attic) is deduplicating backup software for various Unix-like operating systems. Borg is notably included in the Debian, Fedora, and Arch repositories.

## Categories

- Category:2010 software
- Category:All Wikipedia articles written in American English
- Category:All articles with dead external links
- Category:Articles with dead external links from November 2021
- Category:Articles with short description
- Category:Backup software for Linux
- Category:Free backup software
- Category:Python (programming language) software
- Category:Short description is different from Wikidata
- Category:Software using the BSD license
- Category:Use American English from January 2023
- Category:Webarchive template wayback links

## Table of Contents

- History
- Design
- Frontends
- See also
- References
- External links

## Content

Borg (previously called Attic) is deduplicating backup software for various Unix-like operating systems. Borg is notably included in the Debian, Fedora, and Arch repositories.

History
Attic development began in 2010 and was accepted to Debian in August 2013. Attic is available from pip and notably part of Debian, Ubuntu, Arch and Slackware.
In 2015, Attic was forked as "Borg" to support a "more open, faster paced development", according to its developers. Many issues in Attic have been fixed in this fork, but backward compatibility with the original program has been lost (a non-reversible upgrade process exists). Borg 1.0.0 was finally released on 5 March 2016.
The next major version, 2.0, currently in beta, will break backward compatibility again, requiring a non-reversible upgrade process.
As of 2024, Borg is actively developed by many contributors, while Attic is no longer available. Stable releases can be found in various Linux distributions such as Arch Linux, Debian, Fedora, OpenSUSE, Ubuntu, as well as in the ports collection of various BSD derivatives and through Homebrew for macOS. The project also offers pre-built binaries for Linux, FreeBSD, and macOS.
As of April 2021, the attic website was removed.

Design
Borg offers efficient, deduplicated, compressed and (optionally) encrypted and authenticated backups.
A backup includes metadata like owner/group, permissions, POSIX ACLs and Extended file attributes.
It handles special files also - like hardlinks, symlinks, devices files, etc. Internally it represents the files in an archive as a stream of metadata, similar to tar and unlike tools such as git. The Borg project has created extensive documentation of the internal workings.
It uses a rolling hash to implement global data deduplication.
Compression defaults to lz4, encryption is AES (via OpenSSL) authenticated by a HMAC.

Frontends
Since Borg is essentially a command line program, several GUI frontends for Borg exist. A few desktop app, Pika and Vorta for example and many web interfaces. See the community pages for an updated list.

See also
List of backup software
Comparison of backup software

References
External links
Official Website of BorgBackup
Website of Attic Backup Archived 2021-04-15 at the Wayback Machine
Resources from the Borg Community

## Related Articles

### Internal Links

- [Access-control list](https://en.wikipedia.org/wiki/Access-control_list)
- [Acronis True Image](https://en.wikipedia.org/wiki/Acronis_True_Image)
- [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [Arch Linux](https://en.wikipedia.org/wiki/Arch_Linux)
- [Backblaze](https://en.wikipedia.org/wiki/Backblaze)
- [Backup software](https://en.wikipedia.org/wiki/Backup_software)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Carbon Copy Cloner](https://en.wikipedia.org/wiki/Carbon_Copy_Cloner)
- [Clonezilla](https://en.wikipedia.org/wiki/Clonezilla)
- [Code42](https://en.wikipedia.org/wiki/Code42)
- [Comparison of backup software](https://en.wikipedia.org/wiki/Comparison_of_backup_software)
- [Cygwin](https://en.wikipedia.org/wiki/Cygwin)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [Data deduplication](https://en.wikipedia.org/wiki/Data_deduplication)
- [Dd (Unix)](https://en.wikipedia.org/wiki/Dd_(Unix))
- [Debian](https://en.wikipedia.org/wiki/Debian)
- [Disk cloning](https://en.wikipedia.org/wiki/Disk_cloning)
- [Extended file attributes](https://en.wikipedia.org/wiki/Extended_file_attributes)
- [Fedora Linux](https://en.wikipedia.org/wiki/Fedora_Linux)
- [File size](https://en.wikipedia.org/wiki/File_size)
- [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [Git](https://en.wikipedia.org/wiki/Git)
- [GitHub](https://en.wikipedia.org/wiki/GitHub)
- [HMAC](https://en.wikipedia.org/wiki/HMAC)
- [LZ4 (compression algorithm)](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm))
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [List of backup software](https://en.wikipedia.org/wiki/List_of_backup_software)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [NetBSD](https://en.wikipedia.org/wiki/NetBSD)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [OpenBSD](https://en.wikipedia.org/wiki/OpenBSD)
- [OpenSSL](https://en.wikipedia.org/wiki/OpenSSL)
- [OpenSUSE](https://en.wikipedia.org/wiki/OpenSUSE)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Pip (package manager)](https://en.wikipedia.org/wiki/Pip_(package_manager))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Rolling hash](https://en.wikipedia.org/wiki/Rolling_hash)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Tar (computing)](https://en.wikipedia.org/wiki/Tar_(computing))
- [Time Machine (macOS)](https://en.wikipedia.org/wiki/Time_Machine_(macOS))
- [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)
- [Unix](https://en.wikipedia.org/wiki/Unix)
- [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Windows Subsystem for Linux](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux)
- [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web)
- [Wikipedia:Contents/Portals](https://en.wikipedia.org/wiki/Wikipedia:Contents/Portals)
- [Wikipedia:Link rot](https://en.wikipedia.org/wiki/Wikipedia:Link_rot)
- [Template:Backup software](https://en.wikipedia.org/wiki/Template:Backup_software)
- [Template talk:Backup software](https://en.wikipedia.org/wiki/Template_talk:Backup_software)
- [Category:Articles with dead external links from November 2021](https://en.wikipedia.org/wiki/Category:Articles_with_dead_external_links_from_November_2021)
- [Category:Backup software](https://en.wikipedia.org/wiki/Category:Backup_software)
- [Category:Use American English from January 2023](https://en.wikipedia.org/wiki/Category:Use_American_English_from_January_2023)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)
- [Portal:Internet](https://en.wikipedia.org/wiki/Portal:Internet)
- [Portal:Linux](https://en.wikipedia.org/wiki/Portal:Linux)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:25:55.131610+00:00_