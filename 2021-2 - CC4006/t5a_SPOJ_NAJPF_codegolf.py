import re
N=input;exec('j=[str(_.start()+1)for _ in re.finditer(*N().split()[::-1])];print(f"{len(j)}\\n"+" ".join(j)if j else"Not Found");'*int(N()))