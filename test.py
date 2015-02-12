# coding : utf-8

import mistune

__author__ = 'ChenKai'

print mistune.markdown(
    '''
# Markdown

----

Markdown is a text formatting syntax inspired on plain text email. In the words of its creator, [John Gruber][]:

[John Gruber]: http://daringfireball.net/


## Syntax Guide

### Strong and Emphasize

```
*emphasize*    **strong**
_emphasize_    __strong__
```

**Shortcuts**

- Add/remove bold:
    Command-B for Mac / Ctrl-B for Windows and Linux

### Links

Inline links:

```
[link text](http://url.com/ "title")
[link text](http://url.com/)
    '''
, parse_html=True)
