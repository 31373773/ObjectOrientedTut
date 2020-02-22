# Explaining Object Oriented Programming Tutorial
## The four principles of object-oriented programming are encapsulation, abstraction, inheritance, and polymorphism. 
Here's more about them.

### 1) Encapsulation: 
> Encapsulation is achieved when each object keeps its state private, inside a class. Other objects don’t have direct access to this state. Instead, they can only call a list of public functions. The class has private methods and fields. It is important to note that the other classes cannot control the private method. The fields are also known as private variables and they determine the state of the class. Then we have public methods which modify the internal state. Classes can call them but they can't directly modify private fields.  

### 2) Abstraction: 
> When I think of abstraction I think of New York Fashion Week. So much is going on behind the scenes during a fashion show, but only relevant models/styles come down the runway. Abstraction is an extension of encapsulation in a sense that it hides all the background work going on. Both encapsulation and abstraction can help us develop and maintain a big codebase.

### 3) Inheritance: 
> Let's say sometimes objects are very similar and share similar logic, but we want to extract and reuse some into a separate class. The child class reuses all fields and methods of the parent class (common part) and can implement its own (unique part). It's like the rural parents [parent class] raise their child [child class] with all the same morals and logic. The child uses some of that logic, but also decides to be a lawyer instead of a farmer. Growing tomatoes and corn was not something that skill **needed** in the city life so the child did not inherit it. Back to OOP, each class adds only what is necessary for it while reusing common logic with the parent classes. 

### 4) Polymorphism: 
> Polymorphism works in a way that each child class keeps its own methods as they are. This solves the issue of wanting to use a collection,which contains a mix of all these classes and we want a method implemented for the parent class and child class too. This typically happens by defining a (parent) interface to be reused. It outlines a bunch of common methods. Then, each child class implements its own version of these methods.
