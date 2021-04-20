import setuptools
from pathlib import Path

HERE = Path(__file__).parent.resolve()

long_description = (HERE / "README.md").read_text(errors="ignore")

setup_args = dict(name='notbook-snapshot',
                  version='0.0.1',
                  description='A JupyterLab extension for version control',
                  long_description=long_description,
                  long_description_content_type="text/markdown",
                  url='',
                  author='passer',
                  author_mail='whzhoua@gmail.com',
                  python_requires=">=3.6,<4",
                  license="BSD-3-Clause",
                  platforms="Linux, Mac OS X, Windows",
                  keywords=["Jupyter", "JupyterLab", "JupyterLab3", "Version Control"],
                  classifiers=[
                      "Intended Audience :: Developers",
                      "Intended Audience :: Science/Research",
                      "License :: OSI Approved :: BSD License",
                      "Programming Language :: Python",
                      "Programming Language :: Python :: 3",
                      "Programming Language :: Python :: 3.6",
                      "Programming Language :: Python :: 3.7",
                      "Programming Language :: Python :: 3.8",
                      "Programming Language :: Python :: 3.9",
                      "Framework :: Jupyter",
                  ],
                  packages=setuptools.find_packages(),
                  install_require=[],
                  include_package_data=True,
                  entry_points={},
                  zip_safe=False)

if __name__ == '__main__':
    setuptools.setup(**setup_args)
