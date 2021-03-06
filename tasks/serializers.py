from rest_framework import serializers
from tasks.models import Task
from random_words import RandomWords
import random
import requests
from decouple import config

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['url', 'id', 'type', 'title', 'description', 'category']

    trello_auth_params={
        'key': config("TRELLO_KEY"),
        'token': config("TRELLO_TOKEN"),
    }

    def create(self, validated_data):
        member = ""
        label = ""
        if validated_data.get('type') == 'bug':
            # If the task is a Bug then:
            # The title needs to be randomized with the following pattern: bug-{word}-{number}
            # Should be assigned to a random member
            # Should have the “Bug” label
            number = random.randint(1, 999)
            rw = RandomWords()
            word = rw.random_word()
            title = "bug-{word}-{number}".format(word=word,number=number)
            validated_data['title'] = title
            validated_data['category'] = Task.Category.BUG
            response_members = requests.get('https://api.trello.com/1/boards/625b13a3d65e39774e6bb01f/members?',params=self.trello_auth_params)
            if response_members.status_code == requests.codes.ok:
                members = response_members.json()
                member = members[random.randint(0, len(members)-1)].get('id')

        task = Task.objects.create(**validated_data)

        if task.category:
            label = Task.Category(task.category).value
        response_trello = requests.post('https://api.trello.com/1/cards', 
            params=self.trello_auth_params,
            data={
                'idList': '625b141c240a177e6516bd18',
                'name': task.title,
                'desc': task.description,
                'idLabels': label,
                'idMembers': member,
            }
        )
        response_trello.raise_for_status()
        return task