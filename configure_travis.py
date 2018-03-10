"""File which generate automatically the .travis.yml configuration file."""

from io import BytesIO

from ruamel import yaml
import json
import pycurl

query = pycurl.Curl()
data = BytesIO()

query.setopt(query.URL, 'https://api.github.com/orgs/ramp-kits/repos')
query.setopt(query.WRITEFUNCTION, data.write)
query.perform()
query.close()

info_repos = json.loads(data.getvalue())

# repositories to be excluded
exclude_repos = ['pollenating_insects',
                 'pollenating_insects_2',
                 'pollenating_insects_3',
                 'pollenating_insects_3_simplified']

# repositories to test excluding the above repositories
name_repos = ['RAMP_KIT="{}"'.format(repo['name'])
              for repo in info_repos
              if repo['name'] not in exclude_repos]

# repositories allowed to fail
failing_repos = ['solar_wind']
allow_failure_repos = [{'env': 'RAMP_KIT="{}"'.format(repo)}
                       for repo in failing_repos]

travis_yml = {
    'language': 'python',
    'dist': 'trusty',
    'python': ['2.7', '3.6'],
    'env': {'matrix': name_repos},
    'matrix': {'allow_failures': allow_failure_repos},
    'install': 'source build_ci/travis/install.sh',
    'script': 'pytest -s -v ../test_kit.py'
}

with open('.travis.yml', 'w') as outfile:
    yaml.round_trip_dump(travis_yml, outfile,
                         default_flow_style=False)
