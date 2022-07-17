# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

def sum_of_neighbour(numbers: list) -> list:
    neighbour = []
    for i in range(len(numbers)):
        if i == len(numbers) -1:
            neighbour.append(numbers[i-1] + numbers[0])
        else:
            neighbour.append(numbers[i-1] + numbers[i+1])
    return neighbour

print(sum_of_neighbour([1, 2, 3, 4, 5]))