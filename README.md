# WedgeBox-HPC

Simple GPU Performance Monitoring for HPC Clusters

## Overview

WedgeBox-HPC provides detailed GPU telemetry for debugging and optimizing
machine learning workloads on HPC infrastructure.

**Features:**
- Multi-vendor GPU support (NVIDIA, AMD)
- Process-level GPU resource tracking
- Zero-configuration monitoring
- Human-readable console output + detailed JSON reports

## Quick Start
```bash
# Download
wget https://raw.githubusercontent.com/wedgebox/wedgebox-hpc/main/wedgebox-hpc
chmod +x wedgebox-hpc

# Run
./wedgebox-hpc
```

## Requirements

- Python 3.8+
- psutil (`pip install psutil --user`)
- GPU drivers (nvidia-smi for NVIDIA, rocm-smi for AMD)

## For HPC Administrators

See [docs/installation.md](docs/installation.md) for cluster-wide deployment instructions.

## Output

Generates:
- Console summary (human-readable)
- `wedgebox-report-[timestamp].json` (machine-readable)

## Use Cases

- Debug slow training jobs
- Monitor GPU utilization
- Profile memory usage
- Identify resource bottlenecks
- Track multi-GPU workload distribution

## License

MIT License - See LICENSE file