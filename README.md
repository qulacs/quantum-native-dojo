# Welcome to Quantum Native Dojo !

Quantum Native Dojoは量子コンピュータについて勉強したいと思っている方のために作られた自習教材です。

量子コンピュータの基本的な動作原理から、基礎アルゴリズム、それらを応用してどのように化学計算や金融計算などに役立てるかを学ぶことができます。本教材は誤り訂正の有る量子コンピュータのアルゴリズムの他、数年以内に実用されるであろうNISQ (Noisy Intermidiate-Scale Quantum) デバイスのアルゴリズムもカバーしています。

全ての教材が `Jupyter notebook` で製作され、そのまま Google Colaboratory 上で実行可能になっているので、面倒な環境設定をすることなく学習を始めることが可能です。

なおウェブサイト版もありますので、合わせてご利用下さい。  
https://dojo.qulacs.org

## この教材の意義： Becoming Quantum Native
量子コンピュータは、量子力学の原理に基づいて計算を行います。一方、私達がふだん目にする物理現象は主に古典力学に支配されています。ここに「量子コンピュータは難しい」と思われる原因の一端があります。

Quantum Native Dojoでは、みなさまに量子コンピュータの動作を感覚的に理解して使いこなせる**Quantum Native**になっていただくことを目標としています。Quantum Nativeへの道のりは簡単ではありませんが、このDojoを通して基礎からじっくりと量子力学と量子コンピュータの原理・応用を学ぶことが着実な一歩となるでしょう。

このDojoを巣立ち、Quantum Nativeとなったみなさまが様々な量子アルゴリズム/アプリケーションを作るエンジニアとして活躍されることを期待しています！

## 前提となる知識
Quantum Native Dojoの内容を理解するには、以下のような知識が必要です。
- 複素数とは何か
- 簡単な関数(sin, cos, exp, ...)の微積分
- 行列とベクトルの掛け算、対角化とは何か

こちらの前提知識及びPython・NumPyの使用に不安がある方は、[Chainer Tutorial](https://tutorials.chainer.org/ja/tutorial.html)の1. ~ 12.を先に学習することをオススメします。

## 教材の進め方
基本的に、このレポジトリの"notebook"フォルダ以下にある `Jupyter notebook` を読みながら/実行しながら進めていきましょう。
各 `Jupyter notebook` は `Google Colabolatory` で実行することができるので、自前で環境を構築する必要はありません。
(もちろん、Pythonに詳しい方は手元でnotebookを実行して納得するまで使い倒してください)

### `Google Colabolatory`  上で実行する場合
1. [Google Colabolatory](https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja) のページを開きます
2. `ファイル` > `ノートブックを開く` を選択します
![colab](readme-figs/how-to-colab-00.png)
![colab](readme-figs/how-to-colab-01.png)

3. `GITHUB` のタブを選択し、ノートブックの絞り込みの欄に `qulacs` と入力します
![colab](readme-figs/how-to-colab-02.png)

4. レポジトリのプルダウンで `qulacs/quantum-native-dojo` を選択し、ブランチで `master` を選択します
![colab](readme-figs/how-to-colab-03.png)

5. 開きたいノートブックを選択します
![colab](readme-figs/how-to-colab-04.png)

### `Jupyter notebook` で実行する場合
1. [Quantum Native Dojo のリポジトリ](https://github.com/qulacs/quantum-native-dojo) をフォークします
2. Console から `$ jupyter notebook` で[ノートブックを起動](https://jupyter.readthedocs.io/en/latest/running.html#running)させます

`Jupyter` を起動させるためには `Python 3.3` 以上と `Jupyter` をインストールする必要があります。

また、ノートブックに埋め込まれているコードを実行するためには、`numpy`、`scipy`、`sympy` をインストールする必要があります。
上記のパッケージをまとめてインストールするには `anaconda3` のインストールが便利です。


## 目次
===== 第1部：基礎編 =====
- 第0章 そもそも量子コンピュータとは？
- 第1章 量子情報の基礎
  - 1-1. 量子ビット
  - 1-2. 量子ビットに対する基本演算
  - 1-3. 複数量子ビットの記述
  - コラム：ユニバーサルゲートセットとは
  - 1-4. 回路図の基礎
  - コラム1：量子複製不可能 (No-Cloning) 定理
  - コラム2：Bell (CHSH) 不等式
- 第2章 量子アルゴリズム入門
  - 2-1. NISQアルゴリズムとlong-termアルゴリズム
  - 2-2. アダマールテスト
  - コラム：量子乱数生成
  - 2-3. 量子フーリエ変換
  - 2-4. 位相推定アルゴリズム（入門編）
- 第3章 量子アルゴリズムの実行環境
  - 3-1. 世界最高速シミュレータQulacsの使い方
  - 3-2. QiskitとIBM Q Experienceの使い方

===== 第2部：NISQ編 =====

- 第4章 量子ダイナミクスシミュレーション
  - 4-1. シュレディンガー方程式とは、量子ダイナミクスとは
  - 4-2. トロッター分解を用いた量子シミュレーション
- 第5章 変分量子回路に基づくアルゴリズム
  - 5-1. Variational QuantumEigensolver（VQE）アルゴリズム
  - 5-2. Quantum Circuitlearning
  - コラム：Quantum CircuitLearningを用いた分類
  - コラム：量子リザーバコンピューティング
  - 5-3. Quantum Approximate Optimazation Algorithm (QAOA):量子近似最適化アルゴリズム
- 第6章 量子化学計算
  - 6-1. OpenFermionの使い方
  - 6-2. Qulacs を用いた variational quantum eigensolver (VQE)の実装
  - 6-3. 励起状態の探索手法 (subspace-search variational quantumeigensolver)

===== 第3部：Long-term編 =====
- 第7章 量子位相推定アルゴリズムの発展
  - 7-1. 量子位相推定アルゴリズム詳説：水素分子への応用を例として
  - 7-2. Harrow-Hassidim-Lloyd (HHL)アルゴリズム
  - コラム：量子ランダムアクセスメモリー(qRAM)
  - 7-3. HHLアルゴリズムを用いたポートフォリオ最適化
  - コラム：低ランク行列に対する高速な特異値分解とサンプリング（量子-inspiredアルゴリズム
- 第8章 量子探索アルゴリズム
  - 8-1. オラクル
  - 8-2. グローバーのアルゴリズム
- 第9章 量子誤り訂正
  - 9-1. 古典エラー
  - 9-2. 量子エラー
 

`*`がついている章は、物理や化学の専門的知識が必要

## 参考文献
量子力学・量子コンピュータについてより詳しく知りたい/深く理解したい場合には、以下のような参考書をオススメします。
- 量子力学について：
  - 清水明「[量子論の基礎 - その本質のやさしい理解のために](
https://www.amazon.co.jp/dp/4781910629)」、サイエンス社 (2004)
- 量子コンピュータ・量子アルゴリズムについて：
  - 竹内 繁樹「[量子コンピュータ - 超並列計算のからくり](https://www.amazon.co.jp/dp/4062574691)」、講談社 (2005)

また、英語に抵抗がない場合、量子コンピュータの金字塔とも言えるNiesen-Chaungの教科書を読むのがベストです(分量が多いので、時間はかかります)。
- M. Nielsen and I. Chuang,  "[Quantum Computation and Quantum Information: 10th Anniversary Edition](https://www.amazon.co.jp/dp/1107002176)", Cambridge University Press (2010)

## Community
本教材について分からないことは以下のコミュニティで聞いてください。  
[Qulacs Slack Community](https://join.slack.com/t/qulacs/shared_invite/enQtNzY1OTM5MDYxMjAxLWM1ZDc3MzdiNjZhZjdmYTQ5MTJiOTEzZjI3ZjAwZTg0OGFiNjcxY2VjZWRjMWY0YjE5ZTViOWQzZTliYzdmYzY)

## 本教材の作者
本教材は[株式会社QunaSys](https://qunasys.com)と以下のContributorの方々によって作製・メンテナンスされています。

[Keisuke Fujii](http://quantphys.org/wp/keisukefujii/),
[kwkbr](https://github.com/kwkbtr),
[MakotoNakai](https://github.com/MakotoNakai),
[yoooopeeee](https://github.com/yoooopeeee),
[Kosuke Mitarai](https://scholar.google.com/citations?user=TfsGcnMAAAAJ),
[Yuya-O-Nakagawa](https://scholar.google.co.jp/citations?user=LyU8LXsAAAAJ),
[yamamoto-takahiro](https://github.com/yamamoto-takahiro)

## リリース履歴
- 2019/4/26: v0.1.0をリリースしました。
- 2019/12/5: v1.0.0をリリースしました。 
