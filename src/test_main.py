
import unittest
from unittest.mock import patch

from src import main


class TestF1DataTracker(unittest.TestCase):

    def setUp(self):
        # Mantém os testes isolados dos dados reais do usuário.
        self.corridas_original = main.corridas
        self.pilotos_original = main.pilotos
        self.equipes_original = main.equipes
        self.resultados_original = main.resultados

        main.corridas = []
        main.pilotos = []
        main.equipes = []
        main.resultados = []

    def tearDown(self):
        main.corridas = self.corridas_original
        main.pilotos = self.pilotos_original
        main.equipes = self.equipes_original
        main.resultados = self.resultados_original

    def test_cadastrar_equipe(self):
        with patch("builtins.input", side_effect=["Ferrari"]):
            with patch("src.main.salvar_dados"):
                main.cadastrar_equipe()

        self.assertEqual(len(main.equipes), 1)
        self.assertEqual(main.equipes[0]["nome"], "Ferrari")

    def test_impedir_equipe_duplicada(self):
        main.equipes.append({"nome": "Ferrari"})

        with patch("builtins.input", side_effect=["Ferrari"]):
            with patch("src.main.salvar_dados"):
                main.cadastrar_equipe()

        self.assertEqual(len(main.equipes), 1)

    def test_rejeitar_nome_vazio(self):
        with patch("builtins.input", side_effect=["", "McLaren"]):
            resultado = main.ler_texto("Nome: ")

        self.assertEqual(resultado, "McLaren")

    def test_rejeitar_pontos_negativos(self):
        with patch("builtins.input", side_effect=["-10", "25"]):
            resultado = main.ler_pontos()

        self.assertEqual(resultado, 25.0)

    def test_classificacao_por_pontos(self):
        main.resultados.extend([
            {
                "piloto": "Piloto A",
                "pontos": 18,
                "equipe": "Equipe A",
            },
            {
                "piloto": "Piloto B",
                "pontos": 25,
                "equipe": "Equipe B",
            },
        ])

        with patch("builtins.print") as impressao:
            main.consultar_classificacao()

        saida = "\n".join(
            str(chamada) for chamada in impressao.call_args_list
        )

        self.assertLess(
            saida.find("Piloto B"),
            saida.find("Piloto A"),
        )


if __name__ == "__main__":
    unittest.main()
