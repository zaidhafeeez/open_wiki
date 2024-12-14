# Baidu Maps

_Last updated: 2024-12-14T15:09:14.809358_

**Original Article:** [Baidu Maps](https://en.wikipedia.org/wiki/Baidu_Maps)

**Summary:** Baidu Maps is a desktop and mobile web mapping service application and technology provided by Baidu, offering satellite imagery, street maps, street view (which is called "Panorama" – zh:百度全景) and indoor view perspectives, as well as functions such as a route planner for traveling by foot, car, or with public transport. Android and iOS applications are available.
Baidu Maps is available only in the Chinese language and, before 2016, it offered only maps of mainland China, Hong Kong, Macau and Ta

## Categories
- Category:All articles needing additional references
- Category:All articles with unsourced statements
- Category:Articles needing additional references from November 2024
- Category:Articles needing translation from Chinese Wikipedia
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from October 2020
- Category:Baidu
- Category:CS1 Chinese-language sources (zh)
- Category:Internet censorship in India
- Category:Internet properties established in 2005
- Category:Short description is different from Wikidata
- Category:Street view services
- Category:Web mapping

## Content

Baidu Maps is a desktop and mobile web mapping service application and technology provided by Baidu, offering satellite imagery, street maps, street view (which is called "Panorama" – zh:百度全景) and indoor view perspectives, as well as functions such as a route planner for traveling by foot, car, or with public transport. Android and iOS applications are available.
Baidu Maps is available only in the Chinese language and, before 2016, it offered only maps of mainland China, Hong Kong, Macau and Taiwan, with the rest of the world appearing unexplored. Currently, Baidu Maps also offers maps of various other countries. It was reported that more than 150 countries would be supported by the end of 2016. Baidu uses map data supplied by NavInfo, MapKing, Here, LocalKing and OpenStreetMap.
In 2016, it was reported that Baidu Maps had over 348 million monthly active users.

Countries and territories supported
Within Mainland China
Mainland China

Outside Mainland China
History
On September 30, 2005, Baidu Maps was released.
In 2010, Baidu added a detailed three-dimensional view for select cities, which has been described as being SimCity-like. The feature is licensed from the digital mapping service Edushi. Cities covered include Beijing, Shanghai, Guangzhou and Shenzhen. In November 2011, Baidu launched satellite imagery for the Greater China region with better resolution than Google Maps. City-level only includes Beijing, Shanghai, Guangzhou, Shenzhen, Hong Kong, Macao and other major cities.
On September 3, 2012, at its annual Baidu World event, Baidu revealed 360-degree digital imagery for select buildings.
On August 21, 2013, Baidu Maps launched the Baidu Panoramic Map and announced the upgrade of its location-based services business. According to Silicon Valley Power, Shen Li, head of Baidu’s LBS business unit, states that Baidu Maps' users have exceeded 200 million.

Coordinate system
Baidu Maps uses a variant of web Mercator projection for slicing map data into tiles, with distances expressed in degrees. It is associated with an underlying latitude-longitude reference. The reference uses the BD-09 coordinate system, which adds further obfuscation to the already obscure national standard in China, GCJ-02 (which in turn is defined in terms of the de facto standard around the world, WGS 84). Baidu alleges that adopting BD-09 "protects users' privacy".
The Baidu Maps API documentation specifies that "real" (WGS 84) GPS coordinates must be converted via a coordinate conversion interface. An HTTP interface, JavaScript API, Android SDK, and iOS SDK are available.
The JavaScript coordinate conversion API is demonstrated online by Baidu, but without any reverse (to GCJ-02) conversion capabilities. Open source implementations in R and various other languages exist, implemented in a manner much like the reverse GCJ-02 algorithm.
BD-09's latitude-longitude coordinates are derived by scrambling a polar version of GCJ-02 coordinates and adding a fixed offset:

Street view service
The street view service of Baidu Maps was first launched on August 21, 2013. This is a list of cities supported as of March 11, 2015:

Blocking
India
In June 2020, the Indian Government blocked Baidu Maps as well as 58 other Chinese apps, citing national security concerns during the clashes between the People's Liberation Army Ground Force and the Indian Army in the Galwan Valley.

References
External links
Baidu Maps
Baidu Map API example plotting markers with WGS-84, GCJ-02 and BD-09 coordinates