import math


def get_data(test=False):
    if not test:
        with open("data.txt", "r") as file:
            data = file.readlines()
    else:
        with open("test_data.txt", "r") as file:
            data = file.readlines()

    data = [line.strip().split(",") for line in data]

    return data


class Spot:
    def __init__(self, x, y, z):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.min_distance: int
        self.nearest_neighbor: Spot = None
        self.used_connections: list = []

    def find_nearest_neighbor(self, space):
        self.min_distance = float("inf")

        for to_spot in space:
            if to_spot is self:
                continue

            distance = math.sqrt(
                (self.x - to_spot.x) ** 2
                + (self.y - to_spot.y) ** 2
                + (self.z - to_spot.z) ** 2
            )

            if self.min_distance > distance and to_spot not in self.used_connections:
                self.min_distance = distance
                self.nearest_neighbor = to_spot


def part_1(data):
    space = []

    for spot in data:
        space.append(Spot(int(spot[0]), int(spot[1]), int(spot[2])))

    # Calculate shortest distace for each spot
    for spot in space:
        spot.find_nearest_neighbor(space)

    circuits = []
    connections_added = 0

    while True:
        if connections_added >= 1000:
            break

        connections_added += 1

        space.sort(key=lambda s: s.min_distance)
        spot: Spot = space[0]

        sx, sy, sz = spot.x, spot.y, spot.z
        nx, ny, nz = (
            spot.nearest_neighbor.x,
            spot.nearest_neighbor.y,
            spot.nearest_neighbor.z,
        )

        s_circuit_id = None
        n_circuit_id = None

        for i, circuit in enumerate(circuits):
            if (sx, sy, sz) in circuit:
                s_circuit_id = i

            if (nx, ny, nz) in circuit:
                n_circuit_id = i

        if s_circuit_id is not None and n_circuit_id is not None:
            if s_circuit_id == n_circuit_id:
                #print([(nx, ny, nz), (sx, sy, sz)], "is already added")
                pass

            else:
                circuits[s_circuit_id].extend(circuits[n_circuit_id])
                circuits.pop(n_circuit_id)

        elif s_circuit_id is not None:
            circuits[s_circuit_id].append((nx, ny, nz))

        elif n_circuit_id is not None:
            circuits[n_circuit_id].append((sx, sy, sz))

        else:
            circuits.append([(sx, sy, sz), (nx, ny, nz)])

        spot.used_connections.append(spot.nearest_neighbor)
        spot.nearest_neighbor.used_connections.append(spot)

        temp = spot.nearest_neighbor
        spot.find_nearest_neighbor(space)
        temp.find_nearest_neighbor(space)

    circuits.sort(key=lambda a: len(a))

    result = len(circuits[-3]) * len(circuits[-2]) * len(circuits[-1])

    print("Part 1:", result)


def part_2(data):
    answer = 0

    space = []

    for spot in data:
        space.append(Spot(int(spot[0]), int(spot[1]), int(spot[2])))

    # Calculate shortest distace for each spot
    for spot in space:
        spot.find_nearest_neighbor(space)

    circuits = []
    connections_added = 0

    while True:
        connections_added += 1

        space.sort(key=lambda s: s.min_distance)
        spot: Spot = space[0]

        sx, sy, sz = spot.x, spot.y, spot.z
        nx, ny, nz = (
            spot.nearest_neighbor.x,
            spot.nearest_neighbor.y,
            spot.nearest_neighbor.z,
        )

        s_circuit_id = None
        n_circuit_id = None

        for i, circuit in enumerate(circuits):
            if (sx, sy, sz) in circuit:
                s_circuit_id = i

            if (nx, ny, nz) in circuit:
                n_circuit_id = i

        if s_circuit_id is not None and n_circuit_id is not None:
            if s_circuit_id == n_circuit_id:
                #print([(nx, ny, nz), (sx, sy, sz)], "is already added")
                pass

            else:
                circuits[s_circuit_id].extend(circuits[n_circuit_id])
                circuits.pop(n_circuit_id)

        elif s_circuit_id is not None:
            circuits[s_circuit_id].append((nx, ny, nz))

        elif n_circuit_id is not None:
            circuits[n_circuit_id].append((sx, sy, sz))

        else:
            circuits.append([(sx, sy, sz), (nx, ny, nz)])

        spot.used_connections.append(spot.nearest_neighbor)
        spot.nearest_neighbor.used_connections.append(spot)

        temp = spot.nearest_neighbor
        spot.find_nearest_neighbor(space)
        temp.find_nearest_neighbor(space)

        if connections_added >= 1000 and len(circuits) == 1 and len(circuits[0]) == len(space):
            answer = sx * nx
            break

    print("Part 2:", answer)


if __name__ == "__main__":
    data = get_data()

    part_1(data)
    part_2(data)