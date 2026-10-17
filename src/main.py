
# ============================================================
# F1 DATA TRACKER
# Bootcamp II - Entrega Intermediária
# Sistema de Gerenciamento e Análise de Dados da Fórmula 1
# ============================================================

from src.storage import carregar_dados, salvar_dados
from datetime import datetime


# Carrega os dados existentes ao iniciar o programa.
corridas, pilotos, equipes, resultados = carregar_dados()


# ============================================================
# FUNÇÕES DE ENTRADA E VALIDAÇÃO
# ============================================================

def ler_texto(mensagem):
    """Solicita um texto obrigatório."""
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Erro: este campo não pode ficar vazio.")


def ler_data(mensagem):
    """Solicita uma data válida no formato DD/MM/AAAA."""
    while True:
        valor = ler_texto(mensagem)

        try:
            data = datetime.strptime(valor, "%d/%m/%Y")
            return data.strftime("%d/%m/%Y")
        except ValueError:
            print(
                "Erro: data inválida. "
                "Utilize o formato DD/MM/AAAA, por exemplo 15/03/2026."
            )


def ler_inteiro(mensagem, minimo=1):
    """Solicita um número inteiro dentro do limite permitido."""
    while True:
        try:
            valor = int(input(mensagem))

            if valor >= minimo:
                return valor

            print(f"Erro: informe um número igual ou maior que {minimo}.")

        except ValueError:
            print("Erro: digite um número inteiro válido.")


def ler_pontos():
    """Solicita uma pontuação numérica não negativa."""
    while True:
        try:
            valor = float(input("Pontos conquistados: ").replace(",", "."))

            if valor >= 0:
                return valor

            print("Erro: os pontos não podem ser negativos.")

        except ValueError:
            print("Erro: informe uma pontuação numérica válida.")


# ============================================================
# CADASTRO DE CORRIDAS
# ============================================================

def cadastrar_corrida():
    print("\n=== CADASTRAR CORRIDA ===")

    corrida = {
        "nome": ler_texto("Nome da corrida: "),
        "circuito": ler_texto("Circuito: "),
        "data": ler_data("Data da corrida (DD/MM/AAAA): "),
"temporada": ler_inteiro("Temporada (ano): ", 1950),
    }

    if any(
        item["nome"].casefold() == corrida["nome"].casefold()
        and item["temporada"] == corrida["temporada"]
        for item in corridas
    ):
        print("Erro: esta corrida já está cadastrada nesta temporada.")
        return

    corridas.append(corrida)
    salvar_dados(corridas, pilotos, equipes, resultados)

    print("Corrida cadastrada com sucesso!")


# ============================================================
# CADASTRO DE EQUIPES
# ============================================================

def cadastrar_equipe():
    print("\n=== CADASTRAR EQUIPE ===")

    nome = ler_texto("Nome da equipe: ")

    if any(
        equipe["nome"].casefold() == nome.casefold()
        for equipe in equipes
    ):
        print("Erro: esta equipe já está cadastrada.")
        return

    equipes.append({"nome": nome})
    salvar_dados(corridas, pilotos, equipes, resultados)

    print("Equipe cadastrada com sucesso!")


# ============================================================
# CADASTRO DE PILOTOS
# ============================================================

def cadastrar_piloto():
    print("\n=== CADASTRAR PILOTO ===")

    if not equipes:
        print("Cadastre uma equipe antes de cadastrar pilotos.")
        return

    nome = ler_texto("Nome do piloto: ")
    numero = ler_inteiro("Número do piloto: ", 0)

    if any(piloto["numero"] == numero for piloto in pilotos):
        print("Erro: este número já está em uso.")
        return

    listar_equipes()

    nome_equipe = ler_texto("Nome da equipe do piloto: ")

    equipe_encontrada = next(
        (
            equipe for equipe in equipes
            if equipe["nome"].casefold() == nome_equipe.casefold()
        ),
        None,
    )

    if equipe_encontrada is None:
        print("Erro: equipe não encontrada. Cadastre-a primeiro.")
        return

    if any(
        piloto["nome"].casefold() == nome.casefold()
        for piloto in pilotos
    ):
        print("Erro: este piloto já está cadastrado.")
        return

    pilotos.append({
        "nome": nome,
        "numero": numero,
        "equipe": equipe_encontrada["nome"],
    })

    salvar_dados(corridas, pilotos, equipes, resultados)

    print("Piloto cadastrado com sucesso!")


# ============================================================
# REGISTRO DE RESULTADOS
# ============================================================

def registrar_resultado():
    print("\n=== REGISTRAR RESULTADO ===")

    if not corridas:
        print("Cadastre pelo menos uma corrida primeiro.")
        return

    if not pilotos:
        print("Cadastre pelo menos um piloto primeiro.")
        return

    listar_corridas()
    nome_corrida = ler_texto("Nome da corrida: ")

    corrida = next(
        (
            item for item in corridas
            if item["nome"].casefold() == nome_corrida.casefold()
        ),
        None,
    )

    if corrida is None:
        print("Erro: corrida não encontrada.")
        return

    listar_pilotos()
    nome_piloto = ler_texto("Nome do piloto: ")

    piloto = next(
        (
            item for item in pilotos
            if item["nome"].casefold() == nome_piloto.casefold()
        ),
        None,
    )

    if piloto is None:
        print("Erro: piloto não encontrado.")
        return

    if any(
        resultado["corrida"] == corrida["nome"]
        and resultado["piloto"] == piloto["nome"]
        for resultado in resultados
    ):
        print("Erro: já existe um resultado deste piloto nesta corrida.")
        return

    posicao = ler_inteiro("Posição final (0 para não classificado): ", 0)
    pontos = ler_pontos()
    status = ler_texto("Status (ex.: Finalizado, Abandono): ")

    resultados.append({
        "corrida": corrida["nome"],
        "piloto": piloto["nome"],
        "equipe": piloto["equipe"],
        "posicao": posicao,
        "pontos": pontos,
        "status": status,
    })

    salvar_dados(corridas, pilotos, equipes, resultados)

    print("Resultado registrado com sucesso!")


# ============================================================
# CONSULTAS E LISTAGENS
# ============================================================

def listar_corridas():
    print("\n=== CORRIDAS CADASTRADAS ===")

    if not corridas:
        print("Nenhuma corrida cadastrada.")
        return

    for corrida in corridas:
        print(
            f"- {corrida['nome']} | "
            f"Circuito: {corrida['circuito']} | "
            f"Data: {corrida['data']} | "
            f"Temporada: {corrida['temporada']}"
        )


def listar_equipes():
    print("\n=== EQUIPES CADASTRADAS ===")

    if not equipes:
        print("Nenhuma equipe cadastrada.")
        return

    for equipe in equipes:
        print(f"- {equipe['nome']}")


def listar_pilotos():
    print("\n=== PILOTOS CADASTRADOS ===")

    if not pilotos:
        print("Nenhum piloto cadastrado.")
        return

    for piloto in pilotos:
        print(
            f"- {piloto['nome']} | "
            f"Número: {piloto['numero']} | "
            f"Equipe: {piloto['equipe']}"
        )


def consultar_resultados():
    print("\n=== RESULTADOS DAS CORRIDAS ===")

    if not resultados:
        print("Nenhum resultado registrado.")
        return

    nome_corrida = input(
        "Nome da corrida (Enter para exibir todos): "
    ).strip()

    encontrados = [
        resultado for resultado in resultados
        if (
            not nome_corrida
            or resultado["corrida"].casefold() == nome_corrida.casefold()
        )
    ]

    if not encontrados:
        print("Nenhum resultado encontrado para essa corrida.")
        return

    for resultado in encontrados:
        print(
            f"Corrida: {resultado['corrida']} | "
            f"Piloto: {resultado['piloto']} | "
            f"Equipe: {resultado['equipe']} | "
            f"Posição: {resultado['posicao']} | "
            f"Pontos: {resultado['pontos']:g} | "
            f"Status: {resultado['status']}"
        )


# ============================================================
# CLASSIFICAÇÕES
# ============================================================

def consultar_classificacao():
    print("\n=== CLASSIFICAÇÃO DOS PILOTOS ===")

    if not resultados:
        print("Nenhum resultado registrado.")
        return

    pontuacoes = {}

    for resultado in resultados:
        nome = resultado["piloto"]
        pontuacoes[nome] = (
            pontuacoes.get(nome, 0) + resultado["pontos"]
        )

    ordenados = sorted(
        pontuacoes.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    for posicao, (nome, pontos) in enumerate(ordenados, start=1):
        print(f"{posicao}º - {nome}: {pontos:g} pontos")


def consultar_equipes():
    print("\n=== CLASSIFICAÇÃO DAS EQUIPES ===")

    if not resultados:
        print("Nenhum resultado registrado.")
        return

    pontuacoes = {}

    for resultado in resultados:
        equipe = resultado["equipe"]
        pontuacoes[equipe] = (
            pontuacoes.get(equipe, 0) + resultado["pontos"]
        )

    ordenadas = sorted(
        pontuacoes.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    for posicao, (nome, pontos) in enumerate(ordenadas, start=1):
        print(f"{posicao}º - {nome}: {pontos:g} pontos")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def exibir_menu():
    print("\n" + "=" * 42)
    print("             F1 DATA TRACKER")
    print("=" * 42)
    print("1. Cadastrar corrida")
    print("2. Cadastrar piloto")
    print("3. Cadastrar equipe")
    print("4. Registrar resultado")
    print("5. Consultar corridas")
    print("6. Consultar resultados")
    print("7. Consultar classificação dos pilotos")
    print("8. Consultar pontuação das equipes")
    print("9. Listar pilotos")
    print("10. Listar equipes")
    print("0. Sair")
    print("=" * 42)


def main():
    print("F1 Data Tracker iniciado.")
    print(f"Corridas carregadas: {len(corridas)}")
    print(f"Pilotos carregados: {len(pilotos)}")
    print(f"Equipes carregadas: {len(equipes)}")
    print(f"Resultados carregados: {len(resultados)}")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_corrida()

        elif opcao == "2":
            cadastrar_piloto()

        elif opcao == "3":
            cadastrar_equipe()

        elif opcao == "4":
            registrar_resultado()

        elif opcao == "5":
            listar_corridas()

        elif opcao == "6":
            consultar_resultados()

        elif opcao == "7":
            consultar_classificacao()

        elif opcao == "8":
            consultar_equipes()

        elif opcao == "9":
            listar_pilotos()

        elif opcao == "10":
            listar_equipes()

        elif opcao == "0":
            salvar_dados(corridas, pilotos, equipes, resultados)
            print("Dados salvos com sucesso.")
            print("Encerrando o F1 Data Tracker. Até a próxima!")
            break

        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
