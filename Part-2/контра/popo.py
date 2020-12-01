def list_to_array(linked_list, head):
    a = [head[0]]
    t = head[1]
    for i in range(1, len(linked_list)):
        if t != -1:
            a.append(linked_list[t][0])
            t = linked_list[t][1]
    return a
