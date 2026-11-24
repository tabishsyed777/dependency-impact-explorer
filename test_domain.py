import unittest
import core

class DomainTests(unittest.TestCase):
    def test_cycle(self):
        a=core.read(core.DEFAULT)[0]
        b={**a,"id":"reverse","consumer":a["dependency"],"dependency":a["consumer"]}
        self.assertEqual(core.answer([a,b],"impact of cart")["answer"],"checkout")

    def test_diamond(self):
        rows=[dict(id=str(i),source="graph",consumer=a,dependency=b) for i,(a,b) in enumerate([("a","b"),("a","c"),("b","d"),("c","d")])]
        self.assertEqual(core.answer(rows,"impact of d")["answer"],"b, c, a")

    def test_challenge_queries(self):
        rows=core.validate(core.read(core.DEFAULT))
        for query,expected in core.read(core.DEFAULT.parent.parent/"qa/challenge.json"):
            with self.subTest(query=query):
                self.assertEqual(core.answer(rows,query)["answer"],expected)
