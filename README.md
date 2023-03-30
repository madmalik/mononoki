# mononoki

> A font for programming and code review.

For a closer look [http://madmalik.github.io/mononoki/](http://madmalik.github.io/mononoki/).

## Features

- Alternate stylistic set with dotted zero, configurable with `ss01`.

### How to enable

VSCode:

```txt
"editor.fontFamily": "mononoki",
"editor.fontLigatures": "'ss01'",
```

Kitty:

```txt
font_family mononoki
font_features mononoki-Bold +ss01
font_features mononoki-BoldItalic +ss01
font_features mononoki-Italic +ss01
font_features mononoki-Regular +ss01
```

Wezterm:

```txt
font = wezterm.font({
    family = "mononoki",
    harfbuzz_features = { "ss01" },
}),
```

## Installation

[Download mononoki.zip](https://github.com/madmalik/mononoki/releases/download/1.6/mononoki.zip) and unpack it.

- [macOS](http://support.apple.com/kb/HT2509), alternatively there is also a [homebrew formula](https://github.com/Homebrew/homebrew-cask-fonts/blob/master/Casks/font-mononoki.rb).
- [Windows](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1)
- Linux/Unix - distro dependent, if you have a font manager installed on your system, open the font file and hit "Install". Alternatively, there are [mononoki-packages](https://repology.org/project/fonts:mononoki/versions) in many of the package repos, if you prefer installing via package manager.

## Credit

Box drawing characters created with [box drawing](https://github.com/adobe-type-tools/box-drawing).
