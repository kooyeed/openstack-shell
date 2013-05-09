# Setup a mapper
from routes import Mapper
map = Mapper()
map.connect(None, "/error/{action}/{id}", controller="error")
map.connect("home", "/", controller="main", action="index")

# Match a URL, returns a dict or None if no match
result = map.match('/error/myapp/4')
# result == {'controller': 'main', 'action': 'myapp', 'id': '4'}
print(result)