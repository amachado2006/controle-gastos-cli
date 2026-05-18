"""API web simples para deploy do Controle de Gastos."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from gastos import buscar_cotacao, listar_gastos, calcular_total


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = """
            <h1>💸 Controle de Gastos Pessoais</h1>
            <p>Endpoints disponíveis:</p>
            <ul>
                <li><a href="/gastos">/gastos</a> - Lista todos os gastos</li>
                <li><a href="/total">/total</a> - Total gasto</li>
                <li><a href="/cotacao">/cotacao</a> - Cotação USD/EUR</li>
            </ul>
            """
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        elif self.path == "/gastos":
            data = listar_gastos()
            self._json(data)

        elif self.path == "/total":
            data = {"total": calcular_total()}
            self._json(data)

        elif self.path == "/cotacao":
            try:
                data = buscar_cotacao()
            except Exception as e:
                data = {"erro": str(e)}
            self._json(data)

        else:
            self.send_response(404)
            self.end_headers()

    def _json(self, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    print(f"Servidor rodando na porta {port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()