from .models import Comment, Reply, BaseComment
from posts.models import Post
from rest_framework import serializers


class BaseCommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = BaseComment


class CommentSerializer(BaseCommentSerializer):
    replies_count = serializers.SerializerMethodField()
    # replies = serializers.SerializerMethodField()

    class Meta:
        extra_kwargs = {}
        fields = '__all__'
        model = Comment

    def get_replies_count(self, comment):
        """ get the number of replies for single comment """

        return Reply.objects.filter(parent=comment).count()


class ReplySerializer(BaseCommentSerializer):
    class Meta:
        extra_kwargs = {}
        fields = '__all__'
        model = Reply
