# bookmark-file-tag-adder

A simple script to attach tags to each bookmark from its ancestral folders.

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
