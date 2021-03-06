# Summary

Table of Contents

* [1 Building Abstractions with Procedures](README.md)
  * [1.1 The Elements of Programming.md](ch1/1.1TheElementsofProgramming.md)
  * [1.2 Procedures and the Processes They Generate](ch1/1.2ProcedureAndProcess.md)
  * [1.3 Formulating Abstractions with Higher-Order Procedures](ch1/1.3FormulatingAbstractionswithHigher-OrderProcedures.md)

* [2 Building Abstractions with Data](ch2/2BuildingAbstractionswithData.md)

  * [2.1 Introduction to Data Abstraction](ch2/2.1IntroductionToDataAbstract.md)
  * [2.2 Hierarchical Data and the Closure Property](ch2/2.2HierarchicalDataandtheClosureProperty)
  * [2.3 Symbolic Data](ch2/2.3SymbolicData.md)
  * [2.4 Multiple Representations for Abstract Data](README.md)
    * 2.4.1 Representations for Complex Numbers]()
    * 2.4.2 Tagged data]()
    * 2.4.3 Data-Directed Programming and Additivity]()
  * [2.5 Systems with Generic Operations](README.md)
    * 2.5.1 Generic Arithmetic Operations]()
    * 2.5.2 Combining Data of Different Types]()
    * 2.5.3 Example: Symbolic Algebra]()

* [3 Modularity, Objects, and State](README.md)
  * [3.1 Assignment and Local State](README.md)
  	* 3.1.1 Local State Variables]()
  	* 3.1.2 The Benefits of Introducing Assignment]()
  	* 3.1.3 The Costs of Introducing Assignment]()
  * [3.2 The Environment Model of Evaluation](README.md)
  	* 3.2.1 The Rules for Evaluation]()
  	* 3.2.2 Applying Simple Procedures]()
  	* 3.2.3 Frames as the Repository of Local State]()
  	* 3.2.4 Internal Definitions]()
  * [3.3 Modeling with Mutable Data](README.md)
  	* 3.3.1 Mutable List Structure]()
  	* 3.3.2 Representing Queues]()
  	* 3.3.3 Representing Tables]()
  	* 3.3.4 A Simulator for Digital Circuits]()
  	* 3.3.5 Propagation of Constraints]()
  * [3.4 Concurrency: Time Is of the Essence](README.md)
  	* 3.4.1 The Nature of Time in Concurrent Systems]()
  	* 3.4.2 Mechanisms for Controlling Concurrency]()
  * [3.5 Streams](README.md)
  	* 3.5.1 Streams Are Delayed Lists]()
  	* 3.5.2 Infinite Streams]()
  	* 3.5.3 Exploiting the Stream Paradigm
  	* 3.5.4 Streams and Delayed Evaluation
  	* 3.5.5 Modularity of Functional Programs and Modularity of Objects

* [4 Metalinguistic Abstraction](README.md)
  * [4.1 The Metacircular Evaluator](README.md)
  	* 4.1.1 The Core of the Evaluator
  	* 4.1.2 Representing Expressions
  	* 4.1.3 Evaluator Data Structures
  	* 4.1.4 Running the Evaluator as a Program
  	* 4.1.5 Data as Programs
  	* 4.1.6 Internal Definitions
  	* 4.1.7 Separating Syntactic Analysis from Execution
  * [4.2 Variations on a Scheme — Lazy Evaluation](README.md)
  	* 4.2.1 Normal Order and Applicative Order
  	* 4.2.2 An Interpreter with Lazy Evaluation
  	* 4.2.3 Streams as Lazy Lists
  * [4.3 Variations on a Scheme — Nondeterministic Computing](README.md)
  	* 4.3.1 Amb and Search
  	* 4.3.2 Examples of Nondeterministic Programs
  	* 4.3.3 Implementing the Amb Evaluator
  * [4.4 Logic Programming](README.md)
  	* 4.4.1 Deductive Information Retrieval
  	* 4.4.2 How the Query System Works
  	* 4.4.3 Is Logic Programming Mathematical Logic?
  	* 4.4.4 Implementing the Query System
  		 	4.4.4.1 The Driver Loop and Instantiation
  		 	4.4.4.2 The Evaluator
  		 	4.4.4.3 Finding Assertions by Pattern Matching
  		 	4.4.4.4 Rules and Unification
  		 	4.4.4.5 Maintaining the Data Base
  		 	4.4.4.6 Stream Operations
  		 	4.4.4.7 Query Syntax Procedures
  		 	4.4.4.8 Frames and Bindings

* [5 Computing with Register Machines](README.md)
  * [5.1 Designing Register Machines](README.md)
    * 5.1.1 A Language for Describing Register Machines
    * 5.1.2 Abstraction in Machine Design
    * 5.1.3 Subroutines
    * 5.1.4 Using a Stack to Implement Recursion
    * 5.1.5 Instruction Summary
  * [5.2 A Register-Machine Simulator](README.md)
    * 5.2.1 The Machine Model
    * 5.2.2 The Assembler
    * 5.2.3 Generating Execution Procedures for Instructions
    * 5.2.4 Monitoring Machine Performance
  * [5.3 Storage Allocation and Garbage Collection](README.md)
    * 5.3.1 Memory as Vectors
    * 5.3.2 Maintaining the Illusion of Infinite Memory
  * [5.4 The Explicit-Control Evaluator](README.md)
    * 5.4.1 The Core of the Explicit-Control Evaluator
    * 5.4.2 Sequence Evaluation and Tail Recursion
    * 5.4.3 Conditionals, Assignments, and Definitions
    * 5.4.4 Running the Evaluator
  * [5.5 Compilation](README.md)
    * 5.5.1 Structure of the Compiler

    * 5.5.2 Compiling Expressions

    * 5.5.3 Compiling Combinations

    * 5.5.4 Combining Instruction Sequences

    * 5.5.5 An Example of Compiled Code

    * 5.5.6 Lexical Addressing

    * 5.5.7 Interfacing Compiled Code to the Evaluator

      References
      List of Exercises
      List of Figures
      Term Index
      Colophon
