from math import sqrt


def get_sum(nums: list) -> int:
    result = 0

    for num in nums:
        result += num

    return num


def get_sqaure_sum(nums: list) -> int:
    result = 0

    for num in nums:
        result += num * num

    return result


def get_sqrt_sum(nums: list) -> float:
    result = 0

    for num in nums:
        result = sqrt(num)

    return result
