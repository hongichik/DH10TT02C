ds = [
    {"name": "An", "age": 20, "score": 8.0},
    {"name": "Bình", "age": 21, "score": 7.5},
    {"name": "Cường", "age": 19, "score": 9.0}
]
print (max(ds, key=lambda x: x["score"]))
for d in ds: d["score"] += 1
print(ds)

