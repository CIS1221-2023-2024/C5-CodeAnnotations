# C5-CodeAnnotation Challenger's Report

## Project Overview

**Project Name**: C5-CodeAnnotations
**Date of Review**: 14/01/2024
**Challenger**: Giorgio Bellia

The C5-CodeAnnotations is a project that focuses on exploring the use of code annotations, such as decorators, assertions and attributes. Annotations are a poweful tool that enhance the readability and understandability of code. Especially when working in a team, code annotations are fundamental to ensure code can be maintained and modified by other developers. Also, code annotations provide information about the structure of code.
In this report, I critically review the project considering three main aspects: [Project Structure](#project-structure), [code quality](#code-quality) and [functionality](#functionality). Also, I provide recommendations for future enhancements and personal proposals.

### Project Structure
This project explores code annotations in Java and Python. To do so, a simple calculator program is implemented. Regarding the Java directory, I think the solution lacks a structure, all scripts are in the same folder and the Operations.java file contains more than one class, which for small project might be fine; however, it is good practice to place each class to its own file. On the other hand, the Python solutions implements the different calculator operations using functions and not classes. The Python solution is functional while the Java solution is object-oriented, both work fine; however, in my opinion, for this problem the functional paradigm is more suitable. To conclude, the README file is missing instructions on how to install and run the solutions.

### Code Quality
Both solutions are well documented; comments are clear and consise, variable's names are meaningful, annotations are used correctly, module are self contained and it is clear to understand their function. I do not have any suggestion to improve the quality of the code.

### Functionality 
 - ***Java***
The *Override* annotation allows a subclass to redefine a method of the superclass. In this case, the parent class is an abstract class, inside which an abstract method is defined. The override annotation is used by any of the subclasses to implement the abstract method.
The *Deprecated* annotation is useful when working in a team of developers. When a method is deprecated its use is discouraged, it may be the case that the method is removed in the future.
The *SuppressWarnings* annotation is used to turn off the warnings of the compiler. Developers must be careful when using it and only use it on warnings they are aware of.
- ***Python***
In Python, a decorator is an annotation that allows to modify the behavior of functions. Decorators are often used to wrap or enhance the functionality of functions.
