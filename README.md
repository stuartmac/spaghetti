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

## Graph representation of file cross references

- nodes are files and equivalent paths to the same file shouldn't create new nodes
(path normalisation for node path attributes?)
- edges are file cross references. They could be directional, edges could have weights
corresponding its appearance frequency, equivalent cross references (e.g., absolute and
relative) could each count as seperate edges, attributes could include things like 
its immediate context (e.g., commented; then different contexts might lead to different
edges)
