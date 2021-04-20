from traitlets.config.configurable import LoggingConfigurable


class FileManager(LoggingConfigurable):

    def put(self, path, content):
        raise NotImplementedError

    def get(self, path):
        raise NotImplementedError

    def mv(self, from_path, to_path):
        raise NotImplementedError

    def copy(self, src, dest):
        raise NotImplementedError


