def arithmetic_arranger(problems, show_answers=False):
    # Cek jumlah masalah
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must have two operands and an operator."
        
        num1, operator, num2 = parts

        # Cek operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Cek digit
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Cek panjang angka
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2

        first_line.append(num1.rjust(width))
        second_line.append(operator + " " + num2.rjust(width - 2))
        dashes.append("-" * width)

        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            results.append(answer.rjust(width))

    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(dashes)

    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems

# Contoh penggunaan
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "1235 + 6542","123 + 49"]))
print()
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
