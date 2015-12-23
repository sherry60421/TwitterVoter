from distutils.core import setup
import py2exe, sys
sys.argv.append('py2exe')
includes = ["tweepy"]

setup(
    console = [{"script": "C:\TwitterVoter.py"}],
    zipfile = None,
    options = {
        "py2exe":{
            "includes": includes
        }
    }
)

