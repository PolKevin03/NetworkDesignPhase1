# Network Design Project – Team ____

<!-- Optional: add badges if you want -->
<!-- ![language](https://img.shields.io/badge/language-python-blue) -->

## Overview
This repository implements a UDP/TCP-based file transfer protocol across **6 phases**, progressively adding reliability 
mechanisms and performance evaluation.

## Team
| Name | Email | Primary responsibility |
|Kevin Pol|Kevin_Pol@student.uml.edu|Echo/message back, file transfer, testing and fixing|
|  |  |  |
|  |  |  |
|  |  |  |

## Demo Video (submission)
- **Private YouTube link:** *(submit via Blackboard)*   youtube.com/watch?v=YZIItVEGag8&feature=youtu.be
- **Timestamped outline:** *(mm:ss → scenario)*
-00:00-00:19 echo demo
-00:23-00:59 file transfer
---

## Repository Structure (required)
Your repo must match this layout (minimum):

```
src/        # sender, receiver, protocol utilities
scripts/    # experiment runner, plotting utilities
docs/       # design documents and diagrams
results/    # CSV + plots generated from experiments
README.md
```

Optional (recommended):
- `tests/`
- `data/`
- `requirements.txt` (Python)

---

## Requirements
- Language/runtime: (Python 3.x)
- OS tested: (macOS / Windows / Linux)
- Dependencies:
  - Python: `pip install -r requirements.txt`

---

## Standard CLI Interface (required)
Your program must support these standardized flags so the TA can run and grade consistently.

### Receiver (required flags)
- `--port <int>`: UDP port to bind
- `--out <path>`: output file path to write received bytes
- `--seed <int>`: RNG seed (default: 0)
- `--log-level <debug|info|warning|error>` (default: info)

### Sender (required flags)
- `--host <ip/hostname>`: receiver host
- `--port <int>`: receiver port
- `--file <path>`: input file to send
- `--seed <int>`: RNG seed (default: 0)
- `--log-level <debug|info|warning|error>` (default: info)

### Injection flags (if required by phase)
- `--data-error-rate <float 0..1>` (default: 0)
- `--ack-error-rate <float 0..1>` (default: 0)
- `--data-loss-rate <float 0..1>` (default: 0)
- `--ack-loss-rate <float 0..1>` (default: 0)

### Timing / windowing flags (if required by phase)
- `--timeout-ms <int>` (default: 40)
- `--window-size <int>` (default: 10)

**Notes**
- “Rates” are probabilities per packet/ACK.
- Timing experiments must disable verbose logging (use `--log-level warning` or `error`).

---

## Quick Start (Run Locally)
### Start Receiver
```bash
python src/receiver.py --port 9000 --out results/received.bin --seed 0
```

### Run Sender
```bash
python src/sender.py --host 127.0.0.1 --port 9000 --file data/sample.jpg --seed 0 #used localhost
```

---

## Required Demo Scenarios (Current Phase)
Provide the exact commands used to demonstrate each required scenario.

### Scenario 1: ____Echo/Repeated Message______
Receiver:
```bash
python src/server_echo.py
```
Sender:
```bash
python src/client_echo.py
```
Expected behavior:
- Prints hello back

### Scenario 2: ____Save and file transfer copy______
Receiver:
```bash
python src/server_file.py
Sender:
```bash
python src/client_file.py inputfile/bmp_24.bmp
Expected behavior:
- Saves and make file with original image
---

## Figures / Plots (if required by phase) N/A
### Reproduce experiment runs
Your repo must include a script that can reproduce required sweeps and output CSV.

Example:
```bash
python scripts/run_experiments.py --phase 4 --out results/phase4.csv
```

### Generate plots
Example:
```bash
python scripts/plot_results.py --in results/phase4.csv --out results/phase4.png
```

### Results files
- `results/phaseX.csv`
- `results/phaseX.png`

---

## Known Issues / Limitations
List any limitations honestly.
- The inditation issue was issue bad since I was used to c
- The bmp file would create a new file and match but the file outside the result folder.
- file path was not found due to incorrect input in the terminal where I had to use a path and it worked
- tried using docx file but it didn't work from printing a blank document then switched to bmp and it worked.
---

## Academic Integrity / External Tools
Debugging tools (IDE debugger, logging) and LLMs may be used for learning and troubleshooting. Final implementation decisions and understanding are our own.
Phase 1 slides