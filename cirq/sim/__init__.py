# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base simulation classes and generic simulators."""

from cirq.sim.density_matrix import (
    to_valid_density_matrix,
)
from cirq.sim.simulator import (
    SimulatesSamples,
    StepResult,
    SimulatesIntermediateState,
    SimulatesFinalState,
    SimulationTrialResult
)
from cirq.sim.sparse_simulator import (
    Simulator,
    SparseSimulatorStep,
)
from cirq.sim.wave_function_simulator import (
    SimulatesIntermediateWaveFunction,
    WaveFunctionSimulatorState,
    WaveFunctionStepResult,
    WaveFunctionTrialResult
)
from cirq.sim.wave_function import (
    bloch_vector_from_state_vector,
    density_matrix_from_state_vector,
    dirac_notation,
    measure_state_vector,
    sample_state_vector,
    StateVectorMixin,
    to_valid_state_vector,
    validate_normalized_state,
)
