from setuptools import find_packages, setup

setup(
    name='nasa',
    version='1.0.0',
    description='Data receiver from Curiosity rover on Mars',
    author='Mykhailo Pazyniuk',
    author_email='mishanya@protonmail.com',
    url='https://github.com/damoklov/nasa',
    download_url='https://github.com/damoklov/nasa.git',
    keywords=['nasa', 'python', 'Mars'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Web Applications :: NASA API",
        ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'folium'
    ],
)
