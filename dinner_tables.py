from copy import deepcopy


def gen_tables(N):
    tables = []
    x = 1
    for i in xrange(N):
        tables.append(range(x, x + N))
        x += N
    return tables


def print_tables(tables):
    for table in tables:
        print " ".join(map(str, table))
    print


def print_table_perms(perms):
    for perm in perms:
        print_tables(perm)


def gen_table_perms(tables):
    perms = []

    N = len(tables[0])

    for table in tables:
        assert (len(table) == N)

    # first, add the "columns", who won't be mixed together
    perms.append(map(list, zip(*tables)))

    current_tables = deepcopy(tables)
    next_tables = deepcopy(tables)

    # next, mix the columns with a diagonal shift (mod N)
    for i in xrange(N):
        perms.append(deepcopy(current_tables))

        for j in xrange(N):
            for k in xrange(N):
                next_tables[j][k] = current_tables[(j + k) % N][k]

        (current_tables, next_tables) = (next_tables, current_tables)
    return perms


def verify_table_perms(perms):
    N = len(perms[0][0])

    expect = set((x for x in xrange(1, N * N + 1)))

    v = {}
    for i in xrange(1, N * N + 1):
        v[i] = set((i,))

    for perm in perms:
        for table in perm:
            for seat in table:
                v[seat].update(table)

    for s in v.values():
        assert s == expect, s


tables = gen_tables(6)
perms = gen_table_perms(tables)
verify_table_perms(perms)
print_table_perms(perms)
