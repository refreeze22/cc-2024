import socket

# Membuat socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan alamat dan port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Mendengarkan koneksi
server_socket.listen(1)

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
