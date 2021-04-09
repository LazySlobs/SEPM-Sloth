# Python program to find current news details of any country and category using newsapi api

import requests, json
from core.speak import voice_assistant_speak

def read_news_headlines(category, country):
	# For list of available categories and countries, visit https://newsapi.org/docs/endpoints/sources

	# API key
	api_key = "53d2c04adf064905b28bb0535896d44c"

	# base_url variable to store url
	base_url = "https://newsapi.org/v2/top-headlines?"

	# complete_url variable to store complete url address
	complete_url = base_url + "category=" + category + "&country=" + country + "&apiKey=" + api_key

	try:
		response = requests.get(complete_url)
	except:
		print("Unable to access link, please check your Internet ")

	news = json.loads(response.text)

	i = 0 # to get 3 top headlines only
	for article in news['articles']:
		if i < 3:
			title = str(article['title'])
			# description = str(article['description'])
			# print(title)
			# print(description)
			voice_assistant_speak(title, "en")
		else:
			break
		i = i + 1
