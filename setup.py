from setuptools import setup, find_packages

version = '0.1'

setup(
    name='django-herodotos',
    version=version,
    description="Record custom events for your django models.",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django',
    author='Baptiste Mispelon',
    author_email='bmispelon@gmail.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
