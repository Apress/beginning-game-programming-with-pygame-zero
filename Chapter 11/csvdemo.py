import csv
import sys

configfile = "csvdemo.csv"

try:
    with open(configfile, 'r') as file:
        csv_reader = csv.reader(file)
        for enemy_details in csv_reader:
            start_time = float(enemy_details[0])
            # value 1 is type
            image = enemy_details[2]
            start_pos = (int(enemy_details[3]),
                int(enemy_details[4]))
            velocity = float(enemy_details[5])
            print ("Start time {}, Image {}, Start Pos {}, Velocity {}".format(start_time, image, start_pos, velocity))
except IOError:
    print ("Error reading configuration file "+configfile)
    # Just end as cannot play without config file
    sys.exit()
except:
    print ("Corrupt configuration file "+configfile)
    sys.exit()