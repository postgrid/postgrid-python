import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setuptools.setup(
    name='postgrid-python',
    version='1.0.7',
    description='A Python Library for the PostGrid Print & Mail API',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/postgrid/postgrid-python',
    author='PostGrid',
    author_email='info@postgrid.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['postgrid'],
    include_package_data=True,
    install_requires=['requests', 'pyjwt'],
    setup_requires=['wheel']
)
