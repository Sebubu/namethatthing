from bs4 import BeautifulSoup
import urllib
import sqlite3

class Nominee:
    def __init__(self, row, year, event, actor, movie, role, won):
        self.row = row
        self.year = year
        self.event = event
        self.actor = actor
        self.movie = movie
        self.role = role
        self.won = won

    def __str__(self):
        return self.row + ", " + self.year + ", " + self.event + ", " + self.actor + ", " + self.movie + ", " + self.role + ", " + self.won

    def list(self, attrs=[]):
        ret = []
        for attr in attrs:
            ret.append(getattr(self,attr))
        return ret

def read_nominees():
    url = "http://pc-10129.ethz.ch/academyawardnominees/"
    with urllib.request.urlopen(url) as respone:
        html = respone.read()
    html = html.decode('utf-8')

    soup = BeautifulSoup(html)
    table = soup.find(id="myTable")
    rows = table.find_all("tr")
    nominees = []
    for row in rows[1:]:
        cells = row.find_all("td")
        row = cells[0].get_text()
        year = cells[1].get_text()
        event = cells[2].get_text()
        actor = cells[3].get_text()
        movie = cells[4].get_text()
        role = cells[5].get_text()
        won = cells[6].get_text()
        nominee = Nominee(row, year, event, actor, movie, role, won)
        nominees.append(nominee)
    return nominees

nominees = read_nominees()
database_path = "database.db"
with sqlite3.connect(database_path) as conn:
    c = conn.cursor()
    for n in nominees:
        try:
            cmd = "insert into academy_award (year, event, movie, actor, role, won) " \
                  "values (?, ?, ?, ?, ?, ?)"
            c.execute(cmd, (n.year, n.event, n.movie, n.actor, n.role, n.won))
        except Exception as e:
            print(e)


'''
1. Which actor and which actress have won the first ever Academy Award for Best Actor/Actress?
    select * from academy_award order by year asc limit 1
    Ray Milland(1945)
2. Which actor and which actress have won the most Academy Awards?
    select count(*) as count, actor from academy_award where won = "True" group by actor order by count desc
    Daniel Day-Lewis(3) and Katharine Hepburn(3)
3. Which actor and which actress have been nominated for the most Academy Awards?
    select count(*) as count, actor from academy_award group by actor order by count desc
    Meryl Streep(15) and Jack Nicholson(8)
4. Which actor and which actress have received the most nominations without winning a single Academy Award?
    select count(*) as count, actor from academy_award where won = "False" group by actor order by count desc
    Meryl Streep(13) and Peter O'Toole(8)
5. List the shortest and the longest movie title you've collected.
    select movie, LENGTH(movie) as length from academy_award order by length desc
    54: Pirates of the Caribbean: The Curse of the Black Pearl
    select movie, LENGTH(movie) as length from academy_award order by length asc
    3: Ali
'''


