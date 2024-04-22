from pathlib import Path
import os
from setuptools import setup
from setuptools.command.develop import develop


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
            except:  # noqa: E722
                pass

            print(rel_source, "->", target)
            os.symlink(rel_source, target)

        super(DevelopCmd, self).run()


setup(
    cmdclass={
        "develop": DevelopCmd,
    },
)
