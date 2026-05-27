import random

def simular_canicas():
    # 1. Fijar la semilla aleatoria con el valor 2026 antes de cualquier generación
    random.seed(2026)
    
    # 2. Realizar 10,000 repeticiones del experimento correspondiente
    n_sims = 10000
    
    # Experimento base: Una caja contiene 5 canicas rojas, 3 azules y 2 verdes.
    # Se extraen dos canicas al azar sin reemplazo. Estimar la probabilidad de que ambas sean rojas.
    caja = ['R']*5 + ['A']*3 + ['V']*2
    ambas_rojas = 0
    for _ in range(n_sims):
        drawn = random.sample(caja, 2)
        if drawn[0] == 'R' and drawn[1] == 'R':
            ambas_rojas += 1
            
    prob_c1 = ambas_rojas / n_sims
    
    # Condicional de dos cajas:
    # Caja 1: 5 rojas, 3 azules, 2 verdes
    # Caja 2: 2 rojas, 5 azules, 3 verdes
    # Se elige una caja al azar y se extraen dos canicas sin reemplazo, que resultan ser una roja y la otra verde.
    # Estimar la probabilidad de que provengan de la caja 1.
    caja1 = ['R']*5 + ['A']*3 + ['V']*2
    caja2 = ['R']*2 + ['A']*5 + ['V']*3
    rv_from_caja1 = 0
    total_rv = 0
    
    for _ in range(n_sims):
        box = random.choice([1, 2])
        if box == 1:
            drawn = random.sample(caja1, 2)
        else:
            drawn = random.sample(caja2, 2)
            
        # Verificar si resultan ser una roja y la otra verde
        if ('R' in drawn) and ('V' in drawn):
            total_rv += 1
            if box == 1:
                rv_from_caja1 += 1
                
    prob_c2 = rv_from_caja1 / total_rv if total_rv > 0 else 0
    
    # 3. Imprimir las respuestas como un número decimal con cuatro decimales
    print(f"• P(ambas rojas) = {prob_c1:.4f}")
    print(f"• P(Caja 1 | una roja y una verde) = {prob_c2:.4f}")

