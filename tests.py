from classes import Page, Graph

damp = 0.85


def test_mutual_link():
    a = Page("A1", 1)
    b = Page("B1", 1)

    a.outgoing_pages = [b]
    a.incoming_pages = [b]

    b.outgoing_pages = [a]
    b.incoming_pages = [a]

    graph = Graph([a, b], damp)

    assert (graph.calculate_pagerank() ==
            [
                [a, 1],
                [b, 1]
            ])


def test_loop_link():
    a = Page("A2", 1)
    b = Page("B2", 1)
    c = Page("C3", 1)

    a.outgoing_pages = [c]
    a.incoming_pages = [b]

    c.outgoing_pages = [b]
    c.incoming_pages = [a]

    b.outgoing_pages = [a]
    b.incoming_pages = [c]

    graph = Graph([a, c, b], damp)

    assert (graph.calculate_pagerank() ==
            [
                [a, 1],
                [c, 1],
                [b, 1]
            ])


def test_irregular_link():
    a = Page("A3", 1)
    b = Page("B3", 1)
    c = Page("C3", 1)

    a.outgoing_pages = [b, c]
    a.incoming_pages = [b]

    b.outgoing_pages = [a, c]
    b.incoming_pages = [a]

    c.incoming_pages = [a, b]

    graph = Graph([a, b, c], damp)

    assert (graph.calculate_pagerank() ==
            [
                [a, 0.575],
                [b, 0.39437500000000003],
                [c, 0.561984375]
            ])


def test_stacking_link():
    a = Page("A4", 1)
    b = Page("B4", 1)
    c = Page("C4", 1)

    a.outgoing_pages = [b]

    b.outgoing_pages = [c]
    b.incoming_pages = [a]

    c.incoming_pages = [b]

    graph = Graph([a, b, c], damp)

    assert (graph.calculate_pagerank() ==
            [
                [a, 0.15000000000000002],
                [b, 0.2775],
                [c, 0.385875]
            ])


def test_iteration():
    a = Page("A5", 1)
    b = Page("B5", 1)
    c = Page("C5", 1)

    a.outgoing_pages = [b]

    b.outgoing_pages = [c]
    b.incoming_pages = [a]

    c.incoming_pages = [b]

    graph = Graph([a, b, c], damp)
    pagerank = []

    print("\npagerank after 1 iteration: ")
    print(graph.calculate_pagerank())

    for pr in range(1_000000):
        pagerank = graph.calculate_pagerank()

    print("\npagerank after 1000 iterations: ")
    print(pagerank)