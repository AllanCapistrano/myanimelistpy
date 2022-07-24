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

setup(
    name='myanimelistpy',
    packages=packages,
    version='0.1.0',
    description='A library to use the MyAnimeList API more easily.',
    long_description='./README.md',
    long_description_content_type="text/markdown",
    url='https://github.com/AllanCapistrano/myanimelistpy',
    project_urls={
        "Issue tracker": "https://github.com/AllanCapistrano/myanimelistpy/issues",
      },
    author='AllanCapistrano',
    author_email='asantos@ecomp.uefs.br',
    license='GPL-3.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.10",
        'Topic :: Anime',
        'Topic :: Anime :: MyAnimeList',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
	],
    python_requires='>=3.10.0',
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    test_suite='tests',
)