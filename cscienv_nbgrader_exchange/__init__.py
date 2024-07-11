from ._version import __version__
from jupyter_server.serverapp import ServerApp

def _jupyter_server_extension_points():
    return [{
        "module": "cscienv_nbgrader_exchange"
    }]

def _load_jupyter_server_extension(server_app: ServerApp):
    name = "cscienv_nbgrader_exchange"
    server_app.log.info(f"Registered {name} server extension")


# For backward compatibility with notebook server - useful for Binder/JupyterHub
load_jupyter_server_extension = _load_jupyter_server_extension

