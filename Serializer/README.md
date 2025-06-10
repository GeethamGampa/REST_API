Django REST Framework – Basic Serializer (No Model)

This is a simple demo project showing how to use Django REST Framework's Serializer class without using a model. It manually defines fields and validates input data like a form.

What It Does
Creates a StudentSerializer with fields: name and age

Validates dictionary input

Prints:

Validated Python data

JSON-serializable data

Step-by-Step Breakdown

1. Import the serializer class


from rest_framework import serializers

2. Define the serializer

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()


This defines what data is expected.

It works like a form: it will check if the input is valid.

3. Create example data (like a dictionary)

student_data = {
    'name': 'Geetham',
    'age': 24
}


4. Validate the data

serializer = StudentSerializer(data=student_data)

if serializer.is_valid():
    print("Valid Data:", serializer.validated_data)
else:
    print("Errors:", serializer.errors)


is_valid() checks if student_data matches the field types and constraints.

validated_data gives you the cleaned Python data.

If invalid, it shows error messages.

 5. Serialize the data back to JSON-style

 student = StudentSerializer(student_data)
print("Serialized Data (JSON format):", student.data)


Converts Python dictionary into a serializable format (for API responses).

student.data returns:

{'name': 'Geetham', 'age': 24}


Example Output

Valid Data: {'name': 'Geetham', 'age': 24}
Serialized Data (JSON format): {'name': 'Geetham', 'age': 24}

What I Learned
How to define a plain Serializer without using a model

How to validate and clean input data manually

How to serialize data back into JSON-like format.