{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 ---\
title: "How to publish events that conform to .NET Framework Guidelines - C# Programming Guide"\
ms.date: 07/20/2015\
helpviewer_keywords: \
  - "events [C#], implementation guidelines"\
ms.assetid: 9310ae16-8627-44a2-b08c-05e5976202b1\
---\
# How to publish events that conform to .NET Framework Guidelines (C# Programming Guide)\
The following procedure demonstrates how to add events that follow the standard .NET Framework pattern to your classes and structs. All events in the .NET Framework class library are based on the <xref:System.EventHandler> delegate, which is defined as follows:  \
  \
```csharp  \
public delegate void EventHandler(object sender, EventArgs e);  \
```  \
  \
> [!NOTE]\
> The .NET Framework 2.0 introduces a generic version of this delegate, <xref:System.EventHandler%601>. The following examples show how to use both versions.  \
  \
 Although events in classes that you define can be based on any valid delegate type, even delegates that return a value, it is generally recommended that you base your events on the .NET Framework pattern by using <xref:System.EventHandler>, as shown in the following example.  \
  \
### To publish events based on the EventHandler pattern  \
  \
1. (Skip this step and go to Step 3a if you do not have to send custom data with your event.) Declare the class for your custom data at a scope that is visible to both your publisher and subscriber classes. Then add the required members to hold your custom event data. In this example, a simple string is returned.  \
  \
    ```csharp  \
    public class CustomEventArgs : EventArgs  \
    \{  \
        public CustomEventArgs(string s)  \
        \{  \
            msg = s;  \
        \}  \
        private string msg;  \
        public string Message  \
        \{  \
            get \{ return msg; \}  \
        \}\
    \}  \
    ```  \
  \
2. (Skip this step if you are using the generic version of <xref:System.EventHandler%601> .) Declare a delegate in your publishing class. Give it a name that ends with *EventHandler*. The second parameter specifies your custom EventArgs type.  \
  \
    ```csharp  \
    public delegate void CustomEventHandler(object sender, CustomEventArgs a);  \
    ```  \
  \
3. Declare the event in your publishing class by using one of the following steps.  \
  \
    1. If you have no custom EventArgs class, your Event type will be the non-generic EventHandler delegate. You do not have to declare the delegate because it is already declared in the <xref:System> namespace that is included when you create your C# project. Add the following code to your publisher class.  \
  \
        ```csharp  \
        public event EventHandler RaiseCustomEvent;  \
        ```  \
  \
    2. If you are using the non-generic version of <xref:System.EventHandler> and you have a custom class derived from <xref:System.EventArgs>, declare your event inside your publishing class and use your delegate from step 2 as the type.  \
  \
        ```csharp  \
        public event CustomEventHandler RaiseCustomEvent;  \
        ```  \
  \
    3. If you are using the generic version, you do not need a custom delegate. Instead, in your publishing class, you specify your event type as `EventHandler<CustomEventArgs>`, substituting the name of your own class between the angle brackets.  \
  \
        ```csharp  \
        public event EventHandler<CustomEventArgs> RaiseCustomEvent;  \
        ```  \
  \
## Example  \
 The following example demonstrates the previous steps by using a custom EventArgs class and <xref:System.EventHandler%601> as the event type.  \
  \
 [!code-csharp[csProgGuideEvents#2](~/samples/snippets/csharp/VS_Snippets_VBCSharp/csProgGuideEvents/CS/Events.cs#2)]  \
}