import os.path as osp
from jupyterlab.tests.test_app import run_jest

if __name__ == '__main__':
    run_jest(osp.dirname(osp.realpath(__file__)))
