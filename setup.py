import os
import platform
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires=[
    'pyramid>=1.5a',
    'pymongo>=2.6',
    'pyramid_mako',
    'Paste',
    'PasteDeploy',
    'PasteScript',
    ]

setup(name='wwitzel_scaffolds',
      version='0.5',
      description=('Custom scaffolds for the Pyramid web application '
                   'development framework'),
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: Repoze Public License",
        ],
      keywords='web wsgi pylons pyramid',
      author="Wayne Witzel III",
      author_email="wayne@pieceofpy.com",
      url="https://github.com/wwitzel3/wwitzel_scaffolds",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = install_requires,
      entry_points = """\
        [pyramid.scaffold]
        ww3_pymongo=wwitzel_scaffolds:WRoutesMongoTemplate
        [paste.paster_create_template]
        ww3_pymongo=wwitzel_scaffolds:WRoutesMongoTemplate
      """
      )
