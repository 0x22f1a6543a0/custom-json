from setuptools import setup, find_packages

long_description = ""

setup(
    name='custom-json',
    version='0.0.5',
    description='batter than python json',
    long_description = long_description,
    url='',
    author='Zhang Jiaqi',
    author_email='TODO',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='TODO',
    install_requires = [
      "TODO",
    ],
    packages=find_packages(),
    include_package_data = True, #
    entry_points={
        'console_scripts':[
            'cmdname = cmdtoolfilepath:methodname'
        ]
      },
)