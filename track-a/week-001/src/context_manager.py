class ManagedFile:
    def __init__(self, path): self.path = path
    def __enter__(self): self.f = open(self.path, "a+"); return self.f
    def __exit__(self, exc_type, exc, tb): self.f.close()

with ManagedFile("w1.txt") as f:
    f.write("week1\n")
print("closed?", f.closed)

