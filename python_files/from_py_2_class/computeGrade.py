def compute_total_grade(exercises, assignments, exam):
    ''' (list of 7 floats, list of 3 floats, float) -> float

    Compute the total grade earned for LTP: The fundamentals.

    >>> compute_total_grade([0, 18, 16, 14, 14, 13, 12], [41, 24, 37], 14)
    100.0
    >>> compute_total_grade([15, 18, 16, 13, 13, 13, 12], [41, 24, 17], 11.75)
    87.45736808236809
    '''
    E_totals = [15, 18, 16, 14, 14, 13, 12]
    A_totals    = [41, 24, 37]
    A_weights = [10, 15, 15]
    # Exercises: turn individual scores into weighted scores.
    for i in range(0, 7):
        exercises[i] /= E_totals[i]
        exercises[i] *= (35 / 6) # (6 out of 7 rule individual weight)
    # Pop the lowest scored exercise (6 out of 7 rule)
    exercises.remove(min(exercises))
    # Assignments: turn scores into weighted scores.
    for i in range(0, 3):
        assignments[i] /= A_totals[i]
        assignments[i] *= A_weights[i]
    # Final exam:
    exam /= 14
    exam *= 25
    total = sum(exercises) + sum(assignments) + exam
    return total
