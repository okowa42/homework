# ビットコインの価格(米ドル)
[![test](https://github.com/okowa42/homework/actions/workflows/test.yml/badge.svg)](https://github.com/okowa42/homework/actions/workflows/test.yml)

## 概要
- ROS 2のパッケージです.
- [Open Notify API](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd)より取得したビットコインの米ドル価格をトピックにパブリッシュします.

## ノード
- ### bitcoin_publisher
取得したビットコインの現在の米ドル価格を10秒ごとにbitcoin_priceトピックにパブリッシュします．

## トピック
- ### bitcoin_price
bitcoin_publisherノードからパブリッシュされた，以下の形式の情報を持ちます．
```
bitcoin_price: {bitcoin_price} USD
```


## 使用方法
ROS 2のパッケージです．各自のROS 2ワークスペースにて以下のコマンドでクローンし,その後ビルドしてください．
```
git clone https://github.com/okowa42/homework.git
```
実行は以下のコマンドで行えます．
```
ros2 run homework bitcoin_publisher
```
トピックの内容は以下のコマンドで確認してください
```
ros2 topic echo /bitcoin_price 
```
```
data: 'bitcoin_price: 97995.0 USD'
---
data: 'bitcoin_price: 97995.0 USD'
---
data: 'bitcoin_price: 97995.0 USD'
---
```

## 注意点
subscriber.pyおよび，bitcoin_subscribe.launch.pyはテスト用です．

## テスト済み環境
- Ubuntu 22.04 LTS
  - ROS 2 Humble (GitHub Actions)
- Ubuntu 24.04 LTS
  - ROS 2 Jazzy (開発環境)

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)

© 2025 Akari Hirohara 
