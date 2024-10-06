-- Create table for product reviews
CREATE TABLE product_reviews (
    ReviewID INT PRIMARY KEY,
    ProductID INT,
    Review TEXT,
    Sentiment VARCHAR(10)
);

-- Insert data into product_reviews table
-- I'm just using sample inputs for testing. You can replace with your actual data insertions
INSERT INTO product_reviews (ReviewID, ProductID, Review, Sentiment) VALUES 
(1, 101, 'This product is amazing! I loved it.', 'positive'),
(2, 102, 'Not worth the money. Very disappointing.', 'negative'),
(3, 103, 'Average quality, nothing special.', 'neutral'),
(4, 104, 'Excellent value for money!', 'positive'),
(5, 105, 'Poor build quality.', 'negative'),
(6, 106, 'Great product, highly recommend.', 'positive'),
(7, 107, 'Terrible customer service.', 'negative'),
(8, 108, 'Five stars! Very satisfied.', 'positive'),
(9, 109, 'The product stopped working after a week.', 'negative'),
(10, 110, 'Happy with the purchase, will buy again.', 'positive');

-- Query to select data for analysis
SELECT 
    ReviewID,
    ProductID,
    Review,
    Sentiment
FROM 
    product_reviews;
