# Testing repo for ramp kits master branch

[![Build Status](https://travis-ci.org/paris-saclay-cds/rampwf-kits-test-master.svg?branch=master)](https://travis-ci.org/paris-saclay-cds/rampwf-kits-test-master)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)


## Generate travis build

New ramp kits can be added to the `ramp-kits` GitHub organization. To simplify
the update of the `.travis.yml`, you can execute directly the file
`configure_travis.py`:

```
python configure_travis.yml
```

It will generate a new `travis.yml` containing all the ramp-kits. It is also
possible to update the python version by edition `configure_travis.yml`. Once
that you generated a new `.travis.yml`, do not forget to commit the change.


