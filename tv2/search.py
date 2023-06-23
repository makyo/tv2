
def brute_force_search(notebook, query):
    """Return all notes in `notebook` that match `query`.

    Returns a sequence of Note objects that match the given search query.

    Arguments:

    notebook - the notebook to search (NoteBook)

    query - the query to search for (string)

    This is implemented as a standalone function so it can easily be replaced
    with some other function that does the search differently (e.g. you could
    have a config option to choose between different search implementations).

    This implementation does a brute force search that simply reads every file
    in the notebook looking for the search words.

    """
    search_words = query.strip().split()
    matching_notes = []
    for note in notebook:
        match = True
        title = note.dir + '/' + note.title if note.dir and note.dir != '.' else note.title
        for search_word in search_words:
            if search_word.islower():
                # Search for word case-insensitively.
                in_title = search_word in title.lower()
                in_contents = search_word in note.contents.lower()
            else:
                # Search for word case-sensitively.
                in_title = search_word in title
                in_contents = search_word in note.contents
            if (not in_title) and (not in_contents):
                match = False
        if match:
            matching_notes.append(note)
    return matching_notes