from distutils.core import setup, Extension

module1 = Extension('toPy', include_dirs=['/usr/local/include'], libraries=['bcm2835'], library_dirs=['/usr/local/lib'], sources=['toPy.c'])

setup(name='toPy', version='1.0', ext_modules=[module1])
