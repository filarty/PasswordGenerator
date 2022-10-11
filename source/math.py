import random
import numpy

def gen_random_numbers(count: int) -> list[int]:
    return [random.randrange(1, 9) for _ in range(count)]

def get_distribution_numbers(number: int, number_list: list[int]) -> list[int]:
    summ_num_list = sum(number_list)
    result_list = [int(numpy.around((i * number) / summ_num_list)) for i in number_list]
    if sum(result_list) == number:
        return result_list
    return get_distribution_numbers(number, number_list)
    
def get_random_distribution_numbers(count: int) -> list[int]:
    return (get_distribution_numbers(count, gen_random_numbers(count=4)))


if __name__ == "__main__":
    print(get_distribution_numbers(6, gen_random_numbers(count=4)))

