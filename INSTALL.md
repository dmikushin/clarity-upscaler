# Installation Instructions

## Prerequisites
- Python 3.10.4
- Virtual environment activated

## Installation Steps

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Cog Python package:**
   ```bash
   pip install cog
   ```

3. **Download model weights:**
   ```bash
   python download_weights.py
   ```

## Usage

### REST API Server

1. **Start the API server:**
   ```bash
   python serve.py
   ```

2. **Server will be available at:** `http://localhost:5000`

3. **Make predictions via HTTP:**
   ```bash
   curl -X POST http://localhost:5000/predictions \
     -H "Content-Type: application/json" \
     -d '{
       "input": {
         "image": "https://example.com/image.jpg",
         "scale_factor": 2,
         "creativity": 0.35,
         "dynamic": 6,
         "resemblance": 0.6
       }
     }'
   ```

4. **Available API endpoints:**
   - `POST /predictions` - создать предикцию
   - `GET /predictions/{id}` - получить результат

## Available Parameters

- `scale_factor` (default: 2) - коэффициент увеличения
- `dynamic` (1-50, default: 6) - HDR эффект  
- `creativity` (0-1, default: 0.35) - креативность
- `resemblance` (0-3, default: 0.6) - схожесть с оригиналом
- `num_inference_steps` (1-100, default: 18) - количество шагов
- `seed` (default: 1337) - сид для воспроизводимости
- `sharpen` (0-10) - резкость
- `output_format` - формат вывода (webp/jpg/png)

## Notes
- Make sure your virtual environment is activated before installing dependencies
- The `cog` Python package is required for running the API server
- Model weights need to be downloaded before first use
- The REST API is more convenient for integration with other applications