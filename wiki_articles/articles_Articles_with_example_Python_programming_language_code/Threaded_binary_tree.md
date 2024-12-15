# Threaded binary tree

## Metadata
- **Last Updated:** 2024-12-03 07:01:58 UTC
- **Original Article:** [Threaded binary tree](https://en.wikipedia.org/wiki/Threaded_binary_tree)
- **Language:** en
- **Page ID:** 4262609

## Summary
In computing, a threaded binary tree is a binary tree variant that facilitates traversal in a particular order.
An entire binary search tree can be easily traversed in order of the main key, but given only a pointer to a node, finding the node which comes next may be slow or impossible. For example, leaf nodes by definition have no descendants, so given only a pointer to a leaf node no other node can be reached. A threaded tree adds extra information in some or all nodes, so that for any given single node the "next" node can be found quickly, allowing tree traversal without recursion and the extra storage (proportional to the tree's depth) that recursion requires.

## Categories
This article belongs to the following categories:

- Category:All articles needing rewrite
- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Binary trees
- Category:Search trees
- Category:Short description is different from Wikidata
- Category:Wikipedia articles needing rewrite from October 2011

## Table of Contents

- Threading
- Motivation
- Types
- The array of in-order traversal
- Example
- Null links
- References
- External links

## Content

In computing, a threaded binary tree is a binary tree variant that facilitates traversal in a particular order.
An entire binary search tree can be easily traversed in order of the main key, but given only a pointer to a node, finding the node which comes next may be slow or impossible. For example, leaf nodes by definition have no descendants, so given only a pointer to a leaf node no other node can be reached. A threaded tree adds extra information in some or all nodes, so that for any given single node the "next" node can be found quickly, allowing tree traversal without recursion and the extra storage (proportional to the tree's depth) that recursion requires.

Threading
"A binary tree is threaded by making all right child pointers that would normally be null point to the in-order successor of the node (if it exists), and all left child pointers that would normally be null point to the in-order predecessor of the node."

This assumes the traversal order is the same as in-order traversal of the tree. However, pointers can instead (or in addition) be added to tree nodes, rather than replacing. Linked lists thus defined are also commonly called "threads", and can be used to enable traversal in any order(s) desired. For example, a tree whose nodes represent information about people might be sorted by name, but have extra threads allowing quick traversal in order of birth date, weight, or any other known characteristic.

Motivation
Trees, including (but not limited to) binary search trees, can be used to store items in a particular order, such as the value of some property stored in each node, often called a key. One useful operation on such a tree is traversal: visiting all the items in order of the key.
A simple recursive traversal algorithm that visits each node of a binary search tree is the following. Assume t is a pointer to a node, or nil. "Visiting" t can mean performing any action on the node t or its contents.

One problem with this algorithm is that, because of its recursion, it uses stack space proportional to the height of a tree. If the tree is fairly balanced, this amounts to O(log n) space for a tree containing n elements. In the worst case, when the tree takes the form of a chain, the height of the tree is n so the algorithm takes O(n) space. A second problem is that all traversals must begin at the root when nodes have pointers only to their children. It is common to have a pointer to a particular node, but that is not sufficient to get back to the rest of the tree unless extra information is added, such as thread pointers.
In this approach, it may not be possible to tell whether the left and/or right pointers in a given node actually point to children, or are a consequence of threading. If the distinction is necessary, adding a single bit to each node is enough to record it.
In a 1968 textbook, Donald Knuth asked whether a non-recursive algorithm for in-order traversal exists, that uses no stack and leaves the tree unmodified. One of the solutions to this problem is tree threading, presented by Joseph M. Morris in 1979.
In the 1969 follow-up edition, Knuth attributed the threaded tree representation to Perlis and Thornton (1960).

Relation to parent pointers
Another way to achieve similar goals is to include a pointer in every node, to that node's parent node. Given that, the "next" node can always be reached, "right" pointers are still null whenever there are no right children. To find the "next" node from a node whose right pointer is null, walk up through "parent" pointers until reaching a node whose right pointer is not null, and is not the child you just came up from. That node is the "next" node, and after it come its descendants on the right.
It is also possible to discover the parent of a node from a threaded binary tree, without explicit use of parent pointers or a stack, although it is slower. To see this, consider a node k with right child r.  Then the left pointer of r must be either a child or a thread back to k. In the case that r has a left child, that left child must in turn have either a left child of its own or a thread back to k, and so on for all successive left children.  So by following the chain of left pointers from r, we will eventually find a thread pointing back to k.  The situation is symmetrically similar when q is the left child of p—we can follow q's right children to a thread pointing ahead to p.

In Python:

Types
Single threaded: each node is threaded towards either the in-order predecessor or successor (left or right).
Double threaded: each node is threaded towards both the in-order predecessor and successor (left and right).

The array of in-order traversal
Threads are reference to the predecessors and successors of the node according to an inorder traversal. 
In-order traversal of the threaded tree is A,B,C,D,E,F,G,H,I, the predecessor of E is D, the successor of E is F.

Example
Let's make the Threaded Binary tree out of a normal binary tree:

The in-order traversal for the above tree is — D B A E C. So, the respective Threaded Binary tree will be --

Null links
In an m-way threaded binary tree with n nodes, there are n×m − (n−1) void links.

References
External links
GNU libavl 2.0.2, Section on threaded binary search trees

## Archive Info
- **Archived on:** 2024-12-15 21:06:20 UTC
- **Archive Source:** Wikipedia (_en_)
- **Total References:** 0
- **Article Size:** 5287 bytes
- **Word Count:** 941 words
