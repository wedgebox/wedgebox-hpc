# Usage Guide

## Basic Usage
```bash
wedgebox-hpc
```

Generates:
1. Console summary (printed to screen)
2. `wedgebox-report-[timestamp].json` (detailed data)

## Example Output
```
======================================================================
WedgeBox-HPC v1.0.0 - GPU Performance Snapshot
======================================================================

Node: compute-node-42
Time: 2024-03-10T15:30:45Z

──────────────────────────────────────────────────────────────────────
GPUs Detected: 8
──────────────────────────────────────────────────────────────────────

GPU 0: NVIDIA A100-SXM4-80GB
  Vendor:       nvidia
  Utilization:  87.0%
  Memory:       52428 MB / 81920 MB (64.0%)
  Temperature:  72°C
  Power:        350.5W

[... 7 more GPUs ...]

──────────────────────────────────────────────────────────────────────
GPU Processes: 3
──────────────────────────────────────────────────────────────────────

PID 12345: python3
  User:       alice
  GPU Memory: 8192 MB
  CPU:        45.2%

[... more processes ...]
```

## Use Cases

### Debug Slow Training
```bash
# Run during training
wedgebox-hpc

# Check if GPU is fully utilized
# Look for: utilization_gpu_percent < 80%
```

### Monitor Multi-GPU Jobs
```bash
# Check GPU memory distribution
# Look for: uneven memory_used_mb across GPUs
```

### Profile Memory Usage
```bash
# Identify memory-hungry processes
# Look for: high gpu_memory_mb per process
```

## JSON Report Structure
```json
{
  "version": "1.0.0",
  "timestamp": "2024-03-10T15:30:45Z",
  "gpus": [
    {
      "gpu_id": 0,
      "name": "NVIDIA A100",
      "utilization_gpu_percent": 87.0,
      ...
    }
  ],
  "gpu_processes": [
    {
      "pid": 12345,
      "name": "python3",
      "gpu_memory_mb": 8192,
      ...
    }
  ]
}
```