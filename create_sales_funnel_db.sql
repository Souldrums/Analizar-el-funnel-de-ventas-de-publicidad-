CREATE DATABASE spotify_ads_funnel;

USE spotify_ads_funnel;

CREATE TABLE opportunities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    opportunity_name VARCHAR(255),
    stage VARCHAR(50),
    region VARCHAR(100),
    amount DECIMAL(10,2),
    won BOOLEAN
);
