import pstats # this lets us see the profile output

def main():
    p = pstats.Stats('profiling_output')
    p.print_stats()

if __name__ == '__main__':
    main()