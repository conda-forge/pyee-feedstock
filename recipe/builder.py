import os, sys, subprocess, re

SRC_DIR = os.environ["SRC_DIR"]

SETUP_PY = os.path.join(SRC_DIR, "setup.py")


print("reading setup.py...")
with open(SETUP_PY) as fpt:
    setup_py_content = fpt.read()


print("adding version metadata...")
setup_py_content = setup_py_content.replace(
    r"vcversioner={},",
    "version='{}', # version added by conda-forge".format(
        os.environ["PKG_VERSION"]
    )
)


print("clobbering setup_requires...")
setup_py_content = re.sub(
    r'setup_requires=\[.*?\],',
    '# setup_requires removed by conda-forge',
    setup_py_content,
    flags=re.M | re.S
)


print("writing setup.py...")
with open(SETUP_PY, "w") as fpt:
    fpt.write(setup_py_content)


print("installing with pip...")
subprocess.check_call(
    [sys.executable, "-m", "pip", "install", ".", "--no-deps", "-vv"],
    cwd=SRC_DIR
)
