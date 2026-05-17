import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://api.adviceslip.com/advice"
APP_VERSION = "1.0.0"

class MedSync:
    def __init__(self):
        self.medicamentos = []

    def adicionar_medicamento(self, nome, horario):
        if not nome.strip() or not horario.strip():
            raise ValueError("Nome e horário são obrigatórios.")
        item = {"nome": nome, "horario": horario}
        self.medicamentos.append(item)
        return f"Sucesso: {nome} agendado para às {horario}."

    def listar_medicamentos(self):
        if not self.medicamentos:
            return "Nenhum medicamento agendado."
        resultado = "\n--- Medicamentos Agendados ---"
        for m in self.medicamentos:
            resultado += f"\n💊 {m['nome']} - {m['horario']}"
        return resultado

    def obter_dica_saude(self):
        request = Request(API_URL, headers={"Accept": "application/json"})
        try:
            with urlopen(request, timeout=10) as response:
                data = json.loads(response.read().decode("utf-8"))
            return data["slip"]["advice"]
        except (HTTPError, URLError, ValueError, KeyError) as error:
            return f"Não foi possível obter a dica de saúde: {error}"


def menu():
    app = MedSync()
    print(f"=== Bem-vindo ao MedSync (Versão {APP_VERSION}) ===")
    dica = app.obter_dica_saude()
    print(f"\n💡 Dica de Saúde: {dica}\n")

    while True:
        print("\n1. Adicionar Medicamento\n2. Listar Todos\n3. Ver Dica de Saúde\n4. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            n = input("Nome do remédio: ")
            h = input("Horário (ex: 08:00): ")
            try:
                print(app.adicionar_medicamento(n, h))
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            print(app.listar_medicamentos())
        elif opcao == "3":
            print(f"💡 Dica de Saúde: {app.obter_dica_saude()}")
        elif opcao == "4":
            print("Encerrando... Cuide-se!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
