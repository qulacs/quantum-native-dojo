# -*- coding: utf-8 -*-
'''
- HHLアルゴリズムのもっとも簡単なバージョンを実装する.(以下の参考文献のFig.5)
- 参考文献(コード内コメントでは"論文"と略記): "Quantum linear systems algorithms: a primer", arXiv:1802.08227v1
- 使用パッケージ: numpy, qulacs 0.1.0.

Written by Yuya Nakagawa at QunaSys Inc.,  March 2019.
'''

import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

from qulacs import QuantumCircuit, QuantumState, gate
import HHL_func


def HHL_solve(A, b, reg_nbit=4, t=0.5):
    """
    連立一次方程式Ax=bを解く。

    Parameters
    ----------
    A : ndarray
        n×n行列。
    b : ndarray
        n次元ベクトル。
    reg_nbit : int
        計算に用いるレジスタ量子ビットの数。
    t : float
        U=e^{iAt} の位相推定に使う時間
    
    Returns
    -----------
    x_HHL : ndarray
        シミュレーターを用いたHHLアルゴリズムによる解x。
    x_true : ndarray
        np.linalg.solveによる解x。
    """

    assert len(A)==len(b), 'Dimension mismatch.'

    print('A.shape:', A.shape)
    print('b.shape:', b.shape)

    ### ---------  パラメータ設定始まり -------------- ###
    ## 乱数の初期化
    #my_seed = 301
    #np.random.seed(my_seed)

    ## 解きたい一次方程式 Ax=b の行列およびベクトルの大きさ
    n = len(b)

    # nbit = 2 ## bit数 (ベクトルの長さは2^nbit)
    nbit = np.int(np.ceil(np.log2(n))) # 考える行列の次元が2^n (n:整数)でない場合にも対応
    N = 2**nbit

    # A (b) をN×N行列A0 (N次元ベクトルb0) に入れておく。残りの部分は0で埋める。
    A0 = np.zeros((N, N))
    A0[:A.shape[0],:A.shape[1]] = A
    b0 = np.zeros(N)
    b0[:len(b)] = b

    ## U=e^{iAt} の位相推定に使う時間 t とレジスタbitの数
    # t = 0.5
    # reg_nbit = 4
    reg_N = 2**reg_nbit

    ## A*tの固有値として想定する最小の値 (論文(70)式).
    ## 今回は射影が100%成功するので, レジスタで表せる最小値の定数倍でとっておく
    C = 0.5*(2 * np.pi * (1. / 2**(reg_nbit) ))

    ## Ax=bを解く行為を何回繰り返すか
    trial_num = 1
    ### ---------  パラメータ設定終わり -------------- ###

    ## 真の解を求めておく
    x_true = np.linalg.solve(A, b)
    #np.allclose(np.dot(A, x_true), b) ## <- 解が正しいかの確認

    ## 対角化してしまう. AP = PD <-> A = P*D*P^dag 
    D_A, P = np.linalg.eigh(A0)


    ### ---------  以下, 計算コード  -------------- ###
    print("nbit, reg_nbit, t = {0}, {1}, {2}".format(nbit, reg_nbit,t) )


    #####################################
    ### HHL量子回路を作る. 0番目のビットから順に、Aの作用する空間のbit達 (0番目 ~ nbit-1番目), 
    ### register bit達 (nbit番目 ~ nbit+reg_nbit-1番目), conditional回転用のbit (nbit+reg_nbit番目)
    ### とする.
    #####################################
    total_qubits = nbit + reg_nbit + 1
    total_circuit = QuantumCircuit(total_qubits)

    ## ------ 0番目~(nbit-1)番目のbitに入力するベクトルbの準備 ------
    ## 本来はqRAMのアルゴリズム(論文Fig.4)を用いるが, ここでは自作の入力ゲートを用いている. 
    ## qulacsではstate.load(b)でも実装可能.
    state = QuantumState(total_qubits)
    state.set_zero_state() 
    b_gate = HHL_func.input_state_gate(0, nbit-1, b0)
    total_circuit.add_gate(b_gate)

    ## ------- レジスターbit に Hadamard gate をかける -------
    for register in range(nbit, nbit+reg_nbit): ## from nbit to nbit+reg_nbit-1
        total_circuit.add_H_gate(register)

    ## ------- 位相推定を実装 -------
    ## U := e^{i*A*t), その固有値をdiag( {e^{i*2pi*phi_k}}_{k=0, ..., N-1) )とおく.
    ## Implement \sum_j |j><j| exp(i*A*t*j) to register bits
    for register in range(nbit, nbit+reg_nbit):
        ## U^{2^{register-nbit}} を実装.
        ## 対角化した結果を使ってしまう
        U_mat = reduce(np.dot,  [P, np.diag(np.exp( 1.j*D_A*t * (2**(register-nbit)) )), P.T.conj()]  )
        U_gate = gate.DenseMatrix(np.arange(nbit), U_mat)
        U_gate.add_control_qubit(register, 1) ## control bitの追加
        total_circuit.add_gate(U_gate)

    ## ------- Perfrom inverse QFT to register bits -------
    total_circuit.add_gate(HHL_func.QFT_gate(nbit, nbit+reg_nbit-1, Inverse=True))

    ## ------- conditional rotation を掛ける -------
    ## レジスター |phi> に対応するA*tの固有値は l = 2pi * 0.phi = 2pi * (phi / 2**reg_nbit).
    ## conditional rotationの定義は
    ## |phi>|0> -> C/(lambda)|phi>|0> + sqrt(1 - C^2/(lambda)^2)|phi>|1>.
    ## 古典シミュレーションなのでゲートをあらわに作ってしまう.
    condrot_mat = np.zeros( (2**(reg_nbit+1), (2**(reg_nbit+1))), dtype=complex)
    for index in range(2**reg_nbit):
        lam = 2 * np.pi * (float(index) / 2**(reg_nbit) )
        index_0 = index ## integer which represents |index>|0>
        index_1 = index + 2**reg_nbit ## integer which represents |index>|1>
        if lam >= C:
            condrot_mat[index_0, index_0] = C / lam 
            condrot_mat[index_1, index_0] =   np.sqrt( 1 - C*C/lam/lam)
            condrot_mat[index_0, index_1] = - np.sqrt( 1 - C*C/lam/lam)
            condrot_mat[index_1, index_1] = C / lam
        else:
            condrot_mat[index_0, index_0] = 1.
            condrot_mat[index_1, index_1] = 1.
    ## DenseGateに変換して実装
    condrot_gate = gate.DenseMatrix(np.arange(nbit, nbit+reg_nbit+1), condrot_mat) 
    total_circuit.add_gate(condrot_gate)

    ## ------- Perfrom QFT to register bits -------
    total_circuit.add_gate(HHL_func.QFT_gate(nbit, nbit+reg_nbit-1, Inverse=False))

    ## ------- 位相推定の逆を実装(U^\dagger = e^{-iAt}) -------
    for register in range(nbit, nbit+reg_nbit): ## from nbit to nbit+reg_nbit-1
        ## {U^{\dagger}}^{2^{register-nbit}} を実装.
        ## 対角化した結果を使ってしまう
        U_mat = reduce(np.dot,  [P, np.diag(np.exp( -1.j*D_A*t * (2**(register-nbit)) )), P.T.conj()]  )
        U_gate = gate.DenseMatrix(np.arange(nbit), U_mat)
        U_gate.add_control_qubit(register, 1) ## control bitの追加
        total_circuit.add_gate(U_gate)

    ## ------- レジスターbit に Hadamard gate をかける -------
    for register in range(nbit, nbit+reg_nbit): 
        total_circuit.add_H_gate(register)

    ## ------- 補助ビットを0に射影する(古典シミュレーションなので確率100%で可能) -------
    total_circuit.add_P0_gate(nbit+reg_nbit)

    #####################################
    ### HHL量子回路を実行し, 結果を取り出す
    #####################################
    total_circuit.update_quantum_state(state)
    ## 0番目から(nbit-1)番目の bit が計算結果 |x>に対応
    result = state.get_vector()[:2**nbit].real
    x_HHL = result*t/C

    x_HHL = x_HHL[:n] # 不要な部分の切り取り

    return x_HHL, x_true


if __name__ == "__main__":

    #####################################
    ### A, bの準備
    #####################################
    ### 行列の次元
    n = 10

    ### エルミート行列Aをランダムに決める
    A = np.random.rand(n, n) #+ 1.j*np.random.rand(N, N)
    A = (A + A.T.conj()) /2.
    A = A + 1*np.eye(n) ## 固有値が全て正になるように値を足しておく(本来はconditional rotationで補正する)
    ## ベクトルbを決める(ランダム)
    b = np.random.rand(n) #+ 1.j*np.random.rand(n)

    #####################################
    ### Ax=bを解く
    #####################################    
    x_HHL, x_true = HHL_solve(A, b)

    print("HHL:  ", x_HHL)
    print("exact:", x_true)


    