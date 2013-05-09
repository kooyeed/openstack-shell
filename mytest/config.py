# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""Wrapper for test.common.config that configures itself on import."""


from mytest.common import config


config.configure()
CONF = config.CONF

setup_logging = config.setup_logging
register_str = config.register_str
register_cli_str = config.register_cli_str
register_list = config.register_list
register_cli_list = config.register_cli_list
register_bool = config.register_bool
register_cli_bool = config.register_cli_bool
register_int = config.register_int
register_cli_int = config.register_cli_int
setup_authentication = config.setup_authentication
