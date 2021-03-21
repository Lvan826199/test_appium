import os
import shlex
import signal
import subprocess

import pytest

#conftest.py文件就相当于是pytest的配置文件需要配合fixture使用
# 在执行别的test_files文件的时候，会自动使用这个文件

#yield表示在未执行完全部的时候，不会调用他后面的内容
# 他后面的内容可以理解成异常处理中的finally，在最后才会执行的步骤

@pytest.fixture(scope='class',autouse=True)
def record():
    cmd=shlex.split("scrcpy --record tmp.mp4")
    p=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid,signal.CTRL_C_EVENT)
