from open_fable import (
    mythos_1b,
    OpenMythos,
)

cfg = mythos_1b()
model = OpenMythos(cfg)

total = sum(p.numel() for p in model.parameters())
print(f"Parameters: {total:,}")
