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

# Make Your Application Multi-Platform!

Notes:

Hi I'm Arjan Molenaar and I am a software engineer working for Xebia in The
Netherlands. I've been involved in numerous projects ranging from financial
systems to embedded applications. I'm a long time GNOME user and core
contributor to a modeling tool called Gaphor.

Hi my name is Dan Yeaw. I work for Ford Motor Company in Michigan where I help
design safety in to complex software-based automated and electrified
technologies. In my free time, I have been working on an open source tool used
to model these complex system designs. That's how I got involved in contributing
with Arjan on Gaphor.

---

## What are we talking about

> rough talk outline (draft)

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
   - macOS releases often break packaging - signing
1. Take aways: Approach each platform separately. work with upstream projects. Consolidate

Note: speaker notes FTW!

---

## Why go multi-platform

1. Broader user base
1. Feels more future proof (dog fooding / using at work)
1. Reaches people unfamiliar with Open Source

Notes:

Most issues have been raised by Windows users.

---

## Community 

---

## Target

All major desktop platforms:
Windows, macOS, Linux
---
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