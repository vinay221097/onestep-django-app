from distutils.core import setup
setup(name='onestep-django-app',
      description='installing django web app in one step',
      version='0.1',
      url='https://github.com/vinay221097/onestep-django-app',
      author='Vinay Krishna',
      author_email='vinay221097@gmail.com',
      classifiers=[
          'Programming Language :: Python :: 3'
      ],
      packages=['onestep-django-app'],
      install_requires=[
          'django',
          'pillow',
          'psycopg2',
          'dj-database-url',
          'django-crispy-forms',
          'gunicorn'
      ],
      keywords=['python','django','web-app'],
)