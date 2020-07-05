"""
Mini projet Twitter

Etape 4:
Mettez sqlite et mongodb l'auteur, la date du tweet, le tweet, le nombre de mots du tweet, la liste de mots sans les stopwords

Run: python3 create_db_sql.py
"""
import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect('twitter_db.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
    print('Database Created and Successful Connected to SQLite')

    # Create table - TWEET_MUNICIPALES
    conn.execute('''CREATE TABLE IF NOT EXISTS TWEETS
                ([twitter_id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [username] VARCHAR NOT NULL, 
                [date] DATE, 
                [text] VARCHAR NOT NULL, 
                [word_number] INT NOT NULL, 
                [no_stop_words] VARCHAR NOT NULL)''')
                    
    conn.commit()
    print("SQLite table created")

    conn.close()
    print("The SQLite connection is closed !")
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if(conn):
        conn.close()
        print("The SQLite connection is closed !")


tweet_data = pd.read_csv('df_tweet.csv', index_col=0)

conn = sqlite3.connect('twitter_db.db')
# Insert the values from the dataframe into the table 'TWEET_MUNICIPALES'
tweet_data.to_sql('TWEETS', con=conn, if_exists='append', index = False)

conn.execute('''SELECT * FROM TWEETS''').fetchall()