# Lesson Python

## Setup

バージョン管理ツールのインストー

```sh
brew install pyenv
```

終わったらこれを使って Python をインストール

```sh
pyenv install -l
```

でバージョンが見れるのでお好みで

```sh
pyenv install 3.10.5
```

終わったら

```sh
pyenv versions
```

で確認できるが,指定されてないので

```sh
pyenv global 3.10.5
```

とすれば OK

最後に path を通して

```sh
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

ターミナルを再起動して

```sh
python -V
```

もしくは

```sh
python --version
```

インストールしたバージョンが表示されれば準備完了 🎉

## Formatter の設定

`setting.json`

```json
  "[python]": {
    "editor.defaultFormatter": null
  },
```

[ここらへん](https://qiita.com/sin9270/items/85e2dab4c0144c79987d#autopep8)から自由に選択

```json
"python.formatting.provider": "black",
```

私は black を選択した

```
pip install black
```

## Reference

- https://qiita.com/Fendo181/items/a934e4f94021115efb2e
