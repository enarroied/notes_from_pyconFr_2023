# Let's make our site a bit more pretty

## Add read the docs theme

So just because this is a documentation site and a static site, it does not mean it has to be plain and boring. Sphinx comes with a default theme, called [Alabaster](https://alabaster.readthedocs.io/en/latest/). 

Who knows, maybe I will stick to that theme in the future, but here, just to try, I'm gonna install a different theme.

You could use one of the built-in themes (https://www.sphinx-doc.org/en/master/usage/theming.html). You can also find [the read the docs theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html), and install it with pip:

```
pip install sphinx_rtd_theme
```

And the you have to add the theme to the extensions in the ```conf.py``` file.

```python
extensions = [
    ...
    'sphinx_rtd_theme',
]

html_theme = "sphinx_rtd_theme"
```

## Add a favicon

Because favicons are useless but still make your site look better, let's add one. I will use the image from Pycon Fr 2023, since I am making this mock site thank to it!

I found how to do it in this [stack overflow post](https://stackoverflow.com/questions/54639192/change-the-favicon-of-the-sphinx-read-the-docs-theme)

Just add, to ```conf.py``` file:

```python
html_favicon = 'favicon.ico'
```