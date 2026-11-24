"""Dependency Impact Explorer domain retrieval and answer rules."""
NAME = '07-dependency-impact-explorer'

from collections import deque
from common import norm,require
FIELDS=("consumer","dependency")

def validate(rows):
    edges=[(norm(r["consumer"]),norm(r["dependency"])) for r in rows]
    require(len(edges)==len(set(edges)),"duplicate dependency")

def solve(rows,q):
    for prefix in ("impact of ","direct users of ","dependencies of "):
        if not q.startswith(prefix): continue
        node=q[len(prefix):].rstrip("?")
        source,target=("consumer","dependency") if prefix=="dependencies of " else ("dependency","consumer")
        by_node={}
        for edge in sorted(rows,key=lambda r:(norm(r[target]),r["id"])):
            by_node.setdefault(norm(edge[source]),[]).append(edge)
        seen={node}
        queue=deque([node])
        names,ev=[],[]
        while queue:
            for edge in by_node.get(queue.popleft(),[]):
                name=norm(edge[target])
                if name in seen: continue
                seen.add(name)
                names.append(edge[target])
                ev.append(edge)
                if prefix=="impact of ": queue.append(name)
        if ev: return ", ".join(names),ev,prefix.strip()
