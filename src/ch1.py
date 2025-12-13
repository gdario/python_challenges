import math
from collections import deque


def extract_digits(number):
    remaining_value = number
    while remaining_value > 0:
        remaining_value, digit = divmod(remaining_value, 10)
        print(digit, end=' ')


def extract_digits_as_list(number, reverse=False):
    remaining_value = number
    digits = []
    while remaining_value > 0:
        remaining_value, digit = divmod(remaining_value, 10)
        digits.append(digit)
    if reverse:
        return list(reversed(digits))
    else:
        return digits


def count_digits(nuber):
    remaining_value = number
    count = 0
    while remaining_value > 0:
        remaining_value = remaining_value // 10
        count += 1
    return count


def find_proper_divisors(number):
    divisors = [1]
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            divisors.append(divider)
    return divisors


def eratosthenes_sieve1(number):
    candidates = list(range(2, number + 1))
    marked = set()
    primes = []
    for i, p in enumerate(candidates):
        if p in marked:
            continue
        else:
            primes.append(p)
            for j in range(i+1, len(candidates)):
                if candidates[j] % p == 0:
                    marked.add(candidates[j])
    return primes


def is_prime(number):
    return number in eratosthenes_sieve1(number)


def prime_number_pairs(number, dist=2):
    """If dist = 2 returns twin primes.
    If dist = 4 returns cousin primes.
    If dist = 6 returns sexy primes."""
    res = dict()
    for n in range(2, number + 1):
        if is_prime(n) and is_prime(n + dist):
            res[n] = n + dist
    return res


def is_perfect_number(number):
    proper_divisors = find_proper_divisors(number)
    return sum(proper_divisors) == number


def calc_perfect_numbers(max_exclusive):
    return [n for n in range(2, max_exclusive) if is_perfect_number(n)]


def is_armstrong_number(number):
    """An Armstrong number is one where the number is equal to the sum
    of its digits, each exponentiated to the number of digits. For
    example: 153 = 1^3 + 5^3 + 3^3
    """
    digits = extract_digits_as_list(number)
    number_of_digits = len(digits)
    return number == sum([digit ** number_of_digits for digit in digits])


def simple_checksum(number):
    digits = extract_digits_as_list(number, reverse=True)
    return sum(x[0] * x[1]
               for x in (zip(digits, range(1, len(digits) + 1)))) % 10


def calc(m, n):
    return (m*n // 2) % 7


def calc_sum_and_count_all_numbers_div_by_2_or_7_exclusive(max_exclusive):
    candidates = range(2, max_exclusive)
    results = []
    for candidate in candidates:
        if candidate % 2 == 0 or candidate % 7 == 0:
            results.append(candidate)
    return len(results), sum(results)


def number_to_text(n):
    digits = extract_digits_as_list(n, reverse=True)
    mapping = {
        0: 'ZERO',
        1: 'ONE',
        2: 'TWO',
        3: 'THREE',
        4: 'FOUR',
        5: 'FIVE',
        6: 'SIX',
        7: 'SEVEN',
        8: 'EIGHT',
        9: 'NINE'
    }
    return ' '.join([mapping[digit] for digit in digits])


def roman_to_decimal(roman_number):
    # Repetition rule: no more than 3 consecutive identical digits
    # Subtraction rules
    # I only precedes V and X
    # X precedes only L and C
    # C only preceds D and M

    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i, current_numeral in enumerate(roman_number[:-1]):
        next_numeral = roman_number[i+1]
        # Rule 1
        if next_numeral == current_numeral:
            tmp = roman_number[i:i+4]
            if len(tmp) > 3 and len(set(tmp)) == 1:
                print('ERROR! Impossible number')
                break

        # Rule 2
        # if rank_next_numeral >= rank_current_numeral:
        #     result += mapping[current_numeral]
        if (
                (current_numeral == 'I' and next_numeral in 'VX') or
                (current_numeral == 'X' and next_numeral in 'LC') or
                (current_numeral == 'C' and next_numeral in 'DM')
        ):
            result -= mapping[current_numeral]
        else:
            result += mapping[current_numeral]
    return result + mapping[roman_number[-1]]


def decimal_to_roman(number):
    # Compute the digits
    # Compute the orders of magnitude (OoM)
    # Cases: 1-3, 4, 5, 6-8, 9
    # Each OoM has different symbols, but the rules are the same
    digits = extract_digits_as_list(number, reverse=True)
    ooms = range(len(digits)-1, -1, -1)
    digit_oom = zip(digits, ooms)
    mapping = [{1: 'I', 5: 'V'}, {1: 'X', 5: 'L'}, {1: 'C', 5: 'D'},
               {1: 'M', 5: 'B'}]
    result = ''
    for (digit, oom) in digit_oom:
        if digit in (1, 2, 3):
            result += mapping[oom][1] * digit
        elif digit == 4:
            result += mapping[oom][1] + mapping[oom][5]
        elif digit == 5:
            result += mapping[oom][5]
        elif digit in (6, 7, 8):
            result += mapping[oom][5] + mapping[oom][1]*(digit-5)
        elif digit == 9:
            result += mapping[oom][1] + mapping[oom+1][1]
    return result


def combinatorics1(max_val=100):
    results = []
    squares = [x**2 for x in range(1, max_val)]
    for n in range(1, max_val):
        for m in range(1, max_val):
            csq = n**2 + m**2
            if csq in squares:
                results.append((n, m, int(math.sqrt(csq))))
    return results


if __name__ == '__main__':
    number = 299792458
    extract_digits(number)
    print()
    print(count_digits(number))
