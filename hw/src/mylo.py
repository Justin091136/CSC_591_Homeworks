#!/usr/bin/env python3
"""
mylo: recursive bi-clustering via random projections (lo is less. less is more. go lo)
(c) 2023, Tim Menzies, BSD-2

USAGE:
  lua mylo.lua [OPTIONS]

OPTIONS:
  -b --bins   max number of bins              = 16
  -B --Beam   max number of ranges            = 10
  -c --cohen  small effect size               = .35
  -C --Cut    ignore ranges less than C*max   = .1
  -d --d      frist cut                       = 32
  -D --D      second cut                      = 4
  -f --file   csv data file name              = ../data/diabetes.csv
  -F --Far    how far to search for faraway?  = .95
  -h --help   show help                       = false
  -H --Half   #items to use in clustering     = 256
  -p --p      weights for distance            = 2
  -s --seed   random number seed              = 31210
  -S --Support coeffecient on best            = 2
  -t --todo   start up action                 = help]] """

#mylo.py
import argparse
from data import DATA 
from tests import Tests
import Utility

def main():
    parser = argparse.ArgumentParser(description="Perform statistics on a CSV file.")


    parser.add_argument('-c', '--cohen', help="small effect size               = .35")
    parser.add_argument("-f", "--file", help="csv data file name              = '../data/auto93.csv'")
    parser.add_argument("-b", "--bins", type=int, help="max number of bins       = 16")
    parser.add_argument('-B', '--Beam', type=int,help="max number of ranges            = 10")
    parser.add_argument('-s', '--seed', help="random number seed              = 31210")
    parser.add_argument("-t", "--task", help="start up action                 = 'help' ")
    parser.add_argument("-C", "--Cut", help="ignore ranges less than C*max   = .1")
    parser.add_argument("-d", "--d",type=int, help="frist cut                       = 32")
    parser.add_argument("-D", "--D",type=int, help="second cut                       = 4")
    parser.add_argument("-F", "--Far", help="how far to search for faraway?  = .95")
    parser.add_argument("-H", "--Half",type=int, help="#items to use in clustering     = 256")
    parser.add_argument("-p", "--p", help="weights for distance            = 2")
    parser.add_argument("-S", "--Support", help="coeffecient on best            = 2")
    


    args = parser.parse_args()
    

    # Initializing the default values
    if (not args.cohen): args.cohen = Utility.DEFAULT_COHEN_VALUE
    if (not args.file): args.file = "../data/auto93.csv"
    if (not args.bins): args.bins = Utility.DEFAULT_bins_VALUE  # default b=16
    if (not args.Beam): args.Beam = Utility.DEFAULT_Beam_VALUE  # default B=10
    if (not args.seed): args.seed = Utility.DEFAULT_RANDOM_SEED
    if (not args.Cut): args.C = Utility.DEFAULT_CUT_VALUE     #C=0.1
    if (not args.d): args.d = Utility.DEFAULT_d_VALUE       #d=32
    if (not args.D): args.D = Utility.DEFAULT_D_VALUE       #D=4
    if (not args.Far): args.Far = Utility.DEFAULT_F_VALUE       #F =.95
    if (not args.Half): args.Half = Utility.DEFAULT_Half_VALUE    #H=256
    if (not args.p): args.p = Utility.DEFAULT_p_VALUE       #p =2
    if (not args.Support): args.Support = Utility.DEFAULT_S_VALUE      #S= 2

    
    # Load data from CSV file
    data = DATA(args, src=args.file)
    
    # Testing arguments.
    # print(args)
    # Load test cases
    test = Tests(args)

    # Perform the specified task
    if args.task == "dist":
        test.test_dist()
    elif args.task == "far":
        test.test_far()
    elif args.task == "half":
        test.test_half()
    elif args.task == "tree":
        test.test_tree()
    elif args.task == "branch":
        test.test_branch()
    elif args.task == "doubletap":
        test.test_doubletap()
    elif args.task == "all":
        test.run_all_tests()
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
