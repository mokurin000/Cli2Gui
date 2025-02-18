# Helpers

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Gui](./index.md#gui) / Helpers

> Auto-generated documentation for [cli2gui.gui.helpers](../../../../cli2gui/gui/helpers.py) module.

- [Helpers](#helpers)
  - [_themeFromFile](#_themefromfile)
  - [get_base24_theme](#get_base24_theme)
  - [isDarkMode](#isdarkmode)
  - [read_file](#read_file)
  - [stringSentencecase](#stringsentencecase)
  - [stringTitlecase](#stringtitlecase)

## _themeFromFile

[Show source in helpers.py:20](../../../../cli2gui/gui/helpers.py#L20)

Set the base24 theme from a base24 scheme.yaml to the application.

#### Arguments

----
 - `themeFile` *str* - path to file

#### Returns

-------
 - `list[str]` - theme to set

#### Signature

```python
def _themeFromFile(themeFile: str) -> list[str]: ...
```



## get_base24_theme

[Show source in helpers.py:36](../../../../cli2gui/gui/helpers.py#L36)

Set the base24 theme to the application.

#### Arguments

----
 theme (Union[str, list[str]]): the light theme
 darkTheme (Union[str, list[str]]): the dark theme

#### Signature

```python
def get_base24_theme(
    theme: str | list[str], darkTheme: str | list[str]
) -> list[str]: ...
```



## isDarkMode

[Show source in helpers.py:12](../../../../cli2gui/gui/helpers.py#L12)

Monkeypatch for getostheme.isDarkMode.

#### Signature

```python
def isDarkMode() -> bool: ...
```



## read_file

[Show source in helpers.py:133](../../../../cli2gui/gui/helpers.py#L133)

Get the contents of a file path, attempt to parse with catpandoc..pandoc2plain.

#### Arguments

- `file_path` *str* - path to the file (absolute recommended)

#### Returns

Type: *str*
file contents

#### Signature

```python
def read_file(file_path: str, maxLines: int = 200) -> str: ...
```



## stringSentencecase

[Show source in helpers.py:125](../../../../cli2gui/gui/helpers.py#L125)

Convert a string to sentence case.

#### Signature

```python
def stringSentencecase(string: str) -> str: ...
```



## stringTitlecase

[Show source in helpers.py:111](../../../../cli2gui/gui/helpers.py#L111)

Convert a string to title case.

#### Signature

```python
def stringTitlecase(string: str, splitStr: str = "ALL") -> str: ...
```