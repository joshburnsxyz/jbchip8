from . import constants 

def log(msg):
  if constants.LOGGING:
    print(msg)