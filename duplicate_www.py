def duplicate_www(input_file, output_file):
    domains = set()

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or not line.startswith('0.0.0.0 '):
                continue
            _, domain = line.split(None, 1)
            domains.add(domain.lower())

    output_domains = set()

    for d in domains:
        if d.startswith('www.'):
            no_www = d[4:]
            output_domains.add(no_www)
            output_domains.add(d)
        else:
            output_domains.add(d)
            output_domains.add('www.' + d)

    with open(output_file, 'w') as f:
        for domain in sorted(output_domains):  # ORDINAMENTO ALFABETICO
            f.write(f"0.0.0.0 {domain}\n")

if __name__ == "__main__":
    input_file = "pihole_domains.txt"
    output_file = "pihole_domains_www.txt"
    duplicate_www(input_file, output_file)
    print(f"Created {output_file} with domains duplicated and sorted alphabetically.")
