# -*- coding: utf-8 -*
# 参见 http://www.unicode.org/

from __future__ import unicode_literals

strUnicode = u"unicode字符串"

# http://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
print strUnicode.decode(encoding='utf-8')

# UnicodeEncodeError: 'charmap' codec can't encode characters in position 7-9: character maps to <undefined>
# .decode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 7-9: ordinal not in range(128)


print type(strUnicode)
# <type 'unicode'>

print type(strUnicode).__base__
# <type 'basestring'>
