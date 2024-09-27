from setuptools import setup, find_packages

setup(
    name="dummy_spike_prime_2",
    version="0.1",
    packages=find_packages(),
    description="Dummy SPIKE Prime (v2) library for syntax highlighting in VSCode",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Maximilian Kotz",
    author_email="kotzmax@gmail.com",
    url="https://github.com/yourusername/dummy_spike_prime",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
