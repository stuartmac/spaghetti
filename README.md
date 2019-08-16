# spaghetti
Build file cross reference graphs

This project arose out of my need to understand a legacy webapp at work.

The idea is to build a graph of file cross references, analogous to a code map.

## Plan

- use GraphML format
- going to use networkx for graph building and IO

1. Identify file references/ paths, Cn, in a file, P (regex)
2. Represent this as a directed graph P -> Cn
3. Repeat for all Cn

NB. Will want to look at sets of files in (1)