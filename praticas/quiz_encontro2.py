"""Entrega do Encontro 2: identificação, tema do Trabalho Orientado, quiz e justificativa da Prática 3.

Preencha os campos abaixo e rode:
    python praticas/quiz_encontro2.py
As perguntas estão em praticas/QUIZ.md.
"""

ALUNO = "Silas Leandro de Andrade Souza"            # seu nome completo
MATRICULA = ""        # opcional

# Trabalho Orientado: comece a pensar no tema. Uma ou duas frases bastam por enquanto.
TEMA_TRABALHO = (
    "Assistente multimodal de triagem de documentos financeiros que recebe imagem ou áudio, "
    "valida campos obrigatórios e estima custos de processamento."
)    # ex.: "assistente que lê laudos de vistoria de imóveis e resume os problemas"

RESPOSTAS = {
    1: "b",  # a, b, c ou d
    2: "c",
    3: "a",
    4: "b",
    5: "d",
    6: "a",
    7: "c",
    8: "b",
}

# Prática 3: qual variante você escolheria para produção, e por quê? (acurácia e tokens)
JUSTIFICATIVA_P3 = (
    "Em produção, escolheria a B-few-shot. Nos testes, todas as variantes acertaram 100% de "
    "emitente e valor_total, mas o campo data foi o gargalo: A-zero-shot teve 0.33 de acerto em data "
    "(0.78 geral, 1518 tokens/chamada) e C-visual teve 0.67 em data (0.89 geral, 1427 tokens/chamada), "
    "além de C depender de caixas pré-marcadas em posições fixas (inviável para layouts reais variados). "
    "Já B-few-shot atingiu 1.00 de acurácia em todos os campos. Embora consuma quase o dobro de tokens "
    "(2852 tokens/chamada) por enviar uma imagem de exemplo, o custo extra de ~1334 tokens é muito menor "
    "que o custo operacional de enviar notas para revisão humana por erro na data."
)


if __name__ == "__main__":
    faltando = [q for q, r in RESPOSTAS.items() if str(r).strip().lower() not in ("a", "b", "c", "d")]
    print("Aluno:", ALUNO or "NOME NÃO PREENCHIDO")
    print("Tema do Trabalho Orientado:", TEMA_TRABALHO or "AINDA NÃO DEFINIDO: comece a pensar nele")
    print("Respostas:", {q: str(r).strip().lower() for q, r in RESPOSTAS.items()})
    print("Justificativa da Prática 3:", "preenchida" if JUSTIFICATIVA_P3.strip() else "FALTANDO")
    if faltando:
        print("Atenção, perguntas sem resposta válida:", faltando)
    elif ALUNO and JUSTIFICATIVA_P3.strip():
        print("Entrega completa. Envie o link do seu repositório (ou o .zip, sem o arquivo .env) pelo portal.")
