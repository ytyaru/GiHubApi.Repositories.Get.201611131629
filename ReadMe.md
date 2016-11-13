# このソフトウェアについて

GiHubApi.Repositories.Get.201611131629は私個人が学習目的で作成したソフトウェアである。

GitHubのリポジトリ一覧を取得するバッチのPython版（AccessToken認証）。Batch版は[こちら](https://github.com/ytyaru/GiHubApi.Repositories.Get.TwoFactor.201610210748)。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe(ConEmu/Nyagos)
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [furl](https://pypi.python.org/pypi/furl)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
        * ユーザ名
        * パスワード
    * [AccessToken](https://github.com/settings/tokens)
        * scopes
            * repo
    * [API v3](https://developer.github.com/v3/)

# 設定

## HTTPヘッダ

`GetRepositories.py`の以下の部分を任意に変更すること。

```python

    username = 'username'
    token = '0123456789012345678901234567890123456789'
    timezone = 'Asia/Tokyo'

```

## URLパラメータ

`GetRepositories.py`の以下の部分を任意に変更すること。

```python

    f.args['type'] = 'owner'
    f.args['sort'] = 'created'
    f.args['direction'] = 'desc'
    f.args['per_page'] = '1000'

```

GitHubAPIのパラメータに関しては[こちら](https://developer.github.com/v3/repos/#list-your-repositories)を参照。

# 実行

```sh

    python GetRepositories.py

```

`GitHub.{username}.Repositories.json`ファイルが出力される。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

このアプリは [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) のライセンスで配布されている成果物を含んでいる。

以下、各ソフトウェアのライセンス。

software|License
--------|-------
[Python 3.4.4](https://www.python.org/downloads/release/python-344/)|[PSF License (Python Software Foundation License)](https://docs.python.org/3/license.html)
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
[furl](https://github.com/gruns/furl/blob/master/LICENSE.md)|[Unlicense](http://unlicense.org/)
