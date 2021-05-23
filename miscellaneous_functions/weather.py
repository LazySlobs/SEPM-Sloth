# Python program to find current weather details of any city using openweathermap api

# import required modules
import requests, json
from core.speak import voice_assistant_speak


class Current_Weather():

  def __init__(self,city_name):
        self.city_name = city_name

  current_temperature, feel_like,min_temperature, max_temperature, current_pressure, current_humidiy, weather_description = 0, 0, 0, 0, 0, 0, "nothing"
  wind_speed, wind_deg, cloud_value = 0, 0, 0
  city, country = "none", "none"

  def check_city_weather(self):

    # API key
    API_KEY = "c2bafd1b243e168a21ba31492ed247bb"

    # base_url variable to store url
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

    # complete_url variable to store complete url address
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + self.city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise, city is not found
    if x["cod"] != "404":

        # store the value of "main" key in variable y
        y = x["main"]

        # store the value corresponding to the "temp" key of y
        self.current_temperature = y["temp"]

        # store the value corresponding to the "min temp" key of y
        self.min_temperature = y["temp_min"]

        # store the value corresponding to the "max temp" key of y
        self.max_temperature = y["temp_max"]

        # store the value corresponding to the "pressure" key of y
        self.current_pressure = y["pressure"]

        # store the value corresponding to the "humidity" key of y
        self.current_humidiy = y["humidity"]

        # store the value corresponding to the "feel_like" key of y
        self.feel_like = y["feels_like"]

        # store the value of "weather" key in variable z
        z = x["weather"]

        # store the value corresponding to the "description" key at the 0th index of z
        self.weather_description = z[0]["description"]

        # store the value of "wind" key in variable a
        a = x["wind"]

        # store the value of "wind speed" key in variable a
        self.wind_speed = a["speed"]

        # store the value of "wind degree" key in variable a
        self.wind_deg = a["deg"]

        # store the value of "cloud" key in variable c
        self.cloud_value = x["clouds"]["all"]

        # store the value of "country" key in variable c
        self.country = x["sys"]["country"]

        # store the value of "city" key in variable c
        self.city = x["name"]

        return True
    else:
        return False



  def display_weather_console(self):
    if self.check_city_weather():
       # print following values
       print("Temperature (in kelvin unit) = " +
            str(self.current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(self.current_pressure) +
              "\n humidity (in percentage) = " +
              str(self.current_humidiy) +
              "\n description = " +
              str(self.weather_description))
       temp_in_C = self.current_temperature - 273.15
       message = "Current temperature is " + str(int(temp_in_C)) + "degree Celsius and we have" + str(
            self.weather_description) + "."
       voice_assistant_speak(message, "en")
    else:
      print("City not found")

  def display_weather_results(self):
    if self.check_city_weather():
       # return values
       return [self.current_temperature - 273.15, self.current_pressure, self.current_humidiy, self.weather_description,
               self.feel_like - 273.15, self.max_temperature - 273.15, self.min_temperature - 273.15,
               self.wind_speed, self.wind_deg, self.cloud_value,
               self.city, self.country]
    else:
      return 0


if __name__ == '__main__':
	Current_Weather()