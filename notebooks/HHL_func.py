# -*- coding: utf-8 -*-
'''
- HHL.py で使用する関数を定義する.
- 使用パッケージ: numpy, qulacs 0.1.0.

Written by Yuya Nakagawa at QunaSys Inc., Feburary 2019.
'''

import numpy as np
from qulacs import QuantumCircuit, QuantumState, gate
from qulacs.gate import merge, Identity, H, SWAP

def input_state_gate(start_bit, end_bit, vec):
    """ 
    Making a quantum gate which transform |0> to \sum_i x[i]|i>m where x[i] is input vector.
    !!! this uses 2**n times 2**n matrix, so it is quite memory-cosuming.
    !!! this gate is not unitary (we assume that the input state is |0>)
    Args:
      int start_bit: first index of qubit which the gate applies 
      int end_bit:   last index of qubit which the gate applies
      np.ndarray vec:  input vector.
    Returns:
      qulacs.QuantumGate 
    """
    nbit = end_bit - start_bit + 1
    assert vec.size == 2**nbit
    mat_0tox = np.eye(vec.size, dtype=complex)
    mat_0tox[:,0] = vec
    return gate.DenseMatrix(np.arange(start_bit, end_bit+1), mat_0tox)

def CPhaseGate(target, control, angle):
    """ 
    Create controlled phase gate diag(1,e^{i*angle}) with controll. (Qulacs.gate is requried)

    Args:
      int target:  index of target qubit.
      int control:  index of control qubit.
      float64 angle: angle of phase gate.
    Returns:
      QuantumGateBase.DenseMatrix: diag(1, exp(i*angle)).
    """
    CPhaseGate = gate.DenseMatrix(target, np.array( [[1,0], [0,np.cos(angle)+1.j*np.sin(angle)]])  )
    CPhaseGate.add_control_qubit(control, 1)
    return CPhaseGate

def QFT_gate(start_bit, end_bit, Inverse = False):
    """ 
    Making a gate which performs quantum Fourier transfromation between start_bit to end_bit.
    (Definition below is the case when start_bit = 0 and end_bit=n-1)
    We associate an integer  j = j_{n-1}...j_0 to quantum state |j_{n-1}...j_0>.
    We define QFT as
    |k> = |k_{n-1}...k_0> = 1/sqrt(2^n) sum_{j=0}^{2^n-1} exp(2pi*i*(k/2^n)*j) |j>.
    then, |k_m > = 1/sqrt(2)*(|0> + exp(i*2pi*0.j_{n-1-m}...j_0)|1> )
    When Inverse=True,  the gate represents Inverse QFT,
    |k> = |k_{n-1}...k_0> = 1/sqrt(2^n) sum_{j=0}^{2^n-1} exp(-2pi*i*(k/2^n)*j) |j>.

    Args:
      int start_bit:  first index of qubits where we apply QFT.
      int end_bit:    last  index of qubits where we apply QFT.
      bool Inverse: When True, the gate perform inverse-QFT ( = QFT^{\dagger}).
    Returns:
      qulacs.QuantumGate: QFT gate which acts on a region between start_bit and end_bit.
    """

    gate = Identity(start_bit) ## make empty gate
    n = end_bit - start_bit + 1  ## size of QFT

    ## loop from j_{n-1} 
    for target in range(end_bit, start_bit-1, -1):
        gate = merge(gate, H(target)) ## 1/sqrt(2)(|0> + exp(i*2pi*0.j_{target})|1>)
        for control in range(start_bit, target):
            gate = merge( gate, CPhaseGate(target, control, (-1)**Inverse * 2.*np.pi/2**(target-control+1)) )
    ## perform SWAP between (start_bit + s)-th bit and (end_bit - s)-th bit
    for s in range(n//2):  ## s runs 0 to n//2-1
        gate = merge(gate, SWAP(start_bit + s, end_bit - s))
    ## return final circuit
    return gate

