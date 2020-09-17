import socket


class TCPServer:
    def main(self):
        # create an INET, STREAMing socket
        # - socket.AF_INETはおまじない。(IP4桁で通信しますよ的な)
        # - socket.SOCK_STREAM（ストリームを使用するよ）
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to a public host, and a well-known port
        # - bind（どんなドメイン名？ポートはこれだよ）
        serversocket.bind(("localhost", 8080))

        # become a server socket
        # - ソケットの最大数
        serversocket.listen(1)

        print("クライアントからの接続を待ちます。")
        (clientsocket, address) = serversocket.accept()
        print("クライアント接続。")

        # クライアントから受け取ったメッセージを代入
        msg = clientsocket.recv(4096)

        # 受け取ったメッセージをファイルに書き込む
        with open("server_recv.txt", "wb") as f:
            f.write(msg)

        # 送り返す用のメッセージをファイルから読み込む
        with open("server_send.txt", "rb") as f:
            msg = f.read()

        # メッセージを送り返す
        clientsocket.send(msg)

        clientsocket.close()
        print("通信を終了しました。")


if __name__ == '__main__':
    TCPServer().main()
