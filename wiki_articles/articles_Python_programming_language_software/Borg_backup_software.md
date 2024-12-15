# Borg (backup software)

## Metadata
- **Last Updated:** 2024-12-03 07:42:33 UTC
- **Original Article:** [Borg (backup software)](https://en.wikipedia.org/wiki/Borg_(backup_software))
- **Language:** en
- **Page ID:** 46590812

## Summary
Borg (previously called Attic) is deduplicating backup software for various Unix-like operating systems. Borg is notably included in the Debian, Fedora, and Arch repositories.

## Categories
This article belongs to the following categories:

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

## Archive Info
- **Archived on:** 2024-12-15 20:39:37 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2303 bytes
- **Word Count:** 353 words
