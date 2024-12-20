---
title: Common Gateway Interface
url: https://en.wikipedia.org/wiki/Common_Gateway_Interface
language: en
categories: ["Category:All articles needing additional references", "Category:Articles needing additional references from August 2023", "Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Network protocols", "Category:Pages displaying short descriptions of redirect targets via Module:Annotated link", "Category:Pages displaying wikidata descriptions as a fallback via Module:Annotated link", "Category:Servers (computing)", "Category:Short description is different from Wikidata", "Category:Use dmy dates from April 2021", "Category:Web 1.0", "Category:Web technology"]
references: 0
last_modified: 2024-12-19T13:42:03Z
---

# Common Gateway Interface

## Summary

In computing, Common Gateway Interface (CGI) is an interface specification that enables web servers to execute an external program to process HTTP or HTTPS user requests.
Such programs are often written in a scripting language and are commonly referred to as CGI scripts, but they may include compiled programs.
A typical use case occurs when a web user submits a web form on a web page that uses CGI. The form's data is sent to the web server within an HTTP request with a URL denoting a CGI script.

## Full Content

In computing, Common Gateway Interface (CGI) is an interface specification that enables web servers to execute an external program to process HTTP or HTTPS user requests.
Such programs are often written in a scripting language and are commonly referred to as CGI scripts, but they may include compiled programs.
A typical use case occurs when a web user submits a web form on a web page that uses CGI. The form's data is sent to the web server within an HTTP request with a URL denoting a CGI script. The web server then launches the CGI script in a new computer process, passing the form data to it. The CGI script passes its output, usually in the form of HTML, to the Web server, and the server relays it back to the browser as its response to the browser's request.
Developed in the early 1990s, CGI was the earliest common method available that allowed a web page to be interactive. Due to a necessity to run CGI scripts in a separate process every time the request comes in from a client, various alternatives were developed.

History
In 1993, the National Center for Supercomputing Applications (NCSA) team wrote the specification for calling command line executables on the www-talk mailing list. The other Web server developers adopted it, and it has been a standard for Web servers ever since. A work group chaired by Ken Coar started in November 1997 to get the NCSA definition of CGI more formally defined. This work resulted in RFC 3875, which specified CGI Version 1.1. Specifically mentioned in the RFC are the following contributors:

Rob McCool (author of the NCSA HTTPd Web server)
John Franks (author of the GN Web server)
Ari Luotonen (the developer of the CERN httpd Web server)
Tony Sanders (author of the Plexus Web server)
George Phillips (Web server maintainer at the University of British Columbia)
Historically CGI programs were often written using the C programming language. RFC 3875 "The Common Gateway Interface (CGI)" partially defines CGI using C, in saying that environment variables "are accessed by the C library routine getenv() or variable environ".
The name CGI comes from the early days of the Web, where webmasters wanted to connect legacy information systems such as databases to their Web servers. The CGI program was executed by the server and provided a common "gateway" between the Web server and the legacy information system.

Purpose
Traditionally a Web server has a directory which is designated as a document collection, that is, a set of files that can be sent to Web browsers connected to the server. For example, if a web server has the fully-qualified domain name www.example.com, and its document collection is stored at /usr/local/apache/htdocs/ in the local file system (its document root), then the web server will respond to a request for http://www.example.com/index.html by sending to the browser a copy of the file /usr/local/apache/htdocs/index.html (if it exists).
For pages constructed on the fly, the server software may defer requests to separate programs and relay the results to the requesting client (usually, a Web browser that displays the page to the end user).
Such programs usually require some additional information to be specified with the request, such as query strings or cookies. Conversely, upon returning, the script must provide all the information required by HTTP for a response to the request: the HTTP status of the request, the document content (if available), the document type (e.g. HTML, PDF, or plain text), et cetera.
Initially, there were no standardized methods for data exchange between a browser, the HTTP server with which it was communicating and the scripts on the server that were expected to process the data and ultimately return a result to the browser. As a result, mutual incompatibilities existed between different HTTP server variants that undermined script portability.
Recognition of this problem led to the specification of how data exchange was to be carried out, resulting in the development of CGI.  Web page-generating programs invoked by server software that adheres to the CGI specification are known as CGI scripts, even though they may actually have been written in a non-scripting language, such as C.
The CGI specification was quickly adopted and continues to be supported by all well-known HTTP server packages, such as Apache, Microsoft IIS, and (with an extension) Node.js-based servers.
An early use of CGI scripts was to process forms. In the beginning of HTML, HTML forms typically had an "action" attribute and a button designated as the "submit" button. When the submit button is pushed the URI specified in the "action" attribute would be sent to the server with the data from the form sent as a query string. If the "action" specifies a CGI script then the CGI script would be executed, the script in turn generating an HTML page.

Deployment
A Web server that supports CGI can be configured to interpret a URL that it serves as a reference to a CGI script. A common convention is to have a cgi-bin/ directory at the base of the directory tree and treat all executable files within this directory (and no other, for security) as CGI scripts. When a Web browser requests a URL that points to a file within the CGI directory (e.g., http://example.com/cgi-bin/printenv.pl/with/additional/path?and=a&query=string), then, instead of simply sending that file (/usr/local/apache/htdocs/cgi-bin/printenv.pl) to the Web browser, the HTTP server runs the specified script and passes the output of the script to the Web browser. That is, anything that the script sends to standard output is passed to the Web client instead of being shown in the terminal window that started the web server. Another popular convention is to use filename extensions; for instance, if CGI scripts are consistently given the extension .cgi, the Web server can be configured to interpret all such files as CGI scripts. While convenient, and required by many prepackaged scripts, it opens the server to attack if a remote user can upload executable code with the proper extension.
The CGI specification defines how additional information passed with the request is passed to the script. The Web server creates a subset of the environment variables passed to it and adds details pertinent to the HTTP environment. For instance, if a slash and additional directory name(s) are appended to the URL immediately after the name of the script (in this example, /with/additional/path), then that path is stored in the PATH_INFO environment variable before the script is called. If parameters are sent to the script via an HTTP GET request (a question mark appended to the URL, followed by param=value pairs; in the example, ?and=a&query=string), then those parameters are stored in the QUERY_STRING environment variable before the script is called. Request HTTP message body, such as form parameters sent via an HTTP POST request, are passed to the script's standard input. The script can then read these environment variables or data from standard input and adapt to the Web browser's request.

Uses
CGI is often used to process input information from the user and produce the appropriate output. An example of a CGI program is one implementing a wiki. If the user agent requests the name of an entry, the Web server executes the CGI program. The CGI program retrieves the source of that entry's page (if one exists), transforms it into HTML, and prints the result. The Web server receives the output from the CGI program and transmits it to the user agent. Then if the user agent clicks the "Edit page" button, the CGI program populates an HTML textarea or other editing control with the page's contents. Finally if the user agent clicks the "Publish page" button, the CGI program transforms the updated HTML into the source of that entry's page and saves it.

Security
CGI programs run, by default, in the security context of the Web server. When first introduced a number of example scripts were provided with the reference distributions of the NCSA, Apache and CERN Web servers to show how shell scripts or C programs could be coded to make use of the new CGI. One such example script was a CGI program called PHF that implemented a simple phone book.
In common with a number of other scripts at the time, this script made use of a function: escape_shell_cmd(). The function was supposed to sanitize its argument, which came from user input and then pass the input to the Unix shell, to be run in the security context of the Web server. The script did not correctly sanitize all input and allowed new lines to be passed to the shell, which effectively allowed multiple commands to be run. The results of these commands were then displayed on the Web server. If the security context of the Web server allowed it, malicious commands could be executed by attackers.
This was the first widespread example of a new type of Web-based attack called code injection, where unsanitized data from Web users could lead to execution of code on a Web server. Because the example code was installed by default, attacks were widespread and led to a number of security advisories in early 1996.

Alternatives
For each incoming HTTP request, a Web server creates a new CGI process for handling it and destroys the CGI process after the HTTP request has been handled. Creating and destroying a process can consume more CPU time and memory resources than the actual work of generating the output of the process, especially when the CGI program still needs to be interpreted by a virtual machine. For a high number of HTTP requests, the resulting workload can quickly overwhelm the Web server.
The computational overhead involved in CGI process creation and destruction can be reduced by the following techniques:

CGI programs precompiled to machine code, e.g. precompiled from C or C++ programs, rather than CGI programs executed by an interpreter, e.g. Perl, PHP or Python programs.
Web server extensions such as Apache modules (e.g. mod_perl, mod_php and mod_python), NSAPI plugins, and ISAPI plugins which allow long-running application processes handling more than one request and hosted within the Web server.
FastCGI, SCGI, and AJP which allow long-running application processes handling more than one request to be hosted externally; i.e., separately from the Web server. Each application process listens on a socket; the Web server handles an HTTP request and sends it via another protocol (FastCGI, SCGI or AJP) to the socket only for dynamic content, while static content is usually handled directly by the Web server. This approach needs fewer application processes so consumes less memory than the Web server extension approach. And unlike converting an application program to a Web server extension, FastCGI, SCGI, and AJP application programs remain independent of the Web server.
Jakarta EE runs Jakarta Servlet applications in a Web container to serve dynamic content and optionally static content which replaces the overhead of creating and destroying processes with the much lower overhead of creating and destroying threads. It also exposes the programmer to the library that comes with Java SE on which the version of Jakarta EE in use is based.
Standalone HTTP Server
Web Server Gateway Interface (WSGI) is a modern approach written in the Python programming language. It is defined by PEP 3333 and implemented via various methods like mod_wsgi (Apache module), Gunicorn web server (in between of Nginx & Scripts/Frameworks like Django), UWSGI, etc.
The optimal configuration for any Web application depends on application-specific details, amount of traffic, and complexity of the transaction; these trade-offs need to be analyzed to determine the best implementation for a given task and time budget. Web frameworks offer an alternative to using CGI scripts to interact with user agents.

See also
CGI.pm – Perl module for web applications
DOS Gateway Interface – Graphical web browser for DOS and LinuxPages displaying short descriptions of redirect targets
Perl Web Server Gateway Interface – web application frameworkPages displaying wikidata descriptions as a fallback
Rack (web server interface) – API specification for web applications in programming language Ruby
Server Side Includes – Interpreted server-side scripting language

References
External links
The Invention of CGI
RFC 3875 – The Common Gateway Interface (CGI) Version 1.1
CGI Programming 101: Learn CGI Today!, a CGI tutorial