Contributing to tv2
-----------------------------------

Welcome! First of all, note that this project is governed by a [code of
conduct](/code-of-conduct.md)

If you want to contribute a bug report or feature request to tv2, use [GitHub
Issues](https://github.com/makyo/tv2/issues?state=open).

If you want to contribute documentation, for example to explain how to combine
tv2 with an external tool that handles something like note synchronisation or
encryption, use [the wiki](https://github.com/makyo/tv2/wiki).

If you want to contribute code to tv2: create your own GitHub account, fork
tv2, create a new bugfix or feature branch and commit your code to it, push
your branch to your tv2 fork on GitHub, then send a pull request asking to
merge your feature branch into my master branch. In detail:

1. [Install the tv2 development
version](#how-to-install-the-tv2-development-version).

2. Checkout a new branch, forked from the master branch, e.g.  `git checkout -b
my-new-feature`. _Don't commit on the master branch_, instead develop each
bugfix or feature on its own branch forked from master.

3. [Create a GitHub account](https://github.com/signup) (it's free!)

4. Fork my tv2 repo: click the _Fork_ button on the tv2 GitHub page.

5. In the git clone on your dev machine, add your GitHub fork as a remote (you
only need to this once):

        git remote add MY_FORK https://github.com/YOUR_USERNAME/tv2.git

6. Push your feature or bugfix branch to your fork:

        git push MY_FORK my-new-feature

7. Use the _Pull Request_ button on the main tv2 project page to send me a pull
request, asking me to pull your bugfix or feature branch into my master branch.

8. Once I've pulled your pull request, then you can pull my master branch into
the master branch on your dev machine and push it to the master branch on your
GitHub fork, to get the new feature in those master branches as well:

        git checkout master git pull origin master git push MY_FORK master

For code style, I try to follow [PEP
8](http://www.python.org/dev/peps/pep-0008/) and [PEP
257](http://www.python.org/dev/peps/pep-0257/). For git commit messages, I try
to follow these [Commit
Guidelines](http://git-scm.com/book/en/Distributed-Git-Contributing-to-a-Project#Commit-Guidelines).


### How To Install the tv2 Development Version

To install tv2 for development, you need [Python](http://www.python.org/),
[virtualenv](http://www.virtualenv.org/),
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
and [git](http://git-scm.com/) (technically you can make do without virtualenv
and virtualenvwrapper, but they make development a lot more convenient).

Use virtualenvwrapper to create a Python virtualenv and install tv2 and its
dependences into the virtualenv, for example:

    $ mkvirtualenv tv2
    (tv2) $ mkdir -p ~/Projects/tv2
    (tv2) $ cd ~/Projects/tv2
    (tv2) $ setvirtualenvproject
    (tv2) $ git clone https://github.com/vhp/tv2.git
    (tv2) $ cd tv2
    (tv2) $ python setup.py develop
    (tv2) $ deactivate
    $ workon tv2

At this point, the `tv2` command should run your development copy of tv2 from
your virtualenv:

    (tv2) $ which tv2
    /home/makyo/.virtualenvs/tv2/bin/tv2

Each time you open a new shell to start working on tv2 development, you need to
activate your tv2 virtualenv:

    $ workon tv2
    (tv2) $

When you're finished working, deactivate the virtualenv:

    (tv2) $ deactivate
    $

While the virtualenv is deactivated, the `tv2` command will run your installed
release version of tv2 (if you have one) rather than the development version
installed in your virtualenv:

    $ which tv2
    /usr/local/bin/tv2

So you can easily switch between your stable and development copies of Terminal
Velocity by activating and deactivating your virtualenv with the `workon` and
`deactivate` commands. You can also have multiple shells open, some with the
virtualenv activated and others not, so you can use your stable copy of tv2 to
takes note while you hack on your development version.

You can also setup different aliases (e.g. in your `~/.bashrc` or `~/.zshrc`)
for running the release and development versions:

    alias tv="/usr/local/bin/tv2"
    alias tvdev="/home/seanh/.virtualenvs/tv2/bin/python /home/seanh/Projects/tv2/bin/tv2"

