# Matrices Package

## Introduction

This is my first attempt at creating a Python package. It's more a learning project than something that can be published for others to actually use. [NumPy](https://github.com/numpy/numpy) is a very popular Python library that efficiently implements matrices and includes a lot of other useful methods. Although I could've used it as a reference to help build this package, I decided not to as I would like to try to improve the project on my own—pull requests are still welcome!

<div align="center">
  <img width="50%" src="assets/example.png">
  <p>0-based indexed 4 by 7 matrix</p>
</div>

This package implements a matrix by wrapping a class around a 2-dimensional list. Functions that are used within linear algebra, like scaling or transposing, is available for these matrix objects. As of now, only a handful of these functions are available (see documentation below).

## Requirements
- Python 3.6

## A Simple Example

```python
>>> from matrices import Matrix
>>> 
>>> # creating a matrix object
>>> m = Matrix([
...     [1, 6, 8, 5],
...     [2, 3, 7, 4],
...     [0, 4, 1, 5]
... ])
>>> 
>>> m
[1, 6, 8, 5]
[2, 3, 7, 4]
[0, 4, 1, 5]
>>> 
>>> m.m # number of rows
3
>>> m.n # number of columns
4
```

## Documentation

### You can create a matrix object by passing a 2-dimensional list to its constructor.
```python
mtx = matrices.Matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
```

### You can also create an instance of a matrix by specifying dimensions using the alternate constructors.

```python
# for an m x 1 matrix
mtx = matrices.Matrix.from_dimension(3)

# for an m x n matrix
mtx = matrices.Matrix.from_dimensions(3, 3)
```

### Public functions

```python
# scaling a row
mtx.scale(0, 2)

# interchanging two rows
mtx.interchange(1, 2)

# row replacing
mtx.replace(2, 1, 0)

# transposing
mtx.transpose()
```

### Special methods and properties
```python
m1 = matrices.Matrix([[1, 2, 3]])
m2 = matrices.Matrix([[4, 5, 6]])

# adding and subtracting
s = m1 + m2

# matrix multiplication is implemented, but shouldn't be used for large matrices
m3 = m1 * m2

# getting and setting items
first = m1[0][0]
m1[0][0] = -1

# equality
m0 == m1

# string representation
repr(m1)

# there are two properties, m and n, which returns the number of rows and columns, respectively
num_rows = m1.m
num_cols = m1.n
```
