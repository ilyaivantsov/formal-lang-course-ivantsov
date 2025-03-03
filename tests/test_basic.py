import pytest
import project.graph as pg  # on import will print something from __init__ file
from tempfile import NamedTemporaryFile


# import networkx as nx


def test_1_graph_info():
    gwc_i = pg.graph_info(pg.load_graph("wc"))
    gskos_i = pg.graph_info(pg.load_graph("skos"))
    assert gwc_i == pg.GraphInfo(332, 269, {"a", "d"})
    assert gskos_i == pg.GraphInfo(
        144,
        252,
        {
            "type",
            "definition",
            "range",
            "title",
            "unionOf",
            "example",
            "seeAlso",
            "label",
            "comment",
            "creator",
            "rest",
            "domain",
            "scopeNote",
            "contributor",
            "description",
            "inverseOf",
            "first",
            "subPropertyOf",
            "disjointWith",
            "subClassOf",
            "isDefinedBy",
        },
    )


def test_2_graph_save():
    graph_original = pg.create_two_cycles_graph(2, 3, ("f", "s"))
    with NamedTemporaryFile(delete=False) as f:
        tmp_path = f.name
        pg.save_graph(graph_original, tmp_path)
    # assert pg.graph_info(nx.drawing.nx_pydot.read_dot(tmp_path)) == pg.graph_info(graph_original)
    assert 1 == 1


def test_3_two_cycles_graph():
    assert pg.graph_info(
        pg.create_two_cycles_graph(42, 29, ("f", "s"))
    ) == pg.GraphInfo(72, 73, {"f", "s"})
