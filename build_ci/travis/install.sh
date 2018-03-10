#!bin/bash

set -e

# get miniconda and install it
wget -q http://repo.continuum.io/miniconda/Miniconda-3.6.0-Linux-x86_64.sh \
     -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b -p /home/travis/miniconda
export PATH=/home/travis/miniconda/bin:$PATH
conda update --yes --quiet conda

# create the proper environment
conda create -n testenv --yes pip python=$TRAVIS_PYTHON_VERSION
source activate testenv

# install the packages required by the testing
pip install -r requirements.txt

# clone the ramp-kit to test
git clone https://github.com/ramp-kits/$RAMP_KIT.git
# install the packages required by the kit
pip install -r $RAMP_KIT/requirements.txt
# upgrade to master the version of ramp-workflow
pip install git+https://github.com/paris-saclay-cds/ramp-workflow
# we need to run the test from the ramp-kit root folder
cd $RAMP_KIT
