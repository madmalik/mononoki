
import fontforge
font=fontforge.open("mononoki-Regular.ttf")


UNICODE_WHITESPACE_CHARACTERS = [
    0x0009, # character tabulation
    0x000a, # line feed
    0x000b, # line tabulation
    0x000c, # form feed
    0x000d, # carriage return
    0x0020, # space
    0x0085, # next line
    0x00a0, # no-break space
    0x1680, # ogham space mark
    0x2000, # en quad
    0x2001, # em quad
    0x2002, # en space
    0x2003, # em space
    0x2004, # three-per-em space
    0x2005, # four-per-em space
    0x2006, # six-per-em space
    0x2007, # figure space
    0x2008, # punctuation space
    0x2009, # thin space
    0x200A, # hair space
    0x2028, # line separator
    0x2029, # paragraph separator
    0x202f, # narrow no-break space
    0x205f, # medium mathematical space
    0x3000, # ideographic space
    0x180e,
    0xFEFF,
    0x200b,
]


all_glyphs = ""
i = 0
for glyph in font:
	n = fontforge.unicodeFromName(glyph)
	if n > 32 and n not in UNICODE_WHITESPACE_CHARACTERS:
		if i % 9 == 0:
			all_glyphs += "\n"
		all_glyphs += "&#x{:04X}; ".format(n)

		i += 1

print(all_glyphs)