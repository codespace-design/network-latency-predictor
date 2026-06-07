# Network Latency Predictor

A machine learning-based web application that predicts network latency based on packet size using Linear Regression.

## Features

- Real-time latency prediction
- REST API support
- Batch CSV upload processing
- Interactive prediction dashboard
- Data visualization capabilities

## Tech Stack

- Python
- Django
- Django REST Framework
- Pandas
- Scikit-Learn

## Machine Learning Model

- Algorithm: Linear Regression
- Dataset Size: 5,000+ records
- Input: Packet Size (Bytes)
- Output: Predicted Latency (Milliseconds)

## Workflow

1. User submits packet size.
2. Backend processes request.
3. Linear Regression model predicts latency.
4. Results are returned via dashboard or API.

## API Features

### Single Prediction

```
POST /api/predict/
```

### Batch Prediction

```
Upload CSV file containing packet_size column
```

## Learning Outcomes

- Machine Learning integration
- REST API development
- Data preprocessing
- Batch prediction systems

## Future Enhancements

- Multiple network metrics
- Advanced ML algorithms
- Real-time monitoring
- Historical trend analysis
