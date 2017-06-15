# cPaneladdspace

This script checks the available disk space for each cPanel user on the server. It assumes that the cPanel user directories are stored in /home or /home2.
If a user has less than 200MB available, the script will add another 1000MB to the user's disk quota, unless the disk is more than 95% full.
