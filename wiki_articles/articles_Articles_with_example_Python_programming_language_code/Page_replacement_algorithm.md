# Page replacement algorithm

## Metadata
- **Last Updated:** 2024-12-13 14:33:52 UTC
- **Original Article:** [Page replacement algorithm](https://en.wikipedia.org/wiki/Page_replacement_algorithm)
- **Language:** en
- **Page ID:** 727476

## Summary
In a computer operating system that uses paging for virtual memory management, page replacement algorithms decide which memory pages to page out, sometimes called swap out, or write to disk, when a page of memory needs to be allocated. Page replacement happens when a requested page is not in memory (page fault) and a free page cannot be used to satisfy the allocation, either because there are none, or because the number of free pages is lower than some threshold.
When the page that was selected for replacement and paged out is referenced again it has to be paged in (read in from disk), and this involves waiting for I/O completion. This determines the quality of the page replacement algorithm: the less time waiting for page-ins, the better the algorithm. A page replacement algorithm looks at the limited information about accesses to the pages provided by hardware, and tries to guess which pages should be replaced to minimize the total number of page misses, while balancing this with the costs (primary storage and processor time) of the algorithm itself.
The page replacing problem is a typical online problem from the competitive analysis perspective in the sense that the optimal deterministic algorithm is known.

## Categories
This article belongs to the following categories:

- Category:All Wikipedia articles needing clarification
- Category:All articles with unsourced statements
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Articles with unsourced statements from July 2022
- Category:Memory management algorithms
- Category:Online algorithms
- Category:Short description is different from Wikidata
- Category:Use dmy dates from February 2021
- Category:Virtual memory
- Category:Wikipedia articles needing clarification from August 2011
- Category:Wikipedia articles needing clarification from December 2015

## Table of Contents

- History
- Local vs. global replacement
- Detecting which pages are referenced and modified
- Precleaning
- The (h,k)-paging problem
- Marking algorithms
- Conservative algorithms
- Page replacement algorithms
- Implementation details
- Working set
- References

## Content

In a computer operating system that uses paging for virtual memory management, page replacement algorithms decide which memory pages to page out, sometimes called swap out, or write to disk, when a page of memory needs to be allocated. Page replacement happens when a requested page is not in memory (page fault) and a free page cannot be used to satisfy the allocation, either because there are none, or because the number of free pages is lower than some threshold.
When the page that was selected for replacement and paged out is referenced again it has to be paged in (read in from disk), and this involves waiting for I/O completion. This determines the quality of the page replacement algorithm: the less time waiting for page-ins, the better the algorithm. A page replacement algorithm looks at the limited information about accesses to the pages provided by hardware, and tries to guess which pages should be replaced to minimize the total number of page misses, while balancing this with the costs (primary storage and processor time) of the algorithm itself.
The page replacing problem is a typical online problem from the competitive analysis perspective in the sense that the optimal deterministic algorithm is known.

History
Page replacement algorithms were a hot topic of research and debate in the 1960s and 1970s.
That mostly ended with the development of sophisticated LRU (least recently used) approximations and working set algorithms. Since then, some basic assumptions made by the traditional page replacement algorithms were invalidated, resulting in a revival of research. In particular, the following trends in the behavior of underlying hardware and user-level software have affected the performance of page replacement algorithms:

Size of primary storage has increased by multiple orders of magnitude. With several gigabytes of primary memory, algorithms that require a periodic check of each and every memory frame are becoming less and less practical.
Memory hierarchies have grown taller. The cost of a CPU cache miss is far more expensive. This exacerbates the previous problem.
Locality of reference of user software has weakened. This is mostly attributed to the spread of object-oriented programming techniques that favor large numbers of small functions, use of sophisticated data structures like trees and hash tables that tend to result in chaotic memory reference patterns, and the advent of garbage collection that drastically changed memory access behavior of applications.
Requirements for page replacement algorithms have changed due to differences in operating system kernel architectures. In particular, most modern OS kernels have unified virtual memory and file system caches, requiring the page replacement algorithm to select a page from among the pages of both user program virtual address spaces and cached files. The latter pages have specific properties. For example, they can be locked, or can have write ordering requirements imposed by journaling. Moreover, as the goal of page replacement is to minimize total time waiting for memory, it has to take into account memory requirements imposed by other kernel sub-systems that allocate memory. As a result, page replacement in modern kernels (Linux, FreeBSD, and Solaris) tends to work at the level of a general purpose kernel memory allocator, rather than at the higher level of a virtual memory subsystem.

Local vs. global replacement
Replacement algorithms can be local or global.
When a process incurs a page fault, a local page replacement algorithm selects for replacement some page that belongs to that same process (or a group of processes sharing a memory partition).
A global replacement algorithm is free to select any page in memory.
Local page replacement assumes some form of memory partitioning that determines how many pages are to be assigned to a given process or a group of processes. Most popular forms of partitioning are fixed partitioning and balanced set algorithms based on the working set model. The advantage of local page replacement is its scalability: each process can handle its page faults independently, leading to more consistent performance for that process. However global page replacement is more efficient on an overall system basis.

Detecting which pages are referenced and modified
Modern general purpose computers and some embedded processors have support for virtual memory. Each process has its own virtual address space. A page table maps a subset of the process virtual addresses to physical addresses. In addition, in most architectures the page table holds an "access" bit and a "dirty" bit for each page in the page table. The CPU sets the access bit when the process reads or writes memory in that page. The CPU sets the dirty bit when the process writes memory in that page. The operating system can modify the access and dirty bits. The operating system can detect accesses to memory and files through the following means:

By clearing the access bit in pages present in the process' page table. After some time, the OS scans the page table looking for pages that had the access bit set by the CPU. This is fast because the access bit is set automatically by the CPU and inaccurate because the OS does not immediately receive notice of the access nor does it have information about the order in which the process accessed these pages.
By removing pages from the process' page table without necessarily removing them from physical memory. The next access to that page is detected immediately because it causes a page fault. This is slow because a page fault involves a context switch to the OS, software lookup for the corresponding physical address, modification of the page table and a context switch back to the process and accurate because the access is detected immediately after it occurs.
Directly when the process makes system calls that potentially access the page cache like read and write in POSIX.

Precleaning
Most replacement algorithms simply return the target page as their result. This means that if target page is dirty (that is, contains data that have to be written to the stable storage before page can be reclaimed), I/O has to be initiated to send that page to the stable storage (to clean the page). In the early days of virtual memory, time spent on cleaning was not of much concern, because virtual memory was first implemented on systems with full duplex channels to the stable storage, and cleaning was customarily overlapped with paging. Contemporary commodity hardware, on the other hand, does not support full duplex transfers, and cleaning of target pages becomes an issue.
To deal with this situation, various precleaning policies are implemented. Precleaning is the mechanism that starts I/O on dirty pages that are (likely) to be replaced soon. The idea is that by the time the precleaned page is actually selected for the replacement, the I/O will complete and the page will be clean. Precleaning assumes that it is possible to identify pages that will be replaced next. Precleaning that is too eager can waste I/O bandwidth by writing pages that manage to get re-dirtied before being selected for replacement.

The (h,k)-paging problem
The (h,k)-paging problem is a generalization of the model of paging problem: Let h,k be positive integers such that 
  
    
      
        h
        ≤
        k
      
    
    {\displaystyle h\leq k}
  
. We measure the performance of an algorithm with cache of size 
  
    
      
        h
        ≤
        k
      
    
    {\displaystyle h\leq k}
  
 relative to the theoretically optimal page replacement algorithm. If 
  
    
      
        h
        <
        k
      
    
    {\displaystyle h<k}
  
, we provide the optimal page replacement algorithm with strictly less resource.
The (h,k)-paging problem is a way to measure how an online algorithm performs by comparing it with the performance of the optimal algorithm, specifically, separately parameterizing the cache size of the online algorithm and optimal algorithm.

Marking algorithms
Marking algorithms is a general class of paging algorithms. For each page, we associate it with a bit called its mark. Initially, we set all pages as unmarked. During a stage (a period of operation or a sequence of requests) of page requests, we mark a page when it is first requested in this stage. A marking algorithm is such an algorithm that never pages out a marked page.
If ALG is a marking algorithm with a cache of size k, and OPT is the optimal algorithm with a cache of size h, where 
  
    
      
        h
        ≤
        k
      
    
    {\displaystyle h\leq k}
  
, then ALG is 
  
    
      
        
          
            
              k
              
                k
                −
                h
                +
                1
              
            
          
        
      
    
    {\displaystyle {\tfrac {k}{k-h+1}}}
  
-competitive. So every marking algorithm attains the 
  
    
      
        
          
            
              k
              
                k
                −
                h
                +
                1
              
            
          
        
      
    
    {\displaystyle {\tfrac {k}{k-h+1}}}
  
-competitive ratio.
LRU is a marking algorithm while FIFO is not a marking algorithm.

Conservative algorithms
An algorithm is conservative, if on any consecutive request sequence containing k or fewer distinct page references, the algorithm will incur k or fewer page faults.
If ALG is a conservative algorithm with a cache of size k, and OPT is the optimal algorithm with a cache of 
  
    
      
        h
        ≤
        k
      
    
    {\displaystyle h\leq k}
  
, then ALG is 
  
    
      
        
          
            
              k
              
                k
                −
                h
                +
                1
              
            
          
        
      
    
    {\displaystyle {\tfrac {k}{k-h+1}}}
  
-competitive. So every conservative algorithm attains the 
  
    
      
        
          
            
              k
              
                k
                −
                h
                +
                1
              
            
          
        
      
    
    {\displaystyle {\tfrac {k}{k-h+1}}}
  
-competitive ratio.
LRU, FIFO and CLOCK are conservative algorithms.

Page replacement algorithms
There are a variety of page replacement algorithms:

The theoretically optimal page replacement algorithm
The theoretically optimal page replacement algorithm (also known as OPT, clairvoyant replacement algorithm, or Bélády's optimal page replacement policy) is an algorithm that works as follows: when a page needs to be swapped in, the operating system swaps out the page whose next use will occur farthest in the future. For example, a page that is not going to be used for the next 6 seconds will be swapped out over a page that is going to be used within the next 0.4 seconds.
This algorithm cannot be implemented in a general purpose operating system because it is impossible to compute reliably how long it will be before a page is going to be used, except when all software that will run on a system is either known beforehand and is amenable to static analysis of its memory reference patterns, or only a class of applications allowing run-time analysis. Despite this limitation, algorithms exist that can offer near-optimal performance — the operating system keeps track of all pages referenced by the program, and it uses those data to decide which pages to swap in and out on subsequent runs. This algorithm can offer near-optimal performance, but not on the first run of a program, and only if the program's memory reference pattern is relatively consistent each time it runs.
Analysis of the paging problem has also been done in the field of online algorithms. Efficiency of randomized online algorithms for the paging problem is measured using amortized analysis.

Not recently used
The not recently used (NRU) page replacement algorithm is an algorithm that favours keeping pages in memory that have been recently used. This algorithm works on the following principle: when a page is referenced, a referenced bit is set for that page, marking it as referenced. Similarly, when a page is modified (written to), a modified bit is set. The setting of the bits is usually done by the hardware, although it is possible to do so on the software level as well.
At a certain fixed time interval, a timer interrupt triggers and clears the referenced bit of all the pages, so only pages referenced within the current timer interval are marked with a referenced bit. When a page needs to be replaced, the operating system divides the pages into four classes:

3. referenced, modified
2. referenced, not modified
1. not referenced, modified
0. not referenced, not modified
Although it does not seem possible for a page to be modified yet not referenced, this happens when a class 3 page has its referenced bit cleared by the timer interrupt. The NRU algorithm picks a random page from the lowest category for removal. So out of the above four page categories, the NRU algorithm will replace a not-referenced, not-modified page if such a page exists. Note that this algorithm implies that a modified but not-referenced (within the last timer interval) page is less important than a not-modified page that is intensely referenced.
NRU is a marking algorithm, so it is 
  
    
      
        
          
            
              k
              
                k
                −
                h
                +
                1
              
            
          
        
      
    
    {\displaystyle {\tfrac {k}{k-h+1}}}
  
-competitive.

First-in, first-out
The simplest page-replacement algorithm is a FIFO algorithm. The first-in, first-out (FIFO) page replacement algorithm is a low-overhead algorithm that requires little bookkeeping on the part of the operating system. The idea is obvious from the name – the operating system keeps track of all the pages in memory in a queue, with the most recent arrival at the back, and the oldest arrival in front. When a page needs to be replaced, the page at the front of the queue (the oldest page) is selected. While FIFO is cheap and intuitive, it performs poorly in practical application. Thus, it is rarely used in its unmodified form. This algorithm experiences Bélády's anomaly.
In simple words, on a page fault, the frame that has been in memory the longest is replaced.
FIFO page replacement algorithm is used by the OpenVMS operating system, with some modifications. Partial second chance is provided by skipping a limited number of entries with valid translation table references, and additionally, pages are displaced from process working set to a systemwide pool from which they can be recovered if not already re-used.
FIFO is a conservative algorithm, so it is 
  
    
      
        
          
            
              k
              
                k
                −
                h
                +
                1
              
            
          
        
      
    
    {\displaystyle {\tfrac {k}{k-h+1}}}
  
-competitive.

Second-chance
A modified form of the FIFO page replacement algorithm, known as the Second-chance page replacement algorithm, fares relatively better than FIFO at little cost for the improvement. It works by looking at the front of the queue as FIFO does, but instead of immediately paging out that page, it checks to see if its referenced bit is set. If it is not set, the page is swapped out. Otherwise, the referenced bit is cleared, the page is inserted at the back of the queue (as if it were a new page) and this process is repeated. This can also be thought of as a circular queue. If all the pages have their referenced bit set, on the second encounter of the first page in the list, that page will be swapped out, as it now has its referenced bit cleared. If all the pages have their reference bit cleared, then second chance algorithm degenerates into pure FIFO.
As its name suggests, Second-chance gives every page a "second-chance" – an old page that has been referenced is probably in use, and should not be swapped out over a new page that has not been referenced.

Clock
Clock is a more efficient version of FIFO than Second-chance because pages don't have to be constantly pushed to the back of the list, but it performs the same general function as Second-Chance. The clock algorithm keeps a circular list of pages in memory, with the "hand" (iterator) pointing to the last examined page frame in the list. When a page fault occurs and no empty frames exist, then the R (referenced) bit is inspected at the hand's location. If R is 0, the new page is put in place of the page the "hand" points to, and the hand is advanced one position. Otherwise, the R bit is cleared, then the clock hand is incremented and the process is repeated until a page is replaced. This algorithm was first described in 1969 by Fernando J. Corbató.

Variants of clock
GCLOCK: Generalized clock page replacement algorithm.
Clock-Pro keeps a circular list of information about recently referenced pages, including all M pages in memory as well as the most recent M pages that have been paged out. This extra information on paged-out pages, like the similar information maintained by ARC, helps it work better than LRU on large loops and one-time scans.
WSclock. By combining the Clock algorithm with the concept of a working set (i.e., the set of pages expected to be used by that process during some time interval), the performance of the algorithm can be improved. In practice, the "aging" algorithm and the "WSClock" algorithm are probably the most important page replacement algorithms.
Clock with Adaptive Replacement (CAR) is a page replacement algorithm that has performance comparable to ARC, and substantially outperforms both LRU and CLOCK. The algorithm CAR is self-tuning and requires no user-specified magic parameters.
CLOCK is a conservative algorithm, so it is 
  
    
      
        
          
            
              k
              
                k
                −
                h
                +
                1
              
            
          
        
      
    
    {\displaystyle {\tfrac {k}{k-h+1}}}
  
-competitive.

Least recently used
The least recently used (LRU) page replacement algorithm, though similar in name to NRU, differs in the fact that LRU keeps track of page usage over a short period of time, while NRU just looks at the usage in the last clock interval. LRU works on the idea that pages that have been most heavily used in the past few instructions are most likely to be used heavily in the next few instructions too. While LRU can provide near-optimal performance in theory (almost as good as adaptive replacement cache), it is rather expensive to implement in practice. There are a few implementation methods for this algorithm that try to reduce the cost yet keep as much of the performance as possible.
The most expensive method is the linked list method, which uses a linked list containing all the pages in memory. At the back of this list is the least recently used page, and at the front is the most recently used page. The cost of this implementation lies in the fact that items in the list will have to be moved about every memory reference, which is a very time-consuming process.
Another method that requires hardware support is as follows: suppose the hardware has a 64-bit counter that is incremented at every instruction. Whenever a page is accessed, it acquires the value equal to the counter at the time of page access. Whenever a page needs to be replaced, the operating system selects the page with the lowest counter and swaps it out.
Because of implementation costs, one may consider algorithms (like those that follow) that are similar to LRU, but which offer cheaper implementations.
One important advantage of the LRU algorithm is that it is amenable to full statistical analysis. It has been proven, for example, that LRU can never result in more than N-times more page faults than OPT algorithm, where N is proportional to the number of pages in the managed pool.
On the other hand, LRU's weakness is that its performance tends to degenerate under many quite common reference patterns. For example, if there are N pages in the LRU pool, an application executing a loop over array of N + 1 pages will cause a page fault on each and every access. As loops over large arrays are common, much effort has been put into modifying LRU to work better in such situations. Many of the proposed LRU modifications try to detect looping reference patterns and to switch into suitable replacement algorithm, like Most Recently Used (MRU).

Variants on LRU
LRU-K evicts the page whose K-th most recent access is furthest in the past. For example, LRU-1 is simply LRU whereas LRU-2 evicts pages according to the time of their penultimate access. LRU-K improves greatly on LRU with regards to locality in time.
The ARC algorithm extends LRU by maintaining a history of recently evicted pages and uses this to change preference to recent or frequent access. It is particularly resistant to sequential scans.
The 2Q algorithm improves upon the LRU and LRU/2 algorithm. By having two queues, one for hot-path items and the other for slow-path items, items are first placed in the slow-path queue and after a second access of the items placed in the hot-path items. Because references to added items are longer hold than in the LRU and LRU/2 algorithm, it has a better hot-path queue which improves the hit rate of the cache.
A comparison of ARC with other algorithms (LRU, MQ, 2Q, LRU-2, LRFU, LIRS) can be found in Megiddo & Modha 2004.
LRU is a marking algorithm, so it is 
  
    
      
        
          
            
              k
              
                k
                −
                h
                +
                1
              
            
          
        
      
    
    {\displaystyle {\tfrac {k}{k-h+1}}}
  
-competitive.

Random
Random replacement algorithm replaces a random page in memory. This eliminates the overhead cost of tracking page references. Usually it fares better than FIFO, and for looping memory references it is better than LRU, although generally LRU performs better in practice. OS/390 uses global LRU approximation and falls back to random replacement when LRU performance degenerates, and the Intel i860 processor used a random replacement policy (Rhodehamel 1989).

Not frequently used (NFU)
The not frequently used (NFU) page replacement algorithm requires a counter, and every page has one counter of its own which is initially set to 0. At each clock interval, all pages that have been referenced within that interval will have their counter incremented by 1. In effect, the counters keep track of how frequently a page has been used. Thus, the page with the lowest counter can be swapped out when necessary.
The main problem with NFU is that it keeps track of the frequency of use without regard to the time span of use. Thus, in a multi-pass compiler, pages which were heavily used during the first pass, but are not needed in the second pass will be favoured over pages which are comparably lightly used in the second pass, as they have higher frequency counters. This results in poor performance. Other common scenarios exist where NFU will perform similarly, such as an OS boot-up. Thankfully, a similar and better algorithm exists, and its description follows.
The not frequently used page-replacement algorithm generates fewer page faults than the least recently used page replacement algorithm when the page table contains null pointer values.

Aging
The aging algorithm is a descendant of the NFU algorithm, with modifications to make it aware of the time span of use. Instead of just incrementing the counters of pages referenced, putting equal emphasis on page references regardless of the time, the reference counter on a page is first shifted right (divided by 2), before adding the referenced bit to the left of that binary number. For instance, if a page has referenced bits 1,0,0,1,1,0 in the past 6 clock ticks, its referenced counter will look like this in chronological order: 10000000, 01000000, 00100000, 10010000, 11001000, 01100100. Page references closer to the present time have more impact than page references long ago. This ensures that pages referenced more recently, though less frequently referenced, will have higher priority over pages more frequently referenced in the past. Thus, when a page needs to be swapped out, the page with the lowest counter will be chosen.
The following Python code simulates the aging algorithm.
Counters 
  
    
      
        
          V
          
            i
          
        
      
    
    {\displaystyle V_{i}}
  
 are initialized with 0 and updated as described above via 
  
    
      
        
          V
          
            i
          
        
        ←
        (
        
          R
          
            i
          
        
        ≪
        (
        k
        −
        1
        )
        )
        
          |
        
        (
        
          V
          
            i
          
        
        ≫
        1
        )
      
    
    {\displaystyle V_{i}\leftarrow (R_{i}\ll (k-1))|(V_{i}\gg 1)}
  
, using arithmetic shift operators.

In the given example of R-bits for 6 pages over 5 clock ticks, the function prints the following output, which lists the R-bits for each clock tick t and the individual counter values 
  
    
      
        
          V
          
            i
          
        
      
    
    {\displaystyle V_{i}}
  
 for each page in binary representation.

Note that aging differs from LRU in the sense that aging can only keep track of the references in the latest 16/32 (depending on the bit size of the processor's integers) time intervals. Consequently, two pages may have referenced counters of 00000000, even though one page was referenced 9 intervals ago and the other 1000 intervals ago. Generally speaking, knowing the usage within the past 16 intervals is sufficient for making a good decision as to which page to swap out. Thus, aging can offer near-optimal performance for a moderate price.

Longest distance first (LDF) page replacement algorithm
The basic idea behind this algorithm is Locality of Reference as used in LRU but the difference is that in LDF, locality is based on distance not on the used references. In the LDF, replace the page which is on longest distance from the current page. If two pages are on same distance then the page which is next to current page in anti-clock rotation will get replaced.

Implementation details
Techniques for hardware with no reference bit
Many of the techniques discussed above assume the presence of a reference bit associated with each page.  Some hardware has no such bit, so its efficient use requires techniques that operate well without one.
One notable example is VAX hardware running OpenVMS. This system knows if a page has been modified, but not necessarily if a page has been read. Its approach is known as Secondary Page Caching. Pages removed from working sets (process-private memory, generally) are placed on special-purpose lists while remaining in physical memory for some time. Removing a page from a working set is not technically a page-replacement operation, but effectively identifies that page as a candidate. A page whose backing store is still valid (whose contents are not dirty, or otherwise do not need to be preserved) is placed on the tail of the Free Page List. A page that requires writing to backing store will be placed on the Modified Page List. These actions are typically triggered when the size of the Free Page List falls below an adjustable threshold.
Pages may be selected for working set removal in an essentially random fashion, with the expectation that if a poor choice is made, a future reference may retrieve that page from the Free or Modified list before it is removed from physical memory. A page referenced this way will be removed from the Free or Modified list and placed back into a process working set. The Modified Page List additionally provides an opportunity to write pages out to backing store in groups of more than one page, increasing efficiency. These pages can then be placed on the Free Page List. The sequence of pages that works its way to the head of the Free Page List resembles the results of a LRU or NRU mechanism and the overall effect has similarities to the Second-Chance algorithm described earlier.
Another example is used by the Linux kernel on ARM. The lack of hardware functionality is made up for by providing two page tables – the processor-native page tables, with neither referenced bits nor dirty bits, and software-maintained page tables with the required bits present. The emulated bits in the software-maintained table are set by page faults. In order to get the page faults, clearing emulated bits in the second table revokes some of the access rights to the corresponding page, which is implemented by altering the native table.

Page cache in Linux
Linux uses a unified page cache for

brk and anonymous mmaped-regions. This includes the heap and stack of user-space programs. It is written to swap when paged out.
Non-anonymous (file-backed) mmaped regions. If present in memory and not privately modified the physical page is shared with file cache or buffer.
Shared memory acquired through shm_open.
The tmpfs in-memory filesystem; written to swap when paged out.
The file cache including; written to the underlying block storage (possibly going through the buffer, see below) when paged out.
The cache of block devices, called the "buffer" by Linux (not to be confused with other structures also called buffers like those use for pipes and buffers used internally in Linux); written to the underlying storage when paged out.
The unified page cache operates on units of the smallest page size supported by the CPU (4 KiB in ARMv8, x86 and x86-64) with some pages of the next larger size (2 MiB in x86-64) called "huge pages" by Linux. The pages in the page cache are divided in an "active" set and an "inactive" set. Both sets keep a LRU list of pages. In the basic case, when a page is accessed by a user-space program it is put in the head of the inactive set. When it is accessed repeatedly, it is moved to the active list. Linux moves the pages from the active set to the inactive set as needed so that the active set is smaller than the inactive set. When a page is moved to the inactive set it is removed from the page table of any process address space, without being paged out of physical memory. When a page is removed from the inactive set, it is paged out of physical memory. The size of the "active" and "inactive" list can be queried from /proc/meminfo in the fields "Active", "Inactive", "Active(anon)", "Inactive(anon)", "Active(file)" and "Inactive(file)".

Working set
The working set of a process is the set of pages expected to be used by that process during some time interval.
The "working set model" isn't a page replacement algorithm in the strict sense (it's actually a kind of medium-term scheduler)

References


== Further reading ==

## Archive Info
- **Archived on:** 2024-12-15 20:38:37 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 31526 bytes
- **Word Count:** 4822 words
