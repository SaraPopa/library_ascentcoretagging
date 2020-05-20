{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
---\
title: "Arrays as Objects - C# Programming Guide"\
ms.date: 07/20/2015\
helpviewer_keywords:\
  - "arrays [C#], as objects"\
ms.assetid: f76d4403-bd0a-42a0-9bc8-694c55b2c926\
---\
# Arrays as Objects (C# Programming Guide)\
\
In C#, arrays are actually objects, and not just addressable regions of contiguous memory as in C and C++. <xref:System.Array> is the abstract base type of all array types. You can use the properties and other class members that <xref:System.Array> has. An example of this is using the <xref:System.Array.Length%2A> property to get the length of an array. The following code assigns the length of the `numbers` array, which is `5`, to a variable called `lengthOfNumbers`:\
\
[!code-csharp[csProgGuideArrays#3](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideArrays/CS/Arrays.cs#3)]\
\
The <xref:System.Array> class provides many other useful methods and properties for sorting, searching, and copying arrays.\
\
## Example\
\
This example uses the <xref:System.Array.Rank%2A> property to display the number of dimensions of an array.\
\
[!code-csharp[csProgGuideArrays#2](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideArrays/CS/Arrays.cs#2)]\
}