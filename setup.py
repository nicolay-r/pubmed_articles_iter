from setuptools import (
    setup,
    find_packages,
)


def get_requirements(filenames):
    r_total = []
    for filename in filenames:
        with open(filename) as f:
            r_local = f.read().splitlines()
            r_total.extend(r_local)
    return r_total


setup(
    name='pubmed_articles_iter',
    version='0.0.1',
    python_requires=">=3.9",
    description='Non-official JSON-based articles info iterator from fetched XML snapshot',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nicolay-r/pubmed_articles_iter',
    author='Nicolay Rusnachenko',
    author_email='rusnicolay@gmail.com',
    license='MIT License',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=get_requirements([
        'dependencies.txt']),
    packages=find_packages(),
)