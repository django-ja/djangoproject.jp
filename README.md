djangoproject.jp
================

https://djangoproject.jp/ のソースコード。

* docs/: デプロイされるディレクトリー
* miya/: miyadaiku 用のテンプレートなどがあります
* static/: 静的ファイルやmiyadaikuで管理されない古いページがあります

## ビルド

miyadaiku を利用して docs 以下にビルドします。

```shell script
$ make build
```

#### Windows 環境の場合

エンコーディングの関係で次のようなエラーが発生する場合があります。
```
UnicodeDecodeError: 'cp932' codec can't decode byte ...中略...: illegal multibyte sequence
```
この場合、シェル変数または環境変数 `PYTHONUTF8=1` をセットしてから miyadaiku-build を実行してください。

## デプロイ

デプロイにはGitHub Pagesが使われます。
docs 以下が公開されるので、ビルドしてmasterにコミットしてください。
サイト自体はCloudFrontを通してホストされます。
