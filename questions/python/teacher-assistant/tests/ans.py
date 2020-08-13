def TAs_with_at_least_half_discussions_full(enrollment, attendance):
    TAs = []
    for TA in attendance:
        num_full = len([x for x in attendance[TA] if x >= enrollment[TA]])
        if num_full >= 5:
            TAs.append(TA)
    return TAs