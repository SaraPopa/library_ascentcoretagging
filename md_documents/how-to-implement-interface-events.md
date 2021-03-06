{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 ---\
title: "How to implement interface events - C# Programming Guide"\
ms.date: 07/20/2015\
helpviewer_keywords: \
  - "interfaces [C#], event implementation in classes"\
  - "events [C#], in interfaces"\
ms.assetid: 63527447-9535-4880-8e95-35e2075827df\
---\
# How to implement interface events (C# Programming Guide)\
An [interface](../../language-reference/keywords/interface.md) can declare an [event](../../language-reference/keywords/event.md). The following example shows how to implement interface events in a class. Basically the rules are the same as when you implement any interface method or property.  \
  \
## To implement interface events in a class  \
  \
Declare the event in your class and then invoke it in the appropriate areas.  \
  \
```csharp\
namespace ImplementInterfaceEvents  \
\{  \
    public interface IDrawingObject  \
    \{  \
        event EventHandler ShapeChanged;  \
    \}  \
    public class MyEventArgs : EventArgs\
    \{  \
        // class members  \
    \}  \
    public class Shape : IDrawingObject  \
    \{  \
        public event EventHandler ShapeChanged;  \
        void ChangeShape()  \
        \{  \
            // Do something here before the event\'85  \
\
            OnShapeChanged(new MyEventArgs(/*arguments*/));  \
\
            // or do something here after the event.\
        \}  \
        protected virtual void OnShapeChanged(MyEventArgs e)  \
        \{  \
            ShapeChanged?.Invoke(this, e);  \
        \}  \
    \}  \
\
\}  \
```  \
  \
## Example  \
The following example shows how to handle the less-common situation in which your class inherits from two or more interfaces and each interface has an event with the same name. In this situation, you must provide an explicit interface implementation for at least one of the events. When you write an explicit interface implementation for an event, you must also write the `add` and `remove` event accessors. Normally these are provided by the compiler, but in this case the compiler cannot provide them.  \
  \
By providing your own accessors, you can specify whether the two events are represented by the same event in your class, or by different events. For example, if the events should be raised at different times according to the interface specifications, you can associate each event with a separate implementation in your class. In the following example, subscribers determine which `OnDraw` event they will receive by casting the shape reference to either an `IShape` or an `IDrawingObject`.  \
  \
 [!code-csharp[csProgGuideEvents#10](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideEvents/CS/Events.cs#10)]\
  \
}