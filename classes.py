from __future__ import annotations


class Page:
    def __init__(self, link: str, rank: float, incoming_pages: list[Page] = [], outgoing_pages: list[Page] = []):
        self.link = link
        self.rank = rank
        self.incoming_pages = incoming_pages
        self.outgoing_pages = outgoing_pages

    def calculate_pagerank(self, damp: float) -> float:
        """Calculates and updates the pagerank for this page"""
        pagerank_sum = 0

        for page_in in self.incoming_pages:
            pagerank_sum += page_in.rank / len(page_in.outgoing_pages)

        self.rank = 1 - damp + damp * pagerank_sum

        return self.rank


class Graph:
    def __init__(self, pages: list[Page], damp: float):
        self.pages = pages
        self.damp = damp

    def calculate_pagerank(self) -> [Page, float]:
        """Calculates and updates the pagerank of all registered pages of this graph instance"""
        pagerank = []

        for page in self.pages:
            pagerank.append([page, page.calculate_pagerank(self.damp)])

        return pagerank
