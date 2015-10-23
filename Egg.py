#Grabs yer podcasts from the supplied rss feeds, deletes them after the 
#specified time has passed.

#Obtain xml from rss URL in rss list.  If none in rss, end.
#Parse for download urls and return a list of them
#for auto dl, check to see if most recent has already been dl'd
#if not, download, then add filename and dl date 'Egg' tuple to dl list
#if Egg is expired, per user provided timeframe, delete it.
