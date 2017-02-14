from setuptools import setup
readme = open('README.rst').read()

setup(name='marbaloo_telegram',
      version='0.1.0',
      description='python-telegram-bot support for cherrypy.',
      long_description=readme,
      url='http://github.com/marbaloo/marbaloo_telegram',
      author='Mahdi Ghane.g',
      license='MIT',
      keywords='telegram_bot telegram python_telegram_bot cherrypy marbaloo marbaloo_telegram',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Framework :: CherryPy',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Software Development :: Libraries'
      ],
      install_requires=[
          'cherrypy>=8.1.2',
          'python-telegram-bot>=5.3.0'
      ],
      packages=['marbaloo_telegram'],
      )
