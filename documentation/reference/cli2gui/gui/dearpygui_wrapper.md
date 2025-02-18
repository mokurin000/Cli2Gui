# DearPyGuiWrapper

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Gui](./index.md#gui) / DearPyGuiWrapper

> Auto-generated documentation for [cli2gui.gui.dearpygui_wrapper](../../../../cli2gui/gui/dearpygui_wrapper.py) module.

- [DearPyGuiWrapper](#dearpyguiwrapper)
  - [DearPyGuiWrapper](#dearpyguiwrapper-1)
    - [DearPyGuiWrapper()._helpFileWidget](#dearpyguiwrapper()_helpfilewidget)
    - [DearPyGuiWrapper().addItemsAndGroups](#dearpyguiwrapper()additemsandgroups)
    - [DearPyGuiWrapper().addWidgetFromItem](#dearpyguiwrapper()addwidgetfromitem)
    - [DearPyGuiWrapper().main](#dearpyguiwrapper()main)
    - [DearPyGuiWrapper().open_menu_item](#dearpyguiwrapper()open_menu_item)
  - [hex_to_rgb](#hex_to_rgb)

## DearPyGuiWrapper

[Show source in dearpygui_wrapper.py:26](../../../../cli2gui/gui/dearpygui_wrapper.py#L26)

Wrapper class for Dear PyGui.

#### Signature

```python
class DearPyGuiWrapper(AbstractGUI):
    def __init__(self, base24Theme: list[str]) -> None: ...
```

#### See also

- [AbstractGUI](./abstract_gui.md#abstractgui)

### DearPyGuiWrapper()._helpFileWidget

[Show source in dearpygui_wrapper.py:80](../../../../cli2gui/gui/dearpygui_wrapper.py#L80)

Create a UI element with an input text field and a file picker.

#### Signature

```python
def _helpFileWidget(self, item: Item) -> None: ...
```

#### See also

- [Item](../models.md#item)

### DearPyGuiWrapper().addItemsAndGroups

[Show source in dearpygui_wrapper.py:147](../../../../cli2gui/gui/dearpygui_wrapper.py#L147)

Items and groups and return a list of these so we can get values from the dpg widgets.

#### Arguments

- `section` *Group* - section with a name to display and items

#### Returns

Type: *list[Item]*
flattened list of items

#### Signature

```python
def addItemsAndGroups(self, section: Group) -> list[Item]: ...
```

#### See also

- [Group](../models.md#group)
- [Item](../models.md#item)

### DearPyGuiWrapper().addWidgetFromItem

[Show source in dearpygui_wrapper.py:125](../../../../cli2gui/gui/dearpygui_wrapper.py#L125)

Select a widget based on the item type.

#### Arguments

- `item` *Item* - the item

#### Signature

```python
def addWidgetFromItem(self, item: Item) -> None: ...
```

#### See also

- [Item](../models.md#item)

### DearPyGuiWrapper().main

[Show source in dearpygui_wrapper.py:191](../../../../cli2gui/gui/dearpygui_wrapper.py#L191)

Run the gui (dpg) with a given buildSpec, quit_callback, and run_callback.

- Theming + Configure dpg
- Menu Prep
- Create Window, set up Menu and Widgets
- Then, start dpg

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

### DearPyGuiWrapper().open_menu_item

[Show source in dearpygui_wrapper.py:177](../../../../cli2gui/gui/dearpygui_wrapper.py#L177)

Open a menu item.

#### Arguments

- `sender` *_type_* - file to open
- `_app_data` *_type_* - [unused]

#### Signature

```python
def open_menu_item(self, sender: str, _app_data: None) -> None: ...
```



## hex_to_rgb

[Show source in dearpygui_wrapper.py:17](../../../../cli2gui/gui/dearpygui_wrapper.py#L17)

Convert a color hex code to a tuple of integers (r, g, b).

#### Signature

```python
def hex_to_rgb(hex_code: str) -> tuple[int, int, int, int]: ...
```