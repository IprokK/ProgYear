import numpy as np
import time

list_a = np.random.rand(1000000)
list_b = np.random.rand(1000000)
numpy_array_a = np.array(list_a)
numpy_array_b = np.array(list_b)

start_time = time.perf_counter()
result_list = [a * b for a, b in zip(list_a, list_b)]
end_time = time.perf_counter()
print(f"Время выполнения для списков: {str(end_time - start_time)[:8]} секунд")

start_time = time.perf_counter()
result_numpy = np.multiply(numpy_array_a, numpy_array_b)
end_time = time.perf_counter()
print(f"Время выполнения для NumPy: {str(end_time - start_time)[:8]} секунд")
