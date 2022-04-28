from faker import Faker
from app.models import Entry, db

def generate_entries(how_many=10):
   fake = Faker()

   for i in range(how_many):
       post = Entry(
           title=fake.sentence(),
           body='\n'.join(fake.paragraphs(15)),
           is_published=True
       )
   print(post(i))
     #  db.session.add(post)
     #  db.session.commit()
   