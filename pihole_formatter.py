import re

def normalize_domain(line):
    line = line.strip().lower()
    line = re.sub(r'^https?://', '', line)
    line = line.lstrip('0.0.0.0 ').strip()
    line = line.rstrip('/')
    return line

def generate_entries(domain):
    bare = normalize_domain(domain)
    if bare.startswith('www.'):
        base = bare[4:]
        return {f'0.0.0.0 {base}', f'0.0.0.0 {bare}'}
    else:
        return {f'0.0.0.0 {bare}', f'0.0.0.0 www.{bare}'}

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = set()
    for line in lines:
        if line.strip():
            result.update(generate_entries(line))

    sorted_result = sorted(result)
    with open('output.txt', 'w', encoding='utf-8') as f:
        for entry in sorted_result:
            f.write(entry + '\n')

if __name__ == '__main__':
    main()
