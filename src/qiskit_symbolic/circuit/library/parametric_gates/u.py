r"""Symbolic :math:`U(\theta, \phi, \lambda)` and
:math:`CU(\theta, \phi, \lambda, \gamma)` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class UGate(Gate):
    r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate class"""

    def __init__(self, theta, phi, lam):
        """todo"""
        params = [theta, phi, lam]
        super().__init__(name='u', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, phi, lam = self._get_params_expr()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        exp = sympy.exp
        return Matrix([[cos, -exp(i * lam) * sin],
                       [exp(i * phi) * sin, exp(i * (phi + lam)) * cos]])


class CUGate(ControlledGate):
    r"""Symbolic :math:`CU(\theta, \phi, \lambda, \gamma)` gate class"""

    def __init__(self, theta, phi, lam, gamma, control_qubit=0, target_qubit=1):
        """todo"""
        # pylint: disable=too-many-arguments
        params = [theta, phi, lam, gamma]
        base_gate = UGate(theta, phi, lam)
        super().__init__(name='cu', num_qubits=2, params=params,
                         control_qubit=control_qubit, target_qubit=target_qubit,
                         base_gate=base_gate, global_phase=True)
