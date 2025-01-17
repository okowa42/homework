# SPDX-FileCopyrightText: 2025 Akari Hirohara <a.hirohara.0526@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import time

class BitcoinPublisher(Node):
    def __init__(self):
        super().__init__('bitcoin_publisher')
        # パブリッシャーを作成（String 型でトピックを作成）
        self.publisher_ = self.create_publisher(String, 'bitcoin_price', 10)
        # タイマーを作成 (10秒ごとにtimer_callbackを呼び出す)
        self.timer = self.create_timer(10.0, self.timer_callback)

    def timer_callback(self):
        try:
            # CoinGecko APIからビットコインの価格を取得
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
            response = requests.get(url)
            response.raise_for_status()  # HTTPエラーをキャッチ
            data = response.json()

            # ビットコインの価格を取得し、floatに変換
            bitcoin_price = float(data['bitcoin']['usd'])

            # トピックにフォーマットされた文字列をパブリッシュ
            msg = String()
            msg.data = f"bitcoin_price: {bitcoin_price} USD"
            self.publisher_.publish(msg)

        except requests.exceptions.HTTPError as e:
            # レートリミットエラー対応
            if e.response.status_code == 429:
                error_msg = f"Rate limit exceeded. Retrying after delay... ({e})"
                msg = String()
                msg.data = f"bitcoin_price: ERROR - {error_msg}"  # エラーメッセージを送信
                self.publisher_.publish(msg)
                time.sleep(60)  # 60秒待機して再試行
            else:
                error_msg = f"HTTP error occurred: {e}"
                msg = String()
                msg.data = f"bitcoin_price: ERROR - {error_msg}"  # エラーメッセージを送信
                self.publisher_.publish(msg)

        except (requests.RequestException, KeyError, ValueError) as e:
            # その他のエラーが発生した場合
            error_msg = f"Failed to fetch Bitcoin price: {e}"
            msg = String()
            msg.data = f"bitcoin_price: ERROR - {error_msg}"  # エラーメッセージを送信
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    bitcoin_publisher = BitcoinPublisher()

    try:
        rclpy.spin(bitcoin_publisher)
    except KeyboardInterrupt:
        pass

    bitcoin_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

