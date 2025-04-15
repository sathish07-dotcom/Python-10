
## **1. Single Inheritance**

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound())  # Output: Bark




## **2. Access Parent Class Method in Child Class**

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return super().sound() + " and Bark"

dog = Dog()
print(dog.sound())  # Output: Some sound and Bark




## **3. Single Inheritance with `__init__` Method**

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def display(self):
        print("Child name:", self.name)

c = Child("Sathish")
c.display()




## **4. Single Inheritance with Additional Attributes**

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

c = Car("Tesla", "Model S")
print(c.brand, c.model)  # Output: Tesla Model S




## **5. Multiple Inheritance**

class Father:
    def skills(self):
        return "Coding"

class Mother:
    def skills(self):
        return "Painting"

class Child(Father, Mother):
    def all_skills(self):
        return f"{super().skills()} and {Mother.skills(self)}"

c = Child()
print(c.all_skills())  # Output: Coding and Painting




## **6. Multiple Inheritance with `super()`**

class A:
    def show(self):
        return "Class A"

class B:
    def show(self):
        return "Class B"

class C(A, B):
    def show(self):
        return super().show() + " and " + B.show(self)

c = C()
print(c.show())  # Output: Class A and Class B




## **7. Multilevel Inheritance**

class Grandparent:
    def family_name(self):
        return "Singh"

class Parent(Grandparent):
    def parent_info(self):
        return "Parent Info"

class Child(Parent):
    def child_info(self):
        return "Child Info"

c = Child()
print(c.family_name(), c.parent_info(), c.child_info())  




## **8. Hybrid Inheritance**

class A:
    def method_A(self):
        return "Method A"

class B(A):
    def method_B(self):
        return "Method B"

class C(A):
    def method_C(self):
        return "Method C"

class D(B, C):
    def method_D(self):
        return "Method D"

d = D()
print(d.method_A(), d.method_B(), d.method_C(), d.method_D())  




## **9. Hierarchical Inheritance**

class Parent:
    def parent_method(self):
        return "Parent Method"

class Child1(Parent):
    def child1_method(self):
        return "Child1 Method"

class Child2(Parent):
    def child2_method(self):
        return "Child2 Method"

c1 = Child1()
c2 = Child2()
print(c1.parent_method(), c1.child1_method())  
print(c2.parent_method(), c2.child2_method())  




## **10. Overriding Parent Class Method**

class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

c = Child()
print(c.greet())  # Output: Hello from Child




## **11. Calling Parent’s Overridden Method**

class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return super().greet() + " and Hello from Child"

c = Child()
print(c.greet())  # Output: Hello from Parent and Hello from Child




## **12. Using `super()` to Call Parent Constructor**

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = Child()




## **13. Multiple Inheritance with Conflicting Methods**

class A:
    def show(self):
        return "Class A"

class B:
    def show(self):
        return "Class B"

class C(A, B):
    pass

c = C()
print(c.show())  # Output: Class A (depends on method resolution order)




## **14. Checking Instance of Class (`isinstance()`)**

class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))  # Output: True
print(isinstance(d, Animal))  # Output: True




## **15. Checking Subclass (`issubclass()`)**

class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))  # Output: True
print(issubclass(Parent, Child))  # Output: False




## **16. Accessing Parent Attributes with `super()`**

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

c = Child("Sathish", 25)
print(c.name, c.age)  # Output: Sathish 25




## **17. Polymorphism in Inheritance**

class Animal:
    def make_sound(self):
        return "Animal Sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.make_sound())  




## **18. Abstract Class in Inheritance**

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

d = Dog()
print(d.sound())  




## **19. Using `super()` in Multilevel Inheritance**

class A:
    def method(self):
        return "Method in A"

class B(A):
    def method(self):
        return super().method() + " -> Method in B"

class C(B):
    def method(self):
        return super().method() + " -> Method in C"

c = C()
print(c.method())  




## **20. Preventing Inheritance with `final` Method**

class Parent:
    def show(self):
        return "Final Method"

class Child(Parent):
    def show(self):
        return super().show() + " (Overridden)"

c = Child()
print(c.show())  




