"""
    Properties of OOP

    1) Encapsulation - TBinding (or wrapping) code and data together into a single unit are known as encapsulation.
        It is used to restrict access to methods and variables.
    2) Polymorphism - many forms with different signatures
        a) Method Overriding (Runtime Polymorphism/ dynamic polymorphism) -  the child class can use the OOP
            polymorphism concept to override a method of its parent class. That allows a programmer to use one method in
            different ways depending on whether it’s invoked by an
            object of the parent class or an object of the child class.
        b) Method Overloading (Compile-time polymorphism/ static polymorphism)- a single method may perform different
            functions depending on the context in which it’s called. That is, a single method name might work in
            different ways depending on what arguments are passed to
            it.
    3) Inheritance - When one object acquires all the properties and behaviors of a parent object, it is known as
        inheritance. It provides code reusability. It is used to achieve runtime polymorphism.
    5) Operator Overloading - re-defining (reusing differently without much coding) the definition of operator
    6) Data Abstraction - Abstraction is used to hide internal details and show only functionalities.
"""


"""
    Terms used in Object Oriented Design
    1) Coupling - Loose coupling is good, tight coupling is bad
    2) Cohesion - Highly cohesive is good
    3) Association - There can be four types of association between the objects:
            - One to One
            - One to Many
            - Many to One
            - Many to Many
    4) Aggregation - Aggregation is a way to achieve Association. Aggregation represents the relationship where one 
        object contains other objects as a part of its state. It represents the weak relationship between objects
    5) Composition - The composition is also a way to achieve Association. The composition represents the relationship 
        where one object contains other objects as a part of its state. There is a strong relationship between the 
        containing object and the dependent object. It is the state where containing objects do not have an independent 
        existence. If you delete the parent object, all the child objects will be deleted automatically.
        """