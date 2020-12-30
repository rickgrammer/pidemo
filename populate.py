import random
import pymongo
from faker import Faker

faker = Faker()

boards = ['CBSE', 'ICSE', 'state']

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.smqmf.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

def add_books(n=10):
    c_books = db['books']
    c_chapters = db['chapters']
    c_sections = db['sections']

    c_books.drop()
    c_chapters.drop()
    c_sections.drop()

    for i in range(1, n+1):
        chapters = random.randint(6,30)

        book = {
            'book_id': i,
            'book_title': faker.word() + ' ' + faker.word(),
            'board': random.choice(boards),
            'chapter_ids': list(range(1, chapters+1))
        }
        c_books.insert_one(book)

        for j in range(1, chapters+1):
            sections = random.randint(5,10)
            chapter = {
                'book_id': i,
                'chapter_id': j,
                'chapter_name': 'CHAPTER: ' + faker.word() + ' ' + faker.word(),
                'section_ids': list(range(1, sections+1))
            }
            c_chapters.insert_one(chapter)
        
            for k in range(1, sections):
                section = {
                    'book_id': i,
                    'chapter_id': j,
                    'section_id': k,
                    'section_name': 'SECTION: ' + faker.word() + ' ' + faker.word(),
                    'section_text': '\n'.join(faker.text() for i in range(30))
                }
                c_sections.insert_one(section)


if __name__ == '__main__':
    add_books(10)
