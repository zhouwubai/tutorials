# CPlusPlusCheetSheet

# Inheritance
A derived class inherits all base class methods with the following exceptions:
- Constructors, destructors
- Overloaded operators
- The friend functions
A class can be derived from multiple classes by specifying the base classes in a comma-separated list.
For example: class Daughter: public Mother, public Father


When inheriting classes, the base class' constructor and destructor are not inherited.
However, they are being called when an object of the derived class is created or deleted.


# Access Specifiers
Access specifiers are also used to specify the type of inheritance.
Remember, we used public to inherit the Daughter class:
class Daughter: public Mother

private and protected access specifiers can also be used here.

Public Inheritance: public members of the base class become public members of the derived class and protected members of the base class become protected members of the derived class. A base class's private members are never accessible directly from a derived class, but can be accessed through calls to the public and protected members of the base class.

Protected Inheritance: public and protected members of the base class become protected members of the derived class.

Private Inheritance: public and protected members of the base class become private members of the derived class.
Public inheritance is the most commonly used inheritance type.
If no access specifier is used when inheriting classes, the type becomes private by default.


# Polymorphism
The word polymorphism means "having many forms".
Typically, polymorphism occurs when there is a hierarchy of classes and they are related by inheritance.

C++ polymorphism means that a call to a member function will cause a different implementation to be executed depending on the type of object that invokes the function.
Simply, polymorphism means that a single function can have a number of different implementations.


