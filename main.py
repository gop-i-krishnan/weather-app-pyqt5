import sys

import requests
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QLineEdit
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Get Weather",self)
        self.temperature_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description=QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.resize(400, 500)

        vbox = QVBoxLayout()

        # Configure input box with placeholder text
        self.city_input.setPlaceholderText("Enter your city name...")
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description)

        self.setLayout(vbox)

        # Alignments
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)

        # Assign object names for styling
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.get_weather_button.setObjectName("get_weather_button")
        self.emoji_label.setObjectName("emoji_label")
        self.description.setObjectName("description")

        # StyleSheet for UI
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }
            QLineEdit#city_input {
                font-size: 16px;
                padding: 10px;
                border: 2px solid #2C3E50;
                border-radius: 8px;
                color: #34495E;
                background-color: #ECF0F1;
            }
            QLineEdit::placeholder {
                color: #95A5A6;
            }
            QPushButton#get_weather_button {
                font-size: 20px;
                font-weight: bold;
                padding: 10px;
                background-color: #3498DB;
                color: #FFFFFF;
                border-radius: 8px;
            }
            QLabel#temperature_label {
                font-size: 48px;
                color: #E74C3C;
            }
            QLabel#emoji_label {
                font-size: 80px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description {
                font-size: 20px;
                color: #2ECC71;
            }
        """)

        # Connect the button to the weather fetching function
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "ab7853151001b753fd442eec33e500c3"
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:

            response=requests.get(url)
            response.raise_for_status()
            data=response.json()

            if data["cod"]==200:
                self.display_weather(data)
            else:
                self.display_error(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid api key ")
                case 403:
                    self.display_error("Forbidden:\nAccess is Denied")
                case 404:
                    self.display_error("Not Found:\nCity Not Found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response form the server")
                case _:
                    self.display_error(f"HTTP Error occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nCheck your Internet Connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirect:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error:{req_error}")

    def display_error(self,message):
        self.temperature_label.setStyleSheet("""font-size:30px;""")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description.clear()

    def display_weather(self,data):
        self.temperature_label.setStyleSheet("""
                    font-size:75px;

                """)
        temperature_k=data["main"]["temp"]
        temperature_c=temperature_k-273.15
        temperature_f=(temperature_k* 9/5) - 459.67
        weather_id=data["weather"][0]["id"]
        weather_description=data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_c:0.2f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description.setText(f"{weather_description}")

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id < 300:  # Thunderstorm
            return "⛈️"  # Thunderstorm with rain
        elif 300 <= weather_id < 400:  # Drizzle
            return "🌦️"  # Drizzle
        elif 500 <= weather_id < 600:  # Rain
            if weather_id == 511:  # Freezing rain
                return "❄️🌧️"  # Snowflake with rain
            return "🌧️"  # Rain
        elif 600 <= weather_id < 700:  # Snow
            return "❄️"  # Snow
        elif 700 <= weather_id < 800:  # Atmosphere (mist, smoke, etc.)
            return "🌫️"  # Fog or mist
        elif weather_id == 800:  # Clear sky
            return "☀️"  # Sunny
        elif 801 <= weather_id < 900:  # Clouds
            if weather_id == 801:  # Few clouds
                return "🌤️"  # Sun behind small clouds
            elif weather_id == 802:  # Scattered clouds
                return "⛅"  # Sun behind clouds
            elif weather_id == 803:  # Broken clouds
                return "🌥️"  # Sun behind large clouds
            elif weather_id == 804:  # Overcast clouds
                return "☁️"  # Cloudy
        else:
            return "❓"  # Unknown weather condition


def main():
    app=QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()