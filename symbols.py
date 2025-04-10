with open("sf-symbols.csv", "r") as f:
    for line in f:
        [cp, name] = line.strip().split(',')
        print(f"<p data-name={name}>{cp}</p>")
