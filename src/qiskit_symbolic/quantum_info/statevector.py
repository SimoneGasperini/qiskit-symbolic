"""Symbolic quantum statevector module"""

import numpy as np
from sympy import simplify, matrix2numpy, sqrt
from sympy.physics.quantum import TensorProduct
from .quantumbase import QuantumBase


class Statevector(QuantumBase):
    """Symbolic quantum statevector class"""

    def __init__(self, data):
        """todo"""
        super().__init__(data=data)

    @classmethod
    def from_label(cls, label):
        """todo"""
        data = cls._init_from_label(label)
        return cls(data=data)

    def to_numpy(self):
        """todo"""
        try:
            return matrix2numpy(self.to_sympy(), dtype=complex)[:, 0]
        except TypeError:
            return matrix2numpy(self.to_sympy(), dtype=object)[:, 0]

    def norm(self):
        """todo"""
        return simplify(sqrt(self.inner(self)))

    def is_unit_norm(self):
        """todo"""
        try:
            numpy_array = matrix2numpy(self.to_sympy(), dtype=complex)[:, 0]
            return np.allclose(np.linalg.norm(numpy_array), 1)
        except TypeError:
            return self.norm() == 1

    def is_valid(self):
        """todo"""
        return self.is_unit_norm()

    def tensor(self, other):
        """todo"""
        if not isinstance(other, Statevector):
            other = Statevector(other)
        tensorprod = TensorProduct(self.to_sympy(), other.to_sympy())
        return self.__class__(tensorprod)

    def inner(self, other):
        """todo"""
        if not isinstance(other, Statevector):
            other = Statevector(other)
        return (self.to_sympy().T @ other.to_sympy())[0]

    def outer(self, other):
        """todo"""
        if not isinstance(other, Statevector):
            other = Statevector(other)
        return self.to_sympy() @ other.to_sympy().T

    def projector(self):
        """todo"""
        return self.outer(self)
