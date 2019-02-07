# tv2 - Terminal Velocity 2

tv2 is a fast note-taking app for the UNIX terminal, that focuses on letting you create or find a note as quickly and easily as possible, then uses your `$EDITOR` to open and edit the note. It is heavily inspired by the OS X app [Notational Velocity](http://notational.net/). For screenshots and features, see the [Terminal Velocity website](https://github.com/terminal-velocity-notes/terminal_velocity).

## Installation

### pip - Python package manager
To install Terminal Velocity, run:

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

## Releasing to PyPi

To release a new version of Terminal Velocity 2:

1.  Make sure you have setup your \~/.pypirc file for PyPi uploading
2.  Increment the version number in the [setup.py file](setup.py), add an entry to the [changelog](CHANGELOG.txt), commit both changes to git and push them to github. For example, see [aae87b](https://github.com/seanh/terminal_velocity/commit/aae87bcc50f88037b8fc76c78c0da2086c5e89ae).
3.  Upload the new release to [the tv2 package on pypi](https://pypi.python.org/pypi/tv2): run `python setup.py sdist upload -r pypi`.

For more information see <https://packaging.python.org/>.

To contribute code to Terminal Velocity, see
[CONTRIBUTING](https://github.com/makyo/tv2/blob/master/CONTRIBUTING.md#contributing-to-terminal-velocity).

