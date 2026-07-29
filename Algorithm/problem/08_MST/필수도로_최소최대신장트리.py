def solution(n, roads, required):
    
    pair_costs = {}

    for a, b, cost in roads:
        pair = (min(a, b), max(a, b))

        if pair not in pair_costs:
            pair_costs[pair] = []

        pair_costs[pair].append(cost)

    # 중복 필수 조건 제거
    required_pairs = {
        (min(a, b), max(a, b))
        for a, b in required
    }

    def kruskal(reverse=False):
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            parent[root_b] = root_a
            return True

        total_cost = 0
        edge_count = 0

        # 1. 필수 직접 연결 도로부터 선택
        for a, b in required_pairs:
            # 실제로 두 도시를 잇는 도로가 없다면 불가능
            if (a, b) not in pair_costs:
                return None

            if reverse:
                # 최대 신장 트리
                cost = max(pair_costs[(a, b)])
            else:
                # 최소 신장 트리
                cost = min(pair_costs[(a, b)])

            # 필수 도로끼리 이미 사이클이 생기면
            # N-1개짜리 트리를 만들 수 없음
            if not union(a, b):
                return None

            total_cost += cost
            edge_count += 1

        # 2. 나머지 도로를 크루스칼로 선택
        sorted_roads = sorted(
            roads,
            key=lambda x: x[2],
            reverse=reverse
        )

        for a, b, cost in sorted_roads:
            pair = (min(a, b), max(a, b))

            # 필수 쌍은 이미 도로 하나를 선택했으므로 제외
            if pair in required_pairs:
                continue

            if union(a, b):
                total_cost += cost
                edge_count += 1

                if edge_count == n - 1:
                    break

        # 모든 도시를 연결하지 못한 경우
        if edge_count != n - 1:
            return None

        return total_cost

    min_cost = kruskal(reverse=False)
    max_cost = kruskal(reverse=True)

    return [min_cost, max_cost]