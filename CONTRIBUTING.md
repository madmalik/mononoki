# How to contribute

### adding glyphs

One thing you can always do is just ask me to add a glyph. I'll do my best to react to demands, but since I'm doing this in my free time a cannot make garuatees.

If you want to add glyphs yourself: Since my app of choice (glyphs) is closed source and paid, and all open font development seems to happen with fontforge, I created a fontforge version of the regular version of the font.

Please just use this version for contributions. The dimensions of typical elements are:
```              

 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _______  _ _ _ _ _ _ _ 750 _ _ _ _ _ _   ________
                            |       |                                |   ^    |
 _________________________  | _ _ _ | _ _ _ _ _ _ _ 700 _ _ _ _ _ _  |   | 115|
|         ^               | |       |                                |<--+--->| 
|         |77             | |       |                                |   v    |
|         v               | |       |                                 --------
|        -----------------  |       |
|       |                   |       |
| _ _ _ | _ _ _ _ _ _ _ _ _ | _ _ _ | _ _ _ _ ______500  _____________________ 
|       |                   |       |        /      /   |                     |  
|       |                   |       |       /      /    |                     |
|        --------------     |       |      /      /      _____________        |
|                      |    |       |     /      /                    |       |
|                      |    |       |    /      /                     |       |
|        ______________     |        ----      /                      |       |
|       |                   |                 <                       |       |
|   85  |                   |                  \                      |       |
|<----->|                   |        ----       \                     |       |
|       |                   |       |    \       \                    |       |
|       |_________________  |       |     \       \                   |       |
|                         | |       |      \       \                  |       |
|                         | |       |       \       \                 |       |
|                         | |       |        \       \                |       |
 -------------------------   ------- - - - - - -------  - - - - - - - | - - - |
                                                                      |       |
                                                                      /       /
                                                        --___________/       /
                                                       |                    /
                                                       |                   /
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ -250 --_____________---

```

The corners are rounded with a radius 25 points, the glyph width is 575 points.

I'll import the contributions in regular intervalls, check the outlines, create bold and italic versions of them and update the upstream version. 

Contributions don't have to be release-ready. I'm happy to adjust curves, round the corners etc. If you need help, just ask. Fontdesign is fun, and I'm happy to help.



