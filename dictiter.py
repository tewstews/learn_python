import json

jsonList = '''{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}'''

parsed = json.loads(jsonList)


def find_keys(search_key, tree, path=tuple()):
    if isinstance(tree, list):
        for idx, el in enumerate(tree):
            yield from find_keys(search_key, el, path+(idx,))
    elif isinstance(tree, dict):
        for k in tree:
            if k == search_key:
                yield path + (k, )
        for k, v in tree.items():
            yield from find_keys(search_key, v, path+(k,))

def retrieve(tree, path):
    for p in path:
        tree = tree[p]
    return tree

result = list(find_keys("name", parsed))
expected = [("powers", "age", "secretIdentity")]


print(retrieve(parsed, result[0]))