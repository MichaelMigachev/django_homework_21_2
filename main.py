from http.server import BaseHTTPRequestHandler, HTTPServer
import os


# Настройки запуска
HOST_NAME = "localhost"
SERVER_PORT = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Проверяем, какой URL был запрошен
        if self.path == "/":
            # Если запрошен корневой URL, отправляем страницу "Контакты"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Читаем содержимое HTML-файла с контактами
            file_path =  os.path.join(os.path.dirname(__file__), "pages", "contacts.html")  # Формируем путь к файлу contacts.html
            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()
            self.wfile.write(bytes(html_content, "utf-8"))
        else:
            # Если запрошен другой URL, отправляем 404 Not Found
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<h1>404 Not Found</h1>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), MyServer)
    print(f"Server started http://{HOST_NAME}:{SERVER_PORT}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
