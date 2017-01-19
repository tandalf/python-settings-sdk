from distutils.core import setup
setup(
  name = 'fetchr-settings',
  packages = ['fetchr-settings'], 
  version = '0.0.1',
  description = 'A client library used for communicating with fetch\'s' +\
      ' settings api.',
  author = 'Timothy Ebiuwhe',
  author_email = 't.ebiuwhe@fetchr.us',
  url = 'https://bitbucket.org/Fetchr/python-settings-sdk/', 
  download_url = 'https://bitbucket.org/Fetchr/python-settings-sdk/get/b511c194bd55.zip', # I'll explain this in a second
  keywords = ['settings', 'api', 'fetchr', 'micro-service'],
  install_requires = ['requests', 'redis']
)