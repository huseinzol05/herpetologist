<p align="center">
    <a href="#readme">
        <img alt="logo" width="40%" src="https://www.wikihow.com/images/thumb/7/7f/Become-a-Herpetologist-Step-1.jpg/aid1401844-v4-728px-Become-a-Herpetologist-Step-1.jpg.webp">
    </a>
</p>

---

**herpetologist**, Dynamic parameter type checking for Python 3.6 and above. This able to detect deep nested variables.

## problem statement

Let say you want to detect dynamically argument types for a function,

```python
def greeting(name: str):
    # we want to throw exception if name is not `str`.
    print(name) 
```

There is existing library called [typeguard](https://typeguard.readthedocs.io/en/latest/#), it is already good enough but when comes to nested checking, it failed.

```python
List[List[int]] # failed
List[Tuple[int, float, str]] # failed
Tuple(List[int, float], Tuple[float, float]) # failed
Tuple[List[int], Tuple[List[int]]] # failed
Tuple[Tuple[List[Dict[int, str]]], Tuple[List[int]]] # failed
Tuple[Tuple[List[Dict[int, str]]], Tuple[List[int], str]] # failed
```

and list goes on, but this simple decorator `check_type` can helps you, any depth of nested and positions.

I know, who is going to pass that kind of parameter?

## Installing from the PyPI

```bash
pip install herpetologist
```

**Only supports Python 3.6 and above**.

## how-to

```python
from herpetologist import check_snake

@check_snake
def greeting(name: str):
    print(name)
```

#### Support custom types

```python
class ClassA:
    def __init__(self):
        pass

@check_snake
def greeting(name: str, foo: ClassA):
    print(foo)
```

#### Ignore checking

Just simply skip type hinting,

```python
def greeting(name: str, foo):
    print(foo)
```

## example

Simply read more at [example.ipynb](example.ipynb).