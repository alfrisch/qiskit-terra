"""
controlled-Y gate.

Author: Andrew Cross
"""
from qiskit import QuantumCircuit
from qiskit import Gate
from qiskit import CompositeGate
from qiskit.extensions.standard import header


class CyGate(Gate):
    """controlled-Y gate."""

    def __init__(self, ctl, tgt, circ=None):
        """Create new CY gate."""
        super(CyGate, self).__init__("cy", [], [ctl, tgt], circ)

    def qasm(self):
        """Return OPENQASM string."""
        ctl = self.arg[0]
        tgt = self.arg[1]
        return self._qasmif("cy %s[%d],%s[%d];" % (ctl[0].name, ctl[1],
                                                   tgt[0].name, tgt[1]))

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cy(self.arg[0], self.arg[1]))


def cy(self, ctl, tgt):
    """Apply CY to circuit."""
    self._check_qubit(ctl)
    self._check_qubit(tgt)
    self._check_dups([ctl, tgt])
    return self._attach(CyGate(ctl, tgt, self))


QuantumCircuit.cy = cy
CompositeGate.cy = cy
