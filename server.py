import socket
import threading

def handle_client(client_socket, client_address, player_names):
    try:
        # Nhận tên người chơi
        player_name = client_socket.recv(1024).decode()
        # Gửi tên người chơi đến người chơi khác
        for name_socket in player_names:
            if name_socket != client_socket:  # Kiểm tra xem đối tượng có phải là socket hay không
                name_socket.send(player_name.encode())
        # Thêm tên người chơi vào danh sách
        player_names.append(client_socket)
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(2)

    player_names = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established!")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address, player_names))
        client_handler.start()
