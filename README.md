TC2011 - Bayes Network Lab
Size of teams: each team must be made up of at most 2 students.
Querying a Bayes Network
For this lab, you have to write a program to Query a Bayes Network

Objective
Your assignment is to build a program that reads the structure and probability tables of a Bayes Network, and then query it. Querying a Bayes network means to compute the probability of the query variables being true, given certain evidence.

A little help: Suggested steps
Here are a couple of hints on how to approach this lab.

Read the section about input/output formats below carefully. There are number of example testcases for your program that you can use to check it is correct.
Create a data structure for a Bayes Network. Hint: it should have
Variable nodes
For each node, links to zero or more of its parents
Conditional probability tables
Create a function that reads and parses the Nodes and Probability sections of the input, and instantiates a Bayes Network data structure that you created in step 2.
Implement the enumeration algorithm. Watch video 1 and 2 in the Udacity course again if you need a refresher.
Create a function that reads and parses the Queries section of the input
For each Query, have your program calculate and output the probability
Submit your program to AlphaGrader to run it against all available testcases to make sure it is correct.
The program
Input/Output
Your program must read from stdin and output to stdout. See here for instructions how to do this.

Basically, your program will be called by executing run < [problem_file], where problem_file is a file describing the problem (see below). Your program should output the solution as text to the terminal.

Input
The input consists of three sections:

Nodes: a list of variable nodes in the Bayes Network, separated by a comma.
Probabilities: the probability tables associated variable nodes. Entries of a probability table have the following format:

VariableAssignment [| [VariableAssigment]*]? = Probability

This encodes the probability of a variable being true, given its parent nodes in the Bayes Network having a certain value.

A VariableAssignment is formatted as [+-]VariableName. When preceded by a +, it means that the variable is true. A minus (-) indicates the variable is false.

Queries: one or more queries. A query has the following format

[QueryAssignment]* [| [EvidenceAssigment]*]?

Both QueryAssignment and EvidenceAssigment are VariableAssigments.

A query basically requests your program to compute the probability of the query variables having a certain value, given the evidence variables having a certain value.

Output
Output consists multiple lines, one per query. For each query, output the probability, rounded to 7 digits (no trailing zeroes).

Example
The following example encodes a Bayes network for a simple diagnostics test to determine whether a patient is ill.

The network consists of two nodes: "Ill" and "Test". There is one edge from "Ill" to "Test".

There are 3 queries defined.

Input:

[Nodes]
Test, Ill

[Probabilities]
+Ill = 0.001
+Test|+Ill=0.9
+Test|-Ill=0.05

[Queries]
+Ill
-Ill|+Test
+Test|+Ill
Output:

0.001
0.9823009
0.9
More examples can be found in the tests section.

The report
Compare with Hugin Lite
When you’ve finished your program, you can compare your implementation to Hugin Lite. Hugin lite is a software kit for developing graphical Bayes networks. Download it here.

Create your own example network based on a real example. Make it between 3 and 4 nodes. Wikipedia has a good example. You'll have to come up with your own though!

Bayes Network

Then:

Encode your example into the input format for your program (see above)
Create a couple of queries
Run your program
Compare the output to Hugin Lite to see that the values between both match.
Writing your report
Write a reflection or make a table where you compare Hugin Lite to your implementation. Within this you must answer the following questions: What are the differences between what they generate? Do they use the same algorithms? What are their common bases? Which tool would you use for what cases in real life applications? (400 to 500 words)

Include the diagrams of the developed networks.