def toh(source: str, dest: str, aux: str, rings: int) -> None:
    if rings == 1:
        print(f"Move disk {rings} from {source} to {dest}")

    else:
        toh(source, aux, dest, rings - 1)
        print(f"Move disk {rings} from {source} to {dest}")
        toh(aux, dest, source, rings - 1)


toh("A", "C", "B", int(input()))
