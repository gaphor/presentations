% The State of Python in GNOME
% Dan Yeaw (@danyeaw:gnome.org), Arjan Molenaar (@amolenaar:gnome.org)
% July 24, 2025

## About Us

```{=latex}
\begin{center}
```
![](picture.jpg)
```{=latex}
\end{center}
```

- Arjan Molenaar

- Dan Yeaw (pronounced: Yaw)
- Originally from California, now live in Michigan

- PyGObject and Gaphor

::: notes

2 min.

Hi, I'm Dan Yeaw and I'm Arjan Molenaar, and we are sooo excited to talk to you
about Showing up for Python in GNOME!!

We have been helping to maintain PyGObject and have been GNOME Foundation members
for the last couple years.

Arjan:

Dan:
As Engineering Manager for Open Source Software at Anaconda, I lead teams working on projects including BeeWare, PyScript, Jupyter, and fsspec. Over the past seven years, I've been actively contributing to open source projects while building the Michigan Python community as a leader and organizer.

We also help maintain a Python GTK app called Gaphor which is a GNOME Circle app for doing SysML and UML modeling. I also help maintain Gvsbuild which is a build system for GTK on Windows.

:::

## The Easy Door to GNOME

- Python is the most used programming language in the world
- With other language bindings, PyGObject allows new and experienced developers to easily build apps

::: notes

1 min. Is there a new app we could highlight here?

:::

## GNOME Python

- PyGObject is the GTK and related library bindings for Python

![](app-icons.png){height=65%}

::: notes

2 min. PyGObject is Python in GNOME. It is the successor to PyGTK that James Henstridge started in 1998 that uses gobject-introspection directly to allow you to build GNOME apps using Python. If you see the patterns in the app icons here, those deep interests that people geek out on includes drawing and art, modeling, graphing, music, genealogy, manga, classic gaming, and scientific reports.

:::

## Improvements to AsyncIO Support

- Improvements to Async Constructors
- Fix a bug with big endian architectures
- Add finish_func to determine if a function can be awaitable

::: notes

4 min. Last year we released Benjamin Berg's great work to add asyncio support as a beta feature. This year we made improvements and fixed bugs, especially around how to construct new objects. We also added extensive documentation. This has been a great feature that got even better over the last year.

:::

## Enhanced documentation and examples

- https://pygobject.gnome.org
- Added documentation on asyncio usage
- Finished migrating all docs to a central place with the PyData Sphinx theme

::: notes

2 min.

:::

## Python code examples

- As a test, we added Python code examples to GtkSourceView


::: notes

We would need to see if we can get our docs generator to check for these code blocks if we are going to talk about it. This could also be a call to action to add more Python code examples.

## Code formatting and linting

::: notes

2 min. We'll have to get this MR merged if we are going to discuss this.

:::

## Migration to girepository 2.0

- PyGObject 3.52 moved to girepository 2.0
- The migration caused pain for many downstream projects

::: notes

3 min. Upgrading to girepository 2.0 helped modernize PyGObject and added the following benefits .... However, it also caused a lot of pain with downstream users of PyGObject. If we had to do it again we would have included a major version bump as part of the change. Is there some way we could have kept some backwards compatability longer?

:::

## Automatic release pipeline

- Using the GNOME Release Pipeline
- Improves automation and security

::: notes

3 min. In December, Jordan Petridis and others delivered a new CI/CD pipeline release service. Instead of us manually uploading tarballs after a release, this new service helps make sure all tests pass, and then provides automatic upload of release assets. This improves automation and security.

:::

## Other improvements

::: notes

5 min.

:::

## What's Next in GNOME Python (10 min total)

* Continuing to improve APIs and Python API doc examples (4 min)
* Vision and roadmap for the future (6 min)

## Future enhancements

- Add Python 3.14 updates for asyncio

## Wrap-up (7 min total)

* Call to action: How to get involved (3 min)
* Resources and support channels (2 min)
* Contact information and Q&A invitation (2 min)

## Call to Action

https://gitlab.gnome.org/GNOME/pygobject

- Contributions of any kind will help continue to help the community thrive
- Submit and help triage issues
- Continue to help us improve the docs
- Help us fix bugs and implement features
- Add examples to Workbench
- Build projects with PyGObject
- Chat with us at #python:gnome.org

::: notes
Many of you have even more ideas on what we could improve next, and we would love to have your contributions!

:::

## Wrap Up

### Thanks!
Thank you so much to everyone who has contributed to PyGObject!

### License
Creative Commons Attribution-Noncommercial (CC BY-NC)

### Slides
https://github.com/gaphor/presentations/tree/main/state-of-python-in-gnome-2025

# Questions?
