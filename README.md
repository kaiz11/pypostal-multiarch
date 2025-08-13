pypostal-multiarch
------------------

[![Test, Build and Publish](https://github.com/kaiz11/pypostal-multiarch/actions/workflows/build.yml/badge.svg)](https://github.com/kaiz11/pypostal-multiarch/actions/workflows/build.yml) [![PyPI version](https://img.shields.io/pypi/v/pypostal-multiarch.svg)](https://pypi.python.org/pypi/pypostal-multiarch) [![PyPI Downloads](https://pepy.tech/badge/pypostal-multiarch/month)](https://pepy.tech/project/pypostal-multiarch) [![Libraries.io dependency status](https://img.shields.io/librariesio/release/pypi/pypostal-multiarch.svg)](https://libraries.io/pypi/pypostal-multiarch) [![License](https://img.shields.io/github/license/kaiz11/pypostal-multiarch.svg)](https://github.com/kaiz11/pypostal-multiarch/blob/main/LICENSE)

Python bindings to https://github.com/openvenues/libpostal with **multi-architecture support** including ARM64/Apple Silicon and **Python 3.8-3.13** compatibility.

This is a modernized fork of the original [pypostal](https://github.com/openvenues/pypostal) with:
- ✅ **Python 3.8-3.13** support
- ✅ **Multi-architecture wheels** (x86_64, ARM64/aarch64)  
- ✅ **Apple Silicon (M1/M2) native support**
- ✅ **Automated CI/CD** with GitHub Actions
- ✅ **Modern packaging** with pyproject.toml
- ✅ **Comprehensive mypy type support**

## Attribution

This project is a modernized fork of [pypostal](https://github.com/openvenues/pypostal) by OpenVenues. The original project provides the core functionality and much of the installation documentation found in this README. We've extended it with modern Python support, multi-architecture compatibility, and comprehensive type hints.

**Original project**: https://github.com/openvenues/pypostal  
**Original authors**: OpenVenues team  
**License**: MIT (same as original)

Usage
-----
**⚠️ Note**: These examples require that libpostal is already installed on your system. See the [Installation](#installation) section below.

**✅ Verified**: These examples are automatically tested in our CI on every push to ensure they actually work. Wheel building and publishing only happens on version tags after examples pass.

### Address Expansion
Normalize and expand addresses into multiple possible variants:

```python
from postal.expand import expand_address

# Basic expansion
expansions = expand_address('781 Franklin Ave Crown Hts Brooklyn NY')
print(expansions)
# Output: ['781 franklin avenue crown heights brooklyn new york', 
#          '781 franklin avenue crown heights brooklyn ny', ...]

# With language specification  
expansions = expand_address('Quatre vingt douze Ave des Champs-Élysées', languages=['fr'])
print(expansions)
# Output: ['92 avenue des champs elysees', '92 ave des champs elysees', ...]
```

### Address Parsing
Parse addresses into labeled components:

```python
from postal.parser import parse_address

# Parse an address
components = parse_address('The Book Club 100-106 Leonard St, Shoreditch, London, EC2A 4RH, UK')
for component, label in components:
    print(f"{label}: {component}")
# Output:
# house_number: 100-106
# road: leonard st
# suburb: shoreditch  
# city: london
# postcode: ec2a 4rh
# country: uk
```

### Text Normalization
Normalize strings and tokens:

```python
from postal.normalize import normalize_string, normalized_tokens

# String normalization
normalized = normalize_string('St.-Barthélemy')
print(normalized)  # Output: 'saint barthelemy'

# Token normalization with types
tokens = normalized_tokens('123 Main St.')
for token, token_type in tokens:
    print(f"{token} ({token_type})")
# Output:
# 123 (NUMERIC)
# main (WORD)  
# saint (WORD)
```

### Text Tokenization
Split text into tokens with classification:

```python
from postal.tokenize import tokenize

# Tokenize text
tokens = tokenize('123 Main St.')
for token, token_type in tokens:
    print(f"{token} ({token_type})")
# Output:
# 123 (NUMERIC)
# Main (WORD)
# St (ABBREVIATION)
# . (PERIOD)
```

### Address Deduplication
Check if addresses are duplicates:

```python
from postal.dedupe import is_street_duplicate, duplicate_status

# Check if two street names are duplicates
status = is_street_duplicate('Main St', 'Main Street')
print(status)  # Output: EXACT_DUPLICATE

if status == duplicate_status.EXACT_DUPLICATE:
    print("These are the same street")
    # Output: These are the same street
```

### Near-Duplicate Hashing
Generate hashes for similarity detection:

```python
from postal.near_dupe import near_dupe_hashes

# Generate hashes for address similarity
labels = ['house_number', 'road', 'city', 'postcode']
values = ['123', 'Main St', 'New York', '10001']
hashes = near_dupe_hashes(labels, values, address_only_keys=True)
print(f"Generated {len(hashes)} similarity hashes")
# Output: Generated 8 similarity hashes
```

### Type Support
This package includes comprehensive type hints for mypy users:

```python
from typing import List, Tuple
from postal.expand import expand_address
from postal.parser import parse_address
from postal.normalize import normalized_tokens
from postal.tokenize import tokenize
from postal.near_dupe import near_dupe_hashes
from postal.utils.enum import EnumValue

# Type hints work out of the box
expansions: List[str] = expand_address("123 Main St")
components: List[Tuple[str, str]] = parse_address("123 Main St Brooklyn NY")
norm_tokens: List[Tuple[str, EnumValue]] = normalized_tokens("123 Main St")
tokens: List[Tuple[str, EnumValue]] = tokenize("123 Main St")
hashes: List[str] = near_dupe_hashes(['house_number', 'road', 'city', 'postcode'], ['123', 'Main St', 'New York', '10001'], address_only_keys=True)
```

Installation
------------
*Based on installation instructions from the original pypostal project*

### Prerequisites

**⚠️ Important**: Before installing this package, you must first install the libpostal C library. This package won't work without it.

Make sure you have the following prerequisites:

**On Ubuntu/Debian**
```bash
sudo apt-get install -y curl build-essential autoconf automake libtool pkg-config
```

**On CentOS/RHEL**
```bash
sudo yum install curl autoconf automake libtool pkgconfig
```

**On macOS**

Install with one command via MacPorts:
```bash
port install libpostal
```

Or with Homebrew:
```bash
brew install libpostal
```

**Installing libpostal from source**

To compile the C library from source:

```bash
git clone https://github.com/openvenues/libpostal
cd libpostal

# skip if installing for the first time
make distclean

./bootstrap.sh

# Basic configuration (omit --datadir flag to install data in current directory)
./configure --datadir=[...some dir with a few GB of space where a "libpostal" directory exists or can be created/modified...]

# For Intel/AMD processors and the default model
./configure --datadir=[...some dir with a few GB of space where a "libpostal" directory exists or can be created/modified...]

# For Apple Silicon/ARM CPUs and the default model
./configure --datadir=[...some dir with a few GB of space where a "libpostal" directory exists or can be created/modified...] --disable-sse2

# For the improved Senzing model:
./configure --datadir=[...some dir with a few GB of space where a "libpostal" directory exists or can be created/modified...] MODEL=senzing

make -j8
sudo make install

# On Linux it's probably a good idea to run
sudo ldconfig
```

**Using pkg-config**

libpostal has support for pkg-config, so you can use pkg-config to print the flags needed to link your program against it:

```bash
pkg-config --cflags libpostal         # print compiler flags
pkg-config --libs libpostal           # print linker flags
pkg-config --cflags --libs libpostal  # print both
```

For example, if you write a program called app.c, you can compile it like this:
```bash
gcc app.c `pkg-config --cflags --libs libpostal`
```

### Installing the Python Package

Once libpostal is installed, install this Python package:

```bash
pip install pypostal-multiarch
```

**Important Notes:**
- The package installs as `pypostal-multiarch` but imports as `postal` (same as the original)
- The package will install successfully even without libpostal, but **will fail at runtime** when you try to use it
- Always install libpostal first, then install this Python package

**Note**: Pre-built wheels are available for:
- **Linux**: x86_64, aarch64 (ARM64)
- **macOS**: arm64 (Apple Silicon M1/M2/M3)  
- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

Windows and macOS Intel (x86_64) are currently not supported - please install from source if needed.

**Installing from source (Windows/macOS Intel)**

Since pre-built wheels are not available for Windows or macOS Intel, you'll need to build from source. First install libpostal following the instructions above, then:

```bash
# Clone this repository
git clone https://github.com/kaiz11/pypostal-multiarch.git
cd pypostal-multiarch

# Install from source
pip install .
```

For Windows specifically, you may need to use MSYS2 or Visual Studio build tools. See the original [pypostal Windows instructions](https://github.com/openvenues/pypostal#windows) for detailed setup.

Compatibility
-------------

pypostal-multiarch supports **Python 3.8+** (including Python 3.11, 3.12, and 3.13). These bindings are written using the Python C API and thus support CPython only. Since libpostal is a standalone C library, support for PyPy is still possible with a CFFI wrapper, but is not a goal for this repo.

**Architecture Support:**
- **Linux**: x86_64, aarch64 (ARM64) - pre-built wheels available
- **macOS**: arm64 (Apple Silicon) - pre-built wheels available  
- **Windows**: Source installation only
- **macOS Intel (x86_64)**: Source installation only

Tests
-----

To run the tests, first install the package from source:

```bash
# Install in development mode
pip install -e .

# Run tests using pytest (recommended) or unittest
python -m pytest postal/tests/
# OR
python -m unittest discover postal/tests/
```

Note: Tests require libpostal to be installed and may need the libpostal data files for full functionality.

## Troubleshooting

### "cannot import name '_expand' from 'postal'"
This error means libpostal is not installed or not found. Make sure:
1. libpostal is installed system-wide (`sudo make install`)
2. Library paths are updated (`sudo ldconfig` on Linux)
3. You're not in a container or environment where libpostal isn't available

### "ImportError: libpostal.so.1: cannot open shared object file"
This means the libpostal shared library can't be found:
- On Linux: Run `sudo ldconfig` after installing libpostal
- Check that libpostal installed correctly with `ldconfig -p | grep postal`
- Make sure `/usr/local/lib` is in your library path

### Examples don't work  
The usage examples in this README require libpostal to be installed and working. If you're just browsing the documentation, the examples show expected outputs but won't actually run without the full setup.

### Installation is complex
Installing libpostal can be challenging, especially in environments with:
- Multiple Python installations (conda, pyenv, system Python)
- SSL/TLS library conflicts  
- Corporate firewalls blocking downloads
- Limited disk space (libpostal data files are ~1.5GB)
- Permission issues for system-wide installation

If you encounter issues, consider using a clean environment or Docker container for testing.
