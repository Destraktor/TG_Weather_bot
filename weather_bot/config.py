BOT_API_TOKEN = '6161665177:AAE2TZ6M9hYBAsAr7l-dJzOa8JTA5pjpkr4'
WEATHER_API_KEY = '8537d9ef6386cb97156fd47d832f479c'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)
