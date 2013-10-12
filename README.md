tizen-manifest
==============

download source code from https://review.tizen.org/git/ using repo, originated from git://gitorious.org/tizen-toys/tizen-manifest.git


==============
This is the manifest file for Tizen which can be used with repo.

To install, initialize, and configure Repo, follow these steps: $ mkdir ~/bin $ PATH=~/bin:$PATH

Download the Repo script and ensure it is executable: $ curl https://dl-ssl.google.com/dl/googlesource/git-repo/repo > ~/bin/repo $ chmod a+x ~/bin/repo

Create an empty directory to hold your working files. $ mkdir WORKINGDIRECTORY $ cd WORKINGDIRECTORY

Run repo init to bring down the latest version of Repo with all its most recent bug fixes. You must specify a URL for the manifest, which specifies where the various repositories included in the Tizen source will be placed within your working directory. $ repo init -u git://gitorious.org/tizen-toys/tizen-manifest

To pull down files to your working directory from the repositories as specified in the default manifest, run $ repo sync
