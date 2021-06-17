---
title: Large GUI application with Python and GTK
theme: white
highlight-theme: atom-one-dark
revealOptions:
    transition: none
    slideNumber: c
    controls: false
    progress: false
---

# Large GUI application with Python and GTK

Notes:

Hi I'm Arjan Molenaar and I am a software engineer working for Xebia in The
Netherlands. I've been involved in numerous projects ranging from financial
systems to embedded applications. I'm a long time GNOME user and core
contributor to a modeling tool called Gaphor.

---

- describe qualities of used pattern
- application example

---

# Pure Python core

- Clean Architecture
- testable code base
- separation between application core and functionality

---

!image hex-arch
---

# Composition over inheritance

- Easier to manage than inheriting from widgets
- Separation of concerns
- User interaction is often done via multiple widgets

---

Example:

one of the UI components

```python
class Diagrams(UIComponent):

    def construct(self):
        ... construct widgets, set callbacks

```
---

# Extensibility

- Services
- generic functions / dynamic dispatch


---

## Services

In Python, use `entry_points`.

Defined in `pyproject.toml`:
```
[tool.poetry.plugins."gaphor.services"]
"component_registry" = "gaphor.services.componentregistry:ComponentRegistry"
"event_manager" = "gaphor.core.eventmanager:EventManager"
"undo_manager" = "gaphor.services.undomanager:UndoManager"
"element_factory" = "gaphor.core.modeling:ElementFactory"
"modeling_language" = "gaphor.services.modelinglanguage:ModelingLanguageService"
"file_manager" = "gaphor.ui.filemanager:FileManager"
```

---
## Generic functions

Multiple functions with the same name, dispatched based on the parameter type.

Logic can be added incrementally.

```python
@singledispatch
def copy(obj: object):
    # Default behavior
    raise ValueError(f"No copier for {obj}")

@copy.register
def _copy_named_element(element: NamedElement):
    return element.id, copy_named_element(element)
```
---

# Event dispatching

- object or application wide
- app wide -> event bus
- model is emiting events, everything should be able to listen
- listen on an event type

---

!image event dispatching