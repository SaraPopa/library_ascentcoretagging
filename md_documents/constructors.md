{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 ---\
title: "Constructors - C# Programming Guide"\
ms.date: 05/05/2017\
helpviewer_keywords: \
  - "constructors [C#]"\
  - "classes [C#], constructors"\
  - "C# language, constructors"\
ms.assetid: df2e2e9d-7998-418b-8e7d-890c17ff6c95\
---\
# Constructors (C# Programming Guide)\
\
Whenever a [class](../../language-reference/keywords/class.md) or [struct](../../language-reference/builtin-types/struct.md) is created, its constructor is called. A class or struct may have multiple constructors that take different arguments. Constructors enable the programmer to set default values, limit instantiation, and write code that is flexible and easy to read. For more information and examples, see [Using Constructors](./using-constructors.md) and [Instance Constructors](./instance-constructors.md).  \
\
## Parameterless constructors\
  \
If you don't provide a constructor for your class, C# creates one by default that instantiates the object and sets member variables to the default values as listed in the [Default values of C# types](../../language-reference/builtin-types/default-values.md) article. If you don't provide a constructor for your struct, C# relies on an *implicit parameterless constructor* to automatically initialize each field to its default value. For more information and examples, see [Instance constructors](instance-constructors.md).  \
\
## Constructor syntax\
\
A constructor is a method whose name is the same as the name of its type. Its method signature includes only the method name and its parameter list; it does not include a return type. The following example shows the constructor for a class named `Person`.\
\
[!code-csharp[constructors](../../../../samples/snippets/csharp/programming-guide/classes-and-structs/constructors1.cs#1)]  \
\
If a constructor can be implemented as a single statement, you can use an [expression body definition](../statements-expressions-operators/expression-bodied-members.md). The following example defines a `Location` class whose constructor has a single string parameter named *name*. The expression body definition assigns the argument to the `locationName` field.\
\
[!code-csharp[expression-bodied-constructor](../../../../samples/snippets/csharp/programming-guide/classes-and-structs/expr-bodied-ctor.cs#1)]  \
\
## Static constructors\
\
The previous examples have all shown instance constructors, which create a new object. A class or struct can also have a static constructor, which initializes static members of the type.  Static constructors are parameterless. If you don't provide a static constructor to initialize static fields, the C# compiler initializes static fields to their default value as listed in the [Default values of C# types](../../language-reference/builtin-types/default-values.md) article.\
\
The following example uses a static constructor to initialize a static field.\
\
[!code-csharp[constructors](../../../../samples/snippets/csharp/programming-guide/classes-and-structs/constructors1.cs#2)]  \
\
You can also define a static constructor with an expression body definition, as the following example shows.\
\
[!code-csharp[constructors](../../../../samples/snippets/csharp/programming-guide/classes-and-structs/constructors1.cs#3)]  \
\
For more information and examples, see [Static Constructors](./static-constructors.md).  \
  \
## In This Section  \
 [Using Constructors](./using-constructors.md)  \
  \
 [Instance Constructors](./instance-constructors.md)  \
  \
 [Private Constructors](./private-constructors.md)  \
  \
 [Static Constructors](./static-constructors.md)  \
  \
 [How to write a copy constructor](./how-to-write-a-copy-constructor.md)\
}