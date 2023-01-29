import requests
import itertools

def topArticles(limit):    
	url = f"https://jsonmock.hackerrank.com/api/articles?page=1"	
	response = requests.get(url).json()	 
	data = response.get("data")	
	
	num_comments_sort = sorted(data, key=lambda x: x.get("num_comments") if x.get("num_comments") is not None else 0, reverse=True)
	alphabet_sort = sorted(num_comments_sort, key=lambda x: x.get("title") or x.get("story_title", ""), reverse=True)
	
	for d in itertools.islice(alphabet_sort, limit):
		if d["title"]:  
			print(d["title"])
		elif d["story_title"]:
			print(d["story_title"])
		else:
			pass

if __name__ == "__main__":	
	topArticles(2)