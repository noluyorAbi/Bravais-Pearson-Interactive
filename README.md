# 📊 Bravais-Pearson Interactive

An interactive web application to visualize the **Pearson correlation coefficient (r)** using **Streamlit**. The app generates **linear, nonlinear, and random datasets**, calculates correlation values, and provides graphical representations with regression lines.

🔗 **Live Demo:** [Bravais-Pearson Interactive](https://myuninotes-bp.streamlit.app/)  
🔗 **GitHub Repository:** [noluyorAbi/Bravais-Pearson-Interactive](https://github.com/noluyorAbi/Bravais-Pearson-Interactive)

## 📌 Features

- 📈 **Visualize Linear, Quadratic, and Random Relationships**  
- 🔢 **Interactive Parameter Controls** for correlation strength, noise, and sample size  
- 🧮 **Manually Implemented Pearson Correlation Calculation**  
- 🏹 **Real-time Scatter Plots with Regression Lines**  
- 📊 **Statistical Metrics:** Pearson’s r, \( r^2 \) (coefficient of determination), and p-value  
- 🎨 **Seaborn & Matplotlib Styling for Clean Data Visualization**  

## 🚀 Installation

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/noluyorAbi/Bravais-Pearson-Interactive.git
cd Bravais-Pearson-Interactive
```

2️⃣ **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🎯 Usage

Run the Streamlit app:
```bash
streamlit run interactive.py
```

## 🖥️ Project Structure

```
.
├── examples.py          # Example scripts for correlation calculations
├── interactive.py       # Main Streamlit application
└── requirements.txt     # Dependencies for the project
```

## 📚 Pearson Correlation Formula

The **Pearson correlation coefficient (r)** is a measure of the **linear relationship** between two variables:

\[
r = \frac{n \sum xy - (\sum x)(\sum y)}{\sqrt{(n \sum x^2 - (\sum x)^2)\,(n \sum y^2 - (\sum y)^2)}}
\]

**Interpretation of r:**
- **\( r = 1 \):** Perfect positive correlation
- **\( r = -1 \):** Perfect negative correlation
- **\( r = 0 \):** No correlation

## 🛠 Dependencies

- `numpy`
- `matplotlib`
- `scipy`
- `seaborn`
- `streamlit`

Install all dependencies via:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing

If you’d like to contribute, feel free to fork the repository and submit a pull request! 🚀
