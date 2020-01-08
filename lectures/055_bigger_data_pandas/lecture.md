---
theme: "white"
transition: "fade"
marp: true
highlightTheme: "dracula"
---

# Handing bigger data with Pandas

---

## General guidelines for exploring big data tool:
* If data fits in memory, use Pandas/R/Excel
* If data fits on disk, use a database
* If data is bigger than a disk drive, use Hadoop

---

## Well known maxims in computer science:
*"Premature optimization is the root of all evil"* - Don Knuth

*"Developers themselves highlight the fact that those doing research should exercise caution when using such microbenchmarks"* - Wikipedia article about the benchmark game


*"You don't have to be an engineer to be be a racing driver, but you do have to have Mechanical Sympathy."* Jackie Stewart, racing driver - Quoted by Martin Thompson

---

## A very important insight into understanding perfrmance issues: 
The pyramid of latency varies by orders of magnitude

---

## Latency numbers every programmer should know
(source: https://gist.github.com/hellerbarde/2843375)
(originally by Jeff Dean)

```a
L1 cache reference ......................... 0.5 ns
Branch mispredict ............................ 5 ns
L2 cache reference ........................... 7 ns
Mutex lock/unlock ........................... 25 ns
Main memory reference ...................... 100 ns             
Compress 1K bytes with Zippy ........ 3,000 ns =   3 µs
Send 2K bytes over 1 Gbps network .. 20,000 ns =  20 µs
SSD random read ................... 150,000 ns = 150 µs
Read 1 MB sequentially from memory  250,000 ns = 250 µs
Round trip within same datacenter . 500,000 ns = 0.5 ms
Read 1 MB sequentially from SSD*  1,000,000 ns =   1 ms
Disk seek ...................... 10,000,000 ns =  10 ms
Read 1 MB sequentially from disk 20,000,000 ns =  20 ms
Send packet CA->Holland->CA ... 150,000,000 ns = 150 ms
```

---

#### In human terms (multiply above numbers by a billion)

```a

-L1 cache reference                  0.5 s        
    One heart beat (0.5 s)
-Branch mispredict                   5 s          
    Yawn
-L2 cache reference                  7 s          
    Long yawn
-Mutex lock/unlock                   25 s         
    Making a coffee
-Main memory reference               100 s        
    Brushing your teeth
-Compress 1K bytes with Zippy        50 min       
    One episode of a TV show (including ad breaks)
-Send 2K bytes over 1 Gbps network   5.5 hr       
    From lunch to end of work day
-SSD random read                     1.7 days      
    A normal weekend
-Read 1 MB sequentially from memory  2.9 days      
    A long weekend
-Round trip within same datacenter   5.8 days      
    A medium vacation
-Read 1 MB sequentially from SSD    11.6 days      
    Waiting for almost 2 weeks for a delivery
-Disk seek                           16.5 weeks    
    A semester in university
-Read 1 MB sequentially from disk    7.8 months    
    Almost producing a new human being
-The above 2 together                1 year
-Send packet CA->Netherlands->CA     4.8 years     
    Average time it takes to complete a bachelor's degree
```

---

Luckily _amortization_ saves us. You don't actually look up individual integers from disk each time, you read a chunk of of data on disk and read it into memory. Thereby _amortizing_ the cost of a disk access over many, many reads.

---

Check memory prices

---

## Let's look at a real-world file: Chicago Taxi Data
https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew/

Size of full file...no idea, it is simply too big!

---

### My email to data providers:

Subject: *Can you please, for the love of God, show how big a file is before we download it?*

...
I’m sitting at 30 gigs right now for the taxi data and I have no idea how much more needs to be downloaded.
...

Response:
There is a bit of complexity to this but, in the end, these would have to be feature changes in the software we use. ...

---

### Size of (partially downloaded) file (and subsets):

```a
Compressed:
Size of Taxi_Trips.csv.gz:          14G
Size of taxi_trips_small.csv.gz:     1G
Size of taxi_trips_smaller.csv.gz  154M

Uncompressed:
Size of Taxi_Trips.csv:            ????
Size of taxi_trips_small.csv:      3.4G
Size of taxi_trips_smaller.csv:    456M

Lines in Taxi_Trips.csv.gz:         113,115,259 (100 million)
Lines in taxi_trips_small.csv.gz:    11,311,525 (11 million)
Lines in taxi_trips_smaller.csv.gz:   1,131,152 (1 million)
```

---

### Notebooks

* 050 - Work With Taxi Trips - Get to know the file.ipynb
* 100 - Work With Taxi Trips - memory_map.ipynb
* 110 - Work With Taxi Trips - compression.ipynb
* 150 - Work With Taxi Trips - c_parser.ipynb

* 120 - Work With Taxi Trips - feather format.ipynb
* 130 - Work With Taxi Trips - chunking and tqdm.ipynb
* 160 - Work With Taxi Trips - Chunk to parquet.ipynb
* 160B - Work With Taxi Trips - Read from parquet files.ipynb

* 135 - Work With Taxi Trips - skip columns pre-req.ipynb
* 140 - Work With Taxi Trips - skip columns.ipynb
* 140B - Work With Taxi Trips - skip columns.ipynb

---

## Bonus material: Bash commandline as a super-power
* `ls -ltrhc` to get the size of the file
* `cat` to see the contents of a file
* `zcat` to see the contents of a compressed file
* `head -n<number of lines>` or `tail` to see the first or last few lines
* `wc -l` to count the number of lines in a text file
* `cut -d<delimiter> -f<field1, field2>` to retrieve specific columns
* `tr` or `sed` to replace one character or string with another
