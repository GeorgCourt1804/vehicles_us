# 🚗 Car Advertisement Data Viewer

A short program reflecting data on car advertisements
and generates, according to the user's choice, a histogram, scatter plot, or both.

---

## 📋 Description

An interactive web application built with **Stremlit** that loads and visualizes <br>
car advertisement data. Users can explore the dataset through dynamic charts, <br>
choosing to display a histogram, a scatter plot, or both simultaneously.

---

## 🛠️ Technologies Used

- **Python 3.14.3**
- **Pandas** - Data loading and manipulation
- **Plotly Express** - Interactive chart generation
- **Streamlit** - Web application framework

---

## 📁 Project Structure

```
project/
│
├── notebooks/
│   └── EDA.ipynb        # Exploratory Data Analysis
├── app.py               # Main application file
├── vehicles_us.csv      # Dataset with car advertisement data
├── requirements.txt     # Libraries needed for the project 
└── README.md            # Project documentation
```

---

## ⚙️ Installation

1. Clone or download this repository.
2. Install the required dependencies:

```bash
pip install pandas plotly streamlit
```

```conda
conda install anaconda::pandas
```

```conda
conda install conda-forge::streamlit
```

```conda
conda install plotly::plotly_express
```

3. Additionally, you will need to install an extra library (`nbformat`) to enable Plotly Express. Install it with: <br>

   ```conda
   conda install -n myenv nbformat
   ```

---

## 🚀 Usage

Run the application with the following command: <br>

```conda
streamlit run app.py
```

```bash
streamlit run app.py
```

---

## 📊 Features

- ✅ **Histogram** – Displays the distribution of the odometer column.
- ✅ **Scatter Plot** – Shows the relationship between odometer and price.
- ✅ Both charts can be displayed **simultaneously**.

---

## 📄 Dataset

The dataset `vehicles_us.csv` contains car advertisement data with the following key columns: <br>

| Column         | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `price`        | Listed price of the vehicle                                |
| `model_year`   | Year the vehicle model was manufactured                    |
| `model`        | Brand and model of the vehicle                             |
| `condition`    | Condition of the vehicle (good, excellent, fair, like new) |
| `cylinders`    | Number of engine cylinders                                 |
| `fuel`         | Fuel type (gas, diesel, etc.)                              |
| `odometer`     | Mileage of the vehicle                                     |
| `transmission` | Transmission type (automatic, manual)                      |
| `type`         | Vehicle type (SUV, sedan, pickup, etc.)                    |
| `paint_color`  | Exterior color of the vehicle                              |
| `is_4wd`       | Whether the vehicle is 4-wheel drive (1 = Yes)             |
| `date_posted`  | Date the advertisement was posted                          |
| `days_listed`  | Number of days the ad has been listed                      |

---

## 👤 Author

_GeorgCourt1804_
