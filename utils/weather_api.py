import requests
import json
from django.conf import settings
from django.core.cache import cache
from datetime import datetime, timedelta

class WeatherAPI:
    """Weather API integration using OpenWeatherMap"""
    
    def __init__(self):
        self.api_key = getattr(settings, 'OPENWEATHER_API_KEY', 'your_api_key_here')
        self.base_url = 'http://api.openweathermap.org/data/2.5'
        self.cache_timeout = 1800  # 30 minutes
    
    def get_current_weather(self, lat, lon):
        """Get current weather for a location"""
        # Skip cache entirely for now to avoid database cache issues
        # TODO: Re-enable cache once database cache issues are resolved
        pass
        
        url = f"{self.base_url}/weather"
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'en'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            weather_data = {
                'temperature': round(data['main']['temp']),
                'feels_like': round(data['main']['feels_like']),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
                'wind_direction': data['wind'].get('deg', 0),
                'visibility': data.get('visibility', 10000),
                'sunrise': datetime.fromtimestamp(data['sys']['sunrise']),
                'sunset': datetime.fromtimestamp(data['sys']['sunset']),
                'timestamp': datetime.now()
            }
            
            # Try to cache the data, but don't fail if cache is not available
            try:
                cache.set(cache_key, weather_data, self.cache_timeout)
            except Exception:
                # Cache not available, continue without caching
                pass
            return weather_data
            
        except requests.RequestException as e:
            print(f"Weather API error: {e}")
            return self._get_fallback_weather()
    
    def get_forecast(self, lat, lon, days=5):
        """Get 5-day weather forecast for a location"""
        cache_key = f"weather_forecast_{lat}_{lon}_{days}"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return cached_data
        
        url = f"{self.base_url}/forecast"
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'en'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            forecast_data = []
            current_date = None
            daily_data = {}
            
            for item in data['list']:
                date = datetime.fromtimestamp(item['dt']).date()
                
                if current_date != date:
                    if current_date and daily_data:
                        forecast_data.append(daily_data)
                    
                    current_date = date
                    daily_data = {
                        'date': date,
                        'day_name': date.strftime('%A'),
                        'temperature': {
                            'min': round(item['main']['temp_min']),
                            'max': round(item['main']['temp_max']),
                            'avg': round(item['main']['temp'])
                        },
                        'description': item['weather'][0]['description'],
                        'icon': item['weather'][0]['icon'],
                        'humidity': item['main']['humidity'],
                        'wind_speed': item['wind']['speed'],
                        'precipitation': item.get('rain', {}).get('3h', 0)
                    }
                else:
                    # Update min/max temperatures
                    daily_data['temperature']['min'] = min(daily_data['temperature']['min'], round(item['main']['temp_min']))
                    daily_data['temperature']['max'] = max(daily_data['temperature']['max'], round(item['main']['temp_max']))
            
            if daily_data:
                forecast_data.append(daily_data)
            
            # Limit to requested days
            forecast_data = forecast_data[:days]
            
            cache.set(cache_key, forecast_data, self.cache_timeout)
            return forecast_data
            
        except requests.RequestException as e:
            print(f"Weather forecast API error: {e}")
            return self._get_fallback_forecast(days)
    
    def get_weather_by_city(self, city_name, country_code='IN'):
        """Get weather by city name"""
        cache_key = f"weather_city_{city_name}_{country_code}"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return cached_data
        
        url = f"{self.base_url}/weather"
        params = {
            'q': f"{city_name},{country_code}",
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'en'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'coordinates': {
                    'lat': data['coord']['lat'],
                    'lon': data['coord']['lon']
                },
                'temperature': round(data['main']['temp']),
                'feels_like': round(data['main']['feels_like']),
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
                'timestamp': datetime.now()
            }
            
            # Try to cache the data, but don't fail if cache is not available
            try:
                cache.set(cache_key, weather_data, self.cache_timeout)
            except Exception:
                # Cache not available, continue without caching
                pass
            return weather_data
            
        except requests.RequestException as e:
            print(f"Weather city API error: {e}")
            return None
    
    def get_seasonal_recommendations(self, lat, lon):
        """Get seasonal travel recommendations based on weather"""
        current_weather = self.get_current_weather(lat, lon)
        
        if not current_weather:
            return []
        
        temp = current_weather['temperature']
        description = current_weather['description'].lower()
        
        recommendations = []
        
        # Temperature-based recommendations
        if temp < 15:
            recommendations.extend([
                'Wear warm clothing',
                'Perfect for hot beverages',
                'Great for indoor activities',
                'Consider visiting temples and heritage sites'
            ])
        elif temp < 25:
            recommendations.extend([
                'Pleasant weather for outdoor activities',
                'Perfect for sightseeing',
                'Good time for adventure sports',
                'Ideal for beach visits'
            ])
        else:
            recommendations.extend([
                'Stay hydrated',
                'Wear light clothing',
                'Best time for early morning activities',
                'Consider indoor attractions during peak hours'
            ])
        
        # Weather condition-based recommendations
        if 'rain' in description:
            recommendations.extend([
                'Carry an umbrella or raincoat',
                'Indoor activities recommended',
                'Roads might be slippery',
                'Perfect for photography with dramatic skies'
            ])
        elif 'cloud' in description:
            recommendations.extend([
                'Good lighting for photography',
                'Comfortable for outdoor activities',
                'Reduced UV exposure'
            ])
        elif 'clear' in description or 'sunny' in description:
            recommendations.extend([
                'Apply sunscreen',
                'Wear sunglasses and hat',
                'Great for outdoor photography',
                'Perfect for beach activities'
            ])
        
        return recommendations[:6]  # Return top 6 recommendations
    
    def _get_fallback_weather(self):
        """Fallback weather data when API is unavailable"""
        return {
            'temperature': 25,
            'feels_like': 27,
            'humidity': 65,
            'pressure': 1013,
            'description': 'Partly cloudy',
            'icon': '02d',
            'wind_speed': 10,
            'wind_direction': 180,
            'visibility': 10000,
            'sunrise': datetime.now().replace(hour=6, minute=0, second=0, microsecond=0),
            'sunset': datetime.now().replace(hour=18, minute=0, second=0, microsecond=0),
            'timestamp': datetime.now()
        }
    
    def _get_fallback_forecast(self, days=5):
        """Fallback forecast data when API is unavailable"""
        forecast = []
        for i in range(days):
            date = datetime.now().date() + timedelta(days=i)
            forecast.append({
                'date': date,
                'day_name': date.strftime('%A'),
                'temperature': {
                    'min': 20 + i,
                    'max': 30 + i,
                    'avg': 25 + i
                },
                'description': 'Partly cloudy',
                'icon': '02d',
                'humidity': 65,
                'wind_speed': 10,
                'precipitation': 0
            })
        return forecast

# Global weather API instance
weather_api = WeatherAPI()
