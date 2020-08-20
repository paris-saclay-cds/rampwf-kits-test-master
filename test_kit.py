import os
from subprocess import call

from rampwf.utils import assert_submission, assert_notebook

os.environ['RAMP_TEST_MODE'] = '1'


def test_submission_kit():
    kit = os.environ['RAMP_KIT']
    kit_dir = os.getcwd()

    # download the data if necessary
    filename_download = os.path.join(kit_dir, 'download_data.py')
    if os.path.isfile(filename_download):
        call("python {}".format(filename_download), shell=True)
    # testing assert_notebook and optional switches on titanic
    if kit == 'titanic':
        assert_notebook(ramp_kit_dir=kit_dir)
        assert_submission(
            ramp_kit_dir=kit_dir, ramp_data_dir=kit_dir,
            submission='starting_kit', is_pickle=True,
            save_output=True, retrain=True)
    else:
        assert_submission(
            ramp_kit_dir=kit_dir, ramp_data_dir=kit_dir,
            submission='starting_kit')
