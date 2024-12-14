# Common Gateway Interface

## Article Metadata

- **Last Updated:** 2024-12-14T19:35:10.983422+00:00
- **Original Article:** [Common Gateway Interface](https://en.wikipedia.org/wiki/Common_Gateway_Interface)
- **Language:** en
- **Page ID:** 7220

## Summary

In computing, Common Gateway Interface (CGI) is an interface specification that enables web servers to execute an external program to process HTTP or HTTPS user requests.
Such programs are often written in a scripting language and are commonly referred to as CGI scripts, but they may include compiled programs.
A typical use case occurs when a web user submits a web form on a web page that uses CGI. The form's data is sent to the web server within an HTTP request with a URL denoting a CGI script.

## Categories

- Category:All articles needing additional references
- Category:Articles needing additional references from August 2023
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Network protocols
- Category:Pages displaying short descriptions of redirect targets via Module:Annotated link
- Category:Pages displaying wikidata descriptions as a fallback via Module:Annotated link
- Category:Servers (computing)
- Category:Short description is different from Wikidata
- Category:Use dmy dates from April 2021
- Category:Web 1.0
- Category:Web technology

## Table of Contents

- History
- Purpose
- Deployment
- Uses
- Security
- Alternatives
- See also
- References
- External links

## Content

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

## Related Articles

### Internal Links

- [ActiveX](https://en.wikipedia.org/wiki/ActiveX)
- [Active Server Pages](https://en.wikipedia.org/wiki/Active_Server_Pages)
- [Ajax (programming)](https://en.wikipedia.org/wiki/Ajax_(programming))
- [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
- [Apache JServ Protocol](https://en.wikipedia.org/wiki/Apache_JServ_Protocol)
- [List of Apache modules](https://en.wikipedia.org/wiki/List_of_Apache_modules)
- [Application server](https://en.wikipedia.org/wiki/Application_server)
- [Ari Luotonen](https://en.wikipedia.org/wiki/Ari_Luotonen)
- [Asynchronous Server Gateway Interface](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [Browser Helper Object](https://en.wikipedia.org/wiki/Browser_Helper_Object)
- [Browser extension](https://en.wikipedia.org/wiki/Browser_extension)
- [C++](https://en.wikipedia.org/wiki/C%2B%2B)
- [CERN httpd](https://en.wikipedia.org/wiki/CERN_httpd)
- [CGI.pm](https://en.wikipedia.org/wiki/CGI.pm)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [C standard library](https://en.wikipedia.org/wiki/C_standard_library)
- [C (programming language)](https://en.wikipedia.org/wiki/C_(programming_language))
- [Canvas element](https://en.wikipedia.org/wiki/Canvas_element)
- [Client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
- [Client-side persistent data](https://en.wikipedia.org/wiki/Client-side_persistent_data)
- [Code injection](https://en.wikipedia.org/wiki/Code_injection)
- [Communication protocol](https://en.wikipedia.org/wiki/Communication_protocol)
- [Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Overhead (computing)](https://en.wikipedia.org/wiki/Overhead_(computing))
- [Process (computing)](https://en.wikipedia.org/wiki/Process_(computing))
- [Computing](https://en.wikipedia.org/wiki/Computing)
- [Cross-origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
- [Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)
- [DOM event](https://en.wikipedia.org/wiki/DOM_event)
- [Arachne (web browser)](https://en.wikipedia.org/wiki/Arachne_(web_browser))
- [Directory (computing)](https://en.wikipedia.org/wiki/Directory_(computing))
- [Document Object Model](https://en.wikipedia.org/wiki/Document_Object_Model)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Dynamic HTML](https://en.wikipedia.org/wiki/Dynamic_HTML)
- [Dynamic web page](https://en.wikipedia.org/wiki/Dynamic_web_page)
- [Encrypted Media Extensions](https://en.wikipedia.org/wiki/Encrypted_Media_Extensions)
- [Environment variable](https://en.wikipedia.org/wiki/Environment_variable)
- [Fully qualified domain name](https://en.wikipedia.org/wiki/Fully_qualified_domain_name)
- [FastCGI](https://en.wikipedia.org/wiki/FastCGI)
- [File system](https://en.wikipedia.org/wiki/File_system)
- [Filename extension](https://en.wikipedia.org/wiki/Filename_extension)
- [Frontend and backend](https://en.wikipedia.org/wiki/Frontend_and_backend)
- [Gateway (telecommunications)](https://en.wikipedia.org/wiki/Gateway_(telecommunications))
- [Gears (software)](https://en.wikipedia.org/wiki/Gears_(software))
- [Google Native Client](https://en.wikipedia.org/wiki/Google_Native_Client)
- [GraphQL](https://en.wikipedia.org/wiki/GraphQL)
- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [HTML5 File API](https://en.wikipedia.org/wiki/HTML5_File_API)
- [HTML audio](https://en.wikipedia.org/wiki/HTML_audio)
- [HTML video](https://en.wikipedia.org/wiki/HTML_video)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2)
- [HTTP/3](https://en.wikipedia.org/wiki/HTTP/3)
- [HTTPS](https://en.wikipedia.org/wiki/HTTPS)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [POST (HTTP)](https://en.wikipedia.org/wiki/POST_(HTTP))
- [HTTP cookie](https://en.wikipedia.org/wiki/HTTP_cookie)
- [HTTP handler](https://en.wikipedia.org/wiki/HTTP_handler)
- [HTTP message body](https://en.wikipedia.org/wiki/HTTP_message_body)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [HTTP](https://en.wikipedia.org/wiki/HTTP)
- [Hydration (web development)](https://en.wikipedia.org/wiki/Hydration_(web_development))
- [Internet Server Application Programming Interface](https://en.wikipedia.org/wiki/Internet_Server_Application_Programming_Interface)
- [Indexed Database API](https://en.wikipedia.org/wiki/Indexed_Database_API)
- [Internet Information Services](https://en.wikipedia.org/wiki/Internet_Information_Services)
- [Internet Server Application Programming Interface](https://en.wikipedia.org/wiki/Internet_Server_Application_Programming_Interface)
- [Language interpretation](https://en.wikipedia.org/wiki/Language_interpretation)
- [JSGI](https://en.wikipedia.org/wiki/JSGI)
- [Jakarta EE](https://en.wikipedia.org/wiki/Jakarta_EE)
- [Jakarta Servlet](https://en.wikipedia.org/wiki/Jakarta_Servlet)
- [Java Platform, Standard Edition](https://en.wikipedia.org/wiki/Java_Platform,_Standard_Edition)
- [Java Portlet Specification](https://en.wikipedia.org/wiki/Java_Portlet_Specification)
- [Ken Coar](https://en.wikipedia.org/wiki/Ken_Coar)
- [Khronos Group](https://en.wikipedia.org/wiki/Khronos_Group)
- [List of Apache modules](https://en.wikipedia.org/wiki/List_of_Apache_modules)
- [List of application servers](https://en.wikipedia.org/wiki/List_of_application_servers)
- [Machine code](https://en.wikipedia.org/wiki/Machine_code)
- [Mashup (web application hybrid)](https://en.wikipedia.org/wiki/Mashup_(web_application_hybrid))
- [Media Source Extensions](https://en.wikipedia.org/wiki/Media_Source_Extensions)
- [Microservices](https://en.wikipedia.org/wiki/Microservices)
- [List of Apache modules](https://en.wikipedia.org/wiki/List_of_Apache_modules)
- [Mod lisp](https://en.wikipedia.org/wiki/Mod_lisp)
- [Mod mono](https://en.wikipedia.org/wiki/Mod_mono)
- [Parrot virtual machine](https://en.wikipedia.org/wiki/Parrot_virtual_machine)
- [Mod perl](https://en.wikipedia.org/wiki/Mod_perl)
- [List of Apache modules](https://en.wikipedia.org/wiki/List_of_Apache_modules)
- [Mod proxy](https://en.wikipedia.org/wiki/Mod_proxy)
- [Mod python](https://en.wikipedia.org/wiki/Mod_python)
- [Mod ruby](https://en.wikipedia.org/wiki/Mod_ruby)
- [Mod wsgi](https://en.wikipedia.org/wiki/Mod_wsgi)
- [NCSA HTTPd](https://en.wikipedia.org/wiki/NCSA_HTTPd)
- [NPAPI](https://en.wikipedia.org/wiki/NPAPI)
- [National Center for Supercomputing Applications](https://en.wikipedia.org/wiki/National_Center_for_Supercomputing_Applications)
- [Netscape Server Application Programming Interface](https://en.wikipedia.org/wiki/Netscape_Server_Application_Programming_Interface)
- [Node.js](https://en.wikipedia.org/wiki/Node.js)
- [Open API](https://en.wikipedia.org/wiki/Open_API)
- [Open Web Interface for .NET](https://en.wikipedia.org/wiki/Open_Web_Interface_for_.NET)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [Plack (software)](https://en.wikipedia.org/wiki/Plack_(software))
- [Phusion Passenger](https://en.wikipedia.org/wiki/Phusion_Passenger)
- [Plack (software)](https://en.wikipedia.org/wiki/Plack_(software))
- [Plug-in (computing)](https://en.wikipedia.org/wiki/Plug-in_(computing))
- [Process (computing)](https://en.wikipedia.org/wiki/Process_(computing))
- [Progressive web app](https://en.wikipedia.org/wiki/Progressive_web_app)
- [Push technology](https://en.wikipedia.org/wiki/Push_technology)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Query string](https://en.wikipedia.org/wiki/Query_string)
- [REST](https://en.wikipedia.org/wiki/REST)
- [Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments)
- [Rack (web server interface)](https://en.wikipedia.org/wiki/Rack_(web_server_interface))
- [Remote scripting](https://en.wikipedia.org/wiki/Remote_scripting)
- [Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments)
- [Resource-oriented architecture](https://en.wikipedia.org/wiki/Resource-oriented_architecture)
- [Rich Internet Application](https://en.wikipedia.org/wiki/Rich_Internet_Application)
- [Robert McCool](https://en.wikipedia.org/wiki/Robert_McCool)
- [Robert McCool](https://en.wikipedia.org/wiki/Robert_McCool)
- [SVG](https://en.wikipedia.org/wiki/SVG)
- [Scripting language](https://en.wikipedia.org/wiki/Scripting_language)
- [Server-sent events](https://en.wikipedia.org/wiki/Server-sent_events)
- [Client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
- [Server-side scripting](https://en.wikipedia.org/wiki/Server-side_scripting)
- [Server Side Includes](https://en.wikipedia.org/wiki/Server_Side_Includes)
- [Server application programming interface](https://en.wikipedia.org/wiki/Server_application_programming_interface)
- [Simple Common Gateway Interface](https://en.wikipedia.org/wiki/Simple_Common_Gateway_Interface)
- [Single-page application](https://en.wikipedia.org/wiki/Single-page_application)
- [Software portability](https://en.wikipedia.org/wiki/Software_portability)
- [Solution stack](https://en.wikipedia.org/wiki/Solution_stack)
- [Standard streams](https://en.wikipedia.org/wiki/Standard_streams)
- [Standard streams](https://en.wikipedia.org/wiki/Standard_streams)
- [Static web page](https://en.wikipedia.org/wiki/Static_web_page)
- [Thread (computing)](https://en.wikipedia.org/wiki/Thread_(computing))
- [URL](https://en.wikipedia.org/wiki/URL)
- [UWSGI](https://en.wikipedia.org/wiki/UWSGI)
- [URL](https://en.wikipedia.org/wiki/URL)
- [W3C Geolocation API](https://en.wikipedia.org/wiki/W3C_Geolocation_API)
- [WHATWG](https://en.wikipedia.org/wiki/WHATWG)
- [Web-oriented architecture](https://en.wikipedia.org/wiki/Web-oriented_architecture)
- [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly)
- [WebAuthn](https://en.wikipedia.org/wiki/WebAuthn)
- [WebCL](https://en.wikipedia.org/wiki/WebCL)
- [WebDAV](https://en.wikipedia.org/wiki/WebDAV)
- [WebGL](https://en.wikipedia.org/wiki/WebGL)
- [WebGPU](https://en.wikipedia.org/wiki/WebGPU)
- [WebRTC](https://en.wikipedia.org/wiki/WebRTC)
- [WebSocket](https://en.wikipedia.org/wiki/WebSocket)
- [WebUSB](https://en.wikipedia.org/wiki/WebUSB)
- [WebXR](https://en.wikipedia.org/wiki/WebXR)
- [Web API](https://en.wikipedia.org/wiki/Web_API)
- [Web API security](https://en.wikipedia.org/wiki/Web_API_security)
- [Web IDL](https://en.wikipedia.org/wiki/Web_IDL)
- [Web Messaging](https://en.wikipedia.org/wiki/Web_Messaging)
- [Web SQL Database](https://en.wikipedia.org/wiki/Web_SQL_Database)
- [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [Web Services for Remote Portlets](https://en.wikipedia.org/wiki/Web_Services_for_Remote_Portlets)
- [Web application](https://en.wikipedia.org/wiki/Web_application)
- [Web container](https://en.wikipedia.org/wiki/Web_container)
- [HTML form](https://en.wikipedia.org/wiki/HTML_form)
- [Web framework](https://en.wikipedia.org/wiki/Web_framework)
- [Web page](https://en.wikipedia.org/wiki/Web_page)
- [Web resource](https://en.wikipedia.org/wiki/Web_resource)
- [Web server](https://en.wikipedia.org/wiki/Web_server)
- [Web service](https://en.wikipedia.org/wiki/Web_service)
- [Web standards](https://en.wikipedia.org/wiki/Web_standards)
- [Web storage](https://en.wikipedia.org/wiki/Web_storage)
- [Web worker](https://en.wikipedia.org/wiki/Web_worker)
- [Webhook](https://en.wikipedia.org/wiki/Webhook)
- [Webmaster](https://en.wikipedia.org/wiki/Webmaster)
- [Wiki](https://en.wikipedia.org/wiki/Wiki)
- [World Wide Web Consortium](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium)
- [XAML Browser Applications](https://en.wikipedia.org/wiki/XAML_Browser_Applications)
- [XMLHttpRequest](https://en.wikipedia.org/wiki/XMLHttpRequest)
- [Wikipedia:Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)
- [Template:Ref RFC/db/38](https://en.wikipedia.org/wiki/Template:Ref_RFC/db/38)
- [Template:Web interfaces](https://en.wikipedia.org/wiki/Template:Web_interfaces)
- [Template talk:Web interfaces](https://en.wikipedia.org/wiki/Template_talk:Web_interfaces)
- [Help:Authority control](https://en.wikipedia.org/wiki/Help:Authority_control)
- [Help:Maintenance template removal](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal)
- [Help:Referencing for beginners](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners)
- [Category:Articles needing additional references from August 2023](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_August_2023)
- [Category:Use dmy dates from April 2021](https://en.wikipedia.org/wiki/Category:Use_dmy_dates_from_April_2021)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-14T19:35:10.983422+00:00_