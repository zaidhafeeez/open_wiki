# Shiny (web framework)

## Metadata
- **Last Updated:** 2024-12-03 08:00:59 UTC
- **Original Article:** [Shiny (web framework)](https://en.wikipedia.org/wiki/Shiny_(web_framework))
- **Language:** en
- **Page ID:** 70294421

## Summary
Shiny is a web framework for developing web applications (apps), originally in R and since 2022 in python. It is free and open source. It was announced by Joe Cheng, CTO of Posit, formerly RStudio, in 2012. One of the uses of Shiny has been in fast prototyping.
In 2022, a separate implementation Shiny for Python was announced. It is not meant to be a replacement, whereby both implementations will be developed concurrently and may never have all the features of each other. There is also Shinylive that allows running Shiny on the client (i.e., program code does not run on the server, reducing server load to just serving the code itself).

## Categories
This article belongs to the following categories:

- Category:Articles with short description
- Category:Business software
- Category:Free R (programming language) software
- Category:Free web development software
- Category:Official website not in Wikidata
- Category:Python (programming language) web frameworks
- Category:Short description matches Wikidata

## Table of Contents

- Features
- Examples
- Deploying / Hosting Shiny
- References
- External links

## Content

Shiny is a web framework for developing web applications (apps), originally in R and since 2022 in python. It is free and open source. It was announced by Joe Cheng, CTO of Posit, formerly RStudio, in 2012. One of the uses of Shiny has been in fast prototyping.
In 2022, a separate implementation Shiny for Python was announced. It is not meant to be a replacement, whereby both implementations will be developed concurrently and may never have all the features of each other. There is also Shinylive that allows running Shiny on the client (i.e., program code does not run on the server, reducing server load to just serving the code itself).

Features
Shiny creates a reactive context wherein the user specifies, through input variables, the circumstances under which computations are re-executed, or graphs (often visualizations) re-rendered; this occurs almost instantaneously. The input variables are evaluated via a user interface which allows the simple creation of widgets such as text boxes, radio buttons, and drop-down lists.
There are two main parts to a Shiny file, which may alternatively be stored in two separate files. One is designed to accommodate the user interface, the appearance of which is restricted by the default choices, though can be extended through various other R packages. The other is designed to accommodate the server computations and plot generating code, for which all the built-in facilities of R are available.

Examples
This is an example of a basic application in R where:

And the equivalent application written in python:

And shiny express for python:

Deploying / Hosting Shiny
Deploying Shiny (R) can be achieved through several popular methods:

Shiny Server (Open Source): This option allows on-premises hosting for Shiny applications, giving users control over server configurations without licensing costs. It’s ideal for organizations that want direct server access and control.
Posit Connect (formerly RStudio Connect): A commercial, on-premises solution offering advanced features like user authentication, scheduled reporting, and support for multiple content types, including Shiny applications and R Markdown.
shinyapps.io: A cloud-hosted service managed by Posit, providing easy deployment and scaling of Shiny apps without requiring server management. It’s user-friendly, ideal for small teams or solo developers. Hosting a Shiny app on a shinyapps.io server is free up to certain limits but paid tiers are relatively expensive compared to hosting on other cloud computing platforms.

References
External links
Official website
Joe Cheng | Keynote: The Past and Future of Shiny | RStudio (2022) (58:07)

## Archive Info
- **Archived on:** 2024-12-15 20:28:16 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 2665 bytes
- **Word Count:** 408 words
