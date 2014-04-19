from distutils.core import setup

try:
    import concurrent.futures
except ImportError:
    install_requires = ['futures==2.1.6'], # python 2 support
else:
    install_requires = []

from jumble import __version__

setup(name='jumble',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Run something in parallel, and generate results in the order they finish.',
      url='https://github.com/tlevine/jumble',
      packages=['jumble'],
      install_requires = install_requires,
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
