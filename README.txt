Custom scaffolds for the Pyramid Web Framework
The scaffolds both deploy Foundation CSS and a compass build script.

* ww3_pymongo   - Mongo, url dispatch, mako.

Usage
=====

* pip install wwitzel-scaffolds
* pcreate -t ww3_pymongo demo
* cd demo/
* python setup.py develop

At this point you need to edit your development.ini to point to your mongo installation.

* demo_initialize_db development.ini
* pserve development.ini

This will set you up with a basic demo application with two user accounts.

