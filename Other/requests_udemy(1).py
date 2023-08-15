import requests
# response = requests.get('https://www.engineerspock.com')

# print(response.status_code)

# print(type(response))

# if response:
#     print('True')






# for url in ['https://www.engineerspock.com', 'https://www.engineerspock.com/indexsating']:

#     try:
#         response = requests.get(url)
    
#         response.raise_for_status()
    
#     except requests.HTTPError as http_err:
#         print(f'Error: {http_err}')
#     except Exception as err:
#         print(f'Unknown error: {err}')
    
#     else:
#         print('Connected successfully')






# response = requests.get('https://www.engineerspock.com')

# response.encoding = 'utf-8'

# print(response.content)
# print(response.text)





# response = requests.get('http://api.github.com')

# data = response.json()

# print(data)





# blog_response = requests.get('https://www.engineerspock.com')
# github_response = requests.get('http://api.github.com')

# print(blog_response.headers, end='\n')
# print('')
# print(github_response.headers)

# print(blog_response.headers['content-type'])





placeholder_response = requests.get('http://jsonplaceholder.typicode.com/comments', params=b'postId=1')
print(placeholder_response.json())


