pypostal-multiarch
------------------

[![Build Status](https://github.com/kaiz11/pypostal-multiarch/actions/workflows/build.yml/badge.svg)](https://github.com/kaiz11/pypostal-multiarch/actions/workflows/build.yml) [![PyPI version](https://img.shields.io/pypi/v/pypostal-multiarch.svg)](https://pypi.python.org/pypi/pypostal-multiarch) [![License](https://img.shields.io/github/license/kaiz11/pypostal-multiarch.svg)](https://github.com/kaiz11/pypostal-multiarch/blob/master/LICENSE)

Python bindings to https://github.com/openvenues/libpostal with **multi-architecture support** including ARM64/Apple Silicon and **Python 3.8-3.12** compatibility.

This is a modernized fork of the original [pypostal](https://github.com/openvenues/pypostal) with:
- ✅ **Python 3.8-3.12** support (including Python 3.11)
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

```python
from postal.expand import expand_address
expand_address('Quatre vingt douze Ave des Champs-Élysées')

from postal.parser import parse_address
parse_address('The Book Club 100-106 Leonard St, Shoreditch, London, Greater London, EC2A 4RH, United Kingdom')
```

Installation
------------
*Based on installation instructions from the original pypostal project*

Before using the Python bindings, you must install the libpostal C library. Make sure you have the following prerequisites:

**On Ubuntu/Debian**
```
sudo apt-get install curl autoconf automake libtool python-dev pkg-config
```
**On CentOS/RHEL**
```
sudo yum install curl autoconf automake libtool python-devel pkgconfig
```
**On Mac OSX**
```
brew install curl autoconf automake libtool pkg-config
```

**Installing libpostal**

If you're using an M1 Mac, add --disable-sse2 to the ./configure command. This will result in poorer performance but the build will succeed.

```
git clone https://github.com/openvenues/libpostal
cd libpostal
./bootstrap.sh
./configure --datadir=[...some dir with a few GB of space...]
make
sudo make install

# On Linux it's probably a good idea to run
sudo ldconfig
```

To install the Python library, just run:

```
pip install pypostal-multiarch
```

**Note**: Pre-built wheels are available for:
- **Linux**: x86_64, aarch64 (ARM64)
- **macOS**: arm64 (Apple Silicon M1/M2/M3)  
- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12

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

pypostal-multiarch supports **Python 3.8+** (including Python 3.11 and 3.12). These bindings are written using the Python C API and thus support CPython only. Since libpostal is a standalone C library, support for PyPy is still possible with a CFFI wrapper, but is not a goal for this repo.

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
