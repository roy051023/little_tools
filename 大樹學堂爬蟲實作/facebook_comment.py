import requests, json
token = "這邊要放自己的臉書access_token"
re = requests.get('https://graph.facebook.com/v2.5/me/posts?limit=1&access_token=' + token)# api用post就會顯示該使用者的貼文s
#if you want to chose a specific time span, append 'since=1420041600' after 'post?' 
#cause it use Unix seconds, so 1420041600 means 2015/01/01
jsonObj=json.loads(re.text)
for i in jsonObj['data']:
	req_for_posts = requests.get("https://graph.facebook.com/v2.5/{0}/comments?access_token={1}".format(i['id'], token))# api用post就會顯示該使用者的貼文的ID再加上comments就會顯示該篇貼文的評論
	postJson = json.loads(req_for_posts.text)
	for j in postJson['data']:
		print(j)
		req_for_comments = requests.get("https://graph.facebook.com/v2.5/{0}/comments?access_token={1}".format(j['id'], token))#用該篇評論的id再接comments就會顯示該則回應底下的所有回應
		commentJson = json.loads(req_for_comments.text)
		print(commentJson, end="\n\n")
