<p align="center">
    <a href="#readme">
        <img alt="logo" width="30%" src="https://www.wikihow.com/images/thumb/7/7f/Become-a-Herpetologist-Step-1.jpg/aid1401844-v4-728px-Become-a-Herpetologist-Step-1.jpg.webp">
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
Tuple[List[int], Tuple[List[int]]] # failed
List[Dict[str, Dict[str, List[str]]]] # failed
Tuple(List[int, float], Tuple[float, float]) # failed
Tuple[Tuple[List[Dict[int, str]]], Tuple[List[int]]] # failed
Tuple[Tuple[List[Dict[int, str]]], Tuple[List[int], str]] # failed
```

and list goes on, but this simple decorator `check_type` can helps you, any depth of nested and positions.

Ya I know, who is going to pass that kind of variables in function parameters? Me!

## Installing from the PyPI

```bash
pip install herpetologist
```

**Only supports Python 3.6 and above**.

## how-to

```python
from herpetologist import check_type

@check_type
def greeting(name: str):
    print(name)
```

```python
@check_type
def greeting(name: Tuple[Tuple[List[Dict[int, str]]], Tuple[List[int]]]):
    pass

greeting((([{1: 'str'}],), ([1], [1]))) # no error
greeting((([{1: 'str'}],), ([1], [1.1]))) # error
```

```python
@check_type
def greeting(name: List[Dict[str, Dict[str, List[str]]]]):
    pass
    
greeting([{'a': {'b': ['a', 'a']}}]) # no error
greeting([{'a': {'b': ['a', 1]}}]) # error
```

#### Support custom types

```python
class ClassA:
    def __init__(self):
        pass

@check_type
def greeting(name: str, foo: ClassA):
    print(foo)
```

#### Ignore checking

Just simply skip type hinting,

```python
def greeting(name: str, foo):
    print(foo)
```

#### default value

herpetologist will never checked default value, snake is a snake (concept from duck typing)!

```python
@check_type
def greeting(name: List[Dict[str, Dict[str, List[str]]]] = None):
    if name is None:
        print('name is None!')
    
greeting([{'a': {'b': ['a', 'a']}}]) # no error
greeting() # no error
```

#### disable herpetologist using bash environment

Let say we already have a code,

```python
@check_type
def plus(x: int):
    return int + 1
```

Some of our environments we want to enable it, some of it also we want to disable, and we do not want herpetologist to keep check the variables. So to disable it, simply set bash environment,

```bash
export ENABLE_HERPETOLOGIST=false
```

Or, using python,

```python
import os
os.environ['ENABLE_HERPETOLOGIST'] = 'false'
```

**But again, this will disable entire herpetologist.**

## example

Simply read more at [example.ipynb](example.ipynb).