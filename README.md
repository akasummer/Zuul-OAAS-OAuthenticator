# JupyterHub Zuul OAAS Authenticator - A CVUT FIT OAuth2 Authenticator for JupyterHub

## Installation

This package can be installed with pip:

```
pip install jupyterhub-zuuloaasoauthenticator
```

Alternately, you can clone this repository and run:

```
cd Zuul-OAAS-OAuthenticator
pip install -e .
```

## Configuration

You should edit your :file:`jupyterhub_config.py` to set the authenticator class:

##### For authentication
```
c.JupyterHub.authenticator_class = 'zuuloaasoauthenticator.ZuulOAASOAuthenticator.ZuulOAASOAuthenticator'
```
