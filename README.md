# ASIC-Resistant Interleaving Protocol (ARIP) Benchmark

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Algorithm](https://img.shields.io/badge/Hash-SHA--256%20%7C%20SHA--3%20%7C%20ARIP-orange)
![Consensus](https://img.shields.io/badge/Consensus-Proof--of--Work-green)

Benchmarks baseline SHA-256, baseline SHA-3, and the hybrid ARIP engine across Proof-of-Work mining difficulty levels 1 to 5.

Clone the repository and enter the project folder.

```bash
git clone <repository-url>
cd sha-256vs-3onblockchain
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell.

```bash
venv\Scripts\Activate.ps1
```

Install the dependencies.

```bash
pip install psutil pandas matplotlib
```

Run the benchmark.

```bash
python -m src.main
```

Results are written to the data folder and charts are written to the output folder.
