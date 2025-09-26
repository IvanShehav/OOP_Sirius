def generate_paths():
    def backtrack(current, path):
        if current == 42 and len(path) > 0:
            yield 1 
        for steps in (1, 3, -1, -3): 
            next_num = current + steps
            if 40 <= next_num <= 49 and next_num not in path:
                yield from backtrack(next_num, path + [next_num])

    return sum(backtrack(42, []))

print(generate_paths())