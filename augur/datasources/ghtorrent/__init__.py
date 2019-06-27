#SPDX-License-Identifier: MIT
from augur.application import Application
from augur.augurplugin import AugurPlugin
from augur import logger

class GHTorrentPlugin(AugurPlugin):
    """
    This plugin serves as an example as to how to load plugins into Augur
    """
    def __init__(self, augur):
        self.__ghtorrent = None
        # _augur will be set by the super init
        super().__init__(augur)

    def __call__(self):
        from .ghtorrent import GHTorrent
        if self.__ghtorrent is None:
            logger.debug('Initializing GHTorrent')
            self.__ghtorrent = GHTorrent(
                user=self._augur.read_config('GHTorrent', 'user', 'AUGUR_GHTORRENT_DB_USER', 'root'),
                password=self._augur.read_config('GHTorrent', 'pass', 'AUGUR_GHTORRENT_DB_PASS', 'password'),
                host=self._augur.read_config('GHTorrent', 'host', 'AUGUR_GHTORRENT_DB_HOST', '127.0.0.1'),
                port=self._augur.read_config('GHTorrent', 'port', 'AUGUR_GHTORRENT_DB_PORT', '3306'),
                dbname=self._augur.read_config('GHTorrent', 'name', 'AUGUR_GHTORRENT_DB_NAME', 'msr14')
            )
        return self.__ghtorrent

    def create_routes(self, flask_app):
        """
        Responsible for adding this plugin's data sources to the API
        """
        from .routes import create_routes
        create_routes(flask_app)

GHTorrentPlugin.augur_plugin_meta = {
    'name': 'ghtorrent',
    'datasource': True
}
Application.register_plugin(GHTorrentPlugin)

__all__ = ['GHTorrentPlugin']
