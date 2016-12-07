Google app engine for python skelton project. [![Build Status](https://travis-ci.org/arvelt/google-appengine-python-skelton.svg?branch=master)](https://travis-ci.org/arvelt/google-appengine-python-skelton)
---
### Go https://skelton-151713.appspot.com/

### Note
- When execute test using gae-sdk (ex. ndb.Model) in local, it is required env `GAE_SDK`. It is necessary to include GAE_SDK to env `PYTHONPATH`. GAE_SDK is google-appengine sdk location path.
- When execute test using gae-sdk (ex. ndb.Model) in travis-ci, It is required google app engine sdk and to set PATH.
- When App engine Service account deploy app from travis-ci, it is required `App Engine Deployer` role and `Editor` role of google cloud strage.
  - See https://cloud.google.com/appengine/docs/python/access-control
- Encrypt credential file with travis cli. See https://docs.travis-ci.com/user/encrypting-files/
