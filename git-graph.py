import sys
from subprocess import run


def from_log_to_dot(lines):
    """
    # doctest: +NORMALIZE_WHITESPACE
    >>> print("\\n".join(from_log_to_dot([
    ...     "abba (f3ac cc32) master",
    ...     "cc32 () dev feature-x",
    ...     "f3ac (acb2) ",
    ...     "acb2 (3dba) ",
    ...     "3dba () ",
    ... ])))
    digraph git_graph {
        rankdir = BT
        {
            rank = same
            "abba"
            "master"
        }
        "master" [shape=box, style=filled, fillcolor=orange]
        "master" -> "abba"
        "f3ac" -> "abba"
        "cc32" -> "abba"
        {
            rank = same
            "cc32"
            "dev"
            "feature-x"
        }
        "dev" [shape=box, style=filled, fillcolor=orange]
        "feature-x" [shape=box, style=filled, fillcolor=orange]
        "dev" -> "cc32"
        "feature-x" -> "cc32"
        "acb2" -> "f3ac"
        "3dba" -> "acb2"
    }
    """
    yield 'digraph git_graph {'
    yield '    rankdir = BT'
    line: str
    for line in lines:
        commit, _, rest = line.partition(' (')
        parents, _, refs = rest.partition(') ')
        if refs:
            yield '    {'
            yield '        rank = same'
            yield f'        "{commit}"'
            for ref in refs.split(' '):
                yield f'        "{ref}"'
            yield '    }'
            for ref in refs.split(' '):
                yield f'    "{ref}" [shape=box, style=filled, fillcolor=orange]'
            for ref in refs.split(' '):
                yield f'    "{ref}" -> "{commit}"'
        if parents:
            for parent in parents.split(" "):
                yield f'    "{parent}" -> "{commit}"'
    yield '}'
