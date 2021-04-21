import shutil
import os

import nbformat
from traitlets import Type, default
from traitlets.config.configurable import LoggingConfigurable

from .filemanager import LocalFileManager


class SnapshotManager(LoggingConfigurable):

    @default
    def filemanager(self):
        return LocalFileManager

    def put(self, path, content):
        raise NotImplementedError()

    def get(self, path):
        raise NotImplementedError()

    def delete(self, path):
        raise NotImplementedError()

    def copy(self, src_path, dest_path):
        raise NotImplementedError()

    def mv(self, from_path, to_path):
        raise NotImplementedError()


class LocalSnapshotManager(SnapshotManager):

    def __init__(self):
        super(LocalSnapshotManager, self).__init__()

    def put(self, path, content):
        if os.path.exists(path):
            raise RuntimeError(f'{path} already exists!')
        if not content:
            raise RuntimeError(f'notebook content is none')

        if isinstance(content, dict):
            # Content may come from model as a dict directly
            nb = nbformat.versions[
                        content.get("nbformat", nbformat.current_nbformat)
                      ].nbjson.JSONReader().to_notebook(content)

            nbformat.write(nb=nb, fp=path, version=nbformat.current_nbformat)
        else:
            nb = nbformat.reads(s=content, as_version=nbformat.current_nbformat)
            return nbformat.write(nb=nb, fp=path, as_version=nbformat.current_nbformat)

    def get(self, path):
        if not os.path.exists(path):
            raise RuntimeError(f'cannot get a file[{path}] that does not exist')
        return nbformat.read(fp=path, as_version=nbformat.current_nbformat)

    def delete(self, path):
        shutil.rmtree(path)

    def copy(self, src_path, dest_path):
        if os.path.isfile(src_path):
            shutil.copyfile(src_path, dest_path)
        else:
            shutil.copytree(src_path, dest_path)

    def mv(self, from_path, to_path):
        shutil.move(from_path, to_path)


class ConfigurableSnapshotManager(SnapshotManager):

    snapshot_manager_class = Type(
        default_value=LocalSnapshotManager,
        klass=LocalSnapshotManager,
        config=True,
        help='The snapshot manager class to use.'
    )

    def put(self, path, content):
        pass

    def get(self, path):
        pass

    def delete(self, path):
        pass

    def copy(self, src_path, dest_path):
        pass

    def mv(self, from_path, to_path):
        pass



