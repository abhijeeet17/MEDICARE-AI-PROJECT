# 🚀 Render Deployment Checklist

## ✅ Pre-Deployment Checks

### Backend
- [x] `requirements.txt` is complete with all dependencies
- [x] `main.py` has proper lifespan events for model training
- [x] Dataset paths are correctly configured
- [x] CORS is properly configured (currently allows all origins)
- [x] `.gitignore` created for Python files

### Frontend
- [x] API URLs use environment variables (`VITE_API_URL`)
- [x] Vite config includes proxy for development
- [x] Build script works: `npm run build`
- [x] `.env.example` file created
- [x] `.gitignore` created for Node.js files

### Project Structure
- [x] `render.yaml` configuration file created
- [x] Root `.gitignore` created
- [x] README.md with deployment instructions

---

## 🎯 Deployment Steps

### Step 1: Push to Git Repository

```bash
# Initialize git if not already done
git init
git add .
git commit -m "Initial commit - MediCare AI ready for deployment"

# Push to GitHub/GitLab
git branch -M main
git remote add origin https://github.com/yourusername/medicare-ai.git
git push -u origin main
```

### Step 2: Connect to Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Render will detect `render.yaml` automatically

### Step 3: Configure Environment Variables

#### For Backend Service:
```
PORT=10000
PYTHON_VERSION=3.11.0
```

#### For Frontend Service:
```
NODE_VERSION=18.x
VITE_API_URL=https://your-backend-name.onrender.com
```

**Important**: Replace `your-backend-name` with the actual backend URL provided by Render after deployment.

### Step 4: Deploy

1. Click **"Apply"** to start deployment
2. Monitor the deployment logs in Render dashboard
3. Wait for both services to deploy successfully

---

## 🔍 Post-Deployment Verification

### Backend Health Check
Visit: `https://your-backend-name.onrender.com/health`

Expected response:
```json
{
  "status": "healthy",
  "heart_model": "Model Name",
  "diabetes_model": "Model Name"
}
```

### Frontend Check
Visit: `https://your-frontend-name.onrender.com`

Test:
1. Select Heart Disease prediction
2. Fill in sample data or use "Sample Data" button
3. Submit and verify prediction works
4. Repeat for Diabetes

---

## ⚠️ Common Issues & Solutions

### Issue 1: Backend won't start
**Symptoms**: Deployment fails or crashes on startup

**Solutions**:
- Check logs for missing dependencies
- Verify dataset files exist in correct paths
- Ensure `PORT` environment variable is set
- Check Python version compatibility

### Issue 2: Frontend can't connect to backend
**Symptoms**: "Failed to load metadata" error

**Solutions**:
- Update `VITE_API_URL` with correct backend URL
- Rebuild frontend after URL change
- Check CORS settings in backend
- Verify backend is running (check health endpoint)

### Issue 3: Models not trained
**Symptoms**: Health check shows "Not Trained"

**Solutions**:
- Check dataset file paths in `main.py`
- Verify CSV files are in `datasets/` folder
- Check startup logs for training errors
- Ensure sufficient disk space on Render

### Issue 4: Slow first request (30-60 seconds)
**Cause**: Render free tier spins down after inactivity

**Solutions**:
- Upgrade to paid plan for always-on service
- Or accept the delay (models train on startup)

---

## 📊 Monitoring

### Render Dashboard
- View real-time logs
- Monitor resource usage
- Check deployment history
- Restart services if needed

### Health Endpoints
- Backend: `/health`
- Model info: `/info/heart` and `/info/diabetes`

---

## 🔄 Updating Deployment

After initial deployment, updates are automatic:

```bash
# Make changes locally
git add .
git commit -m "Update description"
git push origin main
```

Render will automatically:
1. Detect new commits
2. Rebuild affected services
3. Deploy updates with zero downtime

---

## 💰 Cost Estimation (Free Tier)

### Backend (Web Service - Starter)
- **Cost**: Free
- **Limitations**: 
  - Spins down after 15 min inactivity
  - 750 hours/month limit
  - First request slow after spin-down

### Frontend (Static Site)
- **Cost**: Free
- **Limitations**: None significant
- **Bandwidth**: 100GB/month included

**Total**: $0/month (Free tier sufficient for demos/portfolios)

---

## 🎉 Success Indicators

✅ Both services show "Live" status in Render
✅ Backend health check returns healthy status
✅ Frontend loads without errors
✅ Predictions work correctly
✅ Notebooks are viewable
✅ No errors in service logs

---

## 📞 Support Resources

- [Render Documentation](https://render.com/docs)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)
- [Vite Production Build](https://vitejs.dev/guide/build.html)

---

**Good luck with your deployment! 🚀**
