# Rendezvous hashing

## Metadata
- **Last Updated:** 2024-12-03 07:37:41 UTC
- **Original Article:** [Rendezvous hashing](https://en.wikipedia.org/wiki/Rendezvous_hashing)
- **Language:** en
- **Page ID:** 40543215

## Summary
Rendezvous or highest random weight (HRW) hashing is an algorithm that allows clients to achieve distributed agreement on a set of 
  
    
      
        k
      
    
    {\displaystyle k}
  
 options out of a possible set of 
  
    
      
        n
      
    
    {\displaystyle n}
  
 options. A typical application is when clients need to agree on which sites (or proxies) objects are assigned to.
Consistent hashing addresses the special case  
  
    
      
        k
        =
        1
      
    
    {\displaystyle k=1}
  
 using a different method. Rendezvous hashing is both much simpler and more general than consistent hashing (see below).

## Categories
This article belongs to the following categories:

- Category:Algorithms
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:CS1 errors: missing periodical
- Category:Hashing
- Category:Short description matches Wikidata

## Table of Contents

- History
- Problem definition and approach
- O(log n) running time via skeleton-based hierarchical rendezvous hashing
- Comparison with consistent hashing
- Weighted variations
- Systems using Rendezvous hashing
- Implementation
- References
- External links

## Content

Rendezvous or highest random weight (HRW) hashing is an algorithm that allows clients to achieve distributed agreement on a set of 
  
    
      
        k
      
    
    {\displaystyle k}
  
 options out of a possible set of 
  
    
      
        n
      
    
    {\displaystyle n}
  
 options. A typical application is when clients need to agree on which sites (or proxies) objects are assigned to.
Consistent hashing addresses the special case  
  
    
      
        k
        =
        1
      
    
    {\displaystyle k=1}
  
 using a different method. Rendezvous hashing is both much simpler and more general than consistent hashing (see below).

History
Rendezvous hashing was invented  by David Thaler and Chinya Ravishankar at the University of Michigan in 1996. Consistent hashing appeared a year later in the literature.
Given its simplicity and generality, rendezvous hashing is now being preferred to consistent hashing in real-world applications.  Rendezvous hashing was used very early on in many applications including mobile caching, router design, secure key establishment, and sharding and distributed databases. Other examples of real-world systems that use Rendezvous Hashing include the Github load balancer, the Apache Ignite distributed database, the Tahoe-LAFS file store, the CoBlitz large-file distribution service, Apache Druid, IBM's Cloud Object Store, the Arvados Data Management System, Apache Kafka, and the Twitter EventBus pub/sub platform.
One of the first applications of rendezvous hashing was to enable multicast clients on the Internet (in contexts such as the MBONE) to identify multicast rendezvous points in a distributed fashion. It was used in 1998 by Microsoft's Cache Array Routing Protocol (CARP) for distributed cache coordination and routing. Some Protocol Independent Multicast routing protocols use rendezvous hashing to pick a rendezvous point.

Problem definition and approach
Algorithm
Rendezvous hashing solves a general version of the distributed hash table problem: We are given a set of 
  
    
      
        n
      
    
    {\displaystyle n}
  
 sites (servers or proxies, say). How can any set of clients, given an object 
  
    
      
        O
      
    
    {\displaystyle O}
  
, agree on a k-subset of sites to assign to 
  
    
      
        O
      
    
    {\displaystyle O}
  
? The standard version of the problem uses k = 1. Each client is to make its selection independently, but all clients must end up picking the same subset of sites. This is non-trivial if we add a minimal disruption constraint, and require that when a site fails or is removed, only objects mapping to that site need be reassigned to other sites.
The basic idea is to give each site 
  
    
      
        
          S
          
            j
          
        
      
    
    {\displaystyle S_{j}}
  
 a score (a weight) for each object 
  
    
      
        
          O
          
            i
          
        
      
    
    {\displaystyle O_{i}}
  
, and assign the object to the highest scoring site. All clients first agree on a hash function 
  
    
      
        h
        (
        ⋅
        )
      
    
    {\displaystyle h(\cdot )}
  
. For object 
  
    
      
        
          O
          
            i
          
        
      
    
    {\displaystyle O_{i}}
  
, the site 
  
    
      
        
          S
          
            j
          
        
      
    
    {\displaystyle S_{j}}
  
 is defined to have weight 
  
    
      
        
          w
          
            i
            ,
            j
          
        
        =
        h
        (
        
          O
          
            i
          
        
        ,
        
          S
          
            j
          
        
        )
      
    
    {\displaystyle w_{i,j}=h(O_{i},S_{j})}
  
. Each client independently computes these weights 
  
    
      
        
          w
          
            i
            ,
            1
          
        
        ,
        
          w
          
            i
            ,
            2
          
        
        …
        
          w
          
            i
            ,
            n
          
        
      
    
    {\displaystyle w_{i,1},w_{i,2}\dots w_{i,n}}
  
 and picks the k sites that yield the k largest hash values. The clients have thereby achieved distributed 
  
    
      
        k
      
    
    {\displaystyle k}
  
-agreement.
If a site 
  
    
      
        S
      
    
    {\displaystyle S}
  
 is added or removed, only the objects mapping to 
  
    
      
        S
      
    
    {\displaystyle S}
  
 are remapped to different sites, satisfying the minimal disruption constraint above. The HRW assignment can be computed independently by any client, since it depends only on the identifiers for the set of sites 
  
    
      
        
          S
          
            1
          
        
        ,
        
          S
          
            2
          
        
        …
        
          S
          
            n
          
        
      
    
    {\displaystyle S_{1},S_{2}\dots S_{n}}
  
 and the object being assigned.
HRW easily accommodates different capacities among sites. If site 
  
    
      
        
          S
          
            k
          
        
      
    
    {\displaystyle S_{k}}
  
 has twice the capacity of the other sites, we simply represent 
  
    
      
        
          S
          
            k
          
        
      
    
    {\displaystyle S_{k}}
  
 twice in the list, say, as 
  
    
      
        
          S
          
            k
            ,
            1
          
        
        ,
        
          S
          
            k
            ,
            2
          
        
      
    
    {\displaystyle S_{k,1},S_{k,2}}
  
. Clearly, twice as many objects will now map to 
  
    
      
        
          S
          
            k
          
        
      
    
    {\displaystyle S_{k}}
  
 as to the other sites.

Properties
Consider the simple version of the problem, with k = 1, where all clients are to agree on a single site for an object O. Approaching the problem naively, it might appear sufficient to treat the n sites as buckets in a hash table and hash the object name O into this table. Unfortunately, if any of the sites fails or is unreachable, the hash table size changes, forcing all objects to be remapped. This massive disruption makes such direct hashing unworkable.
Under rendezvous hashing, however, clients handle site failures by picking the site that yields the next largest weight. Remapping is required only for objects currently mapped to the failed site, and disruption is minimal.
Rendezvous hashing has the following properties:

Low overhead: The hash function used is efficient, so overhead at the clients is very low.
Load balancing: Since the hash function is randomizing, each of the n sites is equally likely to receive the object O. Loads are uniform across the sites.
Site capacity: Sites with different capacities can be represented in the site list with multiplicity in proportion to capacity. A site with twice the capacity of the other sites will be represented twice in the list, while every other site is represented once.
High hit rate: Since all clients agree on placing an object O into the same site SO, each fetch or placement of O into SO yields the maximum utility in terms of hit rate. The object O will always be found unless it is evicted by some replacement algorithm at SO.
Minimal disruption: When a site fails, only the objects mapped to that site need to be remapped. Disruption is at the minimal possible level, as proved in.
Distributed k-agreement: Clients can reach distributed agreement on k sites simply by selecting the top k sites in the ordering.

O(log n) running time via skeleton-based hierarchical rendezvous hashing
The standard version of Rendezvous Hashing described above works quite well for moderate n, but when 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is extremely large, the hierarchical use of Rendezvous Hashing achieves 
  
    
      
        O
        (
        log
        ⁡
        n
        )
      
    
    {\displaystyle O(\log n)}
  
 running time. This approach creates a virtual hierarchical structure (called a "skeleton"), and achieves 
  
    
      
        O
        (
        log
        ⁡
        n
        )
      
    
    {\displaystyle O(\log n)}
  
 running time by applying HRW at each level while descending the hierarchy. The idea is to first choose some constant 
  
    
      
        m
      
    
    {\displaystyle m}
  
 and organize the 
  
    
      
        n
      
    
    {\displaystyle n}
  
 sites into 
  
    
      
        c
        =
        ⌈
        n
        
          /
        
        m
        ⌉
      
    
    {\displaystyle c=\lceil n/m\rceil }
  
 clusters 
  
    
      
        
          C
          
            1
          
        
        =
        
          {
          
            
              S
              
                1
              
            
            ,
            
              S
              
                2
              
            
            …
            
              S
              
                m
              
            
          
          }
        
        ,
        
          C
          
            2
          
        
        =
        
          {
          
            
              S
              
                m
                +
                1
              
            
            ,
            
              S
              
                m
                +
                2
              
            
            …
            
              S
              
                2
                m
              
            
          
          }
        
        …
      
    
    {\displaystyle C_{1}=\left\{S_{1},S_{2}\dots S_{m}\right\},C_{2}=\left\{S_{m+1},S_{m+2}\dots S_{2m}\right\}\dots }
  
 Next, build a virtual hierarchy by choosing a constant 
  
    
      
        f
      
    
    {\displaystyle f}
  
 and imagining these 
  
    
      
        c
      
    
    {\displaystyle c}
  
 clusters placed at the leaves of a tree 
  
    
      
        T
      
    
    {\displaystyle T}
  
 of virtual nodes, each with fanout 
  
    
      
        f
      
    
    {\displaystyle f}
  
.

In the accompanying diagram, the cluster size is 
  
    
      
        m
        =
        4
      
    
    {\displaystyle m=4}
  
, and the skeleton fanout is 
  
    
      
        f
        =
        3
      
    
    {\displaystyle f=3}
  
. Assuming 108 sites (real nodes) for convenience, we get a three-tier virtual hierarchy. Since 
  
    
      
        f
        =
        3
      
    
    {\displaystyle f=3}
  
, each virtual node has a natural numbering in octal. Thus, the 27 virtual nodes at the lowest tier would be numbered 
  
    
      
        000
        ,
        001
        ,
        002
        ,
        .
        .
        .
        ,
        221
        ,
        222
      
    
    {\displaystyle 000,001,002,...,221,222}
  
 in octal (we can, of course, vary the fanout at each level - in that case, each node will be identified with the corresponding mixed-radix number).
The easiest way to understand the virtual hierarchy is by starting at the top, and descending the virtual hierarchy. We successively apply Rendezvous Hashing to the set of virtual nodes at each level of the hierarchy, and descend the branch defined by the winning virtual node. We can in fact start at any level in the virtual hierarchy. Starting lower in the hierarchy requires more hashes, but may improve load distribution in the case of failures.
For example, instead of applying HRW to all 108 real nodes in the diagram, we can first apply HRW to the 27 lowest-tier virtual nodes, selecting one. We then apply HRW to the four real nodes in its cluster, and choose the winning site. We only need 
  
    
      
        27
        +
        4
        =
        31
      
    
    {\displaystyle 27+4=31}
  
 hashes, rather than 108. If we apply this method starting one level higher in the hierarchy, we would need 
  
    
      
        9
        +
        3
        +
        4
        =
        16
      
    
    {\displaystyle 9+3+4=16}
  
 hashes to get to the winning site. The figure shows how, if we proceed starting from the root of the skeleton, we may successively choose the virtual nodes 
  
    
      
        (
        2
        
          )
          
            3
          
        
      
    
    {\displaystyle (2)_{3}}
  
, 
  
    
      
        (
        20
        
          )
          
            3
          
        
      
    
    {\displaystyle (20)_{3}}
  
, and 
  
    
      
        (
        200
        
          )
          
            3
          
        
      
    
    {\displaystyle (200)_{3}}
  
, and finally end up with site 74.
The virtual hierarchy need not be stored, but can be created on demand, since the virtual nodes names are simply prefixes of base-
  
    
      
        f
      
    
    {\displaystyle f}
  
 (or mixed-radix) representations. We can easily create appropriately sorted strings from the digits, as required. In the example, we would be working with the strings 
  
    
      
        0
        ,
        1
        ,
        2
      
    
    {\displaystyle 0,1,2}
  
 (at tier 1), 
  
    
      
        20
        ,
        21
        ,
        22
      
    
    {\displaystyle 20,21,22}
  
 (at tier 2), and 
  
    
      
        200
        ,
        201
        ,
        202
      
    
    {\displaystyle 200,201,202}
  
 (at tier 3). Clearly, 
  
    
      
        T
      
    
    {\displaystyle T}
  
 has height 
  
    
      
        h
        =
        O
        (
        log
        ⁡
        c
        )
        =
        O
        (
        log
        ⁡
        n
        )
      
    
    {\displaystyle h=O(\log c)=O(\log n)}
  
, since 
  
    
      
        m
      
    
    {\displaystyle m}
  
 and 
  
    
      
        f
      
    
    {\displaystyle f}
  
 are both constants. The work done at each level is 
  
    
      
        O
        (
        1
        )
      
    
    {\displaystyle O(1)}
  
, since 
  
    
      
        f
      
    
    {\displaystyle f}
  
 is a constant.
The value of 
  
    
      
        m
      
    
    {\displaystyle m}
  
 can be chosen based on factors like the anticipated failure rate and the degree of desired load balancing. A higher value of 
  
    
      
        m
      
    
    {\displaystyle m}
  
 leads to less load skew in the event of failure at the cost of higher search overhead.
The choice 
  
    
      
        m
        =
        n
      
    
    {\displaystyle m=n}
  
 is equivalent to non-hierarchical rendezvous hashing. In practice, the hash function 
  
    
      
        h
        (
        ⋅
        )
      
    
    {\displaystyle h(\cdot )}
  
 is very cheap, so 
  
    
      
        m
        =
        n
      
    
    {\displaystyle m=n}
  
 can work quite well unless 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is very high.
For any given object, it is clear that each leaf-level cluster, and hence each of the 
  
    
      
        n
      
    
    {\displaystyle n}
  
 sites, is chosen with equal probability.

Replication, site failures, and site additions
One can enhance resiliency to failures by replicating each object O across the highest ranking r < m sites for O, choosing r based on the level of resiliency desired. The simplest strategy is to replicate only within the leaf-level cluster.
If the leaf-level site selected for O is unavailable, we select the next-ranked site for O within the same leaf-level cluster. If O has been replicated within the leaf-level cluster, we are sure to find O in the next available site in the ranked order of r sites. All objects that were held by the failed server appear in some other site in its cluster. (Another option is to go up one or more tiers in the skeleton and select an alternate from among the sibling virtual nodes at that tier. We then descend the hierarchy to the real nodes, as above.)
When a site is added to the system, it may become the winning site for some objects already assigned to other sites. Objects mapped to other clusters will never map to this new site, so we need to only consider objects held by other sites in its cluster. If the sites are caches, attempting to access an object mapped to the new site will result in a cache miss, the corresponding object will be fetched and cached, and operation returns to normal.
If sites are servers, some objects must be remapped to this newly added site.  As before, objects mapped to other clusters will never map to this new site, so we need to only consider objects held by sites in its cluster. That is, we need only remap objects currently present in the m sites in this local cluster, rather than the entire set of objects in the system. New objects mapping to this site will of course be automatically assigned to it.

Comparison with consistent hashing
Because of its simplicity, lower overhead, and generality (it works for any k < n), rendezvous hashing is increasingly being preferred over consistent hashing. Recent examples of its use include the Github load balancer, the Apache Ignite distributed database, and by the Twitter EventBus pub/sub platform.
Consistent hashing operates by mapping sites uniformly and randomly to points on a unit circle called tokens. Objects are also mapped to the unit circle and placed in the site whose token is the first encountered traveling clockwise from the object's location. When a site is removed, the objects it owns are transferred to the site owning the next token encountered moving clockwise. Provided each site is mapped to a large number (100–200, say) of tokens this will reassign objects in a relatively uniform fashion among the remaining sites.
If sites are mapped to points on the circle randomly by hashing 200 variants of the site ID, say, the assignment of any object requires storing or recalculating 200 hash values for each site. However, the tokens associated with a given site can be precomputed and stored in a sorted list, requiring only a single application of the hash function to the object, and a binary search to compute the assignment. Even with many tokens per site, however, the basic version of consistent hashing may not balance objects uniformly over sites, since when a site is removed each object assigned to it is distributed only over as many other sites as the site has tokens (say 100–200).
Variants of consistent hashing (such as Amazon's Dynamo) that use more complex logic to distribute tokens on the unit circle offer better load balancing than basic consistent hashing, reduce the overhead of adding new sites, and reduce metadata overhead and offer other benefits.

Advantages of Rendezvous hashing over consistent hashing
Rendezvous hashing (HRW) is much simpler conceptually and in practice. It also distributes objects uniformly over all sites, given a uniform hash function. Unlike consistent hashing, HRW requires no precomputing or storage of tokens. Consider k =1. An object 
  
    
      
        
          O
          
            i
          
        
      
    
    {\displaystyle O_{i}}
  
 is placed into one of 
  
    
      
        n
      
    
    {\displaystyle n}
  
 sites 
  
    
      
        
          S
          
            1
          
        
        ,
        
          S
          
            2
          
        
        …
        
          S
          
            n
          
        
      
    
    {\displaystyle S_{1},S_{2}\dots S_{n}}
  
 by computing the 
  
    
      
        n
      
    
    {\displaystyle n}
  
 hash values 
  
    
      
        h
        (
        
          O
          
            i
          
        
        ,
        
          S
          
            j
          
        
        )
      
    
    {\displaystyle h(O_{i},S_{j})}
  
 and picking the site 
  
    
      
        
          S
          
            k
          
        
      
    
    {\displaystyle S_{k}}
  
 that yields the highest hash value. If a new site 
  
    
      
        
          S
          
            n
            +
            1
          
        
      
    
    {\displaystyle S_{n+1}}
  
 is added, new object placements or requests will compute 
  
    
      
        n
        +
        1
      
    
    {\displaystyle n+1}
  
 hash values, and pick the largest of these. If an object already in the system at 
  
    
      
        
          S
          
            k
          
        
      
    
    {\displaystyle S_{k}}
  
 maps to this new site 
  
    
      
        
          S
          
            n
            +
            1
          
        
      
    
    {\displaystyle S_{n+1}}
  
, it will be fetched afresh and cached at 
  
    
      
        
          S
          
            n
            +
            1
          
        
      
    
    {\displaystyle S_{n+1}}
  
. All clients will henceforth obtain it from this site, and the old cached copy at 
  
    
      
        
          S
          
            k
          
        
      
    
    {\displaystyle S_{k}}
  
 will ultimately be replaced by the local cache management algorithm. If 
  
    
      
        
          S
          
            k
          
        
      
    
    {\displaystyle S_{k}}
  
 is taken offline, its objects will be remapped uniformly to the remaining 
  
    
      
        n
        −
        1
      
    
    {\displaystyle n-1}
  
 sites.
Variants of the HRW algorithm, such as the use of a skeleton (see below), can reduce the 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 time for object location to 
  
    
      
        O
        (
        log
        ⁡
        n
        )
      
    
    {\displaystyle O(\log n)}
  
, at the cost of less global uniformity of placement. When 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is not too large, however, the 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 placement cost of basic HRW is not likely to be a problem. HRW completely avoids all the overhead and complexity associated with correctly handling multiple tokens for each site and associated metadata.
Rendezvous hashing also has the great advantage that it provides simple solutions to other important problems, such as distributed 
  
    
      
        k
      
    
    {\displaystyle k}
  
-agreement.

Consistent hashing is a special case of Rendezvous hashing
Rendezvous hashing is both simpler and more general than consistent hashing. Consistent hashing can be shown to be a special case of HRW by an appropriate choice of a two-place hash function. From the site identifier 
  
    
      
        S
      
    
    {\displaystyle S}
  
 the simplest version of consistent hashing computes a list of token positions, e.g., 
  
    
      
        
          t
          
            s
          
        
        =
        
          h
          
            c
          
        
        (
        S
        )
      
    
    {\displaystyle t_{s}=h_{c}(S)}
  
 where 
  
    
      
        
          h
          
            c
          
        
      
    
    {\displaystyle h_{c}}
  
 hashes values to locations on the unit circle. Define the two place hash function 
  
    
      
        h
        (
        S
        ,
        O
        )
      
    
    {\displaystyle h(S,O)}
  
 to be 
  
    
      
        
          
            1
            
              
                min
                
                  S
                
              
              (
              
                h
                
                  c
                
              
              (
              O
              )
              −
              
                t
                
                  s
                
              
              )
            
          
        
      
    
    {\displaystyle {\frac {1}{\min _{S}(h_{c}(O)-t_{s})}}}
  
 where 
  
    
      
        
          h
          
            c
          
        
        (
        O
        )
        −
        
          t
          
            s
          
        
      
    
    {\displaystyle h_{c}(O)-t_{s}}
  
 denotes the distance along the unit circle from 
  
    
      
        
          h
          
            c
          
        
        (
        O
        )
      
    
    {\displaystyle h_{c}(O)}
  
 to 
  
    
      
        
          t
          
            s
          
        
      
    
    {\displaystyle t_{s}}
  
 (since 
  
    
      
        
          h
          
            c
          
        
        (
        O
        )
        −
        
          t
          
            s
          
        
      
    
    {\displaystyle h_{c}(O)-t_{s}}
  
 has some minimal non-zero value there is no problem translating this value to a unique integer in some bounded range). This will duplicate exactly the assignment produced by consistent hashing.
It is not possible, however, to reduce HRW to consistent hashing (assuming the number of tokens per site is bounded), since HRW potentially reassigns the objects from a removed site to an unbounded number of other sites.

Weighted variations
In the standard implementation of rendezvous hashing, every node receives a statically equal proportion of the keys. This behavior, however, is undesirable when the nodes have different capacities for processing or holding their assigned keys. For example, if one of the nodes had twice the storage capacity as the others, it would be beneficial if the algorithm could take this into account such that this more powerful node would receive twice the number of keys as each of the others.
A straightforward mechanism to handle this case is to assign two virtual locations to this node, so that if either of that larger node's virtual locations has the highest hash, that node receives the key. But this strategy does not work when the relative weights are not integer multiples. For example, if one node had 42% more storage capacity, it would require adding many virtual nodes in different proportions, leading to greatly reduced performance. Several modifications to rendezvous hashing have been proposed to overcome this limitation.

Cache Array Routing Protocol
The Cache Array Routing Protocol (CARP) is a 1998 IETF draft that describes a method for computing load factors which can be multiplied by each node's hash score to yield an arbitrary level of precision for weighting nodes differently. However, one disadvantage of this approach is that when any node's weight is changed, or when any node is added or removed, all the load factors must be re-computed and relatively scaled. When the load factors change relative to one another, it triggers movement of keys between nodes whose weight was not changed, but whose load factor did change relative to other nodes in the system. This results in excess movement of keys.

Controlled replication
Controlled replication under scalable hashing or CRUSH is an extension to RUSH that improves upon rendezvous hashing by constructing a tree where a pseudo-random function (hash) is used to navigate down the tree to find which node is ultimately responsible for a given key. It permits perfect stability for adding nodes; however, it is not perfectly stable when removing or re-weighting nodes, with the excess movement of keys being proportional to the height of the tree.
The CRUSH algorithm is used by the ceph data storage system to map data objects to the nodes responsible for storing them.

Other variants
In 2005, Christian Schindelhauer and Gunnar Schomaker described a logarithmic method for re-weighting hash scores in a way that does not require relative scaling of load factors when a node's weight changes or when nodes are added or removed. This enabled the dual benefits of perfect precision when weighting nodes, along with perfect stability, as only a minimum number of keys needed to be remapped to new nodes.
A similar logarithm-based hashing strategy is used to assign data to storage nodes in Cleversafe's data storage system, now IBM Cloud Object Storage.

Systems using Rendezvous hashing
Rendezvous hashing is being used widely in real-world systems. A partial list includes Oracle's Database in-memory, the GitHub load balancer, the Apache Ignite distributed database, the Tahoe-LAFS file store, the CoBlitz large-file distribution service, Apache Druid, IBM's Cloud Object Store, the Arvados Data Management System, Apache Kafka, and by the Twitter EventBus pub/sub platform.

Implementation
Implementation is straightforward once a hash function 
  
    
      
        h
        (
        ⋅
        )
      
    
    {\displaystyle h(\cdot )}
  
 is chosen (the original work on the HRW method makes a hash function recommendation). Each client only needs to compute a hash value for each of the 
  
    
      
        n
      
    
    {\displaystyle n}
  
 sites, and then pick the largest. This algorithm runs in 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 time. If the hash function is efficient, the 
  
    
      
        O
        (
        n
        )
      
    
    {\displaystyle O(n)}
  
 running time is not a problem unless 
  
    
      
        n
      
    
    {\displaystyle n}
  
 is very large.

Weighted rendezvous hash
Python code implementing a weighted rendezvous hash:

Example outputs of WRH:

References
External links
Rendezvous Hashing: an alternative to Consistent Hashing

## Archive Info
- **Archived on:** 2024-12-15 21:05:54 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 30188 bytes
- **Word Count:** 3542 words
