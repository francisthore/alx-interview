#!/usr/bin/python3
"""
Module to check if all boxes can be unlocked given a list of boxes and keys.
Each box is sequentially numbered and may contain keys to unlock other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    """
    if not isinstance(boxes, list):
        return False

    unlocked_boxes = [0]

    for box_index in unlocked_boxes:
        for key in boxes[box_index]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)

    return len(unlocked_boxes) == len(boxes)
