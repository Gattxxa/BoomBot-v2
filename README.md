# Boom Bot-v2
[![](https://img.shields.io/badge/Python-3.10.x-informational?logo=python&logoColor=1da1f2)](https://www.python.org/) [![](https://img.shields.io/badge/discord.py-v2.0.0α_or_higher-informational?logo=python&logoColor=1da1f2)](https://www.python.org/)  
Discord API v10 に 対応させた [Boom Bot](https://twitter.com/GattxxaGame/status/1421664481114001411?s=20&t=cGi70np_P6eKXdBgXd7EPg) の新バージョン。  
スラッシュコマンドによって操作する形に変更されました。  
[Boom Bot公式WEBページ](https://gattxxa.github.io/boombot/)  
  
## 📚 How to install discord.py v2.0.0α
```
$ git clone https://github.com/Rapptz/discord.py
$ cd discord.py
$ python3 -m pip install -U .[voice]
```
> discord.py - https://github.com/Rapptz/discord.py#installing
  
## 📄 Changes from v1 to v2
- `prefix`が変更、廃止されスラッシュコマンドに移行しました。
- スラッシュコマンドへの移行により特権インテントを必要としなくなりました。
- Botコマンドを使用した際のレスポンスメッセージを変更しました。
- `/valo random` コマンドが追加されました。
- ユーザーデータの管理が `SQLite3` に変更されました。
- 公式WEBページを更新しました。
  
___
  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />この 作品 は <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">クリエイティブ・コモンズ 表示 - 非営利 - 継承 4.0 国際 ライセンス</a>の下に提供されています。
