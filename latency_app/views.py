import pandas as pd
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LatencyPredictionSerializer, BatchPredictionSerializer
from .utils import LatencyModelLoader

class DashboardView(View):
    def get(self, request):
        return render(request, 'latency_app/dashboard.html')

class PredictAPIView(APIView):
    def post(self, request):
        serializer = LatencyPredictionSerializer(data=request.data)
        if serializer.is_valid():
            packet_size = serializer.validated_data['packet_size']
            prediction, source = LatencyModelLoader.predict(packet_size)
            if prediction is not None:
                return Response({
                    'packet_size': packet_size,
                    'predicted_latency': round(prediction, 4),
                    'source': source
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Prediction failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CSVUploadView(View):
    def post(self, request):
        if 'file' not in request.FILES:
             return render(request, 'latency_app/dashboard.html', {'error': 'No file uploaded'})
        
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return render(request, 'latency_app/dashboard.html', {'error': 'Please upload a CSV file'})

        try:
            df = pd.read_csv(csv_file)
            # Expecting 'packet_size' column
            if 'packet_size' not in df.columns:
                return render(request, 'latency_app/dashboard.html', {'error': 'CSV must contain a "packet_size" column'})
            
            predictions = []
            for size in df['packet_size']:
                pred, source = LatencyModelLoader.predict(size)
                predictions.append({
                    'packet_size': size,
                    'predicted_latency': round(pred, 4) if pred is not None else 'N/A',
                    'source': source
                })
            
            return render(request, 'latency_app/dashboard.html', {'results': predictions})
        except Exception as e:
            return render(request, 'latency_app/dashboard.html', {'error': f'Error processing file: {str(e)}'})
