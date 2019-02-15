from setuptools import setup

setup(
    name="tv2",
    version="0.2.3",
    author="Sean Hammond, Vincent Perricone, Madison Scott-Clary",
    author_email='makyo+tv2@drab-makyo.com',
    packages=["tv2"],
    scripts=["bin/tv2"],
    url="http://github.com/makyo/tv2/",
    license="GNU General Public License, Version 3",
    description="A fast note-taking app for the UNIX terminal",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "urwid==2.0.1",
        "chardet==3.0.4",
        "six==1.12.0",
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],
    )
