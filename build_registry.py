"""
This is an extremely rough way to build a registry state but it works for providing an example state
to prototype against. Rather than properly use `ipfs object` calls, we create a database of the current
registry state using the filesystem and then add the root of the database to ipfs recursively.

In the future, the registry should be built taking into account the current state we're transitioning
from and walking from each leaf to root recursively using `object patch`. The genesis of each node
would be an empty unixfs.
"""

from subprocess import check_output
import os
import errno

def makedirs(path):
  try:
    os.makedirs(path)
  except OSError as exc:
    if exc.errno == errno.EEXIST and os.path.isdir(path):
      pass

#   Number         Ph#              Youtube                                        E-Mail
foundationalnumbers = [
  ("11014655996", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("11014655997", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("11014655998", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("11014655999", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),

  ("11014656"   , "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("11014656001", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("11014656002", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("11014656003", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("11014656004", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("11014656005", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),

  ("16022284486", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),

  ("18004655996", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("18007466396", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),
  ("18004726322", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com"),

  ("18887466396", "1800PHONEWORD", "https://www.youtube.com/watch?v=vnbLVuu744I", "jaycarpenter@1-800-phoneword.com")
]

if __name__ == "__main__":
  root_path = os.path.dirname(os.path.realpath(__file__))+'/db'
  makedirs(root_path)
  os.chdir(root_path)

  for foundationalnumber in foundationalnumbers:
    num = foundationalnumber[0]
    print 'working on ' + num
    path = '/'.join(num) + '/_'
    makedirs(path)
    os.chdir(path)

    names = ["phone", "url", "email"]
    for i in range(3):
      name = names[i]
      value = foundationalnumber[i+1]
      print name, value
      with open(name, 'w') as f:
        f.write(value)

    os.chdir(root_path)

  print(check_output(['ipfs', 'add', '-r', '.']))
