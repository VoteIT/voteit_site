#!/bin/bash
rsync -Pz voteit@www.voteit.se:~/srv/voteit_site/var/Data.fs var/Data.fs
rsync -Prz voteit@www.voteit.se:~/srv/voteit_site/var/blob var/.
