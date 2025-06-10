from rest_framework import serializers

# Creating simple Serializer (no model involved)
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

# example data (like a dictionary)
student_data = {
    'name': 'Geetham',
    'age': 24
}

# validate input data
serializer = StudentSerializer(data=student_data)

if serializer.is_valid():
    # Convert to Python data
    print("Valid Data:", serializer.validated_data)
else:
    print("Errors:", serializer.errors)

# Serialize Python data to JSON format
student = StudentSerializer(student_data)
print("Serialized Data (JSON format):", student.data)
