# cPaneladdspace

This script checks the available disk space for each cPanel user on the server.
If a user has less than 200MB available, the script will add another 1000MB to the user's disk quota, unless the disk is more than 95% full.
It also looks for another /home partition, named /home2 and checks the users stored in there too.
