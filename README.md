# git-graph
git-graph, a small tool to generate graph visualizations of a Git history
as PNG file.

```
Usage:
  git-graph.py [<from>] [--to=<outpath>]  
  git-graph.py -h | --help
  git-graph.py --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  <from>            Path to repository to visualize [default: ./].
  --to=<outpath>    Path to output image [default: ./git-log.png].

```


For example, an illustration of this repository until commit [`f5fb6b4`]() looks like the following:

![](example/git-log.png)