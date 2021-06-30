---
title: Open STPA with RAAML and Gaphor
theme: white
highlight-theme: atom-one-dark
revealOptions:
    transition: none
    slideNumber: c
    controls: false
    progress: false
---

# Open STPA with RAAML and Gaphor

2021 STAMP Workshop

Dan Yeaw &amp; Kyle Post

<img src="images/raaml-gaphor.png" height=250>

Notes:

Hi my name is Dan Yeaw. I work for Ford Motor Company where I am a Manager and
Technical Lead for Functional Safety in Product Development.  In my free time,
I have been working on an open source tool used to model these complex system
designs. That's how I got involved in contributing with Gaphor. I also like to
ride bicycles!

Hi I'm Kyle Post. I also work for Ford and I'm the Technical Leader for Systems
Safety in the Research and Advanced Engineering area. I have been leading the
Risk Analysis and Assessment Modeling Language (RAAML) OMG standard.

---

## A Vibrant Community

We want to build an open community for systems safety

- A low barrier to join, learn, and grow 👥
- Diverse contributors who want to help 🔨
- Built on open standards and open source software

Notes:

---

## Safety Standards

- Each industry has developed domain specific standards, most derived fom IEC 61508
- New techniques, like STPA, can improve how we do safety analysis
- However, may lack rigor without a standardized and consistent language and automation

---

## RAAML

- Precise language for systems safety
- OMG spec 1.0 beta available, final release soon 
- STPA metamodel library based on the STPA Handbook
- Facilitates exchange of info between tools and organizations

Notes:

The Risk Analysis and Assessment Language

---

## Gaphor

- An open source UML, SysML, and now RAAML modeling tool written in Python
- Fast and easy to use, while still having a full data model
- Improves rigor through consistency, helps add automation

---

# Demo

---

Step 1: Define Purpose of the Analysis
<img src="images/losses-hazards.png" height=400>

---

Step 2: Model the Control Structure
<img src="images/control-structure.png" height=500>

---

Step 3: Identify Unsafe Control Actions
<img src="images/unsafe-control-actions.png">

---

Step 4: Identify Loss Scenarios
<img src="images/loss-scenarios.png">

---

For more information see:

https://omg.org/spec/RAAML

https://gaphor.org
