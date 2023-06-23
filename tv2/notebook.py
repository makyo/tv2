"""Persistent note storage and search.

This module defines the NoteBook interface and provides the PlainTextNoteBook 
implementation that store notes in a directory of plain text files.

Other implementations could store notes differently (e.g. in a database) and
provide drop-in replacements for PlainTextNoteBook and PlainTextNote by
implementing the same NoteBook and Note interfaces.

A NoteBook is a container of Notes. It behaves like a standard Python
container, e.g. you can do:

    notebook = PlainTextNoteBook("/path/to/my/notes/dir")

    note = notebook[5]

    for note in notebook:
        ...

    if note in notebook:
        ...

    len(notebook)

    reversed(notebook)

    del notebook[3]

    notebook.remove(note)

When deleting or removing a Note from a NoteBook, DelNoteError may be raised if
removing the note fails.

You should not initialise your own Note objects when working with a NoteBook,
instead use the NoteBook's add_new() method:

    try:
        note = notebook.add_new("The Title of My New Note")
    except AddNoteError:
        ...

NoteBooks also provide a search() method for doing fast, full-text search of
notes:

    matching_notes = notebook.search(query)

This module provides a simple brute force full text search implementation.
Other modules could provide better search functions that could be plugged in.

"""
import logging
logger = logging.getLogger(__name__)
import os

from pathlib import Path
from .note import PlainTextNote, InvalidNoteTitleError, NoteAlreadyExistsError
from .search import brute_force_search

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class NewNoteBookError(Error):
    """Exception raised if initialising a new NoteBook fails.

    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PlainTextNoteBook(object):
    """A NoteBook that stores its notes as a directory of plain text files."""

    def __init__(self, path, extension, extensions,
            search_function=brute_force_search, exclude=None):
        """Make a new PlainTextNoteBook for the given path.

        If `path` does not exist it will be created (parent directories too).

        If `path` does exist, any note files in path will be read and included
        in the NoteBook. Subdirectories in `path` will be read recursively.

        Raises NewNoteBookError if creating the notebook directory or reading
        the files in an existing directory fails.

        Arguments:

        path -- absolute path to the directory where this NoteBook's note files
            are kept (string)

        extension -- the filename extension to use for new notes (string)

        extensions -- the filename extensions to read in the notes dir
            (list of strings)

        search_function -- the function to call to search the notebook

        """
        # Expand ~ in path, and transform it into an absolute path.
        self._path = Path(path).expanduser().absolute()

        if extension and not extension.startswith("."):
            extension = "." + extension
        self.extension = extension
        self.search_function = search_function
        self.exclude = exclude
        if not self.exclude: self.exclude = []

        self.extensions = []
        for extension in extensions:
            if not extension.startswith("."):
                extension = "." + extension
            self.extensions.append(extension)

        # Create notebook_dir if it doesn't exist.
        if not self._path.is_dir():
            logger.debug("'{0} doesn't exist, creating it".format(self.path))
            try:
                Path.mkdir(self.path, parents=True, exist_ok=True)
            except Exception as e:
                raise NewNoteBookError(
                        "{0} could not be created: {1}".format(self.path, e))
        else:
            # TODO: Check that self.path is a directory, if not raise.
            pass

        # Read any existing note files in the notes directory.
        self._notes = []
        for root, dirs, files in os.walk(self.path):

            # ignore any dirs we don't want to check
            for name in self.exclude:
                if name in dirs:
                    dirs.remove(name)

            for filename in files:

                # ignore anything listed in our 'exclude' list
                if filename in self.exclude:
                    continue

                # Ignore hidden and backup files.
                if filename.startswith('.') or filename.endswith('~'):
                    continue

                if Path(filename).suffix not in self.extensions:
                    continue

                # Make a Note object for the file and add it to this NoteBook.
                abspath = Path(root) / filename
                subdir = abspath.relative_to(self.path).parent
                title = abspath.stem
                ext = abspath.suffix
                if title is None:
                    # The filename could not be decoded.
                    logger.error(
                            "Could not decode filename: {0}".format(title))
                else:
                    self.add_new(title=title, extension=ext, subdir=subdir)

    @property
    def path(self):
        return str(self._path)

    def search(self, query):
        """Return a sequence of Notes that match the given query.

        Arguments:
        query -- the search query match notes against (string)

        """
        return self.search_function(self, query)

    def add_new(self, title, extension=None, subdir=''):
        """Create a new Note and add it to this NoteBook.

        Returns the newly-created Note object.

        Raises NewNoteError if creating or adding the Note fails.

        Raises NoteAlreadyExistsError if creating or adding the Note fails
        because this NoteBook already contains a Note with the given title.

        Notes can be added to subdirectories of the notebook directory by
        putting slashes in their titles, e.g.
        "programming/python/How to use Decorators in Python"

        Arguments:
        title -- the title for the new note (string)
        extension -- the filename extension for the new note (string, should
            start with a dot e.g. ".txt")

        """
        if extension is None:
            extension = self.extension

        # Don't create notes outside of the notes dir.
        if title.startswith(os.sep):
            title = title[len(os.sep):]

        title = title.strip()

        if not Path(title).stem:
            # Don't create notes with empty filenames.
            raise InvalidNoteTitleError(
                    "Invalid note title: {0}".format(title))

        # Check that we don't already have a note with the same title and
        # extension.
        for note in self._notes:
            if note.title == title and note.extension == extension and note.dir == subdir:
                raise NoteAlreadyExistsError(
                        "Note already in NoteBook: {0}".format(note.title))

        # Ok, add the note.
        note = PlainTextNote(title, self, extension, subdir)
        self._notes.append(note)
        return note

    def __len__(self):
        return len(self._notes)

    def __getitem__(self, index):
        return self._notes[index]

    def __delitem__(self, index):
        raise NotImplementedError

    def __iter__(self):
        return self._notes.__iter__()

    def __reversed__(self):
        return self._notes.__reversed__()

    def __contains__(self, note):
        return (note in self._notes)
