from setuptools import find_packages, setup

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup_requirements = []
with open('setup-requirements.txt') as f:
  setup_requirements = f.read().splitlines()

test_requirements = []
with open('test-requirements.txt') as f:
  test_requirements = f.read().splitlines()

packages = [
    "myanimelistpy",
    "myanimelistpy.enums",
    "myanimelistpy.models",
    "myanimelistpy.services"
]

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(
    name='myanimelistpy',
    packages=packages,
    version='0.1.4',
    description='A library to use the MyAnimeList API more easily.',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/AllanCapistrano/myanimelistpy',
    project_urls={
        "Documentation": "https://myanimelistpy.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/AllanCapistrano/myanimelistpy/issues",
      },
    author='AllanCapistrano',
    author_email='asantos@ecomp.uefs.br',
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
		"Programming Language :: Python :: 3.10",
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
	],
    python_requires='>=3.10.0',
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    test_suite='tests',
)