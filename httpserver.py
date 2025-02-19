import socket
import os

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
HTDOCS_DIR = 'htdocs'  # Define the htdocs directory

def handle_request(client_connection):
    """Handles a single client request."""
    request = client_connection.recv(1024).decode()
    print(request)

    try:
        headers = request.split('\n')
        filename = headers[0].split()[1]
        if filename == '/':
            filename = 'htdocs/index.html'

        filepath = os.path.join(HTDOCS_DIR, filename.lstrip('/')) #correctly handle filepaths

        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r', encoding='utf-8') as fin: #added encoding
            content = fin.read()

        response = f'HTTP/1.0 200 OK\n\n{content}'

    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
    except Exception as e: # Catch any other errors.
        print(f"Error: {e}")
        response = 'HTTP/1.0 500 Internal Server Error\n\nInternal Server Error'

    client_connection.sendall(response.encode('utf-8')) #added encode
    client_connection.close()

def main():
    """Main server loop."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f'Listening on port {SERVER_PORT}...')

    try:
        while True:
            client_connection, client_address = server_socket.accept()
            handle_request(client_connection)
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()