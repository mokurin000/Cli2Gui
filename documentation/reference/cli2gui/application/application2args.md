# Application2args

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Application](./index.md#application) / Application2args

> Auto-generated documentation for [cli2gui.application.application2args](../../../../cli2gui/application/application2args.py) module.

- [Application2args](#application2args)
  - [argFormat](#argformat)
  - [argparseFormat](#argparseformat)
  - [clickFormat](#clickformat)
  - [docoptFormat](#docoptformat)
  - [getoptFormat](#getoptformat)
  - [optparseFormat](#optparseformat)
  - [processValue](#processvalue)

## argFormat

[Show source in application2args.py:89](../../../../cli2gui/application/application2args.py#L89)

Format the args for the desired parser.

#### Arguments

----
 values (dict[str, Any]): values from simple gui
 - `argumentParser` *str* - argument parser to use

#### Returns

-------
 - `Any` - args

#### Signature

```python
def argFormat(values: dict[str, Any], argumentParser: str | ParserType) -> Any: ...
```



## argparseFormat

[Show source in application2args.py:44](../../../../cli2gui/application/application2args.py#L44)

Format args for argparse.

#### Signature

```python
def argparseFormat(values: dict[str, Any]) -> argparse.Namespace: ...
```



## clickFormat

[Show source in application2args.py:78](../../../../cli2gui/application/application2args.py#L78)

Format args for click.

#### Signature

```python
def clickFormat(values: dict[str, Any]) -> list[Any]: ...
```



## docoptFormat

[Show source in application2args.py:67](../../../../cli2gui/application/application2args.py#L67)

Format args for docopt.

#### Signature

```python
def docoptFormat(values: dict[str, Any]) -> dict[str, Any]: ...
```



## getoptFormat

[Show source in application2args.py:62](../../../../cli2gui/application/application2args.py#L62)

Format args for getopt.

#### Signature

```python
def getoptFormat(values: dict[str, Any]) -> tuple[list[Any], list[Any]]: ...
```



## optparseFormat

[Show source in application2args.py:53](../../../../cli2gui/application/application2args.py#L53)

Format args for optparse.

#### Signature

```python
def optparseFormat(values: dict[str, Any]) -> tuple[optparse.Values, list[str]]: ...
```



## processValue

[Show source in application2args.py:13](../../../../cli2gui/application/application2args.py#L13)

#### Signature

```python
def processValue(key: str, value: str) -> tuple[str, Any]: ...
```