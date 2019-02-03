import re

"""
    Script used to generate Icon constant java fiels with unicode icons from css.
"""
f = open("icons.css")

pattern = re.compile(r'^\.icon-(\w[-\w]*)::before\s{\s+content:\s\"\\(e\w+)\";\s+}$', re.MULTILINE)

for match in pattern.finditer(f.read()):
    name = match.group(1).upper().replace('-', '_')
    code = unicode('\u%s' % match.group(2))
    print u'''
    /**
     * <span style="font-size: 80px;" >%s</span>
     */''' % code
    print u'public static final String %s = "%s";' % (name, code)

f.close()
