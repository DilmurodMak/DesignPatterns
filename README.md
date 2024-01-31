<!-- omit in toc -->
# Design Patterns 
- [Strategy Pattern](#strategy-pattern)
- [Observer Pattern](#observer-pattern)
- [Decorator Pattern](#decorator-pattern)
- [Factory Pattern](#factory-pattern)
- [Singleton Pattern](#singleton-pattern)
- [Command Pattern](#command-pattern)
- [Adapter and Facade Pattern](#adapter-and-facade-pattern)
- [Template Method Pattern](#template-method-pattern)
- [Iterator and Composite Pattern](#iterator-and-composite-pattern)
- [State Pattern / Proxy Pattern](#state-pattern--proxy-pattern)
- [Compound Pattern](#compound-pattern)
- [Patterns in the Real World](#patterns-in-the-real-world)
  - [Pattern Categories](#pattern-categories)
  - [Classification of Patterns](#classification-of-patterns)

Strategy Pattern
----------------

![Strategy Pattern](./Images/1_strategy_pattern.png)

Strategy - defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

1) Identify the aspects of your application that vary and separate them from what stays the same.
2) Program to an interface, not an implementation.
3) Favor composition over inheritance.
   
[Duck Simulator Code Sample](./1.%20Strategy%20Pattern/MiniDuckSimulator.py)


Observer Pattern
----------------

![Observer Pattern](./Images/2_observer_pattern.png)

Observer - defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically

1) Strive for loosely coupled designs between objects that interact.

[Weather Station Code Sample](./2.%20Observer%20Pattern/main.py)


Decorator Pattern
-----------------

![Decorator Pattern](./Images/3_decorator_pattern.png)

Decorator - attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

1) Classes should be open for extension, but closed for modification.

[Starbuzz Coffee Code Sample](./3.%20Decorator%20Pattern/main.py)

Factory Pattern
-----------------

![Factory Pattern](./Images/4_factory_pattern_a.png)
![Factory Pattern](./Images/4_factory_pattern_b.png)

Abstract Factory - Provides an interface for creating families of related or dependent objects without
specifying their concrete classes.

Factory Method - Defines an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to the
subclasses.

1) Depend upon abstractions. Do not depend upon concrete classes.

[Pizza Factory Code Sample](./4.%20Factory%20Pattern/main.py)

Singleton Pattern
-----------------

![Singleton Pattern](./Images/5_singleton_pattern.png)

Singleton - ensures a class has only one instance, and provides a global point of access to it.

[Chocolate Boiler Code Sample](./5.%20Singleton%20Pattern/main.py)

Command Pattern
-----------------

![Command Pattern](./Images/6_command_pattern.png)

Command - encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

[Remote Control Code Sample](./6.%20Command%20Pattern/main.py)

Adapter and Facade Pattern
-----------------

![Adapter Pattern](./Images/7_adapter_pattern.png)
![Facade Pattern](./Images/7_facade_pattern.png)

Adapter - converts the interface of a class into another interface the clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.

Pattern | Intent
--- | ---
Decorator | Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
Adapter | Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.
Facade | Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

Design Principle:
- Principle of Lease Knowledge: Talk only to your immediate friends.
  
This principle prevents us from creating designs that have a large number of classes coupled together so that changes in one part of the system cascade to other parts.

[Duck Adapter Code Sample](./7.%20Adapter%20and%20Facade%20Patterns/adapter.py)

[Home Theatre Facade Code Sample](./7.%20Adapter%20and%20Facade%20Patterns/facade.py)

Template Method Pattern
-----------------

![Template Method Pattern](./Images/8_template_method_pattern.png)
![Hollywood Principle](./Images/8_hollywood_principle.png)

Template Method - defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.

Hollywood Principle: Don’t call us, we’ll call you.

With the Template Method, we allow low-level components to hook themselves into a system, but the high-level components determine when they are needed, and how.

Patterns | Description
--- | ---
Template Method | Defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.
Strategy | Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
Factory Method | Defines an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to the subclasses.

[Caffeine Beverage Code Sample](./8.%20Template%20Method%20Pattern/main.py)

Iterator and Composite Pattern
-----------------

![Iterator Pattern](./Images/9_itterator_and_composite_pattern.png)
![Composite Pattern](./Images/9_itterator_composite_b.png)

Iterator - provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

Composite - compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

Design Principle: A Class should have only one reason to change.

Cohesion - is a term that is used to indicate how focused and single-minded a class is. A class with high cohesion has a single purpose or responsibility and the class is well-focused on that purpose. A class with low cohesion has many purposes or responsibilities and is not focused on just one purpose.

[Restaurant Menu Code Sample](./9.%20Itterator%20and%20Composite%20Pattern/itterator.py)

State Pattern / Proxy Pattern
-----------------

![State Pattern](./Images/10_state_pattern.png)
![State Pattern](./Images/10_state_pattern_b.png)
![Proxy Pattern](./Images/10_proxy_pattern.png)

State - allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

Proxy - provides a surrogate or placeholder for another object to control access to it.

Pattern | Description
--- | ---
State | Encapsulates state-based behavior and delegate behavior to the current state object.
Strategy | Encapsulate interchangeable behaviors and use delegation to decide which behavior to use.
Template Method | Subclasses decide how to implement steps in an algorithm.

[Gumball Machine Code Sample](./10.%20State%20Pattern/main.py)

Compound Pattern
-----------------

![Compound Pattern](./Images/11_compound_pattern.png)

Compound - is a pattern that combines two or more patterns into a solution that solves a recurring or general problem. MVC is an example for compound pattern

[ Duck Simulator Code Sample](./11.%20Compound%20Pattern/main.py)

Patterns in the Real World
-----------------

![documenting patterns](./Images/12_documenting_patterns.png)

### Pattern Categories

- Creational Patterns
  - Abstract Factory
  - Factory Method
  - Singleton

- Structural Patterns
  - Adapter
  - Composite
  - Decorator
  - Facade
  - Proxy

- Behavioral Patterns
  - Command
  - Interpreter
  - Iterator
  - Observer
  - State
  - Strategy

### Classification of Patterns

Class Patterns:
- Class patterns deal with relationships between classes and their subclasses. These relationships are established through inheritance, so they are static—fixed at compile-time.

Template Method, Factory Method, and Interpreter are class patterns.


Object Patterns:
- describe relationships between objects and are primarily defined by composition. Relationships in object patterns are typically created at runtime and are more dynamic and flexible.

Adapter, Itterator, Decorator, Composite, State, Proxy, Facade, Command, Abstract Factory, Strategy, Singlton, and Observer are object patterns.
