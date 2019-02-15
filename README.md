# tv2 - Terminal Velocity 2

tv2 is a fast note-taking app for the UNIX terminal, that focuses on letting you create or find a note as quickly and easily as possible, then uses your `$EDITOR` to open and edit the note. It is heavily inspired by the OS X app [Notational Velocity](http://notational.net/). For screenshots and features, see the [Terminal Velocity website](https://tv2.projects.makyo.io).

## Installation

### pip - Python package manager
To install tv2, run:

    pip3 install tv2

Then to launch it just run:

    tv2

To use a different notes directory, run:

    tv2 path/to/your/notes/dir

To see all the command-line options, run:

    tv2 -h

To quit the app, press `ctrl-c` or `ctrl-x`.

To upgrade tv2 to the latest version, run:

    pip install --upgrade tv2

To uninstall it, run:

    pip uninstall tv2

### From Source

Ensure python modules `urwid`, `setuptools`  and `chardet` are installed. Python-dev also.

```
apt install python-setuptools python-chardet python-urwid python-dev
```

Clone the repository from:

    https://github.com/makyo/tv2.git

Move into tv2 directory you just cloned and run the following:

    sudo python setup.py install

## Contributing

To contribute code to Terminal Velocity, see
[CONTRIBUTING](/CONTRIBUTING.md#contributing-to-terminal-velocity).

[![Support me on Patreon](https://img.shields.io/badge/patreon-support-%23222222.svg)](https://patreon.com/makyo)
[![Buy me a Coffee](https://img.shields.io/badge/kofi-support-%23222222.svg)](https://ko-fi.com/drabmakyo)
[![Support me on LiberaPay](https://img.shields.io/badge/liberapay-support-%23222222.svg)](https://liberapay.com/makyo)

