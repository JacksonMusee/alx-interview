#!/usr/bin/python3
'''
This module is all about opening boxes. Technical interview question.
'''


def canUnlockAll(boxes):
    '''
    Check if all boxes can be opened and return a boolean
    '''
    key_set = set(boxes[0])
    locked_boxes = list(range(1, len(boxes)))
    new_keys = []

    while locked_boxes:
        key_set.update(new_keys)
        new_keys = []
        new_valid_key_found = False

        for key in key_set:
            if key in locked_boxes:
                new_valid_key_found = True
                locked_boxes.remove(key)
                for key in boxes[key]:
                    new_keys.append(key)
        if not new_valid_key_found:
            break

    return len(locked_boxes) == 0
