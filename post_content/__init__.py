"""A Jupyter custom magic command to post cell contents to a REST server"""
__version__ = '0.0.1'

from .post_content import PostContent

def load_ipython_extension(ipython):
    print("PostContent loaded")
    ipython.register_magics(PostContent)
