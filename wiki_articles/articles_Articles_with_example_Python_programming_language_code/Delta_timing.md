# Delta timing

## Metadata
- **Last Updated:** 2024-12-03 07:24:46 UTC
- **Original Article:** [Delta timing](https://en.wikipedia.org/wiki/Delta_timing)
- **Language:** en
- **Page ID:** 25586985

## Summary
Delta time or delta timing is a concept used amongst programmers in relation to hardware and network responsiveness. In graphics programming, the term is usually used for variably updating scenery based on the elapsed time since the game last updated, (i.e. the previous "frame") which will vary depending on the speed of the computer, and how much work needs to be done in the program at any given time.  This also allows graphics to be calculated separately if graphics are being multi-threaded.
In network programming, due to the unpredictable nature of internet connections, delta timing is used in a similar way to variably update the movement information received via the computer network, regardless of how long it took to receive the next data packet of movement information.
It is often done by calling a timer every frame per second that holds the time between now and last call. Thereafter the resulting number (delta time) is used to calculate how far, for instance, a video game character would have travelled during that time.  This results in the character taking the same amount of real world time to move across the screen regardless of the rate of update, and whether the delay is caused by lack of processing power or a slow internet connection.
In graphics programming, this avoids the gameplay slowing down or speeding up depending on the complexity of what is happening at any given time, which would make for an inconsistent, jarring experience (e.g. time slowing down the more characters walk onto the screen, or running too fast because only one character is on screen).  In network programming, this keeps the game world of each computer in sync with the others, by making sure each client eventually sees the same activity at the same time, even if more time has passed since the last update for some clients than others.
Big enough delays will eventually negatively affect the gameplay experience, but using Delta Time keeps the gameplay consistent so long as the computer and internet connection meet the minimum hardware requirements of the game.

## Categories
This article belongs to the following categories:

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Graphics
- Category:Short description matches Wikidata
- Category:Video game development

## Table of Contents

- Delta-timing measurement in programming
- Delta-time and frame rate
- When to use delta-time
- See also

## Content

Delta time or delta timing is a concept used amongst programmers in relation to hardware and network responsiveness. In graphics programming, the term is usually used for variably updating scenery based on the elapsed time since the game last updated, (i.e. the previous "frame") which will vary depending on the speed of the computer, and how much work needs to be done in the program at any given time.  This also allows graphics to be calculated separately if graphics are being multi-threaded.
In network programming, due to the unpredictable nature of internet connections, delta timing is used in a similar way to variably update the movement information received via the computer network, regardless of how long it took to receive the next data packet of movement information.
It is often done by calling a timer every frame per second that holds the time between now and last call. Thereafter the resulting number (delta time) is used to calculate how far, for instance, a video game character would have travelled during that time.  This results in the character taking the same amount of real world time to move across the screen regardless of the rate of update, and whether the delay is caused by lack of processing power or a slow internet connection.
In graphics programming, this avoids the gameplay slowing down or speeding up depending on the complexity of what is happening at any given time, which would make for an inconsistent, jarring experience (e.g. time slowing down the more characters walk onto the screen, or running too fast because only one character is on screen).  In network programming, this keeps the game world of each computer in sync with the others, by making sure each client eventually sees the same activity at the same time, even if more time has passed since the last update for some clients than others.
Big enough delays will eventually negatively affect the gameplay experience, but using Delta Time keeps the gameplay consistent so long as the computer and internet connection meet the minimum hardware requirements of the game.

Delta-timing measurement in programming
Delta time can be used to measure how long a given program took to execute in real-time. The python snippet below shows how an example function's execution time can be calculated using the delta of times before and after execution.

Python
Delta-time and frame rate
Delta-time and frame rate are not always related. Video games fall into one of two categories regarding frame rate: frame rate dependent or frame rate independent. Frame rate Dependent games have a frame rate that varies based on the computer running the software. For example, if a frame rate dependent game runs at 300 frames per second (fps) on a computer with a refresh rate of 120 hertz (Hz), then it would run at 150 fps on a computer with a refresh rate of 60 Hz. A standard delta-time expression can create pause screens and intentional slow-motion effects in frame rate-dependent games. Standard delta-time formulas are seldom used for standard game-play because the delta-time between frames varies greatly depending on the refresh rate of the computer on which it is running.
If a game is frame rate independent, the frame rate is preset and runs identically across all computers regardless of their specifications. Frame rate independence limits the maximum graphics quality to make the game available to more consumers. Frame rate independence is particularly popular in mobile games and games optimized for lower-end computers such as Chromebooks. In frame rate independent games, the delta-time between frames is consistent across the entire game. This standardization means that one delta-time expression can create a consistent frame rate for all users on all types of computers.

When to use delta-time
Delta-timing can excel anytime a game's frame rate needs to be independent of its hardware. One example of this could be games that need to run on mobile devices or low-end computers. In some cases, video game developers use delta-timing to standardize the movement speed of an object on the screen. For example, if a character moves across the screen at a constant rate, delta-timing can ensure that this movement speed is consistent and does not fluctuate. Using delta-timing for movement is particularly useful for users who possess inconsistent internet or low-end computer hardware. This method can also regulate the movement of on-screen objects.
One disadvantage of using delta-timing for movement is that it can be complicated for games that incorporate a wide variety of movements and movement speeds. For example, a game could have a specified walking speed and sprinting speed for all characters; however, characters may also drive cars, boats, planes, and other vehicles. If the developer wants each of these movement speeds to be different (to make the game as realistic as possible), they would need a separate delta-time expression for each movement speed (that is only assuming these movements occur at a constant rate). If the movements do not occur at a constant rate, delta-timing expressions are rendered ineffective.

See also
Latency (engineering)


== References ==

## Archive Info
- **Archived on:** 2024-12-15 15:18:25 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 5193 bytes
- **Word Count:** 841 words
