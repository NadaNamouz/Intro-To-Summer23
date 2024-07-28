x = {"a","b","c"}
y = {"x","a","b"}
def similarity(video,video2):
	c=0
	for i in range(len(video[hashtags])):
		for k in range(len(video[hashtags])):
			if video["hashtag"[k]]==video2["hashtag"[k]]:
				c+=1
	return c

print(similarity(x,y))