import { useEffect, useState } from 'react';

interface WeatherData {
  fact: {
    temp: number;
    feels_like: number;
    condition: string;
  };
}

const Weather = () => {
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);

  useEffect(() => {
    fetch('https://example.com')
      .then(response => response.json())
      .then(data => setWeatherData(data))
      .catch(error => console.error('Ошибка при получении данных:', error));
  }, []);

  if (!weatherData) return <div>Загрузка...</div>;

  return (
    <div>
      <h1>Погода в Москве</h1>
      <p>Температура: {weatherData.fact.temp}°C</p>
      <p>Ощущается как: {weatherData.fact.feels_like}°C</p>
      <p>Условия: {weatherData.fact.condition}</p>
    </div>
  );
};

export default Weather;