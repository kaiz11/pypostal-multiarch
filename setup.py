import argparse
import os
import subprocess
import sys
import platform

from setuptools import setup, Extension, Command, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install
from distutils.errors import DistutilsArgError

this_dir = os.path.realpath(os.path.dirname(__file__))

def find_libpostal():
    """Find libpostal library and include paths"""
    include_dirs = []
    library_dirs = []
    
    # Check environment variables first
    if os.environ.get('LIBPOSTAL_INC'):
        include_dirs.append(os.environ['LIBPOSTAL_INC'])
    if os.environ.get('LIBPOSTAL_LIB'):
        library_dirs.append(os.environ['LIBPOSTAL_LIB'])
    
    # Try pkg-config
    if not include_dirs or not library_dirs:
        try:
            import pkgconfig
            if pkgconfig.exists('libpostal'):
                flags = pkgconfig.parse('libpostal')
                include_dirs.extend(flags.get('include_dirs', []))
                library_dirs.extend(flags.get('library_dirs', []))
        except (ImportError, OSError, KeyError):
            pass
    
    # Fallback to common system paths
    if not include_dirs or not library_dirs:
        common_prefixes = ['/usr/local', '/usr', '/opt/homebrew', '/opt/local']
        
        for prefix in common_prefixes:
            inc_path = os.path.join(prefix, 'include')
            lib_path = os.path.join(prefix, 'lib')
            
            if os.path.exists(os.path.join(inc_path, 'libpostal', 'libpostal.h')):
                if inc_path not in include_dirs:
                    include_dirs.append(inc_path)
            
            if os.path.exists(lib_path):
                try:
                    if any(f.startswith('libpostal') for f in os.listdir(lib_path)):
                        if lib_path not in library_dirs:
                            library_dirs.append(lib_path)
                except OSError:
                    pass
    
    # Default fallback
    if not include_dirs:
        include_dirs = ['/usr/local/include']
    if not library_dirs:
        library_dirs = ['/usr/local/lib']
    
    print(f"Using include_dirs: {include_dirs}")
    print(f"Using library_dirs: {library_dirs}")
    
    return include_dirs, library_dirs


VERSION = '1.0.2'


def main():
    # Find libpostal paths dynamically
    include_dirs, library_dirs = find_libpostal()
    
    # Common extension arguments
    common_args = {
        'libraries': ['postal'],
        'include_dirs': include_dirs,
        'library_dirs': library_dirs,
        'extra_compile_args': ['-std=c99'],
    }
    
    # Platform-specific optimizations (no need for explicit arch flag on macOS)
    
    setup(
        name='pypostal-multiarch',
        version=VERSION,
        install_requires=[
            'six',
        ],
        setup_requires=[
            'nose>=1.0',
            'pkgconfig',
        ],
        ext_modules=[
            Extension('postal._expand',
                      sources=['postal/pyexpand.c', 'postal/pyutils.c'],
                      **common_args),
            Extension('postal._parser',
                      sources=['postal/pyparser.c', 'postal/pyutils.c'],
                      **common_args),
            Extension('postal._token_types',
                      sources=['postal/pytokentypes.c'],
                      **common_args),
            Extension('postal._tokenize',
                      sources=['postal/pytokenize.c', 'postal/pyutils.c'],
                      **common_args),
            Extension('postal._normalize',
                      sources=['postal/pynormalize.c', 'postal/pyutils.c'],
                      **common_args),
            Extension('postal._near_dupe',
                      sources=['postal/pyneardupe.c', 'postal/pyutils.c'],
                      **common_args),
            Extension('postal._dedupe',
                      sources=['postal/pydedupe.c', 'postal/pyutils.c'],
                      **common_args),
        ],
        packages=find_packages(),
        package_data={
            'postal': ['*.h', '*.pyi', 'py.typed'],
            'postal.utils': ['*.pyi']
        },
        zip_safe=False,
        url='https://github.com/kaiz11/pypostal-multiarch',
        download_url='https://github.com/kaiz11/pypostal-multiarch/tarball/{}'.format(VERSION),
        description='Python bindings to libpostal for fast international address parsing/normalization',
        license='MIT License',
        maintainer='kaiz11',
        maintainer_email='kaiz11@users.noreply.github.com',
        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: C',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX :: Linux',
            'Operating System :: Microsoft :: Windows',
            'Topic :: Text Processing :: Linguistic',
            'Topic :: Scientific/Engineering :: GIS',
            'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        python_requires='>=3.8',
    )


if __name__ == '__main__':
    main()
