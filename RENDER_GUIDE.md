# Render Deployment Guide

## 🚀 Your Render Service
**URL**: https://ai-engine-1i5x.onrender.com

## 📋 Setup Instructions

### 1. Environment Variables
Go to your Render Dashboard → Your Service → Environment

Copy all variables from `RENDER_ENV.txt` and add them to your Render service.

**CRITICAL Variables** (must be set):
- `MONGO_URI` - Your MongoDB connection string
- `OLLAMA_BASE_URL` - Your Ollama API endpoint
- `JWT_SECRET_KEY` - JWT secret (must match your backend)
- `CORS_ORIGINS` - Allowed origins including your Render URL

**DON'T SET**:
- `PORT` - Render sets this automatically

### 2. Build & Start Commands
Your service should already have:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python run_server.py`

### 3. Health Check
Render will monitor: `/health`

Your service should start and show:
```
INFO:     Uvicorn running on http://0.0.0.0:[PORT]
```

### 4. Test Your Deployment
```bash
# Health check
curl https://ai-engine-1i5x.onrender.com/health

# API docs
https://ai-engine-1i5x.onrender.com/docs
```

## 🔧 Troubleshooting

**Port Detection Issues**:
- The server now reads PORT from environment automatically
- Unbuffered output ensures logs appear immediately
- MongoDB check is skipped in serverless mode (Render is traditional)

**Dependencies**:
- All ML packages (PyTorch, transformers, etc.) are supported
- Build may take 3-5 minutes due to large dependencies

**Logs**:
View real-time logs in Render Dashboard → Logs

## 📦 What's Configured

✅ PORT environment variable detection
✅ Unbuffered Python output for better logging
✅ MongoDB connection verification on startup
✅ CORS with Render URL included
✅ Health check endpoint
✅ JWT authentication
✅ Error handling and graceful startup
