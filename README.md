# bookmark-file-tag-adder

A simple script to attach tags to each bookmark from its ancestral folder names.

Given the following Bookmark tree:

```
Bookmarks/
└── comp
    └── lang
        ├── python
        │   └── website1
        └── website2
```

The following tags are assigned:
- website1: #comp, #lang, and #python
- website2: #comp and #lang

I wrote this to import bookmarks to the self-hosted bookmark manager, [linkding](https://linkding.link/).
