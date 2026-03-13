# MediCare AI - Machine Learning for Healthcare

A full-stack web application that uses machine learning to predict heart disease and diabetes risk factors.

## 🌟 Features

- **Heart Disease Prediction** - Analyzes cardiovascular health indicators
- **Diabetes Prediction** - Assesses likelihood of diabetes based on diagnostic measures
- **Multiple ML Models** - Logistic Regression, KNN, Naive Bayes, Decision Tree
- **Interactive UI** - Modern, responsive design with real-time predictions
- **Notebook Viewer** - View detailed analysis and methodology

## 🏗️ Architecture

### Backend
- **Framework**: FastAPI (Python)
- **ML Libraries**: scikit-learn, pandas, numpy
- **Features**: Model training, prediction APIs, notebook conversion

### Frontend
- **Framework**: React 19 + Vite
- **UI Library**: Tailwind CSS, Framer Motion
- **HTTP Client**: Axios

## 🚀 Deployment on Render

### Prerequisites
- Git repository pushed to GitHub/GitLab
- Render account (free tier available)

### Option 1: One-Click Deploy (Recommended)

1. Connect your repository to Render
2. Render will automatically detect `render.yaml`
3. Click "Apply" to deploy both services

### Option 2: Manual Setup

#### Backend Setup

1. **Create Web Service** on Render
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

2. **Environment Variables**:
   ```
   PORT=10000
   PYTHON_VERSION=3.11.0
   ```

3. **Note**: The backend needs access to dataset files. Ensure these paths are correct:
   - `datasets/Heart_Disease_Prediction.csv`
   - `datasets/Dataset 1 _ Pima Indians diabetes dataset (PIDD).csv`

#### Frontend Setup

1. **Create Static Site** on Render
   - Build Command: `cd MAINN/frontend && npm install && npm run build`
   - Publish Directory: `MAINN/frontend/dist`

2. **Environment Variables**:
   ```
   NODE_VERSION=18.x
   VITE_API_URL=https://your-backend-url.onrender.com
   ```

3. **Important**: Replace `your-backend-url` with your actual backend URL from Render

### Local Development

#### Backend
```bash
cd MAINN/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on: `http://localhost:8000`

#### Frontend
```bash
cd MAINN/frontend
npm install
npm run dev
```

Frontend runs on: `http://localhost:5173`

For production frontend build:
```bash
npm run build
npm run preview
```

## 📊 API Endpoints

### Health Check
- `GET /health` - Check model training status

### Predictions
- `POST /predict/heart` - Heart disease prediction
- `POST /predict/diabetes` - Diabetes prediction

### Model Info
- `GET /info/heart` - Heart disease model metadata
- `GET /info/diabetes` - Diabetes model metadata

### Static Files
- `/notebooks/` - HTML and Jupyter notebooks

## 🔬 Machine Learning Models

### Heart Disease Model
- **Features**: Age, Sex, Chest Pain Type, BP, Cholesterol, Max HR
- **Algorithms**: LR, KNN, NB, Decision Tree
- **Auto-selects** best performing model

### Diabetes Model
- **Features**: Pregnancies, Glucose, Blood Pressure, Insulin, Age, BMI
- **Algorithms**: LR, KNN, NB, Decision Tree
- **Auto-selects** best performing model

## 📁 Project Structure

```
MEDICARE/
├── MAINN/
│   ├── backend/
│   │   ├── ml_logic/       # Model implementations
│   │   ├── notebooks/      # Converted notebooks
│   │   ├── app.py          # Alternative entry point
│   │   ├── main.py         # Main FastAPI app
│   │   └── requirements.txt
│   ├── datasets/           # CSV data files
│   └── frontend/
│       ├── src/
│       │   ├── components/ # React components
│       │   ├── App.jsx     # Main app component
│       │   └── main.jsx    # Entry point
│       ├── dist/           # Production build
│       └── package.json
├── render.yaml             # Render deployment config
└── README.md
```

## ⚠️ Important Notes for Production

1. **Dataset Paths**: The backend looks for datasets relative to the working directory. On Render, ensure the directory structure is maintained.

2. **Model Training**: Models are trained on startup (during lifespan event). First request may take longer.

3. **CORS**: Currently set to allow all origins (`*`). For production, consider restricting to your frontend domain.

4. **Environment Variables**: Create `.env` file in frontend directory:
   ```
   VITE_API_URL=your_production_backend_url
   ```

5. **Free Tier Limitations**: Render's free tier spins down after inactivity. First request may take 30-60 seconds.

## 🛠️ Troubleshooting

### Backend Issues
- **Module not found**: Ensure you're running from `MAINN/backend` directory
- **Dataset not found**: Check CSV file paths in `main.py`
- **Port conflicts**: Render sets `$PORT` environment variable

### Frontend Issues
- **API connection errors**: Update `VITE_API_URL` in `.env`
- **Build failures**: Clear `node_modules` and reinstall
- **CORS errors**: Check backend CORS settings in `main.py`

## 📝 License

MIT License - Feel free to use for educational purposes.

## 🤝 Contributing

This is an educational project. Feel free to fork and enhance!

---

**Made with ❤️ using FastAPI, React, and Machine Learning**