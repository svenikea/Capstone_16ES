from rest_framework import serializers
from .models import Shoe, Shoes_Brand

# class ShoeSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = shoe
# 		fields = '__all__'

# class ShoesBrandSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = shoes_brand
# 		fields = '__all__'

# # Or instead of showing id we can tell it to show the url
# class ShoeSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = shoe
# 		fields = '__all__'

# class ShoesBrandSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = shoes_brand
# 		fields = '__all__'

# Or combine the two we have


# for more read this link https://www.django-rest-framework.org/api-guide/relations/
class ShoeSerializer(serializers.ModelSerializer):
    # brand = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="orm:Shoes_Brand-detail"
    # )

    class Meta:
        model = Shoe
        fields = '__all__'


class ShoesBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes_Brand
        fields = '__all__'
# class ShoeSerializer(serializers.ModelSerializer): # for more read this link https://www.django-rest-framework.org/api-guide/relations/
# 	class Meta:
# 		model = shoe
# 		fields = '__all__'
# class ShoesBrandSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = shoes_brand
# 		fields = '__all__'
