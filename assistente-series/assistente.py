import requests
import os
from dotenv import load_dotenv

load_dotenv()

class AssistenteMaratona:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.url_base = "http://www.omdbapi.com/"

    def buscar_serie(self, nome_serie):
        try:
            params = {
                "apikey": self.api_key,
                "t": nome_serie
            }

            resposta = requests.get(self.url_base, params=params)
            dados = resposta.json()

            if dados["Response"] == "False":
                return {
                    "serie": nome_serie,
                    "erro": "Série não encontrada"
                }

            return {
                "titulo": dados["Title"],
                "ano": dados["Year"],
                "nota": dados["imdbRating"]
            }

        except Exception as erro:
            return {
                "erro": "Erro ao conectar com a API"
            }

    def listar_series(self):

        lista_series = [
            "Breaking Bad",
            "Round 6",
            "Stranger Things",
            "SerieQueNaoExiste"
        ]

        resultados_finais = []

        for serie in lista_series:
            resultado = self.buscar_serie(serie)
            resultados_finais.append(resultado)

        return resultados_finais