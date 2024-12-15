# OfflineIMAP

## Article Metadata

- **Last Updated:** 2024-12-15T04:40:27.578717+00:00
- **Original Article:** [OfflineIMAP](https://en.wikipedia.org/wiki/OfflineIMAP)
- **Language:** en
- **Page ID:** 36810725

## Summary

OfflineIMAP is  IMAP synchronization utility software, capable of synchronizing mail on IMAP server with local Maildir folder or another server.

## Categories

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

## Related Articles

### Internal Links

- [Airmail (email client)](https://en.wikipedia.org/wiki/Airmail_(email_client))
- [Alpine (email client)](https://en.wikipedia.org/wiki/Alpine_(email_client))
- [Anonymous function](https://en.wikipedia.org/wiki/Anonymous_function)
- [Apple Mail](https://en.wikipedia.org/wiki/Apple_Mail)
- [Arachne (web browser)](https://en.wikipedia.org/wiki/Arachne_(web_browser))
- [Balsa (email client)](https://en.wikipedia.org/wiki/Balsa_(email_client))
- [Batch processing](https://en.wikipedia.org/wiki/Batch_processing)
- [Becky!](https://en.wikipedia.org/wiki/Becky!)
- [Beonex Communicator](https://en.wikipedia.org/wiki/Beonex_Communicator)
- [BlitzMail](https://en.wikipedia.org/wiki/BlitzMail)
- [Bloomba](https://en.wikipedia.org/wiki/Bloomba)
- [Cc:Mail](https://en.wikipedia.org/wiki/Cc:Mail)
- [Citadel/UX](https://en.wikipedia.org/wiki/Citadel/UX)
- [Claris Emailer](https://en.wikipedia.org/wiki/Claris_Emailer)
- [Classilla](https://en.wikipedia.org/wiki/Classilla)
- [Claws Mail](https://en.wikipedia.org/wiki/Claws_Mail)
- [Cleancode eMail](https://en.wikipedia.org/wiki/Cleancode_eMail)
- [Columbia MM](https://en.wikipedia.org/wiki/Columbia_MM)
- [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface)
- [Comparison of email clients](https://en.wikipedia.org/wiki/Comparison_of_email_clients)
- [Logging (computing)](https://en.wikipedia.org/wiki/Logging_(computing))
- [Configuration file](https://en.wikipedia.org/wiki/Configuration_file)
- [Courier (email client)](https://en.wikipedia.org/wiki/Courier_(email_client))
- [Curses (programming library)](https://en.wikipedia.org/wiki/Curses_(programming_library))
- [Cyberdog](https://en.wikipedia.org/wiki/Cyberdog)
- [Cyberjack](https://en.wikipedia.org/wiki/Cyberjack)
- [Data synchronization](https://en.wikipedia.org/wiki/Data_synchronization)
- [EM Client](https://en.wikipedia.org/wiki/EM_Client)
- [Elm (email client)](https://en.wikipedia.org/wiki/Elm_(email_client))
- [Email](https://en.wikipedia.org/wiki/Email)
- [EmailTray](https://en.wikipedia.org/wiki/EmailTray)
- [Email client](https://en.wikipedia.org/wiki/Email_client)
- [DR-WebSpyder](https://en.wikipedia.org/wiki/DR-WebSpyder)
- [Eudora (email client)](https://en.wikipedia.org/wiki/Eudora_(email_client))
- [Fdm (software)](https://en.wikipedia.org/wiki/Fdm_(software))
- [Fetchmail](https://en.wikipedia.org/wiki/Fetchmail)
- [Forté Agent](https://en.wikipedia.org/wiki/Fort%C3%A9_Agent)
- [Foxmail](https://en.wikipedia.org/wiki/Foxmail)
- [GNOME Evolution](https://en.wikipedia.org/wiki/GNOME_Evolution)
- [GNUMail](https://en.wikipedia.org/wiki/GNUMail)
- [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License)
- [Geary (e-mail client)](https://en.wikipedia.org/wiki/Geary_(e-mail_client))
- [Getmail](https://en.wikipedia.org/wiki/Getmail)
- [Gmail](https://en.wikipedia.org/wiki/Gmail)
- [Gnus](https://en.wikipedia.org/wiki/Gnus)
- [GNU IceCat](https://en.wikipedia.org/wiki/GNU_IceCat)
- [Graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
- [GroupWise](https://en.wikipedia.org/wiki/GroupWise)
- [GyazMail](https://en.wikipedia.org/wiki/GyazMail)
- [HCL Notes](https://en.wikipedia.org/wiki/HCL_Notes)
- [Heirloom Project](https://en.wikipedia.org/wiki/Heirloom_Project)
- [Hiri (email client)](https://en.wikipedia.org/wiki/Hiri_(email_client))
- [Hula (software)](https://en.wikipedia.org/wiki/Hula_(software))
- [ISSN](https://en.wikipedia.org/wiki/ISSN)
- [Internet Message Access Protocol](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol)
- [Internet Messaging Program](https://en.wikipedia.org/wiki/Internet_Messaging_Program)
- [JSON Meta Application Protocol](https://en.wikipedia.org/wiki/JSON_Meta_Application_Protocol)
- [K-9 Mail](https://en.wikipedia.org/wiki/K-9_Mail)
- [Kontact](https://en.wikipedia.org/wiki/Kontact)
- [Linux.com](https://en.wikipedia.org/wiki/Linux.com)
- [Linux Journal](https://en.wikipedia.org/wiki/Linux_Journal)
- [Linux Magazine](https://en.wikipedia.org/wiki/Linux_Magazine)
- [Local Mail Transfer Protocol](https://en.wikipedia.org/wiki/Local_Mail_Transfer_Protocol)
- [MH Message Handling System](https://en.wikipedia.org/wiki/MH_Message_Handling_System)
- [Mahogany (email client)](https://en.wikipedia.org/wiki/Mahogany_(email_client))
- [Mail (Windows)](https://en.wikipedia.org/wiki/Mail_(Windows))
- [Email client](https://en.wikipedia.org/wiki/Email_client)
- [Message delivery agent](https://en.wikipedia.org/wiki/Message_delivery_agent)
- [Mailbird](https://en.wikipedia.org/wiki/Mailbird)
- [Mailbox (application)](https://en.wikipedia.org/wiki/Mailbox_(application))
- [Maildir](https://en.wikipedia.org/wiki/Maildir)
- [Mailody](https://en.wikipedia.org/wiki/Mailody)
- [Mailpile](https://en.wikipedia.org/wiki/Mailpile)
- [Mailx](https://en.wikipedia.org/wiki/Mailx)
- [Mask](https://en.wikipedia.org/wiki/Mask)
- [Mbox](https://en.wikipedia.org/wiki/Mbox)
- [Microsoft Entourage](https://en.wikipedia.org/wiki/Microsoft_Entourage)
- [Outlook Express](https://en.wikipedia.org/wiki/Outlook_Express)
- [Microsoft Mail](https://en.wikipedia.org/wiki/Microsoft_Mail)
- [Microsoft Outlook](https://en.wikipedia.org/wiki/Microsoft_Outlook)
- [Minnesota Internet Users Essential Tool](https://en.wikipedia.org/wiki/Minnesota_Internet_Users_Essential_Tool)
- [Modest (email client)](https://en.wikipedia.org/wiki/Modest_(email_client))
- [Mozilla Mail & Newsgroups](https://en.wikipedia.org/wiki/Mozilla_Mail_%26_Newsgroups)
- [Mozilla Thunderbird](https://en.wikipedia.org/wiki/Mozilla_Thunderbird)
- [Mulberry (email client)](https://en.wikipedia.org/wiki/Mulberry_(email_client))
- [Mutt (email client)](https://en.wikipedia.org/wiki/Mutt_(email_client))
- [Apple Mail](https://en.wikipedia.org/wiki/Apple_Mail)
- [Netscape Mail & Newsgroups](https://en.wikipedia.org/wiki/Netscape_Mail_%26_Newsgroups)
- [Netscape Navigator 9](https://en.wikipedia.org/wiki/Netscape_Navigator_9)
- [Newton (software)](https://en.wikipedia.org/wiki/Newton_(software))
- [Nylas Mail](https://en.wikipedia.org/wiki/Nylas_Mail)
- [Opera Mail](https://en.wikipedia.org/wiki/Opera_Mail)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Outlook Express](https://en.wikipedia.org/wiki/Outlook_Express)
- [Outlook for Windows](https://en.wikipedia.org/wiki/Outlook_for_Windows)
- [Mark P. McCahill](https://en.wikipedia.org/wiki/Mark_P._McCahill)
- [Pale Moon](https://en.wikipedia.org/wiki/Pale_Moon)
- [Pegasus Mail](https://en.wikipedia.org/wiki/Pegasus_Mail)
- [Pine (email client)](https://en.wikipedia.org/wiki/Pine_(email_client))
- [Pocomail](https://en.wikipedia.org/wiki/Pocomail)
- [Post Office Protocol](https://en.wikipedia.org/wiki/Post_Office_Protocol)
- [Postbox (email client)](https://en.wikipedia.org/wiki/Postbox_(email_client))
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Push-IMAP](https://en.wikipedia.org/wiki/Push-IMAP)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Roundcube](https://en.wikipedia.org/wiki/Roundcube)
- [Galaxy Store](https://en.wikipedia.org/wiki/Galaxy_Store)
- [Scribe Mail](https://en.wikipedia.org/wiki/Scribe_Mail)
- [SeaMonkey](https://en.wikipedia.org/wiki/SeaMonkey)
- [Simple Mail Access Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Access_Protocol)
- [Simple Mail Transfer Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Readdle](https://en.wikipedia.org/wiki/Readdle)
- [Sparrow (email client)](https://en.wikipedia.org/wiki/Sparrow_(email_client))
- [Spike (application)](https://en.wikipedia.org/wiki/Spike_(application))
- [SquirrelMail](https://en.wikipedia.org/wiki/SquirrelMail)
- [Sylpheed](https://en.wikipedia.org/wiki/Sylpheed)
- [TechRepublic](https://en.wikipedia.org/wiki/TechRepublic)
- [The Bat!](https://en.wikipedia.org/wiki/The_Bat!)
- [Tk (software)](https://en.wikipedia.org/wiki/Tk_(software))
- [TouchMail](https://en.wikipedia.org/wiki/TouchMail)
- [Trojitá](https://en.wikipedia.org/wiki/Trojit%C3%A1)
- [Turnpike (software)](https://en.wikipedia.org/wiki/Turnpike_(software))
- [UUCP](https://en.wikipedia.org/wiki/UUCP)
- [Unicode and email](https://en.wikipedia.org/wiki/Unicode_and_email)
- [Unix-like](https://en.wikipedia.org/wiki/Unix-like)
- [Utility software](https://en.wikipedia.org/wiki/Utility_software)
- [Vivaldi (web browser)](https://en.wikipedia.org/wiki/Vivaldi_(web_browser))
- [DR-WebSpyder](https://en.wikipedia.org/wiki/DR-WebSpyder)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Windows Live Mail](https://en.wikipedia.org/wiki/Windows_Live_Mail)
- [Windows Messaging](https://en.wikipedia.org/wiki/Windows_Messaging)
- [YAM (software)](https://en.wikipedia.org/wiki/YAM_(software))
- [Zimbra](https://en.wikipedia.org/wiki/Zimbra)
- [Template:Email clients](https://en.wikipedia.org/wiki/Template:Email_clients)
- [Template:Latest stable software release/OfflineIMAP](https://en.wikipedia.org/wiki/Template:Latest_stable_software_release/OfflineIMAP)
- [Template talk:Email clients](https://en.wikipedia.org/wiki/Template_talk:Email_clients)
- [Category:Email clients](https://en.wikipedia.org/wiki/Category:Email_clients)
- [Category:Use mdy dates from September 2012](https://en.wikipedia.org/wiki/Category:Use_mdy_dates_from_September_2012)
- [Portal:Free and open-source software](https://en.wikipedia.org/wiki/Portal:Free_and_open-source_software)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:40:27.578717+00:00_