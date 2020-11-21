import psutil

def count_cpu():
    print(f"Liczba logicznych procesorów: {psutil.cpu_count()}, liczba procesorów fizycznych: {psutil.cpu_count(logical=False)}")

count_cpu()
