
def check(meetings):
    meetings = sorted(meetings)
    st = [0]
    for i in range(1, len(meetings)):
        if meetings[i][0] < st[-1]:
            st.append(meetings[i][1])
        else:
            st.pop()
    return len(st)


