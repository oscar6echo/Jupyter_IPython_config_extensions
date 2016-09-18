

def _jupyter_server_extension_paths():
    return [{
        "module": "my_module"
    }]


def load_jupyter_server_extension(nbapp):
    print('toto')
    nbapp.log.info("my_module enabled")
