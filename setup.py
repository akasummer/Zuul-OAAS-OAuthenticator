from setuptools import setup

setup(
    name='jupyterhub-zuuloaasoauthenticator',
    version='0.1',
    description='Zuul OAAS FIT CVUT Authenticator for JupyterHub',
    url='https://github.com/akasummer/Zuul-OAAS-OAuthenticator',
    author='akasummer',
    author_email='vanyaginds@gmail.com',
    license='Apache 2.0',
    tests_require = [
    'unittest2',
    ],
    test_suite = 'unittest2.collector',
    packages=['zuuloaasoauthenticator'],
    install_requires=[
        'jupyterhub',
        'python-jose',
    ]
)