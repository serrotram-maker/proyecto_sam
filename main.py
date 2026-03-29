#!/usr/bin/env python3
import sys
from rich.console import Console

console = Console()

def analyze_file(filename):
    total = 0
    mapq60 = 0

    with open(filename) as f:
        for line in f:
            if line.startswith("@"):
                continue
            fields = line.strip().split("\t")
            total += 1

            mapq = int(fields[4])
            if mapq == 60:
                mapq60 += 1

    return total, mapq60

filename = sys.argv[1]

total, mapq60 = analyze_file(filename)

percentage = (mapq60 / total) * 100

console.print("Total de lecturas alineadas:", total)
console.print("Lecturas con MAPQ = 60:", mapq60)
console.print("Porcentaje:", percentage,"%")

