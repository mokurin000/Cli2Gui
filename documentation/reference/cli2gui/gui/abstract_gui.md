# AbstractGUI

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Gui](./index.md#gui) / AbstractGUI

> Auto-generated documentation for [cli2gui.gui.abstract_gui](../../../../cli2gui/gui/abstract_gui.py) module.

- [AbstractGUI](#abstractgui)
  - [AbstractGUI](#abstractgui-1)
    - [AbstractGUI().main](#abstractgui()main)

## AbstractGUI

[Show source in abstract_gui.py:11](../../../../cli2gui/gui/abstract_gui.py#L11)

Abstract base class for GUI wrappers.

#### Signature

```python
class AbstractGUI(ABC):
    @abstractmethod
    def __init__(self) -> None: ...
```

### AbstractGUI().main

[Show source in abstract_gui.py:18](../../../../cli2gui/gui/abstract_gui.py#L18)

Abstract method for the main function.

#### Signature

```python
@abstractmethod
def main(
    self,
    buildSpec: models.FullBuildSpec,
    quit_callback: Callable[[], None],
    run_callback: Callable[[dict[str, Any]], None],
) -> None: ...
```