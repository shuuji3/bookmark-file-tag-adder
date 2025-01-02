"""Adding tags to bookmark file from its ancestral folders

Given the following Bookmark tree:

Bookmarks/
└── comp/
    └── lang/
        ├── python/
        │   └── website1
        └── website2

The following tags are assigned:
- website1: #comp, #lang, and #python
- website2: #comp and #lang
"""

from NetscapeBookmarksFileParser import *
from NetscapeBookmarksFileParser import creator

header = '''
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
'''


def assign_tags(bookmarks: BookmarkFolder | BookmarkShortcut):
    if type(bookmarks) is BookmarkShortcut:
        bookmarks.tags = make_tags(bookmarks)
        # Linkding cannot import bookmark with title more than 512 length
        bookmarks.name = bookmarks.name[:500]
        return

    for i in bookmarks.items:
        assign_tags(i)


def make_tags(shortcut: BookmarkShortcut, folders: [str] = []):
    if not shortcut.parent:
        return folders[1:]

    return make_tags(shortcut.parent, [shortcut.parent.name.lower()] + folders)


def main():
    input_bookmark_file = 'chrome-bookmarks.html'
    output_bookmark_file = 'bookmarks-with-tags.html'

    with open(input_bookmark_file) as f:
        bookmarks = NetscapeBookmarksFile(f).parse()

    assign_tags(bookmarks.bookmarks)

    with open(output_bookmark_file, 'w') as f:
        content = header + '\n' + '\n'.join(creator.folder_creator(bookmarks.bookmarks))
        f.write(content)


if __name__ == "__main__":
    main()
