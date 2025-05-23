# PySimpleGUIWrapper

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Gui](./index.md#gui) / PySimpleGUIWrapper

> Auto-generated documentation for [cli2gui.gui.pysimplegui_wrapper](../../../../cli2gui/gui/pysimplegui_wrapper.py) module.

- [PySimpleGUIWrapper](#pysimpleguiwrapper)
  - [PySimpleGUIWrapper](#pysimpleguiwrapper-1)
    - [PySimpleGUIWrapper()._button](#pysimpleguiwrapper()_button)
    - [PySimpleGUIWrapper()._check](#pysimpleguiwrapper()_check)
    - [PySimpleGUIWrapper()._dropdown](#pysimpleguiwrapper()_dropdown)
    - [PySimpleGUIWrapper()._fileBrowser](#pysimpleguiwrapper()_filebrowser)
    - [PySimpleGUIWrapper()._helpArgHelp](#pysimpleguiwrapper()_helparghelp)
    - [PySimpleGUIWrapper()._helpArgName](#pysimpleguiwrapper()_helpargname)
    - [PySimpleGUIWrapper()._helpArgNameAndHelp](#pysimpleguiwrapper()_helpargnameandhelp)
    - [PySimpleGUIWrapper()._helpCounterWidget](#pysimpleguiwrapper()_helpcounterwidget)
    - [PySimpleGUIWrapper()._helpDropdownWidget](#pysimpleguiwrapper()_helpdropdownwidget)
    - [PySimpleGUIWrapper()._helpFileWidget](#pysimpleguiwrapper()_helpfilewidget)
    - [PySimpleGUIWrapper()._helpFlagWidget](#pysimpleguiwrapper()_helpflagwidget)
    - [PySimpleGUIWrapper()._helpTextWidget](#pysimpleguiwrapper()_helptextwidget)
    - [PySimpleGUIWrapper()._inputText](#pysimpleguiwrapper()_inputtext)
    - [PySimpleGUIWrapper()._label](#pysimpleguiwrapper()_label)
    - [PySimpleGUIWrapper()._spin](#pysimpleguiwrapper()_spin)
    - [PySimpleGUIWrapper()._title](#pysimpleguiwrapper()_title)
    - [PySimpleGUIWrapper().addItemsAndGroups](#pysimpleguiwrapper()additemsandgroups)
    - [PySimpleGUIWrapper().addWidgetFromItem](#pysimpleguiwrapper()addwidgetfromitem)
    - [PySimpleGUIWrapper().createLayout](#pysimpleguiwrapper()createlayout)
    - [PySimpleGUIWrapper().generatePopup](#pysimpleguiwrapper()generatepopup)
    - [PySimpleGUIWrapper().getImgData](#pysimpleguiwrapper()getimgdata)
    - [PySimpleGUIWrapper().main](#pysimpleguiwrapper()main)

## PySimpleGUIWrapper

[Show source in pysimplegui_wrapper.py:16](../../../../cli2gui/gui/pysimplegui_wrapper.py#L16)

Wrapper class for PySimpleGUI.

#### Signature

```python
class PySimpleGUIWrapper(AbstractGUI):
    def __init__(self, base24Theme: list[str], psg_lib: str) -> None: ...
```

#### See also

- [AbstractGUI](./abstract_gui.md#abstractgui)

### PySimpleGUIWrapper()._button

[Show source in pysimplegui_wrapper.py:109](../../../../cli2gui/gui/pysimplegui_wrapper.py#L109)

Return a button.

#### Signature

```python
def _button(self, text: str) -> Any: ...
```

### PySimpleGUIWrapper()._check

[Show source in pysimplegui_wrapper.py:99](../../../../cli2gui/gui/pysimplegui_wrapper.py#L99)

Return a checkbox.

#### Signature

```python
def _check(self, key: str, default: str | None = None) -> Any: ...
```

### PySimpleGUIWrapper()._dropdown

[Show source in pysimplegui_wrapper.py:130](../../../../cli2gui/gui/pysimplegui_wrapper.py#L130)

Return a dropdown.

#### Signature

```python
def _dropdown(self, key: str, argItems: list[str]) -> Any: ...
```

### PySimpleGUIWrapper()._fileBrowser

[Show source in pysimplegui_wrapper.py:139](../../../../cli2gui/gui/pysimplegui_wrapper.py#L139)

Return a fileBrowser button and field.

#### Signature

```python
def _fileBrowser(
    self,
    key: str,
    default: str | None = None,
    _type: ItemType = ItemType.File,
    additional_properties: dict | None = None,
) -> list[Any]: ...
```

#### See also

- [ItemType](../models.md#itemtype)

### PySimpleGUIWrapper()._helpArgHelp

[Show source in pysimplegui_wrapper.py:188](../../../../cli2gui/gui/pysimplegui_wrapper.py#L188)

Return a label for the arg help text.

#### Signature

```python
def _helpArgHelp(self, helpText: str) -> Any: ...
```

### PySimpleGUIWrapper()._helpArgName

[Show source in pysimplegui_wrapper.py:184](../../../../cli2gui/gui/pysimplegui_wrapper.py#L184)

Return a label for the arg name.

#### Signature

```python
def _helpArgName(self, displayName: str, commands: list[str]) -> Any: ...
```

### PySimpleGUIWrapper()._helpArgNameAndHelp

[Show source in pysimplegui_wrapper.py:192](../../../../cli2gui/gui/pysimplegui_wrapper.py#L192)

Return a column containing the argument name and help text.

#### Signature

```python
def _helpArgNameAndHelp(
    self, commands: list[str], helpText: str, displayName: str
) -> Any: ...
```

### PySimpleGUIWrapper()._helpCounterWidget

[Show source in pysimplegui_wrapper.py:243](../../../../cli2gui/gui/pysimplegui_wrapper.py#L243)

Return a set of self that make up an arg with text.

#### Signature

```python
def _helpCounterWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../models.md#item)

### PySimpleGUIWrapper()._helpDropdownWidget

[Show source in pysimplegui_wrapper.py:268](../../../../cli2gui/gui/pysimplegui_wrapper.py#L268)

Return a set of self that make up an arg with a choice.

#### Signature

```python
def _helpDropdownWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../models.md#item)

### PySimpleGUIWrapper()._helpFileWidget

[Show source in pysimplegui_wrapper.py:255](../../../../cli2gui/gui/pysimplegui_wrapper.py#L255)

Return a set of self that make up an arg with a file.

#### Signature

```python
def _helpFileWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../models.md#item)

### PySimpleGUIWrapper()._helpFlagWidget

[Show source in pysimplegui_wrapper.py:218](../../../../cli2gui/gui/pysimplegui_wrapper.py#L218)

Return a set of self that make up an arg with true/ false.

#### Signature

```python
def _helpFlagWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../models.md#item)

### PySimpleGUIWrapper()._helpTextWidget

[Show source in pysimplegui_wrapper.py:230](../../../../cli2gui/gui/pysimplegui_wrapper.py#L230)

Return a set of self that make up an arg with text.

#### Signature

```python
def _helpTextWidget(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../models.md#item)

### PySimpleGUIWrapper()._inputText

[Show source in pysimplegui_wrapper.py:78](../../../../cli2gui/gui/pysimplegui_wrapper.py#L78)

Return an input text field.

#### Signature

```python
def _inputText(self, key: str, default: str | None = None) -> Any: ...
```

### PySimpleGUIWrapper()._label

[Show source in pysimplegui_wrapper.py:118](../../../../cli2gui/gui/pysimplegui_wrapper.py#L118)

Return a label.

#### Signature

```python
def _label(self, text: str, font: int = 11) -> Any: ...
```

### PySimpleGUIWrapper()._spin

[Show source in pysimplegui_wrapper.py:88](../../../../cli2gui/gui/pysimplegui_wrapper.py#L88)

Return an input text field.

#### Signature

```python
def _spin(self, key: str, default: str | None = None) -> Any: ...
```

### PySimpleGUIWrapper()._title

[Show source in pysimplegui_wrapper.py:199](../../../../cli2gui/gui/pysimplegui_wrapper.py#L199)

Return a set of self that make up the application header.

#### Signature

```python
def _title(self, text: str, image: str = "") -> list[Any]: ...
```

### PySimpleGUIWrapper().addItemsAndGroups

[Show source in pysimplegui_wrapper.py:371](../../../../cli2gui/gui/pysimplegui_wrapper.py#L371)

Items and groups and return a list of psg Elements.

#### Arguments

- `section` *Group* - section with a name to display and items

#### Returns

Type: *list[list[Element]]*
updated argConstruct

#### Signature

```python
def addItemsAndGroups(self, section: Group) -> list[list[Any]]: ...
```

#### See also

- [Group](../models.md#group)

### PySimpleGUIWrapper().addWidgetFromItem

[Show source in pysimplegui_wrapper.py:287](../../../../cli2gui/gui/pysimplegui_wrapper.py#L287)

Select a widget based on the item type.

#### Arguments

- `item` *Item* - the item

#### Signature

```python
def addWidgetFromItem(self, item: Item) -> list[Any]: ...
```

#### See also

- [Item](../models.md#item)

### PySimpleGUIWrapper().createLayout

[Show source in pysimplegui_wrapper.py:396](../../../../cli2gui/gui/pysimplegui_wrapper.py#L396)

Create the pysimplegui layout from the build spec.

#### Arguments

- `buildSpec` *FullBuildSpec* - build spec containing widget
:param str | list[str] menu: menu definition. containing menu keys

#### Returns

Type: *list[list[Any]]*
list of self (layout list)

#### Signature

```python
def createLayout(
    self, buildSpec: FullBuildSpec, menu: str | list[str]
) -> list[list[Any]]: ...
```

#### See also

- [FullBuildSpec](../models.md#fullbuildspec)

### PySimpleGUIWrapper().generatePopup

[Show source in pysimplegui_wrapper.py:311](../../../../cli2gui/gui/pysimplegui_wrapper.py#L311)

Create the popup window.

#### Arguments

----
 - `buildSpec` *FullBuildSpec* - [description]
 values (Union[dict[Any, Any]): Returned when a button is clicked. Such
 as the menu

#### Returns

-------
 - `Window` - A PySimpleGui Window

#### Signature

```python
def generatePopup(
    self, buildSpec: FullBuildSpec, values: dict[Any, Any] | list[Any]
) -> Any: ...
```

#### See also

- [FullBuildSpec](../models.md#fullbuildspec)

### PySimpleGUIWrapper().getImgData

[Show source in pysimplegui_wrapper.py:508](../../../../cli2gui/gui/pysimplegui_wrapper.py#L508)

Generate image data using PIL.

#### Signature

```python
def getImgData(self, imagePath: str, first: bool = False) -> bytes: ...
```

### PySimpleGUIWrapper().main

[Show source in pysimplegui_wrapper.py:463](../../../../cli2gui/gui/pysimplegui_wrapper.py#L463)

Run the gui (psg) with a given buildSpec, quit_callback, and run_callback.

#### Arguments

- `buildSpec` *FullBuildSpec* - Full cli parse/ build spec
:param Callable[[], None] quit_callback: generic callable used to quit
:param Callable[[dict[str, Any]], None] run_callback: generic callable used to run

#### Signature

```python
def main(
    self,
    buildSpec: FullBuildSpec,
    quit_callback: Callable[[], None],
    run_callback: Callable[[dict[str, Any]], None],
) -> None: ...
```

#### See also

- [FullBuildSpec](../models.md#fullbuildspec)