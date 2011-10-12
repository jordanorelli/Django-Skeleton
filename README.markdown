This is my personal Django skeleton project.  It's not necessarily going to look exactly how you might lay out your own Django projects, it's just how I lay out mine.

First, I recommend using [pip](http://pypi.python.org/pypi/pip) and [virtualenv](http://pypi.python.org/pypi/virtualenv) to manage your dependencies.  It may seem like a headache at first, but it's honestly less of a headache than installing things globally since your OS provider may put packages in the global space that conflict with packages you wish to use in your project space.  I have included a `requirements.txt` file that details all of the project requirements, which can be installed automatically in pip using `pip install -r requirements.txt`.  pip won't cache downloaded packages automatically, but you can specify a local cache directory by exporting a `PIP_DOWNLOAD_CACHE` environment variable.  I strongly recommend adding `export PIP_DOWNLOAD_CACHE=$HOME/.pip_cache` or something similar to your `.bashrc` to speed up the creation of similar virtual environments.

I am also a fan of [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper) for centralizing my virtual environments and project files.  It's a big help, especially since you can add hooks to it.  In a nutshell it allows you to specify two directories: one for storing virtual environments, the other for storing projects.  When you say `mkvirtualenv` it creates your environment in your preconfigured environment directory.  You can then say `lsvirtualenvs` to get a list of environments, `rmvirtualenv` to remove an environment by name, and `workon` to activate an environment by name instead of having to source the activation script manually or create your own alias every time you make a new environment (which is what I was doing in the past).  The really useful thing is that it includes a `mkproject` function that will make a virtual environment and a project directory, that way when you say `workon my_project` it will activate the environment and navigate there at the same time.  It has bash completion as well, so you can type workon at your command line and hit tab a few times to see which projects are on your system and what their names are.  So cool!  It also has hooks that will let you run arbitrary code when activating or deactivating an environment without having to modify the `bin/activate` script in your environment itself.  Of course, with the proper shebang your hook scripts can be written in Python instead of bash/zsh/whatever.

The way I have my project configured is a bit unconventional, and I don't think it will work out of box on Windows machines (sorry).  Essentially what I do is create a `conf` directory at the root of the project.  Within this directory there are subdirectories that each represent a host or group of hosts.  The `settings.py` in particular uses `conf/base/settings.py` to define the settings that are common to all hosts, which can then (actually must) be extended.  A basic localhost setup is illustrated in `conf/local/settings.py` using sqlite, which I find good enough for localhost development and quickly messing around.

I put all of my project settings into the repository so that every host's settings are versioned, and then manage which settings file is active using a [symbolic link](http://en.wikipedia.org/wiki/Symbolic_link).  The repository starts out with a symlink to `conf/local/settings.py`, which gives you baseline settings that will work out of box.

The "welcome" page has been moved into the project itself so that the way Django routes URLs is more apparent.  It's a bit weird that the default Django project has a welcome page that comes from a completely different area on your system.  Putting the welcome page into the project makes Django's request-handling process a bit more transparent for first-timers.

One thing that I haven't done is linked in the admin media yet, but that's because that's a per-host thing.  For localhost development I just use the Django development server, which will serve up the admin media directly, and for servers I symlink in the admin media.

Apps are put in their own `apps` directory, just to make things tidy, and the base settings file adds this directory to the python path at runtime.  You can see in `conf/base/settings.py` how the `main` app is referenced.

There's an additional `manage.py` command in `apps/main/management/commands/new_secret.py` that serves to illustrate how you can write your own `manage.py` commands and, more importantly, to regenerate the `SECRET_KEY` found in your `conf/base/settings.py` file.  **Be sure to run this command to generate a unique SECRET\_KEY**.  You can do so by typing `./manage.py new_secret` at the project root.

I've also included a `fabfile.py`, which is used to create tasks for [Fabric](http://docs.fabfile.org/en/1.2.2/index.html), a library for managing SSH deployment.  I don't generally condone using the `from modulename import *` syntax since it makes it very non-obvious where things are coming from, but it made it possible to dynamically create connection functions at runtime, which are generated based on host configurations.  There's a sample configuration included in `conf/dev/hosts.py` that would show how you would, in theory, add a remote host configuration for a server called `dev`.  If you fill that in with some real host details you'll be able to `fab dev uname` to use the included `uname` task.  All it does it print out some info about the system, but it's enough to illustrate how to create Fabric tasks and test your host configuration.  Unfortunately Fabric does not currently read your settings in `~/.ssh/config`, so you may have to repeat them.

I personally add a little chunk of code to my `.bashrc` to create a `mkdjango` function, which will create a virtual environment of the same name, create a project directory, clone this skeleton into that directory, regenerate the SECRET\_KEY, remove this README, install all of the requirements to the virtualenv via pip, run `syncdb` to create a developmentdatabase, and fire up the application, all in one command.  Requires pip, virtualenv, and virtualenvwrapper to work properly.  Here is my `mkdjango` function:

    mkdjango () {
        mkproject --no-site-packages --prompt=$1: $1 &&
        git init &&
        git pull git://github.com/jordanorelli/Django-Skeleton.git master &&
        rm README.markdown &&
        pip install -r requirements.txt &&
        ./manage.py new_secret &&
        ./manage.py syncdb &&
        ./manage.py runserver
    }

With that in my `~/.bashrc`, all I have to say is `mkdjango some_project_name` and I'm ready to rock.
