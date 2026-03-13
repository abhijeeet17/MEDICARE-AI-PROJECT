# 🎯 STEP-BY-STEP DEPLOYMENT GUIDE

Follow these exact steps to deploy your MediCare AI application on Render.

---

## 📋 Pre-Deployment Checklist

Before you start, make sure you have:
- [ ] Git installed on your computer
- [ ] A GitHub account
- [ ] A Render account (sign up at https://render.com)
- [ ] All code working locally

---

## 🚀 STEP 1: Test Locally First

### 1.1 Start the Backend

Open PowerShell and run:

```powershell
cd "f:\SEM 5\ML\CA2\MEDICARE\MAINN\backend"
pip install -r requirements.txt
uvicorn main:app --reload
```

**Expected Output:** 
- `INFO:     Uvicorn running on http://0.0.0.0:8000`
- Wait for model training to complete (30-60 seconds)

Keep this terminal open!

### 1.2 Test Backend (New Terminal)

Open a new PowerShell window:

```powershell
cd "f:\SEM 5\ML\CA2\MEDICARE\MAINN\backend"
python test_backend.py
```

**Expected Output:**
- ✅ Health check passed
- ✅ Heart Model info displayed
- ✅ Diabetes Model info displayed
- ✅ Heart prediction successful
- ✅ Diabetes prediction successful

If all tests pass, backend is working! ✅

### 1.3 Start Frontend (New Terminal)

Open another PowerShell window:

```powershell
cd "f:\SEM 5\ML\CA2\MEDICARE\MAINN\frontend"
npm install
npm run dev
```

**Expected Output:**
- `VITE v7.x.x ready in xxx ms`
- `➜  Local:   http://localhost:5173/`

### 1.4 Test Frontend

1. Open browser to: `http://localhost:5173`
2. Click "Heart Disease" card
3. Click "Sample Data" button
4. Click "Analyze Risk Factors"
5. Verify prediction appears
6. Repeat for "Diabetes"

**If everything works locally, you're ready to deploy!** ✅

---

## 🌐 STEP 2: Push to GitHub

### 2.1 Initialize Git (if not already done)

In PowerShell:

```powershell
cd "f:\SEM 5\ML\CA2\MEDICARE"
git init
git add .
git commit -m "Initial commit - MediCare AI ready for deployment"
```

### 2.2 Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `medicare-ai` (or your choice)
3. Make it **Public** or **Private** (your choice)
4. Click "Create repository"

### 2.3 Push to GitHub

Copy and run these commands from GitHub's instructions:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/medicare-ai.git
git push -u origin main
```

**Verify:** Check your GitHub repository - all files should be there!

---

## ☁️ STEP 3: Deploy on Render

### 3.1 Connect to Render

1. Go to https://dashboard.render.com
2. Sign in with GitHub
3. Click **"New +"** button
4. Select **"Blueprint"**

### 3.2 Connect Repository

1. Find your `medicare-ai` repository
2. Click **"Connect"**
3. Render will detect `render.yaml` automatically

### 3.3 Configure Services

You'll see two services:
- **medicare-backend** (Python web service)
- **medicare-frontend** (Static site)

#### Backend Configuration:
- **Name**: medicare-backend
- **Region**: Oregon (closest to you)
- **Branch**: main
- **Root Directory**: Leave blank
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

Click **"Advanced"** and add environment variables:

```
KEY: PORT
VALUE: 10000

KEY: PYTHON_VERSION
VALUE: 3.11.0
```

#### Frontend Configuration:

Click on the frontend service:

- **Name**: medicare-frontend
- **Region**: Oregon (same as backend)
- **Branch**: main
- **Build Command**: `cd MAINN/frontend && npm install && npm run build`
- **Publish Directory**: `MAINN/frontend/dist`

Add environment variables:

```
KEY: NODE_VERSION
VALUE: 18.x

KEY: VITE_API_URL
VALUE: (leave empty for now - we'll update after backend deploys)
```

### 3.4 Start Deployment

1. Review settings
2. Click **"Apply"**
3. Watch the deployment logs!

**Deployment time:** 5-10 minutes

---

## ⏳ STEP 4: Wait for Deployment

### Monitor Progress

1. Go to Render Dashboard
2. Click on each service to see logs
3. Wait for both to show **"Live"** status

### Backend Logs Should Show:
```
Training models...
Heart Disease Model Trained. Best: ...
Diabetes Model Trained. Best: ...
Converting notebooks to HTML...
INFO:     Application startup complete.
```

### Frontend Logs Should Show:
```
npm install completed
npm run build completed
Deployment complete!
```

---

## 🔗 STEP 5: Connect Frontend to Backend

### 5.1 Get Backend URL

1. In Render Dashboard, click on **medicare-backend**
2. Copy the URL (looks like: `https://medicare-backend-xxxx.onrender.com`)

### 5.2 Update Frontend Environment Variable

1. Click on **medicare-frontend** service
2. Go to **"Environment"** tab
3. Find `VITE_API_URL`
4. Paste your backend URL
5. Click **"Save Changes"**

### 5.3 Redeploy Frontend

1. Go to **"Manual Deploy"** section
2. Select **main** branch
3. Click **"Deploy"**

Wait 2-3 minutes for redeployment.

---

## ✅ STEP 6: Test Live Application

### 6.1 Test Backend

Visit in browser:
```
https://your-backend-url.onrender.com/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "heart_model": "Logistic Regression",
  "diabetes_model": "Logistic Regression"
}
```

### 6.2 Test Frontend

Visit in browser:
```
https://your-frontend-url.onrender.com
```

**Test:**
1. Select Heart Disease
2. Use Sample Data button
3. Submit and verify prediction works
4. Test Diabetes too

---

## 🎉 SUCCESS! You're Live!

Your application is now deployed and accessible worldwide! 🌍

---

## 🛠️ Troubleshooting

### Problem: Backend won't start

**Solution:**
1. Check logs in Render dashboard
2. Look for error messages
3. Common issues:
   - Missing dataset files → Check directory structure
   - Port not set → Add PORT=10000 env variable
   - Dependencies missing → Check requirements.txt

### Problem: Frontend shows "Failed to load metadata"

**Solution:**
1. Verify `VITE_API_URL` is correct
2. Check that backend is running (visit /health)
3. Redeploy frontend after updating URL

### Problem: Models show "Not Trained"

**Solution:**
1. Check backend startup logs
2. Verify datasets exist in repository
3. Look for training errors in logs

### Problem: First request takes 30-60 seconds

**This is normal!** Render free tier spins down after inactivity.

**Solutions:**
- Upgrade to paid plan ($7/month) for always-on
- Or just accept the delay (it's free!)

---

## 📊 Monitoring Your App

### Render Dashboard
- View real-time logs
- See resource usage
- Restart services if needed
- Deploy updates

### Automatic Updates

After initial deployment, any push to main branch will auto-deploy:

```powershell
# Make changes
git add .
git commit -m "Updated something"
git push origin main
```

Render will automatically rebuild and deploy!

---

## 💰 Cost Breakdown

**Free Tier:**
- Backend: Free (750 hours/month)
- Frontend: Free (100GB bandwidth)
- **Total: $0/month** ✅

**Paid Tier (optional):**
- Backend Always-On: $7/month
- Frontend: Still free
- **Total: $7/month**

---

## 📞 Resources

- **Render Docs**: https://render.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **Your Dashboard**: https://dashboard.render.com

---

## ✨ Next Steps

1. Share your live URL with friends/recruiters!
2. Add custom domain (optional)
3. Set up monitoring/alerts (optional)
4. Consider upgrading for always-on backend

---

**Congratulations! You've successfully deployed MediCare AI! 🎉**

**Your app is now helping people assess health risks worldwide!** 🏥💙
