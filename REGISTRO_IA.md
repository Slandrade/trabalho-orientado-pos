# Registro do uso de assistentes de IA

O Trabalho Orientado pede o registro transparente e crítico do uso de assistentes de IA. Acrescente uma linha a cada uso relevante.

| Data | Ferramenta e modo | O que pedi | O que o assistente fez bem | O que eu corrigi ou recusei |
| --- | --- | --- | --- | --- |
| 24/11/2026 | GitHub Copilot (Agent) | Adicionar regra em `src/validacao.py` para marcar notas de fim de semana para revisão humana e rodar `python praticas/p1_nota_fiscal.py` para testar. | Reaproveitou `data` já convertida no `try/except` com `data.weekday() >= 5` (sábado e domingo), manteve o estilo/docstring do arquivo e executou o script validando a revisão no cupom de 31/10/2026 (sábado). | Na revisão da etapa anterior, avaliei o alerta sobre dados pessoais em `dados/minha_nota.jpg` e autorizei a execução; na alteração de `src/validacao.py`, nenhum ajuste foi necessário após revisar o diff. |
