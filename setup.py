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
    'pyramid',
    'sqlalchemy',
    'pymongo',
    'mako',
    'Paste',
    'PasteDeploy',
    'PasteScript',
    ]

setup(name='wwitzel_scaffolds',
      version='0.2',
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
        wwitzel_routesalchemy=wwitzel_scaffolds:WRoutesAlchemyTemplate
        wwitzel_routespymongo=wwitzel_scaffolds:WRoutesMongoTemplate
        [paste.paster_create_template]
        wwitzel_routesalchemy=wwitzel_scaffolds:WRoutesAlchemyTemplate
        wwitzel_routespymongo=wwitzel_scaffolds:WRoutesMongoTemplate
      """
      )
