from faker import Faker

def fake_articles():
	fake = Faker()
	articles = {}
	for i in range(10):
		articles[i] = {
			"id": i,
			"author": fake.name(),
			"title": fake.sentence(),
			"description": fake.text()
		}
	return articles

if __name__ == "__main__":
	print(fake_articles())