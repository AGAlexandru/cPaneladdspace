# cPaneladdspace

This script checks the available disk space for each cPanel user on the server. It also checks for users stored in /home2, if there is a /home2 partition.
If a user has less than 200MB available, the script will add another 1000MB to the user's disk quota, unless the disk is more than 95% full, in which case it won't run. These values can be easily edited to suit particular needs.
