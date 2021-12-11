# Exploring the command line

Your computer has a file system, organized in a heirarchy.

### Windows file system looks something like this:

```
c:\
    ...
    Program Files
    Program Files (x86)
    Windows
    Users
        Public
        shahbaz
            Desktop
            Documents
            Pictures
            .gitconfig
            ...
```

### Mac users' file system looks something like this

```
/
    ...
    tmp/
    Applications/
    Library/
    Users/
        shahbaz/
            Applications/
            Desktop/
            Downloads/
            ...
```

### Linux users' file system looks something like this

```
/
    ...
    tmp/
    bin/
    opt/
    home/
        shahbaz/
```
http://cheatsheetworld.com/programming/unix-linux-cheat-sheet/

## Linux/Mac vs Windows
This lecture will concentrate on the Linux command line[1]. Although Windows is more popular among computer users, Linux and Linux like operating systems are much more common on the server.

Mac command line is very similar to the Linux command line; however, there are subtle differences which are beyond the scope of this lecture.


[1] Specifically `bash`

## Log on to a remote server

1. Please download the following:

Termius https://www.termius.com/

cyberduck https://cyberduck.io/

2. Use "Termius" to log on to a remote server 

IP address: 159.89.155.202

User: `<username>`@uchicago.edu

Password: `<username>123`

#### Basic utilities

Use the `up` arrow to recall the last executed command

Use the `tab` key to auto-complete a command

Use `nano` to edit files (most poeple use `vi`, but that is a more advanced editor)

## Navigation

#### `pwd`

When a user is operating thier computer via a terminal, they are always "in a directory/folder." To find out where you are in the filesystem, you can use the `pwd` command. This command "prints" the "working directory."

#### `ls`

The `ls` command "lists" the contents of the current directory. The contents may include files as well as sub-directories. The `ls` command is often used with various parameters. Here are some examples:

`ls` list contents of current directory (and no other information)

`ls -l` lists contents of current directory using the long format (displays access, owner time and size information)

```
total 960
drwxr-xr-x  5 schaudhary schaudhary   4096 Feb  3 02:57 .
drwxr-xr-x 32 root       root         4096 Feb  2 20:25 ..
-rw-r--r--  1 schaudhary schaudhary    220 Apr  4  2018 .bash_logout
-rw-r--r--  1 schaudhary schaudhary   3771 Apr  4  2018 .bashrc
drwx------  2 schaudhary schaudhary   4096 Feb  2 19:16 .cache
-rw-r--r--  1 schaudhary schaudhary      0 Feb  2 18:35 .cloud-locale-test.skip
drwx------  3 schaudhary schaudhary   4096 Feb  2 19:16 .gnupg
drwxrwxr-x  3 schaudhary schaudhary   4096 Feb  2 22:03 .local
-rw-r--r--  1 schaudhary schaudhary    807 Apr  4  2018 .profile
-rw-r--r--  1 schaudhary schaudhary      0 Feb  2 20:02 .sudo_as_admin_successful
-rw-------  1 schaudhary schaudhary   8018 Feb  3 02:57 .viminfo
-rw-rw-r--  1 schaudhary schaudhary    165 Feb  3 02:56 .wget-hsts
-rw-rw-r--  1 schaudhary schaudhary 921936 Feb  3 02:57 game-of-thrones-deaths-data.csv
-rw-rw-r--  1 schaudhary schaudhary   1673 Feb  2 20:24 newusers.txt
-rw-rw-r--  1 schaudhary schaudhary    231 Feb  2 19:20 students.txt
-rw-rw-r--  1 schaudhary schaudhary     12 Feb  3 01:23 test.txt
```

When the first letter is `d`, the listing refers to a directory. All others are files.

`-rwxrwxrwx` refers to permissions. A file or directory can have three levels of permissions: "user", "group" and "global." A file can be be readable `r` or not, writable `w` or not, executable `x` or not.

`ls -t` sorts files by "modification time"

`ls -S` sorts files by size

`ls a` displays hidden files (usually the ones which start with a '.')

These flags are often combined, such as `ls -alS`, which will dipslay all files, including hidden ones, in long format, sorted by size.

**Exercise** Take a look at the reference documentation for `ls` by issuing his command: `ls -h`

**Exercise** Take a look at the manual page for `ls` by issuing the following command `man ls`

#### `cd <directory>`
```
/home/shahbaz/
    assignments/
        assignment1
        ...
```
If a user wants to "change directories," they use the `cd` comamnd. This command requires the name of the destination directory or the path. 

For example, if you have a directory called "assignments" in your current directory, `cd assignments` will put you in the "assignments" directory. 

If the "assignments" directory had directory under it, called "assignment1," this command will get you from your original directory to "assignment1," which is two levels deep: `cd assignments/assignment1`. 

Such concatenation of directories or files is called a "path." Such paths can be absolute `/home/shahbaz/assignments/assignment1/homework.txt` or relative `assignments/assignment1/homework.txt`.

There are three special paths:`.`, `..` and `~`.

`cd .` means change into the current directory. In other words, it does nothing. There are times when you need to refer to the "current" directory.

`cd ..` will put you in the parent directory. For example, if you start out in your home directory `/home/shahbaz`, `cd ..` will put you in `/home`.

No matter where you are in the file system, `cd ~` will put you in the home directory, in my case: `/home/shahbaz`.

#### `find`
The `find assignment1.ipynb` command will search the current directory, and all sub-directories to find the file "assignment1.ipynb." If you just wanted to see everything in your current directory and sub-directories, you would just do `find .`.

**Exercise** Take a look at the reference documentation for `cd` by issuing his command: `cd -h`

**Exercise** Take a look at the manual page for `cd` by issuing the following command `cd ls`

## File exploration

#### `head` / `tail`
Given a file, you can view the first few lines by using `head <filename>`. If you wish to be explicit about how many lines you want to view, do so using `head -n10 <filename>`, which will display 10 lines. Simlarly, the `tail` command shows the end of the file.

#### `more` / `less`
While `head` just displays the first few lines, `more <filename>` displays the whole file, one page at a time. When a page is displayed, the computer waits for you to press the `space` key to display more pages. You can quite the `more` program by pressing the `q` key.

Some systems prefer the `less` command, which works the same as `more`, but allows users to scroll back (instead of just forward).

#### `cat`
The `cat <filename>` command will show the whole file, start to finish. Be careful with this command! If your file is 1 gigabyte in size, this command will display the whole thing on your terminal. If the file is on a remote server, you are essentially downloading the whole thing to your computer (then discarding it as soon as the text scrolls).

#### `grep` 
Given a large file, you can search for specific text using `grep <pattern> <file>`. 

For example, given a file containing all characters from the Game of Thrones and their kill stats, you would search for Arya using `grep Arya got_kills.csv`. 

If you wanted to search for everything EXCEPT Arya, the command `grep -v Arya got_kills.csv` will get you what you want.

`grep -i arya got_kills.csv` will ignore case and return all lines containing Arya, arya, aRya, etc.

#### `wc -l`
The `wc -l` command will count the number of lines in the file. The `wc` command, by itself, counts the number of characters in a file. However, it is most often used with the `-l` parameter since counting lines is a much more common usecase than counting characters.

#### `sort`
A file can be sorted using the `sort` command. By default, `sort` sorts alphanumerically, starting at the beginning of each line.

`sort -n` sorts numerically.

Given a file `test.txt`:
```
123
1008
112
```

`sort test.txt` will return
```
1008
112
123
```

`sort -n test.txt` will correctly return
```
112
123
1008
```

#### `uniq` and `uniq -c`
The `uniq` command will remove redundant lines.

Given a file test2.txt:
```
12
12
13
12
```

`uniq test2.txt` will return:
```
12
13
12
```

`uniq -c test2.txt` will also count how often lines occur:
```
    2   12
    1   13
    1   12
```

It often makes sense to combine `uniq` with `sort`, such as `cat somefile.txt|sort|uniq`. This removes all redundant lines. (see the definition of the `|` operator next).

## The `|` (pipe) character <= Suprisingly important!
Perhaps the most important and powerful feature of command lines (including on windows) is the `|` (pipe) character. This allows you to chain commands together.

`cat got_killings.csv| grep -i arya| head` will start to "display" the whole file, but limit it to only the lines containing "arya" (ignoring case) and display only the first 10 lines.

## Redirection operators: `>` and `>>`
Say you want to create a copy of an existing file, but only keep the first 100 lines (perhaps to test on a smaller set of data). The simples way to do so is: `head -n 100 got_killings.csv > got_killings_small.csv`. If there was an existing file called "got_killings_small.csv", this command will overwrite it. 

Use `>>` if, instead of overwriting, you want to append to the file. For example:
```
cat got_killings.csv >> got_killings_big.csv
cat got_killings.csv >> got_killings_big.csv
```
This will create file, twice as big as the original.

## File transformation

#### sed
The command `sed "s/Arya/NoName/g" got_killings.csv` will change all instances of "Arya" to "NoName" and display to the user. It will _not_ change the original file.

Note that `s/orignal/final/g` is a regular expression. This is a very important, but slightly advanced topic. We will cover this separately.

#### cut
If your file is structured, such as a "csv" file (where fields are separated by commas), you can use the `cut -d<delimiter> -f<column num>` command.

For example, say character names are in column 2 in the file got_killings.csv, mentioned earlier. `cat got_killings.csv | cut -d',' -f2` will extract just the column with character names and ignore all others.


# TODO
## Basic commands

#### whoami
#### ssh
#### df / du 
#### ~ / . / ..
#### wget / curl / scp
#### nano

### Navigation


### File transformation
#### tr
#### sed
#### awk

### File creation/deletion/relocation
#### touch
#### cp
#### mv
#### rm

### Dir creation/deletion
#### rm -rf
#### mv -r
#### cp -r
#### mkdir

#### ctrl-c <= kill whatever I'm running

# Tools
Terminus https://www.termius.com/

cyberduck https://cyberduck.io/