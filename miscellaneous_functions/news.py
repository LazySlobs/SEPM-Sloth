# Python program to find current news details of any country and category using newsapi api

import requests, json
import speech_recognition as sr
from core.listen import record_audio
from core.speak import voice_assistant_speak
import settings

def read_news_headlines_process(r, voice_data):
	countries = ['America', 'India', 'China', 'Japan', 'Korea', 'Singapore', 'Malaysia', 'Thailand', 'Indonesia']
	country = "us"
	if "America" in voice_data or "The US" in voice_data or "USA" in voice_data or "United States of America" in voice_data:
		country = "us"
	elif "India" in voice_data:
		country = "in"
	elif "Australia" in voice_data or "oz" in voice_data or "AU" in voice_data:
		country = "au"
	elif "China" in voice_data:
		country = "cn"
	elif "Japan" in voice_data:
		country = "jp"
	elif "Korea" in voice_data:
		country = "kr"
	elif "Singapore" in voice_data:
		country = "sg"
	elif "Malaysia" in voice_data:
		country = "my"
	elif "Thailand" in voice_data:
		country = "th"
	elif "Indonesia" in voice_data or "Indo" in voice_data:
		country = "id"
	else:
		while voice_data not in countries:
			voice_data2, language = record_audio(r, language='en', ask="Sorry, this country is not supported. Would you like to know the supported countries?")
			if "yes" in voice_data2:
				voice_data3, language = record_audio(r, language='en', ask="We support America, India, China, Japan, Korea, Singapore, Malaysia, Thailand, Indonesia. Which country would you like to check?")
				if voice_data3 not in countries:
					continue
				else:
					if "America" in voice_data3 or "The US" in voice_data3 or "USA" in voice_data3 or "United States of America" in voice_data3:
						country = "us"
					elif "India" in voice_data3:
						country = "in"
					elif "Australia" in voice_data3 or "oz" in voice_data3 or "AU" in voice_data3:
						country = "au"
					elif "China" in voice_data3:
						country = "cn"
					elif "Japan" in voice_data3:
						country = "jp"
					elif "Korea" in voice_data3:
						country = "kr"
					elif "Singapore" in voice_data3:
						country = "sg"
					elif "Malaysia" in voice_data3:
						country = "my"
					elif "Thailand" in voice_data3:
						country = "th"
					elif "Indonesia" in voice_data3 or "Indo" in voice_data3:
						country = "id"
			elif "no" in voice_data2:
				voice_data3, language = record_audio(r, language='en', ask='Which country would you like to check from?')
				if voice_data3 not in countries:
					continue
				else:
					break
			else:
				continue
	
	categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
	category, language = record_audio(r, language='en', ask='Which category would you like to check?')
	category.lower()
	print("category = " + category)

	if category in categories:
		read_news_headlines(category, country)
	else:
		while True:
			voice_data2 = record_audio(r, language='en', ask="Sorry, this category is not available. Would you like to know the available categories?")
			if "yes" in voice_data2:
				category, language = record_audio(r, language='en', ask="We have general, business, entertainment, health, science, sports, technology. Which category would you like to check?")
				if category not in categories:
					continue
				else:
					read_news_headlines(category, country)
			elif "no" in voice_data2:
				category, language = record_audio(r, language='en', ask='Which category would you like to check?')
				if category not in categories:
					continue
				else:
					read_news_headlines(category, country)
			else:
				continue


def read_news_headlines_ask():
	r = sr.Recognizer() # create a recognizer object to recognize texts
	r.energy_threshold = settings.energy_threshold

	category, language = record_audio(r, language='en', ask='Which category would you like to check?')
	
	categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
	category.lower()
	print("category = " + category)

	if category not in categories:
		while True:
			voice_data2 = record_audio(r, language='en', ask="Sorry, this category is not available. Would you like to know the available categories?")
			if "yes" in voice_data2:
				category, language = record_audio(r, language='en', ask="We have general, business, entertainment, health, science, sports, technology. Which category would you like to check?")
				if category not in categories:
					continue
				else:
					break
			elif "no" in voice_data2:
				category, language = record_audio(r, language='en', ask='Which category would you like to check?')
				if category not in categories:
					continue
				else:
					break
			else:
				continue
	
	voice_data, language = record_audio(r, language='en', ask='And from which country would you like to check from?')
	print("voice_data = " + voice_data)

	countries = ['America', 'India', 'China', 'Japan', 'Korea', 'Singapore', 'Malaysia', 'Thailand', 'Indonesia']
	if "America" in voice_data or "The US" in voice_data or "USA" in voice_data or "United States of America" in voice_data:
		country = "us"
	elif "India" in voice_data:
		country = "in"
	elif "Australia" in voice_data or "oz" in voice_data or "AU" in voice_data:
		country = "au"
	elif "China" in voice_data:
		country = "cn"
	elif "Japan" in voice_data:
		country = "jp"
	elif "Korea" in voice_data:
		country = "kr"
	elif "Singapore" in voice_data:
		country = "sg"
	elif "Malaysia" in voice_data:
		country = "my"
	elif "Thailand" in voice_data:
		country = "th"
	elif "Indonesia" in voice_data or "Indo" in voice_data:
		country = "id"
	else:
		while voice_data not in countries:
			voice_data2, language = record_audio(r, language='en', ask="Sorry, this country is not supported. Would you like to know the supported countries?")
			if "yes" in voice_data2:
				voice_data3, language = record_audio(r, language='en', ask="We support America, India, China, Japan, Korea, Singapore, Malaysia, Thailand, Indonesia. Which country would you like to check?")
				if voice_data3 not in countries:
					continue
				else:
					if "America" in voice_data3 or "The US" in voice_data3 or "USA" in voice_data3 or "United States of America" in voice_data3:
						country = "us"
					elif "India" in voice_data3:
						country = "in"
					elif "Australia" in voice_data3 or "oz" in voice_data3 or "AU" in voice_data3:
						country = "au"
					elif "China" in voice_data3:
						country = "cn"
					elif "Japan" in voice_data3:
						country = "jp"
					elif "Korea" in voice_data3:
						country = "kr"
					elif "Singapore" in voice_data3:
						country = "sg"
					elif "Malaysia" in voice_data3:
						country = "my"
					elif "Thailand" in voice_data3:
						country = "th"
					elif "Indonesia" in voice_data3 or "Indo" in voice_data3:
						country = "id"
					read_news_headlines(category, country)
					break
			elif "no" in voice_data2:
				voice_data3, language = record_audio(r, language='en', ask='Which country would you like to check from?')
				if voice_data3 not in countries:
					continue
				else:
					if "America" in voice_data3 or "The US" in voice_data3 or "USA" in voice_data3 or "United States of America" in voice_data3:
						country = "us"
					elif "India" in voice_data3:
						country = "in"
					elif "Australia" in voice_data3 or "oz" in voice_data3 or "AU" in voice_data3:
						country = "au"
					elif "China" in voice_data3:
						country = "cn"
					elif "Japan" in voice_data3:
						country = "jp"
					elif "Korea" in voice_data3:
						country = "kr"
					elif "Singapore" in voice_data3:
						country = "sg"
					elif "Malaysia" in voice_data3:
						country = "my"
					elif "Thailand" in voice_data3:
						country = "th"
					elif "Indonesia" in voice_data3 or "Indo" in voice_data3:
						country = "id"
					read_news_headlines(category, country)
					break
			else:
				continue


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
		print("Unable to access link, please check your Internet")
		voice_assistant_speak("Unable to access link, please check your Internet")


	news = json.loads(response.text)

	i = 0 # to get 3 top headlines only
	for article in news['articles']:
		if i < 3:
			title = str(article['title'])
			# description = str(article['description'])
			# print(title)
			# print(description)
			voice_assistant_speak(title)
		else:
			break
		i = i + 1