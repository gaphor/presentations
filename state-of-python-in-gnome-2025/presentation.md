% The State of Python in GNOME
% Dan Yeaw (@danyeaw:gnome.org), Arjan Molenaar (@amolenaar:gnome.org)
% July 24, 2025 - Creative Commons Attribution-Noncommercial (CC BY-NC)


## About Us

::: columns

:::: column
Arjan Molenaar

- From The Netherlands
- PyGObject and Gaphor
- GTK on macOS
::::

:::: column
Dan Yeaw (pronounced: Yaw)

- Originally from California, now live in Michigan

- PyGObject and Gaphor
- Gvsbuild
::::

:::

::: notes

Hi, I'm Dan Yeaw and I'm Arjan Molenaar, and we are sooo excited to talk to you
about Showing up for Python in GNOME!!

We have been helping to maintain PyGObject and have been GNOME Foundation members
for the last couple years.

Arjan:
I'm a software consultant by day, open source hacker by night. Live in The Netherlands.
Since roughly a year I've been maintaining PyGObject. Apart from that I try to improve
the support for GTK on macOS.

Dan:
As Engineering Manager for Open Source Software at Anaconda, I lead teams
working on projects including BeeWare, PyScript, Jupyter, and fsspec. Over the
past seven years, I've been actively contributing to open source projects while
building the Michigan Python community as a leader and organizer.

We also help maintain a Python GTK app called Gaphor which is a GNOME Circle
app for doing SysML and UML modeling. I also help maintain Gvsbuild which is
a build system for GTK on Windows.

:::

## GNOME Python

PyGObject is the GTK and related library bindings for Python

![](app-icons.png){height=65%}

::: notes

PyGObject is Python in GNOME. It is the successor to PyGTK that James Henstridge started in 1998 that uses the girepository library to allow you to build GNOME apps using Python. If you see the patterns in the app icons here, those deep interests that people geek out on includes drawing and art, modeling, graphing, music, genealogy, manga, classic gaming, and scientific reports.

:::

## What's New in GNOME Python

* Improvements to AsyncIO support
* Enhanced documentation and examples
* Code formatting and linting
* Migration to girepository 2.0
* Automatic release pipeline
* Other notable improvements

## Improvements to AsyncIO support

It's easier to start using `asyncio`:

```python
app = Adw.Application(...)

with gi.events.GLibEventLoopPolicy():
    app.run()
```

Kudos to Benjamin Berg

## Enhanced documentation and examples

::: columns

:::: column
* The documentation is built using PyGObject.
* Only GNOME core libs.
* Recently added docs for async methods.
* GTK 3 docs are still available on https://lazka.github.io/pgi-docs/
::::

:::: column
![](api-docs.png){height=65%}

https://api.pygobject.gnome.org
::::

:::

## Migration to girepository 2.0

* Improved the code base

* Unfortunate fallout: apps not able to upgrade due to dependency on gobject-introspection

## What's Next in GNOME Python

* Continuing to improve APIs and Python API doc examples

* Reduce the amount of custom code (pygtkcompat, option parser)

## Vision and roadmap for the future

* PyGObject is mature

* Take advantage of new Python features

* A local documentation browser for all GI libraries on your system?

::: notes

:::

## Call to Action

https://gitlab.gnome.org/GNOME/pygobject

- Contributions of any kind will help continue to help the community thrive
- Submit and help triage issues
- Continue to help us improve the docs
- Help us fix bugs and implement features
- Add examples to Workbench
- Build projects with PyGObject
- Chat with us at #python:gnome.org
- Blog and create videos

::: notes
Many of you have even more ideas on what we could improve next, and we would love to have your contributions!

:::

## Wrap Up

Thank you so much to everyone who has contributed to PyGObject!

Slides:
https://github.com/gaphor/presentations/tree/main/state-of-python-in-gnome-2025

# Questions?
