from setuptools import setup,find_packages

install_requires=[  # Specify any required dependencies
        'matplotlib',
    ]

setup(
    name='vision',
    version='1.0',
    author='Anupam',
    description='Visualize code',
    packages=find_packages(),
    # package_dir={"": "src"},
    install_requires=install_requires,
)