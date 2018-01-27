from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

import urllib.request

# Create your views here.

def Home(request):

	return render(request, 'ttt/index.html', {

	})

class RetrieveAPIView(APIView):

	def get(self, request, *args, **kwargs):
		n = request.GET.get('n', 0)
		n = int(n)
		if n<0:
			return Response({'Error': 'Invalid input'})
		fin = urllib.request.urlopen('http://terriblytinytales.com/test.txt')
		frequency = dict()
		special_characters = "!\"#$%&'*+,-./:;<=>?@[\]^_`{|}~()-–"
		for line in fin:
			current_line = line.decode().split()
			for word in current_line:
				for char in special_characters:
					word = word.strip(char)
				if not word:
					continue
				if word not in frequency:
					frequency[word] = 1
				else:
					frequency[word]+=1
		words_frequencies = []
		for word in frequency:
			words_frequencies.append([frequency[word], word])
		words_frequencies.sort()
		words_frequencies = words_frequencies[::-1]
		n = min(n, len(words_frequencies))
		n_frequent_words = words_frequencies[:n]
		return Response(n_frequent_words)
		
Retrieve = RetrieveAPIView.as_view()