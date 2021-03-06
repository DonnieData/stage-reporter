import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='stage_reporter',                           # should match the package folder
    packages=['stage_reporter'],                     # should match the package folder
    version='0.2.0',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='Testing installation of Package',
    long_description=long_description,              
    long_description_content_type="text/markdown",  
    author='Donnell Jackson',
    author_email='donnie.developer@gmail.com',
    url='https://github.com/DonnieData/stage-reporter', 
    project_urls = {                                # Optional
        "Bug Tracker": "https://github.com/DonnieData/stage-reporter/issues"
    },
    install_requires=['requests'],                  # list all packages that your package uses
    keywords=["pypi", "stage_reporter", "script report", "tracking"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/DonnieData/stage-reporter/archive/refs/tags/v.0.2.0.tar.gz",
)
