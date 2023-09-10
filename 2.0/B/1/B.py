n, station_sit, station_exit = map(int, input().split())
if station_sit < station_exit:
    minimal, maximal = station_sit, station_exit
else:
    minimal, maximal = station_exit, station_sit
if maximal - minimal <= n/2:
    print(maximal - minimal - 1)
else:
    print(minimal + n - maximal - 1)