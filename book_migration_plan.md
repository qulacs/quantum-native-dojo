# Book Migration Plan

`book.pdf` をもとに、Quantum Native Dojo を「全章 ipynb 前提」で再編するための構成案。

## 方針

- 公開単位は原則すべて `ipynb` に統一する
- `index.rst` はサイト入口として残し、章トップ notebook を `toctree` に並べる
- 各章トップ notebook も含めて、可能な限り書籍版の文言と構成に忠実に移行する
- 各章トップ notebook は書籍版の章扉にある導入文と、その章内の節 notebook への `nbsphinx-toctree` を持つ
- 各節は原則 1 notebook
- コラムは独立性が高いものは別 notebook に分ける
- 図は初回移行ではプレースホルダを置く
- 出力セルは原則コミットしない、または最小限にする
- PDF からの読み取りが難しい箇所や、書籍版との対応に自信が持てない箇所は、その都度報告する

## この方針を採る理由

- 現在の公開基盤は `nbsphinx` なので、`ipynb` を直接サイトに載せる構成と相性がよい
- 書籍版は本文とコードが混在する節が多く、`ipynb` 1本化のほうが自然
- 章トップだけ別形式にすると運用ルールが増える
- 将来的に Colab 導線を復活させやすい

## 推奨運用

- 配布物は `ipynb`
- 編集元は将来的に Jupytext 併用を推奨
- ただし初回移行はまず `ipynb` を正として進めてよい

## 推奨ファイル構成

### サイト入口

- `index.rst`

### notebooks 配下

```text
notebooks/
  0_quantum_computing_basics.ipynb
  0.1_what_is_quantum_computing.ipynb
  0.2_historical_background_of_quantum_computing.ipynb
  0.3_hardware_platforms_for_quantum_computing.ipynb

  1_foundations_of_quantum_information_science.ipynb
  1.1_single_qubit_representation.ipynb
  1.2_single_qubit_operations.ipynb
  1.3_multi_qubit_representation_and_operations.ipynb
  1.4_quantum_circuit_diagrams.ipynb
  1.c1_bloch_sphere.ipynb
  1.c2_universal_gate_sets.ipynb
  1.c3_no_cloning_theorem.ipynb

  2_introduction_to_quantum_algorithms.ipynb
  2.1_classification_of_quantum_algorithms.ipynb
  2.2_hadamard_test.ipynb
  2.3_quantum_fourier_transform.ipynb
  2.4_basics_of_quantum_phase_estimation.ipynb
  2.c1_quantum_algorithm_zoo.ipynb
  2.c2_big_o_notation.ipynb
  2.c3_computational_complexity.ipynb
  2.c4_qpe_complexity_and_quantum_speedup.ipynb

  3_programming_quantum_algorithms_with_quri_parts.ipynb
  3.1_introduction_to_quri_parts.ipynb
  3.2_chsh_simulation_with_quri_parts.ipynb

  4_quantum_dynamics_simulation.ipynb
  4.1_what_is_dynamics.ipynb
  4.2_trotter_based_quantum_dynamics_simulation.ipynb
  4.3_other_quantum_dynamics_simulation_methods.ipynb

  5_variational_quantum_circuit_algorithms.ipynb
  5.1_variational_quantum_eigensolver.ipynb
  5.2_quantum_circuit_learning.ipynb
  5.3_quantum_approximate_optimization_algorithm.ipynb
  5.c1_measurement_of_energy_expectation_and_statistical_fluctuation.ipynb
  5.c2_barren_plateaus.ipynb
  5.c3_quantum_annealing.ipynb

  6_quantum_chemistry_with_nisq_algorithms.ipynb
  6.1_background_of_quantum_chemistry.ipynb
  6.2_implementation_of_vqe_for_quantum_chemistry.ipynb
  6.3_qsci.ipynb
  6.c1_molecular_orbital_method_and_second_quantization.ipynb

  7_applications_of_quantum_phase_estimation.ipynb
  7.1_iterative_quantum_phase_estimation.ipynb
  7.2_shors_algorithm.ipynb
  7.3_hhl_algorithm_for_linear_systems.ipynb
  7.c1_auxiliary_qubit_reduction_in_qpe.ipynb
  7.c2_quantum_circuits_for_classical_computation_and_quantum_arithmetic.ipynb
  7.c3_qram.ipynb

  8_quantum_search_algorithms.ipynb
  8.1_oracles.ipynb
  8.2_grovers_algorithm.ipynb
  8.3_qaa_and_qae.ipynb
  8.c1_fixed_point_grover.ipynb
  8.c2_usefulness_of_quadratic_speedup.ipynb

  9_quantum_error_correction.ipynb
  9.1_introduction_to_quantum_error_correction.ipynb
  9.2_noise_models_in_quantum_mechanics.ipynb
  9.3_basics_of_quantum_error_correcting_codes.ipynb
  9.4_stabilizer_formalism_and_codes.ipynb
  9.5_fault_tolerant_quantum_computing.ipynb
  9.6_surface_codes.ipynb
  9.c1_nisq_and_quantum_error_mitigation.ipynb
  9.c2_physical_metrics_t1_t2.ipynb
  9.c3_discretization_of_errors.ipynb
  9.c4_gottesman_knill_and_quantum_advantage.ipynb
  9.c5_mbqc_and_fault_tolerant_quantum_computing.ipynb
  9.c6_quantum_ldpc_codes.ipynb
```

## 命名規則

- 章トップ: `<chapter>_<chapter_slug>.ipynb`
- 節: `<chapter>.<section>_<section_slug>.ipynb`
- コラム: `<chapter>.c<index>_<column_slug>.ipynb`

例:

- `3_programming_quantum_algorithms_with_quri_parts.ipynb`
- `3.1_introduction_to_quri_parts.ipynb`
- `7.c3_qram.ipynb`

## 章トップ notebook の役割

各章トップ notebook には以下だけを持たせる。

- 章タイトル
- 書籍版の章扉に対応する導入文
- 必要なら前提知識や注意
- 章内節への `nbsphinx-toctree`
- 章内コラムへの `nbsphinx-toctree`

章トップの本文も、要約ではなく書籍版の導入文へできるだけ忠実に合わせる。
ただしサイト導線上の都合で最低限の体裁調整は許容する。

## 章ごとの扱い

### 第0章

- 現行 `0_prologue.ipynb` は全面置換
- 書籍版では 0.1, 0.2, 0.3 の3節構成
- 図依存があるが、初回は図プレースホルダで進められる

### 第1章

- 現行の骨格は比較的近い
- ただしコラム構成は再設計する
- `1.c_CHSH-inequality_etc.ipynb` は分割前提で考える

### 第2章

- 現行との親和性は高い
- コラムを追加して書籍版構成に寄せる

### 第3章

- 現行構成は全面置換
- `Qulacs` / `Qiskit` 章から `QURI Parts` 章へ移行
- 既存ファイルを修正流用するより、新規 notebook を切る方が安全

### 第4章

- 4.1, 4.2 は流用可能性あり
- 4.3 は新設

### 第5章

- 5.1, 5.2, 5.3 は現行資産をベースに再執筆可能
- コラムは書籍版に合わせて入れ替える
- 現行の分類/QRC コラムは別扱いにするか、今回移行対象外として退避を検討

### 第6章

- 現行は `OpenFermion + Qulacs + SS-VQE`
- 書籍版は `背景知識 + VQE + QSCI`
- 章の構成変更が大きいため、新規ファイル作成がよい

### 第7章

- 7.1 は現行資産を一部流用できる可能性あり
- 7.2 は HHL ではなく Shor に変更
- 7.3 は HHL の応用先が変わる
- コラムも入れ替え前提

### 第8章

- 8.1, 8.2 は現行流用可能
- 8.3 は新設

### 第9章

- 現行 2 節構成から書籍版 6 節構成へ大幅拡張
- 章トップから全面的に作り直す
- この章は後半の核なので、独立した移行フェーズに分けるのがよい

## コラムの扱い

コラムは以下のどちらかで統一する。

- 独立 notebook 化する
- 関連節の末尾に内包する

今回は「全章 ipynb 前提」で統一感を出すため、独立 notebook 化を推奨する。

独立化のメリット:

- 目次構造が書籍に近づく
- 再利用しやすい
- 将来の差し替えがしやすい

内包のほうがよいケース:

- 1ページ未満の短い補足
- コードを伴わない注記

## 目次構成のイメージ

`index.rst`:

```rst
.. toctree::
   :maxdepth: 2
   :caption: 目次

   notebooks/0_quantum_computing_basics
   notebooks/1_foundations_of_quantum_information_science
   notebooks/2_introduction_to_quantum_algorithms
   notebooks/3_programming_quantum_algorithms_with_quri_parts
   notebooks/4_quantum_dynamics_simulation
   notebooks/5_variational_quantum_circuit_algorithms
   notebooks/6_quantum_chemistry_with_nisq_algorithms
   notebooks/7_applications_of_quantum_phase_estimation
   notebooks/8_quantum_search_algorithms
   notebooks/9_quantum_error_correction
```

章トップ notebook の `toctree` 例:

```md
- [3-1. QURI Parts とは](3.1_introduction_to_quri_parts.ipynb)
- [3-2. 応用例: ベル不等式（CHSH 不等式）の破れのシミュレーション](3.2_chsh_simulation_with_quri_parts.ipynb)
```

## 既存ファイルの扱い

初回移行では、既存 notebook をすぐ削除しない。

- 旧 notebook はいったん残す
- 新構成を `index.rst` から参照する
- 新章が安定してから旧 notebook を整理する

この進め方だと、大規模移行中もサイトを壊しにくい。

## 初回移行の優先順

1. 骨組みだけ先に作る
2. 第3章を新構成で置き換える
3. 第6章を新構成で置き換える
4. 第7章を置き換える
5. 第9章を拡張する
6. 第0章と第1章を書籍版に寄せる
7. 第4章, 第5章, 第8章を仕上げる

## notebook テンプレート方針

各節 notebook の基本構成は以下を推奨する。

1. タイトル
2. この節で学ぶこと
3. 本文
4. 必要な図プレースホルダ
5. 実装コード
6. まとめ
7. 参考文献

図プレースホルダ例:

```md
> 図 4.2 プレースホルダ
> トロッター分解の概念図を後で挿入
```

## 読み取りが難しい箇所の扱い

- PDF から数式、行列、添字、図表キャプションを機械的に抽出しづらい箇所は、無理に断定せず要確認として扱う
- 旧 notebook や他の既存ソースを援用した場合は、その旨を明記する
- 書籍版と完全一致している自信がない箇所は、移行時にユーザーへ報告する
- 特に数式の崩れ、図参照の対応、コラムの独立化に伴う文脈差分は注意点として残す

## 実装時の最小更新ポイント

- `index.rst` の章一覧差し替え
- 各章トップ notebook 新設
- `README.md` の目次と説明更新
- 必要に応じて `conf.py` に notebook 実行ポリシーを追加

## 補足

- ローカルでは `make html` は未実行完走
- 理由: `sphinx-build` 未導入
- ただし構成上は現行の `nbsphinx` パイプラインにそのまま載せられる

## 次の実装ステップ

この案に沿って着手するなら、次は以下を行う。

1. 新しい章トップ notebook を10本作る
2. 新しい節 notebook の空ファイルを一式作る
3. `index.rst` を新構成へ差し替える
4. まず第3章から本文移行を始める
