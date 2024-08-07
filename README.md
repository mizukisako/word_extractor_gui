# word_extractor_gui
初回ビルドする際は`word_extractor`内の環境構築を行ってください。

## 追加で必要なインストール
重複して既にインストールされているものもあるかもしれませんが、なければこれらも入れておいてください。
```
pip install spacy
pip install spacy[ja]
pip install -U ginza https://github.com/megagonlabs/ginza/releases/download/latest/ja_ginza_electra-latest-with-model.tar.gz
pip install ginza_transformers
pip install sudachipy sudachidict_core
pip install spacy_legacy
pip install --force-reinstall transformers
```

## CLI実行
`python .\word_extractor\script\extract_words.py -i input.txt -o words.csv`

## GUI実行
`python .\gui.py`

## exeファイルの作成 (Windows上でのみ可能)
`--include-data-dir`にしているパスは環境に合わせて変更してください。
```pwsh
pyenv exec nuitka --onefile --enable-plugin=tk-inter `
--include-package=spacy `
--include-package=spacy_legacy `
--include-package=ginza_transformers `
--include-package=sudachipy `
--include-package=sudachidict_core `
--include-package=transformers `
--include-package=unidic_lite `
--include-package=ipadic `
--include-data-dir="C:\Users\mizuki_sako\.pyenv\pyenv-win\versions\3.10.5\lib\site-packages\ipadic\dicdir=ipadic\dicdir" `
--include-data-dir="C:\Users\mizuki_sako\.pyenv\pyenv-win\versions\3.10.5\Lib\site-packages\unidic_lite\dicdir=unidic_lite\dicdir" `
--include-data-dir="C:\Users\mizuki_sako\.pyenv\pyenv-win\versions\3.10.5\lib\site-packages\ja_ginza_electra\ja_ginza_electra-5.2.0=spacy\data\ja_ginza_electra" `
--include-data-dir="C:\Users\mizuki_sako\.pyenv\pyenv-win\versions\3.10.5\Lib\site-packages\sudachipy\resources=sudachipy\resources" `
--include-data-dir="C:\Users\mizuki_sako\.pyenv\pyenv-win\versions\3.10.5\Lib\site-packages\sudachidict_core\resources=sudachidict_core\resources" `
.\gui.py
```

## コードサイニング
`$SignToolPath`は環境に合わせて変更してください。
署名用ドングルをPCに刺した状態で実行する必要があります。
```
$SignToolPath = "C:\Program Files (x86)\Windows Kits\10\App Certification Kit\signtool.exe"
$ExecutablePath = "C:\project\word_extractor_gui\dist\gui.exe"
& $SignToolPath sign /tr http://timestamp.sectigo.com /td sha256 /fd sha256 $ExecutablePath
```