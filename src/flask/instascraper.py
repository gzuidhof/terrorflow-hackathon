import instagramscraper as isc #download with: pip install instagram-scraper
from os import listdir
from os.path import isfile, join
import os

if not os.path.isdir('../../data/instagram_users/'):
    os.mkdir('../../data/instagram_users/')


def scrape_user(usernames, maxfilesperuser=10):
    '''
    usernames = list of users
    maxfilesperuser: maximum number of files to return per given user
    '''
    distname = "../../data/instagram_users/"
    scraper = isc.InstagramScraper(usernames, dst=distname, retain_username=True, max=maxfilesperuser)
    scraper.scrape()
    allfiles = []
    for user in usernames:
        folder = join(distname, user)
        files = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
        if maxfilesperuser > len(files):
            allfiles = allfiles + files
        else:
            allfiles = allfiles + files[0:maxfilesperuser]

    allfiles = filter(lambda x: x.endswith(".jpg"), allfiles)
    return allfiles

#print(scrape_user(['linksjugendsolidstralsund'], 10))