** RealEstate-API**
This project is for predicting real estate prices in Hyderabad. It comprises four main components:

**Data Scraping**
The hydmodel.py script uses Selenium and BeautifulSoup to scrape property listings from MagicBricks. It extracts key details like property title, price, location, number of BHK, and square footage, then saves the data to a CSV file (hyderabad_housing_data.csv).

**Data Preprocessing**
The hprocess.py script loads the raw scraped data and performs cleaning and feature engineering:

Fills missing numeric values (e.g., Price, BHK, Square Feet) using the median.
Fills missing categorical values (e.g., Title, Location) using the mode.
One-hot encodes categorical variables.
Normalizes numeric features using StandardScaler.
Saves the processed data to processed_hyderabad_housing.csv.

**Model Training**
The htrain.py script takes the preprocessed data, splits it into training and testing sets, and trains a linear regression model to predict property prices (target: Price).

It saves the trained model as hyderabad_realestatemodel.pkl.
It also extracts the feature order (i.e., the list of predictor columns) and saves it as feature_order.csv for later use in the API.

**API Deployment**
The hapi.py script provides a Flask-based REST API that loads the trained model and feature order, receives JSON input (with features matching the training data), and returns a predicted house price.

Requriments:
Python – Main programming language
Selenium & BeautifulSoup – For web scraping
Pandas & Scikit-learn – For data processing and machine learning
Flask – For building the REST API
Joblib – For saving/loading the trained model

