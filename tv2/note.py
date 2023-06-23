"""
This module defines the Note interface and provides the PlainTextNote implementation
"""

import os
from pathlib import Path
import logging
logger = logging.getLogger(__name__)

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class NewNoteError(Error):
    """Exception raised if making a new Note or adding it to a NoteBook fails.

    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NoteAlreadyExistsError(NewNoteError):
    """Exception raised when trying to add a new note that already exists.

    """
    pass


class InvalidNoteTitleError(NewNoteError):
    """Exception raised when trying to add a new note with an invalid title.

    """
    pass


class DelNoteError(Error):
    """Exception raised if removing a Note from a NoteBook fails.

    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PlainTextNote(object):
    """A note, stored as a plain text file on disk."""

    def __init__(self, title, notebook, extension, subdirectory=''):
        """Initialise a new PlainTextNote.

        A path for the note's file will be generated from the NoteBook's
        path and the given title and extension.

        If a file already exists at the given path, it will be used as the
        note's file. If not, an empty file will be created (parent directories
        will be created also, if necessary).

        The modified time of the note will be read from the mtime of the file.

        Raises NewNoteError if something goes wrong when creating or reading
        the note file.

        Keyword arguments:
        title -- the title for the note
        notebook -- the PlainTextNoteBook this PlainTextNote will belong to
        extension -- the filename extension to use (string, should start with
            a dot e.g. ".txt")
        subdirectory -- optional subdirectory

        """
        self._title = title
        self._notebook = notebook
        self._extension = extension
        self._filename = self.title + self._extension
        self._relpath = Path(subdirectory) / self._filename
        self._abspath = Path(self._notebook.path) / self._relpath

        # Create the file's parent directories (including note directory
        # subdirs) if they don't exist.
        directory = self._abspath.parent
        if not directory.is_dir():
            logger.debug("'{0} doesn't exist, creating it".format(directory))
            try:
                Path.mkdir(directory, parents=True, exist_ok=True)
            except Exception as e:
                raise NewNoteError(
                        "{0} could not be created: {1}".format(directory, e))

        # Create an empty file if the file doesn't exist.
        Path.touch(self._abspath)

    @property
    def title(self):
        return self._title
    
    @property
    def dir(self):
        return str(self._relpath.parent)

    @title.setter
    def set_title(self, new_title):
        # TODO: Implement note renaming. Should rename file on disk.
        raise NotImplementedError

    @property
    def extension(self):
        return self._extension

    @property
    def contents(self):
        contents = open(self.abspath, "r").read()
        if contents is None:
            logger.error(
                "Could not decode file contents: {0}".format(self.abspath))
            return ""
        else:
            return contents

    @property
    def mtime(self):
        return os.path.getmtime(self.abspath)

    @property
    def abspath(self):
        return str(self._abspath)

    def __eq__(self, other):
        return getattr(other, 'abspath', None) == self.abspath