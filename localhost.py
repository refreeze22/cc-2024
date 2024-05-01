import socket

def start_server(host='0.0.0.0', port=12345):
    # Membuat socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Menentukan alamat dan port
    server_address = (host, port)
    server_socket.bind(server_address)

    # Mendengarkan koneksi
    server_socket.listen(1)
    print(f"Server mendengarkan di {host}:{port}")

    while True:
        # Menerima koneksi
        print("Menunggu koneksi...")
        connection, client_address = server_socket.accept()
        try:
            print(f"Koneksi diterima dari {client_address}")

            # Menerima pesan dari klien
            data = connection.recv(1024)
            print(f"Pesan diterima: {data.decode('utf-8')}")

            # Mengirim balasan ke klien
            message = "Pesan dari server: Terima kasih sudah menghubungi saya."
            connection.sendall(message.encode('utf-8'))
        finally:
            # Menutup koneksi
            connection.close()

if __name__ == "__main__":
    start_server()
