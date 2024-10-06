
# Sentiment Analysis on Product Reviews

This project performs sentiment analysis on product reviews. It analyzes a dataset of product reviews, builds a sentiment classification model, and predicts the sentiment (positive/negative) of reviews.

## Project Overview
This project uses machine learning techniques to classify the sentiment of product reviews. It takes a CSV dataset of product reviews as input, preprocesses the data, trains a model using supervised learning techniques, and outputs predictions of whether a review is positive or negative. The results of the prediction are stored in a CSV file.

## Project Structure
```
├── data/
│   ├── product_reviews.csv         # Input dataset containing product reviews
│   └── sentiment_predictions.csv   # Output file containing sentiment predictions
├── src/
│   └── sentiment_analysis.py       # Main script to perform sentiment analysis
├── create_and_query_product_reviews.sql  # SQL script to create and query the reviews database
├── requirements.txt                # List of required Python packages
├── README.md                       # This README file
```

## Requirements
To run the project, you'll need the following Python libraries:
- `pandas`
- `scikit-learn`
- `nltk`

These libraries are listed in the `requirements.txt` file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dataset
The input dataset `product_reviews.csv` should contain product reviews in text format. The dataset is loaded, preprocessed, and used for model training. It is expected to have at least the following structure:

```
| review_id | review_text          | rating |
|-----------|----------------------|--------|
| 1         | "Great product!"      | 5      |
| 2         | "Not worth the money" | 2      |
```

## How to Run

1. **Prepare the Dataset**: Ensure that the `product_reviews.csv` file is located in the `data/` directory.

2. **Run the Sentiment Analysis Script**:
   ```bash
   python src/sentiment_analysis.py
   ```

3. **View the Results**: After running the script, predictions will be saved in `data/sentiment_predictions.csv`. You can open this file to view the predicted sentiment labels.

## Model Training

The model uses `scikit-learn` and `nltk` libraries to preprocess the reviews and train a sentiment classifier. Here's an overview of the steps:

1. **Text Preprocessing**:
   - Tokenization
   - Stopword removal
   - Lemmatization

2. **Model**:
   - The model is a supervised classification model trained on labeled review data, which classifies reviews as positive or negative.

3. **Evaluation**:
   - The performance of the model is evaluated using standard metrics like accuracy, precision, recall, and F1-score.

## Results

The predicted sentiment for each review is saved in the `sentiment_predictions.csv` file, with the following structure:

```
| review_id | review_text          | predicted_sentiment |
|-----------|----------------------|---------------------|
| 1         | "Great product!"      | positive            |
| 2         | "Not worth the money" | negative            |
```

## Future Improvements
- **More granular sentiment categories**: Instead of just positive and negative, consider adding neutral sentiment classification.
- **Improving the model**: Experiment with advanced machine learning models like LSTM or transformers for better accuracy.
- **Data augmentation**: Add more diverse reviews to improve the model's generalization.


## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please follow the code of conduct when contributing.
