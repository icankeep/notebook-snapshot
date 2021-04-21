import os

from .handler import handlers


def _jupyter_server_extension():
    return [{'module': 'notebook-snapshot'}]


def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    for path, handler in handlers:
        route_pattern = os.path.join(web_app.settings['base_url'], path)
        web_app.add_handlers(host_pattern, [(route_pattern, handler)])
    nb_server_app.log.info('notebook snapshot extension loaded')
