import sys
import os 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/public_submodule_example')
import submodule

if __name__ == '__main__':
  print submodule.submodule()
