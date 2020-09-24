import socket


class TCPClient:
    def main(self):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # サーバーに接続
        clientsocket.connect(("localhost", 8080))

        # 送るのメッセージをファイルから読み込む
        with open("client_send.txt", "rb") as f:
            msg = f.read()

        # メッセージを送って
        clientsocket.send(msg)

        # サーバからのメッセージを受信
        msg = clientsocket.recv(4096)

        # client_recv.txtに書き込む
        with open("client_recv.txt", "wb") as f:
            f.write(msg)

        clientsocket.close()


if __name__ == '__main__':
    TCPClient().main()
