"""Toy app showing how to run the Lilly Medchem Rules from a
python subprocess.
On older hardware,
Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz
and with 4.87M molecules it takes about 9 minutes.
The same command, running outside python, takes about
the same time, so there is little discernable penalty
for rnning inside python using subprocess.

No error checking, in a real app, a failure to launch
error should be handled.
"""

import logging, subprocess, sys

def run_medchem_rules(fname: str):
  cmd = f'/path/to/Lilly_Medchem_Rules.rb {fname}'
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True)
  for line in iter(p.stdout.readline, b''):
    yield line.decode('utf-8')

def pipelined_medchem_rules(fname: str):
  for line in run_medchem_rules(fname):
    print(line.rstrip())


def main(argv):
  """Demonstrate running Lilly Medchem Rules via pipeline"""

  if len(argv) == 1:
    logging.fatal('Must specify smiles file on command line')

  pipelined_medchem_rules(argv[1])

if __name__ == '__main__':
  main(sys.argv)
