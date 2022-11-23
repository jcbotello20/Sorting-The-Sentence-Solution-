import random


def generate_test_cases(num_cases):
    test_cases = []
    for i in range(num_cases):
        words = []
        for j in range(random.randint(1, 10)):
            word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')
                           for _ in range(random.randint(1, 10)))
            num = random.randint(1, 9)
            words.append(word + str(num))
        random.shuffle(words)
        input_str = ' '.join(words)
        expected_output = ' '.join(sorted(words, key=lambda x: int(x[-1]))).replace('1', '').replace('2', '').replace('3', '').replace(
            '4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')  # eliminar los números del output esperado
        test_cases.append((input_str, expected_output))
    return test_cases


test_cases = generate_test_cases(100)

for i, test_case in enumerate(test_cases):
    print(f"Test case {i+1}:")
    print(f"Input: {test_case[0]}")
    print(f"Expected output: {test_case[1]}\n")
