import random

def simular_cartas():
    # 1. Fijar la semilla aleatoria con el valor 2026 antes de cualquier generación
    random.seed(2026)
    
    # 2. Realizar 10,000 repeticiones del experimento correspondiente
    n_sims = 10000
    
    # Baraja estándar de 52 cartas. Representamos Ases como 1 y otras cartas como 0.
    # Hay 4 ases y 48 cartas que no son ases.
    baraja = [1]*4 + [0]*48
    
    ambas_ases = 0
    a_count = 0  # Primera carta es As
    b_count = 0  # Segunda carta es As
    
    for _ in range(n_sims):
        # Se extraen dos cartas al azar sin reemplazo
        drawn = random.sample(baraja, 2)
        
        if drawn[0] == 1:
            a_count += 1
        if drawn[1] == 1:
            b_count += 1
        if drawn[0] == 1 and drawn[1] == 1:
            ambas_ases += 1
            
    prob_ambas = ambas_ases / n_sims
    prob_a = a_count / n_sims
    prob_b = b_count / n_sims
    prob_a_por_b = prob_a * prob_b
    
    # Determinar si los eventos son independientes
    # Matemáticamente, dos eventos A y B son independientes si y solo si P(A y B) = P(A) * P(B).
    # Puesto que es una extracción sin reemplazo, los eventos son dependientes (el resultado del primero afecta las probabilidades del segundo).
    # En la simulación: prob_ambas != prob_a_por_b.
    son_independientes = (prob_ambas == prob_a_por_b)
    
    # 3. Imprimir las respuestas como un número decimal con cuatro decimales
    print(f"• P(ambas ases) = {prob_ambas:.4f}")
    print(f"• P(A) * P(B) = {prob_a_por_b:.4f}")
    print(f"Los eventos son independientes: {son_independientes}")

