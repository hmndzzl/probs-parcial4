import random

def simular_dados():
    # 1. Fijar la semilla aleatoria con el valor 2026 antes de cualquier generación
    random.seed(2026)
    
    # 2. Realizar 10,000 repeticiones del experimento correspondiente
    n_sims = 10000
    sum_7 = 0
    sum_7_given_at_least_one_par = 0
    at_least_one_par_count = 0
    
    for _ in range(n_sims):
        # Simular lanzamiento de dos dados justos de 6 caras
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        
        s = d1 + d2
        is_par = (d1 % 2 == 0) or (d2 % 2 == 0)
        
        # a. Estimar la probabilidad de que la suma sea igual a 7
        if s == 7:
            sum_7 += 1
            
        # b. Estimar la probabilidad de que la suma sea 7 dado que al menos uno de los dados es par
        if is_par:
            at_least_one_par_count += 1
            if s == 7:
                sum_7_given_at_least_one_par += 1
                
    prob_a = sum_7 / n_sims
    prob_b = sum_7_given_at_least_one_par / at_least_one_par_count if at_least_one_par_count > 0 else 0
    
    # 3. Imprimir las respuestas como un número decimal con cuatro decimales
    print(f"• P(suma = 7) = {prob_a:.4f}")
    print(f"• P(suma = 7 | al menos un par) = {prob_b:.4f}")