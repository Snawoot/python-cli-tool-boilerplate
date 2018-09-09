from setuptools import setup

setup(name='clitoolboilerplate',
      version='0.1',
      description='Just another TCP/UDP to Websocket wrapper',
      url='https://github.com/Snawoot/python-cli-tool-boilerplate',
      author='Vladislav Yarmak',
      author_email='vladislav-ex-src@vm-0.com',
      license='MIT',
      packages=['clitoolboilerplate'],
      setup_requires=[
          'wheel',
      ],
      install_requires=[
      ],
      scripts=[
          'cli-tool',
      ],
      zip_safe=True)
