from django.shortcuts import render
import numpy as np
from .models import HepatitisRecord
import pickle

# Load everything once
model_path = 'HepApp/ml_models/model_c1.pkl'
scaler_path = 'HepApp/ml_models/scaler.pkl'
encoder_path = 'HepApp/ml_models/label_encoder.pkl'

with open(model_path, 'rb') as f:
    model = pickle.load(f)
with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)
with open(encoder_path, 'rb') as f:
    le = pickle.load(f)

# Define top features used in training
top_features = ['AST', 'ALT', 'CHE', 'ALP', 'BIL', 'GGT', 'Age', 'ALB']  # modify if needed

label_mapping = {
    0: 'Normal - Blood Donor',
    1: 'Stage 1 - Hepatitis',
    2: 'Stage 2 - Fibrosis',
    3: 'Stage 3 - Cirrhosis'
}

def home(request):
    prediction = None
    if request.method == 'POST':
        try:
            user_input = [float(request.POST.get(f)) for f in top_features]
            input_scaled = scaler.transform([user_input])
            pred = model.predict(input_scaled)
            prediction = label_mapping.get(pred[0], "Unknown")
            HepatitisRecord.objects.create(
            AST=user_input[0], ALT=user_input[1], CHE=user_input[2], ALP=user_input[3], BIL=user_input[4],
            GGT=user_input[5], Age=user_input[6], ALB=user_input[7], prediction_result=str(prediction)
        )
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render(request, 'predict.html', {'prediction': prediction, 'feature_names': top_features})
