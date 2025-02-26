#!/bin/bash
# Start Node.js authentication proxy in the background on port 8000
cd proxy
node proxy.mjs --port=8000 &

# Start Streamlit app on port 8501
cd ..
streamlit run app.py --server.port=8501 --server.enableCORS=false
