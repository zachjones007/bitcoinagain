#printpage

# Import necessary modules and functions
from part1 import get_weather_data
from part2 import fetch_bitcoin_data, analyze_sentiment, calculate_rsi, assign_sentiment_scores, create_label_column, create_feature_dataset, fill_missing_values, drop_missing_values, split_dataset, create_logistic_regression_model, train_logistic_regression_model, test_logistic_regression_model, predict_next_day_label
from part3 import determine_market_outlook

def print_part1():
    # Print status message
    print("Getting weather data...")

    # Get current weather data from OpenWeather API
    data = get_weather_data()

    # Print weather data
    print("Temperature:", data['temperature'], "degrees Fahrenheit")
    print("Conditions:", data['conditions'])
    print("Humidity:", data['humidity'])
    print("Wind speed:", data['wind_speed'])

def print_part2():
    # Print status message
    print("Fetching Bitcoin data...")

    # Fetch historical data for Bitcoin
    data = fetch_bitcoin_data()

    if not data.empty:
        # Analyze the sentiment of the statements made by the Federal Reserve
        print("Analyzing sentiment of Federal Reserve statements...")
        sentiment_scores = analyze_sentiment()

        # Add RSI column
        print("Calculating RSI...")
        data = calculate_rsi(data)

        # Assign sentiment scores to the historical data DataFrame
        print("Assigning sentiment scores to data...")
        data = assign_sentiment_scores(data, sentiment_scores)

        # Create a new column for the label, 1 for an increase in price and 0 for a decrease
        print("Creating label column...")
        data = create_label_column(data)

        # Create a feature dataset, dropping unnecessary columns
        print("Creating feature dataset...")
        features = create_feature_dataset(data)

        # Fill missing values with mean
        print("Filling missing values with mean...")
        features = fill_missing_values(features)

        # Drop rows with missing values
        print("Dropping rows with missing values...")
        features = drop_missing_values(features)

        # Split the dataset into training and testing sets
        print("Splitting dataset into training and testing sets...")
        X_train, X_test, y_train, y_test = split_dataset(features, data['label'])

        # Create a logistic regression model
        print("Creating logistic regression model...")
        log_reg = create_logistic_regression_model()

        # Train the model on the training data
        print("Training logistic regression model...")
        log_reg = train_logistic_regression_model(log_reg, X_train, y_train)

        # Test the model's performance on the testing data
        print("Testing logistic regression model...")
        accuracy = test_logistic_regression_model(log_reg, X_test, y_test)
        print("Accuracy: ", accuracy)

        # Predict the next day's label using the logistic regression model
        print("Predicting next day's label...")
        next_day_label = predict_next_day_label(data, sentiment_scores, log_reg)

def print_part3():
    # Determine market outlook based on predicted label
    print("Determining market outlook based on predicted label...")
    determine_market_outlook()

# Run print functions for each part
print_part1()
print_part2()
print_part3()
