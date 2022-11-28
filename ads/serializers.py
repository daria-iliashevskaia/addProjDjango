from rest_framework import serializers


from ads.models import Category, Ads, User, Location, Selections


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class AdsSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        required=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ads
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name')

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):

        self._location = self.initial_data.pop("location")

        return super().is_valid(raise_exception=False)

    def create(self, validated_data):

        user = super().create(validated_data)

        for location in self._location:

            location_obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)
        user.save()

        user.set_password(user.password)
        user.save()

        return user


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'


class SelectionsSerializer(serializers.ModelSerializer):

    items = ItemsSerializer(many=True)

    owner = serializers.SlugRelatedField(
        required=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Selections
        fields = '__all__'


class SelectionsCreateSerializer(serializers.ModelSerializer):

    items = serializers.SlugRelatedField(
        many=True,
        required=False,
        slug_field='id',
        queryset=Ads.objects.all()
    )

    owner = serializers.SlugRelatedField(
        required=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Selections
        fields = '__all__'