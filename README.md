# 310-tkinter-review
## Review of creating a gui with tkinter

TKinter is an object oriented interface that uses a CLASS to build a framework for a GUI Interface.  We will be using tkinter  to demonstrate how classes can be instantiated to build objects, and how those objects can interact with other objects within a program.

Today, we will review the basics of tkinter including:

* Instantiating a window object from the tkinter class
* instantiating objects/widgets in the window object using the pack, grid and place
* Binding events to buttons
* retrieving values from entry widgets
* entering values into entry widgets

Assigment:

Task 1: Factoring
Create a program to factor a basic trinomial in the format x^2 + bc + c.
You cannot use the quadratic formula.  You must think about how a regular person would factor the trinomial and use that algorithm.

Create a tkinter interface that uses 3 entry widgets to retrieve values for a, b and c.
Display the factored form in a 4th entry widget.
You will also need to add a button for the user to press when they are ready to factor.  This button should be bound to the function that will factor the trinomial.

Task 1a: Use the .pack() method to create your interface
Task 1b: Use the .grid() method to create your interface
Task 1c: Use the .place() method to create your interface.


Task 2: Interface for weather program
Create an interface to display the current weather condtions.

Challenge:
Find out how to retrieve the latitude/longitude for a city and add an option to choose the city and get the current weather conditions there. You can use their geocoding api to help you:
https://openweathermap.org/api/geocoding-api
