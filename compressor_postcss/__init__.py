from django.conf import settings
from compressor.filters import CompilerFilter


DEFAULT_BINARY = "postcss"
DEFAULT_ARGS = " "
DEFAULT_PLUGINS = ()


class PostCSSFilter(CompilerFilter):

    def plugins_as_args(plugins):
        """
        Take the plugins iterable and fix it so it can be used with
        the postcss command.
        """
        args = ''.join(map(lambda plugin: '--use %s ' % plugin, plugins))
        return args

    command = "{binary} {args} {plugins} -o {outfile} {infile}"
    options = (
        ("binary", getattr(settings, "COMPRESS_POSTCSS_BINARY", DEFAULT_BINARY)),
        ("args", getattr(settings, "COMPRESS_POSTCSS_ARGS", DEFAULT_ARGS)),
        ("plugins", plugins_as_args(getattr(settings, "COMPRESS_POSTCSS_PLUGINS", DEFAULT_PLUGINS))),
    )
