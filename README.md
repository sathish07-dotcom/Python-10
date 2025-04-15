
# 📘 Inheritance in Python

## 🧠 Overview
**Inheritance** is a key concept in **Object-Oriented Programming (OOP)** that allows a class to inherit methods and properties from another class. It enables **code reusability**, improves **code structure**, and supports **modular design**.

---

## 📚 Key Concepts

### 🔹 Base Class (Parent)
The class whose properties and methods are inherited.

### 🔹 Derived Class (Child)
The class that inherits from the base class.

---

## ✅ Syntax

```python
class Parent:
    def speak(self):
        print("I am the parent class")

class Child(Parent):
    def talk(self):
        print("I am the child class")

# Creating an object of Child
obj = Child()
obj.speak()  # Inherited from Parent
obj.talk()
```

---

## 🧩 Types of Inheritance

### 1. Single Inheritance
```python
class A:
    pass

class B(A):
    pass
```

### 2. Multiple Inheritance
```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

### 3. Multilevel Inheritance
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

### 4. Hierarchical Inheritance
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass
```

### 5. Hybrid Inheritance
A combination of more than one type of inheritance.

---

## ⚙️ `super()` Function
Used to call the constructor or methods of the parent class.

```python
class Parent:
    def __init__(self):
        print("Parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class")
```

---

## 🔁 Method Overriding
Child class redefines a method from the parent class.

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

obj = Child()
obj.greet()  # Output: Hello from Child
```

---

## 🔍 Useful Built-in Functions
- `isinstance(obj, ClassName)` → Checks if an object is an instance of a class.
- `issubclass(SubClass, ParentClass)` → Checks if a class is a subclass of another.

---

## 📌 Real-Life Example

```python
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Barks")

d = Dog()
d.sound()  # Output: Barks
```

---

## 📝 Summary

| Concept            | Description                         |
|--------------------|-------------------------------------|
| Inheritance        | Deriving a new class from a parent  |
| `super()`          | Calls parent class method/constructor |
| Method Overriding  | Redefining parent method in child   |
| `isinstance()`     | Checks object-class relation        |
| `issubclass()`     | Checks subclass-parent relation     |

--
