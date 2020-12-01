def list_to_array(linked_list, head):
    a = []
    a.append(head[0])
    t = head[1]

    while t != -1:
        a.append(linked_list[t][0])
        t = linked_list[t][1]
    return a
