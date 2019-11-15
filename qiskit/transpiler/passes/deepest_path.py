# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Return the deepest path in a DAGcircuit as a list of DAGNodes."""

from qiskit.transpiler.basepasses import AnalysisPass


class DeepestPath(AnalysisPass):
    """Return the deepest path in a DAGcircuit as a list of DAGNodes."""

    def run(self, dag):
        """Run the DeepestPath pass on `dag`."""
        self.property_set['deepest_path'] = dag.longest_path()