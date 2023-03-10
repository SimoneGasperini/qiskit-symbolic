r"""Symbolic :math:`P(\lambda)` and :math:`CP(\lambda)` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.circuit.gate import Gate
from ...controlledgate import ControlledGate


class PhaseGate(Gate):
    r"""Symbolic :math:`P(\lambda)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='p', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        lam, = self._get_params_expr()
        i = sympy.I
        return Matrix([[1, 0],
                       [0, sympy.exp(i * lam)]])


class CPhaseGate(ControlledGate):
    r"""Symbolic :math:`CP(\lambda)` gate class"""

    def __init__(self, theta, control_qubit=0, target_qubit=1):
        """todo"""
        params = [theta]
        base_gate = PhaseGate(theta)
        super().__init__(name='cp', num_qubits=2, params=params,
                         control_qubit=control_qubit, target_qubit=target_qubit,
                         base_gate=base_gate)
