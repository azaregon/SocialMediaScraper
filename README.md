# SocialMediaScraper

## server.py is the main server file

### for /seeig2 and /seetwt2

there are 4 main parameters

- unamefind    :  the account you want to scrape
- accuname     :  your account's login username for scraping other account
- accpwd       :  your scraping account's password
- postcnt      :  how many post do you want to retrieve (can be more)


usage example:
http://{url}/seetwt2?unamefind={target account}&accuname={your account username}&accpwd={your account password}&postcnt={how many post(s)}



### for /seeig and /seetwt

there are 4 mains parameter

- unamefind    :  the account you want to scrape\
- accuname     :  your account's login username for scraping other account\
- accpwd       :  your scraping account's password\
- scrollcount  :  how many scrolling do you want to do in single page
- postcnt( /seeig2 ) : how many posts you want to retrieve, (0 for all post)



usage example:

http://{url}/seeig?unamefind={target username}&accuname={your username}&accpwd={your password}&scrrollcount={how many scroll}


usage seeig2:
http://{url}/seeig?unamefind={target username}&accuname={your username}&accpwd={your password}&postcnt={how many post}
postcnt= 0 -> for retrieve all postsin the account
