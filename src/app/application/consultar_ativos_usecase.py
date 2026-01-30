import io
import matplotlib.pyplot as plt
from fastapi.responses import StreamingResponse
from .config.database import SessionLocal
from ..domain.services import B3Service
from ..adapters.b3_repository import B3Repository
from ..application.schemas.cotacao_schema import CotacaoSchema


repository = B3Repository(SessionLocal())
service = B3Service(repository)


class ConsultarAtivos:

    def todos_ativos(self) -> list[str]:
        ativos = service.obter_ativos()
        return ativos

    def dados_historicos_ativo(self, ativo: str) -> list[CotacaoSchema]:
        dados = service.obter_dados_historicos(ativo)
        return dados

    def estatisticas_ativo(self, ativo: str) -> dict:
        df = service.obter_dados_historicos_dataframe(ativo)
        return df.describe().to_dict()

    def gerar_grafico(
        self,
        ativo: str,
        campo: str,
        comparar_ativo: bool = False,
        outro_ativo: str = None,
    ):
        if comparar_ativo and outro_ativo != None:
            df_dois_ativos = service.obter_dados_historicos_de_dois_ativos(
                ativo, outro_ativo
            )

            ativo_1 = df_dois_ativos[df_dois_ativos["cod_negociacao"] == ativo]
            ativo_2 = df_dois_ativos[df_dois_ativos["cod_negociacao"] == outro_ativo]

            data_1 = ativo_1["data_pregrao"]
            valores_1 = ativo_1[campo]
            data_2 = ativo_2["data_pregrao"]
            valores_2 = ativo_2[campo]

            plt.figure(figsize=(12, 4))
            plt.plot(data_1, valores_1, color="blue", label=ativo)
            plt.plot(data_2, valores_2, color="red", label=outro_ativo)
            plt.xlabel("Data")
            plt.ylabel(campo)
            plt.title(f"{campo} ao longo do tempo para {ativo} e {outro_ativo}")
            plt.xticks(rotation=45, ha="right")
            plt.grid(alpha=0.3)
            plt.legend()

            buffer = io.BytesIO()
            plt.tight_layout()
            plt.savefig(buffer, format="png")
            plt.close()

            buffer.seek(0)

            return StreamingResponse(buffer, media_type="image/png")

        else:
            df_ativo = service.obter_dados_historicos_dataframe(ativo)
            data = df_ativo["data_pregrao"]
            valores = df_ativo[campo]

            plt.figure(figsize=(12, 4))
            plt.plot(data, valores, label=ativo)
            plt.xlabel("Data")
            plt.ylabel(campo)
            plt.title(f"{campo} ao longo do tempo para {ativo}")
            plt.xticks(rotation=45, ha="right")
            plt.grid(alpha=0.3)
            plt.legend()

            buffer = io.BytesIO()
            plt.tight_layout()
            plt.savefig(buffer, format="png")
            plt.close()

            buffer.seek(0)

            return StreamingResponse(buffer, media_type="image/png")

    def gerar_grafico_volume(self, ativo: str):
        df_ativo = service.obter_dados_historicos_dataframe(ativo)
        data = df_ativo["data_pregrao"]
        valores = df_ativo["volume_total_titulos_negociados"]

        plt.figure(figsize=(12, 4))
        plt.bar(data, valores, label=ativo, width=0.65)
        plt.xlabel("Data")
        plt.ylabel("Volume Total Títulos Negociados")
        plt.title(f"Volume Total Títulos Negociados ao longo do tempo para {ativo}")
        plt.xticks(rotation=45, ha="right")
        plt.grid(axis="y", alpha=0.3)
        plt.legend()

        buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format="png")
        plt.close()

        buffer.seek(0)

        return StreamingResponse(buffer, media_type="image/png")
