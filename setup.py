# PyTOUGH setup script
from distutils.core import setup

setup(name='PyTOUGH',
      version='1.3.1',
      description='Python scripting library for TOUGH2 simulation',
      author='Adrian Croucher',
      author_email='a.croucher@auckland.ac.nz',
      url='https://github.com/acroucher/PyTOUGH',
      license='LGPL',
      py_modules=['geometry','IAPWS97','mulgrids','t2data','t2grids','t2incons','t2listing','t2thermo'],
      )
