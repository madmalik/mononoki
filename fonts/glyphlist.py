
import fontforge
font=fontforge.open("mononoki-Regular.ttf")


all_glyphs = ""
for glyph in font:
	n = fontforge.unicodeFromName(glyph)
	if n > 32:
		all_glyphs += "&#{};<wbr>".format(n)
print all_glyphs