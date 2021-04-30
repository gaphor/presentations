---
title: Make Your Application Multi-Platform!
theme: white
highlight-theme: atom-one-dark
revealOptions:
    transition: none
    slideNumber: c
    controls: false
    progress: false
---

# Make Your Application Multi&#8209;Platform!

Linux App Summit 2021

Dan Yeaw &amp; Arjan Molenaar

Notes:

Hi I'm Arjan Molenaar and I am a software consultant working for Xebia in The
Netherlands. Next to work I like to code, (bi)cycle and brew beer.

Hi my name is Dan Yeaw. I work for Ford Motor Company in Michigan where I help
design safety in to complex software-based automated and electrified
technologies. In my free time, I have been working on an open source tool used
to model these complex system designs. That's how I got involved in contributing
with Arjan on Gaphor.

---

## What are we talking about

1. Why go multi-platform
1. The case: Gaphor
1. Building for Linux - Flatpak + AppImage
1. Building for Windows
1. Building for macOS
1. Take aways

Notes:

* Who build software in their spare time?
* Desktop software?

1. Why go multi-platform (Arjan)
   - Community size is larger (platform user base and developer user base sizes)
1. What are we targetting (os, installation method, user type, automated) Arjan
   - Automatic as much as possible
   - No scary warnings during install
1. The case: Gaphor (Arjan)
1. Before you begin
   - Keep the toolset small (e.g. depend on GTK, but not on a whole lot of other libraries)
   - Avoid dependency hell
   - All dependencies need to be supported on all platforms
   - Use GTK out of the box as possible (avoid issues with GTK upgrades)
   - Keep true to the ecosystem (for Python, use pyproject.toml + a python build tool)
1. Building for Linux - Flatpak + AppImage (Dan)
   - Flatpak dependency install by building from the Python wheel
   - Separate repository in flathub
   - Differences between flatpak and appimage
   - AppImage requires build on older LIBC, challenges with not being able to use the latest GTK
1. Building for Windows (maybe switch order?) - Dan
   - Msys2 overview (familiar environment, presents challenges) - signing
   - Cooperate with upstream projects (PyInstaller)
1. Building for macOS - install script + PyInstaller - Arjan
   - Homebrew overview
   - macOS releases often break packaging - signing
   - library structure (macos libs use absolute references)
1. Take aways: Approach each platform separately. work with upstream projects. Consolidate

---

## A Vibrant Community

We want the apps we build to be useful for others!

- Users who get value out of using our app
- Diverse contributors who want to help make it better

---

<!-- .slide: data-background="images/os_market_share.svg"  -->

---

## Why go multi-platform

1. Broader & more inclusive user base
1. Helps introduce people to Open Source
1. More future proof
1. Improves adaptability - not bound to a specific OS


Notes:

Most issues have been raised by Windows users.

---

## What are we targeting

* All major desktop platforms: Windows, macOS, Linux
* Automate as much as possible
* No scary warnings during install

<img src="images/windows_logo.png" height=90><img src="images/apple_logo.png" height=100><img src="images/linux_logo.svg" height=110>

Notes:
- automate -> build all in CI

---

## The case: Gaphor

<img src="images/gaphor.png">

Notes:

(Arjan)
* A modeling tool, written in Python (~ 44000 lines)
* GTK+ 3 (soon GTK 4)
* Why did I start this project almost 20 years ago: modeling should be
facilitating the creation process and help describe a system in components.

---
# Setup for Success

---

## Painful Upgrades
- Gaphor use to have some highly customized GTK2 widgets to allow advanced window docking
- It was clever, but we would have had to rewrite all of it to upgrade GTK

```python
class CompactButton(gtk.Widget):
    __gtype_name__ = 'EtkCompactButton'
    __gsignals__ = {'clicked':
                        (gobject.SIGNAL_RUN_FIRST | gobject.SIGNAL_ACTION,
                         gobject.TYPE_NONE,
                         tuple())}
    __gproperties__ = {'icon-name-normal':
                           (gobject.TYPE_STRING,
                            'icon name normal',
                            'icon name normal',
                            '',
```

Notes:
(Dan)

@dan should we add this?
---

## Keep Things Simple
- Grab a great GUI toolkit
- Use out of the box widgets and other components
- Use a few key libraries if needed, ensure dependencies are well supported across platforms

Notes:

(Dan)
 - Keep the toolset small (e.g. depend on GTK, but not on a whole lot of other libraries)
 - Avoid dependency hell
 - All dependencies need to be supported on all platforms
 - Use GTK out of the box as possible (avoid issues with GTK upgrades)
 - Keep true to the ecosystem (for Python, use pyproject.toml + a python build tool)

---

## Stay True to the Ecosystem
- Follow the modern best practices for the language you are using
- These solutions will be tried and true
- For Python that includes pyproject.toml, black, mypy, coverage.py, flake8, pytest, tox, and isort

Notes:

@dan: I think tools like black, mypy, flake8, etc. are not relevant for the muti-platform story
---

## Linux

 - Flatpak + AppImage
 - Flatpak dependency install by building from the Python wheel
 - Separate repository in flathub
 - Differences between flatpak and appimage
 - AppImage requires build on older LIBC, challenges with not being able to use the latest GTK

Notes:

@dan: should this be split in two sheets?

---

## Windows

 - Msys2 overview (familiar environment, presents challenges)
 - Signing
 - Cooperate with upstream projects (PyInstaller)

---

## macOS

 - Homebrew
 - Signing

Notes:

* Homebrew started like BSD ports
* Signing requires an Apple Developer subscription

---
## macOS packaging

- A `.app` file in a DMG (disk image)
- Apps have a predefined directory structure

  ```bash
  Gaphor.app/Contents/Info.plist
  Gaphor.app/Contents/MacOS/gaphor
  Gaphor.app/Contents/Resources
  ```

- Library references are absolute - need relocating
- Update environment variables
- Used our own script, now rely in _PyInstaller_

Notes:

- Env vars for shared files (Font config, GI, XDG, GDK-PixBuf)
- macOS releases often break packaging

py2app is an alternative.

## macOS Signing

- Both app and dmg need signing
- All performed from buid pipeline

---

## Take aways

* Approach each platform separately
* Work with upstream projects
* Integrate platform builds in the build pipeline

---

# Questions?

Dan: @danyeaw / dan@yeaw.me

Arjan: @ajmolenaar / gaphor@gmail.com

---

## Random thoughts

Things we may or not may want to discuss in this talk.

1. Keep the toolset small (e.g. depend on GTK, but not on a whole lot of other libraries)
    - Avoid dependency hell
    - All dependencies need to be supported on all platforms
    - Use GTK out of the box as possible (avoid issues with GTK upgrades)
2. Keep true to the ecosystem (for Python, use pyproject.toml + a python build tool)
3. Work with upstream projects (in our case PyInstaller)
4. Build your CI around those platforms (GitHub is your friend here)
    - Check your packaged builds continuously
5. Costs for registering (windows) and notarizing (macos) your app vs benefits
6. Looking forward to the future
    - GTK4

- war stories
