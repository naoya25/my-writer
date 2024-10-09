# MyWriter
PCで入力した文字を手書き風に表示するプログラムです。

# 対応文字
```plaintext
a-z, A-Z, 0-9, !?.,'
```

#  使い方
※ pyenvで環境構築していますが、他の環境でも動作すると思います。
1. 手書き文字を作成する
   1. `images/abc_large.png`, `images/abc.png`, `images/other` を参考にして、手書き文字を作成する
2. 手書き文字の前処理を行う
   1. `python char_image_settings.py` を実行する
   2. `images/abc/` に背景あり画像, `images/rm_bg_chars` に透過画像が保存される
3. 手書き表示した文章を作成する
   1. `python run.py` を実行する
   2. `output.png` に手書き表示された文章が保存される
