# Bluebird Weather App 🌤️

A Python script that fetches and displays **current weather information** for a user-specified city using the [OpenWeatherMap API](https://openweathermap.org/api).  
Demonstrates **API calls, JSON parsing, error handling, and terminal output formatting**.

---

## Features
- Enter a city (and state/country optionally) to fetch current weather  
- Displays:
  - Temperature  
  - “Feels like” temperature  
  - Humidity  
  - Wind speed (and gusts if available)  
  - Weather description (e.g., “Clear Sky”)  
- Handles invalid or unrecognized locations gracefully  
- Easy to expand (e.g., 5-day forecast or multiple cities)  

---

## Requirements
- Python 3.8+  
- Standard libraries: `urllib`, `json`, `datetime`

---

## Usage
1. Clone the repository:
```bash
git clone https://github.com/h0dg/bluebird.git
cd bluebird
```
2. Run the script:
```bash
python bluebird.py
```
3. Enter a city (and option state/country) when prompted:
```bash
Enter a city and state, separated by a comma (ex: Denver, CO): Denver, CO
```
4. Example output:
```bash
Currently in Denver, CO, US:
72 degrees F with a real feel of 70 degrees F
Wind speed is 5 MPH
Weather condition: Clear Sky
```

---

## Future Improvements
- Add 5-day or 7-day forecast
- Accept multiple cities in one run
- Convert temperatures between Celsius and Fahrenheit
- Deploy as a web app using Flask

