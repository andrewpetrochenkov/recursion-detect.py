import setuptools

setuptools.setup(
    name='recursion-detect',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
