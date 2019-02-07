---
layout: post
title:  "Welcome to tv2"
categories: python3
author: Madison Scott-Clary
---

I used [Terminal
Velocity](https://github.com/terminal-velocity-notes/terminal_velocity) for
years before, chasing the latest thing, I switched to Atom, which let me leave
a buffer of notes open without creating a file.

Obviously, this comes with some drawbacks. Even though that note file persists
across reboots, it's not synced anywhere, and it's not very well organized. It
led to a bunch of disparate ideas being left in a table named "untitled". I was
fairly committed to Atom, however, and just toughed it out for a while (despite
Terminal Velocity still being installed).

Eventually, I moved jobs, and this new one was less amenable to working from my
own computer (something something terabytes of test data something). I tried
`sshfs`, but that was too slow for my liking, especially with Atom doing some
weird syncing in the background. Back to Vim I went!

Of course, with Vim, you don't have persistent unnamed buffers, and I got tired
of searching for just *which* notes file I left that little tidbit in, so I went
digging, and lo! Terminal Velocity had been archived. Ah well, it happens. Folks
lose interest, move on to other tools, etc. I have all the respect in the world
for the authors and their work, as well as for their honest explanation of
having moved on, rather than just a live repository with "last commit 3 years
ago".

While the app had been left in a fairly stable state, there were a few things I
wanted to add to it, such as python3 support, a SQL-backed notebook for a
potential web frontend (it'd be nice to be able to take notes on my phone, after
all, and have them show up on my computers!), support for SimpleNote, etc.

Thus [tv2](https://github.com/makyo/tv2)!

I hope to maintain support of the project for a bit yet, and am open to bugs and
pull requests. Feel free to contribute along with me if tv2 is something you
like and use.

As an important note, tv2 drops support for python2, at least for the moment.
The first step was to run `2to3` on the repository. In the future, I'll see
about getting `six` in place.
