from pathlib import Path
import sys
import os
from setuptools import setup
from setuptools.command.develop import develop
import contextlib

pjoin = os.path.join


# these are based on jupyter_core.paths
def jupyter_config_dir():
    """Get the Jupyter config directory for this platform and user.

    Returns JUPYTER_CONFIG_DIR if defined, else ~/.jupyter
    """

    env = os.environ
    home_dir = get_home_dir()

    if env.get("JUPYTER_NO_CONFIG"):
        return _mkdtemp_once("jupyter-clean-cfg")

    if env.get("JUPYTER_CONFIG_DIR"):
        return env["JUPYTER_CONFIG_DIR"]

    return pjoin(home_dir, ".jupyter")


class DevelopCmd(develop):
    prefix_targets = [
        ("nbconvert/templates", "sepal-ui-base"),
        ("voila/templates", "sepal-ui-base"),
    ]

    def run(self):

        target_dir = Path().home() / ".local/share/jupyter"

        for prefix_target, name in self.prefix_targets:
            source = os.path.join("share", "jupyter", prefix_target, name)
            target = os.path.join(target_dir, prefix_target, name)
            target_subdir = os.path.dirname(target)
            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)
            rel_source = os.path.relpath(
                os.path.abspath(source), os.path.abspath(target_subdir)
            )
            try:
                os.remove(target)
            except:
                pass
            print(rel_source, "->", target)
            os.symlink(rel_source, target)

        super(DevelopCmd, self).run()


# WARNING: all files generates during setup.py will not end up in the source distribution
data_files = []
# Add all the templates
for dirpath, dirnames, filenames in os.walk("share/jupyter/"):
    if filenames:
        data_files.append(
            (dirpath, [os.path.join(dirpath, filename) for filename in filenames])
        )


setup(
    name="voila-sepal-ui",
    version="0.0.0",
    description="A sepal-ui template for Voila",
    data_files=data_files,
    install_requires=["voila>=0.2.0,<0.5"],
    include_package_data=True,
    author="Daniel Guerrero Machado",
    author_email="dfgm2006@gmail.com",
    url="https://github.com/dfguerrerom/voila-sepal-ui",
    keywords=["ipython", "jupyter", "widgets", "voila"],
    cmdclass={
        "develop": DevelopCmd,
    },
)
