# State of Python in GNOME

This repository contains a presentation for GUADEC 2025.

The format is based on the following template:

```
git clone https://gitlab.gnome.org/GNOME/presentation-templates.git
cd presentation-templates/GUADEC/2025
```

## Dependencies

### Fedora

```bash
$ dnf copr enable cimbali/pympress
$ sudo dnf install python3-pympress pandoc texlive-latex texlive-beamer texlive-ec texlive-framed texlive-mptopdf
```

### OpenSUSE

```bash
$ sudo zypper install pympress pandoc texlive-latex texlive-beamer texlive-ec texlive-framed texlive-mptopdf
```

## How Can I Create a Presentation?

You can create a presentation using Pandoc or LaTeX. Pandoc is way easier and
recommended as it will be automatically translated into LaTex.

Try it out; open your console, go to the directory where this document lies and
type `make`. This will compile the `presentation.md` into `presentation.pdf` if
you have pandoc installed.

Just look into the md and pdf file to see how you can simply create your
presentation. It's easy! Please try it out!

> **Note**:
>
> You can use `make continuous` to automatically regenerate the PDF whenever you
> touch the document. For that to work you'll need to have the `inotify-tools`
> package installed.

### Using Latex Directly

You can also use LaTeX directly. Use the `make tex` command to compile the
example tex document into a presentation.

### Speaker Notes

Configuration for beamer is in the .sty files. To change speaker note options, then edit
`beamerthemeguadec.sty` and uncomment the `\setbeameroption`.

## Present

Present with speaker notes with [pympress](https://github.com/Cimbali/pympress).

```bash
$ pympress presentation.pdf
```
