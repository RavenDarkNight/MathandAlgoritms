import sys
import math

def main():
    input = sys.stdin.read().split()
    ptr = 0
    
    # Чтение входных данных
    N = int(input[ptr])
    ptr += 1
    h = list(map(int, input[ptr:ptr+N]))
    ptr += N
    
    # Префиксные суммы и суммы квадратов
    prefix = [0] * (N + 1)
    prefix_sq = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i-1] + h[i-1]
        prefix_sq[i] = prefix_sq[i-1] + h[i-1]**2
    
    Q = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(Q):
        l, r = map(int, input[ptr:ptr+2])
        ptr += 2
        
        n = r - l + 1
        sum_h = prefix[r] - prefix[l-1]
        mu = sum_h / n
        
        # Вычисление стандартного отклонения
        sum_sq = prefix_sq[r] - prefix_sq[l-1]
        variance = (sum_sq - 2 * mu * sum_h + n * mu**2) / n
        sigma = math.sqrt(variance)
        
        if sigma == 0:
            results.append(0.0)
            continue
        
        # Вычисление асимметрии
        sum_cubes = 0
        for i in range(l-1, r):
            z = (h[i] - mu) / sigma
            sum_cubes += z**3
        
        asymmetry = sum_cubes / n
        results.append(asymmetry)
    
    # Вывод результатов с требуемой точностью
    for res in results:
        print("{0:.15f}".format(res))

if __name__ == "__main__":
    main()