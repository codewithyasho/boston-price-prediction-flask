# 🏠 Boston House Price Prediction

A machine learning web application that predicts house prices in Boston using XGBoost algorithm. The application features a beautiful, responsive web interface built with Flask, Bootstrap, and custom CSS.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Model Features](#model-features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **🎯 Accurate Predictions**: Uses XGBoost machine learning model for precise house price predictions
- **🎨 Beautiful UI**: Modern, responsive web interface with gradient backgrounds and glass morphism design
- **📱 Mobile Friendly**: Fully responsive design that works on all devices
- **🔧 Easy to Use**: Intuitive form with helpful descriptions for each input field
- **⚡ Fast Performance**: Quick predictions with real-time results
- **🌐 REST API**: JSON API endpoint for programmatic access
- **📊 Feature Scaling**: Automatic data preprocessing with StandardScaler

## 🚀 Demo

### Web Interface
The application provides an elegant web interface where users can input property details:

- **Crime Rate (CRIM)**: Per capita crime rate by town
- **Residential Zone (ZN)**: Proportion of residential land zoned for lots over 25,000 sq.ft.
- **Industrial Area (INDUS)**: Proportion of non-retail business acres per town
- **Charles River (CHAS)**: Charles River dummy variable (1 if tract bounds river; 0 otherwise)
- **NOX Concentration**: Nitric oxides concentration (parts per 10 million)
- **Rooms (RM)**: Average number of rooms per dwelling
- **Age (AGE)**: Proportion of owner-occupied units built prior to 1940
- **Distance (DIS)**: Weighted distances to employment centres
- **Highway Access (RAD)**: Index of accessibility to radial highways
- **Tax Rate (TAX)**: Full-value property-tax rate per $10,000
- **Pupil-Teacher Ratio (PTRATIO)**: Pupil-teacher ratio by town
- **B Value (B)**: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- **Lower Status (LSTAT)**: % lower status of the population

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/codewithyasho/boston-price-prediction-flask
cd boston-price-prediction-flask
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Model Files

Ensure the following model files are present in the project directory:
- `xgboost_model.pkl` - Pre-trained XGBoost model
- `boston_housing_scaler.pkl` - StandardScaler for feature preprocessing

## 🚀 Usage

### Running the Application

1. **Start the Flask Server**:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. **Make Predictions**:
   - Fill in the property details in the web form
   - Click "Predict House Price"
   - View the predicted price in thousands of dollars

### Example Input Values

For testing, you can use these sample values:
- CRIM: 0.00632
- ZN: 18.0
- INDUS: 2.31
- CHAS: 0
- NOX: 0.538
- RM: 6.575
- AGE: 65.2
- DIS: 4.09
- RAD: 1
- TAX: 296
- PTRATIO: 15.3
- B: 396.9
- LSTAT: 4.98

## 🔌 API Endpoints

### Web Interface
- **GET** `/` - Home page with prediction form

### Prediction Endpoints
- **POST** `/predict` - Form-based prediction (returns HTML)
- **POST** `/predict_api` - JSON API prediction (returns JSON)

### API Usage Example

```bash
curl -X POST http://localhost:5000/predict_api \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "CRIM": 0.00632,
      "ZN": 18.0,
      "INDUS": 2.31,
      "CHAS": 0,
      "NOX": 0.538,
      "RM": 6.575,
      "AGE": 65.2,
      "DIS": 4.09,
      "RAD": 1,
      "TAX": 296,
      "PTRATIO": 15.3,
      "B": 396.9,
      "LSTAT": 4.98
    }
  }'
```

## 📁 Project Structure

```
boston-housing/
│
├── app.py                          # Main Flask application
├── xgboost_model.pkl              # Pre-trained XGBoost model
├── boston_housing_scaler.pkl      # StandardScaler for preprocessing
├── HousingData.csv                # Training dataset
├── main.ipynb                     # Jupyter notebook for model development
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
│
├── templates/
│   └── index.html                 # HTML template with modern UI
│
└── static/                        # Static files directory
```

## 🔍 Model Features

The model uses 13 features from the Boston Housing dataset:

| Feature | Description | Type |
|---------|-------------|------|
| CRIM | Per capita crime rate by town | Continuous |
| ZN | Proportion of residential land zoned for lots over 25,000 sq.ft. | Continuous |
| INDUS | Proportion of non-retail business acres per town | Continuous |
| CHAS | Charles River dummy variable | Binary (0/1) |
| NOX | Nitric oxides concentration (parts per 10 million) | Continuous |
| RM | Average number of rooms per dwelling | Continuous |
| AGE | Proportion of owner-occupied units built prior to 1940 | Continuous |
| DIS | Weighted distances to employment centres | Continuous |
| RAD | Index of accessibility to radial highways | Continuous |
| TAX | Full-value property-tax rate per $10,000 | Continuous |
| PTRATIO | Pupil-teacher ratio by town | Continuous |
| B | 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town | Continuous |
| LSTAT | % lower status of the population | Continuous |

## 🛠️ Technologies Used

### Backend
- **Python 3.7+** - Programming language
- **Flask** - Web framework
- **XGBoost** - Machine learning algorithm
- **scikit-learn** - Data preprocessing and model utilities
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation
- **Joblib** - Model serialization

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling with custom animations and gradients
- **Bootstrap 5.3.0** - CSS framework for responsive design
- **Font Awesome 6.0** - Icons
- **Google Fonts (Poppins)** - Typography
- **JavaScript** - Bootstrap interactions

### Design Features
- **Glass Morphism** - Modern design trend with transparency effects
- **Gradient Backgrounds** - Beautiful color transitions
- **Responsive Design** - Mobile-first approach
- **Custom Animations** - Smooth hover and focus effects

## 📊 Model Performance

The XGBoost model has been trained and optimized for predicting house prices with high accuracy. The model includes:

- **Feature Scaling**: StandardScaler preprocessing for optimal performance
- **Cross Validation**: Model validated using cross-validation techniques
- **Hyperparameter Tuning**: Optimized parameters for best performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Boston Housing dataset from UCI Machine Learning Repository
- XGBoost for the powerful gradient boosting framework
- Flask community for the excellent web framework
- Bootstrap team for the responsive CSS framework

## 📞 Contact

If you have any questions, feel free to reach out:

- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)
- **Email**: your.email@example.com

---

⭐ **Star this repository if you found it helpful!**
