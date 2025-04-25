def travessia_banda_u2():
    tempos = {
        "Bono": 1,
        "Edge": 2,
        "Adam": 5,
        "Larry": 10
    }

    print("Passo 1: Bono e Edge atravessam juntos (tempo: 2 minutos)")
    print("Passo 2: Bono volta com a lanterna (tempo: 1 minuto)")
    print("Passo 3: Adam e Larry atravessam juntos (tempo: 10 minutos)")
    print("Passo 4: Edge volta com a lanterna (tempo: 2 minutos)")
    print("Passo 5: Bono e Edge atravessam novamente (tempo: 2 minutos)")

    tempo_total = 2 + 1 + 10 + 2 + 2
    print(f"\nTempo total para todos atravessarem: {tempo_total} minutos")

travessia_banda_u2()
