"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730552319"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value at of an empty Linked List should raise a ValueError."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_value_at_non_empty() -> None:
    """Value at of a non-empty list should return return its data value at given index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 20


def test_max_at_empty() -> None:
    """Max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_at_non_empty() -> None:
    """Max of a non-empty Linked List should return max data value in Node."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_linkify_at_empty() -> None:
    """Linkify of an empty list should return None."""
    items: list[int] = [1]
    assert linkify(items) == Node(1, None)


def test_linkify_at_non_empty() -> None:
    """Linkify of a non-empty list should return all its numbers in a Linked List."""
    items: list[int] = [1, 2, 3]
    assert linkify(items) == Node(1, Node(2, Node(3, None)))


def test_scale_base() -> None:
    """Scale of a node with only one list should return that one single-linked list scaled by int."""
    test_list: Node = Node(1, None)
    assert scale(test_list, 0) == Node(0, None)


def test_scale_non_empty() -> None:
    """Scale of a non-empty list and int should multiple each Node by int factor."""
    test_list: Node = Node(1, Node(2, Node(3, None)))
    assert scale(test_list, 2) == Node(2, Node(4, Node(6, None)))