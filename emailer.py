#! /user/bin/python

import os
import psycopg2
import urlparse

from postmark import PMMail

# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

conn = psycopg2.connect(
    database="capsule",
    user="capsule",
    password="capsule",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()

def create_email():
    _to = "andrewjshum@gmail.com"
    _from = "andrewshum@mit.edu"

    cur.execute("SELECT * FROM app_memory ORDER BY random() LIMIT 1")
    _, author_id, date, body, to = cur.fetchone()

    html = """\
    <html>
        <head></head>
        <body>
            <p>%s</p>
            <p>%s</p>
            <p>%s</p>
        </body>
    </html>
    """ % (to, body, author_id)

    message = PMMail(api_key = os.environ.get('POSTMARK_API_KEY'),
                 subject = "Hello from Postmark",
                 sender = "leonard@bigbangtheory.com",
                 to = _to,
                 text_body = "Hello",
                 tag = "hello")

    message.send()


if __name__ == "__main__":
    create_email()
