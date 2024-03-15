from flask import Flask, render_template, request
import json, os, random, datetime
from datetime import datetime
from jinja2.exceptions import TemplateNotFound
from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)


per_page = 10

def load_data():
    with open('data/football.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data


def logo_data():
    with open('data/logos.json', 'r', encoding="utf8") as f:
       data = json.load(f)
    return data




def prem_data2013():
    with open('data/premier_league_stats/prem2013.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def prem_data2014():
    with open('data/premier_league_stats/prem2014.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def prem_data2015():
    with open('data/premier_league_stats/prem2015.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def prem_data2016():
    with open('data/premier_league_stats/prem2016.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data




def bund_data2013():
    with open('data/bundesliga_stats/bund2013.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def bund_data2014():
    with open('data/bundesliga_stats/bund2014.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def bund_data2015():
    with open('data/bundesliga_stats/bund2015.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def bund_data2016():
    with open('data/bundesliga_stats/bund2016.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data





def seriea_data2013():
    with open('data/seriea_stats/seriea2013.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def seriea_data2014():
    with open('data/seriea_stats/seriea2014.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def seriea_data2015():
    with open('data/seriea_stats/seriea2015.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def seriea_data2016():
    with open('data/seriea_stats/seriea2016.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data





def liga_data2013():
    with open('data/laliga_stats/laliga2013.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def liga_data2014():
    with open('data/laliga_stats/laliga2014.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def liga_data2015():
    with open('data/laliga_stats/laliga2015.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data
def liga_data2016():
    with open('data/laliga_stats/laliga2016.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    return data





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fulldb', methods = ["GET", "POST"])
def fulldb():
    global per_page
    query = request.args.get('query','').strip().lower()
    league = request.args.get('league','').strip().lower()
    team = request.args.get('team','').strip().lower()
    year = request.args.get('year','').strip()
    startdate = request.args.get('startdate','').strip()
    enddate = request.args.get('enddate','').strip()

    if enddate == "":
        enddate = "2018-01-01"

    if startdate == "":
        startdate = "2013-01-01"

    keywords = query.split()


    fixtures = load_data()

    leagues = set(fixture['division'] for fixture in fixtures)
    teams = set(fixture['home_team'] for fixture in fixtures)
    sorted_teams = sorted(teams)
    years = set(datetime.strptime(fixture['date'],'%Y-%m-%d').year for fixture in fixtures)
    sorted_years = sorted(years)
    matches = []
    for fixture in fixtures:
        match_data = {
            'date': fixture['date'],
            'division': fixture['division'],
            'home_team': fixture['home_team'],
            'away_team': fixture['away_team'],
            'home_score': fixture['home_score'],
            'away_score': fixture['away_score'],
            'divisionurl': f'/{fixture["division"].replace(" ", "")}',
            'url': f'/matches/{fixture["home_team"]}_vs_{fixture["away_team"]}_{fixture["date"]}'
        }

        if (not league or league.lower() == fixture['division'].lower()) and\
           (not team or team.lower() == fixture['home_team'].lower() or team.lower() == fixture['away_team'].lower()) and\
           (not year or int(year) == datetime.strptime(fixture['date'], '%Y-%m-%d').year) and\
           (not startdate or (startdate <= fixture['date'] and fixture['date'] <= enddate)):

            if all(keyword in str(match_data).lower() for keyword in keywords):
                matches.append(match_data)

                
    
        
    if startdate != "2013-01-01":
        matches = sorted(matches, key=lambda d: d['date'])
    elif enddate != "2018-01-01":
        matches = sorted(matches, key=lambda d: d['date'])
    else:
        matches = sorted(matches, key=lambda d: d['home_team'])

    page = int(request.args.get('page', 1))
    per_page = int(request.form.get('per_page', per_page))
    offset = (page - 1) * per_page
    items_pagination = matches[offset:offset + per_page]
    inner_window = 2
    outer_window = 1
    total = len(matches)
    pagination = Pagination(page=page, per_page=per_page, offset=offset, total=total, inner_window=inner_window, outer_window=outer_window)
    return render_template('fulldb.html',leagues=leagues,teams=sorted_teams,years=sorted_years,league=league,team=team,year=year,startdate=startdate,enddate=enddate,pagination=pagination, items=items_pagination, query=query, per_page=per_page)


@app.route('/EnglishPremierLeague')
def premierleague():

    standings2013 = prem_data2013()
    eplstats2013 = []
    for standing in standings2013:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2013-08-17&enddate=2014-05-11"
        }
        eplstats2013.append(standing_data)



    standings2014 = prem_data2014()
    eplstats2014 = []
    for standing in standings2014:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2014-08-16&enddate=2015-05-24"
        }
        eplstats2014.append(standing_data)


    standings2015 = prem_data2015()
    eplstats2015 = []
    for standing in standings2015:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2015-08-08&enddate=2016-05-17"
        }
        eplstats2015.append(standing_data)


    standings2016 = prem_data2016()
    eplstats2016 = []
    for standing in standings2016:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2013-08-13&enddate=2014-05-21"
        }
        eplstats2016.append(standing_data)

    return render_template('prem.html',epl2013=eplstats2013,epl2014=eplstats2014,epl2015=eplstats2015,epl2016=eplstats2016)


@app.route('/DeutscheBundesliga')
def bundesliga():


    standings2013 = bund_data2013()
    blstats2013 = []
    for standing in standings2013:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2013-08-09&enddate=2014-05-10"
        }
        blstats2013.append(standing_data)


    standings2014 = bund_data2014()
    blstats2014 = []
    for standing in standings2014:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2014-08-22&enddate=2015-05-23"
        }
        blstats2014.append(standing_data)


    standings2015 = bund_data2015()
    blstats2015 = []
    for standing in standings2015:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2015-08-14&enddate=2016-05-14"
        }
        blstats2015.append(standing_data)

    standings2016 = bund_data2016()
    blstats2016 = []
    for standing in standings2016:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2016-08-26&enddate=2017-05-20"
        }
        blstats2016.append(standing_data)

    return render_template('bundesliga.html',bl2013=blstats2013,bl2014=blstats2014,bl2015=blstats2015,bl2016=blstats2016)




@app.route('/SerieA')
def seriea():


    standings2013 = seriea_data2013()
    srstats2013 = []
    for standing in standings2013:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2013-08-24&enddate=2014-05-18"
        }
        srstats2013.append(standing_data)


    standings2014 = seriea_data2014()
    srstats2014 = []
    for standing in standings2014:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2014-08-30&enddate=2015-05-31"
        }
        srstats2014.append(standing_data)


    standings2015 = seriea_data2015()
    srstats2015 = []
    for standing in standings2015:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2015-08-22&enddate=2016-05-15"
        }
        srstats2015.append(standing_data)

    standings2016 = seriea_data2016()
    srstats2016 = []
    for standing in standings2016:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2016-08-20&enddate=2017-05-28"
        }
        srstats2016.append(standing_data)

    return render_template('seriea.html',sr2013=srstats2013,sr2014=srstats2014,sr2015=srstats2015,sr2016=srstats2016)








@app.route('/LaLiga')
def laliga():


    standings2013 = liga_data2013()
    llstats2013 = []
    for standing in standings2013:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2013-08-17&enddate=2014-05-18"
        }
        llstats2013.append(standing_data)


    standings2014 = liga_data2014()
    llstats2014 = []
    for standing in standings2014:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2014-08-23&enddate=2015-05-23"
        }
        llstats2014.append(standing_data)


    standings2015 = liga_data2015()
    llstats2015 = []
    for standing in standings2015:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2015-08-21&enddate=2016-05-15"
        }
        llstats2015.append(standing_data)

    standings2016 = liga_data2016()
    llstats2016 = []
    for standing in standings2016:
        standing_data = {
            'Pos': standing['Pos'],
            'Logo': standing['Logo'],
            'Team': standing['Team'],
            'Played': standing['Played'],
            'Won': standing['Won'],
            'Drawn': standing['Drawn'],
            'Lost': standing['Lost'],
            'Points': standing['Points'],  
            'Url': f"/fulldb?team={standing['Team']}&startdate=2016-08-20&enddate=2014-05-2017"
        }
        llstats2016.append(standing_data)

    return render_template('laliga.html',ll2013=llstats2013,ll2014=llstats2014,ll2015=llstats2015,ll2016=llstats2016)



@app.route('/matches/<filename>')
def matchsite(filename):

    matchfolder = 'templates/matches'
    if not os.path.exists(matchfolder):
        os.mkdir(matchfolder)

    fixtures = load_data()
    logos = logo_data()

    teamlogo_dict = {team['Team']: team['Logo'] for team in logos}

    for fixture in fixtures:
        if f'{fixture["home_team"]}_vs_{fixture["away_team"]}_{fixture["date"]}' == filename:
            game = fixture
            home_team_logo = teamlogo_dict.get(fixture['home_team'], None)
            away_team_logo = teamlogo_dict.get(fixture['away_team'], None)
            divisionurl = f'/{fixture["division"].replace(" ", "")}'
            home_team_url =  f"/fulldb?team={fixture['home_team']}"
            away_team_url = f"/fulldb?team={fixture['away_team']}"

        
    if game:
        try:
            return render_template(f'matches/{filename}.html')
        
        except TemplateNotFound:
            htmlcont = render_template('matchtemp.html', match=game, home_team_logo=home_team_logo, away_team_logo=away_team_logo, home_team_url=home_team_url, away_team_url=away_team_url, divisionurl=divisionurl)  
            with open(f'templates/matches/{filename}.html', 'w') as matchfile:
                matchfile.write(htmlcont)
            return render_template(f'matches/{filename}.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
                             
if __name__ == '__main__':
    app.run(debug=True)

