djangoproject.jp
================

https://djangoproject.jp/ のソースコード。

* djangoproject.jp/: デプロイされるディレクトリーです
* miya/: miyadaiku 用のテンプレートなどがあります
* static/: 静的ファイルやmiyadaikuで管理されない古いページがあります

## ビルド

miyadaikuコマンドを利用してビルドします。

```shell script
$ miyadaiku miya
$ cp -r static/* miya/outputs/
```

## デプロイ

デプロイにはVercelが使われています。

https://vercel.com/django-ja/djangoproject-jp/

package.json にあるビルドコマンドが実行されて、Vercel上でHTMLが生成されホスティングされます。
サイト自体はCloudFrontを通してホストされます。
