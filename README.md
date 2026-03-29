# project-sam
SAM Project
This project analyzes SAM files using a Python script (`^main.py`) with the [Rich](https://github.com/Textualize/rich) library to produce formatted terminal output. The workflow is automated with [Nextflow](https://www.nextflow.io/) and dependencies are managed with [uv](https://uv.dev/).

# Contents
- `main.py` → Python script that counts total reads, reads with MAPQ = 60, and calculates the percentage.  
- `main.nf` → Nextflow pipeline to run `main.py` on a SAM file.  
- `pyproject.toml` → Dependency management file (uv).  
- `README.md` → Project documentation.

# Requirements

- Python 3  
- [uv](https://uv.dev/)  
- [Nextflow](https://www.nextflow.io/)  
- Python dependencies installed via uv (`rich`)

> Note: uv automatically installs `rich` when you run `uv add rich`.

# Installation

1. Clone the repository:

```bash
git clone https://github.com/serrotram-maker/proyecto_sam.git
cd proyecto-sam
