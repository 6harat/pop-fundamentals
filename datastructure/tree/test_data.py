from dataclasses import dataclass


@dataclass
class Node:
    data: int
    left: 'Node'
    right: 'Node'

tree1 = Node(
    10, 
    Node(
        15,
        Node(
            3,
            Node(5, None, None),
            None
        ),
        Node(6, None, None)
    ),
    Node(
        30,
        None,
        Node(
            2,
            Node(9, None, None),
            Node(8, None, None)
        )
    )
)

tree2 = Node(
    10,
    Node(
        0,
        Node(-1, None, None),
        Node(21, None, None)
    ),
    Node(
        25,
        Node(16, None, None),
        Node(32, None, None)
    )
)

bst1 = Node(
    10, 
    Node(
        -5,
        Node(-10, None, None),
        Node(
            0, 
            None, 
            Node(5, None, None))
    ),
    Node(
        30,
        None,
        Node(36, None, None)
    )
)

bst2 = Node(
    10, None,
    Node(
        15, None,
        Node(
            16, None,
            Node(18, None, None)
        )
    )
)

bst3 = Node(
    10,
    Node(
        -10,
        None,
        Node(
            8,
            Node(6, None, None),
            Node(9, None, None)
        )
    ),
    Node(
        30,
        Node(
            25,
            None,
            Node(28, None, None)
        ),
        Node(
            60,
            None,
            Node(78, None, None)
        )
    )
)

