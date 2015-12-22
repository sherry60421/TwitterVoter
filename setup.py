from distutils.core import setup
import tweepy
import py2exe
import sys
import imp


sys.argv.append('py2exe')

setup(
    windows = [{"script": "TwitterVoter.py"}],
    options = {"py2exe":{"includes": ["tweepy"]}}
    )

