from rest_framework import serializers

class LatencyPredictionSerializer(serializers.Serializer):
    packet_size = serializers.FloatField(min_value=0, help_text="Packet size in bytes")
    predicted_latency = serializers.FloatField(read_only=True)

class BatchPredictionSerializer(serializers.Serializer):
    file = serializers.FileField()
