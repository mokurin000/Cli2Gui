# Models

[Cli2gui Index](../README.md#cli2gui-index) / [Cli2gui](./index.md#cli2gui) / Models

> Auto-generated documentation for [cli2gui.models](../../../cli2gui/models.py) module.

- [Models](#models)
  - [BuildSpec](#buildspec)
  - [FullBuildSpec](#fullbuildspec)
  - [GUIType](#guitype)
  - [Group](#group)
  - [Item](#item)
  - [ItemType](#itemtype)
  - [ParserRep](#parserrep)
  - [ParserType](#parsertype)

## BuildSpec

[Show source in models.py:14](../../../cli2gui/models.py#L14)

Representation for the BuildSpec.

#### Signature

```python
class BuildSpec: ...
```



## FullBuildSpec

[Show source in models.py:80](../../../cli2gui/models.py#L80)

Representation for the FullBuildSpec (BuildSpec + ParserRep).

#### Signature

```python
class FullBuildSpec: ...
```



## GUIType

[Show source in models.py:113](../../../cli2gui/models.py#L113)

Supported gui types.

#### Signature

```python
class GUIType(str, Enum): ...
```



## Group

[Show source in models.py:63](../../../cli2gui/models.py#L63)

Representation for an argument group.

#### Signature

```python
class Group: ...
```



## Item

[Show source in models.py:30](../../../cli2gui/models.py#L30)

Representation for an arg_item.

#### Signature

```python
class Item: ...
```



## ItemType

[Show source in models.py:45](../../../cli2gui/models.py#L45)

Enum of ItemTypes.

#### Signature

```python
class ItemType(Enum): ...
```



## ParserRep

[Show source in models.py:72](../../../cli2gui/models.py#L72)

Representation for a parser.

#### Signature

```python
class ParserRep: ...
```



## ParserType

[Show source in models.py:98](../../../cli2gui/models.py#L98)

Supported parser types.

#### Signature

```python
class ParserType(str, Enum): ...
```