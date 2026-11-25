"""Entrega do Encontro 3: identificação, Trabalho Orientado, quiz e reflexão sobre a interface.

Preencha os campos abaixo e rode:
    python praticas/quiz_encontro3.py
As perguntas estão em praticas/QUIZ3.md.
"""

ALUNO = ""            # seu nome completo
MATRICULA = ""        # opcional

# Trabalho Orientado: o tema (pode ter mudado desde o Encontro 2) e a interface que você imagina.
TEMA_TRABALHO = ""    # ex.: "assistente que lê laudos de vistoria de imóveis e resume os problemas"
INTERFACE = ""        # ex.: "upload de fotos e PDF do laudo; chat para perguntas; botão para gerar o resumo em voz"

RESPOSTAS = {
    1: "",   # a, b, c ou d
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: "",
    11: "",
}

# Prática 4: qual estratégia de memória você usaria no seu Trabalho Orientado, e por quê? (custo e o que precisa ser lembrado)
ESTRATEGIA_MEMORIA = ""


if __name__ == "__main__":
    faltando = [q for q, r in RESPOSTAS.items() if str(r).strip().lower() not in ("a", "b", "c", "d")]
    print("Aluno:", ALUNO or "NOME NÃO PREENCHIDO")
    print("Tema do Trabalho Orientado:", TEMA_TRABALHO or "AINDA NÃO DEFINIDO")
    print("Interface imaginada:", INTERFACE or "FALTANDO")
    print("Respostas:", {q: str(r).strip().lower() for q, r in RESPOSTAS.items()})
    print("Estratégia de memória:", "preenchida" if ESTRATEGIA_MEMORIA.strip() else "FALTANDO")
    if faltando:
        print("Atenção, perguntas sem resposta válida:", faltando)
    elif ALUNO and INTERFACE.strip() and ESTRATEGIA_MEMORIA.strip():
        print("Entrega completa. Envie o link do seu repositório (ou o .zip, sem .env e sem .venv) pelo portal.")
