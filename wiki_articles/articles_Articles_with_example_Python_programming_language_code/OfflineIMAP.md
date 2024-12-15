# OfflineIMAP

## Metadata
- **Last Updated:** 2024-11-24 06:40:53 UTC
- **Original Article:** [OfflineIMAP](https://en.wikipedia.org/wiki/OfflineIMAP)
- **Language:** en
- **Page ID:** 36810725

## Summary
OfflineIMAP is  IMAP synchronization utility software, capable of synchronizing mail on IMAP server with local Maildir folder or another server.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Data synchronization
- Category:Free email software
- Category:Free software programmed in Python
- Category:Software that uses Tk (software)
- Category:Use mdy dates from September 2012

## Table of Contents

- Description
- Configuration
- See also

## Content

OfflineIMAP is  IMAP synchronization utility software, capable of synchronizing mail on IMAP server with local Maildir folder or another server.

Description
The synchronization is performed bidirectionally between two endpoints ("Remote" and "Local" repositories).
OfflineIMAP accesses mail servers only via Internet Message Access Protocol. (It does not support Post Office Protocol, another popular way to get mail from a server.) It works faster (though it is sensitive to connection's latency) and supports more advanced features than most mail clients. A special mode for better handling the non-standard implementation of IMAP in Gmail may optionally be enabled in a configuration file.
When configured to store mail locally, OfflineIMAP uses the Maildir format. Unix mail boxes support may be added in the future, though currently it is not implemented.

Configuration
Several synchronization accounts, each consisting of Remote and Local repositories, may be defined in configuration file. Each repository is then configured separately, allowing to specify credentials and access method.

Filtering and translation
OfflineIMAP is capable of filtering the folders of Remote repository, so that only partial synchronization would occur if needed. To use this capability one has to define the mask that would be matched against the list of folders with each synchronization. This is achieved by using Python's lambda capability; for example, to synchronize only "INBOX", "Sent Mail" and "Received" folders one should specify the following rule:

Remaining folders' names may be altered (translated) using similar construct:

This technique may also be used to synchronize the content of an IMAP server to the folder of another server.

Limitations
Each account has to use separate directory; otherwise the synchronization process may suffer from unexpected behavior or even data loss.

User interface
OfflineIMAP provides several command-line interfaces, including interactive color curses-based, non-interactive console logging, and several yet less verbose modes. Tk-based graphical user interface is also available.

See also

Mail delivery agent
getmail
fetchmail


== References ==

## Archive Info
- **Archived on:** 2024-12-15 20:38:35 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2192 bytes
- **Word Count:** 313 words
