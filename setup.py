import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter-live-graph", # Replace with your own username
    version="0.1.0",
    author="David E",
    author_email="delliott537@gmail.com",
    description="Create and update graphs live in Jupyter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://dav-ell.github.io/jupyter-live-graph",
    packages=setuptools.find_packages(),
    install_requires=['matplotlib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)