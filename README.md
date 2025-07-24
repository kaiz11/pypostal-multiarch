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
- **macOS**: x86_64 (Intel), arm64 (Apple Silicon M1/M2)  
- **Windows**: Coming soon (currently install from source)
- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12

**Installing libpostal on Windows**

Install [msys2](http://msys2.org) and launch a shell using the `MSYS2 MingW 64-bit` start menu option, **not** the usual `MSYS2 MSYS` option.
This is important because we don't want our `libpostal.dll` to [link to](https://www.davidegrayson.com/windev/msys2/) `msys-2.0.dll` (Python seems to hang if you load this DLL).

Then:
```
pacman -S autoconf automake curl git make libtool gcc mingw-w64-x86_64-gcc
git clone https://github.com/openvenues/libpostal
cd libpostal
cp -rf windows/* ./
./bootstrap.sh
./configure --datadir=[...some dir with a few GB of space...]
make
make install
mkdir headers && cp -r /usr/include/libpostal/ headers/
```

Now start a command prompt which has access to the Microsoft toolchain. This can be done by e.g. installing the [Windows 10 SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk) and then running the ``x64 Native Tools Command Prompt``.

Assuming your MSYS and Python are installed in some standard locations, you can use this command prompt to build+install the Python library like so:
```
lib.exe /def:libpostal.def /out:postal.lib /machine:x64
pip install postal --global-option=build_ext --global-option="-I[...libpostal checkout...]\headers" --global-option="-L[...libpostal checkout...]"
copy src\.libs\libpostal-1.dll "C:\Python36\Lib\site-packages\postal\libpostal.dll"
```

Compatibility
-------------

pypostal-multiarch supports **Python 3.8+** (including Python 3.11 and 3.12). These bindings are written using the Python C API and thus support CPython only. Since libpostal is a standalone C library, support for PyPy is still possible with a CFFI wrapper, but is not a goal for this repo.

**Architecture Support:**
- **Linux**: x86_64, aarch64 (ARM64)
- **macOS**: x86_64 (Intel), arm64 (Apple Silicon)
- **Windows**: Coming soon (currently source installation only)

Tests
-----

Make sure you have [nose](https://nose.readthedocs.org/en/latest/) installed, then run:

```
python setup.py build_ext --inplace
nosetests postal/tests
```

The ```build_ext --inplace``` business is needed so the C extensions build in the source checkout directory and are accessible/importable by the Python modules.
