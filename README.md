Google app engine for python skelton project. [![Build Status](https://travis-ci.org/arvelt/google-appengine-python-skelton.svg?branch=master)](https://travis-ci.org/arvelt/google-appengine-python-skelton)
---
### Note
- py.tests required env PYTHONPATH, is application location path.
- py.tests required env GAE_PATH, is google-appengine sdk location path.
- When App engine Service account deploy app from travis-ci, required role `App Engine Deployer` and `Editor` of google cloud strage.
  - See https://cloud.google.com/appengine/docs/python/access-control
- Encrypt credential file with travis cli. See https://docs.travis-ci.com/user/encrypting-files/
