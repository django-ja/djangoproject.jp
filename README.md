djangoproject.jp
================

https://djangoproject.jp/ のソースコード。

* djangoproject.jp/: デプロイされるディレクトリーです
* miya/: miyadaiku 用のテンプレートなどがあります
* static/: 静的ファイルやmiyadaikuで管理されない古いページがあります

## ビルド

miyadaiku-build コマンドを利用してビルドします。

```shell script
$ miyadaiku-build miya
$ cp -r static/* miya/outputs/
```

### miyadaiku-build コマンドについて

このコマンドを実行すると、対象ディレクトリの outputs/ 内にビルド結果が出力されます。

#### Windows 環境の場合

エンコーディングの関係で次のようなエラーが発生する場合があります。
```
UnicodeDecodeError: 'cp932' codec can't decode byte ...中略...: illegal multibyte sequence
```
この場合、シェル変数または環境変数 `PYTHONUTF8=1` をセットしてから miyadaiku-build を実行してください。

## デプロイ

デプロイにはVercelが使われています。

https://vercel.com/django-ja/djangoproject-jp/

package.json にあるビルドコマンドが実行されて、Vercel上でHTMLが生成されホスティングされます。
サイト自体はCloudFrontを通してホストされます。
