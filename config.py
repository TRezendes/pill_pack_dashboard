import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv('.env')

class Config(object):
	PATH_TO_WATCH = os.environ.get('PATH_TO_WATCH')
