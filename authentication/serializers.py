from rest_framework         import serializers
from authentication.models  import UserAccount
from django.contrib.auth    import update_session_auth_hash


class UserAccountSerializer(serializers.ModelSerializer):

    # passwords stored separately, to be able to
    # give it <write_only> attribute
    password = serializers.CharField(write_only=True, required=False)
    password_repeat = serializers.CharField(write_only=True, required=False)

    # defining metadatas for serializer
    class Meta:
        model = UserAccount
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
            'bio_short',
            'bio_long',
            'company',
            'is_reader',
            'is_writer',
            'password',
            'password_repeat')

        read_only_fields = (
            'created_at',
            'updated_at')

        # deserialization method:
        # creating Python object from JSON
        def create(self, validated_data):
            return UserAccount.objects.create(**validated_data)

        # deserialization method:
        # updating previously created Python object <instance> from JSON
        def update (self, object, validated_data):
            # defining (getting) fields that user can change in realtime
            object.username = validated_data.get('username', object.username)
            object.first_name = validated_data.get('first_name', object.first_name)
            object.last_name = validated_data.get('last_name', object.last_name)
            object.bio_short = validated_data.get('bio_short', object.bio_short)
            object.bio_long = validated_data.get('bio_long', object.bio_long)
            object.company = validated_data.get('company', object.company)

            object.save()

            # getting password
            password = validated_data.get('password', None)
            password_repeat = validated_data.get('password_repeat', None)

            # checking password and password_repeat validity
            if password and password_repeat:
                if password == password_repeat:
                    object.set_password(password)
                    object.save()

            # updating authentication hash
            # (if this does not work, or does not exist, user will have to log in again)
            # (shortly after updating UserAccount data
            update_session_auth_hash(self.context.get('request'), object)

            return object

