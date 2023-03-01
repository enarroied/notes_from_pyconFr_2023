# Change the settings to make the html folder

## Why to change the settings

I have the documents used to create the documentation in a folder called "doc". When I create the html files with the ```make html``` command, the html files are inserted in doc/build.html.

But when I uplpoad the documentation to github, if I want github pages to display my page, I need to have it in a folder called "doc" in the root of the project. So it would be very convenient if that was the default setting, instead of having to drag and drop (+ there is the risk of forgetting to do it).


## How to change the settings

So let's be honnest, chatGPT helped me with this one 😃, since I do not often deal with makefiles.

Here are the steps:

1. Change the makefile

in the BUILDDIR line, I changed the relative path to make it the ```docs``` directory, at the same level of the doc folder containing the Sphinx project:

```makefile
BUILDDIR      = ../docs
```

2. Change the python configuration file

Add the following 2 lines to your ```conf.py``` file:

```python
html_baseurl = '.'
html_output_dir = 'docs'
```