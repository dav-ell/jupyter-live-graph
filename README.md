# jupyter-live-graph

Let's you create a graph in a Jupyter cell, and update that graph live in other cells. Uses matplotlib`.draw()`.

![](jupyterdraw.gif)

As simple as:

```
%matplotlib notebook
from draw import Draw

draw = Draw()
# ---
for i in range(1000):
  draw.graph([j for j in range(i)])
```

## License

MIT

## Contributing

This project is wide open to pull requests.
