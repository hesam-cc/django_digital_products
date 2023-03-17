from rest_framework import serializers
from .models import Category,Product,File

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title','description','avatar')

class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('id','title','file_type','file')
    def get_file_type(self,obj):
        return obj.get_file_type_display()

class ProductSerializer(serializers.HyperlinkedModelSerializer): # not url ===> serializers.ModelSerializer
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    custom = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id','title','description','avatar','categories','files','url','custom')
    def get_custom(self,obj):
        return obj.id