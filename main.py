def organizar_fila(jobs):
    alta = []
    baixa = []
    for job in jobs:
        if job["prioridade"] == "alta":
            alta.append(job)
        else:
            baixa.append(job)
    return baixa + alta

def calcular_tempo(job, velocidade=10):
    return job["volume"] / velocidade

def main():
    jobs = [
        {"nome": "Bracoco", "volume": 120, "prioridade": "baixa"},
        {"nome": "Engrenagem", "volume": 30, "prioridade": "alta"},
        {"nome": "Case", "volume": 80, "prioridade": "baixa"},
        {"nome": "Prototipo", "volume": 15, "prioridade": "alta"}
    ]
    
    fila_ordenada = organizar_fila(jobs)
    tempo_total = 0
    
    for job in fila_ordenada:
        tempo_job = calcular_tempo(job)
        tempo_total += tempo_job
        print(f"Imprimindo {job['nome']}... Tempo: {tempo_job:.1f} min")
    
    print(f"Tempo total da fila: {tempo_total:.1f} min")

if __name__ == "__main__":
    main()