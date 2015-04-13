import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = (
    'Arche',
    'pyramid',
    'fanstatic',
    )

setup(name='voteit_site',
      version='0.1dev',
      description='voteit_site',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Development Status :: 3 - Alpha",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='VoteIT development team',
      author_email='robin@betahaus.net',
      url='http://voteit.se',
      keywords='web pylons pyramid voteit',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="voteit_site",
      entry_points="""\
      [fanstatic.libraries]
      voteit_site = voteit_site.fanstatic_lib:voteit_site_lib
      """)
