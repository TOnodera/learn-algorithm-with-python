def movable_right(matrix, I, J, i, j):
    try:
        if j + 1 < J and (
            matrix[i][j + 1] == matrix[i][j] + 1 or matrix[i][j + 1] == matrix[i][j] - 1
        ):
            return True
    except:
        return False
    return False


def movable_left(matrix, I, J, i, j):
    try:
        if j - 1 >= 0 and (
            matrix[i][j - 1] == matrix[i][j] + 1 or matrix[i][j - 1] == matrix[i][j] - 1
        ):
            return True
    except:
        return False
    return False


def movable_down(matrix, I, J, i, j):
    try:
        if i + 1 < I and (
            matrix[i + 1][j] == matrix[i][j] + 1 or matrix[i + 1][j] == matrix[i][j] - 1
        ):
            return True
    except:
        return False
    return False


def movable_right_down(matrix, I, J, i, j):
    try:
        if (
            i + 1 < I
            and j + 1 < J
            and (
                matrix[i + 1][j + 1] == matrix[i][j] + 1
                or matrix[i + 1][j + 1] == matrix[i][j] - 1
            )
        ):
            return True
    except:
        return False
    return False


def movable_left_down(matrix, I, J, i, j):
    try:
        if (
            i + 1 < I
            and j - 1 >= 0
            and (
                matrix[i + 1][j - 1] == matrix[i][j] + 1
                or matrix[i + 1][j - 1] == matrix[i][j] - 1
            )
        ):
            return True
    except:
        return False
    return False


def is_asc(matrix, I, J, i, j, direction):
    if direction == "right":
        if j + 1 < I:
            return matrix[i][j + 1] - matrix[i][j] > 0
    if direction == "left":
        if j - 1 >= 0:
            return matrix[i][j - 1] - matrix[i][j] > 0
    if direction == "down":
        if i + 1 < I:
            return matrix[i + 1][j] - matrix[i][j] > 0
    if direction == "down_right":
        if i + 1 < I and j + 1 < J:
            return matrix[i + 1][j + 1] - matrix[i][j] > 0
    if direction == "down_left":
        if i + 1 < I and j - 1 >= 0:
            return matrix[i + 1][j - 1] - matrix[i][j] > 0
    return False


N = 4
matrix = [
    [
        1,
        3,
        1,
        4,
    ],
    [1, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 1, 2, 4],
]


results = []
for i, row in enumerate(matrix):
    for j, val in enumerate(row):

        mr_cnt = 0
        mri = i
        mrj = j
        prev_asc = None
        while movable_right(matrix, len(matrix), len(row), mri, mrj):
            asc = is_asc(matrix, len(matrix), len(row), mri, mrj, "right")
            if prev_asc is not None and prev_asc != asc:
                break
            prev_asc = is_asc
            mr_cnt += 1
            if mrj + 1 < N:
                mrj += 1
            else:
                break

        ml_cnt = 0
        mli = i
        mlj = j
        prev_asc = None
        while movable_left(matrix, len(matrix), len(row), mli, mlj):
            asc = is_asc(matrix, len(matrix), len(row), mli, mlj, "left")
            if prev_asc is not None and prev_asc != asc:
                break
            prev_asc = is_asc
            ml_cnt += 1
            if mlj - 1 < N:
                mlj -= 1
            else:
                break

        md_cnt = 0
        mdi = i
        mdj = j
        prev_asc = None
        while movable_down(matrix, len(matrix), len(row), mdi, mdj):
            asc = is_asc(matrix, len(matrix), len(row), mdi, mdj, "down")
            if prev_asc is not None and prev_asc != asc:
                break
            prev_asc = is_asc
            md_cnt += 1
            if mdi + 1 < N:
                mdi += 1
            else:
                break

        mdr_cnt = 0
        mdri = i
        mdrj = j
        prev_asc = None
        while movable_right_down(matrix, len(matrix), len(row), mdri, mdrj):
            asc = is_asc(matrix, len(matrix), len(row), mdri, mdrj, "down_right")
            if prev_asc is not None and prev_asc != asc:
                break
            prev_asc = asc
            mdr_cnt += 1
            if mdrj + 1 < N and mdri + 1 < N:
                mdri += 1
                mdrj += 1
            else:
                break

        mdl_cnt = 0
        mdli = i
        mdlj = j
        prev_asc = None
        while movable_left_down(matrix, len(matrix), len(row), mdli, mdlj):
            asc = is_asc(matrix, len(matrix), len(row), mdri, mdrj, "down_left")
            if prev_asc is not None and prev_asc != asc:
                break
            prev_asc = is_asc
            mdl_cnt += 1
            if mdlj - 1 >= 0 and mdli + 1 < N:
                mdli += 1
                mdlj -= 1
            else:
                break

        result = max(mr_cnt, ml_cnt, md_cnt, mdr_cnt, mdl_cnt) + 1
        results.append(result)


print(max(results))
