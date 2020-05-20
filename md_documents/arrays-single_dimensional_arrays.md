{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
---\
title: "Single-Dimensional Arrays - C# Programming Guide"\
ms.date: 07/20/2015\
helpviewer_keywords: \
  - "single-dimensional arrays [C#]"\
  - "arrays [C#], single-dimensional"\
ms.assetid: 2cec1196-1de0-49d2-baf2-c607c33310e8\
---\
# Single-Dimensional Arrays (C# Programming Guide)\
\
You can declare a single-dimensional array of five integers as shown in the following example:  \
  \
 [!code-csharp[csProgGuideArrays#4](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideArrays/CS/Arrays.cs#4)]  \
  \
 This array contains the elements from `array[0]` to `array[4]`. The [new](../../language-reference/operators/new-operator.md) operator is used to create the array and initialize the array elements to their default values. In this example, all the array elements are initialized to zero.  \
  \
 An array that stores string elements can be declared in the same way. For example:  \
  \
 [!code-csharp[csProgGuideArrays#5](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideArrays/CS/Arrays.cs#5)]  \
  \
## Array Initialization\
\
 It is possible to initialize an array upon declaration, in which case, the length specifier is not needed because it is already supplied by the number of elements in the initialization list. For example:  \
  \
 [!code-csharp[csProgGuideArrays#6](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideArrays/CS/Arrays.cs#6)]  \
  \
 A string array can be initialized in the same way. The following is a declaration of a string array where each array element is initialized by a name of a day:  \
\
 ```csharp\
 string[] weekDays = new string[] \{ "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" \};\
 ```\
  \
 When you initialize an array upon declaration, you can use the following shortcuts:  \
  \
 [!code-csharp[csProgGuideArrays#8](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideArrays/CS/Arrays.cs#8)]  \
  \
 It is possible to declare an array variable without initialization, but you must use the `new` operator when you assign an array to this variable. For example:  \
  \
 [!code-csharp[csProgGuideArrays#9](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideArrays/CS/Arrays.cs#9)]  \
  \
 C# 3.0 introduces implicitly typed arrays. For more information, see [Implicitly Typed Arrays](./implicitly-typed-arrays.md).  \
  \
## Value Type and Reference Type Arrays\
\
 Consider the following array declaration:  \
  \
 [!code-csharp[csProgGuideArrays#10](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideArrays/CS/Arrays.cs#10)]  \
  \
 The result of this statement depends on whether `SomeType` is a value type or a reference type. If it is a value type, the statement creates an array of 10 elements, each of which has the type `SomeType`. If `SomeType` is a reference type, the statement creates an array of 10 elements, each of which is initialized to a null reference.  \
  \
For more information about value types and reference types, see [Value types](../../language-reference/builtin-types/value-types.md) and [Reference types](../../language-reference/keywords/reference-types.md).\
\
}