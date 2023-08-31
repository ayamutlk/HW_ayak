
import sqlite3

def sql_connection():
    con = sqlite3.connect("movies_site.db")
    return con

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS data_indicators(id integer PRIMARY KEY,\
     url text, data_type text, locator text, locator_type text)")
    con.commit()
#
# def sql_table_click(con):
#     cursorObj = con.cursor()
#     cursorObj.execute("CREATE TABLE IF NOT EXISTS btn_indicators(id integer PRIMARY KEY,\
#      data_type text, content text, locator text, locator_type text)")
#     con.commit()


# def sql_table_login(con):
#     cursorObj = con.cursor()
#     cursorObj.execute("CREATE TABLE IF NOT EXISTS btn_indicators(id integer PRIMARY KEY,\
#      data_type text, content text, locator text, locator_type text)")
#     con.commit()


con = sql_connection()
sql_table(con)

my_indicators = [(1, "description", "TEST DESCRIPTION", "textarea[name='description']", "CSS_SELECTOR"),
                 (2, "movie_title", "TEST TITLE", "input[name='movie_title']", "CSS_SELECTOR"),
                 (3, "director", "TEST DIRECTOR", "input[name='director']", "CSS_SELECTOR"),
                 (4, "release_year", "1990", "input[name='release_year']", "CSS_SELECTOR"),
                 (6, "poster", "C:/Users/Administrator/Desktop/godfa2.jpg", "input[name='filename']",
                  "CSS_SELECTOR"),
                 (7, "actor", "MAIN ACTORS", "input[name='actor']", "CSS_SELECTOR"),
                 (8, "video", '<iframe width="560" height="315" src="https://www.youtube.com/embed/wPmTp9up26w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
                  "input[name='video']", "CSS_SELECTOR"),
                 (9, "movie", "Click on the movie", "(//img)[12]", "XPATH"),
                 (10, "comment", "Talia", "input[name='name']", "CSS_SELECTOR"),
                 (11, "review text", "Awesome", "textarea[name='review_text']", "CSS_SELECTOR"),
                 (12, "rating", "Awesome", "label[title='Awesome']", "CSS_SELECTOR"),
                 (13, "rating button", "Click on button", "button[type='submit']", "CSS_SELECTOR"),
                 (14, "delete review", "Click on delete review", "//body/ol[2]/form[20]/button[1]", "XPATH"),
                 (15, "about", "ABOUT ME LOGO", "//img[@alt='logo']", "XPATH"),
                 (16, "logo homepage", "LOGO HOMEPAGE", "img[alt='logo']", "CSS_SELECTOR"),
                 (17, "top button", "GO TO TOP BUTTON", "div[class='button']", "CSS_SELECTOR"),
                 (18, "alter button", "ALTER BUTTON", "//a[normalize-space()='alter']", "XPATH"),
                 (19, "director-alt", "Joseph Kosinski", "//input[@name='director']", "XPATH"),
                 (20, "main actors-alt", "Cruise, Jennifer Connelly, Miles Teller", "//input[@name='actor']", "XPATH"),
                 (21, "release year-alt", "2022", "//input[@name='release_year']", "XPATH"),
                 (22, "update", "UPDATE BUTTON", "button[type='submit']", "CSS_SELECTOR"),
                 (23, "login", "LOGIN", "//button[normalize-space()='Sign in'])[1]", "XPATH"),
                 (24, "login button", "LOGIN BUTTON", "button[type='submit']", "CSS_SELECTOR"),
                 (25, "username", "aya", "input[placeholder='Enter your username']", "CSS_SELECTOR"),
                 (26, "password", "123", "input[placeholder='Enter your password']", "CSS_SELECTOR"),
                 (27, "password-inco", "456", "input[placeholder='Enter your password']", "CSS_SELECTOR"),
                 (28, "username-inco", "ayaa", "input[placeholder='Enter your username']", "CSS_SELECTOR"),
                 (29, "login_", "LOGINn", "//img[@src='../static/log-in.png']", "XPATH")]

# btn_indicators = [(1, "http://127.0.0.1:5000/home", "ADD button", ".button", "CSS_SELECTOR"),
#                   (2, "http://127.0.0.1:5000/add_data", "ADD submit", "//button[normalize-space()='ADD']", "XPATH"),
#                   (3, "http://127.0.0.1:5000/alter_movie/", "update", "button[type='submit']", "CSS_SELECTOR"),
#                   (5, "http://127.0.0.1:5000", "login", "//img[@src='../static/log-in.png']", "XPATH"),
#                   (6, "http://127.0.0.1:5000/login", "login button", "button[type='submit']", "CSS_SELECTOR"),
#                   (7, "http://127.0.0.1:5000/movie_info/", "alter button", "//a[normalize-space()='alter']", "XPATH"),
#                   (8, "http://127.0.0.1:5000/movie_info/", "delete review", "//body/ol[2]/form[20]/button[1]", "XPATH"),
#                   (9, "http://127.0.0.1:5000/about_me","about",  "//img[@alt='logo']", "XPATH"),
#                   (10, "http://127.0.0.1:5000/movie_info/", "logo homepage", "img[alt='logo']", "CSS_SELECTOR"),
#                   (11, "http://127.0.0.1:5000/movie_info/","top button", "div[class='button']", "CSS_SELECTOR"),
#                   (15, "http://127.0.0.1:5000", "about","//img[@alt='logo']", "XPATH")]
#

# login_indicators = [(25, "username", "aya", "input[placeholder='Enter your username']", "CSS_SELECTOR"),
# (26, "password", "123", "input[placeholder='Enter your password']", "CSS_SELECTOR"),
# (27, "password-inco", "456", "input[placeholder='Enter your password']", "CSS_SELECTOR"),
# (28, "username-inco", "ayaa", "input[placeholder='Enter your username']", "CSS_SELECTOR")]

def sql_insert(con, entities):
    cursorObj = con.cursor()
    for entity in entities:
        id = entity[0]
        cursorObj.execute("SELECT * FROM data_indicators WHERE id = ?", (id,))
        data = cursorObj.fetchone()
        if data:
            cursorObj.execute("UPDATE data_indicators SET data_type = ?, content = ?, locator = ?, locator_type = ? WHERE id = ?", (entity[1], entity[2], entity[3], entity[4], id))
        else:
            cursorObj.execute("INSERT INTO data_indicators (id, data_type, content, locator, locator_type) VALUES (?, ?, ?, ?, ?)", entity)
    con.commit()

# def sql_insert_btn(con, entities):
#     cursorObj = con.cursor()
#     cursorObj.executemany("INSERT INTO btn_indicators (id, url, data_type, locator, locator_type) VALUES (?, ?, ?, ?, ?)", entities)
#     con.commit()
# # sql_insert_btn(con, my_indicators)
#

# def sql_insert_login(con, entities):
#     cursorObj = con.cursor()
#     cursorObj.executemany("INSERT INTO data_indicators (id, url, data_type, locator, locator_type) VALUES (?, ?, ?, ?, ?)", entities)
#     con.commit()


con = sqlite3.connect("movies_site.db")
sql_insert(con, my_indicators)

cursorObj = con.cursor()
cursorObj.execute("SELECT * FROM data_indicators")
rows = cursorObj.fetchall()
print(rows)


