# simulador-fila-impressora-3d
## Descrição do Problema
Sistema que organiza uma fila de impressão 3D priorizando peças urgentes e calculando o tempo total de impressão com base no volume e velocidade da impressora.
## Requisitos
- Aceitar uma lista de jobs com nome, volume (cm3) e prioridade (alta/baixa).
- Ordenar a fila garantindo que itens de alta prioridade saiam primeiro.
- Calcular o tempo de impressão usando uma velocidade fixa de 10 cm3/min.
- Somar o tempo total da fila.
## Exemplo de Uso
Entrada: jobs = [{"nome": "Suporte", "volume": 50, "prioridade": "baixa"}, {"nome": "PeçaCritica", "volume": 20, "prioridade": "alta"}]
Saída: Fila: Peçacritica -> Suporte. Tempo Total: 7.0 min