import random

def simular_monedas():
    # 1. Fijar la semilla aleatoria con el valor 2026 antes de cualquier generación
    random.seed(2026)
    
    # 2. Realizar 10,000 repeticiones del experimento correspondiente
    n_sims = 10000
    exactamente_2_caras = 0
    total_caras = 0
    
    for _ in range(n_sims):
        # Simular el lanzamiento de tres monedas justas (1 = cara, 0 = cruz)
        flips = [random.choice([0, 1]) for _ in range(3)]
        x = sum(flips)
        
        # a. Estimar la probabilidad de obtener exactamente dos caras
        if x == 2:
            exactamente_2_caras += 1
            
        # b. Estimar E[X] (valor esperado del número de caras)
        total_caras += x
        
    prob_b1 = exactamente_2_caras / n_sims
    ex = total_caras / n_sims
    
    # 3. Imprimir las respuestas como un número decimal con cuatro decimales
    print(f"• P(exactamente 2 caras) = {prob_b1:.4f}")
    print(f"• E[X] = {ex:.4f}")

