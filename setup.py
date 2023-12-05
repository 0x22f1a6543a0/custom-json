from setuptools import setup,find_packages

long_description = "README.md"

setup(
    name='smarterjson',
    version='1.0.0',
    description='A smarter than python json', 
    long_description = long_description, 
    url='TODO',
    author='Zhang Jiaqi',
    author_email='2953911716@qq.com',
    license='MIT',
    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    include_package_data = True,
)
