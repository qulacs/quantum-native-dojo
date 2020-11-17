Welcome to Quantum Native Dojo!
===============================

Quantum Native Dojoは量子コンピュータについて勉強したいと思っている方のために作られた自習教材です。

量子コンピュータの基本的な動作原理から、基礎アルゴリズム、それらを応用してどのように化学計算や金融計算などに役立てるかを学ぶことができます。本教材は誤り訂正の有る量子コンピュータのアルゴリズムの他、数年以内に実用されるであろうNISQ (Noisy Intermidiate-Scale Quantum) デバイスのアルゴリズムもカバーしています。

全ての教材が Jupyter notebook で製作され、そのまま Google Colaboratory 上で実行可能になっているので、面倒な環境設定をすることなく学習を始めることが可能です。

この教材の意義：Becoming Quantum Native
---------------------------------------

量子コンピュータは、量子力学の原理に基づいて計算を行います。一方、私達がふだん目にする物理現象は主に古典力学に支配されています。ここに「量子コンピュータは難しい」と思われる原因の一端があります。

Quantum Native Dojoでは、みなさまに量子コンピュータの動作を感覚的に理解して使いこなせる **Quantum Native** になっていただくことを目標としています。Quantum Nativeへの道のりは簡単ではありませんが、このDojoを通して基礎からじっくりと量子力学と量子コンピュータの原理・応用を学ぶことが着実な一歩となるでしょう。

このDojoを巣立ち、Quantum Nativeとなったみなさまが様々な量子アルゴリズム/アプリケーションを作るエンジニアとして活躍されることを期待しています！

前提となる知識
--------------

Quantum Native Dojoの内容を理解するには、以下のような知識が必要です。

* 複素数とは何か
* 簡単な関数(sin, cos, exp, ...)の微積分
* 行列とベクトルの掛け算、対角化とは何か

こちらの前提知識及びPython・NumPyの使用に不安がある方は、 `Chainer Tutorial <https://tutorials.chainer.org/ja/tutorial.html>`_ の1.〜12.を先に学習することをオススメします。

.. toctree::
   :maxdepth: 2
   :caption: 目次

   notebooks/0_prologue
   notebooks/1_quantum_information_foundation
   notebooks/2_introduction_to_quantum_algorithms
   notebooks/3_execution_environments_of_quantum_algorithms
   notebooks/4_quantum_dynamics_simulation
   notebooks/5_VQC_based_algorithms
   notebooks/6_quantum_chemistry_calculation
   notebooks/7_quantum_phase_estimation
   notebooks/8_quantum_search_algorithm
   notebooks/9_quantum_error_correction


運営・サポート
--------------

運営： `株式会社QunaSys <https://qunasys.com>`_ 

ご意見・ご要望・質問： `Qulacs Slack Community <https://join.slack.com/t/qulacs/shared_invite/enQtNzY1OTM5MDYxMjAxLWM1ZDc3MzdiNjZhZjdmYTQ5MTJiOTEzZjI3ZjAwZTg0OGFiNjcxY2VjZWRjMWY0YjE5ZTViOWQzZTliYzdmYzY>`_ にお寄せ下さい。
