# proxy-list-auto-pull-in-30min
This project basically allows to you auto pull any Github repository with timestamp. Wrote with Python. (document paths setted for unix system)

Clone which proxy-list repository you want to use then set the folder path in autopull.py

# Repo-Auto-Pull
A Script made to pull files from a repo every [amount] of hours.

For this you will need to run ```pip install GitPython ```

I made this script for my FiveM Server so it would pull the updated files every 6 hours.
The Timer can be removed and the script can be added to your start.bat which would look something like this: 
```
cd /d C:\myServer\cfx-server-data
python autopull.py 
Stop (like cmd+c) autopull.py after 90s
C:\myServer\run.cmd +exec server.cfg
```
The ```Stop (like cmd+c) autopull.py after 90s``` allows for the files to pulled from the REPO.

This script can be used for any application, Allowed many developers to upload to your REPO and the new version being updated on your server every [amount] of hours



# proxy-list

Proxies are checked on my VPS every 30 minutes using [proxy-scraper-checker](https://github.com/monosans/proxy-scraper-checker).

Every proxy's entry-node and exit-node are IPv4.

## Folders description

`proxies` - proxies with any anonymity level.

`proxies_anonymous` - anonymous proxies.

`proxies_geolocation` - same as `proxies`, but includes exit-node's geolocation.

`proxies_geolocation_anonymous` - same as `proxies_anonymous`, but includes exit-node's geolocation.

Geolocation format is ip:port::Country::Region::City.

## Credit to Linus Torvalds | Almaz

Thanks for support the open source [Linus Torvalds](https://github.com/torvalds) and [Almaz](https://github.com/monosans).

