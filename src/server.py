import flask
import instagramScrape
import twitterScrape




app = flask.Flask(__name__)



@app.route('/seeig')
def see_the_ig():
    uName_find = flask.request.args['unamefind']
    account_username = flask.request.args['accuname']
    account_pwd = flask.request.args['accpwd']

    try:
        scrollcnt = int(flask.request.args['scrollcount'])
    except:
        scrollcnt = 3

    if uName_find == '' or account_username == '' or account_pwd == '':
        return "some argument not filled,\n fill unamefind = account you want to scrape \n accuname = your account to scrape \n accpwd = your scraping account password"


    result = instagramScrape.go_see_ig(uName_find,account_username,account_pwd,scrollcnt)

    return result

@app.route('/seeig2')
def see_the_ig2():
    uName_find = flask.request.args['unamefind']
    account_username = flask.request.args['accuname']
    account_pwd = flask.request.args['accpwd']

    try:
        postcnt = int(flask.request.args['postcnt'])
    except:
        postcnt = 3

    if uName_find == '' or account_username == '' or account_pwd == '':
        return "some argument not filled,\n fill unamefind = account you want to scrape \n accuname = your account to scrape \n accpwd = your scraping account password"


    result = instagramScrape.go_see_ig_Instaloader(uName_find,account_username,account_pwd,postcnt)

    return result


@app.route('/seetwt')
def see_the_twt():
    uName_find = flask.request.args['unamefind']
    account_username = flask.request.args['accuname']
    account_pwd = flask.request.args['accpwd']

    try:
        scrollcnt = int(flask.request.args['scrollcount'])
    except:
        scrollcnt = 3

    if uName_find == '' or account_username == '' or account_pwd == '':
        return "some argument not filled,\n fill unamefind = account you want to scrape \n accuname = your account to scrape \n accpwd = your scraping account password"


    result = twitterScrape.go_see_x(uName_find,account_username,account_pwd,scrollcnt)

    return result







if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


