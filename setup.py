from setuptools import setup, find_packages

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setup(name='scraperx',
      packages=find_packages(),
      version='0.4.6',
      python_requires='>=3.6.0',
      license="MIT",
      description="ScraperX SDK",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="Eddy Hintze",
      author_email="eddy@hintze.co",
      url="https://github.com/ScraperX/scraperx",
      install_requires=['pyyaml',
                        'parsel',
                        'requests',
                        'boto3',
                        'deepdiff',
                        'smart_open>=1.8.4',
                        ],
      )
