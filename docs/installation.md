# Installation Guide for HPC Clusters

## Cluster-Wide Installation

### Requirements
- Python 3.8+ (standard on modern HPC systems)
- psutil library

### Install psutil (if not available system-wide)
```bash
pip install psutil
# or
conda install psutil
```

### Install WedgeBox-HPC
```bash
# Download
wget https://github.com/wedgebox/wedgebox-hpc/releases/download/v1.0.0/wedgebox-hpc

# Copy to shared location
cp wedgebox-hpc /shared/software/bin/

# Make executable
chmod 755 /shared/software/bin/wedgebox-hpc
```

### Test Installation
```bash
wedgebox-hpc
```

## Module Installation (Optional)

If using Lmod:
```lua
-- /shared/modulefiles/wedgebox-hpc/1.0.lua
help([[WedgeBox-HPC GPU Performance Monitor]])
whatis("GPU performance monitoring tool")
prepend_path("PATH", "/shared/software/bin")
```

Users can then:
```bash
module load wedgebox-hpc
wedgebox-hpc
```

## Security Notes

- Read-only monitoring (no system modifications)
- Open source (full code review available)
- No network calls (local-only operation)
- Uses standard APIs (nvidia-smi, /proc filesystem)

## Uninstall
```bash
rm /shared/software/bin/wedgebox-hpc
```