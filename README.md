PostCSS for django-compressor
============================

<!-- copied directly from postcss's README file -->
<img align="right" width="95" height="95"
     title="Philosopher’s stone, logo of PostCSS"
     src="http://postcss.github.io/postcss/logo.svg">

This module will let you use PostCSS as a filter with django-compressor. You can
use any postcss plugin you wish (assuming the plugin is installed).

Installation
------------

Install this package:

    pip install django-compressor-postcss

You also need to install the postcss tool itself and depending on what plugins
you plan to use, you should install those manually.

Example:

    sudo npm install -g postcss-cli
    sudo npm install -g autoprefixer postcss-font-magician

Configuration
-------------

Your Django's settings should look something like below.

```python
COMPRESS_CSS_FILTERS = (
    ..
    'compressor_postcss.PostCSSFilter',
    ..
)

COMPRESS_POSTCSS_PLUGINS = (
    'autoprefixer',
    'postcss-font-magician'
)
```

`COMPRESS_POSTCSS_PLUGINS` determines the plugins that PostCSS will use.
