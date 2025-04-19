# beings/conexao.py
class ConexaoSimulada:
    def __init__(self):
        self.ativa = False

    def conectar(self):
        print("🔌 Conectando...")
        self.ativa = True

    def desconectar(self):
        print("❌ Desconectando...")
        self.ativa = False