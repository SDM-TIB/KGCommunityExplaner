# SemEP-Node

## 1.  About

Community detection program based on the similarities of the entities.

## 2. License

GNU GENERAL PUBLIC LICENSE Version 2.

## 3. Requirements

* GNU Compiler Collection (GCC) or Clang.
* GNU make (make).

## 4. Installation

Clean and generate necessary files:

`$>make clean`

`$>make`

The result is that executable file 'semEP-node' will be created.

## 5. Usage

SemEP-Node has several three mandatory command line arguments.
Mandatory means that without specifying this argument, the program won't work.

SemEP-Node command synopsis:

`semEP-node semEP-node <nodes> <similarity matrix> <threshold>`

where mandatory arguments are:
* <nodes> file with the list of nodes.
* <similarity matrix> similarity matrix file with the similarities between the nodes.
* <threshold>: threshold of similarity between the nodes.

## 6. Running one sample

>./semEP-node datasets/test1/nodes.txt datasets/test1/matrix.txt 0.8

## 7 SemEP-Node input

### 7.1. The file format of the similarity matrix

Files with the matrices must contain the similarities between the nodes.
The file format is as follows:

	[number of rows and columns]
	[sim node-1 node-1][SPC]...[SPC][sim node-1 node-n]
	...
	...
	...
	[sim node-n node-1][SPC]...[SPC][sim node-n node-n]

### 7.2. The file format of the list of nodes

The file format is as follows:

	[number of nodes n]
	[node 1]
	...
	...
	...
	[node n]

Where *[node x]* is the identifier of the node. The order of each node
correspond to the position of the node in the corresponding similarity matrix.

## 8. SemEP-Node output

SemEP-Node produces as output a directory with suffix *-Clusters* that contains
the clusters with the edge partitioning of the graph.
Each cluster corresponds to a file on the directory.

## 9. Contact

Please, let me know any comment, problem, bug, or suggestion.

Guillermo Palma
[palma at l3s dot de ](mailto:palma@l3s.de)
